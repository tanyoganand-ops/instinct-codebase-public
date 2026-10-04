# Clay 3D animation library - catalog (batch 1)

Common spec: RGBA VP9 webm (yuva420p), 1020x765, 24 fps, 72 frames = 3.0 s, seamless loop (frame 71 flows into frame 0). Each clip ships as two layers: `<clip>_card.webm` (the object, premultiplied-correct alpha) and `<clip>_shadow.webm` (black, alpha-only shadow), so the shadow can be recoloured, moved or dropped. Layer shadow under the object. Use VP9-alpha-capable decode (Chrome / libvpx); for ffmpeg compositing decode with `-c:v libvpx-vp9` before `-i`. Renderer: numpy SDF raymarch, source scene.py / lib.py / clips.py. Palette: blue #9cbcec, orange #F2AE80, Claude peach (.97,.78,.66), Gemini pale blue (.74,.84,.98). Camera: z=5.5, fcam 0.145, canvas half-width about 1.06 world units, half-height 0.8. Check images show frames 0, 18, 36, 54 over #9cbcec.

| Clip | Move | Parameters (t = 0..1 across the loop) |
|---|---|---|
| claude_turntable / gemini_turntable | 360 deg turntable spin of the card (logo front only, back is plain clay) | yaw = 2*pi*t (linear), pitch 0.12*sin(2*pi*t), vertical bob 0.03*sin(2*pi*t); shadow softness follows bob |
| cardflip_gemini_claude | Flip reveal, front Gemini / back Claude, flipped twice per loop | 3.0 s timeline: hold 0.7 s, flip 0.8 s (yaw 0 to pi, ease-out-back overshoot 1.2), hold 0.7 s, flip 0.8 s (pi to 2pi). During flip card lifts 0.5 toward camera (sin arc), tilts pitch -0.12, roll 0.06*sin(pi*lift); shadow gets softer and fainter when lifted |
| sphere_donut_bounce | Squash-and-stretch bounce chain: blue and orange spheres at x=-0.5 / +0.5 alternate | each sphere period 1.0 s (3 bounces per loop), second sphere phase offset 0.5; height h=1-(2u-1)^2, apex 0.62 world units; contact squash when within 12% of ground: sy=1-0.34c, sx=1+0.20c; flight stretch +0.12*sqrt(h); ground shadow is an analytic ellipse layer, shrinks and fades 55% with height. Note: despite the name, only spheres appear |
| donut_orbit | Slow camera orbit around a clay donut (orange) | camera azimuth 0 to 2*pi over the loop, elevation 0.45+0.18*sin(2*pi*t) rad, radius 5.5, looking at origin; torus R=0.40 r=0.19; shadow is the default blurred offset silhouette |

## Reuse notes
- Scale freely in the build; sizes assume the object fills about 60-85% of canvas width.
- Easing used: smoothstep for holds, outback for flips (`c=1.2`).
- Known limits: smooth matte clay (no fingerprints), fake offset shadow (not cast on other objects), 648-1360 px render resolution downsampled to 1020x765 (not 1080x1920; for a full-frame 1080x1920 hero place the clip on the canvas and scale up modestly). The turntable back face is blank.

## Batch 1b
| Clip | Move | Parameters |
|---|---|---|
| gemini_turntable | Same as claude_turntable with the Gemini card (pale blue) | identical spin/bob parameters |
| donut_roll (REDONE) | Donut rolls as a wheel across the canvas, enters left and exits right (empty at the seam), with three clay bumps on the ring and a tilt wobble so the roll reads | x = -1.75 + 3.5*t, scale 0.75, roll angle = -x/0.44, pitch wobble 0.45*sin(2pi*3t), yaw wobble 0.35*sin(2pi*2t); ground at y=-0.65, analytic ellipse shadow follows x |

## Batch 2
| Clip | Move | Parameters (time in seconds across a 3.0 s loop) |
|---|---|---|
| assembly_mosaic | Pop-in assembly: 6 clay tiles (blue, orange, Claude, lilac, Gemini, mint) fly in from off-canvas with spin, lock into a 3x2 mosaic, pulse, then fly out | tile scale 0.36; grid x -0.62/0/0.62, y +0.2/-0.2; fly-in 0 to 1.2 s with ease-out-back c=1.4 and per-tile stagger 0.08 s; start offsets (+-2.6, +-1.6..2.5); spin 3.2+0.5*i rad decaying to 0; pulse +7% at 1.45-1.95 s; fly-out 2.15-2.9 s smoothstep, loop is empty at the seam |
| tumble_drop_exit | Tumble drop: Gemini/Claude card falls spinning from above, bounces twice with damped wobble and slight squash, holds, anticipates (dip), then launches off the top | fall 0-1.1 s from y=1.7 to -0.1 (accelerating), bounce 1 (+0.38) 1.1-1.55 s, bounce 2 (+0.1) 1.55-1.85 s, hold to 2.45 s, dip 0.05 for 0.2 s, exit 2.65-3.0 s (power 2.2); landing wobble 0.5*exp(-3.2t)*sin(11t); squash sy 0.88 at contacts; default silhouette shadow |
| card_pendulum | Gemini/Claude card swinging from a rod, with a slight 3D twist | rod+card rotate about pivot (0,0.95); swing theta = 0.36*sin(2pi*t) rad; twist yaw 0.3*sin(2pi*t+pi/2); rod length 0.5, card scale 0.8; FIXED in batch 3: card orientation is now Rz(swing) @ Ry(twist) so the card's top-edge midpoint stays on the rod end at all swing angles |

## Batch 3
| Clip | Move | Parameters (3.0 s loop) |
|---|---|---|
| card_fan_deal | Card stack fans out like a dealt hand, holds, then collapses back to a stack | 5 cards (mint, lilac, butter tiles; Gemini; Claude on top), scale 0.62, pivot (0,-0.75); fan 0-1.0 s smoothstep, hold 1.0-2.0 s, collapse 2.0-3.0 s; card i angle (i-2)*0.40 rad at full fan; card distance from pivot grows 0.475 to 0.95; z step 0.03 per card. Nit: Gemini logo is mostly hidden under Claude in the fanned pose (increase spread or reorder to show both) |
| bubble_pop_in | Pop-in with overshoot: Gemini card scales from 0 with ease-out-back overshoot, two expanding clay rings (orange then blue) and 6 pastel pellets burst outward; card pops out at the end | card scale outback(t/0.7, c=2.2) then breathe +-2% 0.7-2.4 s, shrink out 2.4-2.9 s; rings: scale 0.6 to 2.6 over 0.8 s (delays 0 and 0.14 s), tube radius 0.035; pellets: radius 0.4 to 1.4 with decelerating ease, size shrinks 0.09 to 0.01 over 1.0 s; loop empty at the seam |
| camera_dolly_through | Camera dollies between two cards (Claude left, Gemini right) past a lilac tile and out the other side, seamless loop | camera z = 4.5 + 2cos(2*pi*t); cards at x = +-0.62, yaw +-0.5 rad; lilac tile behind at x=0 |
| sphere_donut_morph | Blue sphere squash-morphs into an orange donut and back | sphere/torus SDF blend m = 0.5-0.5cos(2*pi*t); pitch 0.6*m; colour blue to lilac to orange; squash 1+0.12 sin(4*pi*t). Nit: hole is only faintly visible at mid-morph |
| card_jelly_settle | Gemini card wobbles like jelly and settles, repeating each loop | warp x += a sin(5y+phi)(1+z), y += 0.8a sin(4x+1.3phi); a = 0.09 e^(-1.6t) cos(13t). Logo deforms with the card (exception to the brand guidance, flagged for approval) |
