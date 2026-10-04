# Multi-agent orchestration - research note (2 Oct 2026)

Findings from a 13-agent / 23-topic sweep of public documentation and
engineering posts on how efficient agent systems run parallel work. Sources at
the bottom. Framing: what the cited public systems do and recommend.

## 1. When to fan out
- Parallelize analysis, not edits: many agents may research; one agent owns
  writes to shared files. Parallel-writer swarms conflict. (Cognition)
- Fan out for breadth-first, independent slices. Tightly coupled work with
  shared context is a poor fit. (Anthropic)
- Scale effort to task complexity: simple fact = 1 agent, 3-10 tool calls;
  comparison = 2-4 agents, 10-15 calls each; complex = 10+ with divided duties.
  (Anthropic)
- Multi-agent runs cost ~15x chat tokens; token usage explained 80% of quality
  variance on Anthropic's research eval. Use swarms only for high-value,
  parallelizable work. (Anthropic; Claude Code costs doc)

## 2. Delegation briefs
Every worker brief needs four parts (Anthropic found vague briefs cause
duplicated work and gaps):
1. Objective - one distinct slice, plus what sibling workers cover.
2. Output format - condensed structured findings + sources; full detail goes to
   a file/artifact, only the summary returns to the lead.
3. Tool/source guidance - prefer primary/official sources; start broad, then
   narrow.
4. Explicit boundaries - scope exclusions, effort cap, when to stop.

## 3. Context discipline
- Each worker gets a clean context window; only condensed results return.
  (Anthropic, Cursor)
- Leads keep decisions and state only; large material stays as references
  (paths, URLs, IDs) loaded just-in-time. (Anthropic)
- Compact before the limit: keep decisions/open issues/constraints, drop raw
  tool output. Critical instructions go at the start or end of a prompt.
  (Anthropic; Lost-in-the-Middle; Chroma context-rot)
- Instruction files stay short (<~200 lines), checkable, pruned. (Claude Code
  memory doc)

## 4. State and resume
- Save the plan to durable state before spawning; context truncates.
  (Anthropic)
- Checkpoint each step; resume from the last checkpoint, never restart.
  (LangGraph, Temporal, Anthropic harnesses)
- One feature per worker per run; end every unit in a mergeable state.
  (Anthropic harnesses)
- Model "waiting on the human" as durable state, not a live agent. (Temporal)

## 5. Errors and retries
- Timeout = outcome unknown. Read target state before re-issuing any write.
  (Stripe/AWS idempotency)
- Retry only transient errors, with backoff + jitter and capped attempts;
  permanent errors escalate. (AWS, Temporal)
- Workers return structured errors (what failed, tried, partial results,
  retryable). (Anthropic)
- Hard step/turn cap + explicit stop condition on every loop. (LangGraph)

## 6. Verification
- Every task gets a runnable pass/fail check; require the evidence in the
  report. (Anthropic best practices)
- Verify with a fresh-context checker, not the producer. Devin's clean-context
  reviewer catches ~2 bugs per PR. (Cognition)
- Separate "complete" (all pieces arrived) from "valid" (contents verified).
  (BagIt RFC 8493)
- Fetch only URLs actually seen in results; never construct URLs. Treat thin
  fetches as unverified. (Claude web-fetch doc)
- Separate citation pass maps every retained claim to its source. (Anthropic
  CitationAgent)

## 7. Merge and synthesis
- Raw worker reports are append-only; one synthesis step, one owner. (LangGraph
  reducers, Cognition)
- Reconcile explicitly: compare by subject/date/scope; conflicts go in a table;
  only disputed claims go back for targeted research. (Anthropic)
- N duplicated reports are not N independent sources. (Anthropic)
- Final gate: accuracy, requested coverage, source quality, internal
  consistency. (Anthropic evaluator loop)

## 8. Human-in-the-loop (what public frameworks recommend)
- Gate per tool/action, not per agent: read-only runs free; risky actions
  (send, spend, delete) pause. (OpenAI HITL)
- Batch pending approvals into one list for one decision pass. (OpenAI,
  LangGraph)
- Support approve / reject-with-feedback / edit-in-place. (LangGraph)
- Pause by persisting state so runs resume after hours. (OpenAI, LangGraph)

## 9. Scheduling
- Event-driven wakes primary; slow polling watchdog as backstop only.
  (Airbyte, Temporal)
- Overlap policy: skip a cycle if the previous run is still going. (K8s,
  Temporal)
- Stale scheduled runs get dropped, not run late. (K8s start deadline)

## 10. Cost control
- Cheapest sufficient model per worker; top model only for hard reasoning.
  (Claude Code costs)
- Hard per-run budget caps; attribute spend per worker; recurring agents are
  the hidden cost. (Claude Code costs)

## 11. Git discipline for agent-written repos
- Commit with explicit paths; conventional commits; verify log + clean tree +
  byte-readback after writing; push --force-with-lease only. (git docs)
- Parallel writers on separate branches/worktrees; one merger. (Cursor,
  git-worktree)

## 12. Artifacts
- Workers write full outputs to files and return references + short summaries;
  preserve originals through merges. (Anthropic)
- Collision-resistant names; immutable revisions. (GitHub artifact docs)
- Consumers wait for producer success before assembling. (GitHub needs)

## Sources
- anthropic.com/engineering/multi-agent-research-system
- anthropic.com/engineering/effective-context-engineering-for-ai-agents
- anthropic.com/engineering/building-effective-agents
- anthropic.com/engineering/effective-harnesses-for-long-running-agents
- anthropic.com/engineering/claude-code-best-practices
- code.claude.com/docs/en/sub-agents, /en/memory, /en/costs
- platform.claude.com/docs/en/build-with-claude/context-windows, /context-editing
- platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use,
  /web-fetch-tool, /memory-tool
- cognition.com/blog/dont-build-multi-agents, /multi-agents-working
- openai.github.io/openai-agents-python/multi_agent, /guardrails,
  /human_in_the_loop
- developers.openai.com/api/docs/guides/agents
- cursor.com/docs/context/subagents, /configuration/worktrees, /rules,
  /background-agent
- aider.chat/docs/repomap.html, /docs/usage/modes.html
- docs.temporal.io (retry-policies, schedule, ai), docs.langchain.com
  (checkpointers, persistence, errors)
- docs.aws.amazon.com/scheduler, kubernetes.io cron-jobs docs
- stripe.com/blog/idempotency, aws.amazon.com/builders-library
- git-scm.com/docs (worktree, commit, fsck, push), conventionalcommits.org
- docs.github.com/en/actions (artifacts), rfc-editor.org/rfc/rfc8493
- arxiv.org/abs/2503.13657, /abs/2312.04511, /abs/2307.03172
- research.trychroma.com/context-rot
