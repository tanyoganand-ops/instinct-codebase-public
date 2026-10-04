# Soft, pastoral web references: colour, curves, depth and motion

Checked: 3 October 2026. This is a research handoff, not a build.

## Best direction

Use **Gentle Guide for the pastel colour fields and soft texture**, **Alma for calm scroll choreography and restrained typography**, and **Wayari as the strongest existing benchmark for layered blur**. Keep **Heyclicky for playful window interactions**. There is no verified single site here that combines every requirement. In particular, a beautiful pastel site is not automatically a frosted-glass site.

"Ghibli" means pastoral colours, soft forms and the feel of the animation. Do not add forests, cottages or characters simply to signal the influence. Borrow layout and interaction patterns; do not reuse another site's artwork, logo, product text or proprietary code without permission.

## Ranked references

| Rank | Live page | What to copy | Evidence and limitation |
|---|---|---|---|
| 1 | [Gentle Guide](https://www.gentle.guide/) | Warm peach/yellow/soft-green overlapping colour fields; a textured backdrop instead of a flat fill; relaxed continuous motion | Official page and current CSS fetched. An independent design article describes its grainy gradient treatment. Best new colour/texture reference, not a glass or complex 3D reference. |
| 2 | [Alma Hospitality](https://almahospitality.it) | Ivory and muted olive palette; oversized thin rounded lettering; sparse navigation; coordinated section/background transitions | Official page, current assets and award breakdown checked. Hero visually inspected. Motion described by Awwwards; GSAP/ScrollTrigger/ScrollSmoother scripts present in current source. Glass not established. |
| 3 | [Wayari](https://wayari.com) | Translucent rounded notification panels, soft focus behind foreground content, overlapping layers, characterful easing | Already a taste benchmark. Official page and specific authored CSS checked. Strongest direct blur evidence. Leave its scenery/art and brand alone. |
| 4 | [Heyclicky](https://www.heyclicky.com/) | Desktop-window hierarchy, media windows, tactile hover details, a modal that dims/blurs the page behind it | Already a taste benchmark. Official page and authored CSS checked. Not uniformly pastoral; use interaction mechanics rather than copying its whole palette. |
| 5 | [Endel](https://endel.io/) | A calm player/product island, slow generative visual mood, rounded device framing | Official page checked. Its page describes generative visuals and exposes player/device imagery. Supplement for ambient mood, not proof of glass or complex scroll choreography. |
| 6 | [Aside](https://aside.com) | Clear browser/product UI hierarchy, breathing room, product demonstration as the central content | Already a taste benchmark. Official page checked. A glass utility exists in its stylesheet, but that alone does not verify a particular visible panel uses it. Treat it as a layout reference. |
| 7 | [Fruitful](https://www.fruitful.com/) | Historical peach/cream + dusty-blue palette, friendly rounded forms and restrained brand interaction | Official page is live, but browser styling failed during this check. The award page and motion designer's case study verify the earlier design, not that today's page exactly matches it. Historical inspiration only until visually rechecked. |

## Exactly what to borrow

### 1. Gentle Guide: colour-field system, not wellness branding

Copy the method: a light warm ground with several large overlapping translucent radial gradients. Keep the colour clouds behind the content, not as small isolated blobs inside cards. Use peach, pale yellow and soft green in the same composition, with enough contrast for readable text.

Current stylesheet evidence includes layered radial gradients with colours such as `rgba(207,216,152,.53)`, `rgba(255,226,120,.72)` and `rgba(254,141,121,.23)`. It also contains a 7-second hue animation and a 45-second continuous marquee. These are authored rules, but not a promise that every rule is active on every device.

The independent Qode review describes grainy gradients, pastel sections, a rotating wheel and a horizontally scrolling strip. That review is from 2022, so its visual descriptions are historical corroboration, not a replacement for the current source check.

**Build instruction:** create a low-contrast textured colour field that moves slowly beneath a stable content layer. Keep the main navigation and reading surfaces calmer than the background. Do not copy the site's healer-marketplace copy or health claims.

### 2. Alma: calm editorial rhythm and coordinated scroll

The inspected hero has a full-width interior photograph, an oversized white thin "alma" wordmark and widely spaced top navigation. The typography and muted materials do more work than decorative UI.

Awwwards records palette colours `#6e7759` and `#fffaf0`, and specifically calls out "Animated Navigation" and "Dynamic Background Transition". Current source loads GSAP, ScrollTrigger and ScrollSmoother. That supports using Alma as a scroll/navigation reference; it does not establish any particular blur radius or timing.

**Build instruction:** use warm ivory as the resting surface, muted olive as a section contrast, a thin rounded display face and a small navigation row. Let the background and foreground change together across sections. For a portfolio, replace hospitality imagery with original project imagery, material closeups or abstract texture. Do not transplant the giant brand wordmark.

### 3. Wayari: separate background softness from foreground glass

Two concrete current-source patterns are useful:

- `.hr-focus` uses `filter: blur(14px)` with a radial mask. This softens part of the background rather than blurring the readable foreground.
- A hero notification treatment uses a translucent warm-light surface, `backdrop-filter: blur(24px) saturate(1.8)`, an 18px corner radius and a thin inset highlight.

The stylesheet also includes movement keyframes and a lighter rendering tier that disables some costly filters/animations. This is worth borrowing: visual richness should have a cheaper path.

**Build instruction:** keep a sharp text/control layer above a softly focused background. Use glass on navigation, small notifications or compact floating controls, rather than making every paragraph a glass card. Give overlapping layers different shadows and highlight strength. The quoted numbers describe inspected source rules, not a universal design recipe.

### 4. Heyclicky: windows that behave like objects

The live page includes `.mov` media items, folder imagery and window controls. Specific authored stylesheet rules provide stronger evidence than generic framework classes:

- a landed modal backdrop uses `backdrop-filter: blur(2px)`;
- the modal backdrop has short fade/opacity transitions;
- the beachball element starts spinning on hover/focus;
- a playing status display animates bar height, with a reduced-motion override;
- the hero has a subtle radial dot grid.

**Build instruction:** show each project as a window with its own frame, media area and concise caption. Make opening and closing feel like the same object changing state. Keep the dot-grid/texture behind windows subtle. Do not add decorative window chrome to every section just because it looks playful.

### 5. Endel: ambient movement, limited use

The official page includes a demo-player cover, a device frame and background artwork. It explicitly describes generative visuals alongside soundscapes. This is enough to consider it for mood and product framing, not to claim that the homepage has any specific CSS blur effect.

**Build instruction:** use one quiet, continuously moving visual behind a compact product/project island. Avoid rapid cuts and multiple competing motion loops. Use the principle of slow ambient movement, not its audio/product claims.

### 6. Aside: structure before decoration

The live page leads with a browser/product demonstration, then feature explanations. Its styles define `.bg-glass` using a partly transparent popover colour and an 8px blur variable. However, the fetched HTML did not establish that the class appears on a specific visible component. Do not cite this as proof that a named navbar or hero card is frosted.

**Build instruction:** borrow the clear separation between the product demo, supporting explanation and call to action. Then apply the desired pastel palette and a verified glass treatment independently.

### 7. Fruitful: useful older design, current visual check unresolved

The Awwwards record gives `#FEE9D1` and `#9DD1E9` and lists gallery interaction, animation and transitions. The motion designer's project page says the brief was simple motion with personality, including a logo animation and site interactions.

The live official homepage returned actual financial-product content. Its browser rendering was unstyled during this session, so do not treat a screenshot or older award video as proof of the current homepage design.

**Build instruction:** take the older cream/peach + pale-blue pairing and simple, friendly motion as a palette/brand reference. Recheck the current visual experience before matching its layout or scroll behaviour.

## Proposed synthesis for a build

This is a design proposal, not a description of any single source site:

1. Start with Alma's warm ivory and olive as the base. Use Gentle Guide's peach/yellow colour fields for softness, and Fruitful's older blue sparingly as an accent.
2. Put texture and slow colour movement behind a legible, mostly sharp foreground. Texture should still be visible through translucent surfaces.
3. Use Wayari-like glass only for a compact floating navigation bar and one or two object-like controls. Use opaque or nearly opaque reading panels when needed.
4. Use Heyclicky-style project windows for selected portfolio pieces. One continuous motion scene is better than a stack of static cards that merely fade in.
5. Coordinate background changes and content movement using Alma's scroll principle. Do not animate every element independently.
6. Include reduced motion, a low-performance fallback and a mobile layout. Do not blur essential text or hijack scrolling.

## Verification and source notes

All listed official pages returned identifiable site content on 3 October 2026, not merely an HTTP success. This confirms reachability at check time, not future uptime. Only Alma's hero had a successful visual inspection in this run. Other visual/motion recommendations are grounded in the fetched page, current authored source or explicitly labelled historical design evidence. Current hover/click/scroll behaviour was not exhaustively tested. Gaussian-style appearance is not proof of a specific rendering kernel; use the exact CSS filter terms above.

Official pages:

- https://www.gentle.guide/
- https://almahospitality.it
- https://wayari.com
- https://www.heyclicky.com/
- https://endel.io/
- https://aside.com
- https://www.fruitful.com/

Independent/editorial and creator evidence:

- https://qodeinteractive.com/magazine/beautiful-pastel-websites/ - older descriptions of Gentle Guide's texture, colour and limited movement.
- https://www.awwwards.com/sites/alma-hospitality - palette and navigation/background-transition breakdown.
- https://wearecroma.it/en/progetti/web-design/alma-hospitality - Alma creator case study, discovered in search; not used as sole proof of current visuals.
- https://www.awwwards.com/sites/fruitful - older palette and interaction record.
- https://www.yaelbienenstock.com/projects/fruitful - creator's motion brief and credits.

Current-source evidence was read from stylesheet links supplied by each official page. A stylesheet's presence alone is weaker than an active rendered effect. Rules cited above are specific authored selectors where possible; framework utilities are explicitly qualified.

## Next step

Choose **Gentle Guide + Alma + Wayari** as the initial three-reference brief. Ask the builder to reproduce the colour-field softness, coordinated scroll rhythm and glass depth separately, then combine them. Do not rebuild a whole site merely to add the effect; apply the brief to the existing base first.

### Exact current stylesheet URLs inspected

These are deployment-specific and may change:

- Wayari: https://wayari.com/_next/static/css/2784857407b421ae.css?dpl=dpl_D7cW33Q1AA4gwwKHueWWbvExoeYk
- Wayari: https://wayari.com/_next/static/css/0f43a965bd09da16.css?dpl=dpl_D7cW33Q1AA4gwwKHueWWbvExoeYk
- Wayari: https://wayari.com/_next/static/css/863cd56e72de59a0.css?dpl=dpl_D7cW33Q1AA4gwwKHueWWbvExoeYk
- Wayari: https://wayari.com/_next/static/css/1ff357a0bd2b0f70.css?dpl=dpl_D7cW33Q1AA4gwwKHueWWbvExoeYk
- Heyclicky: https://www.heyclicky.com/_next/static/chunks/1_239pj1gwz-z.css?dpl=dpl_GT2GY8APaWbwLvtZFVvsjdzwyLwV
- Heyclicky: https://www.heyclicky.com/_next/static/chunks/0zecslmzyw1ed.css?dpl=dpl_GT2GY8APaWbwLvtZFVvsjdzwyLwV
- Aside: https://aside.com/_next/static/immutable/chunks/388ox4gsse6dx.css
- Aside: https://aside.com/_next/static/immutable/chunks/00yh_uwpq6vod.css
- Gentle Guide: https://www.gentle.guide/_next/static/css/60c2be2754cf3e2e898f.css
- Alma: https://almahospitality.it/css/style.css
