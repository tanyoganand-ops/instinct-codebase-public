# Claude vs Gemini v12 - continuous multi-asset flow (Insider-style)
15s, 1080x1920, 30fps, 450 frames, H.264 + existing cue bed. Built with Python/PIL (build.py), not Hyperframes.

## InsiderForce conventions matched (from frame study of https://youtube.com/shorts/3iUo7bnsN30, 69s)
- Pale grey bg with faint grid, soft; assets float above it.
- Tilted floating cards with big soft offset shadows (brand, benchmark cards held at -5/+3 degrees).
- Word-by-word kinetic headline: small grey connector ("vs") + large bold keywords, staggered rise-in.
- Black label bar with white caps for the caveat (their "nobody is talking about this tool" bar).
- Stacked layout: type and cards co-exist, new element arrives while the old one is still leaving.
- Comment CTA as small grey "Comment" + big "VIDEO" quote word.
Not matched: their screenshot/UI-recording cards, icon-list reveals, 3D end logo, per-word typewriter; per-frame blur pops.

## Motion
Assets travel in from another asset's position (brand badges are the origin of benchmark cards, lead pills, verdict tiles) with scale-up from .3, and leave by shrinking toward corners. Every asset carries a +-9/10px float. Audit: min 1, avg 4.6 assets moving per frame; 2 frames (326-327, ~10.9s) have only 1 asset with >0.2px motion. Safe-rect audit (sprite bbox incl. transparent corners): 9 frames (~6.3s) where tilted benchmark card bbox exceeds x888 by <10px; text itself inside.
## Conflict: design MD says no zooms/fly-ins; P's latest says "zooming on screen" - followed P.
## Content exact per MD; "ARGON: LIMITED ROLLOUT" wording is mine. Source rail in 2 lines (48px). Verdict 88px, CTA "VIDEO" 150px, bench names 56px.
