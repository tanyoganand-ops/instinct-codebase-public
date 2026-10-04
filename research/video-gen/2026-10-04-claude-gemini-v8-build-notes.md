# V8 - Clay layout, glass finish

15 seconds, 1080x1920, 30fps, 450 frames. Original composition inspired by the supplied HinedFx Clay ad, not copied footage or website code. Older versions retained.

## Reference reading

The selected ad was inspected at two samples per second across the full 24.867-second source. Its recipe is pale space, mixed-radius UI modules, modest contact shadows, blur-to-clear phrases and horizontal handoffs. The supplied reconstruction tokens distinguish measured colours from estimated geometry; the composition uses canvas #F3F3F3, soft blue tracks #D8E7ED and navy CTA #001030. The evidence panel has a smaller radius and weaker shadow than the model carriers. The exact typography cannot be recovered from a flattened reference. Local bold sans headlines and previously selected Anton model labels are used, not Inter.

This is a clay/glass hybrid suited to the later steering, not a pixel-identical Clay replica. The UI stage remains a full portrait composition, rather than copying the reference's letterboxed square presentation.

## Motion

- Model carriers slide/fade into place over 1.8s, staggered by .2s. They persist throughout and make a 45px vertical handoff to clear the evidence space.
- Real brand images sway +/-1.4 degrees with 3px lift on a continuous pendulum. No fast fly, spin, zoom or bounce.
- Headlines resolve through blur and 22px rise over 1.1s; transitions use sine easing and .65s soft exits. Opening begins partly readable, not empty.
- Inset score wells reveal separately. Scores change only while hidden at the handoff. Values are deterministic at each seek: 64/57 then 71/78. No misleading intermediate score counter.
- Same evidence carrier persists through Terminal-Bench, AutomationBench-AA and verdict. It rounds from 24px to 38px and back during the benchmark handoff; bars reveal on equal 0-100% scales over 1.4s with .15s stagger.
- Connector and small central node assemble with the panel, then fade away into the closing CTA. CTA resolves over 1.4s and holds.
- Continuous V4-derived angular dot field retained, quieter underneath the new clay/glass foreground. Lilac sphere and mint donut have small continuous drift/sway, used sparingly.

## Material

Raised soft UI surfaces plus transparent double-rim lens carriers. A separate canvas samples the live dot field with shifted coordinates and enlarged sampling into the carrier, giving an original 2D lens/refraction approximation. Moving radial highlights, pale rim shading, inner edge bands, backdrop blur and specular gradients complete the finish. It is not a physically based 3D shader or Apple's native Liquid Glass. Do not describe it as true optical refraction.

The two supplied generated clay PNGs are decorative, not representations of actual products. Their contact shadows are added locally. No Mixkit footage was used. No React Bits component code, clay.css code or proprietary Clay footage/code was copied.

## Content

Terminal-Bench 4.0: Sonnet 64%, Argon 57%. AutomationBench-AA: Sonnet 71%, Argon 78%. Different tests, different winners. Artificial Analysis, 30 Sep 2026; Sonnet Max / Argon High; Argon limited rollout. CTA: Comment "VIDEO". Source values carried from the earlier verified version; this is a motion/material revision, not a fresh benchmark investigation.

## QA

450 resolved DOM states saved before final render in frames-v8.json. Dot positions, decorative image sway, light and lens sampling are deterministic equations at each frame's time rather than every pixel being listed. Runtime and contrast checks pass. Final encoded contact sheet inspected at frames 0,60,150,255,345,435; clear settled scores, verdict and CTA, contained lockups and no clipped foreground content. Opening fade/blur is intentional. Full video decode passed. Metadata in verification.json.

Final build uses pinned Hyperframes 0.8.115 and GSAP 3.14.2 with local fonts, scripts and images. No cloud rendering, authentication, publishing or spending. Synthetic cue bed reused; no narration.

## Local rebuild

Install pinned dependencies via npm ci --ignore-scripts. Disable telemetry with HYPERFRAMES_NO_TELEMETRY=1 and DO_NOT_TRACK=1 for each Hyperframes invocation. Run check, then render at 30fps / looks quality with software browser capture and strict lint errors. Mux cues.wav with AAC at 160k, cap duration at 15s, preserve H.264 video, faststart enabled. save-frame-plan.cjs is a validation helper whose Puppeteer and Chrome paths must be adapted for a different machine. Bundled resolved state JSON can be inspected without it.

## Provenance and licences

Reference source supplied by parent: https://www.youtube.com/watch?v=y7E7ZmwEWyM . No reuse licence for its footage/code established, so only choreography and design principles informed this original build.

Source pages from earlier factual verification:
- https://artificialanalysis.ai/articles/gemini-4-argon-google-top-three-labs
- https://artificialanalysis.ai/models/gemini-4-argon
- https://www.anthropic.com/claude-sonnet-5-5
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/

Earlier dot-field technique references, not copied implementations:
- https://raw.githubusercontent.com/DavidHDev/react-bits/main/src/content/Backgrounds/DotGrid/DotGrid.jsx
- https://raw.githubusercontent.com/DavidHDev/react-bits/main/src/content/Backgrounds/Particles/Particles.jsx
- https://github.com/mrdoob/three.js/blob/9813ee76/examples/webgl_points_waves.html

Brand provenance, Anton OFL and Liberation font notices included. GSAP is under the Webflow standard licence, not Apache; retain bundled notices. Supplied clay sphere/donut PNGs were created for this work. Other supplied fleet modules were received after the original implementation was assembled; their code was not copied into this pass.
