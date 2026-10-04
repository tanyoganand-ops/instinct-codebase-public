# Hyperframes local validation and six v7 motion studies

## Result

Local rendering works. The standalone validation clip is 12s, 1080x1920, 30fps, 360 frames. Six comparison clips are each 8s, 1080x1920, 30fps, 240 frames. Silent H.264 MP4s. Original v6 files untouched. No publication or paid generation.

Exercised adopted packs: hyperframes-core (composition contract and clip timing), hyperframes-animation (paused seekable transforms and visible channels), hyperframes-keyframes (SVG DrawSVG/MorphSVG and diagnostics). CLI docs used for lint/check/render. Pinned hyperframes 0.8.115 and GSAP 3.14.2, Node 22, local system Chrome and FFmpeg. Telemetry disabled with HYPERFRAMES_NO_TELEMETRY=1 and DO_NOT_TRACK=1. No login/cloud/publish. Assets/scripts/fonts local during render; package downloads occurred only during setup. Lockfile included.

## Validation proof

The 12s scene exercises SVG draw-on, hexagon/circle/triangle interpolation, single-axis card entrance, paused deterministic timeline, direct-seek count-up and readable final hold. Real-pixel keyframe strip confirms changing shape geometry. Full browser gate: runtime/layout/contrast errors zero; 41/41 contrast checks passed; motion assertions ran across 241 samples and passed. Intentional full-bleed/decorative overflow was explicitly marked. Four nonblocking lint warnings recommend nested scene groups become sub-compositions.

Rendered in 55.4s: screenshot/software GPU, capture 29.1s, encode 25.8s. System Chrome does not expose optimized beginFrame; no headless shell downloaded. This is a proven fallback, not a benchmark of the optimized renderer.

## Documentation gaps

- Minimal skeleton uses CDN GSAP and Inter. Replace with locally vendored assets for this project; do not paste it unchanged.
- Core permits registration after document.fonts.ready; animation guidance prohibits asynchronous/Promise construction. Both instructions cannot be followed literally. Test uses synchronous build and local fonts.
- Minimal nested clips work, but the linter recommends sub-compositions for those same nested groups. Warnings are architectural advice, not a render failure.
- check reports ok=true despite warnings. Inspect counts, browserSkipped and motion.enabled rather than calling this "zero findings".
- Without a motion sidecar, motion checks are disabled, not passed. Validation test adds explicit assertions.
- keyframes --json combined with --shot emits a human status prefix before the JSON. Strip or separate it when parsing.
- GSAP package describes its standard no-charge license; its linked full license page was challenge-blocked. Package README/license metadata were inspected, but independent full-term verification was not possible here. Do not mislabel GSAP as Apache-2.0; Hyperframes' upstream license is separate.

## Six variants

Same endpoint scene (71/78 AutomationBench-AA), same exact logos, same Anton type. Tests vary dot dynamics, frost and slide duration without changing factual content.

| Choice | Dot motion | Glass | Image slide |
|---|---|---|---|
| V1 Pearl ripple | decaying concentric ripples | medium translucent frost, 18px blur | 1.2s |
| V2 Satin wave | crossing rolling sine waves | 24px stronger frost | 1.4s |
| V3 Twin pulse | two offset ripple origins interfere | light 15px frost | 1.1s |
| V4 Glass orbit | angular swirling wave field | transparent 20px frost | 1.6s |
| V5 Aurora depth | layered depth/size waves, soft dot bloom | deep 28px frost | 1.4s |
| V6 Breathing lattice | quiet coherent size/position breathing | heavy 32px frost | 1.8s |

140px single-axis image travel, opacity .05 to 1; no fly/zoom/spin. Text fades/rises over 1.15s, rails fade over 1.2s. 4s restrained specular sweeps. Near-white pale color pools keep the requested shifting-glass treatment. Frost now covers carriers, main text surface and rail surface; dots remain continuous behind those layers. This is CSS backdrop blur/frost/specular, not physically refractive Apple Liquid Glass. Existing Anton was retained because this round was not a new font selection.

Taste shortlist: V1 obvious ripple; V2 fluid surface; V6 most restrained. A chosen motion still needs integration into the full 15s sequence, not automatic approval of these studies as the final Short.

## Public source research

Inspected source code, not merely search excerpts:
- https://github.com/mrdoob/three.js/blob/9813ee76/examples/webgl_points_waves.html
  height uses crossing sine waves; point size also follows sine phase. Adapted into V2/V6.
- https://raw.githubusercontent.com/DavidHDev/react-bits/main/src/content/Backgrounds/DotGrid/DotGrid.jsx
  distance-based falloff, inertia and shock displacement. Adapted as autonomous deterministic ripples in V1/V3/V4, not mouse interaction.
- https://raw.githubusercontent.com/DavidHDev/react-bits/main/src/content/Backgrounds/Particles/Particles.jsx
  time-driven drift on multiple axes and depth-dependent point size. Adapted into V5.
- https://github.com/DavidHDev/react-bits

Implementations here are new small Canvas equations informed by those techniques, not installed/copied Three.js or React Bits demos. tsParticles was discovered but not used, so it receives no implementation credit.

## QA

Each variant: browser check runtime/layout/contrast errors zero; four nonblocking structural lint warnings. Exact 240-frame/8s ffprobe readback; full MP4 decode clean. Inspected all six settled snapshots plus actual encoded frames 20,120,239, and sampled V4 clip. Endpoints, model labels and supporting text fit. Early fades intentionally leave content translucent; settled state remains clear. DOT animation shape differences require playback, not choosing from a static contact sheet alone.

## Rebuild

Run npm ci --ignore-scripts from the source bank. Each V folder is self-contained for assets and HTML. Set telemetry environment variables on every invocation. Example:

```sh
HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1 ./node_modules/.bin/hyperframes check V1 --at .2,2,4,7.9 --snapshots
HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1 ./node_modules/.bin/hyperframes render V1 --output V1.mp4 --fps 30 --quality looks --workers 2 --strict --no-browser-gpu
```

No external assets at render time. build.py regenerates six HTML variants from the standalone validation source if that source is supplied at its original path; existing V folders need no regeneration. validation/index.html and validation/index.motion.json preserve the proof scene. Each variant carries check/verification JSON. No copied upstream helper scripts executed.
