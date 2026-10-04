# InsiderForce editorial Shorts: format research

Checked: 3 October 2026. Scope: exact InsiderForce references, then an original 15-second adaptation. Ghibli generation is outside this plan.

## Answer

The useful unit is a moving editorial layout, not a succession of finished posters. In two inspected InsiderForce Shorts, typography, screenshots, badges, rails and bullets enter at different times while other elements remain in place. Pale backgrounds, strong black type, soft shadows and restrained scale/tilt make a flat composition feel spatial. For a 15-second version, keep one promise, one visible transformation and one payoff. Do not squeeze an entire tools list into 15 seconds.

## Evidence boundaries

Both references were downloaded and their actual pixels inspected, including one-second samples of their first 16 seconds and quarter-second samples of the first reference's opening. The browser player buffered, but public downloads succeeded. These are approximately 69s and 60.681s videos, not 15s videos. Windows below are approximate observations from sampling, not frame-perfect cut measurements. No private retention data was available. Public popularity does not establish why viewers stayed. Product claims in their scripts were not independently verified and should not be repeated as facts.

## Real examples

### A. "You can now build a full APP for free."
https://www.youtube.com/shorts/3iUo7bnsN30

- Roughly 0-3s: floating app panels above and below a large two-line promise. Words accumulate rather than all arriving together. A small black highlight strip adds a curiosity line.
- Roughly 4-10s: the product name becomes the main typographic anchor. A raised website panel changes content independently; support text develops around it, with "OPEN SOURCE" and "TERMINAL" enlarged.
- Roughly 11-15s: the composition changes to the install idea, with a code/document panel and progressive small bullet lines.
- Later sampled frames: logo pills move along edge rails; terminal/document content and text remain separate; the ending changes into an ebook promotion.

### B. "Top 3 Claude Code Skills for Non-Designers"
https://www.youtube.com/shorts/0JZtdAtJiyk

- Roughly 0-3s: count, subject and outcome form a descending type hierarchy. A warm-coloured badge contrasts with the otherwise pale monochrome layout.
- Around 4s: the first named skill appears as a raised card. Subsequent frames change to a phone-shaped UI, independent corner badges on rails, and a growing bullet stack.
- Roughly 5-12s: the phone stays while bullet lines arrive individually. The composition makes accumulating information visible instead of cutting to a new slide for every line.
- Roughly 13-15s: a typographic payoff replaces the dense example. Later samples show another device mockup, typography examples and an outro mark.

## What to borrow, what to avoid

| Priority | Borrow | Why it fits a 15s automation template | Avoid |
| --- | --- | --- | --- |
| 1 | Outcome visible from the opening | The viewer can understand the promise before reading a paragraph | Greeting, logo intro or empty first frame |
| 2 | One persistent object that changes state | It creates continuity and a visible payoff | Unrelated screenshots and hard cuts posing as animation |
| 3 | Type hierarchy and selective emphasis | One important phrase wins attention; supporting text can stay smaller | Every word shouting, illegible website text presented as proof |
| 4 | Separate cards, masks, rails and captions | Each layer can have reusable motion and can be retimed without repainting | Flattened text inside a screenshot |
| 5 | Brief entrances followed by readable holds | Motion introduces information; holds let the viewer absorb it | Endless bouncing or several equally loud movements |
| 6 | Original visuals and accurate claims | The template can become the channel's own format | Reusing their brand, ebook CTA, script, music or product hype |

## Pacing recommendation, not a measured rule

- 0-1s: already show the problem and destination. No blank lead-in.
- 1-3s: state the promise; establish the object that will transform.
- 3-6s: show the action beginning.
- 6-11s: build the result with two or three visibly distinct steps.
- 11-14s: hold the useful payoff.
- 14-15s: a purposeful visual reset or brief final line, not a long CTA.

Use meaningful changes roughly every 1-2 seconds as a starting design choice, not a mandatory cut rate. Keep one leading movement at a time and let secondary layers move quietly. The inspected references often preserve a layout while revealing words or bullets inside it. That is the important difference from slideshow motion.

## Retention: what is grounded

YouTube's January 2025 interview reports Jenny Hoyos's view that a Short has about one second to hook a viewer and describes concise mini-stories and 15-second moments. It supports an immediate promise and a small complete story, not a guarantee of reach.

YouTube Help defines "Stayed to watch" as the percentage who stayed past the initial seconds, and "Engaged views" excludes loops. Average duration and percentage viewed for Shorts are based on engaged views and their watch time. Check the opening decision separately from what happens during the body. Compare like-length videos in the user's own channel; do not declare an arbitrary percentage a universal success bar.

Hypotheses to test after publication, only if the user chooses to publish:
1. Immediate before/after context should improve opening clarity.
2. A visible progressive transformation should help the middle feel purposeful.
3. A completed payoff followed by a visual loop may encourage a second look.

No claim is made that these elements caused InsiderForce's results. A confusing loop or unreadable rapid caption can harm the viewing experience. Never hide the promised payoff to force a rewatch.

## Programmatic route

Use a renderer with an explicit frame clock and a scene graph. Remotion's documented timing and layering primitives demonstrate one suitable implementation, but the plan is renderer-neutral. Animate position, opacity, scale, rotation and masks from frame values. Do not rely on wall-clock CSS animations or randomized motion during export. Pin the implementation version and test local-frame semantics; the fetched Sequence documentation contains malformed examples, so it is not copy-paste implementation code.

## Unknowns and next step

- No exact channel-wide cadence, retention or causal performance analysis was available from this two-video sample.
- The visual downloads were 360x640. They establish layout and movement, not production-resolution texture quality.
- The companion plan is a proposal, not a rendered video or working automation.
- Next: render a silent 15-second animatic of the plan, inspect it on a phone-sized preview, then time a real voiceover. No paid generation is needed for the mock UI itself; any chosen renderer/font/audio licence must be checked before distribution.

## Sources

All fetched or visually inspected on 3 October 2026. Publication dates are listed only when verified on the fetched page.

1. InsiderForce, actual video + transcript: https://www.youtube.com/shorts/3iUo7bnsN30
2. InsiderForce, actual video + transcript: https://www.youtube.com/shorts/0JZtdAtJiyk
3. YouTube Team, 28 January 2025: https://blog.youtube/creator-and-artist-stories/youtube-shorts-deep-dive/
4. YouTube Help, metric definitions: https://support.google.com/youtube/answer/12220281
5. YouTube Help, retention: https://support.google.com/youtube/answer/9314415?co=GENIE.Platform%3DDesktop&hl=en
6. Remotion, timing documentation: https://www.remotion.dev/docs/sequence
7. Remotion, interpolation documentation: https://www.remotion.dev/docs/interpolate
8. Remotion, layering documentation: https://www.remotion.dev/docs/absolute-fill
9. Remotion, spring documentation: https://www.remotion.dev/docs/spring/
10. Prepublish Team, 13 July 2026, secondary commercial editorial: https://prepublish.ai/blog/viewed-vs-swiped-away-youtube-shorts

The secondary article's universal-looking numeric benchmarks and unsupported dropout statistics are not adopted. Source coverage includes primary videos, first-party platform/editorial guidance, technical documentation and secondary editorial analysis.
