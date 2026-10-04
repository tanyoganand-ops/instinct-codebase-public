# V7 full Short - Glass orbit

## Delivered

15.000s, 1080x1920, 30fps, 450 frames, H.264/AAC, faststart MP4. Synthetic cue bed reused from v6; no narration. V6 and all six motion tests preserved separately. Private review, not published.

## Choice and motion

V4 Glass orbit supersedes the earlier V2 routing. The latest user reply named the V4 clip as "rly nice, best so far", then asked for more prominent animation and asset-level work.

Orbit displacement increased from 18px to 36px, angular rotation phase from .15t to .22t, dot radius breathing from +/-0.7px to +/-1.05px, and opacity from .30+/-.15 to .36+/-.18. The deterministic angular wave remains continuous behind the frosted foreground.

Two model carriers enter in 1.6s with 140px horizontal travel and visible opacity .35 to 1; second starts .15s later. No diagonal fly, zoom, spin or bounce. Carriers persist through the whole clip. At the benchmark handoff they counter-slide 20px over .45s, then return over .75s; scores dip, update, and reveal without restarting the whole UI.

Hero text fades/rises over .7s per beat and fades out over .3s. Opening starts partially visible instead of empty. Result surface itself fades/rises over 1.15s. Source rail fades in over .8s. Score count-ups take 1.4s. Specular sweeps take 4s. The final CTA holds to the last frame rather than snapping back to the opening.

Glass: 30% white tint / 20px backdrop blur on carriers; frosted main text surface / 12px blur; frosted source surface / 10px blur; white rims, inner edge bands and restrained shadows. This is CSS frost/backdrop blur/specular, not physically refractive Apple Liquid Glass. Anton remains the selected hero/model-label face; supporting text is bold sans. Exact supplied logo images unchanged.

## Sequence

0-3s faceoff; 3-6.5s Terminal-Bench 4.0 at 64/57; 6.5-10s AutomationBench-AA at 71/78; 10-13s different tests/different winners; 13-15s CTA. Source rail dated 30 Sep 2026, Sonnet Max / Argon High; closing limited-rollout caveat. Scores hidden in opening/closing scenes. This pass changes motion/style, not factual content.

## Verification

Live browser check ran (not skipped): zero runtime, layout and contrast errors. Three nonblocking structural lint warnings recommend sub-compositions for nested groups. Settled text fits; model lockups intact. Visually inspected verdict full-size plus six final encoded states at frames 0,60,150,255,345,435. Early opacity is intentional and readable enough to identify the faceoff, settled states are clear. Full decode passed. verification.json records exact frame count, codecs and size.

frames-v7.json was saved before render with 450 resolved samples of card/text transforms, coordinates, opacity and scores. 450-frame-plan-v7.md is a coordinate overview. Dots and backdrop sampling remain deterministic equations evaluated at saved frame time, not every pixel/particle enumerated.

## Build

Pinned hyperframes 0.8.115, GSAP 3.14.2, lockfile. Local vendored scripts/fonts/brand images. Set HYPERFRAMES_NO_TELEMETRY=1 and DO_NOT_TRACK=1 on every invocation. No auth/cloud/publish, external image generation or spending.

```sh
npm ci --ignore-scripts
HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1 ./node_modules/.bin/hyperframes check . --snapshots
HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1 ./node_modules/.bin/hyperframes render . --output v7-silent.mp4 --fps 30 --quality looks --workers 2 --strict --no-browser-gpu
ffmpeg -y -i v7-silent.mp4 -i cues.wav -c:v copy -c:a aac -b:a 160k -t 15 -movflags +faststart claude-vs-gemini-v7.mp4
```

save-frame-plan.cjs is a validation helper tied to this workspace's Puppeteer install/path; adapt those paths for a separate checkout. Existing saved JSON needs no helper run to inspect. Package excludes node_modules and video binaries. No pending render.

## Source provenance

Research values carried from earlier verified pages, not newly re-researched:
- https://artificialanalysis.ai/articles/gemini-4-argon-google-top-three-labs
- https://artificialanalysis.ai/models/gemini-4-argon
- https://www.anthropic.com/claude-sonnet-5-5
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/

Dot design is a new deterministic Canvas adaptation informed by inspected source techniques, not copied library demos:
- https://raw.githubusercontent.com/DavidHDev/react-bits/main/src/content/Backgrounds/DotGrid/DotGrid.jsx
- https://raw.githubusercontent.com/DavidHDev/react-bits/main/src/content/Backgrounds/Particles/Particles.jsx
- https://github.com/mrdoob/three.js/blob/9813ee76/examples/webgl_points_waves.html

Brand caveats retained in brand-provenance.md: Claude supplied press-kit raster, Gemini Commons mirror, no endorsement claimed. Anton font provenance/license and Liberation license included. GSAP has a distinct standard no-charge license, not Hyperframes' Apache license; full external license page was challenge-blocked during the earlier test, package license metadata was inspected.
