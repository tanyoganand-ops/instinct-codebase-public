# Claude vs Gemini v6 - build and resume notes

## Final deliverable

Private review MP4: 1080x1920, 30fps, 450 frames / 15.000000s. H.264/yuv420p, AAC synthetic cue bed, faststart. No narration or publication. V1-v5 preserved separately.

## Selected direction

Anton (T5) replaces the rejected serif in hero lines and model labels beneath exact logo images. Supporting labels, scores, rails and CTA pill remain bold sans. Anton's named Regular file is an inherently heavy condensed display design, not a thin face. Font binary and SIL OFL license included.

W1 silk mesh replaces the dot field. 102 continuous full-width lines; 15px spacing; 48px sinusoidal displacement; phase = frame*.023 plus per-line offset. The wave passes behind all text and source rails without an exclusion mask, interrupted line, early fade or locally cleared zone. Layer order is ground, mesh, glass/glyphs, foreground text. No masking out of the mesh near words.

White-biased liquid-glass scene retained, rather than the rejected dark study scene. Pale blue/lilac/coral color pools still shift between stops every 90 frames and move on a 180-frame path. This keeps the specifically requested gradient/glass override, but the ground is much lighter than v5.

V5 layout and motion stay: plain 105px horizontal slides over 15 frames, one 140px verdict dropdown; no diagonal paths, zoom, spins or bounce. Same 32px fade-rise text, score count-ups, source rails and CTA. Six marginal translucent glyphs and three original elliptic ring forms remain.

Glass remains a 2D composited approximation: live backdrop sample, 9px displaced edges, 11px blur, frost and rims, 72-frame independent specular sweep. No claim of physical liquid-glass ray tracing.

## Scope and anti-patterns

The reference reel was inspected through supplied contact sheets; its full dark/orbit/HUD/typewriter grammar was not imposed after the user rejected dark and kept the previous glass/layout direction. The supplied anti-pattern constraints are respected apart from the user's explicit choice to retain glass and a shifting gradient: no emoji headings, Inter, badges above headings, italic-serif accents, em dashes in video text, or filler buzzwords. No new content or unrelated visual overhaul.

## Content

0-3s faceoff; 3-6.5s Terminal-Bench 4.0; 6.5-10s AutomationBench-AA; 10-13s verdict; 13-15s CTA, ending with a five-frame return to the opening.

Endpoint scores unchanged: 64/57 and 71/78. Source rail remains Artificial Analysis, 30 Sep 2026, Sonnet Max / Argon High. Animated interim count-up numbers are not new results. AutomationBench-AA differs from Google's Zapier AutomationBench. Limited Argon rollout stays on closing scenes.

Earlier verified research sources, not a new fact-check pass:
- https://www.anthropic.com/claude-sonnet-5-5
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/
- https://artificialanalysis.ai/articles/gemini-4-argon-google-top-three-labs
- https://artificialanalysis.ai/models/gemini-4-argon

Brand caveats: exact supplied Claude press-kit PNG and Gemini Commons-mirror PNG, unaltered. See assets/provenance.md. No invented logo font or external image generation.

Anton provenance:
- https://api.github.com/repos/google/fonts/contents/ofl/anton
- https://raw.githubusercontent.com/google/fonts/main/ofl/anton/Anton-Regular.ttf
- https://raw.githubusercontent.com/google/fonts/main/ofl/anton/OFL.txt

## QA

Inspected 20-state timeline previews, full-size workflow endpoint, and final encoded 360px-wide samples at frames 0,145,245,425 after retaining the shifting gradient. Model labels fit; scores and CTA read clearly. Mesh remains continuous behind text and evidence rails. Source rails remain secondary small print at phone width. The opening left carrier has minimal initial edge padding but its contents are intact.

ffprobe verifies 450 video frames at 30/1, 1080x1920 and 15.000000s. Full decode completed without errors. verification.json contains metadata; qa-encoded-phone.png is decisive encoded evidence.

## Rebuild

Python 3, Pillow, NumPy, ffmpeg and ffprobe. Included fonts and licenses.

```sh
python3 production.py --preview
python3 production.py
```

The 450 resolved states are written before render to frames-v6.json. tracks-v6.json stores authored tracks, and 450-frame-plan-v6.md lists the coordinate plan. Mesh vertices, gradient colors and specular samples are deterministic integer-frame equations, not fully enumerated pixels/particle vertices. Saved mesh/icon/light phases accompany each frame.

Edit production.py for visual bank/content and frame_engine.py for easing. Start a new version for future edits. No queued external task or pending render; no spending occurred.
