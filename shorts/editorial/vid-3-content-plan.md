# Vid-3: Higher score. Still needs review.
Research and proposed content plan, 4 October 2026

## Recommendation and status
Recommend a legal-work reliability Short, rather than another "winner changes by task" Short. On Vals' current model pages, Gemini 4 Argon scores above Claude Sonnet 5.5 on both Legal Research Bench and Harvey's Legal Agent Benchmark. The useful reveal is that Argon's Harvey final score is still only 19.58%. A lead over another model is not proof of dependable completion.

This is a proposed content plan only. No video, assets or repo changes. Current published values are verified, but **equal reasoning/compute settings are not verified**. If matched settings are a hard requirement, hold production until current run metadata is recovered or a verified matched comparison replaces this one. Do not describe these as an equal-compute head-to-head.

## Three fresh concepts
| Rank | Topic and hook | Published facts to feature | CTA | Assessment |
|---|---|---|---|---|
| 1 | Legal-work reliability. "Higher score. Still needs review." | Legal Research Bench: Sonnet 48.08%, Argon 54.81%. Harvey Legal Agent Benchmark final score: Sonnet 2.92%, Argon 19.58%. | "Would you trust it?" | New task and narrative. Strong all-pass/final-score story, no repeated benchmarks. |
| 2 | Code migration. "New language. Same behaviour?" | Code Migration: Sonnet 69.83% ±4.26, Argon 68.17% ±4.35. | "What would you migrate?" | 1.66-point difference is small relative to reported bands. Focus on behavioral testing, not a decisive winner. |
| 3 | Security scores versus product policy. "Skill, or safeguards?" | CyberBench v1.1: Sonnet 59.58% ±5.21, Argon 77.86% ±5.30. Sonnet page discloses 54 fallback runs, 46.55%, and 8 refusals, 6.90%. | "How would you test it?" | Genuine new ground, but harder to explain honestly in 15s. Policy and fallback behavior confound an underlying-model interpretation. Reserve for a longer piece. |

All score values above come from the same evaluator's current model pages, not vendor launch comparisons:
- https://www.vals.ai/models/anthropic_claude-sonnet-5-5
- https://www.vals.ai/models/google_gemini-4-argon

## Top concept: editorial claim
"Argon scores higher on these published legal tests. That still does not make legal work safe to leave unreviewed."

Avoid "Gemini is a better lawyer," "Claude cannot do law," "AI fails 80% of legal work," or universal task-success percentages. These are bounded benchmark results, using model-mediated grading and specific published product configurations.

## Full 450-frame plan
1080 x 1920, 30fps, frames 0-449. Clay 2.5D, pale light stage, separate moving assets, no single morphing carrier.

| Frames | Time | On-screen content | Motion and composition |
|---|---|---|---|
| 0-29 | 0-1s | "Higher score." | Clay Claude/Gemini name tiles enter separately from opposite sides. One modest legal document stack lands centrally; no gavel or authority theatre. |
| 30-59 | 1-2s | "Still needs review." | A small reviewer-check icon enters beside the documents. Hook remains quiet; background travellers keep subtle motion. |
| 60-89 | 2-3s | "Legal Research Bench" | Benchmark label slides in; two fixed-name score carriers enter beneath the one hero illustration. |
| 90-119 | 3-4s | Sonnet 5.5: 48.08%; Argon: 54.81% | Once-only score reveal, settle before the next second. Equal 0-100 visual scale if bars are used; no exaggerated gap. |
| 120-149 | 4-5s | "Every check must pass." | Small all-pass rubric motif beside the document, not a new wall of text. Values stay fixed and readable. |
| 150-179 | 5-6s | Same scores and label | Reading hold with tiny idle breathing. No winner crown or universal recommendation. |
| 180-209 | 6-7s | "Harvey Legal Agent Benchmark" | Research label, score carriers and document exit separately. New carriers and clay work-product folder enter independently in overlapping depth lanes; one continuous stage. |
| 210-239 | 7-8s | Sonnet 5.5: 2.92%; Argon: 19.58% | New scores reveal once. Clearly labelled "Final score". Do not animate the old numbers into the new ones. |
| 240-269 | 8-9s | "Higher. Still below 20%." | Argon tile comes slightly forward. No giant celebratory badge. Sonnet remains legible. |
| 270-299 | 9-10s | Same scores, "Final score" | Hold so the viewer can understand that these are a different benchmark and scoring setup, not a drop on the same test. |
| 300-329 | 10-11s | "Keep human review." | Scores retreat; reviewer-check illustration comes forward without stamping a generated legal document as actually approved. |
| 330-359 | 11-12s | "Published runs. Different settings." | Logo/name tiles at equal depth, caveat readable. This wording remains mandatory until matched run settings are verified. |
| 360-389 | 12-13s | "Would you trust it?" | Navy comment pill rises into lower safe area. |
| 390-419 | 13-14s | Same CTA | Gentle idle motion and clean reading hold. |
| 420-449 | 14-15s | Same CTA plus source rail | End hold. No purchase/access/switch invitation. |

Suggested optional voiceover, around 33 words:
"Argon scores higher on legal research. But on Harvey's stricter legal-work test, its final score is still below twenty percent. Different settings, published runs. Keep human review. Would you trust it?"

Caption-first works without voiceover. Source rail through the score beats: "Vals AI / checked 4 Oct 2026". Full names must appear before shortened "Sonnet" or "Argon" labels. Do not put all source URLs in the video; place them in the publication description with caveats.

## Fact list and evidence
### Legal Research Bench
- Current Sonnet model page: 48.08% ±3.47; 11 fallbacks (5.29%); 3 provider refusals (1.44%), scored as failures.
- Current Argon model page: 54.81% ±3.46.
- Calculated difference: 6.73 percentage points. Published bands overlap slightly; do not assert statistically established superiority from the point values alone.
- Primary metric is all-pass: the response must satisfy every required rubric element. Shared five-tool harness, three-hour task limit. Not financial partial credit and not Harvey's work-product benchmark.
- Operator methodology: https://www.vals.ai/benchmarks/legal_research
- Public harness/examples: https://github.com/vals-ai/legal-research-bench
- Paper: https://arxiv.org/html/2610.00609 . Its thirteen-model snapshot is older and is not the source for the latest scores. Judge validation numbers differ between the paper and live explainer; do not quote either as a current match-specific result.

### Harvey's Legal Agent Benchmark
- Current Sonnet page final score 2.92% ±1.36; Argon 19.58% ±3.31.
- Calculated difference: 16.66 percentage points. No headline "6.7x better": it is misleading on a low-score, narrow benchmark comparison.
- Final score is the average of two judges' task pass rates. For each judge, a task passes only if every criterion passes. The task concerns legal work products using files, documents, spreadsheets and presentations; it is not simply answering a legal question.
- Common offline environment, six file/command tools and three document skills. Internet access disabled. Do not use a browsing animation to depict this benchmark.
- Definition and environment: https://www.vals.ai/benchmarks/hlab
- "Below 20%" describes Argon's published final score, not all legal work, not percentage of criteria passed, and not a precise count of real-world legal tasks successfully completed.

### Settings/comparability gate
The Vals model pages show defaults:
- Sonnet: temperature 1, maximum output 128,000, compute effort Max.
- Argon: temperature 1, maximum output 262,144, reasoning effort High.
Both pages explicitly say particular benchmarks may use other providers or parameters. Therefore the defaults do not verify exact settings for these runs, nor are output limits or reasoning labels matched. Shared task harness and grading rules are verified; matched per-model reasoning budgets and exact run metadata are not.

The general methodology page says selected public benchmarks use a common harness/settings, but these proprietary legal tests cannot inherit an equal-compute claim from that general statement: https://www.vals.ai/methodology

Artificial Analysis was checked as an alternative. It exposes multiple Sonnet settings, but the current release headline is Max/default fallback; no fully verified current matched-setting Argon comparison was recovered in this research. Do not turn a similar "High" label into a claim of identical compute: https://artificialanalysis.ai/models/releases/claude-sonnet-5-5

### Source freshness
Vals explainer narrative leaderboards still discuss older model versions, while current model pages list Sonnet 5.5 and Argon. Used model pages for scores and explainer pages only for benchmark semantics. Recheck values, fallback policy and access immediately before export. Maintain "published runs" language, not a universal winner claim.

## Asset list, for later preparation only
Reuse: blue/peach clay name/score carriers; thinned light depth-lane background; small sphere/donut travellers; independent text overlays; source rail component; restrained shadow treatment and B8 lateral/bob helpers.
New: generic legal research document stack with blank abstract lines; work-product folder with separate file-tab silhouettes; small human-review/checklist icon; four fixed score text states (48.08%, 54.81%, 2.92%, 19.58%); two benchmark labels; final-score label; neutral caveat rail; navy trust-question CTA.

No identifiable client documents, real cases, made-up citations, official legal seals, or illustrative text masquerading as actual model output. No existing calculator needed; this must not look like Vid-2's finance beat. Do not use medical or biological props as a freshness shortcut.

## Style and production constraints
Premium matte clay realism, pale near-white base, blue/peach accent separation, soft directional shadows. Few hero props, limited glass, clear centred hierarchy. One grouped hero per beat, several independent elements crossing in and out, restrained tiny idle motion throughout. No obligatory whip-pan, no card morph and no score recount during swaps.

Use the existing series build-reference safe rect x48-888/y288-1248, type floors, and independent asset discipline. Exact full benchmark names must remain readable. If they cannot fit at the established minimum font size, revise the beat/layout or use a readable two-line label; do not silently shorten Harvey's test to the different Legal Research Bench. Font remains provisional. Final source/caveat layout and all 450 frames require visual inspection once actually built.

## Alternate concept semantics
Code Migration scores hidden behavior tests, not code prettiness, language fluency or percentage of entire migrations completed. Its operator defines equal-repository weighting, with the CLI split weighted three times the COBOL split. Definition: https://www.vals.ai/benchmarks/code-migration

CyberBench scores must retain policy/fallback caveats and cannot be presented as pure underlying security skill. Definition: https://www.vals.ai/benchmarks/cyber . Given the extra caveats and dual-use framing, this is the lowest-priority 15s candidate.

## Completion
Research and 450-frame content proposal complete. No build, generated assets, publication or repository mutation. Settings match remains unresolved; this is an explicitly qualified published-run plan, not a production-ready matched-settings comparison.
