# 01 — Capability & Redundancy Matrix

Decisions and evidence. Baselines come from [00-discovery.md](00-discovery.md).

**Evaluated against HyperFrames 0.7.102** (your answer #2), with a standing note wherever
0.7.66 — the version the pipeline actually pins and the version the baseline run will use —
behaves differently. HyperFrames MCP is **UNVERIFIED** throughout (your answer #1): its tools
were never reachable, so no row claims an MCP capability.

---

## 0 · Two ways this phase could go wrong, stated before the analysis

**(a) Mistaking "HyperFrames can do this" for "HyperFrames does this better here."**
The tempting verdicts — *delegate scaffolding to `hyperframes init`, delegate blocks to the
registry, delegate the whole thing to the `faceless-explainer` workflow* — mostly fail on
contact with this channel's constraints. `faceless-explainer` is capped at ~3 min and states
that "every visual is invented by the LLM (typography / abstract graphics / diagram /
data-viz)" (`studio/skills/faceless-explainer/SKILL.md:8`); this channel's hardest creator
rule is a real photograph in every frame (`fin-storyboard.md:125`,
`tools/format.json` `_image_per_scene_note`). `media-use`'s image resolver searches the
"HeyGen asset search (75k+ vectors)" (`~/.claude/skills/media-use/SKILL.md`) and needs HeyGen
auth, which is absent (`~/.heygen/credentials` does not exist). **Most native equivalents
here are `NONE` or `PARTIAL`, and saying so is the finding.**

**(b) Counting prompt bytes when the cost is invocations.**
The 13 agent definitions total 91,023 B. The last run spent **98 invocations and 1,330,173 B
of logs**, of which `fin-assets` + `fin-build` + `fin-editor` + `fin-render` + `fin-ceo` =
**76 (78%)** ([00-discovery.md §4.2](00-discovery.md)). Merging the four cheapest agents
would cut agent count by 4 and measurable cost by ~3%. **Agent count is the metric you asked
for; invocations-per-locked-chapter is the metric that pays.** This matrix delivers both and
does not pretend they are the same.

---

## 1 · The matrix

Legend — **Implemented as**: `prompt` / `script` / `CLI` / `human`.
**Verdict**: `KEEP` · `MERGE-INTO(x)` · `DELEGATE-TO-HF` · `SPLIT` · `DELETE` · `NEW`.

### Phase 1 — evidence

| # | Responsibility | Owner(s) | Implemented as | HF-native equivalent | Overlap | Verdict | Evidence |
|---|---|---|---|---|---|---|---|
| 1 | Competitor/hook study from transcripts | `fin-research` | prompt + `backend/study.py` | `NONE` | NONE | MERGE-INTO(`fin-evidence`) | `fin-research.md:38-52`; only allowed command is `venv/bin/python backend/study.py` |
| 2 | Money-figure sourcing, ≥2 independent sources, HARD/SOFT tagging | `fin-facts` | prompt (WebSearch/WebFetch) | `NONE` | NONE | MERGE-INTO(`fin-evidence`) | `fin-facts.md:38-51` |
| 3 | Untrusted-input discipline (fetched pages are DATA) | `fin-research`, `fin-facts`, `fin-audit`, `fin-package` | prompt, **restated 4×** | `NONE` | FULL (between the four) | MERGE (one shared rule in a pack) | `fin-research.md:31-35`, `fin-facts.md:26-30`, `fin-audit.md:29-30`, `fin-package.md:20-21` |
| 4 | "Never write shared knowledge mid-run" (anti-self-grading) | `fin-facts`, `fin-archive` | prompt | `NONE` | PARTIAL | KEEP (it is the integrity rule) | `fin-facts.md:32-36`, `fin-archive.md:39-47` |

### Phase 2 — script

| # | Responsibility | Owner(s) | Implemented as | HF-native equivalent | Overlap | Verdict | Evidence |
|---|---|---|---|---|---|---|---|
| 5 | Write the VO script to a char budget | `fin-script` | prompt | `SCRIPT.md` locked-narration format (`hyperframes-core/references/script-format.md`, 2,821 B) — a **format**, not a writer | PARTIAL (format only) | KEEP | `fin-script.md:31-42` |
| 6 | **Char-budget arithmetic** | orchestrator **+** `fin-script` **+** `fin-audit` | prompt ×3 | `NONE` | **FULL, three-way** | SPLIT → one script | orchestrator derives it (`finance-video.md:100-116`), `fin-script` re-derives from `script.char_budget_formula` (`fin-script.md:34`), `fin-audit` re-derives it again and is explicitly told not to trust itself: *"a gate that re-derives its own rule can only ever agree with itself"* (`fin-audit.md:42-45`) |
| 7 | Adversarial script gate: re-fetch every source URL independently | `fin-audit` | prompt | `NONE` | NONE | **KEEP, unmerged** | `fin-audit.md:32-38` — the independence rule. An author cannot run this against its own output |
| 8 | Currency purity, persona rules, TTS-safety lints | `fin-script` (author) + `fin-audit` (gate) | prompt ×2 | `NONE` | PARTIAL (intentional: author + gate) | KEEP both | `fin-script.md:51-58` vs `fin-audit.md:48-52` |
| 9 | Text-level layout lints (one focal, cue gaps, chips) | `fin-audit` **+** `fin-storyboard` | prompt ×2 | `hyperframes lint` (DOM-level, post-build) | PARTIAL | MERGE into the plan schema | `fin-audit.md:53-56` and `fin-storyboard.md:49-51` are the same five rules |

### Phase 3 — voice

| # | Responsibility | Owner(s) | Implemented as | HF-native equivalent | Overlap | Verdict | Evidence |
|---|---|---|---|---|---|---|---|
| 10 | Slice VO lines from the script into `lines.json` | `fin-voice` | prompt | `NONE` | — | **DELETE → script** | `fin-voice.md:40-43` "Slice the source text exactly; never retype it" — a deterministic extraction. `tools/transcript.py` already performs the same join mechanically (`fin-package.md:154-156`) |
| 11 | Generate TTS clips, ffprobe, write `timing.json` | `tools/tts/batch.py` | script (already) | `hyperframes tts` (local Kokoro, 0.7.66+); `media-use` voiceover | PARTIAL — wrong voices | KEEP the script | `fin-voice.md:44-49`; voices are ElevenLabs Amrut/Brian per `format.json cuts.*.voice_id`, not Kokoro |
| 12 | Cost guard (refuse if audit≠PASS, or chars >1.3× budget) | `fin-voice` | prompt | `NONE` | — | **DELETE → assert** | `fin-voice.md:27-31` — two comparisons against files on disk |
| 13 | Write `gen_vo_<cut>.sh` | `fin-voice` | prompt | `NONE` | — | **DELETE → script** | `fin-voice.md:50-52` — writes a fixed 3-line file |

**`fin-voice` has no judgment step.** All four of its responsibilities are deterministic;
it exists to run one command it is not allowed to retry (`fin-voice.md:21-23`). 5 invocations
on the last run.

### Phase 4 — plan

| # | Responsibility | Owner(s) | Implemented as | HF-native equivalent | Overlap | Verdict | Evidence |
|---|---|---|---|---|---|---|---|
| 14 | Per-scene design assignment (`arch`/`ground`/`art`) | `fin-storyboard` | prompt | `NONE` (channel-specific archetypes) | NONE | KEEP | `fin-storyboard.md:52-79` |
| 15 | Scene→image query manifest | `fin-storyboard` | prompt → `manifest.json` | `NONE` | NONE | KEEP | `fin-storyboard.md:140` — already emits JSON |
| 16 | Transition + SFX + music-bed plan | `fin-storyboard` | prompt (prose columns) | `NONE` | NONE | KEEP, **as data** | `fin-storyboard.md:87-107` |
| 17 | **The storyboard artifact's format** | `fin-storyboard` | 100,294 B of prose | **`STORYBOARD.md` + `StoryboardManifest`** parser, `GET /api/projects/<id>/storyboard`, Studio storyboard board | **PARTIAL — real** | **SPLIT: data → `storyboard.json`, prose → ≤1 page** | `hyperframes-core/references/storyboard-format.md:1-10`; the current file is 100 KB and its own guard admits the apparatus "grew **3.1×** and from 17 sections to 41" (`fin-storyboard.md:20-28`) |
| 18 | Contact-sheet view of the plan | — (not done) | — | Studio storyboard board renders frames as a contact sheet | NONE (unused) | NEW, optional | `storyboard-format.md:6` |

### Phase 5 — assets

| # | Responsibility | Owner(s) | Implemented as | HF-native equivalent | Overlap | Verdict | Evidence |
|---|---|---|---|---|---|---|---|
| 19 | Fetch stock photos, contact sheets, full-res promote | `fin-assets` + `tools/stock/pixabay_fetch.py` | script + prompt | `media-use resolve --type image` → **HeyGen vector catalog, needs auth that is absent** | NONE | KEEP | `fin-assets.md:24-31`; `~/.claude/skills/media-use/SKILL.md`; no `~/.heygen/credentials` |
| 20 | **The sound-off image test (5 questions)** | `fin-assets` **AND** `fin-editor` | prompt ×2 | `NONE` | **FULL** | **MERGE — see §2** | `fin-assets.md:197-208` vs `fin-editor.md:59-73` — same five checks, same worked examples ("balanced scale under *thirty times apart*", "*the internet says* needs a screen", "Indian shopkeeper / Japan's national accounts", "demonetised ₹500") |
| 21 | md5 dedupe across projects | `fin-assets` + `pipeline_check` | prompt + script | `NONE` | PARTIAL | KEEP (script side) | `fin-assets.md:64-84` |
| 22 | Licence/attribution (CREDITS row per image) | `fin-assets` + `pipeline_check check assets` | prompt + script | `media-use` ledger (unreachable) | PARTIAL | KEEP script, drop prose | `fin-assets.md:242-255`; 35 uncredited images reached a master once |
| 23 | Lottie search / tint / library write-back | `fin-assets` + `tools/lottie/` | script + prompt | `hyperframes-animation` Lottie adapter (**runtime**, not sourcing) | NONE for sourcing | KEEP | `fin-assets.md:142-185` |

### Phase 6 — build

| # | Responsibility | Owner(s) | Implemented as | HF-native equivalent | Overlap | Verdict | Evidence |
|---|---|---|---|---|---|---|---|
| 24 | **Project scaffolding** | `fin-build` step 1 **AND** `tools/chapter_project.py` | prompt + script | `hyperframes init --non-interactive --example=blank` | **FULL, internal** | **DELETE the prompt copy** | `fin-build.md:29-35` describes copying `tools/scaffold/`; `chapter_project.py:5-8` already writes `index.html` + assets symlinks + `package.json` + `node_modules` symlink + `renders/`. For every MEDIUM/LONG run since 2026-08-04 the prompt's step 1 is dead |
| 25 | **Timing → HTML compilation** | `tools/chapter_project.py` | script (already) | `NONE` | — | KEEP | `chapter_project.py:20-30`: every timing attribute "lifted VERBATIM from the shipped index.html and only the START is rebased" |
| 26 | Design application (archetype, plate, ken, art-off) | `fin-build` | prompt | `NONE` — channel-specific | NONE | KEEP (this is the whole agent) | `fin-build.md:71-182` |
| 27 | Scene transitions + track alternation | `fin-build` | prompt | `hyperframes check` `overlapping_clips_same_track` catches the failure | PARTIAL (detect, not author) | KEEP | `fin-build.md:189-208` |
| 28 | Registry blocks / components | — (**never used**) | — | 109 blocks + 25 components. Direct overlaps: `parallax-zoom`/`parallax-unzoom` ≈ `motion.js` `ken`/`plateKen`; `grain-overlay` ≈ `assets/img/grain.png`; caption-* ≈ `transcript.py` output | PARTIAL | **DEFER — see §3** | `studio/registry/registry.json`; no `hyperframes.json` under `studio/videos/*` |
| 29 | Composition validation | `hyperframes check` **and** `pipeline_check check_build` | CLI + script | `hyperframes check` = lint + runtime + layout | **NONE — complementary** | KEEP BOTH | `check_build` asserts *timing coherence against `timing.json`* (root duration vs last scene end vs line count vs track alternation, `pipeline_check.py:689-780`); `hyperframes check` asserts *composition validity*. Neither subsumes the other. **This is a redundancy I expected to find and did not.** |
| 30 | Max-density snapshot pass | `fin-build` | prompt + `hyperframes snapshot` | `hyperframes snapshot` (the tool); `inspect` (layout across timeline) | PARTIAL | KEEP | `fin-build.md:235-251` |
| 31 | Audio cue list → `assets/audio.json` | `fin-build` | prompt | `NONE` | NONE | MOVE to plan (§4) | `fin-build.md:212-226` — transcribes the storyboard's SFX column; belongs in `storyboard.json` |

### Phase 7 — render

| # | Responsibility | Owner(s) | Implemented as | HF-native equivalent | Overlap | Verdict | Evidence |
|---|---|---|---|---|---|---|---|
| 32 | Draft render + contact sheet | `fin-render` step 0 | prompt wrapping 2 commands | `hyperframes render -q draft` | **FULL** | **DELETE → script** | `fin-render.md:29-44` is exactly two bash lines with no decision between them |
| 33 | Frame check "gate two" (look at frames) | `fin-render` step 1 | prompt (vision) | `NONE` | **PARTIAL with `fin-editor`** | MERGE-INTO(`fin-review`) | `fin-render.md:46-59` — a vision pass over one frame per scene, which `fin-editor` then repeats on a sheet of the same scenes (`fin-editor.md:30-40`) |
| 34 | The full encode | **orchestrator**, not an agent | prompt | `hyperframes render`; `cloud`/`lambda`/`cloudrun` unused | — | KEEP with orchestrator | `fin-render.md:70-77` — the agent is told it *cannot* do this: "a subagent's background task dies when the subagent returns (verified 2026-07-28)" |
| 35 | Render QA: VO drift, peak dBTP, blackdetect, runtime | `fin-render` step 3 | prompt wrapping measurements | `NONE` | — | **DELETE → script** | `fin-render.md:78-83` — four numeric thresholds, zero judgment. `pipeline_check` already owns part (`check_render`, `pipeline_check.py:807-813`) |
| 36 | Audio mix + loudnorm | orchestrator + `tools/audio/mix.py` + `tools/loudnorm.py` | script (already) | `media-use` audio engine (unreachable) | PARTIAL | KEEP | `finance-video.md:205-233` |

**`fin-render` is a bash script wearing an agent costume.** Of its four steps, one does nothing
by design (#34), two are pure measurement (#32, #35), and the fourth duplicates `fin-review`
(#33). 12 invocations on the last run.

### Phase 8 — review

| # | Responsibility | Owner(s) | Implemented as | HF-native equivalent | Overlap | Verdict | Evidence |
|---|---|---|---|---|---|---|---|
| 37 | Build + read the chapter contact sheet | `fin-editor` **AND** `fin-ceo` | prompt ×2, **identical command** | Studio storyboard board (plan frames, not encoded frames) | **FULL** | MERGE-INTO(`fin-review`) | `fin-editor.md:33` and `fin-ceo.md:31` are the same `python3 tools/chapter_sheet.py …` invocation on the same file |
| 38 | Correctness review (image truth, art honesty, craft) | `fin-editor` | prompt | `NONE` | — | KEEP as pass 1 of `fin-review` | `fin-editor.md:49-124` |
| 39 | Retention / brand / flatness review | `fin-ceo` | prompt | `NONE` | — | KEEP as pass 2 of `fin-review` | `fin-ceo.md:36-96` |
| 40 | **Figure traceability to `facts-staging.md`** | `fin-audit` **+** `fin-editor` **+** `fin-ceo` | prompt ×3 | `NONE` | **PARTIAL — three artifacts** | KEEP all three | `fin-audit.md:41` (the script), `fin-editor.md:109-113` (the drawn art generator), `fin-ceo.md:73` (the rendered frame). Three different artifacts; **this hypothesis is refuted** |
| 41 | Round-limit arbitration (3 editor, 2 CEO, then escalate) | orchestrator + both agents | prompt ×3 | `NONE` | PARTIAL | MERGE into one budget | `finance-video.md:261-264,302-305`, `fin-ceo.md:137-139` |
| 42 | Numbered cross-chapter review sheet for the creator | orchestrator + `tools/frames_sheet.py` | script | Studio board | PARTIAL | KEEP | `finance-video.md:273-283` |

### Phase 9 — package & close-out

| # | Responsibility | Owner(s) | Implemented as | HF-native equivalent | Overlap | Verdict | Evidence |
|---|---|---|---|---|---|---|---|
| 43 | Thumbnail design + legibility asserts | `fin-package` | prompt + HF project | `NONE` | NONE | KEEP | `fin-package.md:35-97` |
| 44 | AI-enhance prompt per thumbnail | `fin-package` | prompt | `NONE` | NONE | KEEP | `fin-package.md:99-131` |
| 45 | **Title/tag research** | `fin-package` **AND** orchestrator's vidIQ pass | prompt ×2 | `NONE` | **PARTIAL, and it loops** | SPLIT — one owner | `fin-package.md:133-138` researches titles; `finance-video.md:402-414` re-ranks them *after*, then says "**If a title changes here, re-run `fin-package`'s thumbnail section**" — a designed rework cycle |
| 46 | Captions (.srt + narration) | `tools/transcript.py`, called by `fin-package` **and** orchestrator | script, two call sites | `hyperframes transcribe`; `embedded-captions` skill (not installed) | PARTIAL | KEEP script, one call site | `fin-package.md:149-160` vs `finance-video.md:213` |
| 47 | Gate-2 compliance checklist | `fin-package` | prompt | `NONE` | NONE | KEEP | `fin-package.md:164-172` |
| 48 | Milestone note + `vault/index.md` line | `fin-archive` | prompt | `NONE` | NONE | **DELETE → script** | `fin-archive.md:21-36` is a template fill plus an append; it loads 78,586 B (incl. `vault/index.md` 39,798 + `money-facts` 19,972 + `best-practices` 11,846) and is **forbidden to write two of those three** (`fin-archive.md:39-47`) |
| 49 | Fact promotion staging→knowledge | orchestrator | prompt | `NONE` | NONE | KEEP → script | `finance-video.md:397-400` |
| 50 | Source archival + studio delete | `tools/archive_cut.py` | script (already) | `NONE` | — | KEEP | `vault/CLAUDE.md` finished-video rule |

### Cross-cutting

| # | Responsibility | Owner(s) | Implemented as | HF-native equivalent | Overlap | Verdict | Evidence |
|---|---|---|---|---|---|---|---|
| 51 | Run state | `pipeline_check mark` → `run.json` | script | `NONE` | — | KEEP | — |
| 52 | **Run narrative / decisions / incidents** | `notes.md` | freeform prose | `NONE` | — | **NEW: structured journal (Phase 6)** | 157,996 B, **322 headings**, families `owed.*` (13), `tool_fixes_this_session.*` (6), `incidents.*` (3), `rulings_binding_on_both_cuts.*` (4) |
| 53 | Token accounting | **nothing** | — | `hyperframes telemetry` (render telemetry only) | — | **NEW (Phase 5)** | no `runs/`, no `metrics.json` anywhere |
| 54 | Stage gate for `editor`/`ceo`/`archive` | **nothing** | — | — | — | **NEW** | `pipeline_check` knows 10 stages; these three are absent, contradicting `finance-video.md:13-14` |
| 55 | Agent I/O envelope | 4-line text return | prompt, 11× restated | — | FULL | MERGE into one shared contract | identical block in 11 agent files |
| 56 | Log format (Ran·Failed·Evidence·Changed·Owed) | 11 agents | prompt, 11× restated | — | FULL | MERGE into one shared contract | identical block in 11 agent files |

---

## 2 · The finding that matters most

**Responsibility #20 — the sound-off image test is written twice, in full, and runs at two
different times.**

`fin-assets.md:197-208` and `fin-editor.md:59-73` contain the same five questions with the
same worked examples. `fin-assets` applies them at **fetch time, on a 6-cell contact-sheet
preview**. `fin-editor` applies them at **review time, on a 3-minute draft render**.

Why the first pass under-catches, in the pipeline's own words:

- `fin-assets.md:237-240` — "⚠ **The contact sheet is lossy.** It renders only a trailing
  subset when any preview fails, with no warning — sheets have shipped showing 4 of 12 cells."
- `fin-assets.md:94-102` — "**Read every promoted candidate at FULL RESOLUTION before
  accepting it.** A contact-sheet thumbnail hides exactly the thing that kills a cut: legible
  text… euro/złoty coins on the ₹ hook, '1 ZŁOTY'… all invisible at grid size."
- `fin-assets.md:7-8` — "Image rejection is **the top defect source on record**."

**The cost of catching it late.** One image defect found by `fin-editor` costs: re-fetch
(`fin-assets`) → rebuild (`fin-build`) → re-draft (`fin-render`) → re-review (`fin-editor`)
= **4 invocations plus a ~3-minute render**. Caught at asset time it costs **1**.

The last run's shape is consistent with this: `fin-assets` 23 + `fin-build` 19 +
`fin-render` 12 + `fin-editor` 16 = **70 invocations for 4 locked chapters**.

**The fix is not "delete one reviewer."** It is to run the test **once, on the artifact that
can actually carry it**: a contact sheet built from the **promoted full-resolution jpgs**,
before `fin-build` runs. That is a ~30-line variant of `tools/chapter_sheet.py`, which today
requires an encoded mp4 (`chapter_sheet.py:126,137-141`).

⚠️ **Precision, because the existing tool's docstring earns it:** the post-render sheet does
**not** go away. `chapter_sheet.py:18-22` documents that "Lottie scenes have two failure modes
… that render a silent blank and pass every static check; only the encoded file proves what a
viewer will see." A jpg sheet catches the *image-selection* subset — repetition, wrong
currency, subject absent, picture argues with the line. It cannot catch a blank Lottie. So:
**image acceptance moves early and becomes terminal there; the post-render sheet stays, once,
and stops being the place image choices are litigated.**

---

## 3 · The five hypotheses, answered

| # | Hypothesis | Verdict | Why |
|---|---|---|---|
| 1 | `fin-build` re-implements scaffolding that `hyperframes init` + catalog blocks provide | **PARTIALLY CONFIRMED — and the real duplication is internal, not native** | `hyperframes init` would replace `package.json` + runtime only; it cannot supply `blockframe.css`, the channel's locked design system. But `tools/chapter_project.py` **already does the whole scaffold** for chapter projects (`chapter_project.py:5-8`), so `fin-build.md:29-35` is dead prose on every MEDIUM/LONG run since 2026-08-04. **Registry blocks: DEFER, not delegate** — `parallax-zoom` and `grain-overlay` genuinely overlap `motion.js`/`grain.png`, but swapping a load-bearing motion helper mid-baseline is exactly the change Phase 5 forbids until there is a baseline. |
| 2 | `fin-render` wraps what the CLI does natively, adding only failure modes | **CONFIRMED** | Step 0 = two bash lines. Step 2 = the agent is told it cannot run the encode (`fin-render.md:70-77`). Step 3 = four numeric thresholds. Only step 1 is judgment, and it duplicates `fin-editor`. It is the definition of a wrapper. |
| 3 | `fin-editor` does post-hoc editing that should be corrected upstream | **REFUTED as written; CONFIRMED in substance** | `fin-editor.md:9` — "You do not edit anything yourself — you are the eyes." It is a reviewer, not an editor. **But** its largest check-block is the image sound-off test, which *should* be enforced upstream at `fin-assets` — §2. |
| 4 | `fin-audit`, `fin-ceo`, `fin-facts` are three overlapping review passes | **REFUTED** | `fin-facts` is a producer, not a reviewer (`fin-facts.md:32-36`). `fin-audit` reviews the **script** before any spend and independently re-fetches sources — a thing no downstream reviewer does (`fin-audit.md:32-38`). `fin-ceo` reviews a **rendered chapter**. Three artifacts, three times, one of them pre-spend. **The real triple is `fin-editor` + `fin-ceo` + `fin-render` step 1**, which all look at frames of the same chapter. |
| 5 | `fin-storyboard` produces an artifact that is discarded or re-derived | **PARTIALLY CONFIRMED** | Not discarded — four agents read it. But it is **100,294 B of prose carrying maybe 6 columns of data**, its own guard admits the apparatus grew 3.1× to 41 sections (`fin-storyboard.md:20-28`), one column is already extracted to JSON (`manifest.json`, `fin-storyboard.md:140`), and HyperFrames has a native parsed plan format nobody uses (`storyboard-format.md`). |
| 6 | `fin-archive` + `fin-package` are one responsibility split in two | **REFUTED as stated; a different defect found** | They are genuinely different jobs (make publish assets vs. write the vault record). The defect is that **`fin-archive` is not agent-shaped at all**: a template fill + an index append, on `haiku`, loading 78,586 B of which it is forbidden to write 71,616 B (`fin-archive.md:39-47`). |

---

## 4 · Proposed Roster

**13 → 8.** Every agent below states the one failure it prevents that no other agent can.

| Agent | One job | Failure it prevents | Model tier |
|---|---|---|---|
| `fin-evidence` | Study competitors **and** source every figure to ≥2 independent sources | An unsourced number entering the pipeline at all | frontier |
| `fin-script` | Write the VO script to the budget | — (the generative step) | frontier |
| `fin-audit` | Adversarially re-fetch every source and try to break the script, **before any spend** | A fabricated or unsupported figure surviving to TTS. Must not be the author — `fin-audit.md:42-45` | frontier |
| `fin-plan` | Assign per-scene design + image query + transition + SFX, emitted as **`storyboard.json` + ≤1 page of prose** | `fin-build` inventing a layout (`finance-video.md:329-331`) | frontier |
| `fin-assets` | Source images **and terminally accept them** against the sound-off test at full resolution | The top defect source on record (`fin-assets.md:7-8`) | frontier (vision) |
| `fin-build` | Apply the plan's design to the composition | A composition that renders wrong or drifts from the design system | frontier |
| `fin-review` | One gated review per chapter: **pass 1 correctness, pass 2 retention** — one sheet read, one findings table, one round budget | Shipping a chapter that is wrong (pass 1) or boring (pass 2) | frontier |
| `fin-package` | Thumbnail + publish pack + Gate-2 compliance | An unshippable or non-compliant upload | frontier |

**Not on the list, deliberately:** no `fin-retro` yet. Phase 6 defines it; adding it now
would violate "do not add an agent unless you name the failure mode it prevents" — it prevents
nothing until there are journals to read, and there are none.

---

## 5 · Kill List

| Removed | Absorbed by | Justification |
|---|---|---|
| **`fin-research`** | `fin-evidence` (merge) | Identical toolset, identical untrusted-input rule (`fin-research.md:31-35` ≡ `fin-facts.md:26-30`), identical "never invent a number", both once-per-run, strictly sequential (`finance-video.md:157-158`). 3 of 98 invocations combined — **this merge is cosmetic and is labelled as such.** |
| **`fin-facts`** | `fin-evidence` (merge) | As above. The one-write rule (`fin-facts.md:32-36`) is preserved verbatim in the merged agent — it is the anti-self-grading guarantee. |
| **`fin-voice`** | `tools/tts/prepare.py` (new, ~40 lines) + one `pipeline_check` assert | All four responsibilities are deterministic: slice lines (#10), run `batch.py` (#11, already a script), cost guard (#12, two file comparisons), write `gen_vo.sh` (#13, a fixed 3-line file). No judgment step exists. `tools/transcript.py` already performs the same slice-never-retype join mechanically. **5 invocations removed.** |
| **`fin-render`** | `tools/render_chapter.py` (draft + sheet) + `pipeline_check check render` (extended) + `fin-review` (the frame look) | Step 0 = 2 bash lines (`fin-render.md:29-44`); step 2 = explicitly cannot run (`fin-render.md:70-77`); step 3 = 4 numeric thresholds (`fin-render.md:78-83`); step 1 duplicates `fin-editor.md:30-40`. **12 invocations removed.** |
| **`fin-editor`** | `fin-review` pass 1 | Same sheet, same command as `fin-ceo` (`fin-editor.md:33` ≡ `fin-ceo.md:31`), same inputs, same findings-table shape, same chapter gate. `fin-ceo.md:133` already carries the instruction "Do not re-litigate the editor's job" — a rule that exists because the overlap is real and known. |
| **`fin-ceo`** | `fin-review` pass 2 | As above. Merging makes the round budget one number instead of two (3 + 2 = up to 5 rework cycles today, `finance-video.md:261-264`). |
| **`fin-archive`** | `tools/close_out.py` (new) | Template fill + index append (`fin-archive.md:21-36`). Loads 78,586 B, forbidden to write 71,616 B of it. **0 invocations on the last run — it has never run on the current pipeline shape.** |

**Net: 7 definitions removed, 2 created (`fin-evidence`, `fin-review`) → 13 → 8.**

Applied to the last run's 98 invocations, the removals alone eliminate
`fin-voice` (5) + `fin-render` (12) + `fin-ceo` (6) = **23**, before any effect from moving
the image gate. Projections beyond that arithmetic wait for the Phase 5 baseline.

---

## 6 · Deferred, with reasons

| Deferred | Why not now |
|---|---|
| Registry blocks (`parallax-zoom`, `grain-overlay`, caption components) | Real overlap with `motion.js` and `grain.png`, but swapping a load-bearing motion helper before a baseline exists breaks the measurement Phase 5 depends on. Revisit after baseline. |
| `hyperframes init` for scaffolding | The internal duplicate (`chapter_project.py`) must go first; `init` cannot supply `blockframe.css` and would change only `package.json` + runtime. |
| `faceless-explainer` / `general-video` workflow skills | Not installed; `faceless-explainer` is capped at ~3 min and forbids photographs (`SKILL.md:8`) — the opposite of this channel's hardest rule. `general-video` is the nominally correct route for 8.5 min but is also uninstalled and unevaluated. |
| `media-use`, `hyperframes cloud`/`lambda`/`cloudrun`, `hyperframes tts` | All need HeyGen auth; `~/.heygen/credentials` does not exist. `media-use`'s image search returns vectors, not photographs. |
| HyperFrames MCP | Unauthorized per your answer #1. Every row treats it as UNVERIFIED. |
| Upgrading 0.7.66 → 0.7.102 | Not during the baseline run. Scheduled as a post-baseline migration step in Phase 2. |

---

*Phase 1 complete. Nothing outside `audit/` was modified.*
