# Liquid-glass overlay templates v2 (Anton baked in, amped motion). 1080x1920, 30fps, PIL + numpy.
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
            a2 = 2 * math.pi * t * sp * 1.6 + ph
            cx = .5 + .42 * math.sin(a2 + k) * (1 + li * .1); cy = .5 + .44 * math.cos(a2 * .8 + k * 1.7)
            a = np.exp(-(((xx - cx) * .56) ** 2 + (yy - cy) ** 2) / (r * r * .18))[..., None] * al
            img = img * (1 - a) + np.array(col) * a
    c = Image.fromarray(img.clip(0, 255).astype("uint8")).resize((W, H), Image.BICUBIC).convert("RGBA")
    d = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dd = ImageDraw.Draw(d); sp = 60
    for gy in range(0, H // sp + 1):
        for gx in range(0, W // sp + 1):
            x, y = gx * sp, gy * sp; ph = math.hypot(x - 540, y - 960) / 140 - t * 2 * math.pi * 1.6
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

# ---- G1 glass_card_title: panel slams down from far above with deep overshoot + motion blur, title pops with scale punch.
def g1(i, N, text, f):
    def st(t):
        u = spring(t / .26); out = ease_io((t - .86) / .14)
        return 900 - (1 - u) * 1100 - out * 160, clamp(t * 12) * (1 - out), u
    t = i / (N - 1); f = fit(text, f, 760); cy, al, u = st(t); cyp = st((i - 1) / (N - 1))[0]
    c = bg(t); w = min(960, tw(text, f) + 190)
    glass(c, (W / 2 - w / 2, cy - 170, W / 2 + w / 2, cy + 170), r=80, al=al)
    txt(c, text, f, W / 2, cy, al=clamp((t - .1) / .1) * al, sc=1 + .35 * max(0, back((t - .1) / .2, 3.5) - 1) * 0 + .0 + (0.25 * (1 - back((t - .08) / .22, 3.2)) if t > .08 else .25))
    dblur(c, (W / 2 - w / 2, cy - 170, W / 2 + w / 2, cy + 170), 0, (cy - cyp) * 1.2); return c

# ---- G2 glass_stack: panels whip in from alternating sides with overshoot + blur, accent dot pulses.
def g2(i, N, text, f):
    t = i / (N - 1); items = text.split("|"); out = ease_io((t - .9) / .1); c = bg(t); sm = font(None, 130)
    for k, s in enumerate(items):
        def pos(tt):
            u = spring((tt - .04 - k * .2) / .24); side = -1 if k % 2 == 0 else 1
            return 540 + side * (1 - u) * 1300 + side * out * 1400
        tt = t - .04 - k * .2
        if tt <= 0: continue
        x = pos(t); dx = x - pos((i - 1) / (N - 1)); cy = 700 + k * 280; al = clamp(tt * 14)
        glass(c, (x - 430, cy - 115, x + 430, cy + 115), r=60, al=al)
        pulse = 1 + .35 * math.exp(-tt * 9) * math.cos(tt * 40); r = 26 * pulse
        ImageDraw.Draw(c).ellipse([x - 340 - r, cy - r, x - 340 + r, cy + r], fill=ACC)
        txt(c, s.upper(), sm, x + 20, cy, al=al); dblur(c, (x - 430, cy - 115, x + 430, cy + 115), dx * 1.1, 0)
    return c

# ---- G3 glass_chips: pills fire in from alternating directions with big overshoot; wrapped rows.
def g3(i, N, text, f):
    t = i / (N - 1); c = bg(t); out = ease_io((t - .9) / .1); ws = text.split(); sm = font(None, 112)
    rows, cur, curw = [], [], 0
    for w in ws:
        cw = tw(w.upper(), sm) + 120
        if curw + cw > 980 and cur: rows.append(cur); cur, curw = [], 0
        cur.append((w.upper(), cw)); curw += cw + 24
    rows.append(cur); y0 = 900 - (len(rows) - 1) * 110; n = 0
    for ri, row in enumerate(rows):
        tot = sum(cw for _, cw in row) + 24 * (len(row) - 1); x = W / 2 - tot / 2
        for w, cw in row:
            u = (t - .04 - n * .075) / .2; ang = n * 1.9; n += 1
            if u > 0:
                s = back(u, 3.2); ox = math.cos(ang) * (1 - spring(u)) * 600; oy = math.sin(ang) * (1 - spring(u)) * 600
                al = clamp(u * 5) * (1 - out); hh = 78 * s; cx = x + cw / 2 + ox; cy = y0 + ri * 190 + oy
                glass(c, (cx - cw / 2 * s, cy - hh, cx + cw / 2 * s, cy + hh), r=int(hh), blur=20, al=al)
                txt(c, w, sm, cx, cy, al=al, sc=s); dblur(c, (cx - cw / 2, cy - hh, cx + cw / 2, cy + hh), -ox * .12, -oy * .12)
            x += cw + 24
    return c

# ---- G4 glass_lower_third: panel whips in from left with overshoot, accent bar shoots up, subtitle types in.
def g4(i, N, text, f):
    t = i / (N - 1); c = bg(t); a, b = (text.split("|") + [""])[:2]
    def px(tt): return -1100 + 1100 * spring(tt / .24) - 1100 * ease_io((tt - .82) / .18)
    x = px(t); dx = x - px((i - 1) / (N - 1)); big = fit(a, font(None, 170), 640); sm = font(None, 76)
    glass(c, (x + 50, 1330, x + 1030, 1650), r=64)
    ImageDraw.Draw(c).rounded_rectangle([x + 95, 1375, x + 111, 1375 + 230 * ease_out((t - .1) / .15)], 8, fill=ACC)
    txt(c, a, big, x + 140 + tw(a, big) / 2 + 30, 1470); n = int(len(b) * clamp((t - .22) / .25))
    if n: txt(c, b[:n], sm, x + 140 + tw(b[:n], sm) / 2 + 30, 1575, col=(24, 32, 58, 190))
    dblur(c, (x + 50, 1330, x + 1030, 1650), dx * 1.2, 0); return c

# ---- G5 glass_stat: fast count-up (ease-out), snap tick + flash on landing, panel pulses, ring fills with glow.
def g5(i, N, text, f):
    t = i / (N - 1); c = bg(t); out = ease_io((t - .9) / .1); target = int(text); tl = .42
    ep = ease_out(t / tl); v = int(round(target * ep)); landed = max(0, t - tl)
    s = back(t / .2, 3.0) * (1 + .09 * math.exp(-landed * 14) * math.cos(landed * 55)); al = clamp(t * 12) * (1 - out)
    h = 430 * s; glass(c, (W / 2 - h, 900 - h, W / 2 + h, 900 + h), r=130, al=al)
    d = ImageDraw.Draw(c); r = 340 * s; ext = 360 * ep * target / 100
    d.ellipse([W / 2 - r, 900 - r, W / 2 + r, 900 + r], outline=(255, 255, 255, int(160 * al)), width=24)
    if ext > 1:
        glow = Image.new("RGBA", c.size, (0, 0, 0, 0)); ImageDraw.Draw(glow).arc([W / 2 - r, 900 - r, W / 2 + r, 900 + r], -90, -90 + min(ext, 359.9), fill=ACC[:3] + (170,), width=46)
        c.alpha_composite(glow.filter(ImageFilter.GaussianBlur(18))); d.arc([W / 2 - r, 900 - r, W / 2 + r, 900 + r], -90, -90 + min(ext, 359.9), fill=ACC, width=24)
    txt(c, str(v), font(None, 420), W / 2, 900, al=al, sc=1 + .1 * math.exp(-landed * 12) * math.cos(landed * 50) if landed else 1)
    if landed > 0: flash(c, .5 * math.exp(-landed * 22))
    return shake(c, 18 * math.exp(-landed * 12) if landed else 0, t)

# ---- G6 glass_vs: panels slam together from opposite sides, collide (flash + camera shake), bounce apart, VS badge punches in.
def g6(i, N, text, f):
    t = i / (N - 1); out = ease_io((t - .9) / .1); a, b = (text.split("|") + [""])[:2]; sm = font(None, 190); tc = .26
    def off(tt):  # 0 final, big = far; touches centre gap at tc then bounces out
        if tt < tc: return 1500 * (1 - ease_io(tt / tc) ** .8) + 150 * 0 - 0
        k = tt - tc; return -170 * math.exp(-k * 9) * math.cos(k * 30) * 1.0
    o = off(t); op = off((i - 1) / (N - 1)); al = 1 - out; c = bg(t)
    ya, yb = 560 + (o if o < 0 else 0) * -1 * 0, 1340
    ay = 640 - o * .0; 
    # vertical slam: top panel comes from left, bottom from right, both aimed at the centre line (y=950) then settle to 700 / 1200
    ty = 700 + min(o, 0) * -.9 + (150 if t < tc else 0) * 0
    ax = 540 - max(o, 0) * 1.0 + (o if o < 0 else 0) * .3; bx = 540 + max(o, 0) * 1.0 - (o if o < 0 else 0) * .3
    ay = 760 + (o if o < 0 else 0) * .55; by = 1140 - (o if o < 0 else 0) * .55
    glass(c, (ax - 450, ay - 150, ax + 450, ay + 150), r=76, al=al); txt(c, a.upper(), sm, ax, ay, al=al)
    glass(c, (bx - 450, by - 150, bx + 450, by + 150), r=76, al=al); txt(c, b.upper(), sm, bx, by, col=ACC, al=al)
    d = (o - op)
    dblur(c, (ax - 450, ay - 150, ax + 450, ay + 150), -d * 1.0, 0); dblur(c, (bx - 450, by - 150, bx + 450, by + 150), d * 1.0, 0)
    k = t - tc
    if k > 0:
        s = back(k / .14, 4.0); r = 120 * s; d2 = ImageDraw.Draw(c)
        ring = Image.new("RGBA", c.size, (0, 0, 0, 0)); rr = 120 + 700 * ease_out(k / .3)
        ImageDraw.Draw(ring).ellipse([540 - rr, 950 - rr, 540 + rr, 950 + rr], outline=(255, 255, 255, int(200 * (1 - clamp(k / .3)) * al)), width=10); c.alpha_composite(ring)
        d2.ellipse([540 - r, 950 - r, 540 + r, 950 + r], fill=(255, 255, 255, int(240 * al)), outline=ACC, width=8); txt(c, "VS", font(None, 120), 540, 950, al=al, sc=max(.05, s))
        flash(c, .6 * math.exp(-k * 20))
    return shake(c, 34 * math.exp(-max(0, k) * 10) if k > 0 else 0, t)

T = {"g1": (g1, 75), "g2": (g2, 90), "g3": (g3, 75), "g4": (g4, 75), "g5": (g5, 75), "g6": (g6, 75)}
if __name__ == "__main__":
    name, text, out = sys.argv[1:4]; fp = sys.argv[4] if len(sys.argv) > 4 else None
    fn, N = T[name]; f = font(fp, 190); os.makedirs(out, exist_ok=True)
    for i in range(N): fn(i, N, text, f).convert("RGB").save(f"{out}/f{i:04d}.png")
