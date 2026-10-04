# Notes-to-actions: 15s editorial Short v1

Date: 3 October 2026. Status: playable review render, not published.

## Deliverables

- `notes-to-actions-v1.mp4`: H.264 + AAC, 1080x1920, 30fps, 450 video frames, exactly 15.000 seconds.
- `render.py`: deterministic editable production source.
- `manifest.json`: 34 unique visual node IDs, asset references and beat windows. Animation rules currently live in the renderer, not a fully declarative arbitrary-topic animation engine.
- `assets/`: separate transparent raster resources for the shells, labels, chips, paper and grid. All text is editable in the production source and rerendered from the font; it is not an editable vector layer inside the MP4.
- `original-cues.wav`: locally synthesised original quiet action sounds. No voiceover, copied music or external audio.

## Design and movement

Borrowed the supplied InsiderForce references' pale paper/grid, black and grey sans typography, enlarged important words, raised white panels, soft shadows, black caption strips, and progressive independent reveals.

An already-visible note transforms into three separate task cards. Text travels from source coordinates into the cards; note lines fade as their task text appears. Owners arrive individually, followed by deadlines, then drawn checkmarks. The note disappears and output cards widen and recenter. The settled payoff stays readable before the final paper wipe resets to the opening pose.

Six story beats stay at 0-2, 2-4, 4-6.5, 6.5-9, 9-12.5 and 12.5-15 seconds. Final reset begins at 14.2s. Headlines use staggered short fade/vertical-reveal transitions rather than overlapping illegible text. Cubic easing, fixed frame values, and seeded sound synthesis avoid wall-clock jitter.

## Choices and limits

This is the original fictional notes-to-actions demo proposed in the plan, not a real product screen or verified claim about a tool. Names/task labels are invented. Today and Tomorrow are example chip labels, not actual commitments.

No source creator logo, script, music, screenshot or promotional CTA is copied. Style is adapted, not frame-for-frame reproduction of their scenes.

Native transparent typography and UI assets were chosen rather than Nano Banana/remove.bg. For this text/card composition they avoid generated lettering errors and background-removal halos. Generated illustrative hero objects remain a possible later improvement, not needed for this render.

The composition follows the 34-node inventory, but geometry was tuned for readability: a larger raised demo panel, 330px-wide initial output cards and 546px-wide settled cards. Chip text is 30px, initial task labels fit to their card, then reach 43px in payoff. The original 39-word narration has not been recorded; captions are visual beat summaries, not speech-aligned subtitles.

There is no elaborate 3D camera, photorealistic generated object, phone mockup or branded rails. This v1 tests the reference's clean moving editorial grammar with an original UI story. Quiet original action sounds are included; voice and a music bed remain future creative choices.

## Verification

Inspected actual MP4 sampled pixels, the full 20-frame boundary/entrance contact sheet, three dense 0.2s sampling sheets across all 15 seconds, and phone-size 360x640 output. A first transition pass briefly superimposed old and new headlines; revised it to separate their exit and entry, then inspected the updated transition sheet and updated MP4. Checked opening, scan, migration, chip stack, checkmarks, payoff, closing and wipe/reset. Essential content is inside the intended working region, with no text clipping in inspected output. A real platform UI overlay has not been tested, and a normal-speed human playback review remains useful for subjective rhythm/audio judgment.

`ffprobe -count_frames` verified 450 frames, 30/1fps, 1080x1920, 15.000 seconds. Final-frame reset pixels equal the first-frame composition by construction. Every video frame decodes successfully in the full ffmpeg verification pass.

## Reproduce

Python 3 with Pillow 12.3.0 and NumPy 2.2.6, ffmpeg, local Liberation Sans Regular/Bold. Run `python3 render.py`. Source font paths are Linux-specific and should be changed on other systems. Liberation Fonts use SIL Open Font License 1.1; the installed font licence is included. No font binaries are bundled.

## References supplied for this build

- https://www.youtube.com/shorts/3iUo7bnsN30
- https://www.youtube.com/shorts/0JZtdAtJiyk

Visual comparisons use the supplied first-16-second contact sheets. Their full videos were not re-downloaded for this production pass; no retention or popularity claims are made.
