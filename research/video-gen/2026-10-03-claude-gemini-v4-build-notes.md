# Claude vs Gemini v4 - build and resume notes

## Delivered

15 seconds, 1080x1920, 30fps, 450 video frames. H.264 / yuv420p with AAC synthetic cue bed, fast-start MP4. No narration. Private review render, not published. Older versions are preserved separately.

## What changed

- Immediate diagonal fly/zoom arrivals, staggered by two frames, fully settled in 16 frames. Opening carriers start at 90% opacity; later scene boundaries at 60%, avoiding a vacant frame. The verdict uses a dropdown direction.
- Motion cubic-bezier (0,.71,.2,1.01) is evaluated by solving the x-coordinate before reading y. Hero scale .88 to 1, rotation +/-12 degrees to zero. Type rises 32px with a masked-slide-inspired easing (.625,.05,0,1), plus independent opacity. No actual type clipping mask is applied.
- Noto Serif Display for the hero lines. Liberation Sans for scores, model metadata, source rails and CTA pill. Font files and licenses included.
- Dot field at 42px spacing, 240px radial wavelength, 2.4s period, 18px amplitude decaying over 900px, plus two low-amplitude crossing sine waves. Main text region has reduced dot opacity.
- Six drifting original glass glyphs and three stacked elliptic wire torus forms. The shapes remain near the margins.
- Carriers sample the moving backdrop with 9px edge displacement, 11px blur, frost, multiple rim bands and a 2.4s specular sweep. This is a 2D composited approximation, not physical liquid-glass ray tracing. Ambient glyphs are translucent sprites, not fully refractive glass objects.
- Logos keep original proportions, shapes and colors inside carriers. Carrier rotation does not morph the mark.

## Content

0-3s faceoff; 3-6.5s Terminal-Bench 4.0; 6.5-10s AutomationBench-AA; 10-13s different tests/different winners; 13-15s CTA, ending with a five-frame return to the opening.

Artificial Analysis pairs remain 64/57 and 71/78, respectively. Source rail: 30 Sep 2026; Sonnet Max / Argon High. Count-up values are an animation, not additional benchmark results. AutomationBench-AA is not Google's Zapier AutomationBench. Argon limited-rollout caveat stays on the closing scenes.

Sources carried from the verified research:
- https://www.anthropic.com/claude-sonnet-5-5
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/
- https://artificialanalysis.ai/articles/gemini-4-argon-google-top-three-labs
- https://artificialanalysis.ai/models/gemini-4-argon

Brand asset provenance and trademark caveats are in assets/provenance.md. Gemini's source is a Commons mirror, not a firsthand Google brand-download endpoint. Claude press-kit retrieval rests on the earlier source handoff.

## Asset generation choice

No external image generation used. Native procedural layers keep geometry, reflections, rims and motion independently editable and preserve exact marks/type. A generated sculptural glass illustration remains a possible later asset test, not part of this version. No paid API, purchased asset, or spending occurred.

## QA

Rendered a 20-state contact sheet including entrances, score endpoints, scene boundaries and loop reset. Inspected the full-size opening, benchmark and CTA previews, plus final encoded 360px-wide phone samples at frames 195, 245 and 425. No clipped opening carrier; model lockups, score endpoints and CTA remain readable. Source rails are secondary small print at phone size.

ffprobe verifies 450 H.264 frames at 30/1, 1080x1920, duration 15.000000s. Full MP4 decode completed without errors. See verification.json and qa-encoded-phone.png.

## Rebuild / resume

Dependencies: Python 3, Pillow, NumPy, ffmpeg, ffprobe. From this directory:

```sh
python3 production.py --preview
python3 production.py
```

The first command writes the 450-state plan and QA previews without encoding. The second regenerates the same plan, previews and MP4. No randomness or network is used.

frames-v4.json is the resolved visible node state plan. tracks-v4.json contains the reusable authored motion tracks. 450-frame-plan-v4.md is its human-readable coordinate overview. Ambient particle positions are deterministic equations evaluated at the saved integer frame; the plan saves ambient phases, not every dot/icon vertex. Refraction and specular sampling are likewise deterministic rendering equations rather than individual saved pixels.

Edit production.py for scene text, geometry, ambient bank or carrier styles; edit frame_engine.py for easing. Keep all modifications under a new version when revising. The final state is complete and ready for review, with no queued render or pending external generation.
