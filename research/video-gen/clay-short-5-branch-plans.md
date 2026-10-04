# Clay Short, 15 s, 5 branch scene plans
Sonnet 5.5 Max vs Gemini 4 Argon High. 450 frames at 30 fps.

## Shared facts and constraints (all branches)
- Terminal-Bench 4.0: Sonnet 64, Gemini 57. Sonnet leads.
- AutomationBench-AA: Sonnet 71, Gemini 78. Gemini leads.
- Verdict text: DIFFERENT TESTS. DIFFERENT WINNERS.
- CTA text: COMMENT VIDEO
- Source rail (constant, every frame): Artificial Analysis - 30 Sep 2026 / Sonnet Max / Argon High
- Safe rect: x48-888, y288-1248 (840 x 960). All text and key objects inside it.
- Type floors (px) as given: 48 / 56 / 72 / 64. Assumed mapping: rail 48, labels 56, score numbers 72, verdict and CTA 64 (stacked on 2 lines). Confirm the mapping against the design MD.
- Beat grid (same in all branches so branches are comparable):
  B1 0.0-2.0 s (f0-60) hook
  B2 2.0-4.5 s (f60-135) benchmark 1 setup
  B3 4.5-7.5 s (f135-225) benchmark 1 result 64/57
  B4 7.5-10.5 s (f225-315) benchmark 2 result 71/78
  B5 10.5-13.0 s (f315-390) verdict
  B6 13.0-15.0 s (f390-450) CTA, loop-ready
- Rules from P's steer: one hero visual + one line of text per scene; swipe left/right or drop-down entrances only (no fly/zoom); light/white background with moving colour gradient; Anton font; liquid glass; background motion visible and behind the text; no purple-blue gradient, no gradient hero text; use Claude and Gemini logos.

---

## 1. Liquid depth (content-layer parallax stacks, DOF racks)
Idea: the scene is 3 to 4 flat clay/glass layers at different depths. Layers slide at different speeds; focus racks between them.
Layers: L0 gradient wall (far, always blurred), L1 logos/bars (mid), L2 numbers/text (near, always sharp), L3 floating clay crumbs (nearest, blurred, drifting).
- B1 hook: L0 gradient drifts left. L1 shows both logos as clay discs, swipe in from sides. L2 text "WHO WINS?" drops down. Focus on L2.
- B2: Rack focus L2 to L1. Text swaps to "TERMINAL-BENCH 4.0". Logos separate left/right, L1 parallax 2x L0.
- B3: Two clay bars grow up from the L1 floor. Numbers 64 / 57 on L2 count up. Sonnet bar taller, glass highlight sweeps across it.
- B4: Layers swipe left as a block (parallax stagger). New bars for "AUTOMATIONBENCH-AA": 71 / 78. Gemini taller. Rack focus lands on 78.
- B5: Both bar sets slide back to L0 and blur. L2 drops down verdict on 2 lines, sharp.
- B6: Verdict shrinks up to the top of the rect. "COMMENT VIDEO" drops in at y~900, pill glass button breathes. Crumbs drift.
Moves: layers, focus plane, bars, crumbs. Constant: rail, gradient wall, logo pair (shrunk at B5/B6).
Layout: title y288-380, hero zone y400-1000, numbers y1000-1100, verdict/CTA y1120-1248, rail at y1248 floor row.
Risk: blur must never touch L2 text. Keep blur radius off text layer.

## 2. Clay material realism (touchable matte, moving coherent light)
Idea: everything is matte plasticine with fingerprints and soft contact shadows. One warm key light travels the whole 15 s so every object is lit consistently.
Light: single soft key moving slow arc left to right across 15 s; shadows always fall opposite.
- B1 hook: Two clay blocks (Claude-coloured, Gemini-coloured) are pressed into the table by a thumb-print stamp. Text "SAME DAY. TWO MODELS." as embossed clay letters rising from the surface.
- B2: Blocks roll to the left/right sides. Title "TERMINAL-BENCH 4.0" embossed, swipes in from the right.
- B3: Each block stretches upward into a bar (squash and stretch on landing). 64 vs 57. Light rakes across, showing tooltip-free surface texture. Sonnet bar gets a small crown nub.
- B4: Bars squash back down, then re-stretch with 71 / 78 under "AUTOMATIONBENCH-AA". Gemini gets the nub. Light has moved, so shadow direction shifts smoothly.
- B5: Bars fold flat into a clay slab. Verdict letters press out of the slab line by line.
- B6: Slab becomes a button; thumb presses it, "COMMENT VIDEO" depresses and rebounds. Thumbprint disappears into loop start.
Moves: light, clay forms, letters. Constant: table surface, rail (debossed strip), light direction logic.
Layout: bars occupy x120-820 y500-1000; numbers on bar tops; verdict 2 lines y1000-1200.
Risk: matte texture noise lowers legibility. Keep letters smooth, texture only on bodies.

## 3. Motion immersion (morph handoffs, never static, everything in safe rect)
Idea: no cuts. Each beat's hero morphs into the next beat's hero. Always something moving, but only inside the safe rect.
- B1 hook: Logo discs orbit slowly, then merge into one blob. Text "WHO WINS?" drops down.
- B2: Blob splits into two pills left/right, pills become the bar bases. Title swipes left in.
- B3: Pills extrude up into bars 64 / 57. Idle motion: gentle wobble and gradient shimmer on top faces.
- B4: Bars melt sideways (liquid swap, 0.4 s) into new heights 71 / 78. Numbers roll over like odometers. Winner bar pulses once.
- B5: Bars collapse inward into one horizontal strip, strip morphs into the verdict text block.
- B6: Text block shrinks into the top, strip re-forms as the CTA pill; pill bursts into the first-frame blob so the loop closes.
Moves: everything, always (min 1 moving element per frame). Constant: rail, safe-rect clip mask, gradient background.
Layout: hero centred at y600-1000; text y288-420 and y1050-1230.
Risk: morphs can obscure numbers mid-handoff. Hold each number sharp for the last 1 s of its beat.

## 4. Tasteful hero 3D (1-2 raymarched objects carrying brand identity)
Idea: only two raymarched clay objects exist. Claude = a soft radial clay burst; Gemini = a four-point clay star. They are the hero in every beat, nothing else is 3D.
Everything else is flat 2D type on a light gradient.
- B1 hook: Burst and star rise from below, rotate slowly, soft clay SDF blend between them for 0.5 s then separate. Text drops in.
- B2: Objects dock to left/right of the rect, scale 0.6. Title swipes in.
- B3: Each object's size/height is the score (Sonnet 64 bigger, Gemini 57 smaller). Number labels flat 2D under each. Subsurface-style soft light.
- B4: Objects swap proportions with a springy scale (71 / 78). Gemini star now larger and spins faster.
- B5: Objects shrink to equal size and sit side by side; verdict text drops down above them.
- B6: Objects tilt toward a flat CTA pill and bob. "COMMENT VIDEO".
Moves: two objects, light, gradient. Constant: two objects, rail, light direction.
Layout: objects y450-950, 2D numbers y980-1080, verdict y1100-1230.
Risk: raymarch cost and noise. Cap steps, render 1080x1920 pre-baked; keep brand shapes recognisable, not literal logos if shape reads weak (also supply real logos as flat chips at 56 px).

## 5. Wildcard clay relief stage (one surface, depth by extrusion, no camera move)
Idea: one clay relief tile field fills the safe rect. The camera is fixed top-down-ish. All depth comes from tiles rising and sinking. The same surface is the whole video.
- B1 hook: A 6x8 grid of flat tiles; a wave raises them to spell "WHO WINS?" in relief, then lowers.
- B2: Tiles on the left take Claude colour, right Gemini colour. Rise column heights show "TERMINAL-BENCH 4.0" as a raised strip across the top row.
- B3: Tiles re-form into two bar towers 64 / 57. Numbers stamped as relief on the tower tops.
- B4: Towers sink; ripple travels left to right; new towers 71 / 78 rise. Winner tower gets a taller cap tile.
- B5: All tiles flatten and carve the verdict into the surface, line by line as engraved relief.
- B6: Tiles regroup as a raised CTA button, "COMMENT VIDEO". A last ripple resets the grid for the loop.
Moves: tile heights, ripples, a slow light sweep. Constant: grid, camera, rail (strip of lowest tiles at the bottom).
Layout: grid exactly x48-888 y288-1248 (12 x 16 tiles at 70 px); text tiles sized so letters sit on whole tiles; rail row at the bottom.
Risk: tile resolution limits type. Use big Anton glyphs (>= 72 px) and only 2-line verdict. Letters must snap to the tile grid or be overlaid as a flat layer if too jagged.
