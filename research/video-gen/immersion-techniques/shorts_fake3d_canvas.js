/* Canvas 2D helper: draw one source-image triangle into a destination triangle.
   Use a regular grid (e.g. 8x12 cells) for pseudo-3D cards/fabric/soft props.
   Points are [x,y] arrays in source-image and canvas pixel coordinates. */
function drawImageTriangle(ctx, image, s0, s1, s2, d0, d1, d2) {
  const [x0,y0]=s0, [x1,y1]=s1, [x2,y2]=s2;
  const [u0,v0]=d0, [u1,v1]=d1, [u2,v2]=d2;
  const det=x0*(y1-y2)+x1*(y2-y0)+x2*(y0-y1);
  if (Math.abs(det) < 1e-8) return; // collapsed/degenerate triangle
  const a=(u0*(y1-y2)+u1*(y2-y0)+u2*(y0-y1))/det;
  const c=(u0*(x2-x1)+u1*(x0-x2)+u2*(x1-x0))/det;
  const e=(u0*(x1*y2-x2*y1)+u1*(x2*y0-x0*y2)+u2*(x0*y1-x1*y0))/det;
  const b=(v0*(y1-y2)+v1*(y2-y0)+v2*(y0-y1))/det;
  const d=(v0*(x2-x1)+v1*(x0-x2)+v2*(x1-x0))/det;
  const f=(v0*(x1*y2-x2*y1)+v1*(x2*y0-x0*y2)+v2*(x0*y1-x1*y0))/det;
  ctx.save();
  ctx.beginPath(); ctx.moveTo(u0,v0); ctx.lineTo(u1,v1); ctx.lineTo(u2,v2); ctx.closePath(); ctx.clip();
  ctx.transform(a,b,c,d,e,f);
  ctx.drawImage(image,0,0);
  ctx.restore();
}

/* Call for each cell's two triangles; src grid coordinates use image pixels.
   Add a 0.3-0.6px overlap/edge expansion to hide antialias seams if required. */
function drawWarpGrid(ctx, image, srcGrid, dstGrid) {
  const rows=srcGrid.length-1, cols=srcGrid[0].length-1;
  for(let y=0;y<rows;y++) for(let x=0;x<cols;x++) {
    const s00=srcGrid[y][x], s10=srcGrid[y][x+1];
    const s01=srcGrid[y+1][x], s11=srcGrid[y+1][x+1];
    const d00=dstGrid[y][x], d10=dstGrid[y][x+1];
    const d01=dstGrid[y+1][x], d11=dstGrid[y+1][x+1];
    drawImageTriangle(ctx,image,s00,s10,s11,d00,d10,d11);
    drawImageTriangle(ctx,image,s00,s11,s01,d00,d11,d01);
  }
}

/* Screen-space planar fake reflection: mirror the already rendered scene above
   a horizon into a pre-sized offscreen canvas (mirrorCanvas), then clip it to
   the surface and blend. Capture once per frame only when the reflected scene
   changes; animate a small displacement map/ripple texture for water. */
function compositePlanarReflection(ctx, mirrorCanvas, surfacePath, alpha=0.32, blurPx=1) {
  ctx.save();
  ctx.clip(surfacePath);
  ctx.globalAlpha=alpha;
  ctx.filter=`blur(${blurPx}px)`;
  ctx.drawImage(mirrorCanvas,0,0);
  ctx.filter='none';
  ctx.restore();
}
