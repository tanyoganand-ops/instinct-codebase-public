# Clay ad: reconstruction tokens

Source: `02-clay-saas-apple-ui-35e35be5.mp4`, supplied reference. 1080 × 1920, 30 fps, 746 frames, 24.867 seconds. No audio stream. This is an extraction from the rendered video, not Clay's official design system.

## How to use this spec

The actual animation is a **1080 × 1080 square at video y=420–1499**. The black bands and white "SaaS AD explainer for Clay" title belong to the surrounding presentation, not the product UI. Recreate the square first. Add the surrounding 9:16 frame only if needed.

All implementation tokens below use a **360 × 360 logical stage**, scaled 3× to the source square. Multiply logical px by 3 for source-video px; multiply by `stageWidth / 360` for another output. Use a fixed-size stage and scale the entire stage, including type, shadows and strokes. Do not let the screenshot-like components reflow during the animation.

Confidence key:
- **Measured:** video metadata, sampled colour, settled silhouette or frame timing.
- **Estimated:** geometry/type rounded from pixels; compression and animated scaling affect it.
- **Recipe:** a proposed implementation that matches the look, not recovered source CSS.

The video contains three different visual treatments: rounded error/status cards, a flat integration grid, and a compact screenshot-like composer. Do not force one radius or shadow onto all three.

## 1. Palette

Colours were sampled from decoded frames, avoiding text and antialiased edges where possible. RGB values can vary by a few channels because this is compressed H.264/BT.709, not an original design file.

| Token | Apply | Value | Evidence / confidence |
| --- | --- | --- | --- |
| `canvas` | Square animation background | `#F3F3F3` | Dominant exact decoded RGB 243/243/243 across scenes; measured |
| `surface` | Cards, integration tile, composer | `#FFFFFF` | Settled flat interior pixels; measured |
| `ink` | Hero phrases, card labels | `#080808` | Render includes pure black; use near-black as matching recipe |
| `muted` | Card metadata, body copy | `#777777` | Approximate neutral mid-grey; estimated |
| `placeholder` | Composer empty-state text | `#B9B9B9` | Approximate; estimated |
| `line` | Grid and light component outlines | `#E1E1E1` | Approximate decoded light-grey lines; estimated |
| `divider-strong` | Status-card horizontal rule | `#B0B0B0` | Approximate; estimated |
| `button-soft-blue` | Error-card action fill | `#D8E7ED` | Interior mode 216/231/237 at 2.30s; measured |
| `button-lilac` | "update now" pill | `#D6AEFA` | Interior mode 214/174/250 at 3.50s; measured |
| `button-lilac-ink` | "update now" label | `#8000C8` | Approximate saturated violet; estimated |
| `badge-amber` | "Detected" badge | `#F9ECD8` | Region median 249/236/216; measured approximation |
| `badge-amber-ink` | "Detected" label | `#9A6B33` | Approximate warm brown; estimated |
| `status-cross` | Outdated-data error crosses | `#884358` | Approximate muted wine; estimated |
| `action-blue` | "Generate campaign" button | `#2996FD` | Hue-filtered median 41/150/253 at 15.50s; measured approximation |
| `link-blue` | Composer "settings" link | `#478CC0` | Approximate; estimated |
| `workflow-navy` | Central workflow node | `#001030` | Most frequent quantised navy at 12s; measured approximation |
| `workflow-lime` | Small result/status highlight | `#ECF870` | Most frequent quantised colour at 12s; measured approximation |
| `sweep-cyan` | Moving processing highlight | `#65D7F5` | Approximate; render as translucent gradient, not solid fill |

Clay's arch mark is a shaded multicolour asset, not a flat UI swatch. Representative colours are cyan `#38D0FA`, coral `#FF585D`, yellow `#FFCC00`, with darker cyan edges. Use a supplied/approved logo asset where available. Do not replace the mark with three flat CSS arcs if fidelity matters. Third-party logos keep their own colours.

## 2. Shape, border and shadow

| Component | Logical size at a settled example | Radius | Border | Evidence |
| --- | --- | --- | --- | --- |
| Error card | ~195 × 73 | ~18 | Optional 0.5px `#E7E7E7` | 2.30s: white silhouette ~585 × 219 source px |
| Error-card action | ~158–160 × 23–24 | ~7 | None | 2.30s: fill bounds ~474 × 70 source px |
| Outdated-data card | ~169 × 205 | ~23–25 | 0.5px `#E7E7E7` | 3.50s: white silhouette ~508 × 614 source px |
| Outdated-data action | ~139 × 20–21 | Full pill | None | 3.50s; estimated |
| "Detected" badge | ~48 × 12–13 | ~5–6 | None | 3.50s; estimated |
| Integration tile | ~203 × 181 | 0 | Grid lines ~0.75px | 8.40s: white area ~608 × 542 source px |
| Integration tag | Content width, ~15 high | 1–2 | 0.5px `line` | 8–9s; estimated |
| Workflow source item | ~102 × 23 | ~3–4 | 0.5px `line` | 12s: ~307 × 70 source px |
| Workflow centre node | ~50 × 23 | ~2 | None | 12s: ~149 × 69 source px |
| Workflow result item | ~123 × 32 | ~4 | 0.5px `line` | 12s: ~368 × 97 source px |
| Composer | ~319 × 72 at 15.50s | ~5–6 | 0.5px `line` | White silhouette ~957 × 217 source px; scene scales/pans |
| Composer action | ~64 × 14 | ~2–3 | None | Estimated from settled scene |
| Composer suggestion chip | Content width, ~13–14 high | ~2 | 0.5px `line` | 15–16s; estimated |

### Matching shadow recipes

These are **recipes**, not uniquely recoverable CSS. The error/status cards have a restrained outer/contact shadow. They do not have heavy neumorphic inset shadows or a visibly raised clay texture.

```css
:root {
  /* All dimensions refer to the 360px logical stage. */
  --shadow-card: 0 1px 3px rgb(0 0 0 / 0.07),
                 0 0 1px rgb(0 0 0 / 0.05);
  --shadow-composer: 0 1px 3px rgb(0 0 0 / 0.075),
                     0 0 1px rgb(0 0 0 / 0.04);
  --shadow-flat: none;
}
```

Evidence: below the first error card at 2.30s, the canvas returns from ~231 to 243 over roughly 12 source px (~4 logical px). The shadow is narrow and neutral, with little visible offset. Use no shadow on the integration grid; its pale rules provide separation. Workflow boxes and suggestion chips are mostly border-led.

## 3. Typography

The exact font cannot be identified from a flattened video. The glyphs look like a compact modern grotesk. Start with `Inter`, then `-apple-system`, `BlinkMacSystemFont`, `"Helvetica Neue"`, `Arial`, `sans-serif`. SF Pro is a plausible substitute, not a verified source font. Do not claim this clip establishes the font used by Clay's current website.

| Role | Logical font size | Weight | Line height | Tracking | Notes |
| --- | --- | --- | --- | --- | --- |
| Main kinetic phrase | ~17–18px | 600 | 1.1 | -0.03em | "We've all been there", "Meet Clay", "All in one place"; text changes scale during transitions |
| End-card `clay.com` | ~17–18px | 600 | 1.1 | -0.03em | Settled after its very large first-frame pop |
| Error-card title | ~10–11px | 600–650 | 1.15 | -0.025em | Not the large hero scale |
| Error-card metadata | ~7px | 400 | 1.2 | -0.02em | Grey, deliberately compact |
| Error-card action | ~11–12px | 600 | 1.05 | -0.035em | Slightly larger than title |
| Status-card title | ~9px | 650 | 1.2 | -0.02em | "Outdated data" |
| Status-card rows | ~8px | 600 | 1.5–1.8 | -0.02em | Four rows with wine-coloured crosses |
| Status metadata / badge | ~7px / 6px | 400 / 500 | 1.2 | -0.01em | |
| Integration title | ~10–11px | 600 | 1.2 | -0.02em | Brand name |
| Integration description | ~7–8px | 400 | 1.45 | -0.015em | Short multiline paragraphs |
| Integration tag | ~7px | 400 | 1.2 | -0.01em | |
| Composer heading | ~9px | 600 | 1.2 | -0.025em | At settled composer scale |
| Composer helper | ~6px | 400 | 1.3 | -0.01em | |
| Composer placeholder | ~8px | 400 | 1.2 | -0.02em | |
| Composer button / chips | ~6.5–7px | 500 / 600 | 1.2 | -0.015em | |
| Workflow microcopy | ~4–5px | 400–600 | 1.2 | 0 | Visual diagram labels, not an accessible live UI |

These small sizes describe an **animation composition**, not recommended readable app typography. For a real responsive product page, retain the visual hierarchy but raise body/metadata to accessible sizes and use responsive layouts. For a video clone, preserve the listed proportions.

## 4. Layout and spacing rhythm

Use an estimated **2px logical base unit**, with steps `2, 4, 6, 8, 12, 16, 24, 32`. Geometry is not perfectly aligned to one grid because source screenshots and scale transforms are mixed.

- Square-stage hero anchor: approximately `(180, 180)`. Short phrases sit near the centre. Longer phrases can span the stage during entry before settling.
- Error stack at 2.30s: left ~81px, first top ~60px, card width ~195px; second top ~147px; third top ~231px. Settled gaps are ~12–14px. Early entry frames show larger offsets and lower opacity.
- Error-card internal horizontal padding: ~18px. Icon: ~17px square. Icon-to-copy gap: ~7px. First text block begins ~43px inside the card. Action has ~18px side insets and ~7px bottom inset.
- Outdated-data card at 3.50s: approximately left 94px, top 79px. Horizontal internal padding ~16px. Divider width ~140px. Rows separated by ~16px. Action sits below a generous ~20px gap.
- Integration grid: pale full-stage horizontal and vertical lines extend past the featured white tile. At 8.40s tile left ~79px, top ~90px, width ~203px, height ~181px. Inner padding ~16px. Logo and utility icons share the top row; title, paragraph and tags follow with ~10–12px gaps.
- Workflow: three left source rows, one navy middle node, one right result. Thin curved connectors join the source rows into the middle node. At 12s source left ~18px and width ~102px; middle left ~150px; result left ~227px. Source-row gaps ~7–8px. The diagram drifts horizontally through the scene.
- Composer: heading and helper centred above the input. ~12–16px gap between helper and input. Input interior padding ~10px. Blue action anchored bottom-right. Chips in two centred rows, ~4px horizontal/vertical gaps. The scene pans and changes scale, so do not measure clipped first/last frames as the intended width.
- Mark-to-word gap in the end card: ~10–12px. Clay arch mark ~35–40px wide early in the settled end-card hold, reducing with the lockup.

## 5. Frame-indexed motion map

Time zero is the video start. Frames are zero-based (`frame = round(seconds × 30)`). Times below are approximate visual boundaries, generally within ±2–3 frames unless a range is given. Each frame is 33.33ms. The whole 746-frame sequence was decoded and examined for per-frame change; visual inspection used overview frames, 5fps storyboards, full-size settled frames and denser transition samples. This does not recover the original easing curves or animation code.

| Time / approximate frames | Content | Motion treatment |
| --- | --- | --- |
| 0.00–0.57 / 0–17 | "We've all been there" | Staggered word reveal, upward/diagonal settling, blue-tinted blur/ghost during entry; settles to black |
| 0.57–1.63 / 17–49 | Same phrase | Hold with little motion |
| 1.67–2.17 / 50–65 | Three error cards | Staggered fade/slide into stacked positions; approximately 100–133ms between cards, ~250–350ms individual settling |
| 2.17–2.43 / 65–73 | Error stack | Brief readable hold |
| 2.43–3.13 / 73–94 | Stack becomes status card | Cards move apart/out, then a rounded container changes proportion and its contents resolve. Use a designed crossfade/morph, not a hard cut |
| 3.13–4.03 / 94–121 | "Outdated data" | Readable hold with slight scale drift |
| 4.07–4.27 / 122–128 | "Hours" + clock | Fast scene replacement/reveal |
| 4.73–5.17 / 142–155 | "of manual research" added | Staggered phrase completion; clock remains inline |
| 5.17–5.77 / 155–173 | Full research phrase | Hold |
| 5.77–6.33 / 173–190 | Research phrase exits; "Meet Clay" enters | Vertical travel, fading/blurred incoming text; overlap around 6.2s |
| 6.33–6.70 / 190–201 | "Meet Clay" + logo | Word/logo reveal and settle |
| 6.70–7.40 / 201–222 | Same | Hold, then pronounced scale-up just before scene change |
| 7.43–9.77 / 223–293 | Integration showcase | Flat grid tiles change rapidly, approximately 250–333ms per integration; mild pan/zoom in tile framing |
| 9.80–10.03 / 294–301 | "All in one place" | Quick phrase reveal |
| 10.03–11.20 / 301–336 | Same | Hold |
| 11.23–11.80 / 337–354 | Workflow diagram | Boxes/nodes appear; bright cyan processing sweep travels across the source rows and result |
| 11.80–13.53 / 354–406 | Workflow diagram | Readable hold with slow horizontal drift |
| 13.53–14.17 / 406–425 | "Automatically!" | Workflow leaves towards upper-left; centred phrase enters and settles |
| 14.17–14.83 / 425–445 | Same | Short hold |
| 14.90–15.23 / 447–457 | AI composer | Fast reframing/scale movement into composer; initial frames are deliberately clipped |
| 15.23–16.27 / 457–488 | Empty composer | Hold with slight camera movement |
| 16.30–17.63 / 489–529 | Composer with prompt | Pan/reframe followed by typed text: "Book demo meetings with cold prospects in the SaaS space"; average ~20–35ms per character, not perfectly uniform |
| 17.63–17.93 / 529–538 | Filled composer | Very brief hold |
| 17.97–18.60 / 539–558 | "Your pipeline" | Composer moves down/out while phrase drops in from above and settles |
| 18.60–19.47 / 558–584 | Same | Hold |
| 19.50–19.80 / 585–594 | "Always clean" | Word-level replacement/reveal |
| 19.80–20.87 / 594–626 | Same | Hold |
| 20.90–21.17 / 627–635 | "Always ready" | Fast word replacement |
| 21.17–22.03 / 635–661 | Same | Hold |
| 22.07–22.33 / 662–670 | Clay mark + `clay.com` | Very large scale on first reveal, immediately contracts toward centred end lockup; not a subtle hover pop |
| 22.33–24.33 / 670–730 | End lockup | Hold with a slow reduction in scale, roughly 25–30% across the hold |
| ~24.37–24.83 / 731–745 | End lockup fade | Opacity fade to canvas; surrounding title/bands remain |

The fast integration run visibly includes Notion, Airtable, Apollo.io, PitchBook, Semrush, Google Maps, LeadIQ, Clearbit and Owler. Preserve it as a montage rather than turning it into nine slow feature slides.

### Reusable motion tokens

Recommended matching values, not measured original curves:

```css
:root {
  --duration-word: 220ms;
  --duration-card-enter: 320ms;
  --duration-scene: 400ms;
  --duration-morph: 650ms;
  --duration-sweep: 550ms;
  --duration-end-pop: 250ms;
  --duration-end-fade: 450ms;
  --stagger-word: 67ms;       /* 2 frames */
  --stagger-card: 100ms;      /* 3 frames */
  --ease-out: cubic-bezier(.16, 1, .3, 1);
  --ease-in-out: cubic-bezier(.65, 0, .35, 1);
}
```

- Text entry recipe: opacity `0 → 1`, translateY `8px → 0`, blur `4px → 0`, 220ms ease-out; stagger individual words by 67ms. Use cyan/blue ghost colour only during the opening phrase, then switch to ink.
- Card entry recipe: opacity `0 → 1`, translateY `12–24px → 0`, 320ms ease-out; stagger 100ms. Keep each card's contents together.
- Scene travel: larger movements of ~80–180px over 400–650ms. Recreate with group transforms and crop to stage bounds. Small generic crossfades alone will not match the reference.
- Integration montage: ~267ms per tile as a starting value; retain the continuous grid while replacing tile content. No elaborate individual content entrance is needed.
- Workflow sweep: clipped linear gradient `transparent → rgb(101 215 245 / .75) → transparent`, animate left-to-right over ~550ms across the three source boxes, then the result box. No permanent cyan fill remains.
- Typing: start after reframing around 16.4s; reveal characters over ~1.2s. Use the original visible prompt rather than lorem ipsum.
- End lockup: begin ~4× settled scale, contract over ~200–267ms. Initial oversized lockup is visibly cropped. Then reduce by roughly 25–30% over the hold and fade over ~450ms. This scale factor is a recipe inferred from the dense frames, not a recovered parameter.
- If recreating for an interactive page, use `prefers-reduced-motion` to replace travel, blur and sweeps with short fades. It is not a feature evidenced by the clip.

## 6. Copy-paste base tokens

```css
:root {
  --clay-canvas: #f3f3f3;
  --clay-surface: #fff;
  --clay-ink: #080808;
  --clay-muted: #777;
  --clay-placeholder: #b9b9b9;
  --clay-line: #e1e1e1;
  --clay-soft-blue: #d8e7ed;
  --clay-lilac: #d6aefa;
  --clay-lilac-ink: #8000c8;
  --clay-amber: #f9ecd8;
  --clay-amber-ink: #9a6b33;
  --clay-cross: #884358;
  --clay-action-blue: #2996fd;
  --clay-navy: #001030;
  --clay-lime: #ecf870;
  --clay-font: Inter, -apple-system, BlinkMacSystemFont,
               "Helvetica Neue", Arial, sans-serif;
  --clay-space-1: 2px;
  --clay-space-2: 4px;
  --clay-space-3: 6px;
  --clay-space-4: 8px;
  --clay-space-6: 12px;
  --clay-space-8: 16px;
  --clay-space-12: 24px;
  --clay-space-16: 32px;
  --clay-radius-chip: 2px;
  --clay-radius-input: 6px;
  --clay-radius-button: 7px;
  --clay-radius-card: 18px;
  --clay-radius-status: 24px;
  --clay-shadow: 0 1px 3px rgb(0 0 0 / .07),
                 0 0 1px rgb(0 0 0 / .05);
}

.clay-stage {
  position: relative;
  width: 360px;
  height: 360px;
  overflow: hidden;
  background: var(--clay-canvas);
  font-family: var(--clay-font);
  color: var(--clay-ink);
  -webkit-font-smoothing: antialiased;
}
.clay-hero {
  position: absolute;
  left: 50%; top: 50%;
  /* Animate a nested element so this centring transform stays intact. */
  transform: translate(-50%, -50%);
  font-size: 18px; font-weight: 600;
  line-height: 1.1; letter-spacing: -.03em;
  white-space: nowrap;
}
.clay-error-card {
  width: 195px; height: 73px;
  box-sizing: border-box;
  border: .5px solid #e7e7e7;
  border-radius: var(--clay-radius-card);
  background: var(--clay-surface);
  box-shadow: var(--clay-shadow);
}
.clay-error-action {
  height: 24px;
  border: 0; border-radius: var(--clay-radius-button);
  background: var(--clay-soft-blue);
  color: var(--clay-ink);
  font: 600 11px/1.05 var(--clay-font);
  letter-spacing: -.035em;
}
.clay-grid-tile {
  background: var(--clay-surface);
  border: .75px solid var(--clay-line);
  border-radius: 0;
  box-shadow: none;
}
```

## 7. Fidelity checks for the builder

1. Compare at the same stage size and timestamp. A 360px logical stage must be scaled uniformly to a 1080px square before comparing source screenshots.
2. Canvas is neutral `#F3F3F3`, not warm cream, pure white or a gradient.
3. Hero phrases are small and surrounded by large empty areas. Do not turn the reference into oversized landing-page headings.
4. Rounded cards have white interiors, tight neutral outer shadows and no heavy inset shading.
5. The integration grid is sharp-cornered and almost flat. The AI composer uses much smaller radii than the error cards.
6. Keep the rapid beat changes and deliberate cropping during reframes. They are part of the animation, not rendering bugs.
7. Typography, easing, exact radii and shadows remain reconstruction estimates. Font files, original CSS, source animation keyframes, hidden states and responsive rules cannot be established from this video.

Companion evidence image: `clay-token-evidence.png`, with six labelled settled/near-settled scenes at 2.30s, 3.50s, 8.40s, 12.00s, 15.50s and 22.50s. Use the video itself to judge the transitions.
