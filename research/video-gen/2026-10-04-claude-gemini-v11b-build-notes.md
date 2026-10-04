# Claude vs Gemini v11b

15 seconds, 1080 x 1920, 30fps, 450 encoded frames. H.264 yuv420p with the existing cue bed as AAC. No narration.

## Changes from v11
- Background dot opacity increased from 0.26 to 0.50; blur reduced from 0.65px to 0.15px.
- Content carrier now moves 8px horizontally and 9px vertically with 2.2-degree perspective sway. Evidence moves independently by up to 6px.
- Brand pendulum increased to 2.3 degrees and 5px vertical travel. Sphere and donut travel increased to roughly 18px.
- Existing score morph, blur-rack transitions, card handoff turns, bar sheens and panel-to-CTA morph remain unchanged.

## Verification
All 450 states saved before rendering. Zero visible text-range violations against x48-888/y288-1248. Runtime, layout and contrast checks passed. Asset bound audit found movement in every adjacent pair: minimum 0.551px displacement among sampled brands and accents. Encoded video has 450 frames and zero identical adjacent pairs. Inspected the encoded 15-sample contact sheet: dots are clearer, text and benchmark hierarchy remain readable, carriers and CTA intact.

This is the requested interim v11b, not the newly requested continuous multi-asset on/off-screen rebuild. It still uses the v11 composition with persistent carriers and stronger idle motion.

Prior versions retained. Local work only, pinned Hyperframes 0.8.115, telemetry disabled. Source claims unchanged from v11; no new factual research. Intermediate scores during morph are animation states, not separate measurements. Source provenance retained in brand-provenance.md.
