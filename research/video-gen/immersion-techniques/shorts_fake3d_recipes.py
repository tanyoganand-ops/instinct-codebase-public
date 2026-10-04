"""Stylized 2D fake-3D helpers for Pillow + NumPy.

Dependencies: Pillow and NumPy. All public functions operate on RGB/RGBA Pillow
images. Work at reduced resolution where possible and upscale once at the end.
These are compositing approximations, not general-purpose 3D rendering.
"""
from __future__ import annotations
import math
import numpy as np
from PIL import Image, ImageFilter, ImageOps, ImageEnhance


def _rgb_array(im: Image.Image) -> np.ndarray:
    return np.asarray(im.convert("RGB"), dtype=np.float32) / 255.0


def _mask_array(mask: Image.Image, size: tuple[int, int]) -> np.ndarray:
    return np.asarray(mask.convert("L").resize(size, Image.Resampling.BILINEAR), dtype=np.float32)[..., None] / 255.0


def planar_reflection(scene: Image.Image, horizon_y: int, *, height: int | None = None,
                      opacity: float = .38, blur: float = 1.2,
                      tint=(0.78, 0.88, 0.94), ripple_px: float = 1.5,
                      ripple_period: float = 36.0) -> Image.Image:
    """Fake a horizontal reflective plane below horizon_y.

    Builds a vertically flipped copy of the scene above the horizon, squashes it
    into the reflection region and applies subtle row-wise ripple displacement.
    Composite the returned RGBA image over the original scene using alpha.
    Pass a mask or clip externally if the reflective surface is not full-width.
    """
    w, h = scene.size
    horizon_y = int(np.clip(horizon_y, 1, h - 1))
    height = h - horizon_y if height is None else max(1, min(int(height), h-horizon_y))
    source = scene.crop((0, 0, w, horizon_y)).transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    source = source.resize((w, height), Image.Resampling.BICUBIC)
    rgb = _rgb_array(source)
    # Smooth periodic horizontal displacement, indexed by destination row.
    yy = np.arange(height, dtype=np.float32)
    xx = np.arange(w, dtype=np.float32)
    shifted = np.empty_like(rgb)
    for y in range(height):
        dx = ripple_px * math.sin((y / max(ripple_period, 1e-3)) * 2 * math.pi)
        xsrc = np.clip(np.rint(xx - dx).astype(np.int32), 0, w - 1)
        shifted[y] = rgb[y, xsrc]
    col = np.asarray(tint, dtype=np.float32).reshape(1, 1, 3)
    shifted = np.clip(shifted * col, 0, 1)
    # Reflection fades with distance from the contact line.
    fade = np.linspace(opacity, 0.0, height, dtype=np.float32)[:, None]
    alpha = np.broadcast_to(fade, (height, w)).copy()
    layer = Image.fromarray(np.uint8(np.clip(shifted * 255, 0, 255)), "RGB")
    if blur > 0:
        layer = layer.filter(ImageFilter.GaussianBlur(blur))
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    a = np.zeros((h, w), dtype=np.uint8)
    a[horizon_y:horizon_y+height] = np.uint8(np.clip(alpha * 255, 0, 255))
    layer.putalpha(Image.fromarray(a[horizon_y:horizon_y+height], "L"))
    out.paste(layer, (0, horizon_y))
    return out


def fake_subsurface(image: Image.Image, mask: Image.Image, *, tint=(1.0, .36, .22),
                    radii=(2.0, 7.0, 18.0), weights=(.55, .30, .15),
                    strength=.45) -> Image.Image:
    """Masked, multi-scale diffusion tint: useful for ears, wax, fruit, clay edges.

    Blur premultiplied color and mask separately, divide to avoid dark halos,
    then mix blurred tint into only the supplied object's mask.
    """
    base = _rgb_array(image)
    m = _mask_array(mask, image.size)
    tintv = np.asarray(tint, dtype=np.float32).reshape(1, 1, 3)
    premul = Image.fromarray(np.uint8(np.clip(base * m * 255, 0, 255)), "RGB")
    mask_l = Image.fromarray(np.uint8(np.clip(m[..., 0] * 255, 0, 255)), "L")
    accum = np.zeros_like(base)
    norm = 0.0
    for radius, weight in zip(radii, weights):
        if weight <= 0: continue
        color_blur = _rgb_array(premul.filter(ImageFilter.GaussianBlur(float(radius))))
        mask_blur = np.asarray(mask_l.filter(ImageFilter.GaussianBlur(float(radius))), dtype=np.float32)[..., None] / 255.0
        diffuse = color_blur / np.maximum(mask_blur, 1e-4)
        accum += np.clip(diffuse, 0, 1) * float(weight)
        norm += float(weight)
    diffuse = np.clip(accum / max(norm, 1e-6) * tintv, 0, 1)
    result = np.clip(base * (1 - m * strength) + diffuse * (m * strength), 0, 1)
    return Image.fromarray(np.uint8(result * 255), "RGB")


def motion_blur_accumulate(render_at, frame: int, *, samples=5, shutter=.6) -> Image.Image:
    """Render temporal samples across the shutter interval and weighted-average.

    render_at(float_frame) must return an RGB/RGBA Pillow image and be a pure,
    deterministic scene render. shutter=1 spans one frame interval. For 450
    output frames this multiplies scene-render work by `samples`; use only for
    fast hero motion, or pre-render/cache the samples. Samples use triangular
    weights to reduce harsh exposure-window edges.
    """
    samples = max(1, int(samples))
    offsets = np.linspace(-.5, .5, samples, dtype=np.float32) * float(shutter)
    weights = 1.0 - np.abs(np.linspace(-1, 1, samples, dtype=np.float32))
    if samples == 1: weights[:] = 1.0
    weights /= weights.sum()
    total = None
    for offset, weight in zip(offsets, weights):
        arr = _rgb_array(render_at(frame + float(offset)))
        total = arr * weight if total is None else total + arr * weight
    return Image.fromarray(np.uint8(np.clip(total * 255, 0, 255)), "RGB")


def apply_baked_light(base: Image.Image, lightmap: Image.Image, *, strength=1.0,
                      ambient_floor=.22) -> Image.Image:
    """Apply a precomputed grayscale/RGB illumination map to a static layer.

    Bake contact gradients, broad key/fill pools, and static AO once. Keep
    moving-object shadows and highlights in separate dynamic layers.
    """
    color = _rgb_array(base)
    light = _rgb_array(lightmap.resize(base.size, Image.Resampling.BILINEAR))
    light = np.maximum(light, float(ambient_floor))
    lit = color * (1 - strength + strength * light)
    return Image.fromarray(np.uint8(np.clip(lit * 255, 0, 255)), "RGB")


def warp_quad(image: Image.Image, out_size: tuple[int, int], quad_xy: tuple[tuple[float,float], ...],
              resample=Image.Resampling.BICUBIC) -> Image.Image:
    """Map the full source rectangle into a destination quadrilateral.

    quad order: top-left, top-right, bottom-right, bottom-left in output pixels.
    Pillow's PERSPECTIVE transform wants output-to-input coefficients, so solve
    the inverse homography. For deforming grids, subdivide into quads/triangles
    or use Canvas triangle clipping; cache the mapping if the pose repeats.
    """
    w, h = image.size
    src = [(0,0), (w,0), (w,h), (0,h)]
    A, b = [], []
    for (x, y), (u, v) in zip(quad_xy, src):
        A += [[x,y,1,0,0,0,-u*x,-u*y], [0,0,0,x,y,1,-v*x,-v*y]]
        b += [u,v]
    coeff = np.linalg.solve(np.asarray(A, dtype=np.float64), np.asarray(b, dtype=np.float64))
    return image.transform(out_size, Image.Transform.PERSPECTIVE,
                           tuple(float(x) for x in coeff), resample=resample)


def clay_lighting(size: tuple[int, int], *, seed=7, base=(190, 133, 116),
                  light_dir=(-.45, -.65, .61), macro=0.055, micro=0.018,
                  gloss=0.12) -> Image.Image:
    """Procedural clay-like color and relief for a 2D card or matte illustration.

    Creates deterministic multi-scale value noise, derives a fake normal from
    its height gradient, then shades diffuse + broad low-intensity specular.
    Fingerprint arcs are best added as a separate sparse height/noise layer.
    """
    w, h = size
    rng = np.random.default_rng(seed)
    # Coarse random lattice -> smooth macro lumps; second lattice -> fine grain.
    def smooth_noise(cell):
        gh, gw = max(2, math.ceil(h/cell)+1), max(2, math.ceil(w/cell)+1)
        grid = rng.random((gh, gw), dtype=np.float32)
        im = Image.fromarray(np.uint8(grid * 255), "L").resize((w,h), Image.Resampling.BICUBIC)
        return np.asarray(im, dtype=np.float32) / 255.0
    n0, n1 = smooth_noise(62), smooth_noise(9)
    heightfield = (n0 - .5) * macro + (n1 - .5) * micro
    gy, gx = np.gradient(heightfield)
    nx, ny, nz = -gx * 14, -gy * 14, np.ones_like(gx)
    nlen = np.sqrt(nx*nx + ny*ny + nz*nz)
    nx, ny, nz = nx/nlen, ny/nlen, nz/nlen
    lx, ly, lz = np.asarray(light_dir, dtype=np.float32)
    llen = math.sqrt(lx*lx + ly*ly + lz*lz); lx,ly,lz=lx/llen,ly/llen,lz/llen
    ndotl = np.clip(nx*lx + ny*ly + nz*lz, 0, 1)
    # Broad rough-clay lobe rather than sharp plastic specular.
    spec = np.maximum(0, ndotl) ** 18 * gloss
    grain = np.clip(.94 + (n1-.5)*.10 + (n0-.5)*.12, .78, 1.12)
    shade = np.clip((.48 + .66*ndotl + spec) * grain, .25, 1.3)[...,None]
    rgb = np.clip(np.asarray(base, dtype=np.float32)[None,None,:] / 255 * shade, 0, 1)
    return Image.fromarray(np.uint8(rgb*255), "RGB")


if __name__ == "__main__":
    # Tiny smoke test: execute `python shorts_fake3d_recipes.py`.
    canvas = Image.new("RGB", (96, 160), (125, 160, 190))
    mask = Image.new("L", canvas.size, 0)
    from PIL import ImageDraw
    ImageDraw.Draw(mask).ellipse((24, 24, 72, 92), fill=255)
    assert planar_reflection(canvas, 100).size == canvas.size
    assert fake_subsurface(canvas, mask).size == canvas.size
    assert motion_blur_accumulate(lambda t: canvas, 1, samples=3).size == canvas.size
    assert apply_baked_light(canvas, mask).size == canvas.size
    assert warp_quad(canvas, (96,160), ((5,5),(90,0),(90,155),(0,150))).size == (96,160)
    assert clay_lighting(canvas.size).size == canvas.size
    print("ok: all six recipes smoke-tested")
