# Claude vs Gemini v5 - build and resume notes

## Final state

Private review MP4, 1080x1920, 30fps, 450 frames, 15.000000 seconds. H.264 / yuv420p, AAC synthetic cues, faststart. No narration, publication or spending. Earlier versions preserved.

## Owner-directed changes from v4

- Hero carriers use a plain single-axis horizontal slide, 105px over 15 frames, out_cubic easing. Verdict uses a straight 140px dropdown. Opacity and scale remain 1, rotation remains 0. No diagonal fly, zoom, bounce or spin.
- Same two glass carrier UI, source rails, score hierarchy and CTA.
- Hero type and model labels use the real Noto Serif Display Black font. All supporting text, benchmark names, score numbers, rails and CTA use Liberation Sans Bold. Actual Claude/Gemini logo images retain their own lettering unchanged.
- Model labels below the marks are darker, 32px Black serif. This addresses the user's clarification that he meant the text underneath the logos, followed by his wider request that all type stop feeling spindly.
- Clearly visible dot field: 42px grid, radius 2.4-4.4px, radial displacement amplitude 34px with 900px decay, 240px wavelength, 2.4s period, plus 22px/28px crossing wave movement. Dots are strongly faded behind reading and source zones.
- Gradient visibly shifts blue/violet/coral, transitioning between palette stops over three seconds while broad color pools move over a six-second path.
- Six translucent glass glyphs enlarged to about 70px, drifting around the margins; brighter original stacked elliptical torus forms.
- Glass retained: sampled live backdrop, 9px edge displacement, 11px blur, frost and rim bands, independent 2.4s clipped specular sweep. This remains a 2D composited approximation, not physically ray-traced liquid glass.

## Content and provenance

0-3s faceoff; 3-6.5s Terminal-Bench 4.0; 6.5-10s AutomationBench-AA; 10-13s verdict; 13-15s CTA. Five-frame closing wipe returns to the opening.

Benchmarks unchanged: 64/57 Terminal-Bench 4.0; 71/78 AutomationBench-AA. Artificial Analysis source rail: 30 Sep 2026, Sonnet Max / Argon High. Animated interim count-up numbers are not separate results. AutomationBench-AA is distinct from Google's Zapier AutomationBench. Closing rail retains limited Argon rollout.

Sources from the earlier verified research, not a new research pass:
- https://www.anthropic.com/claude-sonnet-5-5
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/
- https://artificialanalysis.ai/articles/gemini-4-argon-google-top-three-labs
- https://artificialanalysis.ai/models/gemini-4-argon

Brand source caveats remain in assets/provenance.md. Claude is the supplied press-kit lockup; Gemini is a supplied Commons mirror, not a firsthand Google brand-download endpoint. No generated logo or external asset generation used.

## QA

Inspected 20-state contact sheet, full-size benchmark and CTA previews after the type change, and final encoded 360px-wide samples at frames 0, 145, 245 and 425. Black model labels fit inside both carriers; hero lines, score endpoints and CTA read clearly. Bright background remains distinct from text. Reading/source zones have reduced dot contrast. The left opening carrier has minimal edge padding at its initial slide position but its content is intact.

ffprobe verifies exactly 450 frames, 30/1, 1080x1920 and 15.000000 seconds. Full decode passed. verification.json records the 13,050,629-byte MP4. More visible particles increase bitrate versus v4. qa-encoded-phone.png is the decisive encoded contact sheet.

## Rebuild

Python 3, Pillow, NumPy, ffmpeg and ffprobe. Fonts and license texts included.

```sh
python3 production.py --preview
python3 production.py
```

The resolved 450 frame states are written before render to frames-v5.json. tracks-v5.json holds authored animation tracks. 450-frame-plan-v5.md is the readable coordinate plan. Individual particles, gradient samples and specular sampling use deterministic equations from the saved integer frame, not fully enumerated particle vertices or pixels. Ambient phases are stored. No randomness or network.

Edit production.py for content, visual bank and scene timings; frame_engine.py for easing. Keep future revisions in a new version. No pending render or external workflow.


## Anti-patterns from Instagram reel (2026-10-03)

Source: https://www.instagram.com/reel/DcrqbqZRVvC/ by @millee.md, viewed signed-out on 3 October 2026. Caption: "Does your website or app have any of these?" The post title/on-screen heading reads "20 reasons why your app looks vibecoded (Give this to Claude/chatGPT)". The captured opening still shows a creator talking directly to camera in a home office; overlaid list numbers and headline sit on top of the face/background. First two visible items: "Purple-to-blue gradient" and "Gradient hero text." Later entries were not legible in captured frames, so do not infer them from comments or list numbering.

Avoid these patterns on both the video and any accompanying website:
- Default purple-to-blue gradients used as the main page/background treatment.
- Gradient-filled hero/headline text.
- Generic template or "vibecoded" styling without a distinctive, purposeful visual system; keep original personality and choices, rather than stacking common AI-site tropes.
- For reference-driven short videos, do not place dense list numerals/labels across a speaker's face or let overlays compete with the subject. This is a directly observed composition issue, not an asserted item from the reel's unseen list.

Evidence limit: the caption and heading frame establishes that this is a list of 20 anti-patterns, but only items 1 and 2 were readable in the accessed stills. Instagram provided a playable MP4 URL, but playback stayed at readyState 0/currentTime 0/networkState 2 even after using the embed route and Play. Thus entrances, full list, transitions, timing, fonts and later shots could not be verified. Treat the above as the two visible checklist points plus explicit framing note, not as a complete twenty-item extraction. See the checked reel URL above.
