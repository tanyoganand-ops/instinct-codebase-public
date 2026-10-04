"""Procedural 1080x1920 transition helpers for vertical Python/Pillow Shorts.

All transition functions return a fresh RGBA frame. `t` is normalized 0..1.
Input image assets are PIL Images; pass RGBA sprites/cards for transparency.
"""
from __future__ import annotations

from math import ceil
from typing import Iterable, Sequence
from PIL import Image, ImageDraw, ImageFont, ImageOps

SIZE = (1080, 1920)
W, H = SIZE
RGBA = tuple[int, int, int, int]


def _clamp(t: float) -> float:
    return max(0.0, min(1.0, float(t)))


def smoothstep(t: float) -> float:
    """Cubic ease-in/out, with zero slope at both ends."""
    t = _clamp(t)
    return t * t * (3.0 - 2.0 * t)


def cubic_out(t: float) -> float:
    """Quick start, soft landing; useful for arrivals and reveals."""
    t = _clamp(t)
    return 1.0 - (1.0 - t) ** 3


def _mix(a: float, b: float, p: float) -> float:
    return a + (b - a) * p


def _mix_color(a: RGBA, b: RGBA, p: float) -> RGBA:
    return tuple(round(_mix(x, y, p)) for x, y in zip(a, b))  # type: ignore[return-value]


def _canvas(background: RGBA) -> Image.Image:
    return Image.new("RGBA", SIZE, background)


def _font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    paths = (
        ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else
         "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        ("/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf"),
    )
    for path in paths:
        try:
            return ImageFont.truetype(path, max(1, size))
        except OSError:
            pass
    return ImageFont.load_default()


def _fit(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    return ImageOps.fit(image.convert("RGBA"), size, method=Image.Resampling.LANCZOS,
                        centering=(0.5, 0.5))


def _rounded_mask(size: tuple[int, int], radius: int) -> Image.Image:
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size[0] - 1, size[1] - 1),
                                           radius=max(0, radius), fill=255)
    return mask


def _centered_paste(canvas: Image.Image, sprite: Image.Image, cx: float, cy: float,
                    scale: float = 1.0, alpha: float = 1.0) -> None:
    if scale <= 0 or alpha <= 0:
        return
    width = max(1, round(sprite.width * scale))
    height = max(1, round(sprite.height * scale))
    layer = sprite.convert("RGBA").resize((width, height), Image.Resampling.LANCZOS)
    if alpha < 1:
        a = layer.getchannel("A").point(lambda value: round(value * _clamp(alpha)))
        layer.putalpha(a)
    x, y = round(cx - width / 2), round(cy - height / 2)
    canvas.alpha_composite(layer, (x, y))


def _wrap_lines(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont,
                max_width: int) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        line = ""
        for word in words:
            candidate = f"{line} {word}".strip()
            if line and draw.textbbox((0, 0), candidate, font=font)[2] > max_width:
                lines.append(line)
                line = word
            else:
                line = candidate
        lines.append(line)
    return lines or [""]


def _draw_center_text(draw: ImageDraw.ImageDraw, text: str, center: tuple[float, float],
                      max_width: int, font_size: int, fill: RGBA = (255, 255, 255, 255),
                      bold: bool = True, spacing: int = 12) -> None:
    font = _font(font_size, bold)
    lines = _wrap_lines(draw, text, font, max_width)
    boxes = [draw.textbbox((0, 0), line, font=font) for line in lines]
    heights = [b[3] - b[1] for b in boxes]
    total_h = sum(heights) + spacing * max(0, len(lines) - 1)
    y = center[1] - total_h / 2
    for line, box, line_h in zip(lines, boxes, heights):
        line_w = box[2] - box[0]
        draw.text((center[0] - line_w / 2, y - box[1]), line, font=font, fill=fill)
        y += line_h + spacing


def card_to_card(a: Image.Image, b: Image.Image, t: float,
                 box_a: tuple[int, int, int, int] = (90, 410, 990, 1320),
                 box_b: tuple[int, int, int, int] = (150, 540, 930, 1170),
                 radius_a: int = 54, radius_b: int = 42,
                 background: RGBA = (13, 17, 26, 255),
                 content_crossfade: tuple[float, float] = (0.38, 0.66)) -> Image.Image:
    """Morph one rounded card silhouette into another, crossfading its content.

    Boxes are (left, top, right, bottom) in 1080x1920 pixels. Geometry uses
    smoothstep; content crossfades linearly only across the supplied interval.
    """
    t = _clamp(t)
    p = smoothstep(t)
    box = tuple(round(_mix(x, y, p)) for x, y in zip(box_a, box_b))
    x0, y0, x1, y1 = box
    size = (max(1, x1 - x0), max(1, y1 - y0))
    radius = round(_mix(radius_a, radius_b, p))
    lo, hi = content_crossfade
    content_p = _clamp((t - lo) / max(1e-6, hi - lo))
    content = Image.blend(_fit(a, size), _fit(b, size), content_p)
    content.putalpha(_rounded_mask(size, radius))
    out = _canvas(background)
    out.alpha_composite(content, (x0, y0))
    return out


def exit_enter_pair(outgoing: Image.Image, incoming: Image.Image, t: float,
                    travel: tuple[float, float] = (0.0, 0.28),
                    background: RGBA = (13, 17, 26, 255),
                    center: tuple[float, float] = (W / 2, H / 2),
                    arrival_scale: float = 0.96) -> Image.Image:
    """Outgoing sprite leaves along `travel`; incoming sprite enters from opposite.

    `travel` is a pair of viewport fractions: (dx/W, dy/H). Both sprites are
    centered at `center` when settled. Outgoing eases out; incoming uses cubic-out.
    """
    t = _clamp(t)
    out = _canvas(background)
    dx, dy = travel[0] * W, travel[1] * H
    out_p, in_p = smoothstep(t), cubic_out(t)
    _centered_paste(out, outgoing, center[0] + dx * out_p,
                    center[1] + dy * out_p, 1.0 - 0.04 * out_p,
                    1.0 - 0.12 * out_p)
    _centered_paste(out, incoming, center[0] - dx * (1.0 - in_p),
                    center[1] - dy * (1.0 - in_p),
                    _mix(arrival_scale, 1.0, in_p), in_p)
    return out


def same_position_swap(a: Image.Image, b: Image.Image, t: float,
                       center: tuple[float, float] = (W / 2, H / 2),
                       box: tuple[int, int] = (850, 920),
                       background: RGBA = (13, 17, 26, 255),
                       swap_window: tuple[float, float] = (0.38, 0.64)) -> Image.Image:
    """Swap two images in one fixed box: shrink/fade A, then reveal/grow B.

    The swap window controls the crossfade; both assets stay registered to the
    same center to make a clean content replacement rather than a slide.
    """
    t = _clamp(t)
    lo, hi = swap_window
    p = _clamp((t - lo) / max(1e-6, hi - lo))
    eased = smoothstep(p)
    a_scale = 1.0 - 0.08 * smoothstep(t / max(lo, 1e-6))
    b_scale = 0.92 + 0.08 * cubic_out(max(0.0, (t - lo) / max(1e-6, 1.0 - lo)))
    fitted_a, fitted_b = _fit(a, box), _fit(b, box)
    out = _canvas(background)
    _centered_paste(out, fitted_a, *center, a_scale, 1.0 - eased)
    _centered_paste(out, fitted_b, *center, b_scale, eased)
    return out


def _shape_panel(out: Image.Image, box: tuple[float, float, float, float], radius: int,
                 fill: RGBA, label: str, font_size: int = 68,
                 text_fill: RGBA = (255, 255, 255, 255), bold: bool = True) -> None:
    x0, y0, x1, y1 = box
    draw = ImageDraw.Draw(out)
    draw.rounded_rectangle((round(x0), round(y0), round(x1), round(y1)),
                           radius=max(0, radius), fill=fill)
    _draw_center_text(draw, label, ((x0 + x1) / 2, (y0 + y1) / 2),
                      max_width=max(40, round(x1 - x0 - 64)), font_size=font_size,
                      fill=text_fill, bold=bold)


def tile_to_bar(t: float, tile_text: str = "FEATURE",
                bar_text: str = "ONE CLEAR POINT", tile_color: RGBA = (91, 111, 230, 255),
                bar_color: RGBA = (45, 179, 153, 255),
                background: RGBA = (13, 17, 26, 255),
                center: tuple[float, float] = (W / 2, H / 2),
                tile_size: tuple[int, int] = (610, 610),
                bar_size: tuple[int, int] = (920, 210)) -> Image.Image:
    """Turn a square tile into a wide bar while replacing its short label."""
    t = _clamp(t)
    shape = smoothstep(t)
    old_alpha = 1.0 - smoothstep(_clamp((t - 0.22) / 0.18))
    new_alpha = smoothstep(_clamp((t - 0.44) / 0.18))
    width = _mix(tile_size[0], bar_size[0], shape)
    height = _mix(tile_size[1], bar_size[1], shape)
    radius = round(_mix(58, 36, shape))
    out = _canvas(background)
    # Two text passes keep the geometry continuous while the words change.
    fill = _mix_color(tile_color, bar_color, shape)
    box = (center[0] - width / 2, center[1] - height / 2,
           center[0] + width / 2, center[1] + height / 2)
    draw = ImageDraw.Draw(out)
    draw.rounded_rectangle(tuple(round(v) for v in box), radius=radius, fill=fill)
    if old_alpha > 0:
        _draw_center_text(draw, tile_text, center, round(width - 64), 62,
                          fill=(255, 255, 255, round(255 * old_alpha)))
    if new_alpha > 0:
        _draw_center_text(draw, bar_text, center, round(width - 64), 54,
                          fill=(255, 255, 255, round(255 * new_alpha)))
    return out


def bar_to_verdict(t: float, bar_text: str = "THE EVIDENCE",
                   verdict_text: str = "KEEP IT.\nIT WORKS.",
                   bar_color: RGBA = (45, 179, 153, 255),
                   verdict_color: RGBA = (37, 31, 33, 255),
                   background: RGBA = (13, 17, 26, 255),
                   center: tuple[float, float] = (W / 2, H / 2),
                   bar_size: tuple[int, int] = (920, 210),
                   verdict_size: tuple[int, int] = (900, 500)) -> Image.Image:
    """Expand a bar into a verdict card; title changes during the shape settle."""
    t = _clamp(t)
    shape = smoothstep(t)
    old_alpha = 1.0 - smoothstep(_clamp((t - 0.28) / 0.16))
    text_p = smoothstep(_clamp((t - 0.48) / 0.20))
    width = _mix(bar_size[0], verdict_size[0], shape)
    height = _mix(bar_size[1], verdict_size[1], shape)
    radius = round(_mix(36, 54, shape))
    fill = _mix_color(bar_color, verdict_color, shape)
    box = (center[0] - width / 2, center[1] - height / 2,
           center[0] + width / 2, center[1] + height / 2)
    out = _canvas(background)
    draw = ImageDraw.Draw(out)
    draw.rounded_rectangle(tuple(round(v) for v in box), radius=radius, fill=fill)
    if old_alpha > 0:
        _draw_center_text(draw, bar_text, center, round(width - 64), 54,
                          fill=(255, 255, 255, round(255 * old_alpha)))
    if text_p > 0:
        # Verdict occupies a centered block with a small teal marker.
        _draw_center_text(draw, verdict_text, (center[0], center[1] + 48), round(width - 100), 78,
                          fill=(255, 255, 255, round(255 * text_p)))
        dot_y = center[1] - height * 0.36
        draw.ellipse((center[0] - 12, dot_y - 12, center[0] + 12, dot_y + 12),
                     fill=(115, 210, 185, round(255 * text_p)))
    return out


def render_sequence(frames: Iterable[Image.Image], path: str, fps: int = 30) -> None:
    """Write RGBA frames as a looping GIF preview (not intended as final video)."""
    frames = list(frames)
    if not frames:
        raise ValueError("render_sequence needs at least one frame")
    rgb = [frame.convert("RGB") for frame in frames]
    rgb[0].save(path, save_all=True, append_images=rgb[1:], duration=round(1000 / fps),
                loop=0, optimize=False)


if __name__ == "__main__":
    # Tiny smoke demo: `python morph_transitions.py` writes demo_morph.gif.
    card_a = Image.new("RGB", (640, 840), (233, 191, 105))
    card_b = Image.new("RGB", (840, 520), (91, 135, 211))
    for img, text in ((card_a, "CARD A"), (card_b, "CARD B")):
        d = ImageDraw.Draw(img)
        _draw_center_text(d, text, (img.width / 2, img.height / 2), img.width - 80,
                          64, fill=(25, 31, 45, 255))
    frames = [card_to_card(card_a, card_b, i / 29) for i in range(30)]
    render_sequence(frames, "demo_morph.gif", fps=30)
