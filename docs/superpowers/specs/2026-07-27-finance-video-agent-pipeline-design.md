<!-- /autoplan restore point: ~/.gstack/projects/YoutubeScraper/audit-2026-07-17-autoplan-restore-20260728-000040.md -->

# Finance-video agent pipeline — design

**Date:** 2026-07-27
**Status:** approved by creator, ready for implementation planning
**Goal:** `/finance-video "topic"` → four intake questions → a rendered Hindi/₹ video
and a rendered US-English/$ video, each with a thumbnail and a researched publish
pack, with no further human input.

---

## 1. Why this shape

Three finance videos have shipped (`50-30-20-rule`, `emergency-fund`,
`needs-vs-wants`), each as a ₹/$ pair. The pipeline that produced them is real and
repeatable — it is simply executed by hand today:

```
topic → competitor study → sourced numbers → script (char-budgeted)
     → per-segment TTS → ffprobe durations → storyboard (scene DOM + cue table)
     → stock images (each eyeballed) → HyperFrames index.html → npm run check
     → render → re-transcribe QA → thumbnail → youtube-metadata note → vault note
```

Those stages have distinct tool needs, distinct reference knowledge, and large
intermediate artifacts, and collapse into eleven agent roles. That is the
textbook case for subagents: each runs in its
own context window, reads artifacts off disk, and returns a short summary
([Anthropic, building effective agents](https://www.anthropic.com/research/building-effective-agents);
[effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).

**Load-bearing constraint:** the orchestrator must never hold a script, a
composition, or an image in context. It holds intake answers, `run.json`, and one
summary per stage. Everything else lives on disk. A 12-stage run that passes full
artifacts through the parent will rot before it reaches the English cut.

### Creator decisions (2026-07-27)

| Decision | Choice |
|---|---|
| Scope of one run | Through rendered MP4 + thumbnail + publish pack. No upload. |
| Human gates | **None.** Fully autonomous after intake. |
| Research grounding | Local competitor study (`backend/study.py`) **and** web fact-sourcing. |
| Surface | `.claude/agents/*.md` + `.claude/commands/finance-video.md`. |
| Cuts | Always both, sequentially: Hindi/₹ complete, then US-English/$. |
| Thumbnails | In-pipeline (`fin-package`), not manual Canva. |

**Consequence of "no human gates":** the two natural checkpoints are replaced by
automated ones, placed immediately before the two irreversible spends —
`fin-audit` before ElevenLabs credits, and a frame-check inside `fin-render`
before an ~18-minute encode.

---

## 2. Flow

```
/finance-video "topic"
├─ intake — 4 questions, written to run.json
├─ Phase 1  fin-research  ∥  fin-facts          (the only parallel step)
├─ Phase 2  HINDI CUT
│    fin-script → fin-audit → fin-voice → fin-storyboard
│    → fin-assets → fin-build → fin-render → fin-package
├─ Phase 3  US CUT — the same eight, reusing Phase 1 output
└─ Phase 4  fin-archive
```

Phase 1 is parallel because the two agents share no state. Everything after is a
true dependency chain (durations gate the storyboard; the storyboard gates the
image queries; images gate the build) and is run sequentially so a failure is
readable.

### Intake

1. **Topic** (from the command argument; confirmed back).
2. **Target length** — default `2:45`. Shipped range is 2:24–2:58.
3. **Hook angle** — optional. Blank means `fin-research` chooses from what won.
4. **Fresh numbers?** — yes / no. "No" lets `fin-facts` verify-only against
   `money-facts-2026` and `subscription-economics-2026` instead of sourcing new.

Length → char budget: **Hindi ≈ 12.0–12.2 chars/s**, **English ≈ 15 chars/s**
(both measured, `workflows/voiceover-tts.md` and `niches/india-finance-market.md`).
2:45 ⇒ ~2,000 Hindi chars / ~2,475 English chars.

### Slug

`<kebab-topic>`, e.g. `credit-card-minimum-payment`. Derived at intake, confirmed
in the run header, used for every path below.

---

## 3. Files — the handoff medium

```
vault/videos/<slug>/
  run.json                    ← orchestrator state (intake + per-stage status)
  script-hi.md   script-en.md
  audit-hi.md    audit-en.md
  storyboard-hi.md  storyboard-en.md
  youtube-metadata-hi.md  youtube-metadata-en.md
  index.md                    ← milestone note (fin-archive)

vault/knowledge/video-studies/<slug>.md       ← fin-research
vault/knowledge/money-facts-2026.md           ← fin-facts appends

studio/videos/<slug>-hi/  and  <slug>-en/
  assets/voice/{h1..h9}.mp3, lines.json, timing.json
  assets/img/s*.jpg, manifest.json, CREDITS.txt, grain.png
  index.html, package.json, meta.json
  snapshots/, renders/FINAL-1080p-<cut>.mp4

studio/videos/<slug>-thumbs/                  ← one HTML, two sections
  thumbnail-hi.png, thumbnail-en.png
```

`run.json` — deliberately minimal:

```json
{
  "slug": "…", "topic": "…", "target_seconds": 165,
  "hook_angle": null, "fresh_numbers": true,
  "started": "2026-07-27",
  "stages": { "fin-research": "done", "fin-facts": "done",
              "fin-script-hi": "done", "fin-audit-hi": "failed:1", … }
}
```

Its only job is resume: a crashed run restarts at the first non-`done` stage
instead of re-spending TTS credits.

---

## 4. The eleven agents

Each is a `.claude/agents/fin-*.md` file: frontmatter (`name`, `description`,
`tools`), then the role prompt. Universal rules in every one:

- Read `vault/CLAUDE.md` first. One home per fact — numbers in `library.db`,
  everything else in the vault, never duplicated.
- Return **≤20 lines** to the orchestrator. Findings go in files, not the reply.
- Never invent a number. If it isn't in a sourced vault line, it doesn't ship.
- On failure, say what failed and why in one line. Don't paper over it.

### 1. `fin-research` — competitor study
- **Tools:** Bash, Read, Grep, Glob, Write
- **Reads:** `vault/workflows/video-study.md`, `library.db`
- **Does:** `venv/bin/python backend/study.py "<topic query>"` → reads
  TOP/MID/LOW transcripts and keyframes → hook type and when the payoff promise
  lands, beat map with timestamps, views/sub ratio per video, and a concrete
  low-performer autopsy (never just "low views").
- **Writes:** `vault/knowledge/video-studies/<slug>.md` (per `templates/video-study`)
- **Returns:** winning hook type, the beat map in ≤6 lines, the one trap to avoid
- **Fails when:** the library has no comparable videos → says so and asks the
  orchestrator to record a scrape as owed; the run continues on vault knowledge.

### 2. `fin-facts` — money-number sourcing
- **Tools:** WebSearch, WebFetch, Read, Edit, Write
- **Reads:** `knowledge/money-facts-2026`, `knowledge/subscription-economics-2026`
- **Does:** sources every ₹ and $ figure the topic needs — ≥2 independent
  sources for any money claim, official/primary preferred (PLFS, RBI, Fed SHED,
  published price cards). Tags **HARD** (primary, verifiable) vs **SOFT**
  (survey, single source) and explicitly names the blog-tier numbers *not* to
  use. Converts nothing between markets — the ₹ set and the $ set are sourced
  independently.
- **Writes:** appends dated, sourced lines to `knowledge/money-facts-2026.md`
- **Returns:** the hero number for each market + its source line
- **Precedent:** the needs-vs-wants brief's `5 × ₹800 = ₹48,000/yr` did not
  survive real Indian price cards; the bottom-up ₹2,047/mo stack replaced it.
  This agent exists to catch that class of error before scripting, not after.

### 3. `fin-script` — the writer (runs per cut)
- **Tools:** Read, Write, Grep, Glob
- **Reads:** ①②, `skills/long_form_scripting`, `templates/script-template`,
  and per cut: `haryanvi-hindi-script-style` + `niches/india-finance-market`
  (hi) or `us-english-script-style` (en)
- **Does:** 9 segments to the char budget, in the proven shape —
  hook · roadmap · concept · rule · audit · action · the math · do-this-today ·
  recap+CTA. VO paragraphs only in the VO block; on-screen text stays
  English/Hinglish in both cuts. Digits **spelled out** in VO text (Latin digits
  are a coin-flip English reading in ElevenLabs); on-screen numerals carry the
  exact figures. Includes the per-scene timing budget table.
- **The `-en` rule, stated explicitly in the agent prompt:** the English cut is a
  **US rewrite, not a translation** — $ amounts, US institutions (HYSA, FDIC,
  22% APR card), US shocks, US b-roll. It reads the Hindi script only for
  structure. Shipping rupees in a `-en` cut is a hard failure.
- **Writes:** `vault/videos/<slug>/script-<cut>.md`
- **Returns:** segment count, total chars, estimated runtime vs target

### 4. `fin-audit` — adversarial check (runs per cut)
- **Tools:** Read, Edit, Grep, WebSearch
- **Does:** tries to **break** the script, not approve it.
  - Every number traced to a sourced line in `money-facts-2026` /
    `subscription-economics-2026` — untraceable ⇒ cut or replaced.
  - Char total within ±10% of budget.
  - Hook payoff promise lands inside 15s.
  - No product or platform recommended (names appear only as price evidence).
  - Currency purity: no ₹ in `-en`, no $ in `-hi`.
  - No cite refs like `(28:4)` and no bare Latin digits left in VO text — both
    are known silent TTS failures.
- **Authority:** may edit the script directly to fix a violation. Rewrites are
  logged.
- **Writes:** `vault/videos/<slug>/audit-<cut>.md`
- **Returns:** PASS/FAIL + what it killed or rewrote
- **This is gate one.** FAIL twice ⇒ run stops before any TTS spend.

### 5. `fin-voice` — TTS + timing (runs per cut)
- **Tools:** Bash, Read, Write
- **Does:** extracts VO paragraphs to
  `assets/voice/lines.json` `{h1..h9}` (no markdown, no on-screen text) → one
  clip per segment via `tools/tts/elevenlabs_tts.py` → `ffprobe` each →
  `timing.json` with per-segment duration and cumulative start.
- **Voices (locked):** Hindi **Harsh** `HTUuC7OeeEt6OL5fViVe`; US **Brian**
  `nPczCjzI2devNBz1zQrb`. ElevenLabs defaults, style 0.
- **Cost guard:** refuses to run if `fin-audit` did not PASS, or if the script
  exceeds 1.3× budget.
- **Writes:** `assets/voice/*.mp3`, `timing.json`, a per-cut `gen_vo_<cut>.sh`
  that regenerates everything (a fresh one per cut — the existing
  `gen_vo*.sh` scripts hard-`cd` into their own project and must not be reused).
- **Returns:** measured total runtime vs target, per-segment drift

### 6. `fin-storyboard` — scene spec (runs per cut)
- **Tools:** Read, Write, Grep
- **Reads:** script, `timing.json`, `knowledge/design-techtooltester`,
  `templates/storyboard-template`, `skills/hyperframes_production`
- **Does:** every VO line → scene DOM, element IDs, GSAP cue table with real
  start times from `timing.json`, and an image slot per scene with its search
  query. Carries the design system's colour semantics (wants = amber; red is
  only ever the leak) and the "densest scene gets the calmest background" rule.
- **On the `-en` pass:** ports the skeleton and element IDs from
  `storyboard-hi.md` so fixes travel between cuts; only deliberately divergent
  scenes get new IDs, and the divergence is noted.
- **Writes:** `vault/videos/<slug>/storyboard-<cut>.md` + `assets/img/manifest.json`
- **Returns:** scene count, image slot count, which scenes are photo-free

### 7. `fin-assets` — stock images (runs per cut)
- **Tools:** Bash, Read, Write, Edit
- **Reads:** `knowledge/stock-photo-sourcing`
- **Does:** `python3 tools/stock/pixabay_fetch.py --manifest …`, then **looks at
  every image** and rejects on the measured trap list:
  - demonetised pre-2016 ₹500 notes (current series is stone grey)
  - dollars answering a ₹ query (and vice versa)
  - readable brand marks — payment terminals, cards, logos
  - **never a phone-screen photo as a background** — it is someone else's brand
    and the brightest thing in frame (this shipped twice undetected)
  - chart direction contradicting the VO line
  - faces on dense scenes — hands and objects don't fight typography
- **Retry knob:** `--query "…#3"` takes the 3rd result. India-with-people queries
  run ~20% first-try usable; object-led queries ~80–90%. Prefer the object that
  carries the signal over a literal depiction.
- **Authority:** may **drop a cut-in rather than fake it**. Single-photo scenes
  read fine. Notes any near-black texture needing a per-scene `filter:` override.
- **Writes:** `assets/img/s*.jpg`, `CREDITS.txt`
- **Returns:** accepted / rejected counts, what it dropped and why

### 8. `fin-build` — the composition (runs per cut)
- **Tools:** Read, Write, Edit, Bash, Glob
- **Reads:** storyboard, `timing.json`, `skills/hyperframes_production`,
  `studio/videos/needs-vs-wants/index.html` as the reference implementation
- **Does:** scaffolds `studio/videos/<slug>-<cut>/` (package.json pinning the
  same `hyperframes@0.7.66`, meta.json), writes `index.html` with
  `data-start`/`data-duration` taken from `timing.json`, every timed element
  carrying `class="clip"` and `data-track-index`, timelines paused and registered
  on `window.__timelines`, no `Date.now()` / `Math.random()` / network fetches.
  Runs `npm run check` and fixes until clean.
- **Returns:** check result, total composition duration

### 9. `fin-render` — render + QA (runs per cut)
- **Tools:** Bash, Read, Glob
- **Does, in order:**
  1. **Gate two:** `snapshot --at` five frames spread across the timeline and
     *look at them* — layout, contrast, brand marks, wrong-currency imagery.
     Anything wrong goes back to `fin-build` (one retry) before encoding.
  2. `npm run render -- -q high --resolution 1080p --video-bitrate 12M`
     with `PRODUCER_ENABLE_CHUNKED_ENCODE=true`.
  3. QA the master: re-transcribe with faster-whisper and diff placement against
     the `data-start` table (target ≤0.1s), check peak dBTP (must sit below
     −1 dBTP), check for black segments, confirm runtime vs target.
- **Writes:** `renders/FINAL-1080p-<cut>.mp4`, `snapshots/`
- **Returns:** runtime, max drift, peak dBTP, pass/fail

### 10. `fin-package` — thumbnail + publish pack (runs per cut)
- **Tools:** Bash, Read, Write, Grep, WebSearch
- **Does:**
  - **Thumbnail** — a `studio/videos/<slug>-thumbs/` HyperFrames project, one
    HTML with a section per cut, exported via `snapshot --at` → PNG. Text is the
    cut's own language rule; energy over subtlety.
  - **Publish pack** — title options researched from YouTube autocomplete plus a
    competitor scoreboard scraped into `library.db`; description with **real**
    chapter timestamps read from the render; on-screen source citations; a
    verified-autocomplete tag list.
  - **Hard rule:** the Hindi pack and the English pack are researched
    independently — the demand clusters are entirely different search strings.
    Hindi/Urdu cuts get **Roman-script** titles so non-script-readers can read
    them; `-en` stays English.
- **Writes:** `youtube-metadata-<cut>.md`, `thumbnail-<cut>.png`
- **Returns:** recommended title, thumbnail path

### 11. `fin-archive` — the vault close-out (runs once)
- **Tools:** Read, Write, Edit, Glob
- **Does:** writes the milestone note (both cuts, runtimes, voices, hero numbers,
  state, what's owed), adds one line per new note to `vault/index.md`, and
  appends transferable findings as dated evidence lines to
  `knowledge/best-practices.md`. Flags anything confirmed by ~3 studies as ready
  for promotion into a skill.
- **Does NOT** delete renders — post-delivery cleanup runs only after upload,
  on the creator's word.
- **Writes:** `vault/videos/<slug>/index.md`, edits to `index.md` and
  `best-practices.md`
- **Returns:** done + what it flagged as owed

---

## 5. Failure policy

Autonomous means failures must be loud and cheap.

- Every stage retries **once**, with the failure text appended to its prompt.
- A second failure **stops the run**, writes `failed:<reason>` into `run.json`,
  and reports which stage and why. No silent continuation.
- Resume is `/finance-video --resume <slug>`: reads `run.json`, restarts at the
  first non-`done` stage. Completed TTS and images are never regenerated.
- Two agents may self-correct instead of failing: `fin-audit` rewrites offending
  script lines, `fin-assets` drops an unfindable image.
- Two agents are hard gates and their FAIL is terminal for the cut:
  `fin-audit` (before credits) and `fin-render`'s frame check (before encode).

---

## 6. Out of scope

- **Topic selection.** Gate 0 / Gate 1 stay with the creator.
- **Upload.** No YouTube Data API. The pack is written; publishing is manual.
- **Parallel fan-out beyond Phase 1.** The chain is genuinely sequential;
  pipelining it would only make failures harder to read.
- **A new scraper.** `backend/study.py` and `library.db` are the research engine.
- **Post-delivery cleanup.** Separate, creator-triggered, already specified in
  `vault/CLAUDE.md`.

---

## 7. Known risks

| Risk | Mitigation |
|---|---|
| Unattended run ships a wrong hero number | `fin-audit` traces every number to a sourced line before any spend |
| Unattended run burns an 18-min encode on a broken layout | `fin-render` reviews 5 frames before encoding |
| `-en` cut ships as a translation | Explicit rule in `fin-script`'s prompt + a currency-purity check in `fin-audit` |
| Stock photo carries a brand mark | `fin-assets` views every image; the phone-screen ban is absolute |
| ElevenLabs read has a mispronunciation no check catches | Accepted. Proof-listen stays a human step, recorded as owed in the milestone note |
| Pixabay has nothing usable for an India-with-people scene | `fin-assets` drops the cut-in; object-led sourcing is the default, not the fallback |

---

## 8. Success criteria

A run of `/finance-video "<a topic already shipped>"` produces artifacts that a
side-by-side comparison against the corresponding shipped pair judges equivalent
in: number sourcing, script structure, runtime accuracy vs budget, image
cleanliness, render QA numbers, and publish-pack research depth — with no human
input after the four intake questions.

---

# CEO REVIEW — Phase 1 (Step 0), 2026-07-28

Run via `/autoplan`. Dual voices: Claude subagent + Codex, both independent,
both adversarial. 6/6 consensus dimensions CONFIRMED against the plan.

## 0A. Premise challenge

The plan rests on five premises. Four are assumed, not stated, and three are
contradicted by evidence already in this repo.

| # | Premise (implicit) | Verdict | Evidence |
|---|---|---|---|
| P1 | Production speed is the bottleneck | **PARTLY REFUTED** | Five cuts were built by hand in one day (2026-07-27), so production already outruns everything else. But all six are now uploaded + scheduled, so the distribution queue the reviewers flagged is clear. The open bottleneck is cadence, not throughput-per-video. |
| P2 | The six uploads prove the format works | **STILL UNPROVEN** | Scheduled, not yet published. Zero views, zero CTR, zero AVD. `templates/video-study.md`'s CTR/AVD/AVP columns for our own uploads remain empty. First real data arrives ~28 days after the earliest publish date. |
| P3 | A channel exists to publish to | **UPHELD (2026-07-28)** | Creator supplied two live finance channels: **@cashguruguides** (₹/Hindi) and **@moneymavens101** ($/US), 3 uploads each, all scheduled. Neither was recorded in `knowledge/channels.md` — now added. Both reviewers were working from an incomplete vault. |
| P4 | The finance niche cleared Gate 0/1 | **REFUTED** | `niches/india-finance-market.md` records a creator pivot, not a gate pass. `youtube_channel_skill.md` §0.5: "Do not skip a gate." |
| P5 | Policy risk is not material | **REFUTED** | `niches/us-market-2026.md:75`, dated six days before this spec: AI expert personas in finance are ineligible for monetisation regardless of added value. Enforcement is channel-level. |

**Creator context supplied 2026-07-28** closed the P3 gap and softened P1. P2, P4 and P5 stand unchanged.

Additional defect, self-caught: the plan makes `faster-whisper` a render-QA gate
(`fin-render` step 3). It is **not installed** in this repo's venv.

## 0B. Existing code leverage

| Sub-problem | Already exists | Plan reuses it? |
|---|---|---|
| Competitor study | `backend/study.py` + `library.db` (552 videos) | Yes — `fin-research` wraps it |
| TTS + timing | `tools/tts/elevenlabs_tts.py`, per-cut `gen_vo_*.sh` | Yes |
| Stock sourcing | `tools/stock/pixabay_fetch.py` + manifest mode | Yes |
| Composition + render | `studio/videos/needs-vs-wants` as reference impl | Yes |
| Written runbook | `PRODUCTION_RUNBOOK.md` (352 lines) | **No — never mentioned.** This is the zero-code version of the plan and it already exists. |
| Publish + analytics ingestion | **Nothing** | Out of scope — and it is the actual blocked stage |

## 0C. Dream state

```
  CURRENT STATE              THIS PLAN                12-MONTH IDEAL
  6 finance cuts     --->    the same 6 cuts,   ---> a channel where each upload's
  rendered, 0        --->    produced faster,   ---> CTR/AVD decides the next topic,
  uploaded, 0 data   --->    still 0 data       ---> and production is the cheap part
```
Delta: the plan moves throughput, not knowledge. It leaves the 12-month ideal
exactly as far away as it is today, and adds eleven prompt files to migrate when
real data arrives.

## 0C-bis. Implementation alternatives (mandatory)

```
APPROACH A: Distribution-first — publish, measure, then automate
  Summary: Upload the 6 finished cuts, add a weekly Studio-metrics pull into
           library.db, wait 30 days, then build agents against real CTR/AVD.
  Effort:  S (human ~1 day / CC ~1h)     Risk: Low
  Pros:    Unblocks the actual queue; produces the data every later decision
           needs; costs almost nothing; the vault's compounding loop starts working
  Cons:    30-day wait before any pipeline work; feels like doing less
  Reuses:  library.db, the existing publish packs (already written for 4 cuts)

APPROACH B: Runbook + two scripts (the lazy automation)
  Summary: Write the finance-format runbook (the gap AUDIT.md already filed),
           then script only the two stages that are slow AND mechanical:
           voice (TTS + ffprobe + timing.json) and render-QA (render + whisper
           diff + dBTP). No agents. Judgment stays human.
  Effort:  M (human ~2 days / CC ~2h)    Risk: Low
  Pros:    Captures most of the wall-clock win; nothing to migrate when the
           format changes; the judgment layers that are the actual moat stay supervised
  Cons:    Script/storyboard/build stay manual — the slowest creative stages
  Reuses:  PRODUCTION_RUNBOOK.md pattern, gen_vo_*.sh, existing render flow

APPROACH C: The eleven-agent pipeline as specified (the ideal architecture)
  Summary: Full autonomous topic-to-render, both cuts, as written above.
  Effort:  L (human ~1 week / CC ~4h)    Risk: High
  Pros:    Highest ceiling if the format is proven and the channel survives policy;
           the file-handoff design is sound and would scale to other niches
  Cons:    Encodes an unvalidated format into 11 prompt files; no channel to
           publish to; no Gate 2; automates the moat (judgment) rather than the
           mechanics; doubles output of exactly the pattern under channel-level
           enforcement
  Reuses:  everything in 0B except the runbook
```

**RECOMMENDATION: A, then B, then re-decide on C.** Maps to the engineering
preference "right-sized diff" and to the project's own money-first rule: nothing
in C is wrong on the merits, but every hour of it is spent before the cheapest
question ("do these videos work?") has been asked.

## 0D. Scope analysis (SELECTIVE EXPANSION)

Minimum set of changes that achieves the stated goal ("give me a topic, get a
video"): a runbook plus the voice and render-QA scripts (Approach B). Everything
else in the spec is defensible only after the format is validated.

Expansion candidates surfaced, not yet accepted:
1. **Gate 2 compliance agent** — disclosure line, no-expertise framing, and a
   channel-level sameness check across the last five uploads. Not optional if
   the pipeline ever runs; currently absent entirely.
2. **Analytics ingestion** — weekly Studio pull into `library.db`, closing the
   observe→accumulate→promote loop the vault was built for.
3. **Topic-validation lab** — one command producing 20 candidates with search
   clusters, competitor scoreboards, and a kill/make/short-first verdict. Both
   voices independently named this as the 10x reframe.
4. **Deliberate-variation check** — format/length/structure must vary across
   consecutive uploads, checked against the last five, not per-video.
5. **run.json content hashing** — hash `script-<cut>.md` alongside the voice
   stage so an edited script invalidates stale MP3s on resume.

## 0E. Temporal interrogation

```
  HOUR 1  Which channel do these upload to? It does not exist yet.
  HOUR 2-3 Does the AI-expert carve-out trigger on the persona or the voice?
           us-market-2026.md:129 flags this as unresolved. It decides whether
           the vertical is monetisable at all.
  HOUR 4-5 faster-whisper is not installed; fin-render's QA gate cannot run.
           Install it, or drop the re-transcription check and lose the one
           automated verification that the render says what the script says.
  HOUR 6+  What does "better than the last one" mean with no analytics?
           Without an answer, fin-archive writes evidence lines with no evidence
           into best-practices.md — the one file in this project that compounds.
```

## 0F. Mode

**SELECTIVE EXPANSION.** The plan's scope is the baseline; expansions above are
cherry-pick candidates. But the premise gate comes first: three of five premises
are refuted by this repo's own notes, so scope decisions are premature until the
creator rules on them.

---

## CEO REVIEW — Sections 1-11

Creator decision 2026-07-28: **Option A — build now, four holes closed.** Accepted
scope additions: (1) Gate 2 compliance stage, (2) `faster-whisper` installed,
(3) `run.json` script hashing, (4) format constants in one config file.

### Section 1 — Architecture

```
                    ┌──────────────────────────────────────────┐
                    │  /finance-video "topic"  (orchestrator)   │
                    │  holds: intake + run.json + 1 line/stage  │
                    └────────────────┬─────────────────────────┘
                                     │ never holds artifacts
        ┌────────────────────────────┼────────────────────────────┐
        ▼                            ▼                            ▼
  ┌───────────┐              ┌───────────┐              ┌──────────────┐
  │fin-research│  ∥          │ fin-facts │              │ format.json  │  ← NEW (fix 4)
  │ study.py   │             │ WebSearch │              │ 9 segs, 12.2 │
  │ library.db │             │ ≥2 sources│              │ chars/s, …   │
  └─────┬─────┘              └─────┬─────┘              └──────┬───────┘
        │ video-studies/<slug>.md  │ money-facts-2026.md       │ read by all
        └────────────┬─────────────┘  ⚠ SHARED MUTABLE STATE   │
                     ▼                                          │
   ╔═════════════════════════════════════════════════════════╗ │
   ║  PER-CUT CHAIN  (runs twice: -hi to @cashguruguides,     ║◄┘
   ║                  then -en to @moneymavens101)            ║
   ║  fin-script → fin-audit → fin-voice → fin-storyboard     ║
   ║      │           │  gate1     │ £££       │              ║
   ║      │           └─ FAIL×2 ⇒ stop before credits         ║
   ║  → fin-assets → fin-build → fin-render → fin-package     ║
   ║                                │ gate2        │ +Gate 2  ║
   ║                                └─ 5 frames before encode ║
   ╚═════════════════════════════════════════════════════════╝
                     ▼
              fin-archive → vault/index.md + best-practices.md  ⚠ SHARED MUTABLE
```

**Coupling introduced:** `fin-audit` validates the script against
`money-facts-2026.md`, which `fin-facts` wrote earlier **in the same run**. That is
a closed loop — the run grades its own homework. **FINDING 1-A (HIGH).**

**Single points of failure:** ElevenLabs API (no offline fallback), Pixabay API,
`npx --yes hyperframes@0.7.66` (fetched from the network on every `npm run check`,
so the determinism claim rests on the npm cache, not a lockfile). **FINDING 1-B (MED).**

**Scaling:** irrelevant. One run at a time, one creator. Not a concern.

**Rollback posture:** none specified. `fin-facts` and `fin-archive` write to shared
vault knowledge files consumed by every future video. A bad autonomous run poisons
the compounding asset with no undo. **FINDING 1-C (CRITICAL).**

**Auto-decisions (P1 completeness, P5 explicit):**
- 1-A → `fin-audit` must verify the hero number against the **source URL** recorded
  by `fin-facts`, not against the claim text. Independent re-fetch, not self-reference.
- 1-B → accept the API SPOFs (no cheap alternative); pin hyperframes via a committed
  lockfile rather than `npx --yes`.
- 1-C → **`git commit` the vault before each run**, and have `fin-facts` /
  `fin-archive` write through a per-run staging file that the orchestrator merges
  only after `fin-render` passes. One bad run is then one `git revert`.

### Section 2 — Error & Rescue Map

```
 STAGE          | WHAT CAN GO WRONG              | FAILURE CLASS        | RESCUED? | USER SEES
 ---------------|--------------------------------|----------------------|----------|-------------------
 fin-research   | library has no comparable vids | EmptyStudyPacket     | Y        | "scrape owed", run continues
                | yt-dlp 429 / captions missing  | StudyFetchError      | Y        | flagged in manifest
 fin-facts      | no primary source for a number | UnsourcedClaim       | Y        | number dropped, logged
                | web page contradicts itself    | SourceConflict       | N ← GAP  | picks one silently
 fin-script     | over budget >1.3x              | BudgetExceeded       | Y        | fin-voice refuses
 fin-audit      | FAIL twice                     | AuditRejected        | Y        | run stops, no credits spent
 fin-voice      | ElevenLabs 401 / quota         | TTSAuthError         | N ← GAP  | partial mp3 set on disk
                | clip generated but silent      | SilentClip           | N ← GAP  | silent video ships
 fin-storyboard | timing.json missing a segment  | TimingMismatch       | N ← GAP  | scene with no VO
 fin-assets     | every query returns junk       | NoUsableImage        | Y        | drops the cut-in
 fin-build      | npm run check never goes clean | CompositionInvalid   | Y        | stops after retry
 fin-render     | encode OOM / disk full         | RenderFailed         | N ← GAP  | partial mp4
                | whisper diff >0.1s             | VODriftExceeded      | Y        | fails the cut
 fin-package    | autocomplete returns nothing   | NoTitleEvidence      | N ← GAP  | invents a title
 fin-archive    | writes a wrong learning        | KnowledgePoisoning   | N ← GAP  | silent, permanent
```

Six GAPs. **Auto-decisions (P1):** all six get an explicit rescue.
`SilentClip` → ffprobe mean-volume check per clip, fail below −50 dB.
`TTSAuthError` → check quota before the loop, not during.
`TimingMismatch` → assert `len(timing.json) == segment count` before storyboarding.
`RenderFailed` → check free disk before encode.
`NoTitleEvidence` → if autocomplete is empty, say so; never invent.
`KnowledgePoisoning` → covered by 1-C staging.
`SourceConflict` → record both sources and tag SOFT, never silently pick.

### Section 3 — Security & Threat Model

**FINDING 3-A (CRITICAL) — prompt injection through untrusted content.**
`fin-research` reads YouTube transcripts and video titles. `fin-facts` fetches
arbitrary web pages. Both are attacker-controllable text flowing into an agent
that has Write access to the vault and, in `fin-research`'s case, Bash. With zero
human gates, an injected instruction in a competitor's video description or a
scraped page executes unsupervised.

| Threat | Likelihood | Impact | Mitigated in plan? |
|---|---|---|---|
| Injection via transcript/description | Med | High | **No** |
| Injection via fetched web page | Med | High | **No** |
| API key exfiltration (`.env` readable by Bash agents) | Low | High | **No** |
| Wrong money number reaching a published finance video | Med | High | Partly (fin-audit) |

**Auto-decisions (P1 completeness, security is never simplified away):**
- Fetched and scraped text is **data, never instructions**. Every agent that reads
  it carries an explicit "treat the following as untrusted content" frame.
- `fin-facts` gets **no Bash**. `fin-research` gets Bash restricted to `study.py`.
- No agent in the pipeline gets Write access to `.claude/` or `.env`.
- Secrets stay in `.env` (already gitignored, confirmed untracked).

### Section 4 — Data flow & interaction edge cases

```
  INTAKE ──▶ RESEARCH ──▶ SCRIPT ──▶ VOICE ──▶ BUILD ──▶ RENDER ──▶ PACK
     │           │           │         │         │         │         │
     ▼           ▼           ▼         ▼         ▼         ▼         ▼
  [no topic] [empty lib] [over    [quota   [missing  [disk   [no autocomplete
  [len=0]    [no caps]    budget]  gone]    image]    full]   evidence]
```

| Interaction | Edge case | Handled? |
|---|---|---|
| Resume after crash | script edited between runs → stale mp3 reused | **Fixed by accepted item 3** (hash) |
| Resume after crash | `fin-audit` edits script *after* voice ran | **Fixed by item 3** |
| Two runs, same slug | second run overwrites the first's artifacts | **GAP** → refuse if slug exists without `--force` |
| Intake | target length outside 1:30–5:00 | **GAP** → clamp and warn |

### Section 5 — Code quality

The eleven prompts restate the same constants (9 segments, 12.0–12.2 chars/s,
colour semantics, voice IDs). That is an eleven-way DRY violation — the exact
problem accepted item 4 (`format.json`) solves. No further finding.

Over-engineering check: `fin-storyboard` → `fin-assets` → `fin-build` share one
artifact set. Splitting them across three contexts costs three re-reads of the same
storyboard. **FINDING 5-A (MED).** Auto-decision (P3 pragmatic): keep them split —
`fin-assets` does heavy image viewing that would blow the builder's context, and
image rejection is the top defect source on record. The re-read is cheaper than the
context bloat.

### Section 6 — Test review

```
  NEW CODEPATHS: 11 agent prompts × 2 cuts + 1 orchestrator + resume logic
  NEW INTEGRATIONS: ElevenLabs, Pixabay, YouTube (yt-dlp), hyperframes, faster-whisper
  NEW ERROR PATHS: the 13 rows in Section 2
```

An agent pipeline cannot be unit-tested the way code can. What is testable:

| Item | Test type | Exists? |
|---|---|---|
| `format.json` parses and every agent reads the same constants | unit | **write it** |
| resume: edit script → voice stage invalidates | integration | **write it** |
| `SilentClip` guard: silent mp3 fails the run | unit | **write it** |
| Full pipeline on an already-shipped topic | E2E golden run | **the §8 criterion** |
| Injection resistance: transcript containing "ignore previous instructions" | adversarial | **write it** |

**Auto-decision (P1):** the four unit/integration checks land as one
`tools/test_pipeline.py` with asserts, no framework. The golden run stays the
acceptance test. **Flakiness risk:** the E2E test depends on live APIs and is
inherently flaky; run it manually, never in a loop.

### Section 7 — Performance

Wall-clock per run, measured from the record: encode ~18 min × 2 cuts = **~36 min
of pure ffmpeg**, untouchable by agent design. TTS ~9 clips × 2. Agent time
dominates nothing; the encode does.

**FINDING 7-A (HIGH):** no cost ceiling. "Every stage retries once" doubles
worst-case ElevenLabs spend and encode time. Auto-decision (P1): `run.json` carries
a `budget` block; the orchestrator refuses to start a stage that would exceed it.

### Section 8 — Observability

`run.json` records stage status only. If a run produces a bad video you cannot
reconstruct why. **FINDING 8-A (HIGH).** Auto-decision (P1): each stage appends
`{stage, started, ended, tokens, cost, summary}` to `run.json`. That is the
debuggability floor for an unattended pipeline, and it doubles as the cost ledger
Section 7 needs.

### Section 9 — Deployment

Agents ship as markdown files in `.claude/agents/`. Rollback is `git revert`.
**FINDING 9-A (CRITICAL):** `.gitignore:32` ignores `studio` — every composition,
timing table and render is outside version control, and there is still no git
remote. Auto-decision: un-ignore `studio/videos/*/index.html`, `meta.json`,
`package.json`, `assets/voice/timing.json` (text, tiny, is the actual build source);
keep ignoring `renders/`, `*.mp3`, `assets/img/`. Then push a remote.

### Section 10 — Long-term trajectory

Reversibility: **4/5.** Eleven markdown files and one config; deleting them costs
nothing and the manual pipeline still works. That is the strongest argument for
building now — this is a two-way door, and the CEO objection treated it as one-way.

Debt introduced: eleven prompts to keep in sync with the format (mitigated by
`format.json`), and a pipeline whose external deps all drift.

The 1-year question: a new reader in 12 months sees `format.json` and eleven
agents that reference it. That reads clearly. Without `format.json` it would not.

### Section 11 — Design & UX

The "user" here is the creator running one command, plus the viewer watching the
output. Interaction state coverage for the command:

| State | Specified? |
|---|---|
| Loading (which stage is running) | **GAP** → orchestrator must print stage transitions |
| Empty (no research found) | Yes, `fin-research` continues on vault knowledge |
| Error (stage failed twice) | Yes, stops with reason |
| Success | Yes, reports paths |
| Partial (hi cut done, en failed) | **GAP** → must report the hi cut as usable |

AI-slop risk on the video output itself: **high and structural**. Nine fixed
segments, one design system, two voices, both channels. This is Section 3's policy
risk wearing a design hat. The accepted Gate 2 sameness check is the mitigation.

### Failure Modes Registry

```
 CODEPATH        | FAILURE MODE          | RESCUED? | TEST? | USER SEES  | LOGGED?
 ----------------|-----------------------|----------|-------|------------|--------
 fin-voice       | silent clip           | N→Y fix  | N→Y   | Silent←BAD | N→Y
 fin-facts       | source conflict       | N→Y fix  | N     | Silent←BAD | N→Y
 fin-archive     | knowledge poisoning   | N→Y fix  | N     | Silent←BAD | N→Y
 fin-research    | prompt injection      | N→Y fix  | N→Y   | Silent←BAD | N→Y
 fin-package     | invented title        | N→Y fix  | N     | Silent←BAD | N→Y
 orchestrator    | no cost ceiling       | N→Y fix  | N     | £££        | N→Y
```
Six CRITICAL GAPs, all silent-failure class, all now assigned a fix.

### NOT in scope (deferred, with rationale)

- Topic selection / Gate 0-1 — creator's call, and the niche gate is still owed.
- YouTube upload — both channels already have a working manual upload flow.
- Analytics ingestion — **P3, deferred to TODOS**, but it is the highest-value
  follow-up and should land before the second month of uploads.
- Topic-validation lab — both CEO voices named it as the 10x reframe. Deferred,
  not dismissed.

---

## DESIGN REVIEW — Phase 2

Dual voices: Claude subagent + Codex. 6/6 consensus dimensions CONFIRMED.
Five concrete claims verified against the repo before acceptance.

### D-1 (CRITICAL) — the spec names the wrong design system

`design-techtooltester.md:21-22` — "BRIGHT white/pastel drifting gradient… **No
grain. No vignette. No black.**" The shipped finance composition is `--bg:#0d1017`,
full-bleed photo, `.scrim` 4-layer, `.grain` at 0.05. They contradict each other on
background, grain, media sizing, fonts, SFX and outro. §4.6 sends `fin-storyboard`
to the bright doc and §4.8 sends `fin-build` to the dark reference. Drift starts
on run #1, from the spec itself.

**Auto-decision (P4 DRY, P5 explicit):** extract
`vault/knowledge/design-finance-blockframe.md` from the shipped `index.html` +
both storyboards (tokens, grade, scrim, per-scene `--tint`, type ladder, motion
helpers, ken alternation, no-SFX, CTA-not-logo). It becomes the **only** design
doc the finance agents read. Fork `templates/storyboard-template.md` into a
finance variant — the current one hardcodes the bright link, `build.mjs`, and the
logo outro.

### D-2 (CRITICAL) — "fixes until clean" will degrade every video

`storyboard-hi.md:267`: *"Do not 'fix' it by lightening the text."* The contrast
pass mis-reads the rotated `#s3stamp` (1.7:1 reported, legible in frame). §4.8
tells `fin-build` to fix until clean. An autonomous builder lightens the token,
the signature stamp goes mushy, silently, forever.

**Auto-decision:** `format.json` carries `known_benign: [{selector, rule, reason}]`.
`fin-build` fails loudly on a **new** finding and may never edit a design token to
satisfy a checker. Principle stated in the prompt: **the checker is evidence, not
authority.**

### D-3 (CRITICAL) — information hierarchy is temporal and written nowhere

Hierarchy in the shipped video is reveal-order, not layout: kicker → one focal
element → chip cascade → stamp. One focal per scene, nothing before its word.
The spec's entire design brief is "wants = amber" plus "densest scene gets the
calmest background." An agent can legally emit two focal elements or three cues
at the same offset and pass every check.

**Auto-decision:** hard constraints in `format.json`, linted by `fin-audit` at
text level (free, pre-TTS): exactly one focal element per scene; kicker first;
consecutive cues ≥0.8s apart except a declared cascade (≤5 items, 0.6-0.7s);
≤6 simultaneous elements; something on screen by scene-start +0.5s.

### D-4 (HIGH) — cues are character-interpolated and nothing measures them

Cue offsets ship as `0.4 + chars_before/total × clip_duration`. `fin-render`'s QA
diffs **VO clip placement**, not cue placement — a chip can pop 1.5s after its
word with every gate green. Worst on Hindi, where delivery rate swings across a
26s clip.

**Auto-decision:** `faster-whisper` is already an accepted install. `fin-voice`
emits `words.json` (word-level timings); `fin-storyboard` anchors each cue to a
word token, not a character ratio. Highest-value design fix available, costs one
extra output file from a stage already running.

### D-5 (HIGH) — no type ladder; font sizes drift first

Class defaults are hand-overridden in 5 of 9 scenes. The pipeline's equivalent
move is shrinking `.huge` to fit, which silently violates D-3 with a green check.
Predicted drift order: font sizes → per-scene `--tint` → motion vocabulary → ken
alternation → the filter grade (the only reason nine unrelated photos read as one
film).

**Auto-decision:** discrete ladder in `format.json` (focal ∈ {240,112,88,76},
chip 32, kicker 30, foot 26); no inline `font-size` outside it; step down the
ladder, never interpolate. Add a **max-density snapshot pass** in `fin-build`:
seek to each scene's *last* cue, measure `.stack` against the safe area, fail on
overflow. Nine deterministic frames replace `fin-render`'s five time-spaced ones,
which sample under 10% of the ~60 distinct layout states.

### D-6 (HIGH) — number rendering is wrong in the reference implementation

Verified in `studio/videos/needs-vs-wants/index.html`:
1. No `tabular-nums` anywhere — `countUp` rewrites `textContent` per frame inside
   a centered flex column, so counters physically shimmy while counting.
2. `index.html:339` groups digits Western-only. `124564` renders `124,564`; the
   Indian-correct form is `1,24,564`. Latent because at 5 digits the two agree.
   The first six-figure Hindi hero number ships wrong to an Indian audience.
3. No reserved width, so `₹24,564` and `$1,596` land the two cuts' columns at
   different widths for no designed reason.

**Auto-decision:** `tabular-nums` on every numeric class;
`Intl.NumberFormat('en-IN')` for `-hi`, `'en-US'` for `-en` inside `countUp`
(deterministic in Chrome, no network); `min-width` on `.counter`. Fix the
reference file **before** any agent copies it.

### D-7 (HIGH) — the thumbnail is generated into an open loop

`fin-package` renders thumbnails with no reviewer and no CTR signal, and analytics
are deferred. Twenty videos in: forty thumbnails, zero knowledge. Concrete
failures: no line-length clamp (the design holds ~14 chars/line; "MINIMUM PAYMENT
KA JAAL" is 23), duplicate-thumbnail syndrome across a channel grid, and
**fabricated focal numbers** — `fin-audit` traces numbers in the script, never in
the thumbnail, so the one artifact everyone sees is the one with no fact-check.

**Auto-decision (P1 completeness):** generate **3 variants per cut**; the creator
picks one at the manual upload step, which is already human — this is a free human
eye that costs zero extra interruption. Replace "energy over subtlety" with: ≤12
chars/line, ≤2 lines, one focal colour, one accent. Add a legibility assert
(downscale to 320×180, largest line must span ≥40% width). Add a sameness diff
against the channel's last 3. `fin-audit` traces thumbnail numerals to the script.

### D-8 (HIGH) — a per-video colour inversion was frozen into the channel system

"wants = amber; red is only the leak" was a **thesis-derived** inversion for
needs-vs-wants ("wants aren't the enemy"). On `credit-card-minimum-payment` it is
meaningless, and red should be the interest trap.

**Auto-decision:** `format.json` names **roles** (`positive`/`accent`/`danger`/
`cta`) with hex values, never meanings. `fin-storyboard` writes a 4-line colour
table derived from *this* video's thesis; `fin-audit` checks coloured elements
against it. This is the check that catches "the video argues against its script."

### D-9 (HIGH) — porting hi→en breaks on rhythm, not width

On-screen text is English/Hinglish in both cuts, so width is not the issue. The
delta is VO rate (12.0-12.2 vs 15 chars/s). Because cue offsets are a fraction of
clip duration, **every** gap stretches proportionally — dead air lands inside a
cascade instead of in the hold.

**Auto-decision:** split cue offsets into `anchored` (scales, lands on a word) and
`fixed` (cascades, stamp slams: constant). Surplus time goes to holds, never
cascades. `fin-storyboard` emits an explicit divergence list for the `-en` pass
with a reason per scene; `fin-audit` flags a `-en` storyboard with **zero**
divergences as suspicious — that is translation-not-rewrite wearing a layout
costume. No auto-wrap on focal classes.

### D-10 (MEDIUM) — photo-free scenes are an unspecified state that failure creates more of

s2 and s7 drop `.bg` **and** `.scrim`, losing the per-scene tint, rendering flat.
Fine as a deliberate 2-of-9 rest beat. But `fin-assets` may "drop a cut-in", and
nothing caps the count — at Pixabay's ~20% India-with-people hit rate you reach
4-5 flat scenes and the film unity is gone. Flat black passes every check.

**Auto-decision:** cap photo-free scenes at **2**, declared before sourcing. If
`fin-assets` cannot fill a slot it converts the scene to the photo-free recipe and
**fails the run if that would exceed the cap**. Add a mean-luminance check on each
graded image so `fin-assets` sets the `filter:` override itself instead of passing
a note downstream.

### D-11 (MEDIUM) — chip rows wrap silently, legally, and ugly

`.row{flex-wrap:wrap}`. Four long chips wrap 3+1 with an orphan. Nothing overflows
or clips, so `check` passes. **Auto-decision:** ≤3 chips/row, ≤22 chars/chip, rows
declared explicitly in the storyboard. Text-level, so `fin-audit` catches it free.

### D-12 (MEDIUM) — the font stack is fiction

`fc-list | grep -ci "arial black"` → **0**. `fc-match "Arial Black"` →
`NotoSans-Regular.ttf`. Every "font-weight:900" in every shipped finance video is
faux-bold Noto Sans, and the hand-tuned letter-spacing is calibrated to a fallback.
`design-techtooltester.md` states the rule the shipped file breaks.

**Auto-decision:** self-host one variable woff2 with Latin + `₹` coverage in
`studio/library/fonts/`, `@font-face` it, delete the system stack. State in
`format.json` that all on-screen and thumbnail text is Latin script in both cuts;
lint for non-Latin codepoints.

### D-13 (MEDIUM) — neither finance channel has a brand mark

`studio/library/brand/` holds `techtooltester/` and `historyframesfilm/` only.
The standing outro rule (logo + SUBSCRIBE) is unsatisfiable and the finance cuts
silently ignore it. **Auto-decision:** one wordmark per channel before the
pipeline runs, placed in s9 and a fixed thumbnail corner; until it exists, delete
the outro rule from the finance design doc rather than leave a rule the pipeline
can only break.

### Design gaps in the command's own UX

| State | Specified? | Fix |
|---|---|---|
| Loading (which stage is running) | GAP | orchestrator prints stage transitions |
| Partial (hi done, en failed) | GAP | report the hi cut as usable |
| Compliance disclosure placement | GAP | Gate 2 must name where it appears on screen |

---

## ENG REVIEW — Phase 3

Dual voices: Claude subagent + Codex. Claims verified against the code before acceptance.

```
ENG DUAL VOICES — CONSENSUS TABLE
  Dimension                     Claude  Codex  Consensus
  ───────────────────────────── ─────── ────── ──────────
  1. Architecture sound?        PARTLY  NO     CONFIRMED (handoff idea right, impl unreliable)
  2. Test coverage sufficient?  NO      NO     CONFIRMED (no contracts = nothing to assert)
  3. Determinism guaranteed?    NO      NO     CONFIRMED (CDN + unpinned TTS + npx)
  4. Security threats covered?  NO      NO     CONFIRMED (injection → vault poisoning)
  5. Error paths handled?       NO      NO     CONFIRMED (half-written artifacts indistinguishable)
  6. Resume actually works?     NO      NO     CONFIRMED (no invalidation, no skip-if-exists)
```

### E-1 (CRITICAL) — stage completion is asserted by an LLM, never verified

`run.json` is the state machine, and a stage becomes `done` because a subagent's
reply said so. No stage has a machine-checked postcondition. Every guarantee in §5
rests on a natural-language self-report from the stage most likely to be confused
about whether it finished.

**Auto-decision (P1):** orchestrator writes `done` only after
`tools/pipeline_check.py <stage> <slug> <cut>` passes — `timing.json` parses and
has 9 entries, every `hN.mp3` exists with ffprobe duration > 1.0s, every
`manifest.json` key has a file on disk, root `data-duration` equals last scene
start + duration. ~80 lines. The agent's reply becomes advisory.

### E-2 (CRITICAL) — the handoff files the design rests on do not exist

`find studio -name timing.json` → **0 results**. The real artifacts are
`hindi-lines.json` / `english-lines.json` / `haryanvi-lines.json` / `lines.json`
(four competing names across six projects), and durations exist only as terminal
output hand-copied into `index.html`. §3 described new surface area as if it were
existing reuse.

**Auto-decision:** declare `timing.json` as new, define its schema in the spec, and
have a thin `tools/tts/batch.py` emit it — not an agent transcribing ffprobe by
eye. Normalise all six projects to `lines.json`.

### E-3 (CRITICAL) — GSAP is fetched from a CDN at render time

`index.html:6` loads `gsap` from jsdelivr. `studio/CLAUDE.md:111` forbids
render-time network fetches. Failure mode is the worst class: fetch fails or is
slow past first paint → `gsap` undefined → the inline script throws → **no timeline
registers** → the render *succeeds*, producing a video with every element visible
from frame 0 and zero motion. `npm run check` runs against the same network and
usually passes. A five-frame check shows plausible static frames.

**Auto-decision:** vendor `gsap.min.js` into `studio/library/js/`, reference
locally. One file; deletes an entire class of silent render corruption. Applies to
the already-shipped videos too.

### E-4 (CRITICAL) — injection → vault poisoning through a self-grading audit loop

`fin-research` reads yt-dlp transcripts, titles and descriptions (anyone can upload
a video whose description targets this pipeline) and holds Bash. `fin-facts`
fetches arbitrary pages and holds Write into shared knowledge. `fin-audit` then
validates numbers against the file `fin-facts` wrote **in the same run**. An
injected page planting a plausible dated "RBI" line passes the audit by
construction, ships in a finance video, and persists for every future video.

**Auto-decision (security is never simplified away):**
(a) `fin-facts` writes to `vault/videos/<slug>/facts-staging.md`, never to shared
knowledge; promotion is a separate post-render step.
(b) `fin-audit` re-fetches the recorded source URL and matches the figure against
the fetched page, not the claim text.
(c) Every agent reading fetched text carries an explicit untrusted-data frame.
(d) `fin-research` Bash allowlisted to `study.py` only; `fin-facts` and
`fin-assets` get no Bash; no agent may read `.env` or write `.claude/`.

### E-5 (CRITICAL) — `fin-voice` is not resumable; the core resume claim is false

`elevenlabs_tts.py` has **zero** skip-if-exists (`pixabay_fetch.py:93` has it).
`gen_vo_hi.sh` regenerates all nine unconditionally. A crash at clip 6 re-spends
all nine. `vault/workflows/voiceover-tts.md` already states this exact rule and
the finance scripts don't implement it.

Compounding: `gen_vo_hi.sh` is `set -e` with **no `pipefail`**, piped to `tail -1`,
so a 401/429 at clip 3 prints one line and the loop keeps going. Nothing on disk
distinguishes "8 of 9 clips" from "9 of 9".

**Auto-decision:** add `--skip-existing` to `elevenlabs_tts.py` (4 lines, mirrors
pixabay); resume unit becomes the clip, not the stage; `set -euo pipefail`; write
`timing.json` via tmp-file + `os.replace` so it is never observed half-written;
assert each clip > 10KB and within ±35% of `chars / rate`.

### E-6 (HIGH) — Phase 1's parallelism is the one place with a lost-update race

"The two agents share no state" is false — both touch `vault/index.md`, and `Edit`
is read-modify-write with no locking. **Auto-decision (P3):** serialize Phase 1.
It saves ~90 seconds of a ~3-hour run; the parallelism is not worth a bug class.

### E-7 (HIGH) — `study.py` cannot fetch Hindi captions

`backend/study.py:116` — `subtitleslangs: ["en","en-orig","en-US","en-GB"]`. A
Hindi competitor video will never yield a transcript, which is exactly the corpus
the `-hi` cut needs. **Auto-decision:** add `hi`, `hi-orig`; `study.py` exits
non-zero if fewer than 2 of 3 picks produced a transcript; `fin-research` refuses
to write a study note below that threshold rather than degrading silently.

### E-8 (HIGH) — retry defeats its own image fix

`pixabay_fetch.py:93` skips on **filename only**. The §5 retry re-runs the stage,
so a changed query for `s3.jpg` prints `skip (exists)` and the rejected image
ships. This is the highest-frequency defect class in the spec's own account.
**Auto-decision:** store the resolved query hash beside the file; skip only on
match.

### E-9 (HIGH) — duration numbers are duplicated four ways

Each scene's timing lives in `<section data-start/data-duration>`, the JS `S` map,
the `<audio>` row, and the root `data-duration`. The relation is an unwritten
constant, verified across both cuts: `scene_duration = 0.4 + clip_duration + 1.0`.
A partial retry updating three of four passes `check` and ships a video whose
animations fire against the old timeline. **Auto-decision:** generate the timing
block from `timing.json` with a script; `pipeline_check` asserts the copies agree.

### E-10 (HIGH) — no cost ceiling; determinism unpinned

~4,475 TTS chars per run, doubled by retry-once, unbilled-checked; `npx --yes
hyperframes@0.7.66` resolves over the network every `check` and `render` with no
lockfile; TTS passes no `--model`/`--seed` while `voiceover-tts.md` records
`eleven_v3` as decided. **Auto-decision:** preflight the ElevenLabs quota against
the run's total char count; `budget` block in `run.json`; `npm i -D` with a
committed lockfile; pin model and seed in the generated `gen_vo_<cut>.sh`.

### E-11 (TASTE — surfaced, not auto-decided) — four of eleven agents are scripts

`fin-voice` (API loop + ffprobe), the timing half of `fin-build` (templating),
`fin-render` (npm + ffprobe + whisper diff), and `fin-archive` (file appends)
contain no judgment. Making them agents costs a context window each, makes them
untestable, and makes deterministic work nondeterministic. The reviewer's
alternative: four judgment agents (`fin-research`, `fin-facts`+`fin-audit`,
`fin-script`, `fin-assets`) plus scripts for the rest.

This contradicts the creator's approved "eleven agents" decision, so it goes to
the gate rather than being applied.

### Testing (E-12) — what makes this testable at all

The test surface is the ten handoffs, not the eleven prompts.
**Auto-decision (P1):** (1) the three machine-consumed handoffs become JSON with
fixed schemas — `timing.json`, `manifest.json`, `run.json`; markdown stays for
human-read artifacts. (2) One `tools/pipeline_check.py` holding every
postcondition, with `--selftest` on fixtures — the same pattern `study.py` and
`pixabay_fetch.py` already use. (3) `FIN_FAKE_APIS=1` honored by
`elevenlabs_tts.py` (emit a silent mp3 sized from char count) and
`pixabay_fetch.py` (copy a fixture jpg) — a full dry run then costs zero credits
and zero encode while exercising every handoff and crash path. ~30 lines across
two files, and it is the single highest-value testability change. (4) Every
arithmetic rule moves out of prompts into `tools/fin_format.py` with a selftest.

---

## DX REVIEW — Phase 3.5

```
DX DUAL VOICES — CONSENSUS TABLE
  Dimension                       Claude  Codex  Consensus
  ─────────────────────────────── ─────── ────── ──────────
  1. TTHW acceptable?             NO      —      single-voice finding
  2. Intake questions right?      NO      —      CONFIRMED by inspection
  3. Errors actionable?           NO      NO     CONFIRMED ("failed:1" is one token)
  4. Prompts maintainable?        NO      NO     CONFIRMED (third memory home)
  5. Resume usable in practice?   NO      —      CONFIRMED (5 separate gaps)
  6. Discoverable in 3 months?    NO      NO     CONFIRMED (zero entry points)
```

**TTHW: today ~5 h attended per pair. As specified ~2h45–3h30 wall clock, ~36 min
of it pure ffmpeg, but with no progress output the honest first-run figure is
4–6 h. Target: 0 questions + 1 confirm, first watchable cut ≤50 min, both cuts
≤2 h, zero silent waiting.**

### X-1 (CRITICAL) — no confirm before a 3-hour, real-money run
A typo in the topic is discovered 90 minutes later, after credits and an encode.
**Auto-decision:** after intake print derived slug, both char budgets, voice IDs,
estimated TTS chars, estimated wall clock, output paths — require one `y`.
`--yes` skips it.

### X-2 (CRITICAL) — the creator sees nothing for three hours
§1 forbids the orchestrator holding artifacts and caps returns at 20 lines, but
never says it *prints* anything. **Auto-decision:** one line per stage transition
(`▶ fin-storyboard-hi · 6/17 · 00:41 elapsed`), the agent's return echoed under
it, notification on terminal states. State explicitly that renders run
backgrounded — an 18-minute foreground render inside a subagent is a timeout.

### X-3 (CRITICAL) — `failed:1` is not debuggable, and the schema contradicts itself
§3 writes `"failed:1"` (a counter); §5 says `failed:<reason>` (a string). Worse,
the failing agent holds the actual evidence — the `check` error text, the HTTP
body, the ffprobe output — and that context is **discarded** on return.
**Auto-decision:** each agent writes
`vault/videos/<slug>/logs/<stage>-<cut>-<attempt>.md` before returning;
`run.json` stores `{status, reason, log, at}` with the retry counter as a separate
field; on terminal failure the orchestrator prints the reason, the log path, and
**the exact command to re-run that stage alone**.

### X-4 (HIGH) — two of four intake questions are unanswerable at intake time
Hook angle is asked before `fin-research` reads a single transcript. "Fresh
numbers?" is a lookup, not a decision. Target length is asked before the
competitor scoreboard exists, and the default is almost always right.
**Auto-decision:** one input (the topic, already the argument) + the X-1 confirm
with a pre-filled length. Drop the hook question; replace the numbers question
with a grep during Phase 1. **Missing entirely: which channel this pair targets** —
there are two live finance channels.

### X-5 (HIGH) — agent `description` frontmatter will hijack unrelated work
Claude Code auto-selects subagents by `description`. Eleven finance agents in a
repo that also produces Urdu history videos (no-face depiction lock, Nastaliq
masters) means "write the storyboard for the Aad video" can fire `fin-storyboard`
and apply finance design rules and ₹/$ currency-purity to a history script.
**Auto-decision:** every description is scoped and terminal — *"Finance-pipeline
stage. Invoked only by /finance-video. Do not select for other work."*

### X-6 (HIGH) — the invocation contract is never specified
A `.claude/agents/*.md` file has no parameters. Nothing says how the orchestrator
tells `fin-script` it is on the `-en` pass, or what shape the return takes.
**Auto-decision:** one identical block at the top of every agent file — receives
`slug`, `cut`, `attempt`, plus prior failure text on attempt 2; everything else
read from `run.json`. Returns exactly four lines: `STATUS:` / `ARTIFACTS:` /
`SUMMARY:` / `NEXT:`.

### X-7 (HIGH) — eleven prompts restating vault facts breaks this repo's top rule
`CLAUDE.md`: *"One home per fact. Never duplicate a fact across layers."*
`.claude/agents/` becomes a **third memory home** outside the vault's session
protocol, so nothing keeps it current. **Auto-decision:** prompts carry
*procedure*; the vault carries *facts*, read by path. Machine-readable constants
live in exactly one `format.json`. Add a line to `vault/CLAUDE.md`'s session
protocol covering `.claude/agents/`.

### X-8 (CRITICAL) — `--resume` is under-specified in five ways
No downstream invalidation (audit-edits-script-after-voice is the *normal* case,
so mtime can't fix it); `--resume <slug>` needs a slug the creator never saw; no
`--from <stage>` for the subjective image stage; partial-artifact semantics
undefined; and `run.json` outlives its artifacts — `studio/` is gitignored and the
post-delivery cleanup rule deletes renders, so a status string can lie.
**Auto-decision:** content-hash the script beside the voice stage and mark all
downstream stages not-done on any re-run; bare `--resume` picks the most recent
incomplete run; add `--list` and `--from <stage>`; existence-check every artifact
path before trusting a `done`; add a run lock.

### X-9 (HIGH) — nothing tells a future session this pipeline exists
Root `CLAUDE.md` is 14 lines and never mentions `studio/`. `vault/index.md` has no
pipeline entry. And `PRODUCTION_RUNBOOK.md` at root is 352 lines about *"A Century
of Travel"* — a history slideshow with Kokoro TTS — which is an active trap for
anyone grepping "runbook". **Auto-decision:** add `studio/` and `/finance-video`
to root `CLAUDE.md`; move and rename `PRODUCTION_RUNBOOK.md` →
`vault/workflows/runbook-history-slideshow.md`; add `[[workflows/finance-video]]`
to `vault/index.md`; write `vault/workflows/finance-video.md` as the human-facing
doc, matching the existing workflow convention.

### X-10 (MEDIUM) — no dry run, and "no human gates" hides two human steps
**Auto-decision:** `--dry-run` prints the stage plan, derived budgets, exact
commands and estimated spend, then exits. And the completion summary states
`Owed before publish: proof-listen (hi, en) · thumbnail check · upload.`

### X-11 (MEDIUM) — preflight doctor
`faster-whisper` is not importable; `timing.json` has no precedent; the lines-file
name has drifted four ways. **Auto-decision:** a `doctor` preflight before Phase 1
checking imports, keys, `ffprobe`, node version and free disk — fail in five
seconds with the fix command, not at minute 95.
*(Reviewer claim that the API keys are empty-valued was **refuted** — both are
populated.)*

---

## Implementation Tasks (aggregated across phases)

Ordered by what must be true before the pipeline runs unattended. P1 blocks the
first run; P2 lands same branch; P3 is a follow-up.

**Group 0 — fix the reference implementation first (it propagates by copy)**
- [ ] **T1 (P1, human ~30m / CC ~5m)** — studio — vendor `gsap.min.js` into `studio/library/js/`, drop the jsdelivr `<script>`. *Eng E-3. Silent render corruption: no timeline, static video, green checks.*
- [ ] **T2 (P1, human ~20m / CC ~5m)** — studio — `Intl.NumberFormat('en-IN'|'en-US')` in `countUp`, `tabular-nums` + `min-width` on numeric classes. *Design D-6. `1,24,564` currently renders `124,564`.*
- [ ] **T3 (P1, human ~1h / CC ~10m)** — studio — self-host one variable woff2 (Latin + `₹`), `@font-face`, delete the system stack. *Design D-12. Arial Black resolves to Noto Sans Regular.*
- [ ] **T4 (P2, human ~30m / CC ~10m)** — repo — un-ignore `studio/videos/*/{index.html,meta.json,package.json,assets/voice/timing.json}`; keep ignoring renders/mp3/img. Push a git remote. *CEO 9-A.*

**Group 1 — make the design system exist**
- [ ] **T5 (P1, human ~3h / CC ~30m)** — vault — write `vault/knowledge/design-finance-blockframe.md` from the shipped composition + both storyboards. Fork the storyboard template. *Design D-1. The spec currently names the opposite (bright) system.*
- [ ] **T6 (P1, human ~1h / CC ~15m)** — config — `format.json`: type ladder, colour **roles** (not meanings), cue-spacing floor, chip limits, `known_benign` checker findings, scene formula `0.4 + clip + 1.0`, voice IDs, char rates, hyperframes pin. *Design D-2/D-3/D-5/D-8/D-11, DX X-7, Eng E-9.*

**Group 2 — make failure visible**
- [ ] **T7 (P1, human ~3h / CC ~30m)** — tools — `tools/pipeline_check.py` with every stage postcondition + `--selftest`. Orchestrator writes `done` only on pass. *Eng E-1.*
- [ ] **T8 (P1, human ~1h / CC ~15m)** — tools — `--skip-existing` on `elevenlabs_tts.py`; `set -euo pipefail`; atomic `timing.json` via tmp+replace; per-clip size and duration asserts. *Eng E-5.*
- [ ] **T9 (P1, human ~2h / CC ~20m)** — tools — `FIN_FAKE_APIS=1` in the TTS and Pixabay tools. Full dry run, zero credits, zero encode. *Eng E-12.*
- [ ] **T10 (P1, human ~1h / CC ~15m)** — orchestrator — per-stage log files, `{status, reason, log, at}` in `run.json`, retry counter as its own field, print the re-run command on failure. *DX X-3.*

**Group 3 — close the security holes**
- [ ] **T11 (P1, human ~2h / CC ~20m)** — agents — `fin-facts` writes to `facts-staging.md` only; `fin-audit` re-fetches the source URL; untrusted-data frame on every agent reading scraped text; Bash allowlists; deny `.env` and `.claude/**`. *Eng E-4, CEO 3-A.*
- [ ] **T12 (P1, human ~1h / CC ~10m)** — orchestrator — vault `git commit` before each run; shared-knowledge writes staged and merged only after render passes. *CEO 1-C.*

**Group 4 — the pipeline itself**
- [ ] **T13 (P1, human ~1h / CC ~10m)** — orchestrator — confirm line before spend; stage-transition output; background the render. *DX X-1, X-2.*
- [ ] **T14 (P1, human ~1h / CC ~10m)** — orchestrator — intake to one input + confirm; **add the channel question** (two live finance channels exist). *DX X-4.*
- [ ] **T15 (P1, human ~2h / CC ~20m)** — orchestrator — resume: script content-hash, downstream invalidation, bare `--resume`, `--list`, `--from <stage>`, artifact existence checks, run lock. *DX X-8, CEO S4.*
- [ ] **T16 (P1, human ~30m / CC ~5m)** — agents — scoped terminal `description` frontmatter; identical invocation + 4-line return contract at the top of every agent file. *DX X-5, X-6.*
- [ ] **T17 (P2, human ~1h / CC ~10m)** — orchestrator — `doctor` preflight (faster-whisper, keys, ffprobe, node, disk); `--dry-run`; quota preflight and `budget` block. *DX X-11, X-10, Eng E-10.*
- [ ] **T18 (P2, human ~30m / CC ~10m)** — backend — add `hi`/`hi-orig` to `study.py` subtitle langs; exit non-zero below 2 of 3 transcripts. *Eng E-7.*
- [ ] **T19 (P2, human ~30m / CC ~5m)** — tools — query-hash keyed skip in `pixabay_fetch.py`. *Eng E-8.*
- [ ] **T20 (P2, human ~2h / CC ~20m)** — agents — Gate 2 compliance stage: disclosure placement, no-expertise framing, channel-level sameness check vs last 5 uploads. *CEO P5, accepted at the premise gate.*
- [ ] **T21 (P2, human ~1h / CC ~15m)** — agents — thumbnail: 3 variants per cut, ≤12 chars/line, legibility assert at 320×180, sameness diff, numerals traced to script. *Design D-7.*
- [ ] **T22 (P2, human ~1h / CC ~15m)** — agents — word-level cue anchoring from `words.json`; `anchored` vs `fixed` offset classes. *Design D-4, D-9.*
- [ ] **T23 (P2, human ~30m / CC ~10m)** — agents — photo-free scene cap of 2, luminance check, convert-not-degrade on image failure. *Design D-10.*

**Group 5 — discoverability**
- [ ] **T24 (P2, human ~1h / CC ~15m)** — docs — root `CLAUDE.md` gains `studio/` + `/finance-video`; move `PRODUCTION_RUNBOOK.md` → `vault/workflows/runbook-history-slideshow.md`; add `vault/workflows/finance-video.md`; index line. *DX X-9.*

**Deferred to follow-up (P3)**
- [ ] **T25 (P3)** — analytics ingestion: weekly Studio pull into `library.db`. Both CEO voices named this the highest-value follow-up; it closes the observe→promote loop the vault was built for.
- [ ] **T26 (P3)** — topic-validation lab: 20 candidates → search clusters → competitor scoreboards → kill/make/short-first verdict.
- [ ] **T27 (P3)** — run Gate 0/1 on the India-finance niche and record the pass/fail.

## FINAL SWEEP — Phase 5 (re-review) + creator decisions round 2

Creator decisions 2026-07-28 (round 2):
1. **Agents stay; deterministic work becomes SCRIPTS the agents invoke as tools.**
   Resolves the E-11 user challenge — uniformity of eleven agents kept, testability
   of scripts gained.
2. **Length tiers:** SHORT 1-5 min · MEDIUM 5-10 min · LONG >10 min.
3. **Thumbnails:** 3 variants per cut, creator picks at upload. No in-pipeline gate.
4. **Gate 2 compliance stage** accepted.

A fifth independent reviewer swept the whole plan for what four rounds missed.
30 new findings. The sharpest are verified below.

### ✅ POLICY QUESTION RESOLVED — the carve-out triggers on the persona, not the voice

Verified against `support.google.com/youtube/answer/1311392`. Synthetic narration
alone does **not** disqualify content; *"AI-generated podcast hosts offering
financial guidance, investment tips, or wealth management advice"* does. Full
finding and the four binding rules now live in
[[vault/knowledge/niches/us-market-2026]] under "RESOLVED 2026-07-28".

**Consequence for this plan:** the pipeline is viable. The exposure is category 1
(mass production / template sameness), which is channel-level — so the Gate 2
sameness check is no longer a nice-to-have, it is the single compliance control
that matters. The persona rules go into `fin-script` as hard constraints: no host
persona, no first-person expertise, no investment/stock/fund picks, disclosure
toggle recorded in every publish pack.

### R-1 (CRITICAL) — LONG is structurally impossible on the 9-segment template

`vault/workflows/voiceover-tts.md` **Rule 0** (creator rule, hardened 2026-07-22):
one TTS clip per *line* (~2-8s), never per paragraph. The finance format already
breaks it (`h6`=26.3s, `h7`=25.0s). At LONG on 9 fixed segments each clip is
**~66s** — longer than the 69s clip the vault names as the exact failure that
forced a 56-paragraph → 307-line rebuild.

**The repo already solved this.** `studio/videos/firaun-ka-anjaam/build.py` (36 KB,
verified): *"ONE LINE = ONE CLIP = ONE SCENE = ONE EXACT SPAN. No weight-splitting
— that hand-guessed share is exactly what drifted the images out of sync."*

**Decision:** the tiers are not a parameter, they are **two formats**.
- SHORT keeps the 9-segment blockframe template as-is.
- MEDIUM and LONG use the per-line architecture from `firaun/build.py`, chapter-wise
  (`--chapter N`), one line per clip per scene.
`fin-voice`'s hardcoded `{h1..h9}` is replaced by a line manifest. `format.json`
carries a `tiers` block, not a single segment count.

### R-2 (CRITICAL) — T12's auto-commit would swallow 55 uncommitted files

`git status --porcelain` = **55** entries of in-flight creator work. Branch
`audit/2026-07-17`, `git remote` empty. T12 commits the vault before each run so a
bad run is one `git revert` — but the first automated commit absorbs all 55, and
reverting the run reverts the creator's work with it. T12 is P1; "push a remote"
was P2.

**Decision:** T12 commits **only** `vault/videos/<slug>/` and
`vault/knowledge/money-facts-2026.md` by explicit path — never `git add -A`. It
refuses to run if those paths are dirty from a prior session. Pushing a remote is
promoted **P1, and it goes first.**

### R-3 (HIGH) — the postcondition that makes scripts-as-tools actually binding

`pipeline_check.py` as specified asserts `timing.json` parses, has 9 entries, and
each mp3 exists with duration > 1.0s. It never asserts the durations **in**
`timing.json` equal ffprobe's. An agent that hand-writes `timing.json` from a char
estimate — today's exact process — passes every gate and the whole composition is
built on fabricated timing.

**Decision:** add the cross-check. One assertion, and it is what makes "the script
is the authority" true rather than aspirational.

### R-4 (HIGH) — the Hindi char rate in this spec is wrong

§2 cites "Hindi ≈ 12.0-12.2 chars/s". Verified: `voiceover-tts.md:169` says that is
the **Nastaliq Urdu** rate; `india-finance-market.md:52` says **Hindi ≈ 12.5
chars/s** and explicitly calls 12.0-12.2 "the sister fact… Urdu rate". ~4s drift at
2:45, **~12s at 10:00**. `format.json` was about to freeze the wrong number.

### R-5 (HIGH) — the image library is already collapsing across both channels

md5-verified: `21fa39c794753b46dd8a5e1020f036d0` is `s9.jpg` in
`50-30-20-rule-en`, `emergency-fund` **and** `emergency-fund-en` — the closing CTA
frame, byte-identical across two videos and **both channels**. Separately,
`needs-vs-wants` and `needs-vs-wants-en` ship byte-identical `s3-want.jpg` *despite
genuinely different US/India queries* — Pixabay's top hit collapsed.

So query divergence does not produce image divergence, and D-9's "flag zero
storyboard divergences" will not catch it. At 20 uploads × 37 slots the channel
grid becomes one image set — which is category-1 mass-production evidence.

**Decision:** a repo-wide asset ledger keyed by md5. `fin-assets` refuses any image
whose hash already appears in any project on either channel, and takes the next
Pixabay result instead.

### R-6 (HIGH) — ElevenLabs commercial rights were never verified, and six videos are live

`monetization.md:25`: *"Free tier = NO commercial rights; Starter (~$5) = first
monetizable tier."* Six ElevenLabs-voiced videos are uploaded and scheduled on two
monetisation-seeking channels, and nothing in the vault records the account tier.
Default-library voices (Harsh, Brian, Prayan) also carry attribution requirements
on lower tiers. **This gates content already published.** One-line check owed
before publish date.

### R-7 (HIGH) — @cashguruguides has two narrators across three uploads

Verified: `emergency-fund` → Prayan `9BHT…` (Haryanvi); `needs-vs-wants` and
`50-30-20-rule-hi` → Harsh `HTUu…` (standard Hindi). The uploaded title says
*"Explained in Haryanvi"*. §4.5 locks Harsh **and** sends `fin-script` to
`haryanvi-hindi-script-style.md` — producing a Haryanvi-marked script read by a
standard-Hindi voice. **Creator decision owed:** which voice is the channel's
identity?

### R-8 (HIGH, license) — people as the subject of a negative money claim

Manifests are full of `"indian man smartphone"`, `"indian young man smiling"`,
`"family watching television"`. Pixabay's Content License bars use of identifiable
persons in a way that is unflattering or implies endorsement. A recognisable person
under a VO about wasting ₹24,564/yr is exactly that. `fin-assets`' trap list covers
brand marks, currency and density — nothing about depicting a person as the subject
of the claim. Exposure scales with image count, so LONG makes it ~4× worse.
**Decision:** add it to the trap list; prefer the object-led rule that
`stock-photo-sourcing.md` already established.

### R-9 (HIGH) — disk will stop the pipeline within a handful of LONG runs

`df`: **91% full, 22 GB free.** Measured 841 MB per 2:45 pair; Pompeii at 19:56 =
933 MB for one cut. A LONG pair is ~3-4 GB plus hyperframes work dirs (whose own
script warns two orphaned `work-*` dirs once filled the disk). §4.11 forbids
`fin-archive` from deleting renders; cleanup is creator-triggered. **An unattended
producer with a human-gated garbage collector.** Decision: preflight free-disk
against the tier's measured footprint; refuse to start below 2× headroom.

### R-10 (MEDIUM) — accepted caps are absolutes tuned to 9 scenes

Photo-free cap of 2 (from 2-of-9), 9 snapshot frames ("one per scene"), 6
simultaneous elements. At 30 scenes the photo-free cap fails nearly every run.
**Decision:** every cap in `format.json` becomes a **ratio**, resolved per tier.

### R-11 (MEDIUM) — tier boundaries ignore the only length threshold that pays

Mid-roll ads require **≥8:00**. MEDIUM (5-10) straddles it: 7:00 earns no mid-roll,
8:30 does. Neither the plan nor the vault mentions 8:00. **Flagged for the creator:**
if longer videos exist for revenue, the boundary is 8:00.

### R-12 (MEDIUM) — script exit codes carry no retry semantics

`elevenlabs_tts.py` exits 1 for 401 (terminal), 429 (retryable), network
unreachable (retryable) and missing key (terminal) — distinguishable only by prose
on stderr. Under scripts-as-tools an agent cannot tell "retry in 60s" from "stop,
the key is dead". **Decision:** distinct exit codes per class; the agent's retry
policy keys off the code, not the prose. Also: `pixabay_fetch.py` exits **0** with
the image missing, and aborts mid-batch leaving downloaded images with no
`CREDITS.txt` attribution — a licensing gap, not just a state gap.

### R-13 (MEDIUM) — three retry owners, no arbitration

The script (never retries), the agent (may re-invoke on its own), the orchestrator
(§5 "retries once"). "Retries once" can therefore mean 1, 2 or N billed API calls.
**Decision:** agents may not retry; only the orchestrator retries, and the `budget`
block counts **API calls**, not stage attempts.

### R-14 (MEDIUM) — the thumbnail loop never closes

3 variants × 2 cuts = 6 PNGs; the creator picks at upload; nothing writes the pick
back. `fin-archive` and `best-practices.md` never learn which won, so D-7's
sameness diff has no record of the last 3. **Decision:** the publish pack carries a
one-line `chosen: <file>` the creator fills at upload; `fin-archive` reads it.

### R-15 (MEDIUM) — the vault's own retention evidence contradicts the format

`best-practices.md` §Structure & retention carries **five dated confirmations** that
winners are 18-32 min, across two validated lanes. The finance format is 2:22-3:43
and the new LONG tier tops out at ">10 min". `fin-archive` appends dated evidence
lines to that same file — so with zero views on all six uploads, the pipeline would
start writing unfounded evidence next to five older lines that say the opposite.
**Decision:** `fin-archive` may not write to `best-practices.md` until a video has
28 days of real analytics. Until then it writes to the video's own milestone note.

### Corrections to earlier review rounds

- §2's "shipped range is 2:24-2:58" is **wrong**. Measured finals span
  141.7s-223.3s; `50-30-20-rule-en` is **3:43**. SHORT (1-5 min) therefore swallows
  every video ever shipped, so the tier choice changes nothing for the only format
  that currently exists.
- X-4 (drop the length question) is **superseded** by creator decision 2. The tier
  is asked — but `fin-research` should *propose* it at the confirm line rather than
  the creator guessing before any competitor data exists.
- T14's channel question conflicts with "always both cuts". **Resolved:** both cuts
  always ship, one per channel, so there is nothing to ask. The question is dropped.
- `.claude/` **does not exist** — verified. 12 of 27 tasks write into a directory
  that must be created first. This is greenfield, not an extension.

### New tasks from the final sweep

- [ ] **T28 (P1)** — push a git remote **before** T12. *R-2.*
- [ ] **T29 (P1)** — T12 commits explicit paths only, never `git add -A`. *R-2.*
- [ ] **T30 (P1)** — `format.json` gains a `tiers` block; MEDIUM/LONG use the
      per-line architecture from `firaun/build.py`, not the 9-segment template. *R-1.*
- [ ] **T31 (P1)** — `pipeline_check` asserts `timing.json` durations == ffprobe. *R-3.*
- [ ] **T32 (P1)** — correct the Hindi rate to **12.5 chars/s**. *R-4.*
- [ ] **T33 (P1)** — verify the ElevenLabs account tier carries commercial rights;
      record it in `monetization.md`. Gates six already-scheduled videos. *R-6.*
- [ ] **T34 (P1)** — repo-wide md5 asset ledger; `fin-assets` refuses a reused hash. *R-5.*
- [ ] **T35 (P2)** — distinct exit codes per failure class in both tools;
      `pixabay_fetch.py` must exit non-zero when an image is missing and write
      `CREDITS.txt` incrementally. *R-12.*
- [ ] **T36 (P2)** — caps in `format.json` become ratios resolved per tier. *R-10.*
- [ ] **T37 (P2)** — free-disk preflight against the tier's measured footprint. *R-9.*
- [ ] **T38 (P2)** — only the orchestrator retries; budget counts API calls. *R-13.*
- [ ] **T39 (P2)** — `fin-script` carries the persona rules as hard constraints;
      Gate 2 records the disclosure toggle in every publish pack. *policy resolution.*
- [ ] **T40 (P2)** — identifiable-person trap added to `fin-assets`. *R-8.*
- [ ] **T41 (P2)** — `chosen: <file>` line in the publish pack; `fin-archive` reads it. *R-14.*
- [ ] **T42 (P2)** — `fin-archive` may not write `best-practices.md` without 28 days
      of analytics. *R-15.*

### Creator decisions owed

1. **@cashguruguides narrator identity** — Harsh (2 uploads) or Prayan/Haryanvi
   (1 upload, and the uploaded title says "Explained in Haryanvi"). *R-7.*
2. **MEDIUM tier boundary** — 5-10 min as stated, or split at 8:00 for mid-rolls. *R-11.*

---

## CREATOR DECISIONS — round 3 (2026-07-28), both owed items closed

### 1. @cashguruguides narrator: STANDARD HINDI (Harsh `HTUuC7OeeEt6OL5fViVe`)

Recorded in [[vault/knowledge/niches/india-finance-market]]. `fin-script` no longer
reads `haryanvi-hindi-script-style.md` for finance work — that guide stays available
for other lanes. The scheduled `emergency-fund` upload is genuinely Haryanvi and
internally honest, so it needs no retitle or re-render; the channel converges on
Harsh from the next upload.

### 2. Tier boundaries: MEDIUM targets 8:30

Mid-roll ads require **≥8:00**. The original 5-10 min band straddled it, meaning a
7-minute video costs ~2.5× a short one and earns no mid-roll — the worst cell in
the table. Removing that dead zone:

| Tier | Target | Format | Mid-roll | Notes |
|---|---|---|---|---|
| **SHORT** | 1-5 min, default **2:45** | 9-segment blockframe (the proven, shipped format) | No | Every video shipped to date is here |
| **MEDIUM** | **8:30** | per-line chapter architecture (`firaun/build.py`) | **Yes** (30s margin over the 8:00 threshold) | The revenue tier |
| **LONG** | >10 min | per-line chapter architecture, chapter-wise build | Yes | Highest cost; only once MEDIUM proves out |

`format.json` `tiers` block carries per-tier: target seconds, segment/line model,
image-slot ratio, photo-free-scene ratio, snapshot count, char budget (Hindi
**12.5** chars/s · English 15), and the disk-footprint estimate used by the
free-space preflight.

**Consequence worth stating:** MEDIUM and LONG are a different production
architecture, not a longer run of the same one. They inherit the per-line pipeline
the repo already proved on Firaun — one line, one clip, one scene, one exact span —
and none of the 9-segment constants apply to them. SHORT remains the only tier with
a shipped, validated format.

---

## GROUP 0 — APPLIED 2026-07-28 (reference implementation fixed)

Applied to `studio/videos/needs-vs-wants/` and `needs-vs-wants-en/` — the pair
`fin-build` is specified to copy. Both pass `npm run check` (0 errors, 0 warnings).
Mirrored to `compositions/`.

- **T1 DONE** — GSAP vendored to `assets/js/gsap.min.js`; the jsdelivr `<script>`
  is gone from both cuts. `grep -c cdn.jsdelivr` = 0.
- **T2 DONE** — `Intl.NumberFormat("en-IN")` for `-hi`, `"en-US"` for `-en`, plus
  `font-variant-numeric: tabular-nums` on `.counter/.mega/.billrow/.head2/.huge`.
  Six-figure Hindi numbers now group as `1,24,564`; counters no longer shimmy.
- **NEW: dead-air fix** — measured on the shipped render, `s2` was **79% frozen**
  and `s7` held **7.5s motionless** at the count-up payoff, because photo-free
  scenes drop `.bg` and therefore get no `ken()` zoom. Added a `drift()` helper
  (slow continuous scale, `ease:"none"`) applied to every photo-free scene's
  `.stack`. Becomes a `format.json` rule: **no scene may hold a static frame
  beyond ~2s.**

### ⚠️ T3 CORRECTED — the specified font fix was wrong

`design-techtooltester.md` specifies **Archivo Black**, and both the design review
and this spec recommended self-hosting it. Verified with fontTools against the
local `ArchivoBlack-Regular.woff2` (220 glyphs):

| glyph | Archivo Black | Noto Sans Bold (system) |
|---|---|---|
| `₹` U+20B9 | **NO** | YES |
| `→` U+2192 | **NO** | **NO** |
| `$` `·` `—` | YES | YES |

The Hindi cut uses `₹` 10× and `→` 6×; the English uses `→` 9×. Self-hosting
Archivo Black would have **broken the rupee sign in the hero number of the Hindi
channel** — strictly worse than today's fallback. No font on this machine covers
the format's glyph set at display weight (the only ₹-carrying faces are Spectral
at weight 400-500, a serif).

**T3 is reopened as a creator decision**, since the typeface defines how every
future video looks. Options: (a) download a real Black-weight face with ₹ and →
coverage (Noto Sans variable to 900, Archivo variable, Manrope ExtraBold);
(b) self-host Noto Sans Bold for a real 700 instead of synthetic 900-on-400 and
let `→` keep falling back as it does today; (c) replace `→` with a CSS-drawn
arrow, which removes the constraint entirely.

Until resolved, the system stack stays — it is the only configuration verified to
render every glyph the format uses.

### Live confirmation of D-2

`npm run check` on both cuts reports exactly one warning: `#s3stamp` at 1.7:1
(hi) / 1.61:1 (en). `storyboard-hi.md:267` says *"Do not 'fix' it by lightening
the text."* An agent instructed to "fix until clean" would degrade the signature
stamp on every future video. `known_benign` in `format.json` is load-bearing.

---

## T3 RESOLVED 2026-07-28 — self-hosted variable face + CSS-drawn glyphs

Creator chose (c)+(a): remove the arrow dependency, then pick on looks.

**Font.** `studio/library/fonts/NotoSansFinance-var.woff2` — Noto Sans variable,
subset to the Latin + punctuation + currency the format actually uses, width axis
pinned, **weight axis kept at 100-900**. 32 KB. Carries `₹` U+20B9. Wired into both
cuts as `@font-face { font-family: "FinanceSans"; font-weight: 100 900 }` with
`--font: "FinanceSans", system-ui, sans-serif`.

This replaces synthetic bold on a 400-weight fallback with a **real 900**, and it
removes the last render-time dependency on installed system fonts.

**Glyphs.** `→` U+2192 and `▶` U+25B6 are absent from the subset (and from Archivo
Black, and from system Noto Sans Bold). Rather than carry a fallback chain, both
are now drawn in CSS — `.arrow`/`.arr` (shaft + rotated-border head) and `.tri`
(border triangle), all em-based so they scale with the host element's font-size.
Verified by snapshot at t=152.5s and t=176.5s: both render cleanly.

**Unexpected win:** contrast went from `✗ #s3stamp 1.7:1` to **41/41 text checks
pass WCAG AA**. The warning was not purely a checker artifact — real 900 strokes
clear the threshold that faux-bold-on-400 could not. `known_benign` is still worth
having, but this specific entry is no longer needed.

**Verification:** `npm run check` passes on both cuts, 0 errors, 0 warnings beyond
the pre-existing `.grain` / `.bg`-bleed infos.

### Live defect found while verifying (not fixed — already published)

The t=152.5s frame of the shipped Hindi cut shows `s8` sitting on a **phone-screen
photo, upside down, with the carrier string `MTN-SA` legible**. This is verbatim
the trap in `knowledge/stock-photo-sourcing.md`: *"Never use a phone-screen photo
as a background — the screen is someone else's brand, and it's the brightest thing
in frame."* The note records this shipping twice undetected; it is now three.
`s9` additionally rests the whole recap on an identifiable person's face while the
VO discusses wasted money — the license concern in R-8.

Not corrected here: that video is uploaded and scheduled. It is evidence for why
`fin-assets` needs the trap list enforced, not a change to make now.

---

## GSTACK REVIEW REPORT

| Review | Trigger | Why | Runs | Status | Findings |
|--------|---------|-----|------|--------|----------|
| CEO Review | `/plan-ceo-review` | Scope & strategy | 1 | issues_open | 5 proposals, 4 accepted, 2 deferred; 6 critical gaps |
| Design Review | `/plan-design-review` | UI/UX gaps | 1 | issues_open | score 3/10 → 8/10, 13 decisions |
| Eng Review | `/plan-eng-review` | Architecture & tests (required) | 1 | issues_open | 12 issues, 5 critical gaps |
| DX Review | `/plan-devex-review` | Developer experience gaps | 1 | issues_open | score 3/10 → 8/10, TTHW 4-6h → 2h |
| Outside Voice | `/codex review` | Independent 2nd opinion | 4 | issues_found | codex+subagent, 24/24 consensus dimensions confirmed |

- **CROSS-MODEL:** four phases, eight independent voices, 24/24 consensus dimensions CONFIRMED with zero disagreements. Two model claims were checked and **refuted** by direct inspection (P3 "no channel exists" — two live channels supplied by the creator; "API keys empty" — both populated).
- **VERDICT:** CEO + DESIGN + ENG + DX reviewed. Plan is **approved with 27 tasks**, 24 of them blocking or same-branch. Not ready to implement until Group 0-3 land — the reference implementation those agents would copy is itself non-deterministic.

**UNRESOLVED DECISIONS:**
- E-11: four of the eleven agents (`fin-voice`, the timing half of `fin-build`, `fin-render`, `fin-archive`) contain no judgment and both eng voices recommend making them scripts. This contradicts the creator's approved "eleven agents" decision and is surfaced, not applied.
