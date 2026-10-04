# Domain Expansion hand-sign detection

## Verified facts
- 2026-09-28 19:44 (P): symbol/Domain Expansion detection ~50% accurate. P said this is separate from the punch problem (20:45).
- 2026-09-28 20:45 (P): in game, Domain Expansion stops the other person/cursed spirit from attacking you.

## Proposal (2026-09-28 20:52, untested)
- Reuse the SAME hand tracker as the rest of the game, no second model.
- Turn the 21 hand landmarks into wrist-centred normalised vectors plus finger angles.
- Collect 100-200 frames per sign across 5 sessions, plus a few hundred "none" frames.
- Train a kNN classifier (scikit-learn) with a margin and a distance cutoff so it can answer "no sign".
- Gate: sign must be stable 150-300ms, then 1s cooldown.

## 2026-09-30 06:05 stack decision (reported to P)
MediaPipe Pose (33 body points) + Hands (21 per hand), reported as Apache-2.0, runs fully in the browser, no API quota. MoveNet Lightning as speed fallback. Instinct reported hosted YOLO demos fail on AGPL licensing. Licence claims were not re-checked in this backfill; verify before shipping.

## 2026-10-01 18:30 verdict
Hand tracking only for special moves (not for punches).

## Gaps
- Which signs, how many, and P's current classifier are unknown.
- No labelled data collected yet.
