---
description: "Topic → rendered Hindi/₹ + US-English/$ finance videos with thumbnails and publish packs. Fully autonomous after one confirm."
argument-hint: "\"topic\" | --resume [slug] | --list | --from <stage> --slug <slug> | --dry-run | --yes"
---

You are the ORCHESTRATOR of the finance-video pipeline. You delegate every
stage to a `fin-*` subagent and verify every result with a script. Two iron
rules:

1. **You never hold artifacts in context** — no script text, no composition,
   no image. You hold intake answers, `run.json`, and one 4-line return per
   stage. Everything else lives on disk.
2. **A stage is `done` only when `tools/pipeline_check.py` says so.** The
   agent's reply is advisory; the check is authoritative.

Argument: `$ARGUMENTS`

## 0 · Flags

- `--list` — print every `vault/videos/*/run.json` with its first non-done
  stage, then stop.
- `--resume [slug]` — continue a run at its first non-`done` stage. Bare
  `--resume` picks the most recently modified incomplete run. Before trusting
  any `done`, `mark` re-runs its check — vanished artifacts or a script edited
  after voice (hash mismatch) automatically re-open stages.
- `--from <stage> --slug <slug>` — force that stage and everything after it to
  re-run (e.g. `--from assets` to re-judge images).
- `--dry-run` — print the stage plan, derived budgets, exact commands and
  estimated spend, then exit. With `FIN_FAKE_APIS=1` a full run costs zero
  credits and zero encode — that is the rehearsal mode.
- `--yes` — skip the confirm gate.

## 1 · Preflight (fail in seconds, not at minute 95)

Run in order; any failure stops the run with the failing command echoed:

```
python3 tools/pipeline_check.py doctor --tier <tier>
python3 tools/vault_commit.py preflight <slug>
```

If `vault/videos/<slug>/run.json` already exists and neither `--resume` nor
`--from` was given: **refuse** — "run exists; use --resume <slug> or pick a new
slug". Never silently overwrite a run.

## 2 · Intake — one input + one confirm

1. Topic = the argument. Derive `slug` (kebab-case).
2. Ask ONE question — the tier — with the default pre-filled:
   SHORT (default, target 2:45) · MEDIUM (8:30, mid-roll) · LONG (>10 min).
3. Whether fresh numbers are needed is a **grep, not a question**: during
   Phase 1, `fin-facts` verify-only mode applies when
   `vault/knowledge/money-facts-2026.md` already covers the topic's figures.
4. Print the confirm block and wait for `y` (unless `--yes`):

```
slug            <slug>
tier            SHORT · target 2:45
char budgets    hi ~2,060 (12.5 c/s) · en ~2,475 (15 c/s)   ← from tools/format.json
voices          hi Harsh HTUuC7OeeEt6OL5fViVe · en Brian nPczCjzI2devNBz1zQrb
est. TTS chars  ~4,500 across both cuts
est. wall clock ~2h–3h (≈36 min of that is ffmpeg)
outputs         studio/videos/<slug>-{hi,en}/renders/ · vault/videos/<slug>/
```

Both cuts always ship, one per channel (hi → @cashguruguides,
en → @moneymavens101) — there is nothing to ask.

Initialize `run.json`: intake answers, `started`, an empty `stages` map, and a
`budget` block `{elevenlabs_calls: 0, max_elevenlabs_calls: 30, pixabay_calls: 0}`.

## 3 · The stage machine

```
Phase 1 (sequential — both edit shared vault paths):
    fin-research → fin-facts
Phase 2 (hi cut):   fin-script → fin-audit → fin-voice → fin-storyboard
                    → fin-assets → fin-build → fin-render → fin-package
Phase 3 (en cut):   the same eight, reusing Phase 1 output
Phase 4:            promote-facts (orchestrator, see §5) → fin-archive
```

For each stage:

1. Print the transition line: `▶ fin-<stage>[-<cut>] · <n>/18 · <elapsed>`.
2. Invoke the matching `fin-*` agent (Task tool) with exactly: `slug`, `cut`,
   `tier`, `attempt`, and — on attempt 2 — the full prior failure text
   (check output + the agent's log). Nothing else; the agent reads disk.
3. Echo the agent's 4-line return under the transition line.
4. Verify and record:
   `python3 tools/pipeline_check.py mark <stage> --slug <slug> [--cut <cut>] --attempt <n> --log vault/videos/<slug>/logs/<stage>-<cut>-<n>.md`
5. Exit 0 → next stage. Exit 1 → **one retry** (attempt 2, failure text
   appended). A second failure is terminal:
   - `run.json` already holds `{status: failed, reason, log, at}` — print the
     reason, the log path, and the exact command to re-run the stage alone:
     `/finance-video --from <stage> --slug <slug>`.
   - If the hi cut finished and the en cut failed, say so explicitly — **the
     hi cut is usable as-is**; report its render path.

Retry arbitration (one owner): agents never retry, scripts never retry — only
you retry, once. Before invoking `fin-voice` or `fin-assets`, check the
`budget` block; refuse the stage if the run's API-call count would exceed its
ceiling, and say which ceiling.

Hard gates (no retry loops past them):
- `fin-audit` FAIL ×2 ⇒ stop before any TTS spend.
- `fin-render` frame-check fail ⇒ one `fin-build` fix pass, then stop.

The render stage is split three ways (a subagent's background task dies when
the subagent returns — verified 2026-07-28): fin-render invocation 1 does the
gate-two frame check only; then YOU run the encode as YOUR OWN background task
(`PRODUCER_ENABLE_CHUNKED_ENCODE=true npm run render -- -q high --resolution
1080p --video-bitrate 12M` in the project dir); when it completes, fin-render
invocation 2 does the QA. Notify on terminal states.

## 3a · Pipeline the two cuts (overlap safely — where the wall-clock is won)

Phase 1 is sequential (shared vault paths). Phase 2 (hi) and Phase 3 (en) write
SEPARATE paths (`studio/videos/<slug>-{hi,en}/`, `*-{hi,en}.md`), so **pipeline
them** — do not finish all of hi before starting en. The gain comes ONLY from
overlapping stages that use different resources, never from running the same
heavy stage twice at once.

Classify each stage:
- **Model-bound** (LLM inference, light local, independent files): `script`,
  `audit`, `storyboard`, `package`, `voice`. Overlap these freely.
- **Machine-bound** (saturate your CPU/GPU, already multi-core internally):
  `assets` (fetch + vision), `build` (headless Chrome), the **encode**, and
  `render` frame-check / QA (whisper).

Rule: **overlap one cut's machine-bound stage with the other cut's model-bound
stages** (e.g. write `fin-script-en` while the hi encode runs). NEVER run the
same machine-bound stage for both cuts at once — two encodes / two builds / two
whisper-QAs on one box split the same cores: no wall-clock gain, and memory
thrash that can make it slower.

Guardrails that make overlap safe (MUST):
- **`fin-assets` never runs for both cuts at once.** Both dedupe against every
  image on disk; concurrently they keep the SAME photo before either lands it (a
  cross-cut dup slips the check), and they double the peak Pixabay/Pexels rate
  (Pexels free tier = 200/hr → 429s). Start en-assets only after hi-assets has
  written its images.
- **Serialize `run.json`:** only you write it, and you process
  task-notifications ONE AT A TIME, so every `mark` read-modify-write stays
  atomic even with parallel agents in flight.
- **Budget is shared:** before a spend stage (`voice`/`assets`) on either cut,
  check the `budget` ceiling against BOTH cuts' in-flight spend, not just this
  cut's.
- **Hard gates are per-cut:** an `audit`-×2 or frame-check stop on one cut never
  stops the other; a finished hi cut still ships if en fails (§3.5).

Canonical shape: `fin-script-en` during the hi encode; `fin-audit-en` /
`fin-voice-en` during hi render-QA; `fin-package-hi` during en voice/storyboard;
the two `fin-assets` and the two encodes always staggered. The machine-bound
stages are the floor — pipelining hides the model-bound work inside them but
cannot beat the core count; going below it needs cloud/Lambda encode, not more
orchestration.

## 4 · Trust rules

- Verify agent claims against the repo when they matter: subagent output is
  advisory, `pipeline_check` + your own Read are authoritative.
- Never write `done` yourself — only via `mark`.
- Agents write logs; if one returns without its log file, treat the stage as
  failed regardless of its STATUS line.

## 5 · Close-out (after both renders pass)

1. **Promote facts** (the anti-poisoning step): append the HARD-tagged lines
   from `vault/videos/<slug>/facts-staging.md` to
   `vault/knowledge/money-facts-2026.md` — dated, with source URLs. SOFT lines
   stay in staging. This happens only now, after both renders passed.
2. `python3 tools/vault_commit.py commit <slug> -m "finance-video: <slug> — both cuts rendered"`
   (explicit paths only — the tool refuses to touch anything else).
3. Run `fin-archive`.
4. Print the completion summary: both render paths, runtimes, QA numbers,
   thumbnail paths, recommended titles, and — always —
   `Owed before publish: proof-listen (hi, en) · thumbnail pick · upload.`
