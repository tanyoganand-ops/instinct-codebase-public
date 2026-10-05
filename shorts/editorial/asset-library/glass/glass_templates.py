# Liquid-glass overlay templates, same style as kinetic_templates.py (1080x1920, 30fps, PIL).
# Usage: python3 glass_templates.py <g1..g6> "TEXT" <out_dir> [font.ttf]
# Frames are opaque RGB (light moving-gradient bg + frosted panels). Encode:
#   ffmpeg -framerate 30 -i out/f%04d.png -c:v libx264 -pix_fmt yuv420p -crf 18 out.mp4
# Text formats: g1 "TITLE"; g2 "a|b|c"; g3 "w1 w2 w3"; g4 "TITLE|subtitle"; g5 "87" (number); g6 "A|B".
import sys, os, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H, FPS = 1080, 1920, 30
INK = (24, 32, 58, 255); ACC = (110, 150, 245, 255); CLAY = (236, 170, 138, 255)
def clamp(x): return min(max(x, 0.0), 1.0)
def ease_out(t): t = clamp(t); return 1 - (1 - t) ** 3
def ease_io(t): t = clamp(t); return t * t * (3 - 2 * t)
def back(t, c=1.2): t = clamp(t); return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2
def spring(t, k=7.0): t = clamp(t); return 1 - math.exp(-5 * t) * math.cos(k * t)
def font(path, size):
    for p in (path, "Anton-Regular.ttf", "DejaVuSans-Bold.ttf"):
        try: return ImageFont.truetype(p, size)
        except Exception: pass
    return ImageFont.load_default()

# ---- moving gradient background: 4 soft blobs drifting on a pale base (blue, peach, mint, lilac-free). Renders at 1/8 res then upscales.
BLOBS = [((140, 180, 255), .0, .3), ((255, 200, 170), 1.7, .25), ((170, 235, 205), 3.1, .28), ((150, 205, 250), 4.4, .22)]
def bg(t):
    w, h = W // 8, H // 8; yy, xx = np.mgrid[0:h, 0:w]; xx = xx / w; yy = yy / h
    img = np.ones((h, w, 3)) * np.array([246, 248, 252.0])
    for k, (col, ph, r) in enumerate(BLOBS):
        cx = .5 + .38 * math.sin(2 * math.pi * t * .5 + ph + k); cy = .5 + .40 * math.cos(2 * math.pi * t * .5 + ph * 1.3)
        a = np.exp(-(((xx - cx) * .56) ** 2 + (yy - cy) ** 2) / (r * r * .18))[..., None] * .75
        img = img * (1 - a) + np.array(col) * a
    return Image.fromarray(img.clip(0, 255).astype("uint8")).resize((W, H), Image.BICUBIC).convert("RGBA")

# ---- glass panel: blur what is behind, white tint, top-light gradient, 2px rim, soft shadow.
def glass(canvas, box, r=60, tint=.38, blur=28, al=1.0):
    x0, y0, x1, y1 = [int(v) for v in box]
    if x1 - x0 < 8 or y1 - y0 < 8 or al <= 0: return
    pad = 70; sh = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x0, y0 + 26, x1, y1 + 26], r, fill=(43, 45, 66, int(60 * al)))
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(34)))
    reg = canvas.crop((x0, y0, x1, y1)).filter(ImageFilter.GaussianBlur(blur)).convert("RGBA")
    mask = Image.new("L", reg.size, 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, reg.width - 1, reg.height - 1], r, fill=int(255 * al))
    wh = Image.new("RGBA", reg.size, (255, 255, 255, int(255 * tint)))
    grad = Image.linear_gradient("L").resize(reg.size).point(lambda v: int((255 - v) * .35 * al))
    wh2 = Image.new("RGBA", reg.size, (255, 255, 255, 255)); wh2.putalpha(grad)
    reg.alpha_composite(wh); reg.alpha_composite(wh2)
    rim = Image.new("RGBA", reg.size, (0, 0, 0, 0)); ImageDraw.Draw(rim).rounded_rectangle([0, 0, reg.width - 1, reg.height - 1], r, outline=(255, 255, 255, int(210 * al)), width=3)
    reg.alpha_composite(rim); canvas.paste(reg, (x0, y0), mask)

def txt(canvas, s, f, cx, cy, col=INK, al=1.0, sc=1.0):
    b = f.getbbox(s); im = Image.new("RGBA", (b[2] - b[0] + 40, b[3] - b[1] + 40), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((20 - b[0], 20 - b[1]), s, font=f, fill=col)
    if sc != 1: im = im.resize((max(2, int(im.width * sc)), max(2, int(im.height * sc))), Image.LANCZOS)
    if al < 1: im.putalpha(im.split()[3].point(lambda v: int(v * al)))
    canvas.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))
    return im.width, im.height
def tw(s, f): b = f.getbbox(s); return b[2] - b[0]

# ---- G1 glass_card_title: one wide panel drops in with spring, title fades up inside. Use: chapter / hook title.
def g1(i, N, text, f):
    t = i / (N - 1); c = bg(t); out = ease_io((t - .86) / .14); u = spring(t / .3)
    while tw(text, f) > 780 and f.size > 40: f = font(getattr(f, 'path', None), f.size - 10)
    w = min(940, tw(text, f) + 160); cy = 900 - (1 - u) * 500 - out * 80; al = clamp(t * 10) * (1 - out)
    glass(c, (W / 2 - w / 2, cy - 150, W / 2 + w / 2, cy + 150), al=al)
    txt(c, text, f, W / 2, cy, al=clamp((t - .12) / .15) * (1 - out)); return c

# ---- G2 glass_stack: "a|b|c" panels drop in one by one, staggered; each has an accent dot. Use: lists / three-point beats.
def g2(i, N, text, f):
    t = i / (N - 1); c = bg(t); out = ease_io((t - .88) / .12); items = text.split("|")
    for k, s in enumerate(items):
        u = spring((t - .04 - k * .2) / .28)
        if (t - .04 - k * .2) <= 0: continue
        cy = 700 + k * 270 - (1 - u) * 420; al = clamp((t - k * .2) * 10) * (1 - out)
        glass(c, (110, cy - 105, 970, cy + 105), r=52, al=al)
        d = ImageDraw.Draw(c); d.ellipse([170, cy - 24, 218, cy + 24], fill=ACC[:3] + (int(255 * al),))
        sm = font(None, 96); txt(c, s, sm, 600, cy, al=al)
    return c

# ---- G3 glass_chips: words become pill chips that pop in with overshoot in a wrapped row layout. Use: tags, tool names.
def g3(i, N, text, f):
    t = i / (N - 1); c = bg(t); out = ease_io((t - .88) / .12); ws = text.split(); sm = font(None, 90)
    rows, cur, curw = [], [], 0
    for w in ws:
        cw = tw(w, sm) + 110
        if curw + cw > 960 and cur: rows.append(cur); cur, curw = [], 0
        cur.append((w, cw)); curw += cw + 24
    rows.append(cur); y0 = 900 - (len(rows) - 1) * 100
    n = 0
    for ri, row in enumerate(rows):
        tot = sum(cw for _, cw in row) + 24 * (len(row) - 1); x = W / 2 - tot / 2
        for w, cw in row:
            u = (t - .05 - n * .09) / .22; n += 1
            if u > 0:
                s = back(u, 1.9); al = clamp(u * 4) * (1 - out); hh = 80 * s; cx = x + cw / 2; cy = y0 + ri * 200
                glass(c, (cx - cw / 2 * s, cy - hh, cx + cw / 2 * s, cy + hh), r=int(hh), blur=20, al=al)
                txt(c, w, sm, cx, cy, al=al, sc=s)
            x += cw + 24
    return c

# ---- G4 glass_lower_third: "TITLE|subtitle" panel slides in from left near the bottom, accent bar grows, slides out. Use: names, sources.
def g4(i, N, text, f):
    t = i / (N - 1); c = bg(t); a, b = (text.split("|") + [""])[:2]
    u = ease_out(t / .25); out = ease_io((t - .82) / .18); x = -900 + 900 * u - 900 * out
    glass(c, (x + 60, 1360, x + 1020, 1620), r=56)
    ImageDraw.Draw(c).rounded_rectangle([x + 100, 1400, x + 100 + 14, 1400 + 180 * ease_out((t - .12) / .25)], 7, fill=ACC)
    big = font(None, 110); sm = font(None, 62)
    txt(c, a, big, x + 140 + tw(a, big) / 2 + 20, 1455); txt(c, b, sm, x + 140 + tw(b, sm) / 2 + 20, 1550, col=(24, 32, 58, 170)); return c

# ---- G5 glass_stat: big counter inside a round-cornered square panel with a ring that fills. Use: scores, percentages.
def g5(i, N, text, f):
    t = i / (N - 1); c = bg(t); out = ease_io((t - .88) / .12); target = int(text)
    s = back(t / .22, 1.4); al = clamp(t * 10) * (1 - out); h = 420 * s
    glass(c, (W / 2 - h, 900 - h, W / 2 + h, 900 + h), r=120, al=al)
    d = ImageDraw.Draw(c); r = 330 * s; ext = 360 * ease_out(t / .7) * target / 100
    d.ellipse([W / 2 - r, 900 - r, W / 2 + r, 900 + r], outline=(255, 255, 255, int(150 * al)), width=22)
    if ext > 1: d.arc([W / 2 - r, 900 - r, W / 2 + r, 900 + r], -90, -90 + min(ext, 359.9), fill=ACC, width=22)
    v = int(round(target * ease_out(t / .7))); txt(c, str(v), font(None, 300), W / 2, 900, al=al); return c

# ---- G6 glass_vs: "A|B" two panels slide in from opposite sides, round VS badge pops between. Use: comparisons.
def g6(i, N, text, f):
    t = i / (N - 1); c = bg(t); out = ease_io((t - .88) / .12); a, b = (text.split("|") + [""])[:2]
    u = ease_out(t / .3); al = 1 - out; sm = font(None, 130)
    glass(c, (90 - (1 - u) * 1000, 520, 990 - (1 - u) * 1000, 800), r=70, al=al)
    glass(c, (90 + (1 - u) * 1000, 1100, 990 + (1 - u) * 1000, 1380), r=70, al=al)
    txt(c, a, sm, 540 - (1 - u) * 1000, 660, al=al); txt(c, b, sm, 540 + (1 - u) * 1000, 1240, col=ACC, al=al)
    k = back((t - .3) / .2, 2.0)
    if k > 0:
        r = 95 * k; d = ImageDraw.Draw(c); d.ellipse([540 - r, 950 - r, 540 + r, 950 + r], fill=(255, 255, 255, int(235 * al)), outline=ACC, width=6)
        txt(c, "VS", font(None, 90), 540, 950, al=al, sc=k)
    return c

T = {"g1": (g1, 75), "g2": (g2, 90), "g3": (g3, 75), "g4": (g4, 75), "g5": (g5, 75), "g6": (g6, 75)}
if __name__ == "__main__":
    name, text, out = sys.argv[1:4]; fp = sys.argv[4] if len(sys.argv) > 4 else None
    fn, N = T[name]; f = font(fp, 150); os.makedirs(out, exist_ok=True)
    for i in range(N): fn(i, N, text, f).convert("RGB").save(f"{out}/f{i:04d}.png")
