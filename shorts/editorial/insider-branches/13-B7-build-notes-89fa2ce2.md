# B7: Stats as heroes

15 seconds, 1080 x 1920, 30 fps, H.264 yuv420p, silent. 450 frames.

## Distinct treatment
Paired 176 px scores are the hero assets. Each benchmark gets a score-slab beat followed by a separate paired bar beat. The bars are proportional on the same 0-100 scale: 64/57, then 71/78. Scores never interpolate through invented intermediate values. Supporting raster brand cards, benchmark labels and winner strips travel simultaneously with the scores. Every scene uses separate incoming and outgoing sprites rather than morphing existing objects. The background does not move.

Matte pastel peach and periwinkle, raised clay edges, diffuse cast shadows, Anton headlines and labels. Benchmark text 64 px; verdict 82 px; CTA 76 px; source 48 px. Logos preserve shape, aspect ratio and original colours.

## Timeline
- 0-1.8s: matchup + brand cards + hook.
- 1.8-3.7s: Terminal-Bench 4.0, giant 64/57 counters.
- 3.7-5.7s: Terminal-Bench 4.0, paired proportional bars.
- 5.7-7.6s: AutomationBench-AA, giant 71/78 counters.
- 7.6-9.6s: AutomationBench-AA, paired proportional bars.
- 9.6-12.1s: Different tests. Different winners.
- 12.1-15s: Make videos like this? Comment "VIDEO".
- Source rail during proof beats; limited-rollout caveat during verdict and CTA.

## Audit and inspection
All 450 transform states saved. Full decoded-frame MD5 audit finds zero identical adjacent frames. At least four assets change position/scale between adjacent states. Exact metrics in audit.json. Checked encoded contact sheet and full-resolution bar scene; fixed score/bar overlap and re-rendered before delivery. Checked paired score frames at phone size.

Content pixels are masked to x48-888/y288-1248. Entrances/exits deliberately reveal partial travelling sprites inside this mask. Their whole transformed bounds can go outside it, which is necessary for travel. Settled content is readable inside it. There are brief overlaps between outgoing and incoming text at transitions; no static frames, cuts, orbit, spins or camera ride.

## Scope and caveats
Locked benchmark/model figures and source text came from the brief and source bank; no new factual verification was performed. User review branch, not a publication decision. This matches the requested moving-stat concept, not a proven frame-for-frame InsiderForce replication. Applied structural reference conventions: early hook, proof beats, sound-off readable text and keyword-comment CTA. The supplied conventions file explicitly says its frame timings are unmeasured; no measured InsiderForce video reference was available during this build.

## Rebuild
Requires Python 3, Pillow and ffmpeg. Run `python3 render_stats.py` from this folder. The source ZIP includes the script, required fonts, original raster lockups, brand provenance, font licences, frame plan and audit. Video is supplied separately.

## Measured-reference revision
A measured InsiderForce resource arrived after v1. This v2 borrows its alternating-side, 4-frame lateral arrival and ~10-frame decaying spring settle. Spring excursion is at most 30 px nominal, attenuated to about 15 px at its first peak. Scale zoom remains a slower ~14-frame ease-out to preserve legibility. Exits accelerate over about 10 frames. Added a faint static dot grid. New encode again has 450 frames and zero identical adjacent decoded frames. Updated encoded contact sheet and automation score frame inspected.

References supplied by parent: https://www.youtube.com/shorts/bS6IlkUozAI ; https://www.youtube.com/shorts/4qIZmI_1Zgs ; https://www.youtube.com/shorts/J_xP1PhUmqg . I inspected the supplied frame-step images and measurement report, not these three videos independently. Does not copy their hard cuts, idle holds, single-hero constraint, VO captions or follow-gate because those conflict with this locked 15s silent, continuously travelling multi-asset brief.
