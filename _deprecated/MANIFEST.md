# Deprecated — moved, never deleted

Every entry: what moved, when, why, and what absorbs its work. Restoring any of these
is `git mv` back plus reverting the orchestrator lines named in the reason.

Audit trail: [audit/01-capability-matrix.md](../audit/01-capability-matrix.md) §5 (Kill List),
[audit/02-target-architecture.md](../audit/02-target-architecture.md) §7 (migration plan).

| Moved | Date | Why | Absorbed by |
|---|---|---|---|
| `fin-render` §0 (chapter draft mode) | 2026-08-09 | Two fixed commands, no decision between them; 318,807 tokens/invocation × 21 invocations. | `tools/render_chapter.py`; orchestrator calls it directly (`finance-video.md` §3b step 4). Agent kept for gate-two until `fin-review` exists (migration step 8). |
| `fin-voice.md` + `tools/format/fin-voice.json` | 2026-08-09 | No judgement step exists: slice the lines, refuse to overspend, run one command, write a fixed 3-line shell script. 318,929 tokens/invocation × 5. | `tools/tts/prepare.py` (slice + guard + run + `gen_vo_<cut>.sh`) and `pipeline_check.voice_cost_guard` (the refusal, as an assert). Orchestrator calls it at `finance-video.md` §3; the stage is still marked `voice`, so `run.json` and `--resume` are unchanged. |
| `fin-render` §3 (master QA) | 2026-08-09 | Four numeric thresholds, no judgement; `check_render` already owned one of the four, so two numbers had two homes. | `pipeline_check check render` — VO drift per clip via Silero VAD, true peak vs `qa.peak_dbtp_max`, `blackdetect`, runtime vs `timing.json`. |
| `fin-archive.md` | 2026-08-09 | A template fill plus a catalog append, on haiku, loading 78,586 B of which it was forbidden to write 71,616 B. **0 invocations — it never ran on the current pipeline shape.** | `tools/close_out.py` — writes the milestone note's *measured* half, the catalog line, and the HARD-row fact promotion (absorbing `finance-video.md` §5.1). The editorial half is left as explicit TODO markers for the orchestrator, which already holds the run narrative; see the module docstring for why that split is deliberate. |
