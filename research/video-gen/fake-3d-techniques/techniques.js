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
