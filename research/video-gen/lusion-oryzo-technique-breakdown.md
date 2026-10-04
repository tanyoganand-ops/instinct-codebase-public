# Lusion "Oryzo AI" - technique breakdown and 2D HTML/CSS feasibility

Site: https://oryzo.ai/ (Lusion, Awwwards SOTD 13 Apr 2026, FWA SOTD, later Site of the Month)

## Read this first: what is verified and what is inferred

- **Verified from sources:** the stack (Three.js, WebGL, GSAP), the production pipeline (Houdini, Redshift, Gaussian splats), the splat counts, the palette, and the list of Awwwards "highlight" elements.
- **Inferred:** how each highlight is built. Lusion has not published shader code or a per-effect breakdown in the parts I could read (BTS parts 1-3 of 7; later parts were not findable yet).
- **Not found in any source:** the words "prismatic borders". The Awwwards highlight list has no element by that name. If that came from watching the site, treat my border section as a reasonable guess, not a teardown.

## 1. What the site is made of (verified)

| Fact | Source |
|---|---|
| Three.js + WebGL + GSAP; tags: transitions, storytelling, 3D, filters and effects | https://www.awwwards.com/sites/oryzo-ai |
| Awwwards highlight elements: WebGL Sketches Interaction, Footer Interactive Particles, 3D -> 2D -> 3D Transition, Reveal Transition, Intro Transition, Intro Interaction, Gallery Transition | https://www.awwwards.com/sites/oryzo-ai |
| Awwwards palette: #100904 and #FF8539 (the Lusion blog says the full system is 4 colours: cream, near black, muted olive, orange; ~99% of type is one family) | Awwwards page above; https://blog.lusion.co/oryzo-bts-part-3-7-website-ux-ui-and-illustrations |
| Scenes were built in Houdini, rendered in Redshift, then converted to Gaussian splats for real-time WebGL. Image sequences and video lacked interactivity; real-time PBR was not good enough | https://blog.lusion.co/oryzo-bts-part-2-7-3d-design-and-motion-graphics |
| Full-scene splats hit ~900k and still looked flawed. Final hybrid: splats only for props and desk reflections (~78k desktop, ~45k mobile), simple texture-mapped planes for the rest | same |
| Desk and mat: orthographic top and front passes stitched in Photoshop; shader warps UV coverage so the centre 50% of the surface gets ~90% of texture detail | same |
| Design rules: realistic image, product at centre, seamless transitions, humour; as few fonts and colours as possible | Part 3 above |
| Showcase post by the dev (edankwan), tag "shaders" | https://discourse.threejs.org/t/oryzo-ai-a-wearable-product-in-the-ai-era/90696 |
| One user complaint: scroll length is exhausting | same thread |

**Core insight:** the "dense 3D feel" is mostly **pre-rendered offline 3D (Houdini/Redshift) played back as textures and a few real splats**, not live heavy 3D. The camera, lighting and material richness are baked. Live code adds scroll-driven camera, transitions, particles and sketch interactions on top.

## 2. Highlight-by-highlight: how it is likely produced, and 2D feasibility

Feasibility key: **High** = pure HTML/CSS/SVG, **Med** = needs canvas/JS or pre-rendered assets, **Low** = needs WebGL.

### a) 3D -> 2D -> 3D transition (the "organic transition")
- **Likely technique (inferred):** a full-screen shader pass blends the 3D scene render target with a flat 2D illustration texture through a noise-warped mask (organic, wobbly edge), then reverses. Standard pattern: render both to textures, `mix(a, b, smoothstep(edge, edge+w, noise(uv) + progress))`, progress driven by GSAP/scroll.
- **Open-source refs:**
  - Codrops, WebGL shader techniques for dynamic image transitions (circle with sine/cosine noise on the perimeter, smooth blend; this is the closest published match to an "organic" reveal): https://tympanus.net/codrops/2025/01/22/webgl-shader-techniques-for-dynamic-image-transitions/
  - Codrops, Three.js postprocessing transition: https://tympanus.net/codrops/2022/10/10/how-to-code-a-three-js-postprocessing-transition/
  - Codrops, grid-to-fullscreen with Three.js: https://tympanus.net/codrops/2019/05/22/creating-grid-to-fullscreen-animations-with-three-js/
  - Noise functions for the mask: https://github.com/ashima/webgl-noise
- **2D feasibility: Med-High (as an imitation).**
  - Organic mask edge in CSS: animate a `clip-path: path()` or an SVG `<mask>` whose shape is a wobbly blob; or an SVG `feTurbulence` + `feDisplacementMap` filter on the mask edge (https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feTurbulence).
  - Page-to-page version: View Transition API with a `clip-path` animation on `::view-transition-new(root)` (https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API, https://developer.mozilla.org/en-US/docs/Web/CSS/clip-path).
  - The "3D" end of the transition has to be a **pre-rendered image/video frame**, which is exactly what Lusion did upstream anyway.

### b) Intro / reveal / gallery transitions
- **Likely technique:** scroll- or time-driven GSAP timelines moving camera and planes; textured planes with displacement or mask shaders for image reveals and gallery changes.
- **Open-source refs:**
  - GSAP: https://github.com/greensock/GSAP (check the licence terms before shipping; the library is free to use but not an OSI open licence)
  - Lenis smooth scroll: https://github.com/darkroomengineering/lenis
  - Codrops, on-scroll revealing WebGL images: https://tympanus.net/codrops/2024/02/07/on-scroll-revealing-webgl-image-explorations/
  - Codrops, WebGL distortion hover effects (displacement-map technique): https://tympanus.net/codrops/2018/04/10/webgl-distortion-hover-effects/
  - Codrops, liquid distortion: https://tympanus.net/codrops/2017/10/10/liquid-distortion-effects/
  - Codrops, abstract image slideshow with OGL + GLSL + GSAP: https://tympanus.net/codrops/2021/08/16/abstract-image-carousel-ogl-glsl-gsap/
  - Lightweight WebGL lib (alternative to Three.js): https://github.com/oframe/ogl
- **2D feasibility: High** for reveals (`clip-path` inset/polygon/circle animated with GSAP or CSS scroll-driven animations), **Med** for the displacement/liquid look (SVG `feDisplacementMap` works on images but is CPU-heavy on large areas).
  - CSS scroll-driven animations: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations and https://developer.chrome.com/docs/css-ui/scroll-driven-animations (Chromium and Safari support; check Firefox status before relying on it, or use GSAP ScrollTrigger as fallback).

### c) "Rotations" / dense 3D-feeling motion
- **Likely technique:** scroll maps to a camera path through a baked scene (splats + textured planes). The depth you feel comes from parallax between layers and splat view-dependence, not from live geometry.
- **Open-source refs for the splat part:**
  - https://github.com/mkkellogg/GaussianSplats3D (Three.js viewer)
  - https://github.com/sparkjsdev/spark (Three.js splat renderer)
  - Training: LichtFeld Studio https://github.com/MrNeRF/LichtFeld-Studio (free; Lusion also used paid Postshot)
- **2D feasibility:**
  - **High:** fake depth with layered PNG/WebP cutouts and CSS 3D: `perspective` on a parent, `transform: translateZ() rotateX/Y()` per layer, driven by scroll or pointer. Items rotate in true 3D space on flat planes. This gives ~80% of the "dense" feel for objects that are flat-ish.
  - **Med:** pre-rendered turntable as an image sequence on `<canvas>` or a scrubbed video, tied to scroll. Lusion explicitly tried and rejected this for interactivity, but for a portfolio it is a legitimate 2D route to genuine 3D-looking rotation. Keep frame counts low and use WebP/AVIF.
  - **Low:** real splats or free camera movement. Needs WebGL.

### d) Prismatic / iridescent borders (unverified in sources)
- **Likely technique if it exists:** a fresnel/rainbow-ramp in a shader, or a CSS-style rotating conic gradient. I could not confirm which, or whether the site has them.
- **Open-source / free refs for the effect itself:**
  - Conic-gradient border: https://web.dev/articles/conic-gradient-border
  - Animated rotating border via `@property` (animate the gradient angle): https://developer.mozilla.org/en-US/docs/Web/CSS/@property
  - Prismatic sweep card (rainbow bar in `screen` blend mode): https://codefronts.com/motion/css-card-hover-effects/prismatic-sweep/
  - Holographic UI in pure CSS: https://hegxib.me/blog/holographic-ui-techniques and https://blog.openreplay.com/creating-holographic-effects-css/
- **2D feasibility: High.** Recipe: `background: conic-gradient(from var(--a), ...spectrum...)` on a pseudo-element, masked to a 1-2px ring (`mask-composite: exclude` or `padding` + inner background), animate `--a` registered via `@property`; add `mix-blend-mode: screen/color-dodge` and a pointer-driven highlight for the "light refracting" feel.

### e) WebGL sketches interaction and footer interactive particles
- **Likely technique:** GPU particle system (positions in float textures, updated by a fragment shader) reacting to pointer; sketch lines drawn as textured strips or a distortion pass.
- **Open-source refs:**
  - GPU particles, 1M+: https://github.com/soulwire/WebGL-GPU-Particles
  - The dev's own earlier work (same author as the Oryzo showcase post): https://github.com/edankwan/The-Spirit and https://github.com/edankwan
  - Postprocessing for glow/grain: https://github.com/pmndrs/postprocessing
- **2D feasibility:** **Med** with a 2D `<canvas>` particle system (a few thousand particles is fine on CPU; tens of thousands need WebGL or OffscreenCanvas). Pointer-reactive sketch lines: SVG paths with `stroke-dashoffset` animation (High). The "sketches come alive" distortion: Med via SVG filters, Low for true shader quality.

## 3. What makes it feel dense (and what to copy in 2D)

1. **Bake the realism.** Render in Blender/Houdini, ship images. Do not try to light things live. (Lusion Part 2.)
2. **Hybrid, not all-in.** They killed the "everything as splats" approach and used the expensive tech only where it paid off. In 2D: use rich pre-rendered assets for 2-3 hero objects, flat CSS for everything else.
3. **Spend detail where the camera looks.** Centre 50% of the surface got ~90% of texture detail. In 2D: crop and size assets to the visible region, large hero, small elsewhere.
4. **Restraint in UI.** One type family, 2-4 colours, UI stays quiet so motion carries the page. This is half of why it reads as premium.
5. **Every state change is a transition.** Their principle is "seamless transitions". Nothing cuts; elements morph, reveal or mask into the next section.
6. **Humour/personality** is an explicit design principle, not decoration.

## 4. Suggested 2D HTML/CSS pipeline (for the builder)

| Goal | Technique | Tooling |
|---|---|---|
| Fake-3D rotations | CSS 3D layers (`perspective`, `translateZ`, `rotateX/Y`), pointer + scroll driven | CSS, GSAP |
| True-looking 3D rotation | Pre-rendered image sequence on canvas, scrubbed by scroll | Blender export, WebP |
| Organic section transitions | Animated `clip-path: path()` / SVG mask with turbulence | CSS, View Transition API, GSAP |
| Prismatic borders | Conic-gradient ring, `@property` angle, blend mode | pure CSS |
| Scroll choreography | Scroll-driven animations with ScrollTrigger fallback | CSS, GSAP, Lenis |
| Particles / footer | 2D canvas particles, pointer repulsion | canvas |
| If one WebGL section is allowed | OGL plane with displacement/noise-mask shader | OGL + Codrops shaders |

**Best fit if the pipeline must stay 2D:** (1) CSS 3D layered parallax, (2) clip-path/SVG organic transitions, (3) conic-gradient prismatic borders, (4) scrubbed pre-rendered sequence for one hero rotation. Skip real splats and shader-quality distortion unless one small OGL canvas is acceptable.

## 5. Gaps and next steps

- No code for the actual transitions is public in what I found. For an exact teardown, someone would need to open oryzo.ai in browser dev tools (Network tab for shader/texture assets, Sources for the GSAP timelines). I did not do that here.
- Lusion BTS parts 4-7 may cover web development in detail. Only parts 1-3 were findable on https://blog.lusion.co/ as of today; worth re-checking.
- Lusion's earlier teardown for context: https://www.worldprogramming.org/posts/deconstructing-lusionco-how-i-reverse-engineered-the-most-awarded-webgl-site-on-the-internet-69h6t4 (not about Oryzo; not read in full).

## Source list
- https://oryzo.ai/
- https://lusion.co/projects/oryzo_ai/
- https://www.awwwards.com/sites/oryzo-ai
- https://blog.lusion.co/oryzo-bts-part-2-7-3d-design-and-motion-graphics
- https://blog.lusion.co/oryzo-bts-part-3-7-website-ux-ui-and-illustrations
- https://discourse.threejs.org/t/oryzo-ai-a-wearable-product-in-the-ai-era/90696
- https://tympanus.net/codrops/2026/04/13/lusion-where-digital-craft-meets-ambitious-experimentation/
