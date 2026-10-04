# JJK webcam fighting game - research index (A06)

Owner: P. Planning/research agent: Instinct. Backfilled 2026-10-02 from the WhatsApp history (28 Sep - 2 Oct 2026).

## What the project is
A webcam computer-vision fighting game themed on Jujutsu Kaisen. Player punches at the screen and makes Domain Expansion hand signs. Purpose: fun + portfolio. Built with Claude Code; repo link not yet shared with Instinct (P, 28 Sep 20:45: "I'll give you the repo link sometime").

## Status of P's build (P's own words, 28 Sep 19:44 and 20:45)
- Single-player works. 2-player intended, P unsure how to run a server.
- Punch detection ~50% accurate, real punches are missed.
- Domain Expansion sign detection ~50% accurate.
- Laptop: normal 8GB, CPU only. Live webcam; resolution/fps unknown to P.

## Topic files
- [punch-detection.md](punch-detection.md) - missed punches, eval rig, state machine, skeleton overlay
- [domain-expansion-signs.md](domain-expansion-signs.md) - hand-sign classifier approach
- [performance-and-benchmark.md](performance-and-benchmark.md) - CPU budget, architecture, MoveNet vs MediaPipe benchmark direction
- [game-design-and-multiplayer.md](game-design-and-multiplayer.md) - single-player cursed-spirit fighting first, multiplayer later, assets, portfolio

## Evidence rules used in these files
- VERIFIED = P stated it, or a dated Instinct message reported it. Quoted with date/time (BST).
- PROPOSAL = Instinct recommendation, not yet tested on P's laptop.
- No external URLs were recorded in the history for this project. The 5 planning agents' source links were not preserved in the chat, so none are cited here. Re-source before relying on any library claim (licences, browser support, accuracy).
- Nothing has been benchmarked yet. No accuracy numbers other than P's ~50% estimates exist.

## Timeline
- 2026-09-28 19:44 P briefs the project, makes Instinct planning agent. 19:45 Instinct asks 10 questions.
- 2026-09-28 20:45 P answers. 20:48 answers locked. 20:52 5-agent plan delivered (P: "Cheers").
- 2026-09-30 06:05 CV stack final: MediaPipe Pose + Hands, MoveNet Lightning fallback.
- 2026-09-30 06:08-06:09 Multiplayer transport and free game assets findings.
- 2026-09-30 06:29 AI game jam flagged (closed that day 1pm).
- 2026-10-01 18:30 Wrap-up verdict: feasible in browser, benchmark first.
- 2026-10-02 07:52 Benchmark queued as an unattended item; no result recorded as of 17:30.

## Open questions
- Actual resolution/fps and current library in P's build (P unsure).
- Repo access, to read the real punch logic.
- Whether game keeps JJK characters (see game-design file, jam note).
