# Missed-punch detection

## Verified facts
- 2026-09-28 19:44 (P): punching mechanism "like 50% accurate", still being worked on.
- 2026-09-28 20:45 (P): failure mode is missing real punches, not random triggers. Wants it "good in terms of fast".
- Recognition style P wants: skeleton overlay over the body/hands, "similar in terms of actual recognition" to the app P compared it to (comparison name garbled in transcript).

## Instinct's diagnosis (2026-09-28 20:52, PROPOSAL, untested)
Problem is "almost certainly event logic + frame timing, NOT the model". Advice: do not swap models yet.

## Ordered plan from 28 Sep (PROPOSAL)
0. Build an eval rig first. Record 30-50 punches per arm plus 30-50 non-punches (waving, reaching, signs). Save timestamped wrist/elbow/shoulder landmarks, label them, measure recall, false triggers, latency. Test every change against it. Portfolio value: "improved punch recall from 50% to X%".
1. Replace the threshold with a per-arm state machine: READY (wrist near shoulder, elbow bent) > EXTENDING (elbow straightens, wrist displaces) > PEAK (enough travel in 100-500ms) > COOLDOWN. Fire once at peak.
2. Velocity from real frame timestamps, not frame counts. Normalise travel by shoulder width. 3-frame median smoothing, accept 2-of-3 motion samples.
3. Why fast punches vanish: LIVE_STREAM style async tracking drops frames when busy. Use latest-frame-only processing (see performance-and-benchmark.md).

## 2026-10-01 18:30 verdict (as reported to P)
"Per-arm state machines for punches, hand tracking only for special moves."

## Gaps
- Real punch code not seen. Thresholds above (100-500ms window, 2-of-3) are starting values proposed by Instinct, not tuned values.
- No eval-rig data exists yet.
