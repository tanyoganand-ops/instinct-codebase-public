# Vid-2 research and content plan - 4 October 2026

Recommend "Same app score. Different finance score." Vals' current model pages put Sonnet 5.5 and Gemini 4 Argon within 0.48 percentage points on Vibe Code Bench v1.1, but 7.30 points apart on Finance Agent v2. It is a new task contrast rather than repeating Vid-1's terminal/automation contrast. This describes published runs, not an equal-compute universal winner. No video build, asset generation, or repo changes.

## Concepts, ranked
1. Apps versus finance. Hook: "Building apps? Almost level." Vibe Code Bench: Sonnet 92.39%, Argon 91.91%. Finance Agent v2: Sonnet 58.10%, Argon 65.40%. CTA: "Comment your task." Same evaluator on both sides, strong changing-score visual, most useful task-selection story.
2. Can your AI read this chart? Hook: "A chart can change the winner." Chartography: Sonnet 61.6% no tools (Anthropic announcement), Argon 71.6% (Surge live board, High). CTA: "Comment CHART." One clay Sankey chart is a clean hero. Lower confidence in comparability: Sonnet's figure is vendor-reported and was not present in the fetched Surge live list.
3. Score versus bill. Hook: "The higher score isn't the whole bill." Vals Index: Argon 68.90%, Sonnet 67.04%; cost/test $15.68 versus $21.34; latency 46m33s versus 78m4s. CTA: "Score or speed?" These are index-run averages at different configurations and price assumptions, not prices for a user's prompt. Caveats make this less suitable for 15 seconds.

## Top concept: 15s / 450 frames at 30fps
| Frames | Time | On-screen text | Action |
|---|---|---|---|
| 0-59 | 0-2s | Building apps? | Claude Sonnet 5.5 and Gemini 4 Argon clay logo tiles enter from opposite sides around one centred clay laptop. No score yet. |
| 60-179 | 2-6s | Almost level. | Two independent score tiles: Sonnet 92.39%, Argon 91.91%; label Vibe Code Bench v1.1. Laptop shows a deliberately generic mock app, not benchmark output. Scores reveal once and settle; no winner badge for the tiny gap. |
| 180-299 | 6-10s | Finance changes the gap. | Laptop travels off; filing stack and clay calculator travel on independently in the same space. New benchmark label Finance Agent v2. Sonnet 58.10%, Argon 65.40%. Slight foreground handoff toward Argon; badge says HIGHER SCORE, not BEST MODEL. |
| 300-359 | 10-12s | Test your task. | Props leave separately; two logo tiles return to equal depth. Supporting rail: Published runs. Different settings. |
| 360-449 | 12-15s | Comment your task. | Navy CTA pill rises into the lower safe area. Brand tiles retain slight breathing motion. |

Optional narration: "Building apps? Sonnet and Argon are almost level. Financial research? Argon scores higher. These are different test settings. Test your task. What would you use it for?"

Caption-first works without narration. Narration is optional, not a dependency.

## Facts and limitations
- Vibe values are functional app test scores, not proportions of perfectly built apps or design-quality ratings. Reported uncertainty bands are ±1.26 for Sonnet and ±1.90 for Argon; do not call a 0.48-point difference a decisive winner or a formal statistical tie.
- Finance uses dealbreaker-gated partial credit. Do not say Argon completed 65% of financial tasks perfectly. Sonnet model page discloses 81 fallback runs (6%); published result includes product/fallback behavior.
- Vals default model configurations are Sonnet Max and Argon High; pages say individual benchmarks may use different parameters. Do not imply identical compute budgets or assert exact per-benchmark settings without run metadata.
- Google announcement describes a phased Fairwind rollout. End-card or description must not imply everyone can switch to Argon today; recheck access before publishing.
- Persistent source rail: Vals AI / checked 4 Oct 2026. Full URLs and caveats in post description. Content plan needs approval before production.

## Asset list
Reuse: clay brand tiles/logo artwork; sphere and donut assets; B8 lateral entrances/bob/count helpers; existing shadows and limited glass accents; thinned B4d depth-lane background; safe rectangle and type-size rules from repository reference.
New assets to prepare later: clay laptop with clearly illustrative app UI; filing stack; calculator; four separate fixed-value score tile states; two benchmark labels; Higher score badge; source rail; settings rail; navy comment pill. Foreground illustration is one grouped hero per beat. Never morph laptop into calculator, reset/recount during a swap, or use decorative data as if it were benchmark evidence.
Motion: one continuous light stage; independent overlapping object exits/entrances; one subtle depth handoff; no full-screen cut or obligatory whip-pan. All background traffic stays outside essential text. Pale near-white base, blue/peach clay accents, soft directional shadows, frosted glass only on small carriers. Heavy headline face is provisional, not declared approved. No pixels generated or inspected because this assignment is a content plan only.

## Sources
Current values: https://www.vals.ai/models/anthropic_claude-sonnet-5-5 and https://www.vals.ai/models/google_gemini-4-argon
Definitions: https://vals.ai/benchmarks/vibe-code and https://vals.ai/benchmarks/fabv2
Composite definition: https://www.vals.ai/benchmarks/vals_index
Model announcements: https://www.anthropic.com/claude-sonnet-5-5 and https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/
Chart board and protocol: https://surgehq.ai/benchmarks/chartography and https://arxiv.org/html/2608.10677v1
Code: https://github.com/surge-ai/chartography
Secondary triangulation: https://memeburn.com/gemini-4-argon-vs-claude-sonnet-5-5/

Caveat: Vals' benchmark explainer pages contain older narrative leaderboards than its current model pages. Use model pages for the dated figures, explainers for scoring definitions; recheck at export rather than carrying the old narrative rankings forward.
