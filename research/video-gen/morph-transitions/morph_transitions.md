# Procedural morph and handoff transitions

A small Pillow toolkit for vertical 1080 x 1920 Shorts. The companion `morph_transitions.py` returns one RGBA frame per normalized progress value `t` in `[0, 1]`; call it from an encoder loop (for example, 30 fps). All coordinates and default centers use the 1080 x 1920 canvas. Pass your own transparent PNG sprites or rendered card images to the image-based transitions.

## Setup

```bash
python -m pip install Pillow
```

```python
from PIL import Image
from morph_transitions import (
    card_to_card, exit_enter_pair, same_position_swap,
    tile_to_bar, bar_to_verdict,
)

# Typical frame loop
frames = [card_to_card(card_a, card_b, i / 44) for i in range(45)]
```

The frame endpoints are exact: `t=0` is the outgoing/start state and `t=1` is the settled incoming/end state. Clamp `t` if your render loop can overshoot.

## 1. Card-to-card silhouette morph

```python
frame = card_to_card(
    card_a, card_b, t,
    box_a=(90, 410, 990, 1320),
    box_b=(150, 540, 930, 1170),
    radius_a=54, radius_b=42,
)
```

The rounded silhouette smoothly reshapes from the first box to the second; the card artwork crossfades inside that shared moving mask. This keeps edges clean while still allowing portrait-to-landscape or large-to-small handoffs. Boxes use `(left, top, right, bottom)` pixels. The geometry uses `smoothstep(t) = 3t² - 2t³` (cubic ease-in/out); content crossfades linearly from `t=.38` to `.66` by default. Keep important text away from the crop edges because each asset is cover-fit to the changing silhouette.

## 2. Coordinated exit / enter pair

```python
frame = exit_enter_pair(
    outgoing_sprite, incoming_sprite, t,
    travel=(0.0, 0.30),  # fraction of canvas: exit downward, enter from above
)
```

Both sprites settle at the canvas center. The outgoing sprite travels in the direction given by `(dx fraction, dy fraction)` while the incoming sprite starts the same distance in the opposite direction. Outgoing position eases with cubic `smoothstep`; the incoming uses `cubic_out(t) = 1-(1-t)³` for a quicker arrival and soft landing. The outgoing also scales/fades slightly as it leaves; the incoming grows from 96% and fades in. For a left/right exchange use `travel=(.38, 0.0)`.

## 3. Same-position swap

```python
frame = same_position_swap(old_sprite, new_sprite, t, box=(850, 920))
```

The assets are fit to the same fixed box and share the same center. The old sprite gently shrinks, then fades away as the new one fades and grows in place. Its fade crossover uses smoothstep through `swap_window=(.38, .64)`. Use this for a changed number, photo, icon, or card face where spatial continuity matters more than motion.

## 4. Element transform: tile becomes bar

```python
frame = tile_to_bar(
    t, tile_text="SIGNAL", bar_text="THE MAIN POINT",
    tile_color=(91, 111, 230, 255), bar_color=(45, 179, 153, 255),
)
```

This is drawn from rounded geometry rather than a pre-rendered image: a 610 x 610 tile widens and flattens into a 920 x 210 bar by default. The shape and color use cubic smoothstep. The old label fades out from `.22` to `.40`; the new label fades in from `.44` to `.62`. A brief text-free beat avoids doubled lettering while the shape keeps moving. Both use smoothstep.

## 5. Element transform: bar becomes verdict

```python
frame = bar_to_verdict(
    t, bar_text="THE EVIDENCE", verdict_text="KEEP IT.\\nIT WORKS."
)
```

The 920 x 210 bar expands into a 900 x 500 verdict card. Its color and corner radius morph with cubic smoothstep; the old line gives way to the verdict from `.42` to `.66`. Verdict copy wraps to fit. A small teal marker appears above it as the final state settles. Supply a short verdict or explicit `\\n` line breaks for deliberate text pacing.

## Frame export example

```python
from PIL import Image
from morph_transitions import tile_to_bar

fps = 30
frames = [tile_to_bar(i / 44, "FEATURE", "ONE CLEAR POINT") for i in range(45)]
# Save a quick proof-of-motion preview; use your video encoder for a Short.
frames[0].convert("RGB").save(
    "tile-to-bar.gif", save_all=True,
    append_images=[f.convert("RGB") for f in frames[1:]],
    duration=round(1000 / fps), loop=0,
)
```

The module's `render_sequence(frames, path, fps)` is a convenience for looping GIF previews. It is not a final video encoder; feed the returned Pillow frames to the user's preferred video pipeline for H.264/MP4 output.
