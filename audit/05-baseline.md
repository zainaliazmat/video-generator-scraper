# 05 — Measured baseline (current 13-agent system)

**This supersedes [00-discovery.md §6 item 8](00-discovery.md)**, which said token cost
"cannot be measured from artifacts." That was true of the repo and wrong overall: Claude Code
writes per-subagent transcripts with full usage records, and they were on disk the whole time.

Extractor: [tools/run_metrics.py](../tools/run_metrics.py) (`--selftest` covers both
transcript shapes). Raw data: [metrics-baseline-passive-income-number.json](metrics-baseline-passive-income-number.json).

---

## 1 · Where the numbers come from

```
~/.claude/projects/<cwd-slug>/
  <session>.jsonl                       ← orchestrator turns (message.usage)
  <session>/subagents/
      agent-<id>.meta.json              ← {agentType, description, toolUseId}
      agent-<id>.jsonl                  ← every child turn, with usage
```

The `subagents/` directory is authoritative. The parent transcript's
`toolUseResult.totalTokens` is a fallback for older sessions and is present on only 18% of
historical calls — which is why the first extraction attempt looked unusable.

**Billed tokens** = `input + cache_creation + output`. `cache_read` is reported separately
throughout and never folded in: it is discounted, and including it would roughly 7× every
figure in this document.

**Scope:** the three sessions that ran `passive-income-number` — `2a8cff1e`, `e3cdf0b8`,
`256591ad`. Coverage **123 of 124 fin-agent invocations (99.2%)**.

---

## 2 · The baseline

| Agent | Calls | Billed tokens | Mean/call | Share | Agent hours |
|---|---:|---:|---:|---:|---:|
| `fin-assets` | 31 | 15,345,645 | 495,020 | **26.4%** | 15.0 |
| `fin-build` | 29 | 13,028,442 | 449,256 | **22.4%** | 10.6 |
| `fin-script` | 5 | 6,725,134 | **1,345,026** | 11.6% | 3.0 |
| `fin-editor` | 17 | 5,514,991 | 324,411 | 9.5% | 3.5 |
| `fin-render` | 17 | 5,419,735 | 318,807 | 9.3% | 4.4 |
| `fin-storyboard` | 4 | 4,590,399 | **1,147,599** | 7.9% | 1.5 |
| `fin-audit` | 6 | 3,453,740 | 575,623 | 5.9% | 1.4 |
| `fin-voice` | 5 | 1,594,647 | 318,929 | 2.7% | 0.9 |
| `fin-ceo` | 7 | 1,480,420 | 211,488 | 2.5% | 1.0 |
| `fin-facts` | 1 | 480,203 | 480,203 | 0.8% | 0.3 |
| `fin-research` | 2 | 426,268 | 213,134 | 0.7% | 0.2 |
| **Subagents** | **124** | **58,059,624** | | | **41.8** |
| Orchestrator | 1,585 turns | 12,406,618 | | | |
| **TOTAL** | | **70,466,242** | | | |

Plus **448,082,790 cache-read tokens** — context re-sent across turns. At the usual 10%
discount that is ~44.8M billed-equivalent, i.e. the cache-read stream costs roughly **64% as
much again** as everything in the table above.

### Per unit of output

| Metric | Value |
|---|---|
| Locked chapters produced | **4 of 13 planned** |
| Billed tokens per locked chapter | **17,616,560** |
| Agent invocations per locked chapter | **31.0** |
| Agent-hours per locked chapter | 10.5 |
| Straight-line projection for the full 13 chapters | **~229,000,000 tokens** |

### 2.1 · Final baseline — the run as paused, 2026-08-09

The run was carried two chapters further (en ch3, hi ch3) and then **paused at ch3 on both
cuts** by creator decision, once the token baseline turned out to be recoverable from
transcripts rather than requiring a completed run.

| Metric | At 4 chapters | **At 6 chapters (final)** |
|---|---:|---:|
| Locked chapters | 4 | **6 of 13** — ch1–3 on both cuts, a matched set |
| Subagent billed tokens | 58,059,624 | **67,262,202** |
| Orchestrator billed tokens | 12,406,618 | **17,903,328** |
| **Total billed** | 70,466,242 | **85,165,530** |
| cache-read | 448,082,790 | 762,527,367 |
| fin-agent invocations | 124 | **153** |
| **Tokens per locked chapter** | 17,616,560 | **14,194,255** |
| Invocations per locked chapter | 31.0 | **25.5** |

**Cost per chapter falls as the run continues**, because `fin-script`, `fin-storyboard`,
`fin-audit`, `fin-voice`, `fin-research` and `fin-facts` are paid once per cut and amortise:
those six are 22.4% of subagent tokens and produced no chapters at all.

**Marginal cost is the number the refactor must beat.** Locking en ch3 and hi ch3 from
already-assembled state cost **14,699,288 tokens for 2 chapters = ~7.35M each** — roughly half
the all-in average. A refactor that only reduces per-chapter cost is competing against 7.35M,
not 17.6M.

Ranking is unchanged and the two-agent concentration got sharper: `fin-assets` 24.4% +
`fin-build` 21.6% = **46.0%** of subagent tokens in two agents.

**Accuracy at the pause: `evals/run.py --slug passive-income-number` scores all six locked
chapters 48 pass · 0 fail · 0 blocker failures.** Raw:
[evals/results/after-ch3-2026-08-09.json](../evals/results/after-ch3-2026-08-09.json).

---

## 3 · What this confirms and what it corrects

**Confirms the Phase 2 thesis.** The chapter loop — `assets` + `build` + `editor` + `render`
+ `ceo` — is **70.1%** of all subagent tokens. [01 §0(b)](01-capability-matrix.md) argued this
from invocation counts alone; the token data agrees within a point.

**Corrects the emphasis on `fin-script` and `fin-storyboard`.** Those two run 4–5 times a run
but cost **1.35M and 1.15M tokens per call** — 3–6× the mean of every other agent. They are
also the two with the largest static context loads (78,015 B and 98,376 B) and the two that
emit the largest artifacts (`script-hi.md` 99,696 B, `storyboard-hi.md` 100,294 B). The pack
work in [02 §2](02-target-architecture.md) targets exactly these two hardest, which was
guessed from byte counts and is now confirmed by spend.

**Refutes nothing in the roster.** The three agents on the kill list for being mechanical —
`fin-voice` (2.7%), `fin-render` (9.3%), `fin-archive` (absent this run) — total **12.0%** of
subagent tokens. Removing them is real money, not just tidiness: `fin-render` alone is 5.4M
tokens for work that is two bash commands and four numeric thresholds.

**One number worth staring at.** `fin-assets` spent **15.0 agent-hours and 15.3M tokens** —
more than any other stage — and image rejection is still, in its own words, "the top defect
source on record" (`fin-assets.md:7-8`). That is the case for [02 §4](02-target-architecture.md):
the money is already being spent on looking at images; it is being spent at the wrong time, on
lossy previews, and then again after a render.

---

## 4 · Limits of this baseline, stated

1. **It is a partial run** — 4 of 13 chapters. The per-chapter figures are sound; the
   full-run projection is straight-line and assumes later chapters cost like earlier ones.
   Finishing the run (your answer #4) replaces the projection with a measurement.
2. **One invocation of 124 is uncovered** (0.8%) — a background dispatch whose child
   transcript is absent.
3. **Orchestrator turns include this audit's own sessions where they overlap** the same
   transcripts. The subagent figures do not — they are attributed per `agentType`.
4. **Cache-read pricing is assumed at 10%.** The token count itself is measured; the
   billed-equivalent is an estimate and is labelled as one.
5. **These are tokens, not dollars.** No pricing table is applied anywhere in this document.

---

## 5 · Success criteria — how each will now be measured

| Criterion | Baseline | Measured by |
|---|---|---|
| 1 · agent count reduced | 13 | count of `.claude/agents/fin-*.md` |
| 2 · tokens per video lower | **17.6M / locked chapter** | `tools/run_metrics.py --slug <slug>` |
| 3 · eval accuracy equal or higher | **16 blocker failures across 41 cuts** | `python3 evals/run.py` — §6 |
| 4 · first-attempt render success up | **0 of 4 chapters locked on round 1** (rounds 2, 2, 3, 3) | `run.json.chapters[*].round` |
| 5 · human interventions down | **23** (13 `owed.*` + 6 `tool_fixes` + 4 rulings) | `runs/<id>/interventions.md` (Phase 6) |
| 6 · journal + one `fin-retro` diff | none exist | Phase 6 |

---

## 6 · Accuracy baseline (Tier A)

`python3 evals/run.py` — 10 asserted checks over 41 finance cuts. Rubric:
[evals/rubric.md](../evals/rubric.md). Raw:
[evals/results/baseline-2026-08-09.json](../evals/results/baseline-2026-08-09.json).

**302 pass · 43 fail · 65 n/a · 16 blocker failures.**

| Check | Fail | Pass | Reading |
|---|---:|---:|---|
| `watermark` | 14 | 26 | all pre-August cuts; the rule postdates them |
| `track_alternation` | 13 | 28 | same — the rule is dated 2026-08-01 (`fin-build.md:194-198`) |
| `photo_every_scene` | 6 | 35 | `needs-vs-wants` + `pay-yourself-first` predate the 2026-07-28 rule; `jmm/hi-ch1` is the retired vector-only experiment |
| `no_network_fetch` | 5 | 36 | `50-30-20-rule`, `emergency-fund` — the oldest cuts |
| `no_repeated_image` | 3 | 38 | `emergency-fund`, `first-lakh` ×2 — genuine repeats |
| `image_credits` | 2 | 38 | `emergency-fund` hi + en — **exactly the two `vault/CLAUDE.md` already documents as having no CREDITS** |
| `currency_purity` · `vo_text_hygiene` · `timing_coherence` · `captions` | 0 | — | clean everywhere they apply |

**The six current chapter projects (`passive-income-number-{hi,en}-ch1..3`) pass every
applicable check.** Every blocker failure is historical, and each traces to a rule introduced
after the cut was built. That is the signal the checks are calibrated rather than merely
strict: `image_credits` independently landed on the two cuts the vault had already flagged
by hand.

**Ceiling, stated:** Tier A cannot see whether a photograph is *relevant* — the top defect
source on record. That is Tier B, it needs eyes, and no number here substitutes for it.

### Two defects found at preflight for the baseline run (2026-08-09)

**1 · The tofu guard could not run, and `doctor` blocked the whole pipeline on it.**
`font_codepoints()` did `from fontTools.ttLib import TTFont` in the *current* interpreter and
returned `None` on failure. Every agent and the orchestrator invoke
`python3 tools/pipeline_check.py` (`finance-video.md:38`), and system python3 here is
**PEP 668 EXTERNALLY-MANAGED**, so fontTools exists only in the venv. Result: the guard
silently skipped every build — precisely what its own error message warns about — while
`doctor` reported `FAIL` and refused to start any run. The sibling `faster_whisper` probe
forty lines below already shells out to `venv/bin/python`; the fontTools path now matches it.
**Fixed** (`tools/pipeline_check.py`, `font_codepoints` + `_font_codepoints_via_venv`);
`doctor` now passes and `font_codepoints()` returns 97 codepoints under system python3.

**2 · The tofu guard is still inert on chapter compositions — NOT fixed, deliberately.**
`uncovered_glyphs()` returns `[]` unless the literal string `FinanceSans` appears in the
composition HTML. Chapter compositions declare `font-family: var(--font)` and the face is
named only in the **linked** `blockframe.css` — which is exactly what `fin-build.md:37-45`
mandates ("Link the system; never copy it"). So the design rule that fixed the lost-font bug
is the same rule that blinded this guard. Verified: all six current chapter projects report
`links_FinanceSans=False` and score clean regardless of content.

Left unfixed on purpose. Activating a gate that has never once fired, in the middle of the
run being used as the baseline, is risk #3 in
[02 §8](02-target-architecture.md) — the baseline would measure a hybrid. Scheduled for
migration step 7. The fix is to resolve linked stylesheets before the check, or to test for
`var(--font)` as well.

### One defect found by the first eval run

`tools/archive_cut.py:32` keeps `assets/img/CREDITS.txt`. Chapter projects write attribution
to `assets-ch<N>/final/CREDITS.txt`, which that glob does not match, so archived chapter
subdirectories carry no CREDITS of their own. **Attribution is not lost** — the cut-level
file covers the same images, which is why the check passes once scoped to the archive unit —
but a chapter directory alone is not the complete reproducing record the archive claims to be.

Same class of bug as the md5 dedupe glob documented at `fin-assets.md:72-80`, which "read
ZERO files for every chapter-based cut" and "could not fail from 2026-08-05 until 2026-08-09."
A one-line fix to the keep-list; logged, not yet applied — no code changes before the
baseline run.
