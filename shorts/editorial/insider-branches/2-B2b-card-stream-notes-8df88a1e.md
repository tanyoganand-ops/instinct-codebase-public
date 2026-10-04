# B2 - Card stream

15 seconds, 1080x1920, 30 fps. Silent review cut.

## Branch treatment

Twenty separate story cards, grouped into five four-card packets: headline, Claude lockup/score, Gemini lockup/score, and proof/CTA. Each packet travels into and out of the screen with scale-based depth, staggered lanes and an accelerating departure. No card changes its text or logo geometry in place. The camera and pale paper background stay fixed.

Packets: hook 0-2.8s; Terminal-Bench 2.8-6.3s; AutomationBench 6.3-9.8s; verdict 9.8-12.5s; CTA 12.5-15s. Entry starts 0.6s before each packet, with 75ms sibling staggers; departures overlap incoming cards. The reading phase continues a gentle forward travel rather than coming to a full stop. Text disappears before the card crosses the reading zone; the card continues offscreen.

Pastel matte surfaces, extruded-edge shadows, received raster brand lockups and Anton type. This is scale-based 2.5D depth, not real 3D geometry. Four useful cards move together throughout; supporting source rail stays fixed for readability.

## Checks

- 450 encoded frames; 15.000 seconds; H.264; 1080x1920; 30 fps; no audio stream.
- Saved all 450 composition states and checked every visible text range against x48-888 / y288-1248: zero violations.
- At least four visible cards change their geometric bounds in every adjacent frame pair. No pair has fewer than three moving cards.
- All 450 decoded low-resolution frame hashes differ from their preceding frame.
- Runtime/layout gate passes; 39/39 sampled contrast checks pass. One informational panel-out-of-canvas finding is intentional departure of the empty verdict carrier.
- Inspected encoded 9-frame contact sheet and seven transition/reading-phase snapshots: lockups intact; score pairs 64/57 and 71/78 correct; verdict and CTA readable; no text occlusion after final adjustment.

## Reference limits

Uses the assigned InsiderForce-style hook -> evidence -> verdict -> comment-keyword structure. Actual source-channel frame timing was not measured in this branch. It should be judged as a card-stream experiment, not an exact replica.

Content and benchmark numbers are preserved from the locked production brief. This branch did not independently re-check the benchmark source. The source rail records the supplied 30 Sep 2026 snapshot, not a fresh benchmark claim. Logo provenance caveats remain in brand-provenance.md.

## B2b measured-resource timing update

Revision made after the parent supplied frame-stepped InsiderForce research. Entry shortened from 550ms to 420ms (about 13 frames), within the measured motion-burst range, with a small decaying 2.8% sine settle added to scale. Alternating lanes, growing cards and down-right shadows remain. P's current multi-card travel requirement takes priority over the reference's single-hero hard cuts and still holds. This does not reproduce the measured 3-4-frame linear lateral travel exactly; the card-stream branch retains a decelerating zoom-entry vocabulary. The reference informed timing, not user authority or new content.

B2b encoded sheet inspected directly. All 450 states re-audited: zero visible-text safe violations, minimum four geometrically moving cards per adjacent pair. Encoded metadata and frame hashes rechecked. B2 initial is retained; B2b is the current timing revision.
