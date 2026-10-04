# Game design, single-player first, multiplayer later

## Verified (P, 2026-09-28 20:45)
- Loop: player punches at the screen and does Domain Expansion. Fights different cursed spirits.
- Single player first (locked 20:48).
- Maybe multiplayer later: players punch each other, Domain Expansion stops the other player's attacks, one winner.
- Purpose: fun + portfolio.

## Multiplayer proposal (2026-09-28 20:52)
- Build a clean event boundary now: landmarks + Punch/Domain events in, combat state separate. Multiplayer then slots in without a rewrite.
- Same-screen split zones first. Online: send landmarks over WebSocket, never video.
- Free hosting tiers such as Render sleep after 15 minutes, so unsuitable for live matches yet.

## Transport finding (2026-09-30 06:08)
Reported to P: for two-player, PeerJS peer-to-peer is the fast route. Other options reported: InstantDB temp apps (deleted after 24h), Cloudflare Durable Objects (reported 100k req/day free), Ably (reported 6M msgs/month free). Free-tier numbers were not re-verified here.

## Assets (2026-09-30 06:09)
Reported: a CC0 boxer sprite pack (punches, blocks, KO) and Kenney particles/impact sounds, downloaded and checked. Files not listed in the history.

## Portfolio packaging (2026-09-28 20:52 proposal)
README with side-by-side GIF (game + skeleton overlay), metrics table, CLAUDE.md for Claude Code discipline, itch.io browser port once detection is solid.

## Game jam note (2026-09-30 06:29)
Ultimate AI-Powered Game Jam #4 closed 30 Sep 1pm. Instinct noted JJK characters would need swapping for original ones. P did not reply in the history reviewed. Same IP caution applies to any public release.
