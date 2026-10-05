# Liquid-glass overlay templates v3 (soft Apple-style motion; font = Anton until P's pick). 1080x1920, 30fps, PIL + numpy.
# Usage: python3 glass_templates.py <g1..g6> "TEXT" <out_dir> [font.ttf]   (default font: Anton-Regular.ttf next to this file)
# Encode: ffmpeg -framerate 30 -i out/f%04d.png -c:v libx264 -pix_fmt yuv420p -crf 18 out.mp4
# Text formats: g1 "TITLE"; g2 "a|b|c"; g3 "w1 w2 w3"; g4 "TITLE|subtitle"; g5 "87"; g6 "A|B".
import sys, os, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H, FPS = 1080, 1920, 30
INK = (24, 32, 58, 255); ACC = (110, 150, 245, 255); CLAY = (236, 170, 138, 255)
HERE = os.path.dirname(os.path.abspath(__file__)); ANTON = os.path.join(HERE, "Anton-Regular.ttf")
def clamp(x): return min(max(x, 0.0), 1.0)
def ease_out(t): t = clamp(t); return 1 - (1 - t) ** 4
def ease_io(t): t = clamp(t); return t * t * (3 - 2 * t)
def back(t, c=2.6): t = clamp(t); return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2
def spring(t, k=9.0): t = clamp(t); return 1 - math.exp(-4.2 * t) * math.cos(k * t)
def font(path, size): return ImageFont.truetype(path or ANTON, size)   # no stand-in fonts: missing Anton raises

# ---- background: 3 parallax blob layers (slow big / mid / fast small) + rippling dot-wave. Blobs at 1/8 res, upscaled.
LAYERS = [  # (speed, radius, alpha, [(colour, phase)])
    (.25, .34, .60, [((150, 190, 255), 0), ((255, 205, 175), 2.1), ((175, 235, 210), 4.0)]),
    (.55, .20, .62, [((120, 170, 255), 1.0), ((255, 190, 160), 3.3), ((150, 225, 200), 5.2)]),
    (1.0, .10, .55, [((100, 150, 250), .4), ((255, 175, 140), 2.7), ((255, 255, 255), 4.4), ((130, 215, 235), 5.9)])]
def bg(t):
    w, h = W // 8, H // 8; yy, xx = np.mgrid[0:h, 0:w]; xx = xx / w; yy = yy / h
    img = np.ones((h, w, 3)) * np.array([246, 248, 252.0])
    for li, (sp, r, al, bl) in enumerate(LAYERS):
        for k, (col, ph) in enumerate(bl):
            a2 = 2 * math.pi * t * sp * .8 + ph
            cx = .5 + .42 * math.sin(a2 + k) * (1 + li * .1); cy = .5 + .44 * math.cos(a2 * .8 + k * 1.7)
            a = np.exp(-(((xx - cx) * .56) ** 2 + (yy - cy) ** 2) / (r * r * .18))[..., None] * al
            img = img * (1 - a) + np.array(col) * a
    c = Image.fromarray(img.clip(0, 255).astype("uint8")).resize((W, H), Image.BICUBIC).convert("RGBA")
    d = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dd = ImageDraw.Draw(d); sp = 60
    for gy in range(0, H // sp + 1):
        for gx in range(0, W // sp + 1):
            x, y = gx * sp, gy * sp; ph = math.hypot(x - 540, y - 960) / 140 - t * 2 * math.pi * .6
            r = 3.2 + 2.6 * math.sin(ph); yo = 5 * math.sin(ph)
            dd.ellipse([x - r, y + yo - r, x + r, y + yo + r], fill=(70, 100, 170, 70))
    c.alpha_composite(d); return c

def dblur(c, box, dx, dy, n=7):
    """directional motion blur of region `box` along (dx,dy) pixels/frame, strength ~ speed."""
    L = math.hypot(dx, dy)
    if L < 6: return
    x0, y0, x1, y1 = [int(v) for v in box]; p = 90
    x0, y0, x1, y1 = max(0, x0 - p), max(0, y0 - p), min(W, x1 + p), min(H, y1 + p)
    if x1 <= x0 or y1 <= y0: return
    P = int(L) + 4; base = np.pad(np.array(c.crop((x0, y0, x1, y1)), dtype=float), ((P, P), (P, P), (0, 0)), mode="edge"); hh, ww = y1 - y0, x1 - x0; acc = np.zeros((hh, ww, 4))
    for k in range(n):
        f = (k / (n - 1) - .5) * .9; ox, oy = int(dx * f), int(dy * f)
        acc += base[P - oy:P - oy + hh, P - ox:P - ox + ww]
    c.paste(Image.fromarray((acc / n).astype("uint8")), (x0, y0))

def glass(canvas, box, r=60, tint=.38, blur=28, al=1.0, mv=(0, 0)):
    x0, y0, x1, y1 = [int(v) for v in box]
    if x1 - x0 < 8 or y1 - y0 < 8 or al <= 0: return
    sh = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x0, y0 + 30, x1, y1 + 30], r, fill=(43, 45, 66, int(70 * al)))
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(36)))
    reg = canvas.crop((x0, y0, x1, y1)).filter(ImageFilter.GaussianBlur(blur)).convert("RGBA")
    mask = Image.new("L", reg.size, 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, reg.width - 1, reg.height - 1], r, fill=int(255 * al))
    reg.alpha_composite(Image.new("RGBA", reg.size, (255, 255, 255, int(255 * tint))))
    grad = Image.linear_gradient("L").resize(reg.size).point(lambda v: int((255 - v) * .4 * al))
    hi = Image.new("RGBA", reg.size, (255, 255, 255, 255)); hi.putalpha(grad); reg.alpha_composite(hi)
    rim = Image.new("RGBA", reg.size, (0, 0, 0, 0)); ImageDraw.Draw(rim).rounded_rectangle([0, 0, reg.width - 1, reg.height - 1], r, outline=(255, 255, 255, int(220 * al)), width=3)
    reg.alpha_composite(rim); canvas.paste(reg, (x0, y0), mask)

def txt(canvas, s, f, cx, cy, col=INK, al=1.0, sc=1.0):
    b = f.getbbox(s); im = Image.new("RGBA", (b[2] - b[0] + 40, b[3] - b[1] + 40), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((20 - b[0], 20 - b[1]), s, font=f, fill=col)
    if sc != 1: im = im.resize((max(2, int(im.width * sc)), max(2, int(im.height * sc))), Image.LANCZOS)
    if al < 1: im.putalpha(im.split()[3].point(lambda v: int(v * al)))
    canvas.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))
def tw(s, f): b = f.getbbox(s); return b[2] - b[0]
def fit(s, f, maxw):
    while tw(s, f) > maxw and f.size > 30: f = ImageFont.truetype(f.path, f.size - 8)
    return f
def shake(c, amp, t):
    if amp < .5: return c
    ox, oy = int(amp * math.sin(t * 190)), int(amp * .7 * math.cos(t * 230))
    arr = np.pad(np.array(c), ((60, 60), (60, 60), (0, 0)), mode="edge"); return Image.fromarray(arr[60 - oy:60 - oy + H, 60 - ox:60 - ox + W])
def flash(c, a):
    if a > .01: c.alpha_composite(Image.new("RGBA", c.size, (255, 255, 255, int(255 * clamp(a)))))

class OD:  # alpha-correct drawing: composites each shape instead of overwriting pixels (fixes white blobs at alpha 0)
    def __init__(s, c): s.c = c
    def _do(s, m, *a, **k):
        o = Image.new("RGBA", s.c.size, (0, 0, 0, 0)); getattr(ImageDraw.Draw(o), m)(*a, **k); s.c.alpha_composite(o)
    def ellipse(s, *a, **k): s._do("ellipse", *a, **k)
    def arc(s, *a, **k): s._do("arc", *a, **k)
    def rounded_rectangle(s, *a, **k): s._do("rounded_rectangle", *a, **k)

# ---- Motion language (v3, Apple liquid-glass feel): soft decelerating ease, no overshoot, no impact, no shake, no flash.
# Every element: fade + gentle glide (60-120px) + slight scale 0.94->1, staggered; exits mirror entrances, slightly faster.
def enter(t, st, dur): return ease_out((t - st) / dur)
def exit_(t, st=.86, dur=.14): return ease_io((t - st) / dur)
def glide(t, st, dur, dist=90): e = enter(t, st, dur); return e, (1 - e) * dist

def g1(i, N, text, f):
    t = i / (N - 1); c = bg(t); f = fit(text, f, 760); e, dy = glide(t, .04, .34, 110); x = exit_(t); al = e * (1 - x)
    cy = 900 + dy - x * 50; sc = .94 + .06 * e; w = min(960, tw(text, f) + 190) * sc
    glass(c, (W / 2 - w / 2, cy - 170 * sc, W / 2 + w / 2, cy + 170 * sc), r=80, al=al)
    txt(c, text, f, W / 2, cy, al=enter(t, .12, .3) * (1 - x), sc=sc); return c

def g2(i, N, text, f):
    t = i / (N - 1); c = bg(t); items = text.split("|"); x = exit_(t, .88, .12); sm = font(None, 130)
    for k, s in enumerate(items):
        e, dy = glide(t, .05 + k * .13, .3, 80)
        if e <= 0: continue
        al = e * (1 - x); cy = 700 + k * 280 + dy - x * 40; sc = .95 + .05 * e
        glass(c, (540 - 430 * sc, cy - 115 * sc, 540 + 430 * sc, cy + 115 * sc), r=60, al=al)
        OD(c).ellipse([200 - 24, cy - 24, 200 + 24, cy + 24], fill=ACC[:3] + (int(255 * al),))
        txt(c, s.upper(), sm, 560, cy, al=enter(t, .1 + k * .13, .28) * (1 - x))
    return c

def g3(i, N, text, f):
    t = i / (N - 1); c = bg(t); x = exit_(t, .88, .12); ws = text.split(); sm = font(None, 112); rows, cur, curw = [], [], 0
    for w in ws:
        cw = tw(w.upper(), sm) + 120
        if curw + cw > 980 and cur: rows.append(cur); cur, curw = [], 0
        cur.append((w.upper(), cw)); curw += cw + 24
    rows.append(cur); y0 = 900 - (len(rows) - 1) * 110; n = 0
    for ri, row in enumerate(rows):
        tot = sum(cw for _, cw in row) + 24 * (len(row) - 1); px = W / 2 - tot / 2
        for w, cw in row:
            e, dy = glide(t, .05 + n * .08, .28, 60); n += 1
            if e > 0:
                al = e * (1 - x); sc = .92 + .08 * e; hh = 78 * sc; cx = px + cw / 2; cy = y0 + ri * 190 + dy
                glass(c, (cx - cw / 2 * sc, cy - hh, cx + cw / 2 * sc, cy + hh), r=int(hh), blur=20, al=al); txt(c, w, sm, cx, cy, al=al, sc=sc)
            px += cw + 24
    return c

def g4(i, N, text, f):
    t = i / (N - 1); c = bg(t); a, b = (text.split("|") + [""])[:2]; e = enter(t, .03, .32); x = exit_(t, .84, .16)
    ox = -420 * (1 - e) - 420 * x; al = e * (1 - x); big = fit(a, font(None, 170), 640); sm = font(None, 76)
    glass(c, (50 + ox, 1330, 1030 + ox, 1650), r=64, al=al)
    OD(c).rounded_rectangle([95 + ox, 1375, 111 + ox, 1375 + 230 * enter(t, .12, .3)], 8, fill=ACC[:3] + (int(255 * al),))
    txt(c, a, big, 140 + ox + tw(a, big) / 2 + 30, 1470, al=enter(t, .12, .3) * (1 - x)); txt(c, b, sm, 140 + ox + tw(b, sm) / 2 + 30, 1575, col=(24, 32, 58, 190), al=enter(t, .22, .3) * (1 - x)); return c

def g5(i, N, text, f):
    t = i / (N - 1); c = bg(t); x = exit_(t, .9, .1); target = int(text); e, dy = glide(t, .03, .3, 70); al = e * (1 - x); sc = .94 + .06 * e
    ep = ease_out((t - .08) / .62); v = int(round(target * ep)); h = 430 * sc; cy = 900 + dy
    glass(c, (W / 2 - h, cy - h, W / 2 + h, cy + h), r=130, al=al); d = OD(c); r = 340 * sc; ext = 360 * ep * target / 100
    d.ellipse([W / 2 - r, cy - r, W / 2 + r, cy + r], outline=(255, 255, 255, int(160 * al)), width=24)
    if ext > 1:
        glow = Image.new("RGBA", c.size, (0, 0, 0, 0)); ImageDraw.Draw(glow).arc([W / 2 - r, cy - r, W / 2 + r, cy + r], -90, -90 + min(ext, 359.9), fill=ACC[:3] + (int(120 * al),), width=40)
        c.alpha_composite(glow.filter(ImageFilter.GaussianBlur(16))); d.arc([W / 2 - r, cy - r, W / 2 + r, cy + r], -90, -90 + min(ext, 359.9), fill=ACC[:3] + (int(255 * al),), width=24)
    txt(c, str(v), font(None, 420), W / 2, cy, al=al); return c

def g6(i, N, text, f):
    t = i / (N - 1); c = bg(t); x = exit_(t, .9, .1); a, b = (text.split("|") + [""])[:2]; sm = font(None, 190)
    e1, d1 = glide(t, .03, .36, 0); e2 = enter(t, .12, .36); e3 = enter(t, .5, .3); sc3 = .85 + .15 * e3
    for (lab, e, side, ay, col) in ((a, e1, -1, 760, INK), (b, e2, 1, 1140, ACC)):
        ox = side * 520 * (1 - e) + side * 420 * x; al = e * (1 - x)
        glass(c, (540 + ox - 450, ay - 150, 540 + ox + 450, ay + 150), r=76, al=al); txt(c, lab.upper(), sm, 540 + ox, ay, col=col, al=al)
    al = e3 * (1 - x); r = 110 * sc3; d = OD(c)
    d.ellipse([540 - r, 950 - r, 540 + r, 950 + r], fill=(255, 255, 255, int(235 * al)), outline=ACC[:3] + (int(255 * al),), width=6); txt(c, "VS", font(None, 120), 540, 950, al=al, sc=sc3)
    return c

T = {"g1": (g1, 75), "g2": (g2, 90), "g3": (g3, 75), "g4": (g4, 75), "g5": (g5, 75), "g6": (g6, 75)}
if __name__ == "__main__":
    name, text, out = sys.argv[1:4]; fp = sys.argv[4] if len(sys.argv) > 4 else None
    fn, N = T[name]; f = font(fp, 190); os.makedirs(out, exist_ok=True)
    for i in range(N): fn(i, N, text, f).convert("RGB").save(f"{out}/f{i:04d}.png")
