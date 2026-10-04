# Why this Clay SaaS ad feels premium

A builder's motion and visual checklist, based on the attached 24.87-second, 30 fps reference. Times below are approximate scene boundaries read from sampled frames; they are useful targets, not frame-accurate keyframe data. The source does not expose its original easing curves, so easing descriptions are visual readings, not recovered editor settings.

## The core recipe

The ad earns polish through **selective change**. Most of the frame is a quiet, nearly white field. One compact object or phrase appears, becomes legible, and gets time to land. Transitions are soft and controlled; the interface's geometry stays stable. The sequence alternates concrete product evidence with very short verbal claims, then gives the logo a comparatively long, clean finish.

The premium feeling is not “more animation.” It is clear hierarchy, low motion density, consistent restraint, and enough stillness for the viewer to read.

## Motion map

| Approx. time | Beat | What changes | What stays still / why it works |
|---|---|---|---|
| 0.0-1.3 s | “We've all been there” | A short line resolves from a soft, faint entrance into crisp black type. | The pale background and centered composition do not compete. The phrase gets roughly 0.8 s of readable stillness after its entrance. |
| 1.5-3.7 s | Messy research inputs | Three small issue cards arrive and stack vertically; a stale-data card appears as a second example. | Cards keep their rounded rectangles, icon/text/button layout and compact scale. The entrance is staged rather than making every card fly independently. The first stack has a short read hold before the next example. |
| 3.9-5.8 s | “Hours [clock] of manual research” | The phrase assembles in a few restrained steps: “Hours,” clock, then the rest of the sentence. | No large camera move or background transition. The clock is the only expressive symbol. The completed claim holds for about 0.7 s before the next beat. |
| 6.0-7.3 s | “Meet Clay” | Type and the small Clay mark appear together. | Centered type, mark and white field remain the whole composition. A clean, short pause makes this a chapter marker. |
| 7.5-9.7 s | Product/customer cards | A sparse grid is revealed in sequence, with cards appearing across it one at a time. | Grid lines and card design remain consistent. Sequential reveal gives the eye a path; it avoids a simultaneous wall of cards. |
| 9.9-11.5 s | “All in one place” | A single centered phrase replaces the grid. | The empty field returns, allowing the claim to read without interface clutter. Hold is about 1.3-1.5 s. |
| 11.8-13.3 s | Workflow strip | A compact horizontal flow appears: inputs, Clay, then an output/result. | Components retain a shared baseline and clear gaps. Movement is lateral and purposeful, not decorative. The strip stays small enough to read as one system. |
| 13.5-14.3 s | “Automatically!” | One word takes over the frame. | The workflow disappears rather than lingering behind the claim. The word gets a short, uncluttered hold. |
| 14.7-18.6 s | AI message workflow | A wide, low interface enters; the prompt fills in progressively and the surrounding message/workflow context becomes visible. | The UI is the subject, not an excuse for camera choreography. Text changes are the action; the panel's structure stays calm. This is the longest explanatory product beat, about 4 s. |
| 19.0-19.7 s | “Your pipeline” | The interface yields to a centered phrase. | A quiet reset between detailed product proof and closing claims. |
| 19.8-20.8 s | “Always clean” | Short claim appears. | Same placement and type treatment as the other claims. No new visual flourish. |
| 21.0-21.7 s | “Always ready” | Next short claim replaces the prior one. | Same scale and center, preserving rhythm through repetition. |
| 21.8-24.7 s | Clay mark + clay.com | The logo/URL resolves into a centered end card and stays visible to the end. | This is a deliberate long hold, roughly 2.8 s. The end card does not keep animating after it has landed. |

## Timing and easing: the feel to reproduce

- **Use a soft ease-out for entrances.** The visible change is quick enough to keep the ad moving, then settles without a sharp stop. Think “glide to rest,” not spring. A starting point for testing is `cubic-bezier(0.22, 1, 0.36, 1)` over roughly 350-550 ms for a card or phrase entrance; this is a practical approximation, not a measured curve from the source.
- **Use a gentle ease-in-out for fades and scene handoffs.** Avoid a linear opacity ramp that looks mechanical. Keep crossfades brief enough that the outgoing and incoming ideas do not become a muddy double exposure.
- **No overshoot or bounce.** There is no visible elastic landing, wobble, or repeated settling. Objects arrive once and become still.
- **Let opacity do much of the work.** Faint-to-crisp phrase entrances and soft UI reveals read more quietly than large travel. If adding scale, keep it tiny (for example, 0.98 to 1.00) and make it subordinate to the fade.
- **Build phrases in meaningful chunks, not letter-by-letter by default.** A short staged reveal can direct attention (the clock between “Hours” and “of manual research”); prolonged typewriter effects would make the same language feel less composed.
- **Give every beat a read hold.** Most short claims sit still for around 0.6-1.4 s after resolving. Give complex UI about 3-4 s. Reserve the longest hold for the brand/end card, around 2.5-3 s.
- **Keep transitions short relative to the hold.** Motion is a handoff, not the content. If the viewer notices the easing more than the new idea, reduce distance, duration, or stagger.

## How much should move at once?

Use **one primary moving group per beat**. A few related elements may follow in sequence, but do not animate every visible property independently.

- Cards: reveal the stack or grid in a small number of coordinated steps. Keep each card's contents internally stable.
- Workflow: move/reveal the connected group along its reading direction. Do not also rotate, bounce, pulse, and pan the camera.
- Text: change the phrase or reveal a relevant symbol; leave unrelated UI still.
- UI forms: allow the prompt/content to progress while panel edges, buttons, and background stay anchored.
- Between beats: clear the prior subject before asking the eye to read the next claim. The ad repeatedly returns to empty space as a visual reset.

A useful production cap: at any instant, only one visual event should demand attention. Supporting motion may occur, but it should be low contrast and subordinate.

## Shadow and surface language

- Use very light, broad, low-opacity shadows under the small white cards so they separate from the off-white field without looking elevated like floating hardware.
- Prefer soft ambient separation over a dark, sharp drop shadow. Avoid colored glow, hard outlines, glossy highlights, and dramatic depth.
- Keep cards white or near-white against a slightly tinted light background; let the subtle edge/shadow do the separation.
- Use consistent corner radii and restrained internal spacing. The cards feel like real product UI because their edges and components behave consistently, not because they have heavy effects.
- Keep the background flat and quiet. Do not add gradients, texture, particles, or ornamental light unless the product itself requires them.

## What does not move

- The overall canvas and background remain fixed.
- Type does not drift after it lands; its position and alignment are stable across claims.
- Card geometry, text hierarchy, buttons, and icon placement do not wobble or reflow for decoration.
- Grid lines and workflow alignment remain calm while the relevant cards/steps are revealed.
- The composition does not continuously zoom or pan to manufacture energy.
- The logo/end card becomes still after its entrance.

This stable frame is a major part of the premium effect: movement has a clear cause, so the product looks assured rather than busy.

## Restraint patterns to preserve

1. **Alternate evidence and assertion.** Show the pain/product, then let a short line summarize it. Do not narrate every UI detail with extra labels.
2. **Return to negative space.** Empty frames are purposeful pauses, not missing content.
3. **Keep color rare.** Mostly neutral surfaces and black type; color lives in product marks, small UI accents, and calls to action.
4. **Use one visual metaphor at a time.** The clock makes “hours” tangible; the pipeline diagram makes automation tangible. Avoid layering extra metaphors onto the same beat.
5. **Repeat a visual grammar.** Similar centered claim placement, stable card style, and consistent reveal behavior make the film feel designed as one piece.
6. **Do not animate for animation's sake.** Every move introduces an idea, shows a relationship, or helps reading order.
7. **End decisively.** Let the mark and URL remain legible. No last-second extra transition or competing callout.

## Builder checklist

### Before animation
- [ ] Write one intended takeaway for each beat; remove any object or line that does not serve it.
- [ ] Choose the reading order before choosing the motion.
- [ ] Set the neutral canvas, card radius, type scale, button treatment, and shadow once; reuse them.
- [ ] Decide which elements are anchors. Keep the canvas, card geometry, and recurring text alignment fixed.

### For each entrance or transition
- [ ] Is there only one primary event for the eye to follow?
- [ ] Does the move have a reason: reveal, connect, focus, or clarify sequence?
- [ ] Can a fade and very small scale change do the job instead of a large translation?
- [ ] Does it ease gently into rest, with no bounce or overshoot?
- [ ] Are related elements staggered in a small, readable number of steps?
- [ ] Does the prior beat clear cleanly rather than cluttering the next one?

### For pacing
- [ ] Does each short claim get about 0.6-1.4 s of still reading time after it lands?
- [ ] Does detailed UI get about 3-4 s, with enough time to parse its hierarchy?
- [ ] Is the end card held for about 2.5-3 s?
- [ ] Are transitions shorter and quieter than the holds?
- [ ] Is there a deliberate still/negative-space reset between dense product demonstrations?

### For surfaces and polish
- [ ] Are shadows broad, faint, and consistent, with no hard dark edge or glow?
- [ ] Is depth subtle enough that the UI still feels like a product, not a stack of floating promo cards?
- [ ] Are color accents limited to meaningful UI/brand signals?
- [ ] Are type, icons, buttons, and card internals stable while their group reveals?
- [ ] Does nothing keep drifting, pulsing, or zooming after it has communicated its point?

### Final review
- [ ] Watch once at normal speed without pausing: can every beat be understood on first viewing?
- [ ] Watch muted: does the visual sequence still make sense?
- [ ] Check that fades do not wash out small UI text or make shadows flicker.
- [ ] Remove any motion that calls attention to itself more than to the product.
- [ ] Confirm the final mark and URL have a clean, motion-free reading hold.

**Practical note:** the source is a flattened video, so exact original keyframe curves and sub-frame durations cannot be recovered from inspection. Use the timings and easing above as a reproducible target, then tune against the supplied reference at full playback speed.
