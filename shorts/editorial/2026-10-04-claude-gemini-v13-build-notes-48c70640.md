# Claude vs Gemini v13

15s, 1080x1920, 30fps, 450 frames. H.264 yuv420p and existing cue-bed AAC; no narration.

## Build
V9's centered paired clay/glass carriers, inset score wells, directional shadows, perspective depth and lens refraction are the material base. Separate hook logos, two benchmark card pairs, separate evidence plates, lead badges, verdict chips and CTA move independently. No card morphing. The quiet hook/verdict alternate with deliberate benchmark activity.

B8 pack functions wired directly: lateral, bob, badgeX, count, chips, bgInit/bgUpdate and kf. B6 cam, sceneX, K, blurSD and idle functions are wired directly. Rendered tests inspected before final export. Six crossing clay props in top and two bottom depth lanes replace the eleven-prop background. Pale blue/rose washes shift gently; prominent dot ripples span behind all content. Background props avoid the essential text region. Foreground gets the single whip; background does not share the camera parallax.

## Choices
- Heavy Anton headlines and model labels, bold Liberation Sans support. Provisional font choice, not a claim of font approval.
- One nine-frame whip centred on frame 198, between benchmarks.
- Readable 48px black limited-rollout bar on the CTA beat.
- Scores carry 64/57 into the benchmark handoff and then rise to 71/78 rather than reset/recount. Intermediate integers are animation states, not measured results.
- Logo-chip crossing uses extra vertical separation to prevent collision.

## QA
450 frame states saved before final render. All 450 visible text states audited: zero cross-asset text overlaps; stage clipping guarantees essential visible text/logos/CTA stay within x48-888/y288-1248. Raw off-stage bounds during lateral entrances, exits and whip are intentional and preserved in the plan, not falsely counted as fully in-bounds. Type floors: headline88px, benchmark56px, support/model/source48px, CTA72px, scores112px.

Runtime and contrast checks pass; layout has zero errors/warnings. Informational findings concern intended clipped travel. Inspected encoded contact sheet and final transition strip: readable benchmark holds, correct final scores, separate chip arcs without touching verdict text, one blurred lateral whip, readable caveat/CTA. No identical adjacent encoded frames. Clay travellers populate the lower third, which has no essential copy below the safe stage.

## Sources rechecked 4 October 2026
https://artificialanalysis.ai/articles/gemini-4-argon-google-top-three-labs
Article dated 30 September 2026 confirms Terminal-Bench 4 values 64/57; AutomationBench-AA 71/78; Claude Sonnet 5.5 Max and Gemini 4 Argon High settings; selected-user rollout and not public availability.
https://artificialanalysis.ai/models/gemini-4-argon
Current model page supports benchmark names and High setting.

Old versions retained. Local work only; Hyperframes pinned 0.8.115; telemetry disabled; no paid API, cloud render or publication.
