# Tasteful 3D type in motion: reference notes for Anton on pastel clay

**Research checked: 4 October 2026**

The premium look comes from treating type as designed geometry, not piling on a heavy extrusion effect. Keep the front face readable, let a small bevel catch soft light, and use the side faces and cast shadow to describe depth. A real clay-like reference with a useful production breakdown is the Hellmann's TV campaign; studio cases for Microsoft and Ordinary Folk show how dimensional type can sit within broader brand motion. Public reference pages rarely disclose actual depth or bevel settings, so the numeric starting points below are art-direction proposals, not extracted production settings.

## Reference shortlist

| Reference | What it demonstrates | Depth, light and edge evidence |
|---|---|---|
| [Hellmann's 2025 TV typography, Angela Gigica / Irresistible Studios](https://afoxonabox.com/hellmannstvcommercial) | Closest match to playful, tactile type. The artist describes building a mayo-inspired 3D callout, softening the corners of the brand font before turning it 3D, and iterating against live-action footage. | Inflated/creamy look, with softened edges rather than hard bevels. The artist specifically mentions tests of lighting, speed and material response to keep type legible and integrated. Exact depth/bevel figures are not published. |
| [Microsoft SharePoint Agents Anthem, Spin Creative](https://www.spincreativegroup.com/microsoft-sharepoint-3d-anthem) | Premium SaaS launch film using dimensional type alongside floating UI and depth-driven icons. The studio says these devices bring familiar actions to life; UI-driven compositions maintain clarity at an ad pace. | Confirms depth can support product storytelling rather than act as decoration. The case page does not specify bevel geometry or light rig. Its stills show dimensional type within colourful 3D scenes. |
| [Introducing Spline, Ordinary Folk](https://www.ordinaryfolk.co/project/introducing-spline) | High-end 3D brand film with published styleframes and process images. Useful for seeing type/product world-making within a coherent art direction rather than as a standalone preset. | 3D product film and styleframes verified; the page does not describe type extrusion dimensions or bevel settings. Treat as broad scene/motion reference, not a precise settings guide. |
| [3D text extrusion, Wondermake on Awwwards](https://www.awwwards.com/inspiration/3d-text-extrusion-wondermake) | A direct, Awwwards-curated extrusion reference. Good as a quick visual prompt for the basic face/side-plane relationship. | Awwwards' page names it as 3D text extrusion but exposes little written process detail; exact depth, bevel and light placement are not verifiable from the page text. |
| [3D + Non-Linear Text Animation, Non-Linear Studio on Awwwards](https://www.awwwards.com/inspiration/3d-non-linear-text-animation-non-linear-studio) | Alternative to static extrusion: dimensional type with non-linear motion, represented by desktop/mobile stills and tagged 3D/WebGL/typography. | Strong movement/interaction reference; the Awwwards entry does not report material, bevel or depth values. Avoid copying an effect just because it is technically 3D. |
| [3D Typography, School of Astonishing Pursuits / ED. on Awwwards](https://www.awwwards.com/inspiration/3d-typography-school-of-astonishing-pursuits) | Formal 3D typography/WebGL reference with a published desktop still. Helpful for compositional experiments. | The listing identifies 3D/WebGL/Three.js only; it does not state exact extrusion, bevel or lighting choices. |
| [IWC The Big Pilot Roadshow, Luca Banchelli on Awwwards](https://www.awwwards.com/inspiration/3d-typography-distortion-iwc-the-big-pilow-roadshow-2) | Distorted dimensional type in a luxury-watch roadshow context. Useful as a boundary case for sculptural distortion used as a deliberate brand moment. | Page/title and still verify a dimensional/distorted treatment; technical parameters aren't published. For Anton on pastel clay, borrow only a restrained hint of distortion, if any. |
| [Kinetic typography in true 3D, Maxon](https://www.maxon.net/en/solutions/kinetic-typography) | Reliable explanation of what real 3D buys: extruded letter geometry, custom bevels, editable text, actual lighting/highlights/shadows, and per-character control. | The page directly states bevels and depth are adjustable, and real 3D receives real lighting and drop shadows instead of simulated 2D effects. It gives no numerical recipe. |
| [3D Typography, Spline](https://spline.design/solutions/3d-typography) | Practical design workflow: explore extrusion and bevel, then tune material and lighting; animate letters on a timeline. | Confirms extrusion, bevel, material and lighting are independent controls to compose together, rather than a single preset. No quantitative settings. |
| [Kula SaaS product demo, Picto Design Studio on Behance](https://www.behance.net/gallery/230985579/Product-Demo-Video-for-SaaS-Kinetic-Typography-Motion?locale=en_US) | A useful SaaS clarity counterexample: the creator describes bold kinetic text transitions to communicate product functions, and labels the piece 2D. | Not an extrusion example. Use for message hierarchy and pace: dimensional effects must not compete with the words or product claim. |
| [CHANEL Chance kinetic typography, Ultratype](https://www.ultratype.tv/chanel-kinetic-typography) | Luxury motion example using soft palettes, circular visual motifs, text woven with product imagery, and fluid transformations. | Studio describes movement and integration, not extruded type. Borrow its restraint and visual rhythm, not a claim about bevel or lighting. |

## Direction for extruded Anton headlines on pastel clay

These are testable starting recommendations derived from the references, not disclosed settings from a particular campaign.

1. **Keep the face dominant.** Use Anton for the front face, but don't inflate the extrusion until it competes with the counter-shapes and word silhouette. Start with extrusion depth around **8-15% of cap height**. Check the headline at phone size; reduce depth if side planes close up Anton's counters or merge adjacent letters.
2. **Use a soft, small bevel.** Start around **1-2% of cap height**, scaling down on narrow stems. It should create a readable highlight roll, not a shiny outline. The Hellmann's process is the better clay cue: softened corners plus an inflated material, rather than razor-sharp machined edges.
3. **Light the bevel, not every surface equally.** Try one large soft key from high camera-left, with modest fill from the opposite side. Let the key create a broad highlight along the top/left bevel; keep extrusion side faces a slightly darker tint of the face colour. A gentle contact shadow anchors the word. Avoid hard white streaks, multiple competing speculars, and black ambient-occlusion seams.
4. **Make pastel clay satin-matte.** Give the face and extrusion related pastel hues, with enough value contrast to separate them. Use soft reflections and visible but restrained roughness. High gloss or a strong mirror highlight makes the material read as plastic/candy, not clay. Keep texture subtle so Anton stays crisp.
5. **Animate for one clear read.** Reveal with a short eased rise/slide or slight yaw, then land close to camera-facing and hold. If staggering letters, keep timing tight and intentional. Avoid continuous spins, extreme perspective, elastic bounce on every character, and fast camera orbits; these obscure the message and quickly feel like a stock 3D title preset.
6. **Give the type breathing room.** On a pastel clay set, use one dimensional headline as the hero and keep secondary copy flat or materially quieter. Use the clay shapes to support the word rather than crowd it. The SaaS and Microsoft references reinforce the central rule: depth should clarify the product message, not become an unrelated effect.

### Quick test pass

Render the same Anton word in three variants: (A) shallow extrusion / micro-bevel, (B) slightly deeper extrusion / same bevel, (C) same as A with softened, inflated corners. Keep camera and lighting fixed. Compare thumbnail legibility, side-face visibility and whether the material reads as clay. Pick the shallowest depth that survives the target crop; reserve the inflated corner pass for friendlier copy, not every headline.

## Evidence limits

The Awwwards entries are useful curated visuals, but their written pages do not reveal depth measurements, bevel radii, shader values or light rigs. The case studies often explain intent and production choices, not shot-by-shot numeric settings. All explicit numeric ranges above are practical art-direction tests proposed for this specific Anton/pastel-clay brief, not claims about the cited campaigns.

## Source notes

- [Awwwards: Wondermake extrusion](https://www.awwwards.com/inspiration/3d-text-extrusion-wondermake)
- [Awwwards: Non-Linear Studio](https://www.awwwards.com/inspiration/3d-non-linear-text-animation-non-linear-studio)
- [Awwwards: School of Astonishing Pursuits](https://www.awwwards.com/inspiration/3d-typography-school-of-astonishing-pursuits)
- [Awwwards: IWC / Luca Banchelli](https://www.awwwards.com/inspiration/3d-typography-distortion-iwc-the-big-pilow-roadshow-2)
- [Maxon: Kinetic Typography in True 3D](https://www.maxon.net/en/solutions/kinetic-typography)
- [Angela Gigica: Hellmann's TV commercial](https://afoxonabox.com/hellmannstvcommercial)
- [Spin Creative: SharePoint Agents Anthem](https://www.spincreativegroup.com/microsoft-sharepoint-3d-anthem)
- [Ordinary Folk: Introducing Spline](https://www.ordinaryfolk.co/project/introducing-spline)
- [Spline: 3D Typography](https://spline.design/solutions/3d-typography)
- [Picto Design Studio: Kula SaaS demo](https://www.behance.net/gallery/230985579/Product-Demo-Video-for-SaaS-Kinetic-Typography-Motion?locale=en_US)
- [Ultratype: CHANEL Chance](https://www.ultratype.tv/chanel-kinetic-typography)
