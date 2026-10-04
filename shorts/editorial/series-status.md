# Claude-vs-Gemini Shorts: series status
As of 4 October 2026, 15:40 BST. Repository: `tanyoganand-ops/instinct-codebase`.

## At a glance
| Track | Current state | Next decision |
|---|---|---|
| Vid-1 | v14c delivered to P; awaiting verdict. Not final-approved or published. | P's v14c verdict. |
| Vid-2 | Apps-versus-finance recommended; plan and reusable clay pack committed. Concept pick pending; no video built. | P's concept choice, then verify comparability before production. |
| Vid-3 | Legal reliability recommended; plan and reusable clay pack committed. No video built or final concept approval. | P's concept choice, then verify comparability before production. |
| UGC | Three animated style-pitch previews delivered and committed. Not submittable real-use demos. | Real product usage/footage and each programme's required approval/application steps. |

## Vid-1: use v14c as the current candidate
Direction: v13b foreground animation language with B4d background assets, a plain-background zoom hook, B8 perspective trade and B6 whip-slide used sparingly, and the existing cue-bed/whoosh mix. Earlier versions remain as history, not the preferred candidate.

v14c joins entrance, perspective trade and exit into a continuous trajectory instead of switching transforms at hard boundaries. The trade is padded to 0.85s; the whip is padded to 18 frames with less blur. Reading-area props fade while crossing essential copy, then return at the margins. Content, hook, B4d assets, sound mix and CTA are unchanged. Latest notes report 450 frames/15s and inspection of encoded hook, trade and handoff frames. Audio signal/timing was checked, but no subjective listening pass is recorded.

Content: Claude Sonnet 5.5 versus Gemini 4 Argon. Artificial Analysis Terminal-Bench 4.0: 64 versus 57; AutomationBench-AA: 71 versus 78. These are rounded published-run values, not universal capability ratings. Verdict: different tests, different winners. CTA: `Comment VIDEO`. Keep source/date/configuration context and the Argon access caveat with the work. Recheck facts at final export.

### Current candidate and supporting files
- `shorts/editorial/1-claude-vs-gemini-v14c-448c7574.mp4`
- `shorts/editorial/2-encoded-polish-qa-2de70649.png`
- `shorts/editorial/3-claude-gemini-v14c-source-bank-0c4342de.zip`
- `shorts/editorial/2026-10-04-claude-gemini-v14c-build-notes-f75cc540.md`
- `shorts/editorial/450-frame-plan-v14c-863f0db9.md`

### Direction references
- `shorts/editorial/final-build-spec.md`: earlier consolidated reference; latest v14c notes take precedence where motion/background details changed.
- `shorts/editorial/bg-asset-spec-b4d.md`
- `shorts/editorial/10-claude-vs-gemini-v13b-7da63fbb.mp4`
- `shorts/editorial/12-claude-gemini-v13b-source-bank-2433b813.zip`
- `shorts/editorial/2026-10-04-claude-gemini-v13b-build-notes-652936d5.md`
- `shorts/editorial/insider-branches/1-clay-b4d-blue-orange-anim-eb846df7.mp4`
- `shorts/editorial/insider-branches/2-clay-b4d-source-21ef794a.zip`

## Vid-2: apps versus finance
Recommended hook: `Building apps? Almost level.` Then `Finance changes the gap.` CTA: `Comment your task.`

Current Vals model-page values, checked 4 October:
- Vibe Code Bench v1.1: Sonnet 92.39%, Argon 91.91%.
- Finance Agent v2: Sonnet 58.10%, Argon 65.40%.

Vibe score concerns functional app tests, not design quality or perfectly completed apps. Finance uses dealbreaker-gated partial credit, not percentage of wholly successful analyst tasks. The app-score gap is small relative to reported uncertainty; do not call it a decisive winner or a formal statistical tie. Sonnet's finance result includes disclosed fallback behavior.

Plan includes three concepts, a 450-frame recommended timeline, sources, narration option and assets. The committed pack contains clay laptop, filings, calculator, four deterministic score states, blank carriers and separate text overlays. Alpha and pale/dark composites were checked. These are independently movable raster sprites, not 3D meshes or internally layered props. Font and final phone-scale layout remain provisional. No vid-2 render exists.

### Exact paths
- `shorts/editorial/vid-2-content-plan.md`
- `shorts/editorial/1-vid2-clay-assets-bcf9a06b.zip`
- `shorts/editorial/2-alpha-check-c1d7497d.png`
- `shorts/editorial/3-pale-dark-composite-check-4c5cb74f.png`

## Vid-3: legal reliability
Recommended hook: `Higher score. Still needs review.` CTA: `Would you trust it?`

Current Vals model-page values, checked 4 October:
- Legal Research Bench: Sonnet 48.08%, Argon 54.81%.
- Harvey's Legal Agent Benchmark final score: Sonnet 2.92%, Argon 19.58%.

The narrative is reliability, not "Gemini is a better lawyer". Legal Research Bench is all-pass legal research. Harvey measures legal work products and reports the average of two judges' task pass rates, with every criterion required for a pass. `Below 20%` describes Argon's published Harvey final score, not all real-world legal work. The research-score uncertainty bands overlap slightly; point estimates alone do not establish statistical superiority.

Plan includes legal reliability, code migration and cybersecurity/policy alternatives, with a full 450-frame top-concept timeline. Pack includes generic research papers/magnifying glass, work-product folder, review clipboard with empty boxes, four score states, blank carriers and separate overlays. Full Harvey name wraps onto two lines. Alpha and pale/dark composites were checked. No fake citations, client data or approval stamps. Same raster/font/layout limits as vid-2. No vid-3 render exists.

### Exact paths
- `shorts/editorial/vid-3-content-plan.md`
- `shorts/editorial/1-vid3-clay-assets-4945816f.zip`
- `shorts/editorial/2-alpha-check-988ec575.png`
- `shorts/editorial/3-pale-dark-composite-check-0e4c43bc.png`

## Settings-comparability gate for vid-2 and vid-3
Values come from Vals' own current model pages:
- https://www.vals.ai/models/anthropic_claude-sonnet-5-5
- https://www.vals.ai/models/google_gemini-4-argon

Shared benchmark harness/scoring definitions are verified. Equal reasoning/compute settings are **not** verified. Model pages show Sonnet Max/128k output and Argon High/262k output defaults, and explicitly warn individual benchmarks can use different providers or parameters. Do not present either proposed Short as an equal-compute or matched-reasoning head-to-head. Keep `Published runs. Different settings.` If exact matched settings are required, production must wait for verified run metadata or a replacement comparison.

Benchmark explainer pages have older narrative leaderboard summaries than the current model pages. Use current model pages for dated scores and explainers for scoring definitions. Recheck scores, policy/fallback effects and Argon access before publication. Detailed definitions and source URLs are in each plan.

## UGC: three style-pitch previews, not application-ready demos
GenieAI, Pallo and ThetaWave each have a 15s animated illustration preview. They are style-pitch assets, labelled illustration/not sponsored, with no fake product usage, UI, testimonial or invented result. They do not satisfy real-use demo requirements. P needs genuine product experience and recorded footage for submittable versions; do not fill real-result placeholders with invented examples. No company submission, sponsorship or public posting is recorded.

GenieAI's process includes concept approval before recording. Pallo requires real app/canvas use; its rate needs written confirmation before committing work. ThetaWave asks for authentic study use. Concept pre-approval is programme-specific, not a blanket claim that all three use identical approval rules. Recheck each current brief before applying.

### Concept brief
- `research/ugc-content/ugc-spec-ad-concepts-2026-10-04.md`

### GenieAI preview
- `research/ugc-content/1-genieai-animated-spec-concept-v1-a3f176aa.mp4`
- `research/ugc-content/2-encoded-qa-27dba0f6.png`
- `research/ugc-content/3-genieai-animated-spec-concept-v1-source-c1ef35f6.zip`
- `research/ugc-content/build-notes-8ea24584.md`
- `research/ugc-content/450-frame-plan-c281475a.md`

### Pallo preview
- `research/ugc-content/1-pallo-animated-spec-concept-v1-4748cc33.mp4`
- `research/ugc-content/2-encoded-qa-a0768a95.png`
- `research/ugc-content/3-pallo-animated-spec-concept-v1-source-39465c04.zip`
- `research/ugc-content/build-notes-65044f01.md`
- `research/ugc-content/450-frame-plan-9d8a975e.md`

### ThetaWave preview, corrected source/notes
- `research/ugc-content/1-thetawave-animated-spec-concept-v1-c6204aba.mp4`
- `research/ugc-content/2-encoded-qa-ee50f345.png`
- `research/ugc-content/3-thetawave-animated-spec-concept-v1-source-5f8d0667.zip`
- `research/ugc-content/build-notes-e5c56a61.md`
- `research/ugc-content/450-frame-plan-66e09924.md`

Use the corrected ThetaWave source and notes above. The notes record one identical adjacent pair in the downsampled audit, not zero; no prolonged static hold. Earlier superseded variants are not the current source.

## Pickup order
1. Get P's v14c verdict before declaring vid-1 finished.
2. Confirm vid-2 concept; resolve or explicitly retain the published-run settings caveat; then build and inspect the chosen timeline.
3. Confirm vid-3 concept and the same comparability gate before building.
4. For UGC, replace illustrated pitch material with genuine usage footage only after checking the relevant programme's brief and approval process.

Numeric filename prefixes and hash suffixes are upload artifacts, not sequence or approval markers. Keep exact paths when opening source packs. This status file is a snapshot, not permission to publish, send company pitches, submit applications or spend money.
