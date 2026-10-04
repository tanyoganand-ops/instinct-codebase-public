# Hugging Face: Wan 2.2 Fast and LTX Video Fast

## 2026-10-01 - Can Wan make a useful free vertical anime clip?

**Question:** Can a hosted Wan 2.2 route animate a vertical keyframe without a paid account or watermark?

**Findings:** The 17:10 BST test report recorded a successful image-to-video clip from Wan 2.2 Fast: 5.06 seconds, 81 frames at 16 fps, 480x832, H.264, about 1.4 MB. Sampled frames were reported to show no watermark, consistent palette/face, and movement in grass, skirt and clouds. It was soft at 480p. Total call time was about 55 seconds including queue. No account was needed. This particular Space was tested as image-to-video only, despite a broader title.

The same report cited 2 minutes/day anonymous and 5 minutes/day free-account ZeroGPU allowances. Its proposed 4-8 clips/day was an unmeasured estimate, not a tested yield. A 21:03 BST update reported that an earlier saved login was rejected; it did not establish a working HF account.

**Sources:** Historical test reports at 17:10, 17:13 and 21:03 BST, 1 October, in the owner's conversation; referenced public pages:
- https://huggingface.co/spaces/zerogpu-aoti/wan2-2-fp8da-aoti-faster
- https://huggingface.co/docs/hub/main/en/spaces-zerogpu

**Verdict/next:** Proven short I2V output in that test. Preserve the original keyframe for style control. Do not promise 4-8 daily clips until quota is measured. Interpolation/upscaling were editing suggestions, not completed processing.

## 2026-10-02 - Does LTX add text-to-video, and how small is the quota?

**Question:** Can another free Space cover T2V and I2V, and can the combined anonymous quota sustain repeated generation?

**Findings:** At 07:16 BST, LTX Video Fast was reported to work for both text-to-video and image-to-video without signup or watermark. The described T2V sample used a girl in a straw hat in a meadow: 480x832, about 5.1 seconds, anime-style lines/sky, simple motion and mild face drift. The report's separate phrase "15 s per clip" was not explained. It must not be treated as output duration, which was explicitly about 5.1 seconds.

A follow-up quota probe then failed with "exceeded your ZeroGPU quota, 120s requested vs -60s left". Each LTX call requested 120 seconds of GPU. The report counted roughly two clips total across the Wan and LTX tests in that session, attributed to a shared anonymous per-IP/day bucket. Exact reset time was not shown. This is a session observation, not a universal two-clips/day policy.

**Sources:** Historical result and closeout at 07:16 BST, 2 October, in the owner's conversation:
- https://huggingface.co/spaces/Lightricks/ltx-video-distilled
- https://huggingface.co/spaces/zerogpu-aoti/wan2-2-fp8da-aoti-faster
- https://huggingface.co/docs/hub/main/en/spaces-zerogpu

**Verdict/next:** Wan I2V plus LTX T2V/I2V covers both modes at short-clip scale. The measured limit supersedes the optimistic anonymous capacity estimates. A free account might improve quota, but no larger measured yield is recorded. Check account completion and real allowance before planning a daily batch. Commercial-use/model-license terms remain unverified in these tests.
