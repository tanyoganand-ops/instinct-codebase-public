# Transition-physics pack: snappy Insider-style moves
Canvas 1080x1920, 30 fps, 15 s = 450 frames. All values are starting points tuned for fast, clean, "swipe/drop" motion (P's steer: simple swipe left/right or drop-down, no fly/zoom, bold, liquid glass, one hero visual per scene). Spring numbers below were simulated (not guessed): overshoot and settle time are measured.

## 1. Golden rules
- Enter = decelerate (ease-out). Exit = accelerate (ease-in). Never ease-in-out for UI-style moves, it feels mushy.
- Enter slower than exit. Enter 10-14 f, exit 6-9 f.
- Travel is short for elements (60-200 px) and full-screen only for scene wipes. Long travel + short time = whip.
- One motion idea per scene. Max 2 things moving at once besides background.
- Stagger 3-4 f between siblings (never more than 5, or it reads slow). Max 4 staggered items.
- Hold time after settle >= 12 f (0.4 s) so the eye can read. Text readable: ~2 words per 0.25 s max.
- Overshoot only on hero/logo/pop moments. Text and cards: <=4%.
- Always animate opacity with position: 0 to 1 over the first 60% of the move.

## 2. Cubic-bezier library (CSS / GSAP CustomEase / Lottie)
| Name | cubic-bezier | Use |
|---|---|---|
| Snap-out (enter) | 0.16, 1, 0.3, 1 | default enter, expo-out feel |
| Quint-out | 0.22, 1, 0.36, 1 | text, cards |
| Back-out (soft overshoot) | 0.34, 1.56, 0.64, 1 | logos, badges, ~10% overshoot |
| Snap-in (exit) | 0.7, 0, 0.84, 0 | default exit, expo-in |
| Quint-in | 0.64, 0, 0.78, 0 | exit alt |
| Whip (in-out, fast middle) | 0.85, 0, 0.15, 1 | scene wipe, cuts with blur |
| Smooth (loops/bg) | 0.45, 0, 0.55, 1 | background drift, gradient shift |
| Linear | 0,0,1,1 | only for continuous drift/marquee |

## 3. Spring presets (Remotion spring(), framer-motion equivalent in notes)
Remotion: `spring({frame, fps:30, config:{damping, mass, stiffness}})`. Framer-motion: stiffness and damping same, mass same.
| Preset | damping | mass | stiffness | Overshoot | Settles (98%) |
|---|---|---|---|---|---|
| Tight | 26 | 1 | 300 | 2.5% | 10 f (0.33s) |
| Snappy | 20 | 1 | 200 | 4.0% | 13 f (0.43s) |
| Pop | 12 | 1 | 180 | 20.5% | 19 f (0.63s) |
| Bouncy | 8 | 1 | 150 | 33.6% | 28 f (0.93s) |
| Soft settle | 18 | 1 | 120 | 1.0% | 11 f (0.37s) |
| Heavy | 15 | 1 | 100 | 2.7% | 17 f (0.57s) |
Which one:
- Tight: text lines, small chips, UI labels.
- Snappy (default): cards, glass panels, headlines.
- Soft settle: big panels, drop-downs (no visible bounce).
- Pop: logos (Claude / Gemini), badges, check icons, CTA button.
- Bouncy: one playful moment per video at most (end card button).
- Heavy: large hero objects, 3D-ish scenes.
Add `overshootClamping:true` to kill bounce on any preset.

## 4. Enter / exit recipes (frames at 30 fps)
Positions are offsets from final resting position, in px at 1080x1920.
| Move | Offset | Enter | Exit | Curve |
|---|---|---|---|---|
| Swipe in from right | x +160 (card), +1080 (full-screen) | 12 f | 7 f to x -160 | Snap-out / Snap-in |
| Swipe in from left | x -160 | 12 f | 7 f to x +160 | same |
| Drop-down | y -220 plus opacity 0->1 | 14 f, Soft settle spring | 8 f up y -120 | spring / Snap-in |
| Rise-up (captions) | y +80 | 10 f | 6 f, y -40 fade | Quint-out |
| Headline line | x 120 or y 60, mask reveal optional | 11 f, Snappy | 6 f | Quint-out |
| Logo pop | scale 0.6 -> 1, opacity 0->1 in 6 f | Pop spring ~19 f | scale 1 -> 0.9, fade 6 f | spring |
| Glass card | y +140, scale 0.96 -> 1, blur 24 -> 0 px | 14 f | 8 f, y -80, opacity 0 | Snap-out |
| Stat number count | count 0->N in 18 f, ease-out; scale pulse 1->1.06->1 over 8 f | | | Quint-out |
| Underline / bar wipe | scaleX 0->1 from left | 9 f | 5 f | Snap-out |
| CTA button | scale 0.8->1 Pop, then idle pulse 1->1.04 every 24 f | | | spring + sine |
Stagger: 3 f between siblings (4 f if each is large).
Staggered exit: reverse order or all together, 2 f offset max.

## 5. Whip-blur settings
Whip = fast move with directional motion blur on the moving layer, used for scene-to-scene cuts and big swipes.
- Duration: 8-10 f total (in-out whip curve 0.85,0,0.15,1). Under 6 f reads as a glitch, over 12 f loses snap.
- Travel: full width 1080 px (horizontal) or 1920 px (vertical). Outgoing exits 0 -> -1080, incoming 1080 -> 0, offset so both overlap the same frames.
- Blur: directional (along motion axis only), peak 60-90 px at 1080 wide (about 6-8% of width), 0 px at start and end, peak at mid-move. Formula: blur_px = clamp(|velocity_px_per_frame| * 0.5, 0, 90).
- Shutter-style alternative: 180 degree shutter, 8-12 subframe samples (Remotion `@remotion/motion-blur` Trail: `layers=10, lagInFrames=0.2, trailOpacity=0.6`).
- CSS-ish: `filter: blur(Npx)` is isotropic. For directional blur use an SVG `feGaussianBlur stdDeviation="N 0"` (horizontal) or "0 N" (vertical), N = 30-45 peak (stdDev about half the visual length).
- After Effects / Premiere: Directional Blur, length 80-120 px peak at 1080 wide, keyframe 0 -> peak at mid -> 0, eased. Or Pixel Motion Blur on, shutter angle 180-270.
- Add slight chromatic split at peak: R offset +4 px, B offset -4 px, only mid-frames. Optional, skip if the style is clean-white glass.
- Pair with 1 f of 3-5% white flash at the cut midpoint to hide the swap.

## 6. Scene cuts (15 s example grid)
Typical 5 scenes x 3 s = 90 f each. Per scene: enter 0-14 f, hold ~60 f, exit 76-84 f, overlap next enter by 4-6 f.
Cut types, pick one per video and reuse:
1. Whip-swipe horizontal (section 5), 9 f.
2. Drop-through: outgoing falls y 0 -> +400 with Snap-in over 8 f while the incoming drops from y -220 with Soft settle over 14 f.
3. Glass wipe: a full-height glass panel sweeps left to right in 10 f (Whip curve), content swaps behind it at mid.
4. Mask circle/rect reveal from hero asset: 12 f, Snap-out.

## 7. Background motion (continuous, never stops)
- Gradient hue shift: 8-12 s per loop, Smooth curve, hue range +-25 degrees. Keep light/white base, per P's steer.
- Silk mesh wave: translate x 0 -> 240 px over 450 f linear, plus sine y amplitude 40 px, period 150 f. Must stay behind text for the whole scene, no fade before text exits.
- Parallax: bg 0.2x, mid 0.5x, fg 1x of the swipe distance.
- Slow push-in on hero: scale 1 -> 1.04 over the hold (60 f), linear/Smooth. Subtle, keeps frames alive.

## 8. Timing budget per scene (3 s)
| Phase | Frames |
|---|---|
| Enter (stagger incl.) | 0-14 |
| Settle + read | 14-70 |
| Secondary accent (underline, count, pulse) | 24-40 |
| Exit | 76-84 |
| Overlap with next | 80-90 |
Never leave a scene fully static >20 f: add the slow push-in or bg drift.

## 9. Copy-paste code
### Remotion
```ts
import {spring, interpolate, useCurrentFrame, useVideoConfig, Easing} from 'remotion';
export const SPRING = {
  tight:  {damping: 26, mass: 1, stiffness: 300},
  snappy: {damping: 20, mass: 1, stiffness: 200},
  pop:    {damping: 12, mass: 1, stiffness: 180},
  bouncy: {damping: 8,  mass: 1, stiffness: 150},
  soft:   {damping: 18, mass: 1, stiffness: 120},
  heavy:  {damping: 15, mass: 1, stiffness: 100},
};
export const EASE = {
  out:  Easing.bezier(0.16, 1, 0.3, 1),
  in:   Easing.bezier(0.7, 0, 0.84, 0),
  back: Easing.bezier(0.34, 1.56, 0.64, 1),
  whip: Easing.bezier(0.85, 0, 0.15, 1),
};
// enter + exit for a card: in at `start`, out at `end`
export function useMove(start: number, end: number, dx = 160) {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const inP = spring({frame: f - start, fps, config: SPRING.snappy});
  const outP = interpolate(f, [end, end + 7], [0, 1],
    {easing: EASE.in, extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const x = (1 - inP) * dx - outP * dx;
  const opacity = interpolate(f - start, [0, 7], [0, 1], {extrapolateRight: 'clamp'}) * (1 - outP);
  return {transform: `translateX(${x}px)`, opacity};
}
// whip blur (SVG filter stdDeviation, px) for a move of progress p in [0,1]
export const whipBlur = (p: number, peak = 40) => Math.sin(Math.PI * p) * peak;
// usage: <feGaussianBlur stdDeviation={`${whipBlur(p)} 0`} />
```
### Python / MoviePy / numpy (frame-based)
```python
import numpy as np
def bezier(x1,y1,x2,y2):
    def f(t):
        lo,hi=0.0,1.0
        for _ in range(30):
            m=(lo+hi)/2; x=3*(1-m)**2*m*x1+3*(1-m)*m*m*x2+m**3
            lo,hi=(m,hi) if x<t else (lo,m)
        m=(lo+hi)/2; return 3*(1-m)**2*m*y1+3*(1-m)*m*m*y2+m**3
    return f
OUT=bezier(.16,1,.3,1); IN=bezier(.7,0,.84,0); WHIP=bezier(.85,0,.15,1)
def spring(frames, k=200, c=20, m=1, fps=30, sub=20):
    x=v=0; dt=1/(fps*sub); out=[]
    for i in range(frames*sub):
        a=(k*(1-x)-c*v)/m; v+=a*dt; x+=v*dt
        if i%sub==sub-1: out.append(x)
    return np.array(out)
```
### GSAP
```js
CustomEase.create("snapOut","0.16,1,0.3,1"); CustomEase.create("snapIn","0.7,0,0.84,0");
gsap.from(".card",{x:160,opacity:0,duration:0.4,ease:"snapOut"});   // 12 f
gsap.to(".card",{x:-160,opacity:0,duration:0.23,ease:"snapIn",delay:2.5}); // 7 f
```
### CSS
```css
.enter{animation:in .4s cubic-bezier(.16,1,.3,1) both}
@keyframes in{from{transform:translateX(160px);opacity:0}}
.exit{animation:out .23s cubic-bezier(.7,0,.84,0) both}
@keyframes out{to{transform:translateX(-160px);opacity:0}}
```
Frames to seconds at 30 fps: 6 f = 0.2 s, 8 f = 0.27 s, 10 f = 0.33 s, 12 f = 0.4 s, 14 f = 0.47 s, 18 f = 0.6 s.

## 10. Don'ts
- No linear or ease-in-out on UI enters. No bounce on body text. No fly-in from far off-screen for small elements (P disliked fly/zoom). No blur on text at rest. No whip longer than 12 f. No more than 4 staggered siblings. Don't fade the background wave out before the text leaves. Avoid purple-blue gradients and gradient hero text.

## 11. Source note
Easing curves are standard expo/quint/back families; spring overshoot and settle times were computed by simulating the spring ODE at 30 fps (semi-implicit Euler, 20 substeps). Durations, offsets and blur sizes are tuned recommendations, not measured from InsiderForce videos. Verify against reference frames before locking.
