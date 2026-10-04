# Claude vs Gemini v3: uncluttered three-layer composition

3 October 2026. Review render, not published.

## Owner feedback applied

Keep the animation quality, remove the screenfuls of chart/text blocks. Each scene now has two hero logo carriers, one or two hero lines underneath, and slowly moving ambient background light. Full chart panels and dense scoreboard are removed. The four verified scores move into the hero carriers instead. Small factual/source rails are supporting metadata, not main reading blocks.

## Scene plan

- 0-3s: two brand carriers, "CLAUDE OR GEMINI?", short model-name line.
- 3-6.5s: same two carriers show Sonnet 64% / Argon 57%; "Sonnet leads here." and "Terminal-Bench 4.0" below.
- 6.5-10s: two carriers show Sonnet 71% / Argon 78%; "Gemini leads here." and "AutomationBench-AA" below.
- 10-13s: carriers return to brand identity; "Different tests. Different winners."
- 13-15s: two brand carriers; "Make videos like this?" / "Comment VIDEO" CTA; short wipe to opening.

The carriers are softly frosted, blur the underlying backdrop, preserve logo colours and aspect ratios, have bright rims and follow their depth shadows. This is restrained 2D composited glass, not physically simulated liquid refraction or true 3D modelling. The background is blue/violet softly drifting light with faint independent diagonal texture. It is not an evidence chart and carries no implied scores.

## Exact plan and verification

All 450 resolved states written before pixel rendering; renderer reloads `frames-v3.json`. Reused easing primitives from v2. Source has separate hero, type and background segments. JSON stores exact positions, rotations, opacity, score progress and score text for each visible node. Ambient motion uses the saved frame index and fixed deterministic equations in the source.

450-frame Markdown plan is `450-frame-plan-v3.md` (generated writer filename renamed from its generic v2 default). Technical output: H.264/AAC, 1080x1920, 30fps, 450 frames, exactly 15.000 seconds, 1,495,641 bytes. Full decode passes.

Visually inspected final MP4 samples, 20 boundary/entrance frames, 75 dense samples across the full timeline and 360x640 phone preview. First preview briefly emptied the hero at transitions; fixed visibility to keep the carriers present, reinspected and rerendered. No clipping in inspected output. Normal-speed human playback/audio judgment and real platform-overlay test are not claimed.

Motion is cleaner and less busy than v2, but intentionally reduced: carrier entrances, score counts, separate type reveals and background drift remain; complex chart compaction and scorecard stacking are gone with the clutter. This tradeoff follows the latest design direction, and owner review will decide if the simplification is too restrained.

## Grounding and assets

Unchanged Artificial Analysis pairs, Sonnet Max versus Argon High:
https://artificialanalysis.ai/articles/gemini-4-argon-google-top-three-labs
Exact benchmark names:
https://artificialanalysis.ai/models/gemini-4-argon
Model announcements:
https://www.anthropic.com/claude-sonnet-5-5
https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/

Source/date is visible during factual scenes and ending. Limited-rollout note appears during verdict and CTA. No universal superiority claim. No mixing with Zapier AutomationBench/vendor scores.

Claude asset source report: https://anthropic.com/press-kit . Gemini supplied Commons mirror: https://commons.wikimedia.org/wiki/File:Google_Gemini_logo_2025.svg . Retain v2 logo-provenance caveat, trademark discipline and no endorsement. Transparent originals included in source bank. Liberation Sans OFL licence included. Original synthetic cues reused; no narration/music.

## Resume

Source package contains frame engine, production source, all 450 states, tracks, plan, logos/provenance, cues, verification, MP4 and QA. No repo overwrite by this task. Await owner review. Future revision alters exact states before rerender.
