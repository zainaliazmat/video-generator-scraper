# Paste this into a new session

---

You are a Principal Systems Architect continuing a pipeline refactor already in progress in
`/home/zain-ali/Documents/YoutubeScraper`. Phases 0–2 are **complete and approved**; a
measured baseline exists; three migration steps have landed. **Do not restart the audit.**

**Read these four files first, in this order, before touching anything:**

1. `audit/05-baseline.md` — the measured baseline. Every claim you make about improvement
   is against these numbers.
2. `audit/02-target-architecture.md` — the approved design and the migration plan (§7).
   **§2 contains two levers I withdrew after measuring them; do not re-propose them.**
3. `audit/01-capability-matrix.md` — §4 Proposed Roster, §5 Kill List. This is the contract
   for what dies and what absorbs it.
4. `CLAUDE.md` and `vault/CLAUDE.md` — the project's own rules. `vault/CLAUDE.md` is
   mandatory before any channel work.

`audit/00-discovery.md` is the raw factual map — read it only when you need a specific fact
about the system as it was. Two of its items are marked SUPERSEDED; honour the supersession.

---

## Where things stand

**Branch `refactor/pipeline-v2`, working tree clean, 2 commits ahead of `master`.**
`master` is untouched. Nothing has been deleted anywhere; removals go to
`_deprecated/2026-08-09/` with a row in `_deprecated/MANIFEST.md`.

| | |
|---|---|
| Agents | still **13** — no agent file has been removed yet |
| Landed | BOX packs (step 4), `tools/render_chapter.py` (part of step 7) |
| Dropped | step 5 (shared contract file) and step 6 (re-cut format slices) — **both measured wrong, see below** |
| Next | rest of step 7, then step 8, then step 9 |

**The video run is paused deliberately.** `passive-income-number` has ch1–3 locked on both
cuts (6 of 13 chapters). It is NOT to be finished — the creator stopped it at ch3 once the
baseline turned out to be recoverable without it. `run.json.baseline_note` records this.
Resume only if explicitly asked: `/finance-video --resume passive-income-number`.

**Backups exist.** `studio/videos/` is now its own git repo (text source only; renders,
images and audio excluded because the project's own rule says those are re-buyable).
`studio/` itself is gitignored by the parent and is NOT a repo, despite what `CLAUDE.md:14-15`
still claims.

---

## The measured baseline — memorise these five numbers

From `tools/run_metrics.py --slug passive-income-number`, 99.2% coverage:

| Metric | Value |
|---|---|
| Total billed tokens | **85,165,530** (+762M cache-read) |
| Locked chapters | **6 of 13** |
| Tokens per locked chapter | **14,194,255** |
| **Marginal cost of locking an already-assembled chapter** | **~7,350,000** |
| Chapter loop share (`assets`+`build`+`editor`+`render`+`ceo`) | **70%** of subagent tokens |

**Beat 7.35M, not 14.2M.** The all-in average flatters any change, because
`fin-script`/`fin-storyboard`/`fin-audit`/`fin-voice`/`fin-research`/`fin-facts` are paid once
per cut and amortise. Comparing against the easier number is the trap.

Per-invocation means worth knowing: `fin-build` 439,515 · `fin-assets` 483,560 ·
`fin-script` **1,345,257** · `fin-storyboard` **1,147,599** · `fin-render` 318,807 ·
`fin-editor` 308,842 · `fin-ceo` 208,050 · `fin-voice` 312,202.

---

## How to measure anything

```bash
python3 tools/run_metrics.py --slug <slug>      # real per-agent tokens, from CC transcripts
python3 evals/run.py                            # 10 asserted quality checks over every cut
python3 evals/run.py --slug passive-income-number
python3 tools/pipeline_check.py doctor --tier medium   # preflight; regenerates packs + views
```

Token data lives in `~/.claude/projects/<cwd-slug>/<session>/subagents/agent-*.jsonl` +
`.meta.json`. Nothing in the repo records tokens; the transcripts do.

**Current eval state: 6 targets, 48 pass, 0 fail, 0 blocker failures.** Across all history:
41 targets, 16 blocker failures, all historical (rules introduced after those cuts shipped).
`evals/rubric.md` defines Tier B (judged, needs eyes) — Tier A cannot see whether a photograph
is *relevant*, which is the top defect source. Never let a green Tier A stand in for Tier B.

**The rule: Tier A blocker failures must not increase, and Tier B B1/B2 must not drop.
A change that lowers tokens while worsening either is reverted.**

---

## Two levers I withdrew — do not re-propose them

Both were in the approved plan. Both were **my arithmetic errors**, caught by measuring
before building. They are documented in `audit/02-target-architecture.md` §2.

1. **Shared contract file.** I claimed extracting four repeated blocks into one
   `packs/contract.md` saves ~12,000 B. Measured: the blocks total 6,309 B across 13 agents,
   **485 B per agent**. Each invocation loads exactly **one** agent definition — the other 12
   copies are never in context. Replacing 485 B of inline text with a pointer plus a ~2,000 B
   `Read` is **4× worse**. The duplication is a maintenance cost, not a token cost.
2. **Re-cutting `tools/format/` slices.** Same error (each agent reads only its own slice).
   And the test for "unused" — whether the prompt names the key — is invalid: `fin-voice`
   never writes the word `cuts` but needs `cuts.<cut>.voice_id` (`fin-voice.md:14,31`).
   Acting on it would cause the silent too-narrow diet that `write_agent_views`'
   `_if_a_constant_is_missing` hatch already warns about. **Deferred to `fin-retro`**, which
   can read real `MISSING-CONSTANT:` lines instead of guessing.

**Generalise the lesson: "duplication across agent files" is free at runtime. Only what one
agent loads in one invocation costs anything.**

---

## What to do next, in order

### Step 7 (finish it) — the remaining mechanical deletions

`tools/render_chapter.py` already replaced `fin-render`'s draft mode and is wired into
`finance-video.md` §3b step 4. `fin-render.md` §0 now refuses `--chapter` and points at the
script. The agent still exists for gate-two and master QA.

Still to do:

- **`fin-voice` → `tools/tts/prepare.py`** (~60 lines) + one `pipeline_check` assert.
  All four of its responsibilities are deterministic: slice VO lines into `lines.json`
  ("slice the source text exactly; never retype it" — `fin-voice.md:40-43`), run the existing
  `tools/tts/batch.py`, the cost guard (`audit-<cut>.md` must contain PASS **and** chars ≤1.3×
  budget, `fin-voice.md:27-31`), and write a fixed 3-line `gen_vo_<cut>.sh`.
  Worth **2.8%** of subagent tokens. `tools/transcript.py` already does the same
  slice-never-retype join mechanically — read it first and reuse rather than re-implement.
- **`fin-archive` → `tools/close_out.py`** (~120 lines). A milestone-note template fill plus a
  `vault/index.md` append (`fin-archive.md:21-36`). It loads 78,586 B of which it is
  **forbidden to write 71,616 B**. It has never run on the current pipeline shape.
  Also absorb the orchestrator's fact-promotion step (`finance-video.md` §5.1).
- **`fin-render`'s master QA → `pipeline_check check render`.** Four numeric thresholds:
  VO drift ≤0.1s (subtract `qa.vad_onset_latency_seconds` first), peak below −1 dBTP,
  black-segment scan, runtime vs `timing.json`. `check_render` already owns part of this.

### Step 8 — the merges (first behaviour change; measure alone)

- **`fin-editor` + `fin-ceo` → `fin-review`**, two labelled passes (1 correctness,
  2 retention), **one** sheet read, **one** round budget of 3 total (today it is 3 + 2 = up to
  5 rework cycles, each costing a rebuild and a draft render).
  Keep the checklists separate; merge the context load, not the lenses. `fin-ceo.md` already
  carries "Do not re-litigate the editor's job" — that instruction exists because the overlap
  is real.
- **`fin-research` + `fin-facts` → `fin-evidence`.** Honest framing: this is **cosmetic** —
  3 of 153 invocations, 2.4% of tokens. Do it for the roster count, and say so plainly.

### Step 9 — the one change that actually alters quality

**Image acceptance becomes terminal at `fin-assets`, on full-resolution frames.**
Build `tools/image_sheet.py` (~50 lines) tiling the *promoted full-res jpgs* for a chapter.
`fin-assets` reads its own sheet before returning; a failure is re-picked without touching
`fin-build`.

Rationale (`audit/01-capability-matrix.md` §2): the sound-off test is written **twice, in
full** — `fin-assets.md:197-208` and `fin-editor.md:59-73`, same five checks, same worked
examples. It runs first on a 6-cell preview that `fin-assets.md:237-240` documents as lossy
("sheets have shipped showing 4 of 12 cells"), then again after a 3-minute draft render.
A defect caught late costs **4 invocations**; caught early, **1**.

⚠ **The post-render sheet does not go away.** `chapter_sheet.py:18-22` documents why the
encoded file is irreplaceable: Lottie has two failure modes that render a silent blank and
pass every static check. A jpg sheet catches the image-*selection* subset only.

**This is the highest-risk change in the refactor** (risk #2 in `audit/02` §8). Do it last,
alone, and measure post-lock image defects before and after. If they rise, revert.

### Then

Step 10 `storyboard.json`; step 11 journal + `fin-retro` (Phase 6); step 12 upgrade
HyperFrames 0.7.66 → 0.7.102 and re-run evals; step 13 evaluate registry blocks. Phase 7 is
the handover doc.

---

## Traps this project has already paid for

- **A checker that cannot see the work reports green.** `fin-assets.md:260-263`. Two live
  examples found during this audit: the md5 dedupe glob read zero files for every
  chapter-based cut, and the tofu guard could not import fontTools under system python3
  (fixed) *and still* cannot see the font name because it lives in the linked stylesheet
  (**deliberately not fixed** — activating a never-fired gate would have contaminated the
  baseline; scheduled for step 7).
- **An asset swap needs a REBUILD, not just a re-render.** The path stays the same, so
  nothing looks wrong. Cost two drafts and a full editor pass on hi ch3.
  `tools/render_chapter.py` now refuses when `build.mjs` is newer than `index.html`.
- **Verify, do not infer.** Two reviewers asserted a CSS feather would be a "no-op" on
  another chapter without measuring; both were wrong. The build agent measured and was right.
- **A grep is not evidence.** I twice nearly reported a false defect in my own pack extractor
  from a case-sensitive or mis-numbered grep. Read the content.
- **`archive_cut.py:32`** keeps `assets/img/CREDITS.txt`; chapter projects write to
  `assets-ch<N>/final/CREDITS.txt`, so the glob misses them. Attribution is not lost (the
  cut-level file covers it) but a chapter directory is not the complete record it claims.
  One-line fix, logged, not applied.

## HyperFrames reality (verified, not assumed)

Three versions coexist: projects pin **0.7.66** (what runs), `studio/` builds **0.7.10**,
npm latest is **0.7.102**. `hyperframes check` does **not exist** in 0.7.10. The registry has
**147 items** and the pipeline uses **zero** — every composition comes from a hand-written
per-chapter `build.mjs` (357,832 B for one video). 19 skills published, **7 installed**.
**HyperFrames MCP is unauthorized** — treat as UNVERIFIED, never claim an MCP capability.
`media-use` needs HeyGen auth that does not exist here and returns vectors, not photographs.

## How the creator wants to be talked to

Short reports — 3–4 lines, plain everyday words, as if explaining to a child. No jargon.
Put the detail in a file and point at it. Lead with what's good, what's bad, what to change.
Flag large spends before making them; they will choose.
