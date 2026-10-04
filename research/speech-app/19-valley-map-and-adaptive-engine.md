# Valley map, saved progress, sticker garden, adaptive engine (2 Oct 2026 spec, part 2)

PROPOSAL. Task agent output 2 Oct ~17:25, appended to little-steps-coreloop-spec. Spec only. The agent did not re-open the live prototype, so the upgrade plan assumes the 6 games from memory.

## Valley map home
- One full-bleed painted valley, scrolls sideways. 4 parallax layers (sky, far hills, mid hills, foreground grass), drifting clouds, swaying grass. Reduced-motion makes it static.
- Each game is a landmark, 120px or larger, spaced so a child cannot hit two by accident (pond = Echo Pond, stepping stones = Syllable Steps, garden bed = Name It Garden, lantern hill = Lantern Follow).
- Mascot stands at last-played landmark, walks to the tapped one (1 sec), game opens. Switch-scan cycles left to right.
- Top bar: sticker-garden button (left), parent button (right, hold 2 sec). No score, timer or streak.
- Daily nudge: one landmark glows ("today's friend"). No locks, no come-back pressure.

## Saved progress (on-device only, no account)
- Per game: level 1-5, last played, rounds completed, rolling hit rate (last 10), preferred input mode.
- Global: stickers, reduced-motion, sound level, font, session length limit.
- Parent area: plain weekly list, level per game, reset. No health claims.

## Sticker garden
- One plant per finished 5-round session (flower, mushroom, butterfly, lantern, stone cairn), type depends on the game.
- Never removed, no rarity tiers. About 40 stickers, then a new season background.

## Adaptive engine
- Level state per game, 5 levels, one function nextLevel(history): down after 2 misses in a row, up after 3 hits in a row, max one step per round. Level tables are data, not code.
- Hint ladder: 1) glow, 2) bigger glow plus mascot points, 3) answer shown, child taps to confirm. A hint counts as a half hit.
- First 3 upgrades:
  - Gentle Pairs: 2, 3, 4, 6, 8 pairs by level, no timer.
  - Sound Friends: 2 choices, 3 choices, two-sound sequence, rhythm, mixed. Browser TTS limit, real voices later.
  - What Comes Next?: 2-step, 3-step with 2 choices, 3-step with 3 choices, 4-step, 4-step with distractor.
- Build order: engine + level tables, Gentle Pairs, Sound Friends, What Comes Next, valley map, garden. Rough estimate 1 session each (agent's estimate, unvalidated).
