# InsiderForce measured motion conventions

Source: 3 recent Shorts from youtube.com/@InsiderForce, downloaded directly with yt-dlp (no block). All 1080x1920, 30 fps. Frame numbers are 30 fps (1 frame = 33 ms).
- bS6IlkUozAI "Free tool cuts Claude Code web browsing tokens by 90%": https://www.youtube.com/shorts/bS6IlkUozAI (100.7 s, 3021 frames)
- 4qIZmI_1Zgs "Get 1000 Free APIs for Claude Code": https://www.youtube.com/shorts/4qIZmI_1Zgs (92.2 s, 2767 frames)
- J_xP1PhUmqg "Claude Code, Codex, Cursor 10x faster with this one tool": https://www.youtube.com/shorts/J_xP1PhUmqg (106.7 s, 3202 frames)

Method: per-frame mean abs difference series on all frames (cuts, bursts, still gaps), white-card bounding-box tracking frame by frame (entrances), brightness/position tracking of single words, and 32-frame contact sheets stepped at 1 frame. Entrance numbers below come from Short 1 (bS6...) frames 0-63 and 100-175; the others were checked visually for the same patterns. Pixel numbers are on a 540-wide frame (x2 for 1080). Not measured: audio/VO sync, easing curves to the exact bezier (inferred from per-frame deltas).

## 0. Headline surprises vs a 15 s plan
- These are NOT 60 s. They run 92-107 s. For a 15 s version, keep the pattern, compress the cut spacing.
- Canvas: flat pale grey (about #F0F0F0), faint dot/grid pattern, watermark "insiderforce.io" bottom-centre, constant the whole video. Light mode only, no dark backgrounds except inside embedded screenshots.
- One hero asset per scene, caption block beneath it, never more than 2-3 lines.

## 1. Measured conventions

| Convention | Measured value |
|---|---|
| Major scene change (new hero asset) | Hard cut, 0 frames, no wipe/dissolve. Median gap 4.6 s (S1), 3.1 s (S2), 5.4 s (S3). Range 1.0-17.6 s. Overall about 3-5 s per scene |
| Visual change events (anything moving big, incl. chips/words entering) | Median 2.8 s (S1), 1.4 s (S2), 2.0 s (S3) between events |
| Time with visible motion | 37% (S1), 64% (S2, busiest), 37% (S3). Fully static frames 25% / 7% / 24%. So holds exist, but background drift/shadow keeps things alive |
| Typical motion burst | Median 10-15 frames (0.33-0.5 s); p90 38-51 frames. Peak speed lands at about 40-45% through the burst, so it accelerates fast then decays (ease-out dominant). 50% of peak speed reached 3-5 frames in |
| Still gap between bursts | Median 10-19 frames (0.35-0.65 s); p90 77-90 frames (2.5-3 s) |
| Exit of an asset | None animated. Whole scene hard-cuts out in 1 frame (S1 f150: 4-chip stack and caption gone in one frame). Text clears on the same cut |
| Entrance of the next scene | Starts SMALL (about 15% scale) and scales up over about 25 frames, ease-out (S1 f151-175: tiny Claude icon grows into the 3-chip row while a connector line extends and a globe icon scales up from a dot) |
| Stagger between related assets in one scene | 20 frames (0.67 s) between chip 2 and chip 3 in the stack (Codex f26, Hermes f46) |
| Words/captions | See section 3 |
| Idle motion on held assets | Continuous slow float/drift, about 0.5 px per frame at 540 wide, plus very slow scale-up (stack grows about 1-2% over 6 frames during hold). Nothing is ever perfectly still |
| Shadows | Soft large drop shadow under every card, offset down-right, moves with the card. Card = white rounded rect on grey |

## 2. Asset entrance detail (S1, frames from start)

Directions and distances, 540 px frame, measured per frame:

1. Chip 1 "Claude": drops from ABOVE the top edge. Top edge y: f4=14, f8=47, f12=65, f16=76, f20=83, f24=87, f28=89, then fixed. About 75 px of travel in 24 frames. 77% of the travel is done by f15 (11 frames). Pure decelerating ease-out, no vertical overshoot. Left edge also settles 69 -> 118 in the same time (diagonal settle with a slight scale down, about 15%).
2. Chip 2 "Codex": slides in from the LEFT. Left edge x: f26=37, f27=69, f28=101, f29=119. That is 32 px/frame (5.9% of width per frame), constant speed for 3 frames, then a quick stop with small overshoot (to x=112 at f39, a 7 px / 1.3% overshoot) and settle by f43. Total about 17 frames, 3 of them travel.
3. Chip 3 "Hermes": slides in from the RIGHT, same 32 px/frame for 4 frames (right edge 539 -> 507 -> 475 -> 444 -> 412), then spring overshoot to x=99 at f54 (19 px / 3.5% past rest), back to rest at f59-62. Total about 14 frames after arrival.
4. Chip 4 "opencode": enters from the left (cut-in on the scene change at f510 in the sequence, shows as a 6-frame cluster of change).

Summary: lateral entrances are fast linear travel (3-4 frames, about 6% of frame width per frame) followed by a spring settle of 8-14 frames with 1-3.5% overshoot. Top entrance is a slower 24-frame ease-out drop with no overshoot. Alternate left/right for consecutive chips. Distance travelled is whole-frame (starts off-screen) for chips; small for later settle.

## 3. Text treatment

- Typeface: neo-grotesk sans (Inter/Roboto-like). Headline emphasis words are heavier (bold/extra-bold, condensed look at big sizes), filler words are regular weight and about 70-80% of the size. Occasional italic bold for the keyword ("Follow", "sends").
- Captions are word-by-word, synced to VO. Each word fades in and darkens from light grey to near-black while rising into its baseline. Measured on "have" (S1 f107): grey 164 at f107, 112 at f110, 61 at f116, 33 at f120, 10 at f127, 0 (black) at f132. So about 25 frames (0.8 s) to fully settle, 60% of the change in the first 10 frames. Rise: about 50 px lower start (at 540 scale a word region mean y fell 112 -> 62 over those frames), ease-out.
- Word cadence while VO runs: a new word about every 5-6 frames at the fast moments (S1 f107 "have", f112 "the", f117 "same"). Words are laid out so the line grows left to right and re-wraps; earlier words stay.
- Line structure: 2-3 lines max, left/centre aligned block, sits under the hero asset about 55-80% down the frame. Key noun/verb is bigger and bolder than the connecting words ("they all have the same" small, "expensive habit" in a black filled box with white text, big).
- Highlight device: black rounded rectangle with white text for the key phrase; wipes in left to right over about 8 frames (S1 f404 region: "free & op..." clipped by a moving mask).
- Text is cleared by the scene hard cut, not faded out.

## 4. CTA handling (identical in all 3 Shorts)

Last about 8 s of each Short:
1. Hard cut to a hero asset with caption. Prompt is "Comment 'WORD'" (S1 "WEB", S3 "FAST") with the word in quotes, letter-spaced, then grows to bold large over about 15 frames, then "and I will send you ..." words reveal one at a time (about 0.5 s apart).
2. Final 4-5 s: black crown/"InsiderForce" logo mark centred, scales in. Caption "make sure you Follow InsiderForce" at top (InsiderForce set large and bold), "the system only sends it to FOLLOWERS" at bottom with FOLLOWERS in the biggest bold caps. Same words word-by-word reveal as the body.
3. S2 used "Save this before you..." mid-video and no comment-keyword CTA, only the follow card.
The CTA is part of the template, not rebuilt per Short. Suggest the same for ours: fixed end card, keyword in quotes bolded.

## 5. Per-Short evidence

### S1 bS6IlkUozAI (100.7 s)
- Hard cuts (d>14) at s: 5.0, 9.0, 13.5, 16.9, 18.1, 18.8, 24.2, 32.0, 35.5, 40.0, 48.3, 56.1, 66.8, 76.5, 81.1, 84.6, 96.8. After merging cuts within 1 s: 16 major cuts, median gap 4.6 s, mean 6.1 s.
- 33 event onsets, median 2.8 s apart. 69 motion bursts: mean 15.9 f, median 11 f. Still gaps median 10.5 f.
- f0-28: Claude chip drops in. f26 Codex from left, f46 Hermes from right (numbers in section 2). f150 hard cut to the tiny icon that grows into a 3-icon row (Claude/Codex/Hermes mini cards) with a vertical line and globe. Slow connector line grows downward 1-2 px/frame; "i" icon drops down the line about 1.5 px/frame.
- Caption f100-131: "they all have the same" word-by-word, new word every 5 frames.

### S2 4qIZmI_1Zgs (92.2 s) - the busiest
- 25 cut candidates, 24 major cuts, median 3.1 s apart (fastest of the three). 64% of frames have motion.
- Opening: orange hand-drawn bursts at the frame corners and two hands reaching in to a blue "API's" folder, caption "This is how you get 1000 FREE" (FREE in bold caps).
- Mid: phone mock-up with a screenshot card inside; screenshots swap inside the phone every ~1 s (3 variants in 3 s). Wide card with soft shadow and a "fly through" background (orange to blue, 15-frame cross blur, f213-228) while the caption "People are turning these free APIs" builds word by word, and the whole caption fades (about 10 frames) as the card changes.
- Dark GitHub screenshot card as a hard cut. Mix of one dark card on a light canvas.
- End: crown logo, follow CTA.

### S3 J_xP1PhUmqg (106.7 s)
- 18 major cuts, median 5.4 s, one 17.6 s hold. 37% motion, 24% static frames. Same template as S1 (grey canvas, cards, keyword caption), screenshot-style cards in the middle.
- End: "this is what your coding agent was always supposed to feel like" word reveal, then Comment "FAST" (letter-spaced small -> large bold in about 15 frames), "and I will send you the direct link", then crown + follow card.

## 6. Replace the [DEFAULT] numbers with these

- Scene cut: hard cut, 0 frames (not a transition).
- Scene length: 3-5 s (S2 3.1 s median, S1 4.6, S3 5.4). For 15 s: 3-4 scenes.
- Sub-event beat: new visual event every 1.4-2.8 s.
- Lateral entrance: 3-4 frames travel at about 6% width/frame, then 8-14 frame spring settle, 1-3.5% overshoot. Alternate left and right.
- Top drop-in: 24 frames, ease-out, no overshoot; 77% done by frame 15.
- Scene-start scale-up: from 15% to 100% over 25 frames, ease-out.
- Stagger between assets in a group: 20 frames.
- Word reveal: 25-frame fade+darken+rise per word, new word every 5-12 frames.
- Exit: none. Cut out.
- Idle drift on all held items; shadows always on.
- CTA: last 8 s, fixed template (comment keyword, then logo + follow card).

## 7. Caveats
- Sample is 3 Shorts, all in the same format; numbers for easing are inferred from per-frame deltas (not fitted beziers). The 6%-per-frame linear travel and the overshoot percentages are measured on two chips only (Codex, Hermes).
- Frame rate is 30 fps; timings may be rounded by 1 frame.
- I did not see the existing conventions file with the [DEFAULT] tags, so the section 6 list is the replacement set, not a diff.
