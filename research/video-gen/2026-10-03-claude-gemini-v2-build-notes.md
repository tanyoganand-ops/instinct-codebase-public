# Claude vs Gemini: v2 production closeout

3 October 2026. Status: rendered review video. No channel publication performed.

## Content and approval

The owner confirmed the new topic as Sonnet 5.5 versus the new Gemini benchmark model, requested brand logos, requested second-by-second approval first, approved that plan at 16:57:17 BST, and added a comment CTA. The final wording is: "Want to make videos like this? Comment \"VIDEO\"". It replaces the earlier task-fit question during seconds 13-15.

The two charts use one independent evaluator, Artificial Analysis. Sonnet 5.5 at Max effort: Terminal-Bench 4.0 64%, AutomationBench-AA 71%. Gemini 4 Argon at High: Terminal-Bench 4.0 57%, AutomationBench-AA 78%. Colours and chart scales are consistent; each bar uses the same 0-100% base width. Both scorecards remain visible in the final stack. Verdict: "Different tests. Different winners." / "No overall winner from these two tests." A visible "ARGON: LIMITED ROLLOUT" badge preserves access context.

## Evidence

- Sonnet 5.5 launch, 28 September: https://www.anthropic.com/claude-sonnet-5-5
- Argon launch, 30 September, initial restricted rollout: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/
- Exact head-to-head score pairs and effort settings, read and re-fetched: https://artificialanalysis.ai/articles/gemini-4-argon-google-top-three-labs
- Exact benchmark naming: https://artificialanalysis.ai/models/gemini-4-argon

No vendor scores are mixed into the independent comparison. AutomationBench-AA is not the Zapier AutomationBench reported by Google. Anthropic's own Terminal-Bench score of 70.6% comes from a different setup and is not silently substituted for AA's 64%. The pairing is user-selected, not a statement that the models occupy identical product tiers. Scores do not establish universal superiority.

## Frame contract and implementation

`frames-v2.json` contains every one of the 450 frames, numbered 0-449, with exact per-node x/y, scale, rotation, opacity, bar progress and resolved count text. `450-frame-plan-v2.md` lists all 450 frames with visible asset values. `tracks-v2.json` stores editable source timing curves. These state artifacts are written before the renderer makes visual pixels. The renderer reloads and draws the saved JSON states; no wall clock animation, model decisions or random render motion.

57 logical nodes include paper/grid, logo carriers, hero words, question stamp, each chart group/shell/title/subtitle/axis/row label/track/bar/count/winner rule/effort label, winner captions, verdict, CTA, source rail, rollout badge and wipe. Exact inventory count is verified in the source validation output. Text is editable in code, rendered from a font; logos are received files, not generated approximations.

Reusable motion bank: clamp, linear, quintic ease-out, cubic ease-in-out, cubic ease-out, back easing and critically damped entrance; generic track/node expansion; exact-state JSON and Markdown writer. Reusable visuals are text, shell, rectangle/bar/rule, logo carrier, stamp/pill, grid and wipe. Bank components are actual production code, not just proposed names.

Motion changes: logo carriers dock to upper rails; comparison cards build independently; bars/counts animate together on equal scales; winner underlines draw; first chart shrinks and shifts before second chart arrives; evidence cards stack; CTA gets a readable hold; brief final wipe returns to the exact opening frame. Logo files retain their shape, colour and aspect ratio. Only carriers rotate during the entrance.

## QA

Inspected actual MP4 sampled pixels, 24 boundary/entrance contacts, 75 dense samples (every 0.2s across all 15 seconds), full-resolution representative charts and a 360x640 phone preview. Fixed a first-pass incoming-card overlap, a pre-delay visibility bug and an overly strong grid; regenerated the exact plan and inspected the revised render. Scores at animation endpoints match the approved values; opacity is bounded; all 450 unique frame numbers exist. Frame 449 pixel state equals frame 0. Full ffmpeg decode reports no errors.

Final ffprobe: H.264 + AAC, 1080x1920, 30/1fps, 450 video frames, 15.000 seconds, 1,142,165 bytes. Original quiet synthetic cues only, no borrowed music, no voiceover. A real platform-controls overlay was not tested. Dense sampled visual checks do not claim a normal-speed human playback/listening review, which remains useful for rhythm.

## Logo provenance and limits

Claude logo/Spark were supplied from Anthropic's press kit, reported by dedicated logo research as a redirect to an official CDN media ZIP. Source: https://anthropic.com/press-kit . Source report includes the ZIP https://www-cdn.anthropic.com/ae59ca4ca194dac9c9dc3bc78c5829468cb0e8af.zip . This production task visually inspected the received files; its own page fetch only returned a redirect page. No licence file was reported in the kit. Treat as trademarked identification in editorial context, not a grant for branding our channel.

Gemini is a Commons-hosted mirror, not a firsthand official Google download: https://commons.wikimedia.org/wiki/File:Google_Gemini_logo_2025.svg . Commons identifies Google LLC and About Gemini inline SVG, tags PD-textlogo and Trademarked. Supplied PNG is a rasterisation of the original SVG. The current mark visually matches the logo research reference, but current status was not independently proven through Google's application-gated brand portal. Preserve this caveat in asset provenance. No endorsement by either company is implied.

## Reproduce and resume

Python 3, Pillow 12.3.0, NumPy 2.2.6, ffmpeg and Linux Liberation Sans files. Liberation Sans is SIL OFL 1.1; licence text is included, font binaries are not. Source contains Linux font paths. Run `python3 production.py --preview` or `python3 production.py` after installing the dependencies.

The source ZIP uses root `shorts/editorial/`, with project files under `projects/claude-gemini-v2/`, brand originals/provenance under `banks/assets/logos/`, motion source under `banks/motion/`, and QA/verification. The renderer supports these repo-relative paths. The ZIP also includes the playable MP4 so the exact review output survives.

Next step: owner review of v2. No new third render or publication is authorised by this closeout. Revisions should change timing/data in the plan, regenerate all frame states, rerender and reinspect. Current progress is source and video complete, awaiting owner feedback.
