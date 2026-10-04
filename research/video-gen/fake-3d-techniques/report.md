# Fake 3D for a clay-style 2D Short

Research and implementation notes, 4 October 2026.

The strongest quick upgrade is a coherent stack: convex relighting, floor contact shadows, restrained layered camera motion, then mild depth of field. Add seam darkening only at actual contacts. Keep refraction for a glass, liquid or heat-effect shot; it does not improve opaque clay. The examples below are original implementation recipes, not code copied from the linked sources. All numeric presets are art-direction starting points, not benchmark results or physically measured parameters.

## What to implement first

| Order | Technique | What it changes | Cost and limit |
|---|---|---|---|
| 1 | Contact + cast shadows | Stops characters looking like stickers floating over the floor | Cache alpha mask; draw under subject, over receiver. Flat-floor approximation |
| 2 | Sprite normals + matte light | Makes a flat silhouette read as a rounded clay volume | Bake once for a static light; cannot recover hidden geometry |
| 3 | Layered perspective | Gives camera travel real depth ordering | Cheap draw transforms; needs separated layers and overscan |
| 4 | Depth-of-field sprites | Separates the subject from the set | Pre-bake a few blur levels; platform-check Canvas filter |
| 5 | Local seam AO | Makes hands, feet and overlapping forms feel joined | Hand-place contacts; this is artistic AO, not SSAO |
| 6 | Refraction displacement | Adds visible glass/liquid distortion | CPU example is for small patches or offline rendering; move to WebGL for large animated passes |

## Assumptions and conventions

- Assets are decoded images or canvases with transparency. Helper functions assume same-origin images or images fetched with valid CORS permission. Cross-origin canvas readback can throw `SecurityError` [S3].
- All dimensions, translations, blur radii and heights in the code are canvas backing-store pixels. At 2x output size, scale relevant pixel constants by 2. Do not mix CSS dimensions with backing-store coordinates.
- Canvas x points right, y points down, and our synthetic surface z points toward the viewer. Light `[-0.45, -0.65, 0.8]` is top-left and in front of the sprite.
- This is 2.5D: scale, translation and lighting can change, but a large head turn still needs another pose or actual geometry. It does not expose the side of a sprite.
- Matte clay means broad weak highlights and soft shadows. Never bake moving random noise into every frame. Lock any clay surface texture to the object.

## Shared helpers

Paste these once before the technique functions. The complete assembled code is also attached as `techniques.js`.

```js
// Canvas 2D fake-3D kit. Coordinates are backing-store pixels, not CSS pixels.
const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
function surface(w, h) {
  const c = document.createElement('canvas');
  c.width = w; c.height = h; return c;
}
function pixels(img) {
  const c = surface(img.naturalWidth || img.width, img.naturalHeight || img.height);
  const g = c.getContext('2d', {willReadFrequently: true});
  g.drawImage(img, 0, 0);
  return {canvas: c, ctx: g, data: g.getImageData(0, 0, c.width, c.height)};
}

```

## 1. Layered parallax rates and perspective

Use inverse-distance scaling instead of arbitrarily sliding every layer by nearly the same amount. `scale = focal / depth` controls both apparent size and movement under camera translation. Camera x increasing moves the scene left. Draw larger z (farther layers) first.

With `focal=600` and camera z=0, these **calculated** rates are:

| Plane | z | Motion rate / size scale |
|---|---:|---:|
| Foreground | -100 | 1.20 |
| Main subject | 0 | 1.00 |
| Mid-background | 600 | 0.50 |
| Far set | 1800 | 0.25 |
| Distant backdrop | 5400 | 0.10 |

Example art direction: a camera travel of 12 output pixels yields foreground travel 14.4, subject 12, mid-background 6, far set 3, backdrop 1.2 pixels. Supply enough overscan to hide those shifts plus blur padding. Keep subtitles in a separate screen-space pass. Keep camera z well short of `focal + nearestLayer.z`; the clamp in the example is defensive, not a valid near-plane solution.

This is geometric camera parallax, not the UV height-map parallax mapping described in [S7]. Do not conflate the two.

```js
// 1. Perspective-correct layered parallax. Camera units match x,y,z units.
function projectLayer(layer, camera, W, H, focal = 600) {
  const depth = Math.max(1, focal + layer.z - (camera.z || 0));
  const scale = focal / depth;
  return {
    x: W / 2 + (layer.x - camera.x) * scale,
    y: H / 2 + (layer.y - camera.y) * scale,
    scale
  };
}
function drawLayers(ctx, layers, camera, W, H, focal = 600) {
  // z positive is farther away; farther layers draw first.
  for (const l of [...layers].sort((a, b) => b.z - a.z)) {
    const p = projectLayer(l, camera, W, H, focal);
    const w = l.image.width * p.scale, h = l.image.height * p.scale;
    ctx.drawImage(l.image, p.x - w / 2, p.y - h / 2, w, h);
  }
}

```

Call with layers `{image, x, y, z}`. x/y are world offsets from the centre of the frame, and images are centre-anchored. Animate the camera using a deterministic timeline, for example `{x: 12*Math.sin(t*0.35), y: 3*Math.sin(t*0.27), z: 0}`. Avoid independent layer drift unless an object itself is moving.

## 2. Depth-of-field blur recipes

Our blur law is an artistic approximation using relative distance from the focus plane. It is not an optical circle-of-confusion calculation. At a 1080-pixel output width, try sigma 0 for the hero, 2-4 for a mid set, 5-8 for the far set, and 8-12 for a very close foreground edge. Keep eyes, product details and subtitles sharp. For rack focus, interpolate `focus`, not the camera position.

Canvas `blur()` is Gaussian, and the argument is its standard deviation [S1]. Three-sigma padding is a practical cutoff, not an exact finite boundary. Blur each whole sprite or layer, including alpha. Draw blurred far layers before sharp near layers.

```js
// 2. Depth of field: a deliberately art-directed blur, not a lens simulator.
function blurSigma(depth, focus, strength = 18, maxSigma = 12) {
  return Math.min(maxSigma, strength * Math.abs(depth - focus) / Math.max(depth, 1));
}
function blurSprite(image, sigma) {
  // Three standard deviations of padding on every side limits cropped blur.
  const pad = Math.ceil(3 * sigma) + 2;
  const out = surface(image.width + pad * 2, image.height + pad * 2);
  const g = out.getContext('2d');
  g.filter = `blur(${sigma}px)`;
  g.drawImage(image, pad, pad); // Image must be decoded first.
  g.filter = 'none';
  return {image: out, pad};
}
function drawDOFSprite(ctx, cached, x, y, scale = 1) {
  ctx.drawImage(cached.image, x - cached.pad * scale, y - cached.pad * scale,
    cached.image.width * scale, cached.image.height * scale);
}
// Cache blurSprite(image, quantizedSigma) by image ID + sigma, not per frame.

```

Use positive `depth = focal + layer.z - camera.z` and the matching positive focus depth. Quantize sigma to steps of 0.5-1 pixels and cache variants. `drawDOFSprite` x/y denote the original unpadded sprite's top-left. Do not place the padding as if it were the sprite's origin.

**Compatibility:** MDN marks `CanvasRenderingContext2D.filter` as limited availability [S1]. Test the actual export browser. A property-presence test alone is not enough. If blur rendering fails, use pre-rendered PNG blur variants or a WebGL Gaussian pass. Never silently produce a sharp layer when blur is required. Our demo verified the filter path in headless Chrome only.

## 3. Normal-map-style shading from one sprite

A transparent sprite does not contain enough information to identify its real 3D shape. This recipe invents a convex bevel using distance to the alpha boundary, smooths that height field, differentiates it into normals, then applies diffuse and weak broad specular lighting. Normal mapping changes per-pixel lighting without changing geometry [S5].

Distance-to-edge avoids turning dark painted facial features into pits, which happens if brightness is naively interpreted as height. It still cannot distinguish separate overlapping volumes inside one silhouette. Split head, arms, body and feet into their own sprites for better results. Use `radius` around 25-45% of a part's short dimension; start with height 15-30% of that radius.

The Gaussian smoothing step is important: the first visual test showed spoke-like ridges in raw chamfer-distance gradients. Smoothing before differentiation removed those strong ridges in the final inspection.

```js
// 3. Approximate convex height/normal field from a single transparent sprite.
// No albedo luminance is used: dark painted eyes should not become cavities.
function spriteNormals(image, {radius = 36, height = 24} = {}) {
  const {data} = pixels(image), w = data.width, h = data.height;
  const d = new Float32Array(w * h);
  let H = new Float32Array(w * h);
  const normals = new Float32Array(w * h * 3);
  const inside = i => data.data[i * 4 + 3] >= 128;
  // Two-pass chamfer distance to transparency. Border is treated as outside.
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
    const i = y * w + x;
    d[i] = !inside(i) ? 0 : (x === 0 || y === 0 || x === w-1 || y === h-1 ? 1 : 1e6);
  }
  const relax = (x,y, dx,dy, cost) => {
    const i=y*w+x, xx=x+dx, yy=y+dy;
    if(xx>=0 && xx<w && yy>=0 && yy<h) d[i]=Math.min(d[i], d[yy*w+xx]+cost);
  };
  for(let y=0;y<h;y++) for(let x=0;x<w;x++) {
    relax(x,y,-1,0,1); relax(x,y,0,-1,1);
    relax(x,y,-1,-1,Math.SQRT2); relax(x,y,1,-1,Math.SQRT2);
  }
  for(let y=h-1;y>=0;y--) for(let x=w-1;x>=0;x--) {
    relax(x,y,1,0,1); relax(x,y,0,1,1);
    relax(x,y,1,1,Math.SQRT2); relax(x,y,-1,1,Math.SQRT2);
  }
  for(let i=0;i<d.length;i++) {
    const t=clamp(d[i]/radius,0,1);
    H[i]=height*Math.sqrt(Math.max(0,1-(1-t)*(1-t)));
  }
  // Smooth before differentiation: raw distance gradients create chamfer spokes.
  const sigma=3, r=9, kernel=[];
  for(let k=-r;k<=r;k++) kernel.push(Math.exp(-k*k/(2*sigma*sigma)));
  const total=kernel.reduce((a,b)=>a+b,0);
  for(let k=0;k<kernel.length;k++) kernel[k]/=total;
  const tmp=new Float32Array(w*h), smooth=new Float32Array(w*h);
  for(let y=0;y<h;y++) for(let x=0;x<w;x++) {
    let v=0;for(let k=-r;k<=r;k++) v+=H[y*w+clamp(x+k,0,w-1)]*kernel[k+r];
    tmp[y*w+x]=v;
  }
  for(let y=0;y<h;y++) for(let x=0;x<w;x++) {
    let v=0;for(let k=-r;k<=r;k++) v+=tmp[clamp(y+k,0,h-1)*w+x]*kernel[k+r];
    smooth[y*w+x]=v;
  }
  H=smooth;
  const at=(x,y)=>H[clamp(y,0,h-1)*w+clamp(x,0,w-1)];
  for(let y=0;y<h;y++) for(let x=0;x<w;x++) {
    const i=y*w+x;
    const nx=-(at(x+1,y)-at(x-1,y))/2;
    const ny=-(at(x,y+1)-at(x,y-1))/2;
    const len=Math.hypot(nx,ny,1);
    normals.set([nx/len,ny/len,1/len],i*3);
  }
  return {w,h,albedo:data,normals,height:H};
}
function shadeSprite(field, light = [-0.45,-0.65,0.8]) {
  const {w,h,albedo,normals}=field, out=surface(w,h), g=out.getContext('2d');
  const result=g.createImageData(w,h);
  const n=Math.hypot(...light), L=light.map(v=>v/n);
  const hn=Math.hypot(L[0],L[1],L[2]+1), half=[L[0]/hn,L[1]/hn,(L[2]+1)/hn];
  for(let i=0;i<w*h;i++) {
    const j=i*3, a=i*4;
    const diffuse=Math.max(0,normals[j]*L[0]+normals[j+1]*L[1]+normals[j+2]*L[2]);
    const ndh=Math.max(0,normals[j]*half[0]+normals[j+1]*half[1]+normals[j+2]*half[2]);
    // Matte clay: broad weak highlight, never a sharp white plastic spot.
    const gain=0.50+0.50*diffuse, spec=12*Math.pow(ndh,10);
    for(let c=0;c<3;c++) result.data[a+c]=clamp(albedo.data[a+c]*gain+spec,0,255);
    result.data[a+3]=albedo.data[a+3];
  }
  g.putImageData(result,0,0); return out;
}

```

Usage: `const field=spriteNormals(sprite,{radius:62,height:30}); const lit=shadeSprite(field);` Both values are pixels. Cache `field` per asset. For a static key light, cache `lit` too. Move dynamic shading to the GPU if many large assets relight every frame. The simple CPU shader works in stored color values rather than a linear-light pipeline; it is suitable for stylized previews, not colorimetric production rendering.

Optional fine clay texture: derive a weak additional normal perturbation from an object-space height texture, then renormalize. Keep perturbation very small compared with the macro shape. Do not use frame-dependent noise or let texture swim during camera motion.

## 4. Displacement/refraction sampling

Capture an opaque background first, then sample it at a small offset derived from the synthetic surface normal. Bilinear sampling avoids nearest-neighbour steps. The alpha silhouette supplies coverage, not physical glass transmission. `strength` is displacement in background pixels; start at 3-8 pixels at 1080-wide output, and increase only if the shot needs obvious distortion.

```js
// 4. CPU refraction: transparent foreground mask + normal-driven background warp.
// Input background must be opaque. Use a low-resolution patch for animation.
function refractPatch(background, field, left, top, strength = 8, tint = [0.92,0.98,1]) {
  const bg=pixels(background).data, {w,h,normals,albedo}=field;
  const out=surface(w,h), g=out.getContext('2d'), dst=g.createImageData(w,h);
  function sample(x,y,c) {
    x=clamp(x,0,bg.width-1); y=clamp(y,0,bg.height-1);
    const x0=Math.floor(x), y0=Math.floor(y), x1=Math.min(x0+1,bg.width-1), y1=Math.min(y0+1,bg.height-1);
    const fx=x-x0, fy=y-y0, p=(xx,yy)=>bg.data[(yy*bg.width+xx)*4+c];
    return (1-fy)*((1-fx)*p(x0,y0)+fx*p(x1,y0))+fy*((1-fx)*p(x0,y1)+fx*p(x1,y1));
  }
  for(let y=0;y<h;y++) for(let x=0;x<w;x++) {
    const i=y*w+x, j=i*3, a=i*4;
    const coverage=albedo.data[a+3]/255;
    for(let c=0;c<3;c++) dst.data[a+c]=sample(left+x+normals[j]*strength,top+y+normals[j+1]*strength,c)*tint[c];
    dst.data[a+3]=coverage*255;
  }
  g.putImageData(dst,0,0); return out;
}
// Snapshot background BEFORE drawing the refractor. Never sample the prior output.

```

Call `refractPatch(background, field, left, top, strength)` and draw the returned patch at the same left/top. `field` and patch use a 1:1 pixel scale; if the refractor is scaled or rotated, resample the field and transform the displacement direction too. Clamp sampling prevents out-of-bounds reads but can smear the edges; capture an oversized background patch if the object is near a boundary.

Never feed the prior composited frame back into this pass. That creates feedback smearing rather than stable refraction. The background passed here must be opaque; transparent backgrounds need premultiplied-alpha interpolation. The shader-friendly equivalent is `uvWarped = uv + normal.xy * strengthPixels / textureSize`. Texture sampling, pixel-size offsets and edge clamping are documented in [S9]. Avoid sampling from a texture currently bound as the render target.

For heat haze, substitute smooth object-locked sinusoidal offsets, such as `dx=2*Math.sin(y*0.04+t*1.2)` and `dy=0.5*Math.sin(x*0.03+t)`, then fade them with a soft plume mask. Keep the CPU pass to a small region or offline frames. No mobile frame-rate claim has been established.

## 5. Cast shadows and contact shadows

Use two layers. The projected alpha silhouette is the directionally cast shadow; a smaller darker elliptical patch directly under the feet is the contact shadow. Blur and lighten the cast shadow as the subject rises. Fade or remove the contact patch when a foot loses contact.

```js
// 5. Alpha-silhouette cast shadow and a separate contact shadow.
function shadowMask(sprite, color = '#392a30') {
  const c=surface(sprite.width,sprite.height), g=c.getContext('2d');
  g.drawImage(sprite,0,0);
  g.globalCompositeOperation='source-in';
  g.fillStyle=color; g.fillRect(0,0,c.width,c.height);
  g.globalCompositeOperation='source-over'; return c;
}
function castShadow(ctx, mask, footX, footY, {height=0, lean=0.45, squash=0.25}={}) {
  ctx.save(); ctx.globalCompositeOperation='multiply';
  ctx.globalAlpha=0.26*Math.exp(-height/90);
  ctx.translate(footX+height*0.7,footY+height*0.25);
  // Sprite bottom centre lands at the foot; upper parts project along the floor.
  ctx.transform(1,0,-lean,-squash,0,0);
  ctx.filter=`blur(${3+height*0.08}px)`;
  ctx.drawImage(mask,-mask.width/2,-mask.height);
  ctx.restore();
}
function contactShadow(ctx, x, y, rx=38, ry=10, opacity=0.30) {
  ctx.save(); ctx.globalCompositeOperation='multiply';
  ctx.translate(x,y); ctx.scale(rx,ry);
  const grad=ctx.createRadialGradient(0,0,0,0,0,1);
  grad.addColorStop(0,`rgba(42,29,35,${opacity})`);
  grad.addColorStop(0.4,`rgba(42,29,35,${opacity*0.6})`);
  grad.addColorStop(1,'rgba(42,29,35,0)');
  ctx.fillStyle=grad; ctx.fillRect(-1,-1,2,2); ctx.restore();
}

```

Draw order: floor receiver, cast shadow, contact shadow, character, foreground. Only apply floor shadows inside the floor's mask, if it does not cover the whole frame. A shadow must not darken a wall or foreground object accidentally. The cast-shadow helper assumes the asset's foot is at the bottom-centre of its canvas; trim transparent bottom padding or pass a corrected origin. Pair the shadow's lean/offset direction with the key light direction. Our top-left key projects shadows generally right/down.

These affine projections do not compute occlusion or true lighting. Real shadow mapping uses a light-space depth map and a later depth comparison [S8]. This shortcut is for a flat floor, not curved receivers or shadows cast around corners.

## 6. Ambient-occlusion/contact recipes

Ambient occlusion darkens regions with blocked ambient light; real SSAO samples a geometry/depth-derived neighbourhood [S6]. Here we place small soft stamps at known contact points, clip them to the receiver, then multiply over the receiver. This is art-directed seam darkening, not SSAO.

Good placements: wrist on torso, fingers around a held object, underside of a chin, sole on floor, rim/body joint of a clay bowl. Bad placement: a dark outline around the entire sprite, which reads as a cutout. Use a long thin stamp for a seam, a compact stamp for a grip, and a floor ellipse for a planted foot. Remove the stamp when pieces separate.

```js
// 6. Artistic AO: local soft darkening where pieces touch, clipped to the receiver.
// This is not SSAO: there is no depth buffer, visibility test or geometry.
function seamAO(receiver, stamps) {
  const ao=surface(receiver.width,receiver.height), g=ao.getContext('2d');
  for(const s of stamps) {
    g.save(); g.translate(s.x,s.y); g.rotate(s.angle || 0); g.scale(s.rx,s.ry);
    const grad=g.createRadialGradient(0,0,0,0,0,1);
    grad.addColorStop(0,`rgba(39,28,31,${s.opacity ?? 0.18})`);
    grad.addColorStop(1,'rgba(39,28,31,0)');
    g.fillStyle=grad; g.fillRect(-1,-1,2,2); g.restore();
  }
  g.globalCompositeOperation='destination-in'; g.drawImage(receiver,0,0);
  const out=surface(receiver.width,receiver.height), o=out.getContext('2d');
  o.drawImage(receiver,0,0); o.globalCompositeOperation='multiply'; o.drawImage(ao,0,0);
  return out;
}
```

`stamps` use receiver-local pixel coordinates: `{x:76,y:139,rx:32,ry:9,opacity:0.18,angle:0}`. Start with opacity 0.10-0.22. AO and directional shadows should not simply add into a black seam. Inspect at the actual phone viewing size and reduce opacity if the expression or silhouette gets dirty.

## Integration checklist

1. Separate background, floor, hero parts and foreground. Record alpha bounds and foot anchors.
2. Choose one key-light direction for all sprites and shadows.
3. Cache normal fields, static relighting, silhouette masks, blur variants and static AO.
4. Render background far-to-near, receiver floor, its shadows, hero parts with their seam AO, foreground. Keep captions out of the DOF pass.
5. For transparent objects, snapshot only the background visible behind them and apply refraction before foreground overlays.
6. Render from explicit `t=frameIndex/fps` rather than wall-clock time for repeatable exports. Do not tie animation quality to variable live frame duration.
7. Check transparent edge halos, texture stability, shadow-foot alignment, blur clipping and camera overscan in representative first/middle/last frames.
8. Validate the final Short separately. This kit was tested against a procedural synthetic sprite, not the user's existing video or assets.

## Verification performed

- `node --check techniques.js` passed.
- Six Canvas recipes executed in headless Chrome using the attached self-contained demo and script.
- Assertions passed for inverse-depth projection scales, zero blur at focus, finite/unit-length normals and zero-strength refraction matching the source background at fully covered pixels.
- Visually inspected the actual 1040x930 screenshot. The first render exposed chamfer spokes; the height field was smoothed and the second render was inspected. Final panels show a rounded relit sprite, floor shadow/contact, foreground/background focus separation, warped stripe sampling and perspective layer sizing.
- No target-device performance benchmark, WebGL host integration, real-asset QA or finished-video inspection was performed.

## Sources and what they support

These are nine fetched technical sources across API documentation and independent graphics tutorials. There was no useful third source type required for these API/geometry claims. Sources support the underlying mechanics, not our artistic numeric presets or the exact original implementation.

- **S1. MDN, CanvasRenderingContext2D.filter.** Gaussian blur semantics and compatibility caveat. https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/filter
- **S2. MDN, globalCompositeOperation.** `source-in`, `destination-in`, `multiply` and other blend/mask operations. https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/globalCompositeOperation
- **S3. MDN, getImageData.** Pixel readback and cross-origin `SecurityError`. https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/getImageData
- **S4. MDN, Compositing and clipping.** Restricting draws to masks/clip regions. https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Compositing
- **S5. LearnOpenGL, Normal Mapping.** Per-fragment normals change surface lighting without changing the mesh; RGB normal encoding. https://learnopengl.com/Advanced-Lighting/Normal-Mapping
- **S6. LearnOpenGL, SSAO.** Geometry/depth-derived ambient visibility approximation, distinct from painted darkening. https://learnopengl.com/Advanced-Lighting/SSAO
- **S7. LearnOpenGL, Parallax Mapping.** Height-map-based texture-coordinate displacement, distinct from moving depth layers. https://learnopengl.com/Advanced-Lighting/Parallax-Mapping
- **S8. LearnOpenGL, Shadow Mapping.** Light-space depth-map shadow comparison and limitations. https://learnopengl.com/Advanced-Lighting/Shadows/Shadow-Mapping
- **S9. WebGL Fundamentals, WebGL Image Processing.** Texture sampling, pixel-size offsets, convolution and `CLAMP_TO_EDGE`. https://webglfundamentals.org/webgl/lessons/webgl-image-processing.html

All URLs were discovered through search and fetched successfully on 4 October 2026. Source content dates were not consistently exposed; freshness here means fetched on this date, not recently published.
