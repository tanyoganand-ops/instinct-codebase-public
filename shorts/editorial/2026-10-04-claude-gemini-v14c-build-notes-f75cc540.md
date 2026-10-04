# V14c animation polish

15s, 1080x1920, 30fps, 450 H.264 yuv420p frames with the same AAC cue-bed/whoosh mix.

## Motion fixes
- Removed a real discontinuity: v14b switched from chip-swap transforms into trade transforms and back at hard boundaries. V14c computes entrance, perspective trade and exit as one continuous trajectory. Keeps B8's 28-degree yaw/1.1-0.9 scale and separated arcs. Trade length padded to .85s.
- Whip padded from 9 to 18frames at the same benchmark handoff; horizontal blur cap lowered from48 to22px, gain .42 to .25.
- Benchmark and verdict lateral entrances use shorter travel over longer time, retaining opposed slide directions. Badge entrance retimed earlier for more reading space.
- Under-story props fade while crossing the essential reading area, then return smoothly at the margins. Asset pixels, lane paths, icons and B4d inner animations unchanged. This clears background shapes from hook logos, scores and verdict words instead of changing assets.
- Plain-background zoom hook, locked content, background asset set, sound mix and CTA unchanged.

## QA
450 states saved before final render. Zero cross-asset essential text overlap frames. Essential stage clipped to x48-888/y288-1248. Runtime/layout/contrast pass without errors/warnings. Encoded full decode confirms450frames/15s, no identical adjacent pairs. Inspected encoded hook, benchmark hold, padded whip and trade before/mid/after positions. Trade stays separated without a boundary jump; core copy is clear of lane props. Decorative lane logos remain outside the essential safe audit. Audio signal/timing verified in v13b; no subjective listening pass available.

Earlier versions retained. First capture was interrupted by the command time cap; final independent render completed and was verified. Local-only Hyperframes0.8.115 with telemetry disabled. No paid service/publication.

Facts unchanged from October4 source verification: https://artificialanalysis.ai/articles/gemini-4-argon-google-top-three-labs and https://artificialanalysis.ai/models/gemini-4-argon . Intermediate score integers are animation states.
