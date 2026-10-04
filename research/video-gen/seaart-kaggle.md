# SeaArt access and Kaggle compute

## 2026-10-02 - Is SeaArt worth pursuing as a free video route?

**Question:** Can email signup finish, and is daily stamina usable for worthwhile free clips?

**Findings:** The 05:48 BST test report said signup did not finish and no video was generated. In the combined email/password form, the email field accepted input but the password remained visibly empty; submission returned "Please enter your password". Repeated fresh-field attempts did not fix it. No CAPTCHA or signup email was seen.

A live Daily Rewards popup was reported, with a screenshot confirming "Regular users receive 130 Stamina/day after logging in, usable for all scenarios", resetting daily. Make Videos and several video models were visible. Video stamina cost and watermark were not checked without an account. The suggestion that this means only a couple of clips/day was an estimate, not a measured result.

**Sources:** Historical test report and owner-facing skip recommendation at 05:48 BST, 2 October. The recorded site identifier was seaart.ai; no exact rewards-popup URL was preserved:
- https://seaart.ai

**Verdict/next:** Rejected for this workflow after the broken email-signup attempt, not established as impossible for all users. Keep 130 stamina/day separate from unknown clips/day. No completed account, render or watermark test should be inferred. Alternate sign-in methods were proposed, not executed.

## 2026-10-01 - Is Kaggle a plausible larger-volume route?

**Question:** Can weekly notebook GPU compute support Wan or LTX beyond tiny hosted-demo quotas?

**Findings:** The 17:06 BST comparison cited about 30 GPU hours/week from Kaggle's efficient-GPU documentation and listed T4/P100 options. Wan 2.2 5B or LTX notebooks were proposed. Setup effort, large model downloads, quantization and an estimated 10-30 minutes per clip were research estimates, not a completed notebook benchmark. Account and phone verification were identified as access requirements.

**Sources:** Historical comparison, 1 October 2026, 17:06 BST:
- https://kaggle.com/docs/efficient-gpu-usage

**Verdict/next:** Promising compute lead, not yet a tested video route. Validate current quota and hardware in the actual account before relying on them.

## 2026-10-02 - What remains unfinished on Kaggle?

**Question:** Did account setup reach GPU access or a working render?

**Findings:** By the 07:16 BST closeout, an account existed and was logged in, but phone verification was unfinished and no SMS had been sent. Earlier signup had been paused at a CAPTCHA, followed by an email-verification step. No Kaggle GPU notebook run or video result was reported.

**Sources:** Historical Kaggle closeout at 07:16 BST, 2 October; compute-documentation lead from the prior comparison:
- https://kaggle.com/docs/efficient-gpu-usage

**Verdict/next:** Parked at phone verification. Resolve that access step and then test one notebook, recording hardware, runtime, quota usage and output. This record is not permission to send an SMS, use personal details or create another account. Account credentials and verification codes are intentionally excluded.
