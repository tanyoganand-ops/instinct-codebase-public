# Open-source liquid glass: five implementations worth trying

Checked: 4 October 2026.

Start with **deepika-builds/liquid-glass** for the smallest understandable SVG enhancement. Use **apple-liquid-glass-webgl** when actual refraction in Safari and Firefox is a requirement, especially over a background you control. **Glasskit** is the most useful comparison harness because it offers CSS, SVG, DOM-clone and WebGL modes behind one API. These are ranked by integration fit and documented constraints, not a measured performance or visual-quality contest.

## Ranked shortlist

| Rank | Implementation | Rendering | Licence checked | Best fit | Main tradeoff |
|---|---|---|---|---|---|
| 1 | [deepika-builds/liquid-glass](https://github.com/deepika-builds/liquid-glass) | CSS + generated SVG displacement map | MIT | Small cards, buttons, navs; minimal vanilla-JS adoption | Real backdrop refraction only in Chromium; Safari/Firefox get frosted blur |
| 2 | [Oliverrr2424/webgl-apple-liquid-glass](https://github.com/Oliverrr2424/webgl-apple-liquid-glass) | WebGL2, DOM adapter or owned canvas | MIT | Cross-browser refraction; video/canvas heroes; custom optical surfaces | Its DOM backdrop is repainted, not sampled directly, so complex CSS needs extra work |
| 3 | [amanblog/glasskit](https://github.com/amanblog/glasskit) | CSS, SVG, SVG-clone, WebGL | MIT | One API for trying several rendering routes, vanilla JS/web components/React | Clone fidelity needs testing; WebGL route uses an explicit image/canvas/video |
| 4 | [naughtyduk/liquidGL](https://github.com/naughtyduk/liquidGL) | WebGPU → WebGL2 → WebGL1 → CSS fallback | MIT for source code; demo assets excluded | Fixed/sticky lenses, interactive panes, stacked glass | Snapshot/reconstruction costs and animation limits; Safari large-panel warning |
| 5 | [rdev/liquid-glass-react](https://github.com/rdev/liquid-glass-react) | React component with displacement effect | MIT | Existing React UI wanting controls for elasticity, frost and aberration | Safari/Firefox do not show displacement |

## 1. deepika-builds/liquid-glass: best minimal SVG starting point

- One JavaScript file, no runtime dependencies. The source inspected was 8,696 bytes unminified; this is not a gzip or npm-package size measurement.
- Uses a canvas-generated displacement-map image inside an SVG filter. Three staggered displacement passes create colour fringing. Applies the filter through `backdrop-filter`, leaving foreground text and inputs as DOM.
- API: `liquidGlass(element, options)`, plus `refresh()` and `destroy()`; resize handling is built in.
- CSS owns the tint, border, highlights and shadow. That makes it easy to fit an existing design rather than inherit a component system.
- Maintainer guidance: map generation scales with surface area; avoid surfaces larger than roughly 800 pixels per side. This is guidance, not a benchmark guarantee.
- Fit: use it when a graceful blur-only fallback is acceptable. Do not depend on refraction to convey meaning.

Source: https://github.com/deepika-builds/liquid-glass

## 2. apple-liquid-glass-webgl: best controlled WebGL route

- Framework-free ES modules, TypeScript declarations, no runtime dependencies according to current documentation.
- Current API includes `new LiquidGlass('.navbar')` for DOM elements and lower-level `LiquidGlassWebGL` for scenes you compose yourself.
- WebGL2 shader handles refraction, dispersion, edge capture and lighting. Falls back to CSS blur when WebGL2 is unavailable.
- Strongest fit: an explicit wallpaper, video or canvas backdrop. This avoids asking a custom page painter to reproduce your whole site's CSS.
- The `backdrop: 'auto'` route repaints backgrounds, borders, images, video, canvas and text. It skips pseudo-elements, shadows, filters, SVG and form controls; rotated/scaled text is not reproduced faithfully. Custom painters can fill gaps.
- Moving background content during a CSS transition or JS animation needs `LiquidGlass.refreshAll()` from the animation update callback for frame-by-frame alignment.
- Group surfaces with `targets` rather than create a WebGL context for every card. CORS rules apply to external images.

Repository: https://github.com/Oliverrr2424/webgl-apple-liquid-glass

Playground: https://oliverrr2424.github.io/webgl-apple-liquid-glass/

Documentation: https://oliverrr2424.github.io/webgl-apple-liquid-glass/docs/

## 3. Glasskit: best multi-backend experiment

- Zero dependencies according to its README; vanilla API, a `<glass-kit>` web component and React bindings.
- `css`: blur/tint only, not lens refraction.
- `svg`: live backdrop refraction in Chromium.
- `svg-clone`: a cloned DOM background passed through a regular SVG filter, intended for Safari/Firefox as well. Treat it as a reconstructed scene, not an arbitrary live-pixel capture.
- `webgl`: refraction over a supplied image, canvas or video.
- `auto`: Chromium chooses SVG; elsewhere a supplied background enables SVG-clone, otherwise CSS fallback.
- Rounded rectangles, pills and circles are supported; arbitrary outline refraction needs a custom displacement map.
- Fit: useful for comparing the right technical lane before committing. Cross-browser and clone claims are maintainer documentation, not independently tested here.

Repository: https://github.com/amanblog/glasskit

Its linked generator could not be verified by the page fetch, so this report deliberately uses the verified repository rather than presenting the generator as working.

## 4. liquidGL: best feature-rich fixed/sticky lens candidate

- Current repository README is **v3.0.0**, with WebGPU, WebGL2, WebGL1 and finally CSS fallback. No runtime dependencies; a built-in rasteriser reconstructs the page background.
- Supports tint, fluid pointer/touch interaction, chromatic aberration, draggable and stacked lenses.
- Videos are detected automatically. Other dynamic content needs registration; the feature table explicitly says real-time CSS animation capture is unsupported.
- Reduce capture area instead of snapshotting a huge document. Higher capture resolution costs memory; long pages can exceed GPU texture limits.
- The README warns that Safari can be unstable with lenses larger than half the viewport width or height. Test on target devices, not only desktop Chromium.
- Documentation contains both newer per-group stacking guidance and older blanket same-z-index wording. Do not assume every stacking configuration works without testing.
- Important licence detail: MIT covers `scripts/` and `package/`. The demo `assets/` directory, including audio and fonts, is explicitly excluded. Reuse the engine, not the whole demo asset bundle.

Repository: https://github.com/naughtyduk/liquidGL

Live demo/docs: https://liquidgl.naughtyduk.com

## 5. liquid-glass-react: best React-specific shortcut

- Wrap arbitrary children in `LiquidGlass`; exposes displacement, blur, saturation, chromatic aberration, elasticity, corner radius and padding controls.
- Suitable if React is already part of the stack and a Chromium-first enhancement is enough.
- Its README explicitly warns that Safari and Firefox show only partial effects, without displacement. Adding React just to obtain this effect would not be my first choice.

Repository: https://github.com/rdev/liquid-glass-react

Live demo: https://liquid-glass.maxrovensky.com

Licence text: https://github.com/rdev/liquid-glass-react/blob/master/LICENSE

## How to choose

1. **Regular product UI, broad browser support, lowest risk:** a translucent CSS surface with `backdrop-filter: blur(...)`, a controlled tint and a fine border. Add SVG refraction as progressive enhancement, using option 1.
2. **Real refraction in Safari/Firefox:** option 2 over a controlled image/video/canvas, or test option 3's DOM-clone route if the background is simple DOM.
3. **Several interactive fixed lenses:** prototype option 4, then check capture cost, stacking and mobile Safari before adopting it widely.
4. **Existing React project:** option 5 is the shortest component route if its browser limitation is acceptable.

CSS blur is not curved-lens refraction. General support for `backdrop-filter` also does not imply support for its SVG `url(...)` filter route. SVG displacement remaps pixels using a displacement map; WebGL needs a texture from a scene the implementation owns, captures or repaints. None of these should be described as a universal browser-native way to read arbitrary page pixels.

Keep readable foreground content outside the optical layer, make the non-glass state work, respect motion preferences and test contrast against the busiest actual background. Pin a version or commit after a successful prototype.

## Other candidates checked

- [ybouane/liquidglass](https://github.com/ybouane/liquidglass): capable WebGL alternative, but its DOM capture uses `html-to-image`, glass must be a direct child of a configured root, and per-frame dynamic capture is expensive. Useful for a deliberately structured scene, less attractive for a tiny drop-in enhancement.
- [dashersw/liquid-glass-js](https://github.com/dashersw/liquid-glass-js): useful shader reference, but page capture requires `html2canvas`; its broad zero-dependency wording therefore needs qualification.

## Verification and source notes

All five repository links were opened and matched the intended project. Their current README files and actual licence files were also read from the live repositories. Oliver's playground/docs, liquidGL's site and the React demo returned matching project content. No dependencies were installed, no forms were submitted and no site was changed.

This was source/API/licence research, not a rendered visual comparison or a device benchmark. Browser claims and performance advice are labelled or attributed to project documentation. MIT generally permits commercial reuse with the required notice; third-party assets and dependencies still need their own licence checks.

Two freshness traps were found: the public fetch of liquidGL's repository returned an older v2.0.1 README, and Oliver's returned an older renderer-only README. The live repository files take precedence in this report; do not build from the stale descriptions.

Technical background:

- https://kube.io/blog/liquid-glass-css-svg - first-principles CSS/SVG refraction explanation and the Chrome-only backdrop demo constraint.
- https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter - platform documentation for backdrop filtering and the need for transparency.

Evidence coverage: official implementations and licences, primary technical explanation and platform documentation. No independent comparative benchmark was used. The rank reflects a practical preference for understandable code, explicit fallbacks and a controlled backdrop, not popularity or an unverified speed claim.
