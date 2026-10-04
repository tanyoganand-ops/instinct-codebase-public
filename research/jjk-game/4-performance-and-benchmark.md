# CPU performance budget and pose-tracker benchmark direction

## Constraint (P, 2026-09-28 20:45)
Normal 8GB laptop, CPU only, live webcam. Goal: as accurate as possible while running on a moderate machine. Resolution/fps unknown to P.

## Architecture proposal (2026-09-28 20:52, untested)
- ONE hand landmarker model, real timestamps, VIDEO or LIVE_STREAM mode.
- Capture thread + latest-frame-only slot, game loop decoupled at 30-60 fps.
- Capture at 640x480. Bright even light facing the player, shoulders and hands in frame.
- LIVE_STREAM drops frames when busy, which is where fast punches disappear, so async latest-frame processing matters.

## Stack choice (2026-09-30 06:05)
MediaPipe Pose + Hands primary, MoveNet Lightning speed fallback. Runs client-side in the browser.

## Benchmark direction (2026-10-01 18:30 verdict; queued 2026-10-02 07:52)
Benchmark MoveNet vs MediaPipe on P's actual laptop before committing. PROPOSAL for what to measure (derived from the plan, not a recorded spec):
- Per-frame inference time and sustained fps at 640x480 on the 8GB CPU-only laptop
- Dropped frames during fast punches
- Punch recall and false triggers using the eval rig from punch-detection.md
- CPU load while the game also renders
Pose-only tracking for punches, hand model only when a special move is being attempted, is the proposed way to save CPU.

## Status
Not run as of 2026-10-02 17:30 BST. No benchmark numbers exist. Needs P's laptop (or its specs and a test clip).
