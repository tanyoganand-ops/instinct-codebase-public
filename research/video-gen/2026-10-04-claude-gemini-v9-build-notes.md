# V9 - depth pass on the selected V8

Iterates on V8, not a new layout. Same 15-second narrative, model marks, score pairs, pale background, restrained timing, pendulum sway, verdict and CTA. V8 preserved.

## Changes

Separate foreground UI / evidence / background parallax, with small continuous perspective movement. Model carriers turn +/-5 degrees in depth at the benchmark handoff, lift 12px in z, and travel 32px sideways before returning. Evidence carrier moves 22px and rounds through the same handoff. Clay sphere/donut turn +/-13 degrees in perspective with a small x-axis nod, retaining gentle drift. This is 2.5D image-plane motion, not volumetric models.

Directional contact shadows and soft ambient-occlusion-style inner wells. Defocused accents/background have small blur falloff while text stays sharp. White UI surfaces are more opaque, contact shadows narrower, liquid-glass detail confined to carrier edges.

Glass now samples the live dot background in six-pixel strips, with stronger edge-dependent offsets and sampling stretch. Gloss/rim shading remains animated. Original 2D lens-displacement approximation, not a physically based glass shader or native Apple Liquid Glass.

Phone legibility: source rail 37px (was 29px), benchmark headings 41px (was 35px), evidence names 31px (was 26px), hint 30px (was 26px). Tiny metadata still needs deliberate viewing; no guarantee of readability on every device size.

## QA and export

450 resolved states saved before render in frames-v9.json. Runtime, layout and contrast checks pass with zero errors and no layout/contrast warnings. Five nonblocking lint warnings remain for composition structure, intentional lens canvas clipping and cue audio muxed after capture. Seven decoded final states inspected, including mid-handoff: soft disappearance of old scores before new numbers, correct 64/57 and 71/78, intact verdict/CTA and source rail. Full decode passed. 1080x1920, 30fps, 450 frames, 15.000 seconds, H.264 yuv420p + AAC, faststart.

Local render captured all 450 JPEG frames, then the long render process was interrupted during encoding. The incomplete video-only file was not used. Re-encoded the complete captured sequence with FFmpeg libx264, CRF16, fast preset, and the existing cue WAV. Final metadata is recorded in verification.json. No cloud/publish/auth/spending.

## Build and sources

Pinned Hyperframes 0.8.115 / GSAP 3.14.2, local scripts/fonts/assets. HYPERFRAMES_NO_TELEMETRY=1 and DO_NOT_TRACK=1 on all invocations. Save state before capture, run check, render locally at 30fps, then mux the cue bed. Helper uses workspace-specific Puppeteer/Chrome paths, adapt for other machines. State JSON is portable to inspect. Source bank omits intermediate capture frames/node_modules/video binaries.

Original V8 code was retained and revised. No third-party animation component code copied, no Mixkit footage. Clay sphere/donut are supplied generated decorative assets. Real raster product lockups retained; supplied Anthropic corporate-A SVG was not substituted for Claude's product logo. Brand provenance and font notices included.

Reference choreography: https://www.youtube.com/watch?v=y7E7ZmwEWyM . No reference footage or website code reused. Later Cartier/Lusion signals informed continuity/depth goals, not asset reuse. This pass is not a claim of comparable real-3D production quality.

Benchmark snapshot sources carried from the earlier verified version, not freshly re-researched:
- https://artificialanalysis.ai/articles/gemini-4-argon-google-top-three-labs
- https://artificialanalysis.ai/models/gemini-4-argon
- https://www.anthropic.com/claude-sonnet-5-5
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/

30 Sep 2026 Artificial Analysis snapshot, Sonnet Max / Argon High. AutomationBench-AA is distinct from Google/Zapier AutomationBench. No universal-winner claim. Original dot equations were informed by earlier inspected three.js wave and React Bits technique references, not copied code. GSAP standard licence and font/brand caveats retained.
