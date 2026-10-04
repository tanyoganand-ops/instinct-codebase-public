# Video generation - pipeline proof and route audit (2 Oct 2026, evening)

## Pipeline proof (18:03-18:10)
- HF account tanyoganand (tanyoganand@gmail.com), email verified, password in vault entry "Hugging Face password".
- ZeroGPU free quota: 5 GPU-minutes/day, resets 24h after first GPU use (docs: https://huggingface.co/docs/hub/spaces-zerogpu).
- LTX Video Fast (https://huggingface.co/spaces/Lightricks/ltx-video-distilled): one t2v test, ~25s click-to-clip, 704x512 30fps 1.9s. Billing meter stayed 0/5 - small clips cost seconds, exact draw unmeasurable.
- Repeat steps: open Space signed in, text-to-video tab, prompt, duration (0.3-8.5s), generate, download. Gradio iframe refs change per click.

## Route audit (18:22 closeout)
- HF Wan 2.2 (https://huggingface.co/spaces/zerogpu-aoti/wan2-2-fp8da-aoti-faster): one 1s i2v test OK, 832x624 16fps. Shares the SAME 5-min pool as LTX - not extra quota. Draw unknown (meter unchanged).
- PixVerse (jack19tan): 30 credits/day, resets 00:00 UTC, expires daily. Works, 576x1024 24fps WITH watermark. Earlier "charged but never finished" job actually finished - naan clip recovered (https://app.pixverse.ai/video/427579666763014). Today's 30 spent.
- Dreamina (jack19tan account, verified by numeric ID match to 30 Sep signup): ledger confirms +120 daily free credits (Oct 1 + Oct 2 entries), balance 232 bonus. Editor loads again (1 Oct blank-page failure cleared). First 60-credit test FAILED service-side ("Couldn't generate 1 item", 0 credits spent). User says cheaper settings exist (~4 credits/sec); cost-ladder check at cheapest setting in progress.
- SeaArt: 130 stamina/day advertised on login panel. Email login blocked (password field rejects secure fill twice). Not usable this session; password reset via agent mailbox is the fix if pursued. Existing account registration unconfirmed.

## Constraints carried
- P: human-paced usage, no ban risk, one generic warm-up clip per account (30 Sep), ask before any new signup, agent-owned accounts only (no P data), no multi-accounting, no VPN.
