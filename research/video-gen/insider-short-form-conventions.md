# Insider-style short-form conventions (for the build fleet)

## Read this first: sourcing and limits

- P's reference channel is **InsiderForce** (youtube.com/@InsiderForce, AI-tools Shorts). The brief said "Business Insider / Insider", which is a different thing (Insider Inc., the publisher). I used both, labelled below. If the fleet should copy only one, it is InsiderForce.
- I could not watch video or inspect frames (YouTube blocks page fetches, 403 on the example Short). So **timing numbers for InsiderForce are not measured from their frames**. They come from (a) the scripts YouTube exposes for their Shorts, (b) published facts about Insider Inc.'s house style, (c) P's own steering across v1-v6 of the editorial Short (see memory), and (d) captioning guidance. Every rule is tagged: [SRC] = from a cited source, [P] = P's stated preference, [DEFAULT] = my recommended starting value, tune against P's reaction.
- Before building at scale: have someone frame-step 2-3 InsiderForce Shorts (e.g. https://youtube.com/shorts/3iUo7bnsN30) and confirm the [DEFAULT] numbers.

## 1. Structure and script (what is actually evidenced)

- InsiderForce Shorts are spoken, list or "here's what changed" scripts, 30-60 s, e.g. "Top 3 Claude Code Skills for Non-Designers" (first / second / third beats), "Claude Code Just Added Routines (Here's How They Work)". [SRC: YouTube Shorts 0JZtdAtJiyk, 52gdKYHeRJ0]
- Hook is the title claim in the first line ("make you look like a designer overnight"). One idea per beat, each beat = one named thing + one concrete payoff sentence. [SRC: transcript of 0JZtdAtJiyk]
- End card is a comment-keyword CTA: "Comment human and I'll send you my ebook... follow." Our end card should carry a comment CTA (P already asked for this). [SRC: 0JZtdAtJiyk; P]
- Insider Inc. template: Hook (most interesting moment first) -> intro -> experience -> behind the scenes. For our tech explainer map this to Hook -> claim -> 2-3 proof beats -> CTA. [SRC: typito.com]
- Built to work with sound off: every word of information is on screen as text. [SRC: Digiday 2016, BI 2018]

## 2. Kinetic typography behavior

- One line of text per scene, 2-6 words, one hero visual. Never two competing text blocks. [P: "one hero visual + one line of text per scene"]
- Emphasis by colour, not by size jumps: base text white (or ink on light bg), the key word in one accent colour. Insider Inc. does white text + green highlight on important words. [SRC: typito.com]
- Reading speed ceiling: 3 words/sec; a line must stay on screen at least ~1.5 s in a Short (2 s in captioning guidance for full sentences). Keep words and visual in sync with the VO beat. [SRC: unimelb.edu.au captioning guide; DEFAULT for the 1.5 s]
- Line length: max ~37 chars per line, max 2 lines. [SRC: unimelb]
- Type: bold grotesque, tight tracking, heavy weight. Insider Inc. uses Lab Grotesque (straightforward, minimal, legible). Anton was picked by P after "spindly" feedback; stay heavy. [SRC: typito; P]
- Text entrance: simple swipe left/right or drop-down, ~8-12 frames at 30 fps (0.25-0.4 s), ease-out. No fly-in-from-far, no zoom, no per-letter spin. [P: disliked fly/zoom; DEFAULT timings]
- Text exit: cut or the same swipe reversed, 4-6 frames, or simply replaced by the next scene's swipe. Never fade slowly. [DEFAULT]
- Word-by-word reveal only for the hook line and the CTA; elsewhere whole line enters as one unit. [DEFAULT]
- Safe zone: keep text out of the bottom ~20% and right ~12% (platform UI), top ~10%. [DEFAULT, standard Shorts UI]

## 3. Pacing and cut rhythm

- Something changes on screen every ~1.5-2.5 s (new asset, new line, or camera move). Dead frame > 2 s is a bug. [DEFAULT; the Ghibli research on the Rainlit Village Short found ~1.6 s cuts, in memory]
- Action in frame 1: no logo sting or title wait. Insider Inc. opens on the most striking shot. [SRC: BI 2016 "mesmerizing images of things coming into form"; Digiday 2016 "grab attention immediately"]
- 15 s Short budget (450 frames at 30 fps): hook 0-2 s, 3 content beats of ~3.5 s, payoff 11-13 s, CTA end card last 2 s. [DEFAULT, matches P's approved frame-plan format]
- Beat length can vary (2 s, 3 s, 4 s) so it doesn't feel metronomic; hold the payoff slightly longer. [DEFAULT]

## 4. Transitions

- Cut or directional swipe only, same direction as the entrance of the next element. One transition vocabulary per video. [P: "simple swipe left/right or drop-down"]
- Transition happens inside the background (the colour/gradient shifts) while text swaps, so the video reads continuous, not slideshow. P's strongest complaint was "looks like a slideshow". [P]
- No cross-dissolves, no glitch, no 3D flips. [DEFAULT]

## 5. How assets enter and exit

- Each scene has a hero asset (logo, UI card, icon, object). Enter: slide + 2-4% overshoot settle, 10-14 frames. Exit: slide off in the same axis or be pushed by the next asset. [DEFAULT]
- Assets are layered (bg / mid / hero / text) so the background keeps moving behind them: a silk-mesh or gradient wave must run **behind the text for the whole video**, not fade out before it. [P]
- Idle motion while held: slow drift or 1-2% scale breathing so nothing is frozen. [DEFAULT]
- Location pins and source tags (Insider Inc. shows a pin with the place name) map to our "source chip" or "tool name chip" in a corner. [SRC: typito]
- Brand mark: Insider Inc. shows the logo at start and as a watermark throughout, with a tagline end frame. Do the same with a small corner mark + end card. [SRC: typito]

## 6. Colour and surface treatment

- Light, whiter background with a visible, shifting colour gradient. No dark mode. Liquid-glass cards. [P]
- Limit palette: 1 ink, 1 paper, 1 accent. Avoid the "vibecoded" tells: purple-blue gradients, gradient hero text. [P; InsiderForce itself criticises "same fonts, same gradients" in 0JZtdAtJiyk]
- Bold, high contrast, "bolder" over refined. [P]

## 7. Pre-ship checks for the QA agent

1. Every 2 s window has a visible change. 2. One text line per scene, <= 6 words. 3. Entrances are swipe/drop only. 4. Background wave visible under text in every frame. 5. Text fully inside safe zone. 6. End card has comment CTA. 7. No dark bg, no purple-blue gradients. 8. Play at 1x on a phone-sized render and check it doesn't read as a slideshow.

## Sources

- InsiderForce channel: https://www.youtube.com/@InsiderForce ; channel bio via https://socialcounts.org/youtube-channel-analytics/UC8L6EV01fAJ2A0sDpsQ-T5g
- InsiderForce Shorts (scripts only): https://www.youtube.com/shorts/0JZtdAtJiyk , https://www.youtube.com/shorts/52gdKYHeRJ0 ; example given by P https://youtube.com/shorts/3iUo7bnsN30 (not fetchable, 403)
- Insider Inc. style: https://typito.com/blog/insider-inc-viral-video-design/ ; https://www.businessinsider.com/how-we-built-the-worlds-8th-most-watched-video-publisher-in-a-year-2016-10 ; https://www.businessinsider.com/insider-inc-30-second-video-views-2018-10 ; https://digiday.com/media/business-insider-facebook-video/
- Caption legibility: https://www.unimelb.edu.au/accessibility/video-captioning/style-guide
- P's preferences: memory workstream animated-shorts-series (feedback on editorial v1-v6)
