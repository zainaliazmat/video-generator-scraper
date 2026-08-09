# 02 — Target Architecture `[GATE — awaiting approval]`

Builds on [00-discovery.md](00-discovery.md) and [01-capability-matrix.md](01-capability-matrix.md).
**Nothing here is implemented.** No file outside `audit/` has been changed by this phase.

---

## 0 · Two ways this phase could go wrong, stated first

**(a) Designing a v2 that cannot be measured against v1.** You approved a *real* baseline run
(answer #4) that is also the completion of `passive-income-number`. If any part of this design
lands before that run finishes, the baseline measures a hybrid and the whole exercise is
unfalsifiable. **Migration step 2 is therefore "run the old system to completion," and every
step after it is gated on that.**

**(b) Trading accuracy for cheapness on the one axis where this system must not be cheap.**
Success criterion 3 says eval accuracy must hold or improve. The riskiest change below is
moving image acceptance earlier (§4, migration step 8): done wrong it *lowers* the bar rather
than moving it. It is deliberately the **last** behavioural change, after every mechanical one,
so it is measured alone.

---

## 1 · Roster + rationale

Eight agents. `Static context` = agent definition + its `tools/format/` slice + its packs —
everything loaded before it touches a run artifact. Current figures are measured
([00-discovery.md §2](00-discovery.md)); target figures are budgets this design commits to.

| Agent | One job | Tool allowlist (minimum viable) | Model | Static ctx now | Static ctx target |
|---|---|---|---|---|---|
| `fin-evidence` | Study the lane **and** source every figure to ≥2 independent sources | `WebSearch, WebFetch, Read, Write, Grep, Bash(study.py only)` | frontier | 57,608 | **≤ 13,000** |
| `fin-script` | Write the VO script to the derived budget | `Read, Write, Grep, Glob` | frontier | 78,015 | **≤ 20,000** |
| `fin-audit` | Re-fetch every source independently and try to break the script, **before any spend** | `Read, Write, Edit, Grep, WebFetch, WebSearch` | frontier | 19,805 | **≤ 17,000** |
| `fin-plan` | Per-scene design + image query + transition + SFX → `storyboard.json` + ≤1 page prose | `Read, Write, Grep` | frontier | 98,376 | **≤ 22,000** |
| `fin-assets` | Source images **and terminally accept them** at full resolution | `Bash(stock/lottie tools), Read, Write, Edit` | frontier (vision) | 69,474 | **≤ 23,000** |
| `fin-build` | Apply the plan's design to the composition | `Read, Write, Edit, Bash(npm/npx/node in project dir), Glob` | frontier | 114,722 | **≤ 24,000** |
| `fin-review` | One gated chapter review: pass 1 correctness, pass 2 retention | `Bash(sheet+ffmpeg read-only), Read, Grep, Glob` | frontier | 95,594 | **≤ 25,000** |
| `fin-package` | Thumbnail + publish pack + Gate-2 compliance | `Bash(snapshot/autocomplete/transcript), Read, Write, Grep, WebSearch` | frontier | 47,057 | **≤ 17,000** |
| | | | | **580,651** | **≤ 161,000** |

*(The eight rows above exclude `fin-voice` 14,701, `fin-render` 16,340 and `fin-archive`
81,177 — deleted — so the roster total differs from the 692,869 all-13 figure.)*

### 1.1 · Why every surviving agent is frontier tier

You asked for cheap models on mechanical steps. **After this refactor there are no mechanical
agent steps left** — they all became scripts (§1.2). The two agents that carry `model: haiku`
today are `fin-render` (`fin-render.md:5`) and `fin-archive` (`fin-archive.md:5`) — and those
are precisely the two the kill list removes. The model-tier lever and the delete-the-agent
lever point at the same two files, and deleting strictly dominates downgrading: a deleted
agent costs zero tokens and cannot be wrong.

Downgrading any survivor would hit a judgment step where the documented failures are expensive:
image acceptance (`fin-assets.md:7-8` "the top defect source on record"), fabricated figures
(`fin-audit.md:32-38`), or a re-timed chapter (`chapter_project.py:20-24`). **No survivor is
downgraded, and that is a deliberate refusal, not an oversight.**

### 1.2 · What absorbs the deleted work

| New script | Absorbs | Lines (est.) |
|---|---|---|
| `tools/tts/prepare.py` | `fin-voice` #10, #12, #13 — slice lines, cost guard, write `gen_vo.sh` | ~60 |
| `tools/render_chapter.py` | `fin-render` #32 — draft render + contact sheet | ~40 |
| `pipeline_check check render` (extend) | `fin-render` #35 — VO drift, dBTP, blackdetect, runtime | ~80 |
| `tools/close_out.py` | `fin-archive` #48 + orchestrator #49 — milestone note, index line, fact promotion | ~120 |
| `tools/image_sheet.py` | **NEW** — contact sheet from promoted full-res jpgs (§4) | ~50 |

~350 lines of Python replacing 3 agent definitions (24,196 B of prompt) and, on the last run,
17 invocations.

---

## 2 · Context budget — how the target is reached

Three measured levers, in order of size.

### Lever 1 — extract the BOXes (measured: −89.6%)

Five knowledge notes already carry a `> **BOX**` section, and four agents are **already told
to read only that box**: `fin-storyboard.md:31-33`, `fin-build.md:73-76`, `fin-editor.md:95-97`,
`fin-ceo.md:94-96`, `fin-assets.md:45-47`. `Read` loads the whole file anyway.

| Note | Full | BOX | BOX share |
|---|---|---|---|
| `design-finance-blockframe.md` | 34,793 | 3,632 | 10.4% |
| `design-chapter-archetypes.md` | 22,415 | 2,199 | 9.8% |
| `stock-photo-sourcing.md` | 19,950 | 2,128 | 10.7% |
| `design-icons-emoji-lottie.md` | 14,707 | 1,950 | 13.3% |
| `evidence-discipline.md` | 12,454 | 967 | 7.8% |
| **total** | **104,319** | **10,876** | **10.4%** |

**This is a pure win with no behaviour change** — the agents are not asked to read anything
different from what their prompts already tell them to read. It is the cleanest measured
number in the audit.

### ~~Lever 2 — the shared contract, written once instead of eleven times~~ — **WITHDRAWN, measured wrong**

**Corrected 2026-08-09 before implementation.** The claim was that extracting four repeated
blocks into one `packs/contract.md` saves ~12,000 B. It does not, and would make token cost
**worse**.

Measured across all 13 agents: the four blocks total **6,309 B**, a mean of **485 B per
agent** — not 1,100.

The arithmetic error was counting duplication *across files* as if it were paid at runtime.
**Each invocation loads exactly one agent definition**; `fin-storyboard`'s copy of the
boilerplate is never in `fin-build`'s context. So the per-invocation cost is 485 B, and
replacing it with a pointer (~80 B) plus a `Read` of a ~2,000 B shared file costs **2,080 B —
4× worse**.

The 6,309 B is a **maintenance** cost (13 places to edit), not a token cost. At 485 B ≈ 121
tokens against `fin-build`'s measured **439,515 tokens per invocation**, it is 0.03%. Not
worth a change in either direction. **Step 5 is dropped.**

### ~~Lever 3 — stop over-slicing `tools/format/`~~ — **WITHDRAWN, not safely actionable**

Same arithmetic error, plus a second problem. `tools/format.json` is 24,403 B and its 11
derived views total 102,312 B — but again, each agent reads only its own slice, so the 4.2×
"duplication" costs nothing at runtime. The only real question is whether a given slice is
wider than its agent needs.

Testing that by grepping each prompt for its slice's key names gives this:

| Slice | Size | Bytes of keys never named in the prompt |
|---|---:|---:|
| `fin-editor.json` | 14,566 | 6,774 (`layout`, `chapter_design`) |
| `fin-voice.json` | 4,966 | 3,291 (`cuts`, `tiers`) |
| `fin-audit.json` | 9,014 | 3,291 (`cuts`, `tiers`) |
| all 11 | 102,312 | 21,716 |

**That evidence is not good enough to act on.** `fin-voice` never writes the word `cuts`, but
`fin-voice.md:14` needs `cuts.<cut>.voice_id` and `:31` needs the cut's `chars_per_second` —
the key is required and unnamed. Trimming on a grep would produce exactly the silent
too-narrow diet that `write_agent_views` already warns about in its own `_if_a_constant_is_missing`
escape hatch.

The mechanism to do this safely already exists and points the other way: the
`MISSING-CONSTANT: <key>` log line detects a diet that is **too narrow**, from evidence.
Detecting one that is **too wide** needs run evidence this refactor does not have. **Step 6 is
deferred until the `MISSING-CONSTANT` lines from several runs can be read**, which is
`fin-retro`'s job (Phase 6), not a guess made now.

### What actually paid

Lever 1 (BOX extraction) was the whole win: **−84.4% on notes, −49.8% on static context for
the five affected agents.** Levers 2 and 3 were arithmetic, and the arithmetic was wrong.
The remaining large, safe reduction is **step 7 — deleting the three agents that carry no
judgment**, measured at **12.0% of subagent tokens**.

### 2.1 · The packs

| Pack | Contents | Est. size | Read by |
|---|---|---|---|
| `packs/contract.md` | I/O envelope, log format, untrusted-input rule, never-write list, the relevant 1 page of `vault/CLAUDE.md` | 2,000 | all 8 |
| `packs/money-discipline.md` | `evidence-discipline` BOX, HARD/SOFT, one-write rule, currency purity | 2,000 | evidence, script, audit, review |
| `packs/script-style-hi.md` / `-en.md` | distilled from `long_form_scripting.md` (30,768) + `us-english-script-style.md` + `india-finance-market.md` | 4,000 ea | script |
| `packs/design-system.md` | `design-finance-blockframe` BOX + `design-chapter-archetypes` BOX + the `chapter_design` constants | 6,000 | plan, build, review |
| `packs/image-acceptance.md` | `stock-photo-sourcing` BOX + **the sound-off test, once** | 3,000 | assets, review |
| `packs/vector-art.md` | `design-icons-emoji-lottie` BOX | 2,000 | plan, assets, build |
| `packs/thumbnail.md` | distilled from `design-thumbnail-ai-enhance.md` (24,380) | 4,000 | package |

Full notes stay on disk and stay authoritative. A pack that cannot answer something names the
note and the section — progressive disclosure, not deletion.

---

## 3 · Orchestration

```
PHASE 1 — evidence                                    [sequential; shared vault paths]
    fin-evidence  ──► video-study.md + facts-staging.md

PHASE 2 — script & plan            [per cut; hi and en pipelined per §3a rules, unchanged]
    fin-script ──► script-<cut>.md
        │
        ▼  ══ GATE 1 ══  fin-audit → audit-<cut>.md must contain PASS
        │                FAIL ×2 ⇒ stop. No TTS spend has occurred.
        ▼
    tools/tts/prepare.py + tools/tts/batch.py ──► lines.json, timing.json   [script, no agent]
        │
        ▼
    fin-plan ──► storyboard.json + storyboard-<cut>.md (≤1 page)

PHASE 3 — the chapter loop                                       [per chapter, sequential]
    fin-assets ──► assets-ch<N>/final/*.jpg + CREDITS
        │
        ▼  ══ GATE 2 (NEW) ══  tools/image_sheet.py → fin-assets reads its OWN full-res
        │                      sheet and accepts or re-picks. TERMINAL HERE.
        ▼
    tools/chapter_project.py ──► index.html scaffold + verbatim timing lift   [script]
    fin-build  ──► design applied
        │
        ▼  ══ GATE 3 ══  hyperframes check  AND  pipeline_check check build
        ▼
    tools/render_chapter.py ──► DRAFT-ch<N>.mp4 + SHEET-ch<N>.jpg            [script]
        │
        ▼  ══ GATE 4 ══  fin-review (pass 1 correctness, pass 2 retention)
        │                PASS ⇒ lock.  REWORK ⇒ fin-build fix ⇒ re-draft ⇒ fin-review.
        │                ONE budget: 3 rounds total, then escalate to creator.
        ▼
    lock → run.json.chapters[N]

    ── all chapters locked ⇒ frames_sheet.py + concat preview ⇒ creator batch review ──

PHASE 4 — master
    concat ──► orchestrator's own background encode ──► mix.py ──► loudnorm.py ──► transcript.py
        │
        ▼  ══ GATE 5 ══  pipeline_check check render  (drift, dBTP, blackdetect, runtime)
        ▼
    fin-package ──► thumbnail + publish pack + captions + Gate-2

PHASE 5 — close-out
    tools/close_out.py ──► milestone note, vault/index.md, fact promotion   [script]
    tools/vault_commit.py commit
```

**Parallelism is unchanged** from `finance-video.md:340-385`. Those rules are evidence-backed
(both cuts' `fin-assets` must never run concurrently or they keep the same photo and double
the Pexels rate toward the 200/hr free-tier limit) and this design keeps them verbatim.

**Gate count: 5, down from a system where three of thirteen agents had no gate at all**
([00-discovery.md §2.1](00-discovery.md)). `fin-review` gets one, via a new
`pipeline_check check review`.

### 3.1 · The round budget, unified

Today: 3 editor rounds **plus** 2 CEO rounds = up to 5 rework cycles per chapter, each costing
a rebuild + a draft render (`finance-video.md:261-264`). Under `fin-review` it is **3 total**.
`fin-ceo.md:128-131` already argues for this ceiling in its own words: "Two reviewers who each
demand a re-render for preference will never converge, and every rework costs a real draft
render."

---

## 4 · The one behavioural change

**Image acceptance becomes terminal at `fin-assets`, on full-resolution frames.**

Today the sound-off test runs twice — once at fetch on a 6-cell preview grid that
`fin-assets.md:237-240` documents as lossy ("sheets have shipped showing 4 of 12 cells"), and
again after a 3-minute draft render at `fin-editor.md:59-73`. A defect caught late costs
**4 invocations** (re-fetch → rebuild → re-draft → re-review); caught early it costs **1**.

`tools/image_sheet.py` tiles the **promoted full-res jpgs** for a chapter into one sheet.
`fin-assets` reads its own sheet before returning, and a failure there is re-picked without
touching `fin-build`.

⚠️ **The post-render sheet does not go away, and this is not a downgrade of the bar.**
`chapter_sheet.py:18-22` documents why the encoded file is irreplaceable: "Lottie scenes have
two failure modes … that render a silent blank and pass every static check; only the encoded
file proves what a viewer will see." A jpg sheet catches the *image-selection* subset —
repetition, wrong currency, subject absent, picture argues with the line. `fin-review` still
watches the encoded draft, once, and stops being the place image choices are litigated.

---

## 5 · Context flow — artifact-passing, not accumulation

Every agent receives exactly this, and reads everything else from disk:

```json
{ "slug": "...", "cut": "hi|en", "chapter": 3, "attempt": 1,
  "inputs":  ["vault/videos/<slug>/storyboard.json", "..."],
  "prior_failure": null }
```

Every agent returns exactly this:

```json
{ "status": "ok|fail",
  "artifacts": ["studio/videos/<slug>-hi-ch3/index.html"],
  "warnings":  ["s27 photo is 1.4x upscaled"],
  "unresolved":["s31 cut-in dropped — no honest @commons match"],
  "log": "vault/videos/<slug>/logs/build-hi-ch3-1.md",
  "figures": [ {"value":"₹2,500","source":"facts-staging.md#L44","confidence":"HARD"} ] }
```

- `figures[]` is **mandatory** for any agent that touches a money number
  (`fin-evidence`, `fin-script`, `fin-audit`, `fin-build`, `fin-package`). Missing `source`
  or `confidence` is a gate failure, not a warning. Fabricated numbers are the
  highest-severity failure in this system and this is the mechanism that makes them
  structurally visible instead of prose-visible.
- `unresolved[]` replaces the `owed.*` convention that produced **13 open items** in one run's
  `notes.md` ([00-discovery.md §4.4](00-discovery.md)) — machine-readable, so it can be
  counted and closed rather than reread.
- The orchestrator holds intake answers, `run.json`, and one envelope per stage. It never
  holds a script, a storyboard or a composition. That rule already exists
  (`finance-video.md:10-12`); this makes it enforceable.

**`notes.md` stops being a dumping ground.** It is replaced by `runs/<run-id>/` (Phase 6):
`decisions.jsonl`, `metrics.json`, `interventions.md`. The 322-heading, 157,996 B narrative
file is the thing that convinced me a journal is a mechanism and not a nice-to-have.

---

## 6 · Budget table

### 6.1 · Static context — measured now, budgeted after

| Stage | Now (B) | Target (B) | Δ |
|---|---|---|---|
| evidence (`research`+`facts`) | 57,608 | 13,000 | −77% |
| script | 78,015 | 20,000 | −74% |
| audit | 19,805 | 17,000 | −14% |
| plan (`storyboard`) | 98,376 | 22,000 | −78% |
| assets | 69,474 | 23,000 | −67% |
| build | 114,722 | 24,000 | −79% |
| review (`editor`+`ceo`) | 95,594 | 25,000 | −74% |
| package | 47,057 | 17,000 | −64% |
| voice | 14,701 | **0** (script) | −100% |
| render | 16,340 | **0** (script) | −100% |
| archive | 81,177 | **0** (script) | −100% |
| **TOTAL** | **692,869** | **161,000** | **−77%** |

**Assumptions, stated:** (a) BOX extraction is measured at −89.6% on the five notes and
assumed to hold for the two not yet measured (`design-thumbnail-ai-enhance`,
`long_form_scripting`); (b) the shared contract saves ~1,100 B × 11; (c) `format.json` slices
are re-cut so no slice exceeds 8,000 B after `chapter_design`/`architectures`/`vector_art` move
into `packs/design-system.md`; (d) rewritten agent definitions average 5,000 B — today's mean
is 7,002 B and the two biggest (`fin-assets` 16,582, `fin-build` 15,452) are large **because
they inline knowledge that becomes packs**.

### 6.2 · Per-run cost — now measured

**Updated 2026-08-09.** This section originally said no "before" existed. It does — Claude
Code's per-subagent transcripts carry full usage. Full figures:
[05-baseline.md](05-baseline.md).

| Baseline, `passive-income-number` (3 sessions, 99.2% coverage) | Value |
|---|---|
| subagent billed tokens | 58,059,624 |
| orchestrator billed tokens | 12,406,618 |
| **total billed** | **70,466,242** (+448,082,790 cache-read) |
| fin-agent invocations | 124 |
| locked chapters produced | 4 of 13 |
| **billed tokens per locked chapter** | **17,616,560** |
| **invocations per locked chapter** | **31.0** |

Where it goes: the chapter loop (`assets` 26.4% + `build` 22.4% + `editor` 9.5% +
`render` 9.3% + `ceo` 2.5%) is **70.1%** of subagent tokens — the invocation-count argument in
[01 §0(b)](01-capability-matrix.md) holds on tokens too.

What the kill list removes by arithmetic alone: `fin-voice` 2.7% + `fin-render` 9.3% +
`fin-ceo` 2.5% = **12.0% of subagent tokens (7.0M)**. What the pack work targets:
`fin-script` (1.35M/call) and `fin-storyboard` (1.15M/call) are the two most expensive calls
in the system *and* the two largest static context loads — 78,015 B and 98,376 B.

Everything beyond that arithmetic — the earlier image gate, the unified round budget, the
smaller contexts — remains a hypothesis that the post-migration re-run measures against these
numbers.

---

## 7 · Migration plan

Ordered. Each step independently revertible. Branch `refactor/pipeline-v2`; removals move to
`_deprecated/2026-08-09/` with a line in `_deprecated/MANIFEST.md`. Nothing is deleted.

| # | Step | Touches | Revert | Gated on |
|---|---|---|---|---|
| 0 | ✅ **done** — `studio/videos` backup repo | `studio/videos/.git` | `rm -rf studio/videos/.git` | — |
| 1 | Build `evals/` + token instrumentation (Phase 5) — **wraps the current system, changes nothing** | new dir + an orchestrator logging hook | delete `evals/` | — |
| 2 | **Baseline: finish `passive-income-number` on the current 13-agent system, HyperFrames 0.7.66, unchanged** | run artifacts only | n/a | step 1 |
| 3 | Create branch `refactor/pipeline-v2` | git | delete branch | step 2 |
| 4 | Extract BOXes → `packs/`; repoint agent `Reads` lines | 5 notes (unchanged) + 8 agent files | revert 8 files | step 3 |
| 5 | `packs/contract.md`; strip the 4 duplicated blocks from 11 agents | 11 agent files | revert | step 4 |
| 6 | Re-cut `tools/format/` slices | `pipeline_check doctor` | regenerate | step 5 |
| 7 | **Mechanical deletions**: `fin-voice`, `fin-render`, `fin-archive` → 4 new scripts | 3 agents → `_deprecated/`, 4 new `tools/*.py`, orchestrator | restore 3 files | step 6 |
| 8 | **Merges**: `fin-editor`+`fin-ceo` → `fin-review`; `fin-research`+`fin-facts` → `fin-evidence`; unify round budget | 4 agents → `_deprecated/`, 2 new | restore 4 files | step 7 + evals |
| 9 | **The behavioural change**: `tools/image_sheet.py`, image acceptance terminal at `fin-assets` | 1 new script, `fin-assets`, `fin-review` | revert 2 files | step 8 + evals |
| 10 | `storyboard.json` schema; `fin-plan` emits data + ≤1 page | `fin-plan`, `fin-build`, `fin-assets`, `fin-review`, `pipeline_check` | revert | step 9 + evals |
| 11 | Structured journal + `fin-retro` (Phase 6) | new `runs/`, 1 new agent | delete | step 10 |
| 12 | **HyperFrames 0.7.66 → 0.7.102**, re-run evals | project `package.json` pins | re-pin 0.7.66 | step 11 |
| 13 | Evaluate registry blocks (`parallax-zoom`, `grain-overlay`, captions) | `motion.js`, scaffold | revert | step 12 |

Steps 4–7 are **behaviour-preserving by construction** — same instructions, fewer bytes; same
work, moved from prompt to script. Steps 8–10 change behaviour and each is measured alone
against the step-2 baseline. **Vault restructure (Phase 3) rides on step 4** and is scoped there
rather than as a separate big-bang rewrite.

---

## 8 · Risk register

| # | Risk | Severity | Detection | Mitigation |
|---|---|---|---|---|
| 1 | A pack drops a rule that only lived in a note's body, and a defect it prevented returns | **high** | eval suite (Phase 5) includes one brief per documented past defect: wrong-currency imagery, uncredited image, re-timed chapter, blank Lottie, transition overlap | Packs are additive-only at first: the pack is written, the note stays, and the agent's `Reads` line names both for one full run before the note is dropped |
| 2 | Moving image acceptance early **lowers** the bar rather than moving it | **high** | eval rubric scores image defects found *after* lock; if post-lock image defects rise, the change failed | Step 9 is last and measured alone. Post-render sheet is retained in full |
| 3 | Baseline is contaminated by a partially-migrated system | **high** | step 2 completes before branch creation at step 3 | Ordering is the mitigation; `refactor/pipeline-v2` does not exist until the baseline lands |
| 4 | Merging `fin-editor`+`fin-ceo` collapses two lenses into one and misses what one lens caught | medium | eval rubric tracks findings by lens (correctness vs retention); `fin-ceo`'s regression check (`fin-ceo.md:76-79`) becomes an explicit pass-2 item | Two labelled passes in one agent, one sheet read, findings tagged by pass — merge the context load, not the checklists |
| 5 | `storyboard.json` loses nuance that prose carried | medium | `fin-build`'s `unresolved[]` count rises; schema misses force escalation | Step 10 keeps a ≤1-page prose companion; schema starts as a superset of the columns four agents already parse |
| 6 | Deleting `fin-voice` loses its cost guard | medium | `pipeline_check check voice` asserts audit=PASS and chars ≤1.3× budget before `batch.py` runs | The guard becomes an assert, which is strictly harder to skip than a prompt instruction |
| 7 | 0.7.66 → 0.7.102 changes render output or `check` semantics | medium | step 12 re-runs the full eval suite; 92 versions of drift is a lot | Pin is one line in each project `package.json`; revert is one line |
| 8 | `fin-retro` proposes diffs that bloat prompts back up | medium | Phase 6 promotion criteria: ≥3 recurrences **and** evals hold or improve | Lessons are `candidate` until both conditions hold; retired lessons are removed, not archived in-prompt |
| 9 | The baseline run needs TTS credits it does not have | **retired** | — | **Verified 2026-08-09:** 163 clips on disk (hi 81, en 82); both `script_sha256` values in `run.json` match the current files, so no stage re-opens on hash mismatch. Remaining spend is image fetches only |
| 10 | `studio/` monorepo (7.4 GB, 0.7.10) drifts further from the pinned 0.7.66 and confuses tooling | low | `hyperframes info` in a project vs `studio/packages/cli` version | Out of scope for this refactor; recorded so it is a decision rather than a surprise |

---

## 9 · What this design deliberately does not do

- **Does not adopt `faceless-explainer` or `general-video`.** Not installed; `faceless-explainer`
  caps at ~3 min and states every visual is LLM-invented (`SKILL.md:8`), which contradicts this
  channel's photograph-per-frame rule.
- **Does not adopt `media-use` for images.** Its image resolver searches HeyGen's vector
  catalog and needs auth that does not exist on this machine.
- **Does not touch the two-cut pipelining rules** (`finance-video.md:340-385`) — they are
  evidence-backed and correct.
- **Does not replace `hyperframes check` with `pipeline_check`, or vice versa.** They assert
  different things ([01 §1 row 29](01-capability-matrix.md)); this is a redundancy I looked for
  and did not find.
- **Does not add `fin-retro` yet.** It prevents nothing until journals exist.

---

## 10 · Decision requested

Approve, or tell me what to change:

1. **The roster: 13 → 8** (§1), with `fin-voice`/`fin-render`/`fin-archive` becoming ~350 lines
   of Python and `editor`+`ceo` / `research`+`facts` merging.
2. **The ordering** (§7): baseline first on the *unchanged* system, branch second, mechanical
   changes before behavioural ones, image gate last.
3. **The one behavioural change** (§4): image acceptance terminal at `fin-assets`, on full-res
   frames, with the post-render sheet retained.

**I have not written any code and will not until you approve.**
