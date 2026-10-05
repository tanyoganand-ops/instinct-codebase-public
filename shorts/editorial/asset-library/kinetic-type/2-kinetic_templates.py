# DRAFT - not rendered or tested. Usage: python3 kinetic_templates.py <template> "TEXT" <out_dir> [font.ttf]
# Then: ffmpeg -framerate 30 -i out/f%04d.png -c:v libvpx-vp9 -pix_fmt yuva420p -crf 22 -b:v 0 out.webm
import sys, os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H, FPS = 1080, 1920, 30
INK = (24, 32, 58, 255)          # dark ink, readable on light bg
ACC = (110, 150, 245, 255)       # blue accent used across the library
CLAY = (236, 170, 138, 255)

def clamp(x): return min(max(x, 0.0), 1.0)
def ease_out(t): t = clamp(t); return 1 - (1 - t) ** 3
def ease_io(t): t = clamp(t); return t * t * (3 - 2 * t)
def back(t, c=1.2): t = clamp(t); return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2
def spring(t, k=7.0): t = clamp(t); return 1 - math.exp(-5 * t) * math.cos(k * t)

def font(path, size): return ImageFont.truetype(path or "Anton-Regular.ttf", size)

def glyph(ch, f, col=INK, pad=20):
    b = f.getbbox(ch); w, h = b[2] - b[0] + 2 * pad, b[3] - b[1] + 2 * pad
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((pad - b[0], pad - b[1]), ch, font=f, fill=col)
    return im

def text_img(s, f, col=INK, pad=20):
    b = f.getbbox(s); im = Image.new("RGBA", (b[2] - b[0] + 2 * pad, b[3] - b[1] + 2 * pad), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((pad - b[0], pad - b[1]), s, font=f, fill=col); return im

def place(canvas, im, cx, cy, sc=1.0, al=1.0, rot=0.0, sx=1.0):
    if sc != 1 or sx != 1:
        im = im.resize((max(2, int(im.width * sc * sx)), max(2, int(im.height * sc))), Image.LANCZOS)
    if rot: im = im.rotate(rot, resample=Image.BICUBIC, expand=True)
    if al < 1:
        a = im.split()[3].point(lambda v: int(v * al)); im.putalpha(a)
    canvas.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))

# ---- T1 word_stack_drop: words drop in one per line, spring settle. Use: hook / list beats.
def t1(i, N, text, f):
    t = i / (N - 1); c = Image.new("RGBA", (W, H)); words = text.split()
    for k, w in enumerate(words):
        u = (t - 0.04 - k * 0.12) / 0.3
        if u <= 0: continue
        y = 760 + k * 170 - (1 - spring(u)) * 420
        out = ease_io((t - 0.85) / 0.15)
        place(c, text_img(w, f), W / 2, y, al=min(1, u * 4) * (1 - out))
    return c

# ---- T2 letter_cascade: per-letter rise with 1-frame stagger offset; cheap, readable. Use: titles, chapter names.
def t2(i, N, text, f):
    t = i / (N - 1); c = Image.new("RGBA", (W, H)); gl = [glyph(ch, f) for ch in text]
    tot = sum(g.width * 0.78 for g in gl); x = W / 2 - tot / 2
    for k, g in enumerate(gl):
        u = (t - k * 0.025) / 0.25; adv = g.width * 0.78
        if u > 0:
            y = 900 + (1 - back(u)) * 120; place(c, g, x + adv / 2, y, al=clamp(u * 3) * (1 - ease_io((t - 0.88) / 0.12)))
        x += adv
    return c

# ---- T3 highlight_pop: one keyword scales up on a marker band; others dim. Use: emphasis on key claim word.
def t3(i, N, text, f, key=0):
    t = i / (N - 1); c = Image.new("RGBA", (W, H)); words = text.split(); d = ImageDraw.Draw(c)
    imgs = [text_img(w, f) for w in words]; tot = sum(m.width for m in imgs) + 30 * (len(imgs) - 1); x = W / 2 - tot / 2
    for k, m in enumerate(imgs):
        cx = x + m.width / 2; hot = (k == key); u = ease_out((t - 0.15) / 0.2) if hot else 0
        if hot and u > 0:
            band = Image.new("RGBA", (int((m.width + 30) * u), m.height - 10), (255, 214, 90, 150)); place(c, band, cx, 900)
        place(c, m, cx, 900, sc=1 + 0.18 * back((t - 0.15) / 0.25) * (1 if hot else 0), al=1 if hot else 1 - 0.45 * u0(t))
        x += m.width + 30
    return c
def u0(t): return ease_io((t - 0.15) / 0.2)

# ---- T4 swipe_line_reveal: each line wipes in via a mask moving L->R with a soft edge. Use: sentence captions, calm pacing.
def t4(i, N, text, f):
    t = i / (N - 1); c = Image.new("RGBA", (W, H)); lines = text.split("|")
    for k, s in enumerate(lines):
        m = text_img(s, f); u = ease_out((t - k * 0.2) / 0.3)
        if u <= 0: continue
        mask = Image.new("L", m.size, 0); ImageDraw.Draw(mask).rectangle([0, 0, int(m.width * u), m.height], fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(10)); a = Image.fromarray(__import__("numpy").minimum(__import__("numpy").array(m.split()[3]), __import__("numpy").array(mask)))
        m.putalpha(a); place(c, m, W / 2, 800 + k * 170, al=1 - ease_io((t - 0.88) / 0.12))
    return c

# ---- T5 counter_roll: number counts 0->N with ease-out and a final scale tick. Use: stats, scores, "9/10".
def t5(i, N, text, f):
    t = i / (N - 1); c = Image.new("RGBA", (W, H)); target = int(text)
    v = int(round(target * ease_out(t / 0.7))); sc = 1 + (0.12 * math.exp(-(t - 0.7) * 10) * math.cos((t - 0.7) * 20) if t > 0.7 else 0)
    place(c, text_img(str(v), f), W / 2, 900, sc=sc, al=clamp(t * 8) * (1 - ease_io((t - 0.9) / 0.1)))
    return c

# ---- T6 slide_swap: old phrase slides out left as new slides in from right, gentle blur-free. Use: A -> B comparisons (vs. beats).
def t6(i, N, text, f):
    t = i / (N - 1); c = Image.new("RGBA", (W, H)); a, b = text.split("|")[:2]
    u = ease_io((t - 0.4) / 0.3)
    place(c, text_img(a, f), W / 2 - u * 1100, 900, al=1 - u)
    place(c, text_img(b, f, ACC), W / 2 + (1 - u) * 1100, 900, al=u)
    return c

# ---- T7 underline_type: typewriter reveal (per-char, with caret) then wavy underline draws under it. Use: quotes, search-bar style beats.
def t7(i, N, text, f):
    t = i / (N - 1); c = Image.new("RGBA", (W, H)); n = int(len(text) * clamp(t / 0.5))
    place(c, text_img(text[:max(n, 1)] + ("|" if int(t * 12) % 2 == 0 and t < 0.6 else ""), f), W / 2, 900, al=1 - ease_io((t - 0.9) / 0.1))
    if t > 0.5:
        u = ease_out((t - 0.5) / 0.25); wdt = f.getbbox(text)[2]; d = ImageDraw.Draw(c)
        pts = [(W / 2 - wdt / 2 + wdt * u * k / 40, 1010 + 7 * math.sin(k / 40 * 6.9)) for k in range(41)]
        d.line(pts, fill=ACC, width=14, joint="curve")
    return c

# ---- T8 scale_punch: single word slams in oversized, snaps down with overshoot, brief shake. Use: hook word, "WAIT", "STOP".
def t8(i, N, text, f):
    t = i / (N - 1); c = Image.new("RGBA", (W, H)); u = clamp(t / 0.18)
    sc = 2.4 - 1.4 * back(u, 1.6); shake = 10 * math.exp(-(t - 0.18) * 14) * math.sin(t * 90) if t > 0.18 else 0
    place(c, text_img(text, f, INK), W / 2 + shake, 900, sc=sc, al=clamp(t * 12) * (1 - ease_io((t - 0.88) / 0.12)))
    return c

T = {"t1": (t1, 75), "t2": (t2, 75), "t3": (t3, 60), "t4": (t4, 75), "t5": (t5, 75), "t6": (t6, 60), "t7": (t7, 90), "t8": (t8, 45)}
if __name__ == "__main__":
    name, text, out = sys.argv[1:4]; fp = sys.argv[4] if len(sys.argv) > 4 else None
    fn, N = T[name]; f = font(fp, 150 if name != "t1" else 190); os.makedirs(out, exist_ok=True)
    for i in range(N): fn(i, N, text, f).save(f"{out}/f{i:04d}.png")
