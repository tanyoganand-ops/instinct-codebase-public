# Codebase memory design

Research date: 1 October 2026.

## Recommendation
Use a tiny root `CLAUDE.md` importing a concise, shared `memory.md`. Keep the task backlog separate and open project-specific notes only when needed. Add real build/test commands once real source is present, not speculative commands for a scaffold.

## Verified documentation facts
Claude Code reads project `CLAUDE.md` files and supports `@path` imports. Imported files still consume startup context. Its documentation recommends clear, specific, consistent instructions and a target below 200 lines. Nested instructions and path-scoped rules can reduce irrelevant context for larger repositories.

Claude auto memory is different: its project-local memory directory contains `MEMORY.md`, whose first 200 lines or 25KB load at startup. It is machine-local and is not the same as a committed lowercase `memory.md`. The root import makes this repository's named file useful without pretending it is automatic memory.

The official best-practices guide recommends giving work a verification method, planning before larger changes, and keeping instructions lean. Anthropic's context-engineering article recommends the smallest high-signal context and retrieving details when needed. HumanLayer's guide independently supports a short project orientation and linked, task-specific details instead of putting everything in one file.

## Applied choices
- `CLAUDE.md`: only the startup entry point and pointers.
- `memory.md`: project map, stable preferences, accuracy boundaries and the repeatable workflow.
- `tasks.md`: grouped, numbered historical requests and considered opportunities. Every item awaits the owner's review.
- `research/codebase-memory.md`: sources and design rationale; not imported at startup.
- Existing project folders stay unchanged. No framework, dependency install or deployment was invented.

## Tradeoffs and open checks
A single large history file would preserve more detail but waste context and mix stale requests with current work. A highly fragmented rules tree would be premature for four README-only folders. Start small, then split project-specific details when there is real source.

This is a documentation layout, not a new running automation system. Claude Code was not launched against this repository in this task. On the user's machine, use `/context` or `/memory` to confirm what loaded; run `/init` after importing real project code and review any generated commands before accepting them.

## Sources inspected
1. Official Claude Code memory documentation: https://code.claude.com/docs/en/memory
2. Official Claude Code best practices: https://code.claude.com/docs/en/best-practices.md
3. Anthropic technical article, effective context engineering: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
4. Anthropic Help Center, project context and prompts: https://support.claude.com/en/articles/14553240-give-claude-context-claude-md-and-better-prompts
5. HumanLayer independent engineering guide: https://www.humanlayer.com/blog/writing-a-good-claude-md
6. Community guide, used as supporting evidence only: https://claudecodeguide.dev/docs/foundations/claude-md
7. Anthropic context-engineering cookbook: https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools

Official documentation owns the filename, import and loading semantics. Community advice is supporting rationale, not a substitute for those semantics.
