# Hyperframes adoption notes

Adopted 3 October 2026 after a security review that came back clean with precautions. Source: https://github.com/heygen-com/hyperframes by HeyGen, Apache-2.0. Docs: https://hyperframes.heygen.com/introduction

Vendored skill copies live in research/video-gen/hyperframes-skills/, taken from tag v0.8.115. See hyperframes-skills/ATTRIBUTION.md and hyperframes-skills/LICENSE.

## Rules

- Pin to version 0.8.115. Never run `npx hyperframes@latest` or an unpinned `npx hyperframes`. Commit the lockfile.
- Telemetry off: set `HYPERFRAMES_NO_TELEMETRY=1` and `DO_NOT_TRACK=1` in every environment that runs it.
- Never use the auth, cloud or publish commands. Never set or store a HeyGen key.
- Vendor GSAP and fonts locally so renders are offline and reproducible. No CDN loads at render time. GSAP has its own licence: check it before vendoring.
- Render locally only (headless Chrome and FFmpeg, Node 22+).
- Animation must be seek-driven. Run `npx hyperframes lint` before render.

## Notes

- Skills are agent instructions. Skim any copied file before an agent follows it, and skip any helper that fetches or executes remote code.
- The scope of what was copied, and anything skipped, is listed in hyperframes-skills/ATTRIBUTION.md.

## Copied scope and skipped files

Copied unmodified from tag v0.8.115: the 21 SKILL.md files and every skill's top-level references/*.md (153 files). Skipped: all scripts and code (222 files, including 9 .sh helpers), nested or archived markdown, and all assets. The full skipped list is in hyperframes-skills/SKIPPED.md so individual scripts can be cherry-picked later after a case-by-case read.

## Copied docs that conflict with the rules above

Review of the copied markdown found no prompt-injection style text, but several skills tell an agent to do things the rules above forbid. Treat these instructions as overridden by this note:

- `npx hyperframes auth status` / `auth login`, HeyGen credentials (`HEYGEN_API_KEY`, `~/.heygen/credentials`) and HeyGen-hosted voice or music (faceless-explainer/SKILL.md, media-use/audio references, hyperframes-cli/references/cloud.md).
- `hyperframes cloud render`, `cloudrun` and `publish` (hyperframes-cli references, hyperframes/references/capability-menu.md, hyperframes-registry/references/contributing.md).
- `npx hyperframes@latest upgrade --project . --check` (hyperframes/SKILL.md). Use the pinned 0.8.115 only.

Files that mention any of these:

- faceless-explainer/SKILL.md
- general-video/SKILL.md
- hyperframes-cli/SKILL.md
- hyperframes-cli/references/cloud.md
- hyperframes-cli/references/cloudrun.md
- hyperframes-cli/references/preview-render.md
- hyperframes-cli/references/upgrade-info-misc.md
- hyperframes-registry/references/contributing.md
- hyperframes/SKILL.md
- hyperframes/references/capability-menu.md
- media-use/audio/references/bgm.md
- media-use/audio/references/requirements.md
- media-use/audio/references/tts.md
- music-to-video/SKILL.md
- pr-to-video/SKILL.md
- product-launch-video/SKILL.md
- remotion-to-hyperframes/SKILL.md
- remotion-to-hyperframes/references/api-map.md
