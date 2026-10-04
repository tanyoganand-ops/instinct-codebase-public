# Final-build spec: Claude vs Gemini Short (video 1)

Source of truth: P's own verdicts in the WhatsApp thread, 3-4 Oct 2026, collated 4 Oct 11:55 BST. Where a rule is my reading of a short reply ("Nah", "Meh"), it is marked (reading). Where a detail comes from a builder's note and not from P, it is marked (builder).

## 0. One-line brief

v9's 3D look and layout as the base, with a thinned version of B8's background, B8's duel animations, B6's whip-pan used sparingly, B3's "never a static frame" discipline, and the clay-ad feel. Several assets moving on and off screen at once. No morphing single card.

## 1. Base look (locked)

- **Base = v9.** P: "Really really like the 3d looks" (v9). Later: "I like this better than v10 as it's more centered and intricate and has shadows." v10's reflow is not wanted.
- Ingredients of v9 to keep: layered depth, directional shadows, depth blur, lens refraction on the glass carriers, clay accents turning in perspective, centred intricate layout.
- **Target feel:** P: "The clay advertisement is rly good, that's what I'm aiming for." Soft 3D clay elements, Apple-style layout, premium. P also wants "apple ui kinda".
- **Liquid glass / frosted glass:** P wants it, but "in moderation" ("Don't like too much. Use it in moderation"). Earlier asks: frosted glass throughout, light/white background ("don't like dark").
- **3D objects:** only a few assets, used tastefully. P on Hero 3D: "I think a few assets can be used with 3D, but tastefully, this is OK, use not great." P on raymarched cube/torus: "Meh, 3D objects not used tastefully enough." Rule: 3D on a small number of hero assets (clay props, brand cards), not on everything.
- **Clay turntable test** (volumetric clay brand cards): P reacted "Nicee". Candidate for the tasteful-3D treatment on the brand cards.
- **Typography:** P has said the fonts looked spindly and disliked several. No font has been approved by name. Use heavy, bold type; builders have used Anton (headlines) and Inter (supporting). Treat as provisional and confirm with P on the first frame test.
- **Image-heavy beats:** one hero image per beat, one short line of text under it, things moving in the back (P, 3 Oct: less clutter, no walls of text).

## 2. Background spec

P likes the backgrounds of two branches and wants the first one thinned.

- **Base = B8's background** ("a nice animations and bg"): pale `#f4f4f1` base, blue wash top-left, rose wash bottom-right, 11 clay props (sphere, donut and similar) crossing the full frame in both directions with scale pulse. Spec lives in the B8 duel-anim pack (`BG_SPECS`, `bgInit`, `bgUpdate`).
- **Thin it out.** P on B4's bg: "I really like bg but a bit too cluttered, too many stuff, but rly lik it tho." Apply the same note to B8: fewer props, more air. Starting point: cut the 11 crossing props to about 5-6, keep at most 2 on screen in any lane at once, nothing crossing the text or score areas. (builder-side numbers are my suggestion, not P's.)
- **Depth-lane idea from B4** (3 lanes at different speeds and blur) is liked as a background; keep the lane logic, drop the mid lane first (B4 builder said that is a one-line change).
- **Dots:** P asked for a dot-wave background and then "make the bg dots more prominent" (about 2x). Keep a visible rippling dot grid underneath. Dots must be noticeable; background motion must be noticeable, with the colour gradient shifting alongside it.
- **Parallax:** P said "needs to be used elsewhere, not the bg necessarily." Keep parallax on foreground assets (the whip-pan streaks), not as a bg effect. It stays in the toolkit.
- Background must go behind text (P, 3 Oct: wave pattern must pass behind text, not stop short of it). Applies to any wave or dot field.

## 3. Animation toolkit

### 3.1 Core rule
P: "Animation individually good. Not good when you apply it to all of them, use sparingly." Every technique below is an accent. Pick where each fires. Do not run all of them on every beat. Keep deliberate quiet beats (hook, verdict).

### 3.2 Always on
- **Never a static frame** (B3's discipline; P: good idea). Idle bob, sway or breathing on everything that is on screen (B8 `bob()`; B6 `idleX/idleY/restScale`). Keep drift small so text stays inside the safe rect.
- **Multiple assets moving on and off the screen at once, continuously.** P, at length: not one box distorting and shifting, but "multiple things zooming on screen, not morphing." Scores may count up live; cards must not morph into each other.
- **Silky, purposeful motion.** Not abrupt, slower than earlier drafts, fades clearly visible, image slide-ins slower with more motion. A slight pendulum on images (P, 4 Oct 7:20).
- Entrances in the brief P liked: simple swipe left/right, drop down.

### 3.3 Existing packs (use these, do not rebuild)
1. **B8 duel-anim pack** (`B8-duel-anim-pack.zip`: `duel-anim.js`, `USAGE.md`, clay sphere and donut PNGs). P: "we can snip the animations from this, I really like the animations." Pure functions of time `t` in seconds, no GSAP. Contents:
   - `E` easings (out, io, back with ~10% overshoot) and `kf()` keyframe interpolator
   - `bob()` idle float
   - `lateral()` slide in from an off-stage side with overshoot, hold, slide out; opposite-side pairs staggered 0.2s
   - `trade()` card swap over 1.3s: one card arcs up, scales to 1.1, rotates -28deg in perspective; the other dips, scales to 0.9, rotates +28deg
   - Badge pass: LEADS badge flies in over 0.5s with overshoot, rides the card, exits; losing card dips 18px
   - `count()` 0 to v count-up over 1.1s, ease-out
   - `coinY()` VS coin pop
   - `chips()` logo chips enter from opposite sides, swap with a 50px vertical split, leave opposite
   - CTA pill timing (documented in file)
   - Background: `bgInit`, `bgUpdate`, `BG_SPECS`
   - Known nit from the B8 builder: scores reset and recount mid-swap, which reads like a morph. Fix by carrying the number across the swap.
2. **B6 whip-pan pack** (`B6-whip-pan-pack.zip`: `whip.js`, `USAGE.md`, clay sphere and donut PNGs). P: "I like whip pan animations, we can use sparingly for some of them." Pure functions of frame number, no GSAP. Contents:
   - `whipEase` and `cam`: lateral swap, bezier (.85, 0, .15, 1), 9 frames centred on the swap frame. Pass a short `whips` array (for example only `[198, 306]`) for sparing use. Beats not listed never move laterally.
   - `sceneX` and `K`: per-asset parallax multiples 1.0 to 1.9 (headline 1.0, label 1.12, bar rows 1.25/1.5, brand cards 1.2/1.45, verdict lines 1.0/1.3, logo tiles 1.6/1.9, CTA 1.1, caveat 1.5). Higher k lands later and leaves faster so assets streak off and on one after another.
   - `blurSD`: horizontal-only motion blur from per-frame x velocity, gain .42, cap 48px, via SVG `feGaussianBlur`.
   - `idleX`, `idleY`, `restScale`: bob 4px, sway 7px, scale .954-.978 so 840px text boxes stay in the safe rect. Larger drift broke the rect.
   - Margin travellers (clay props zooming on and off): spec at the bottom of `whip.js`.
   - Neither pack has been re-rendered from the module, only smoke-tested in node. Render a test before relying on them.
3. The full reference builds sit in the earlier source zips (`b6-whip-pan-source.zip`, B8 source). Both packs are queued for the repo under `shorts/editorial/insider-branches/`.

### 3.4 Other techniques P liked (use as accents)
- **v12 multi-asset flow**: "This animation ok actually, we can use it in conjunction with the other animations." Assets travelling in from each other's positions, shrinking out to corners, scores counting up. Accent only, inside v9's look.
- **Immersive-motion idea** (blur-rack swaps, panel-to-pill transform, zero cuts): "Merge the immersive motion idea with v9." Became v11. Use the motion; the single-carrier layout of v11 was rejected.
- **Liquid depth** (cards split into depth planes, rack focus on entrance and exit, winner shifts forward at handoff, 10 degree yaw): P "like the liquid depth animation but it's meh". Optional light use for the winner handoff.
- **UI references liked:** glass-panels demo ("I like the UI, we can have this sort of UI"), card-stack micro-interaction ("good", 3D rendering difficulty a concern), orizon UI short ("good, but idk how difficult to render 3D"), rich-transition-3 and lusion-oryzo ("animation is nice").
- **B7 v3 "sparing" method** is the model for restraint: big zoom or spring only on the paired score heroes, bars and CTA; everything else a tiny reveal then holds still. P's follow-up was "Nah v9 was better", so this method is only borrowed as a restraint pattern.

### 3.5 Suggested allocation (my proposal, not P's words)
- Hook: quiet. Word-by-word headline, idle bob, background only.
- Benchmark 1 and 2 beats: B8 `lateral()` entrances, `count()` and bars, B8 badge pass. Idle motion everywhere.
- One whip-pan, between the two benchmarks. A second one only if the first reads well (B6 used four; P wants fewer).
- Verdict: quiet beat, B8 `chips()` swap at most.
- CTA: B8 CTA pill timing.

## 4. Content rules

Locked facts (from the v9 to v11 builds, which P approved as the base; builders relied on an Artificial Analysis check, not re-verified by them). Re-verify against the source once before export.
- Topic: Claude vs Gemini, "Sonnet 5.5 vs the new Gemini model"; Claude and Gemini logos used.
- Terminal-Bench 4.0: Sonnet 64, Gemini 57 (Sonnet leads).
- AutomationBench-AA: Sonnet 71, Gemini 78 (Gemini leads).
- Verdict: "Different tests. Different winners." with "Pick for your task" (Code execution: Sonnet; Multi-step tasks: Gemini).
- Source rail: "Artificial Analysis - 30 Sep 2026 / Sonnet Max / Argon High".
- CTA: navy "Comment VIDEO" pill.
- Argon caveat (limited rollout) was a separate black caveat bar in v12. Add it if it fits the safe rect at readable size. B2's builder dropped it for lack of room.
- Do not use "135 vs 135 / tie on paper" or "Top settings": those came from the 90s cut and were builder inferences, flagged as unverified.

Layout (from the v9 branch specs):
- Canvas 1080x1920, 30fps, 15s, 450 frames, H.264 yuv420p.
- **Safe rect for all essential text, logos and CTA: x 48-888, y 288-1248.** Shadows and background shapes may spill outside.
- Type floors at 1080 wide: source rail 48-50px, benchmark names 56-58px, supporting copy 48px, headlines 84-108px (verdict 84-96px), CTA 72px, tile scores 96px (up to 150px for hero scores).
- Audit all 450 frames for safe-rect violations. Keep text boxes <= 840px wide so idle drift stays inside.
- Fix the empty lower third that several builds had.

## 5. Format

- **15-second vertical Short, finish this first.** P rejected the 90s long-form cut ("Nah") and said: "I want to fine-tune the animations etc before I commit to a larger video." Long format (InsiderForce runs 90-107s) is parked.
- Reference channel: replicate InsiderForce "as good as possible" for structure and pace, with v9's look. The v12 line (their exact grammar) was rejected as a look, only usable as accent motion.
- **Video 2** (after video 1 is done, P's words "leave for after we finish vid 1"): the clay-realism, zero-cut immersive style.

## 6. Rejected, do not rebuild

| Direction | P's verdict |
|---|---|
| v12, v12b, v12c (InsiderForce-grammar full replica) | Nah / Meh / Nah. Line closed. v12 motion only as accent. |
| v10 (v9 reflowed) | v9 preferred: more centred, intricate, has shadows. |
| B7 v1/v2 stats-as-heroes, B7 v3 "sparing" | Nah (v1, v2). v3: "v9 was better." |
| B1 kinetic type | Nah |
| B2 / B2b card stream | Nah |
| B3 / B3b spring physics | Meh. Only the "never a static frame" idea is kept. |
| B5 carousel orbit | Meh. Shelved, no more work. |
| 90s long-form (v90) | Nah |
| V8-line wildcard (continuous camera journey) and relief-stage wildcard | Nah |
| v9 raymarched 3D objects (cube/torus) | Meh, not tasteful |
| v9 material (porcelain tiles) | Meh |
| Liquid-glass-heavy single morphing card | Too much; moderation only |
| Single-card morphing layouts (v11, v11b) | Wrong motion model. Assets must move on and off, not morph. |
| Dark background | Not wanted. Light/white. |
| Wave-pattern background and the Instagram reels P said not to copy | Dropped (3 Oct, P: disliked both pattern and font) |
| Awwwards / scroll / SVG / GSAP.com / Stripe / OWID reference clips | "Too simple" / "So bad" |

## 7. Ordered to-do for the final build

1. Pull the two packs: B8 `duel-anim.js` and B6 `whip.js`, plus the clay PNGs. Render a short test of each module to confirm they work outside their original builds (neither has been re-rendered).
2. Start from v9's source bank (layout, cards, shadows, refraction, depth blur).
3. Lay out the 15s timeline in the safe rect with the locked facts (section 4). Reserve a lower-third element so it is not empty.
4. Build the thinned B8 background: pale base, two washes, rippling dots visible at about 2x, 5-6 clay props max, lane logic from B4, nothing crossing the text.
5. Wire B8 animations per section 3.5: lateral entrances, count-ups carried across the swap, badge pass, chips swap, CTA pill.
6. Add idle motion to every on-screen asset so there is never a static frame.
7. Add one whip-pan (B6) between benchmarks, pass `whips=[frame]`; test a second only if it reads well.
8. Add a few 3D clay assets on the brand cards or hero props (turntable style), the rest 2D, glass only as accent.
9. Fix type sizes to the floors. Confirm font with P on a first still (spindly fonts disliked).
10. Audit 450 frames for safe-rect violations, overlapping text and blank cards. Check on phone size.
11. Re-verify the scores and source line against Artificial Analysis. Export.
12. Send to P for a verdict. Then park video 2 (clay realism, immersive motion).
13. Housekeeping: repo uploads of all videos, packs, this spec and the conventions MD are still queued through GitHub (web UI renames files, rename each after upload).

## 8. Open points for P
- Font choice (none approved by name).
- Whether the Argon caveat bar goes in video 1.
- How many whip-pans (suggested: 1-2).
