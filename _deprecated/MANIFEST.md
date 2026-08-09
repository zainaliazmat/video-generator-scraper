# Deprecated — moved, never deleted

Every entry: what moved, when, why, and what absorbs its work. Restoring any of these
is `git mv` back plus reverting the orchestrator lines named in the reason.

Audit trail: [audit/01-capability-matrix.md](../audit/01-capability-matrix.md) §5 (Kill List),
[audit/02-target-architecture.md](../audit/02-target-architecture.md) §7 (migration plan).

| Moved | Date | Why | Absorbed by |
|---|---|---|---|
| `fin-render` §0 (chapter draft mode) | 2026-08-09 | Two fixed commands, no decision between them; 318,807 tokens/invocation × 21 invocations. | `tools/render_chapter.py`; orchestrator calls it directly (`finance-video.md` §3b step 4). Agent kept for gate-two and master QA until `fin-review` exists (migration step 8). |
