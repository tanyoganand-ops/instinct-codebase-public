# Beyond parallax: practical fake-3D recipes for a 2D Shorts builder

**Prepared October 4, 2026.** The existing kit already has parallax, cached DOF, alpha-normal relighting, bilinear refraction, cast/contact shadows, and seam AO. The best next gains are (1) motion-aware mesh deformation for hero layers, (2) screen-space planar reflections, (3) baked static illumination, (4) restrained fake subsurface diffusion, (5) temporal motion blur on selected motion, and (6) clay-specific multi-scale relief. The attached Python module implements the image operations; the JS file has a Canvas triangle-mesh warp and reflection composite.

## Priority and fit

| Rank | Technique | Visual payoff | Per-frame cost | Best use |
|---|---|---:|---:|---|
| 1 | Mesh-warp pseudo-3D | High | Medium; scales with triangles | Turning cards, bending labels, squash/stretch, soft props |
| 2 | Screen-space planar reflections | High on wet/glossy planes | Medium if reflected frame changes; low if cached | Puddles, tabletops, shiny floors |
| 3 | Baked light maps | High and stable | Very low after bake | Static background, set, props, AO/light gradients |
| 4 | Fake subsurface scattering | Medium-high on edge-lit translucent forms | Medium; do once per moving subject/pose or low-res | Wax, fruit, ears, clay, soft plastic |
| 5 | Motion-blur accumulation | High for fast motion | High: N extra scene evaluations per output frame | Fast hero move, impact, whip, only short spans |
| 6 | Procedural clay normal/texture | Medium-high close-up | Low-medium; cache texture, cheaply animate phase | Stop-motion/clay look, close-up hero |

## Render-budget assumptions

A 1080x1920 RGB8 frame has 2,073,600 pixels and about 5.93 MiB of pixel data (RGBA8: 7.91 MiB). A float32 RGB image is about 23.7 MiB. One full-frame read plus write per output frame moves at least 5.56 GiB over 450 frames (RGB8), before intermediate images, filtering, encoding, or memory copies. The recipes below are deliberately cacheable and should not imply a guaranteed wall-clock time: CPU, Pillow build, browser, codec, filter radius, layer count and storage dominate. Profile on the target render machine.

Recommended budget: do spatially broad effects at 1/2 or 1/4 resolution then upscale; restrict work to the subject/surface bounding box; use RGB8/Pillow ops rather than repeatedly allocating float32 full-frame arrays; cache invariant masks, lightmaps, textures, mesh topology and noise; precompute transforms per frame; use RGBA premultiplied compositing consistently; avoid a full-frame blur for each prop. For 450 frames, a 5-sample shutter would mean up to 2,250 full-scene renders, so reserve it for a few shots or use analytic 2D trails for simple translation.

## 1. Screen-space reflections (SSR-style, without pretending to have a 3D depth buffer)

In a 2D compositor, SSR's useful idea is reusing visible scene color: copy the already-rendered scene, flip it about the plane's horizon, squash/warp it to the reflective surface, blur by roughness, tint, and fade by distance. Clip to the surface silhouette. Add subtle horizontal ripples or a low-frequency displacement map. The `planar_reflection()` helper does the flip/squash/ripple/tint/fade pass; `compositePlanarReflection()` in the JS file shows the Canvas clipping/blending pattern. Build the mirror input from visible layers only, omit particles/text that should not reflect, and render it only if its source changes.

For a screen-space ray-march variant, maintain a coarse depth/height proxy and color image. Starting at a reflective pixel, march a reflected 2D ray in screen pixels, compare ray depth against proxy depth, and sample first hit color. Step in coarse increments, binary-refine the crossing, blur by roughness, and fade at screen borders. This provides parallax-correct local hits but is fragile: anything offscreen, hidden, back-facing, transparent, or missing from the proxy cannot reflect. For graphic scenes a planar mirror often looks cleaner and is much cheaper. Fade border misses and blend toward a tinted environment gradient rather than showing black gaps. Avoid mirror-within-mirror recursion.

**Cost controls:** render reflection at 1/2 size, constrain to a surface crop, reuse each frame's visible scene, blur once at downsampled resolution. Ray march only inside a tight mask, with e.g. 12-24 coarse steps plus 2-4 refinements; this is a starting range, not a measured optimum. Reflection mask, roughness and surface geometry can be cached.

## 2. Fake subsurface scattering (SSS)

Real SSS is spatial diffusion under a surface. A cheap 2D cue is a warm, softened copy of an object's own color that blooms slightly beyond its silhouette only on the light-facing/thin edge, then is clipped back to the shape for a separate internal diffusion term. Use at least two radii (small and broad), weighted more toward small; multiply by a light-side/edge mask; keep opacity low. Premultiply color before blur and blur the alpha/mask too, then divide by blurred mask to avoid dark halos. The Python `fake_subsurface()` supplies multi-scale mask-normalized diffusion; derive a light-facing edge mask from the existing normal map or a directional mask, and composite only that region. For a warm translucent cue, set tint approximately `(1.0, .36, .22)` and tune strength down for pale objects.

Better production split: (a) blur RGB at small radius, (b) blur at broad radius, (c) use both only inside a hand-authored or normal-derived rim mask. Do not blur the whole image: it washes fine detail and bleeds across neighboring objects. A cheap one-sided red/orange rim glow is often more legible than a physically-inspired full diffusion pass.

**Cost controls:** crop to the object's bounds plus 3x the largest blur radius, process at half resolution, cache static poses; combine subject instances into one mask only when they do not overlap or require distinct material color.

## 3. Motion blur accumulation tricks

For physically plausible shutter integration, evaluate a deterministic scene at several subframe times inside the exposure and average with shutter-profile weights. `motion_blur_accumulate(render_at, frame, samples=5, shutter=.6)` does this with triangular temporal weights. Use sample timestamps centered on frame time; ensure animation interpolation is continuous and random seeds are fixed, otherwise grain flickers. Exposure length .5-.8 frame intervals is a useful starting range for stylized work; tune to the motion and frame rate.

If re-rendering is expensive, approximate by drawing a moving 2D layer at 3-5 previous/future interpolated poses into a small transparent buffer with decaying alpha, then composite once. This is especially effective for a translating prop, less accurate for rotation, occlusion changes, deformation, or highlights. Keep the static background sharp; blur only the moving layer. A directional smear/trail can also be made by drawing a downscaled layer repeatedly along its velocity vector. Never average the whole sequence's neighboring frames: that creates ghosting where object silhouettes differ and carries the wrong occlusion.

**Cost controls:** accumulation multiplies work by sample count. Apply only to moving cutouts/hero object and only during fast beats; use 3 samples first, compare with 5; reuse existing rendered layers for samples; keep DOF and blur passes after accumulation only if the order is intentional. For blur length expressed in pixels, cap by actual displacement and scene scale.

## 4. Baked light maps

Paint or generate static illumination once for fixed scenery: broad key/fill gradients, contact darkening, ambient bounce, static AO, window/light pools. Store as a grayscale or RGB map, multiply it into the base layer before moving elements. Keep dynamic highlights, cast shadows, and changing lights separate. `apply_baked_light()` multiplies an illumination map into the image with a configurable ambient floor. Make maps at quarter-size and bilinearly upscale; use RGB when warm/cool indirect light matters, grayscale for brightness-only shading.

Do not bake a shadow whose occluder moves, or a light that changes direction/intensity. Use object-local maps for props that move as a rigid unit, and scene-space maps for static sets. Add padding around atlas islands if packaging many object lightmaps to avoid bilinear seams; keep lighting textures in linear-light space if your pipeline supports it, otherwise test the contrast shift caused by sRGB multiplication.

**Cost:** essentially one texture sample/multiply per pixel per static layer at render time; bake cost happens only when scene art changes. Caching gives unusually strong return across a 450-frame shot.

## 5. Mesh-warp pseudo-3D

Treat an image as a texture and deform a grid of destination points over time: perspective turn (narrow one side), bend/sag, wave, squash/stretch, or pin a corner while moving others. Split each quad into two triangles and map source triangles affinely, clipping each draw to its destination triangle. `warp_quad()` provides inverse-homography warp for one quadrilateral in Python/Pillow; `drawImageTriangle()` and `drawWarpGrid()` provide Canvas 2D mesh mapping without WebGL. Keep UV/source grid fixed, animate destination grid with smooth curves. Add a small lighting gradient driven by local stretch/facing so the warped card is not a flat sticker.

Use 6x8 to 10x14 cells as a starting point for a hero object; more cells are not automatically better and increase draw/clip calls. Canvas 2D triangle mapping is affine within a triangle, so use enough tessellation for curvature. For sharp-edged artwork prefer perspective quad mapping, which avoids visible triangle facets. Watch for folded triangles and flipped winding; reject near-zero-area faces, preserve triangle order, and use a slight shared-edge overlap (or render a tiny seam underlay) if antialiased cracks appear. Precompute all points per output frame and crop to the object's bounding box.

## 6. Clay-specific texture and normals

A plausible stylized clay surface combines low-frequency lumpy height, smaller grain, shallow fingerprint arcs, matte broad highlights, and slight value/roughness variation. Avoid using raw high-contrast noise as color: it reads like stone. Build object-space or UV/object-local deterministic noise so texture sticks to the object; derive normals from the height gradient; use a broad, weak specular lobe rather than sharp white highlights. Sparse curved fingerprint strokes should be shallow grooves with a slight oily sheen beside them; occasional flattened Voronoi-like patches can suggest hand-smoothed clay. Keep temporal evolution quantized to a few stop-motion steps only if the desired aesthetic includes surface boil; otherwise a stable seed prevents crawling.

`clay_lighting()` creates deterministic two-scale value noise, a height-gradient fake normal, diffuse shading and a broad low-level highlight. Add a few fingerprint arcs to the heightfield for hero close-ups; cache the map and vary only its transform with the object. Use a subtle amount - too much bump/noise reads as rock or sand. The attached `joebinns/clay` example supports fingerprint dents/oily smoothness and Voronoi/Perlin shaping; Jonas Johansson's Unity write-up describes hand-made fingerprint, fur/fold, dust and grain layers.

## Integration order for a frame

1. Draw/correct static BG and apply cached lightmap.
2. Draw depth-ordered static and moving layers; mesh-warp selected hero items.
3. Add object-local clay/SSS treatment before final compositing; retain proper object masks.
4. Create reflections from chosen visible layers and clip them to planes.
5. Add dynamic cast/contact shadow and foreground occlusion.
6. Apply motion blur only to selected motion layers at exposure time; finish global grade and encoding.

This is a suggestion, not a universal stack: blur/SSS/reflection order changes the look. Test a representative hero frame plus a fast-motion frame and an occlusion boundary. Preserve deterministic seeds and inspect the encoded output for seams/flicker, not only the intermediate image.

## Evidence and caveats

The cited real-time SSR sources describe depth-buffer ray tracing, screen visibility limits, and edge/fade controls. The proposed 2D adaptation intentionally replaces 3D depth correctness with a visible-scene mirror and simple proxies. Separable SSS research supports reducing diffusion work to separable passes; the supplied PIL helper is a stylized multi-blur approximation, not that production algorithm. Accumulation references describe combining intermediate subframes across an exposure; this implementation costs multiple evaluations. Unity's lightmap documentation describes precomputed illumination stored in textures; here it is a compositing cache. Mesh warp sources cover image warping/texture mapping and triangle-based Canvas transforms. Clay examples are practitioner shader writeups, not evidence of one physically unique clay model. Runtime figures are pixel-count estimates, not a benchmark.

## Sources

- Morgan McGuire & Mike Mara, *Efficient GPU Screen-Space Ray Tracing*, Journal of Computer Graphics Techniques (2014): https://jcgt.org/published/0003/04/04/paper.pdf
- Vizrt, *Screen Space Reflection* (screen-space visibility limitations and controls): https://docs.vizrt.com/viz-artist-guide/5.1/Screen_Space_Reflection.html
- Babylon.js, *Screen Space Reflections (SSR) Rendering Pipeline*: https://doc.babylonjs.com/features/featuresDeepDive/postProcesses/SSRRenderingPipeline/
- Jimenez et al., *Separable Subsurface Scattering*: https://www.activision.com/cdn/research/Separable_Subsurface_Scattering_Expanded_Technical_Report_NEW.pdf
- Jimenez et al., *Screen-Space Perceptual Rendering of Human Skin*: https://iryoku.com/sssss/
- Unity Recorder, *Accumulate motion blur*: https://docs.unity3d.com/Packages/com.unity.recorder%405.1/manual/RecordingAccumulationMotionBlur.html
- Unity HDRP, *Understand multiframe rendering and accumulation*: https://docs.unity3d.com/Packages/com.unity.render-pipelines-high-definition%4017.5/manual/rendering-understand-multiframe-rendering.html
- Unity, *Introduction to Lightmap UVs*: https://docs.unity3d.com/6000.4/Documentation/Manual/LightingGiUvs.html
- Paul Bourke, *Mesh format for image warping*: https://paulbourke.org/dataformats/meshwarp/
- T. Ullrich, *Perspective-correct texturing using HTML5 Canvas*: https://tulrich.com/geekstuff/canvas/perspective.html
- Jan Vai, *Warping an image across a deformable mesh in plain Canvas 2D*: https://dev.to/janvai/warping-an-image-across-a-deformable-mesh-in-plain-canvas-2d-no-webgl-44j9
- CMU, *Fundamentals of Texture Mapping and Image Warping*: https://www.cs.cmu.edu/~ph/texfund/texfund.pdf
- Joe Binns, *clay* shader example (fingerprints, Voronoi and Perlin): https://github.com/joebinns/clay
- Jonas Johansson, *Clay Material in Unity*: https://www.jonasjohansson.dev/blog/clay-material-in-unity/
- Pillow docs, `Image.transform`: https://pillow.readthedocs.io/en/stable/reference/Image.html?highlight=image.transform
