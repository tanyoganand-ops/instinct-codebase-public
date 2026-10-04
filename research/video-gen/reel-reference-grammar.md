# Reel reference grammar

Style grammar decoded from a reference Instagram reel (DdyCdl5iToA): a screen recording of an X post by mexicat, "Somebody built this using Opus 5.5". Decoded 3 October 2026 from the user's reel. Style reference only, not a template to copy.

## Palette

- Near-black ground with a faint blueprint grid.
- One burnt-orange/amber accent plus white. Nothing else.
- No screen-wide gradients.
- Soft orange bloom around bright elements.

## Type

- Huge, bold, tight grotesk sans in white or orange. Oversized, partly cropped, bleeding off frame or running behind objects.
- Monospace for terminal and HUD text, typed with a caret, with an orange highlight on key words.
- Small mono HUD labels, axes and ticks used as texture.

## Type behaviour

- Word-by-word or typewriter reveals.
- Line swaps per beat.
- Text wraps around 3D shapes.
- Text sits inside the scene, in depth and behind objects, rather than as an overlay.

## Scenes

- One hero element per roughly 2-10 seconds: line-art diagrams, wireframe objects, contour ripples, ring tunnels, matte 3D shapes, forms, mazes.
- Lots of dark negative space.

## Motion

- Continuous camera moves (push-in, orbit, pan), not hard cuts.
- Line art draws on with a glowing lead point.
- Elements enter by drawing or typing, not sliding.
- Scenes change by morph or camera move.

## Application for the Short

Dark ground, one accent, very bold oversized type running behind and through line-art waves, a glowing lead point, typewriter and word reveals, small mono HUD details, and a slow camera push.


## Anti-patterns - 20 vibecoded tells (reel DcrqbqZRVvC, @millee.md)

Context: the user has deliberately chosen to keep liquid glass and the shifting gradient for the current Short despite items 1, 6 and 20. His direction overrides the list for that Short. Everything else on the list is to be avoided in all video and site work.

1. Purple-to-blue gradient
2. Gradient hero text
3. Emojis in headings
4. Inter font everywhere
5. Colored border cards
6. Glassmorphism cards
7. Low-contrast dark mode
8. 3 icon boxes in a row
9. Badge above the headline
10. Lucide icons everywhere
11. Untouched shadcn UI
12. Fade-in on scroll
13. Cursor-following beam
14. Buttons fade on hover
15. Inconsistent spacing
16. Em dashes everywhere
17. Generic buzzword copy
18. Serif italic accents
19. Space Grotesk + Instrument Serif
20. Grain over a gradient


## Further reel references (2026-10-03, evening)

- Reel DcyeD8wpNfh (@set_angle, 30s): an After Effects circular track-matte transition tutorial. Recipe: two solid-colour layers, keyframe a circle's opacity, duplicate circles to fill the screen, precompose, track-matte the second background, add a fast box blur. Demo style: forest green and bright red, white condensed sans subtitles in black backplates, brisk procedural pacing. Technique reference only.
- Reel DdzuazdMxvU (@benkaluza.lab, 15s, labelled AI-generated): an AI motion-graphics experiment made with Claude Opus 5.5 and Hyperframes. A single point of light draws a human-evolution storyline. Thin luminous outlines (cyan-white and warm amber) on near-black charcoal, glossy wet-floor reflections, haze and bloom, lateral camera tracking, particle sparks, a slow dreamy chronological reveal, and stable title and prompt text over a narrow cinematic band. Same draw-on-with-glowing-lead-point family as the mexicat reel, but darker and more cinematic. Awaiting the user's decision on whether it feeds the next Short version.


## Hyperframes repo (2026-10-03)

The tool behind the benkaluza.lab reel is Hyperframes by HeyGen: https://github.com/heygen-com/hyperframes (Apache-2.0, about 56k stars). Docs: https://hyperframes.heygen.com/introduction

- What it does: HTML/CSS plus seekable animation (GSAP, Lottie, Three.js), rendered to deterministic MP4 via headless Chrome and FFmpeg.
- Needs: Node 22+ and FFmpeg.
- CLI: `npx hyperframes init`, `lint`, `preview`, `render`.

Reusable for the user's pipeline:

- The /skills folder: 21 agent skills, including hyperframes-animation, hyperframes-keyframes (SVG draw and morph), faceless-explainer and embedded-captions.
- The renderer CLI (data-width 1080, data-height 1920).
- packages/shader-transitions.
- packages/lint (seekability checks).
- The DESIGN.md-to-video-spec pattern.

Caveats:

- Animation must be seek-driven. His scenes already are.
- GSAP is loaded from a CDN and has its own licence (unverified).
- The benkaluza reel's actual prompts are not published.
