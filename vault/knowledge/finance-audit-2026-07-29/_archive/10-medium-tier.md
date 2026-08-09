# What 8:30 actually costs — MEDIUM tier for /finance-video

Read-only investigation, 2026-07-30. Every number is tagged **FACT** (measured from an
artifact on disk, or read from code) or **ESTIMATE** (extrapolated). No file in the repo
was modified; no render, encode or paid API was run. `ffprobe` was run on existing
masters; `pipeline_check.py check build` was run (read-only) against a shipped cut.

---

## 1. The reference architecture — what `per-line-chapters` actually is

**FACT.** `studio/videos/firaun-ka-anjaam/build.py` (648 lines) is a **per-chapter
generator, not a long-composition generator**:

```
python3 build.py --chapter 1     # emits index.html for chapter 1 only, clock from 0
```

- `CHAPTERS` (build.py:41–46) maps 10 chapter numbers → segment id sets. `--chapter N` is
  mandatory (`raise SystemExit` if absent or unknown, build.py:266–268).
- Each invocation **overwrites the single `index.html`** with that chapter's scenes only,
  laid out on its own clock from 0 (`scenes, audio, held, t = [], [], [], 0.0`, line 292).
- `scenes[0]["trans"] = "NONE"` — "standalone chapter: hard in" (line 373). Chapter
  boundaries are deliberate hard cuts.
- One scene per VO **line**, where a line is one spoken sentence/clause (~2–8 s):
  307 lines → 307 scenes → 23:05 runtime (docstring + `vault/skills/hyperframes_production.md`
  §5b).
- Each chapter is rendered to its own file: `renders/ch{1..10}-draft.mp4`
  (**FACT**, 14 files on disk; ch3-hookfix = 115.73 s / 3,471 frames / 64 MB;
  ch6-draft = 181.14 s / 116 MB).
- The composition currently on disk is one chapter: **28 `<section>` elements, root
  `data-duration="137.61"`, 27 KB of HTML** (FACT). *A 28-scene single composition is
  already a proven, rendered artifact in this repo.*

**Where the concat happens: outside the renderer, at the very end, by ffmpeg.**
`vault/skills/hyperframes_production.md` §5c (creator rule 2026-07-18):

1. build chapter N → draft-render just it (~3–7 min vs ~55 min for a full timeline)
2. creator proof-**watches** that chapter → a fix is one number + one cheap re-render
3. once ALL chapters are locked → **ffmpeg concat, stream-copy** + a music/SFX mix pass
   (`assemble.py` pattern) → one final-quality encode

Corollary recorded in the same section: *"design chapter boundaries as hard cuts (a
cross-chapter dissolve breaks stream-copy concat)"*.

**FACT:** the `assemble.py` that performed the concat lived in the Pompeii studio dir and
is gone (`vault/videos/video-hist-01-pompeii/index.md`: the 10 chapter renders and the
assembly script were deleted at sign-off). **There is no concat tool in `tools/`.** Adopting
`per-line-chapters` for finance means writing it.

**Structural difference vs blockframe-9, in one line:** blockframe-9 is *one composition,
one render, one mp4, 9 scenes each ~18 s*; per-line-chapters is *N compositions, N renders,
N mp4s concatenated, each chapter ~25–30 scenes of ~4.5 s*. The loop it buys is a **human
proof-watch per chapter** — which is precisely the loop finance does not have (gate two is
an automated per-scene frame check by `fin-render`, not a person watching).

**FACT — the flicker fix is the one mechanism worth stealing** (build.py:351–388, and the
creator rule in memory): consecutive scenes sharing the same image are joined by an
*invisible* cut (`sc["trans"] = "CUT"`, overlap 0) and run **one continuous zoom** across
the whole group, because re-dissolving the same picture at a mismatched zoom produces a
luminance dip. `OVERLAP = {"XD": 1.0}` — only real dissolves overlap; CUT/BLK/NONE get 0.
This is what makes N scenes ≠ N images. **It is directly incompatible with the new finance
assertion** (§3 item 3).

---

## 2. Cost of an 8:30 pair vs the known 3:00 pair

### 2.0 The measured baseline (credit-history, shipped 2026-07-29)

| | hi | en | source |
|---|---|---|---|
| Runtime | **177.71 s** container / 177.667 video | **173.25 s** / 173.233 | FACT `ffprobe` |
| Frames | **5,330** | **5,197** | FACT `ffprobe` |
| Video bitrate | **12,412 kb/s** (12,595 overall) | **11,765** (11,949) | FACT `ffprobe` |
| FINAL size | **279,767,597 B (280 MB)** | **258,766,680 B (259 MB)** | FACT |
| PUBLISH size | **279,783,658 B** | **258,787,214 B** | FACT `ffprobe` |
| VO lines | **9** | **9** | FACT `timing.json` |
| VO chars | **2,082** | **2,587** | FACT `timing.json` |
| Mean clip | **18.34 s** / 231 chars | **17.85 s** / 287 chars | FACT `timing.json` |
| Measured c/s | 2082 / 165.04 = **12.61** | 2587 / 160.63 = **16.10** | FACT — format.json's 12.5 / 16.1 are accurate |
| Encode | **21 m 38.5 s** | **16 m 47.9 s** | FACT `logs/fin-render-{hi,en}-2.md` |
| s / frame | **0.2437** | **0.1940** | FACT (derived) |
| Project dir | **1.4 GB** | **1.4 GB** | FACT `du -sh` |

Per-cut disk breakdown (FACT, `du`, hi): `node_modules` 757 MB (tier-independent) ·
`renders` 534 MB · `snapshots` 93 MB · `assets` 12 MB · text ~0.2 MB.
Plus `credit-history-thumbs` 14 MB. **Pair total on disk = 2.81 GB.**

**A note on "lines".** The finance pipeline's "line" is **not** a firaun line. It is an
~18 s paragraph (231–287 chars). One scene per paragraph. This matters for every number
below, and it is the single decision that determines the whole cost profile.

### 2.1 ElevenLabs

Char budget at a target runtime `T` with `n` scenes, from the code
(`batch.py:53–64`, `format.json scene`): each scene = `0.4 lead + clip + 1.0 tail`, so
speech time = `T − 1.4n` and `chars = rate × (T − 1.4n)`.

| | 3:00 pair (FACT) | 8:30 pair, ~18 s scenes (ESTIMATE) | 8:30 pair, firaun granularity (ESTIMATE) |
|---|---|---|---|
| scenes / cut | 9 | **28** (510 − 39.2 = 470.8 s speech) | ~100–113 (~4.5 s lines) |
| hi chars | 2,082 | **5,885** | ~5,300 |
| en chars | 2,587 | **7,580** | ~6,800 |
| pair chars | 4,669 | **13,465 (2.88×)** | ~12,100 |
| **API calls / pair** | **18** | **56** | **200–226** |
| vs cap 30 | ok | **BREAKS** | **BREAKS hard** |

ElevenLabs bills per **character**, so call count is purely this pipeline's own guardrail.
`eleven_multilingual_v2` accepts ~5,000 chars/request, so 231-char lines are nowhere near a
vendor limit.

**Where the cap lives — and it is not a control.** **FACT:**
`max_elevenlabs_calls: 30` appears in exactly one place,
`.claude/commands/finance-video.md:82`, as *prose telling the orchestrator to write the
number into `run.json`*. Enforcement is one more sentence of prose (§3, "before invoking
`fin-voice` or `fin-assets`, check the `budget` block; refuse the stage"). It is **not** in
`tools/format.json`, **not** in `tools/pipeline_check.py`, **not** in `tools/tts/batch.py`
(which loops over `lines.json` unconditionally, batch.py:41–51). Grep confirms: the only
other occurrences are in vault prose. Per the creator's own 2026-07-29 rule ("prose
warnings aren't a control"), this cap is exactly the class of thing that failed for
architecture rotation. **Raise it to 70** (56 + retry headroom) **and move it to
`tools/format.json` `tiers.<tier>.max_elevenlabs_calls`**, where the orchestrator already
reads its other constants.

### 2.2 Images — **this is the binding constraint, and it binds first**

**FACT, measured baseline** (`vault/videos/credit-history/index.md:21–23`):
hi **34 fetches over 4 rounds → 14 accepted** (13 in the shipped manifest, 3 cut-ins
dropped); en **41 fetches over 6 rounds → 11 accepted** (6 cut-ins dropped).
Manifests on disk: hi 13 slots, en 11 slots (FACT).

**FACT, the pool is measurably spent for India**
(`vault/knowledge/finance-audit-2026-07-29/05-visuals.md:91–95`):
pay-yourself-first hi = 3 India signifiers in 9 slots → good-debt hi = 2 in 16 →
credit-history hi = **0 in 13**. The same file measures the alternatives and records the
negative result: *"`@pexels` is a different pool, not a deeper one"*; Unsplash adds a third
shallow pool plus an attribution obligation. AI generation is the audit's own top
recommendation and the creator has declined it.

| | 3:00 (FACT) | 8:30, one image per scene (ESTIMATE) | 8:30, bg reused across non-adjacent scenes (ESTIMATE) |
|---|---|---|---|
| bg slots / cut | 9 | **28** | **14** |
| cut-in slots / cut | 2–4 | ~8 | ~6 |
| total slots / cut | 11–13 | **~36 (2.9×)** | **~20 (1.6×)** |
| fetches / cut | 34–41 | **95–130** | **50–65** |
| retry rounds / cut | 4–6 | **10–16** | **5–8** |

**Say it plainly: at one image per scene, 8:30 does not work on stock.** 36 slots per cut,
72 per pair, against a no-repeat cross-project md5 ledger and a pool that already yielded
**zero** India signifiers at 13 slots. The retry ladder — not the API budget — is what the
last run's own note says cost it, and this triples the ladder.

**The way through, at zero code cost.** The visuals audit's own finding is that after
`grayscale(.32) brightness(.62) contrast(1.05)` + a four-layer scrim + grain, photos are
*"texture, not information"* — a `manometer` and a `pocket watch` sat under credit-history's
VO and nobody objected. So: **let one background serve 2–3 scenes, placed non-adjacently**,
so every scene boundary is still a real image change (the 0.45 s dissolve stays correct, no
flicker, no invisible-cut machinery, no change to `motion.js` or `check_build`). A returning
background under different type and an opposite `ken` direction reads as a callback; it is
strictly less visible than a wrong subject. `check_assets` iterates `manifest.json` names —
two scenes pointing at one `sN.jpg` is one manifest entry and **passes unchanged** (FACT,
pipeline_check.py:246–255).

This is what turns the image cost from 2.9× (fatal) into 1.6× (affordable).

### 2.3 Render / encode time and disk

**Encode.** `npm run render` captures frames *and* encodes; the measured cost is
per-frame and linear. FACT: 0.2437 s/frame (hi), 0.1940 s/frame (en).

| | 3:00 pair (FACT) | 8:30 pair (ESTIMATE) |
|---|---|---|
| frames / cut @30 fps | 5,330 / 5,197 | **15,300** |
| hi encode | **21 m 38.5 s** | **62 min** |
| en encode | **16 m 47.9 s** | **50 min** |
| pair encode | **38 m 26 s** | **112 min (1 h 52 m)** |
| loudnorm (stream-copy) | ~20 s / cut | ~60 s / cut |

The orchestrator's confirm block says "≈36 min of that is ffmpeg" — **FACT, accurate for
SHORT** (38 m 26 s measured). At MEDIUM it is ~3× wrong.

Two recorded render gotchas apply and are already handled: the 10-min single-process ffmpeg
encode timeout (the orchestrator already sets `PRODUCER_ENABLE_CHUNKED_ENCODE=true`; the
ledger also recommends `FFMPEG_ENCODE_TIMEOUT_MS` for long finals — cheap belt, not set),
and orphaned `renders/work-*` scratch dirs (3–4 GB each on a 12-min video) that once caused
ENOSPC at 56%.

**Disk — `tiers.medium.disk_gb_per_pair: 3.0` is not realistic. Neither is `short: 1.0`.**

| | short, claimed | short, MEASURED | medium, claimed | medium, ESTIMATE |
|---|---|---|---|---|
| steady-state pair | 1.0 GB | **2.81 GB** | 3.0 GB | **~5.2 GB** |
| `doctor` demands (2×) | 2.0 GB | — | 6.0 GB | — |
| peak during a render | — | ~4–5 GB | — | **~8 GB** |

MEDIUM per-cut estimate: `node_modules` 757 MB (fixed) + renders 1,533 MB (FINAL+PUBLISH at
2.87× runtime) + snapshots ~290 MB (28 scenes vs 9) + assets ~30 MB ≈ **2.6 GB**, ×2 cuts
≈ 5.2 GB, plus a transient `work-*` of ~2.5–3 GB while each render runs.
`doctor --tier medium` would demand only 6 GB and then permit a run whose peak is ~8 GB —
the exact ENOSPC failure the ledger records. **Set `medium: 6.0` and `short: 3.0`.**
(FACT: the box has 21 GB free of 234 GB, 91% used — a MEDIUM pair fits, but barely, and
only if `work-*` dirs are swept first.)

### 2.4 Wall clock for a full pair

Orchestrator estimate for SHORT: **~2 h–3 h** (FACT, `.claude/commands/finance-video.md:74`),
of which 38 min is measured encode.

| Stage (pair) | SHORT | MEDIUM (ESTIMATE) | why it scales |
|---|---|---|---|
| research + facts | 25–45 m | **50–100 m** | ~3–4× sourced claims; `library.db` has **no finance lane** (fin-research rescued twice, FACT) |
| script ×2 | 15–25 m | **35–50 m** | 2.9× chars |
| audit ×2 | 20–30 m | **45–70 m** | re-fetches every load-bearing source |
| voice ×2 | 5–10 m | **12–20 m** | 56 calls vs 18, 510 s of audio/cut |
| storyboard ×2 | 20–30 m | **50–80 m** | 28 scene DOM + cue tables, + the `-en` divergence list |
| assets ×2 | 60–80 m | **100–140 m** | 20 slots/cut, 5–8 retry rounds |
| build ×2 | 30–45 m | **60–90 m** | 28-scene generator + snapshot pass |
| render gate 2 ×2 | 15–25 m | **40–60 m** | 1 snapshot + 1 vision pass **per scene** → 56 |
| **encode ×2** | **38 m (FACT)** | **112 m** | linear in frames |
| render QA ×2 | 15–25 m | **40–60 m** | whisper over 510 s; blackdetect over 15,300 frames |
| package ×2 + close-out | 30–45 m | **40–60 m** | ~flat (one thumbnail per cut) |
| **serial total** | ~4.5–6 h | **~10–14 h** | |
| **with the §3a pipelining rule** | **2–3 h** | **5–7 h** | model-bound work hides inside machine-bound |
| **machine-bound floor** | ~1.5 h | **~4 h** | encode 112 m + 2 builds + 56 snapshots + 2 whispers + 2 asset stages, all serialized by rule |

---

## 3. What breaks — verified, not assumed

| # | Thing | Verdict | Evidence |
|---|---|---|---|
| 1 | `format.json architectures` rotation vs tier | **BREAKS** | Both entries carry `"tier": "short"`; **`per-line-chapters` is not in the map at all**. `next_architecture()` (pipeline_check.py:360–377) never reads `tier`. At MEDIUM the orchestrator (§2a) writes a *short* architecture into `run.json` for fin-storyboard/fin-build, while fin-script reads `tiers.medium.architecture = "per-line-chapters"`. Two stages get contradictory instructions. |
| 2 | `check_build` `len(scenes) == len(timing.lines)` | **PASSES** at 28 | pipeline_check.py:280–282 — N-agnostic. But it reads exactly one `studio/videos/<slug>-<cut>/index.html`, so any **multi-composition chapter build BREAKS it** (it would see only the last chapter built). |
| 3 | `check_build` transition-overlap assertion | **PASSES** at 28 for one composition with a dissolve at every boundary. **BREAKS** if firaun's same-image invisible-CUT grouping is ported (overlap 0 at those boundaries, vs the asserted 0.45 ± 0.05). **AND it already fails today:** `python3 tools/pipeline_check.py check build --slug credit-history --cut hi` → **exit 1, 8 problems, "overlaps the next by 0.000s"** (measured just now). `build.mjs:16` butt-joins durations *on purpose* — "the linter calls it an overlapping clip". No shipped composition has ever satisfied this assertion; `--from build` on any of the six shipped runs now fails. |
| 4 | `hyperframes` linter vs the required overlap | **DEGRADES** | `build.mjs:11–16` (written by this pipeline) says a **1 ms** start+dur overlap makes the linter report an overlapping clip. The new rule mandates 450 ms × every non-final boundary — 8 at SHORT, **27 at MEDIUM** — while `format.json known_benign` is `[]` and fin-build is told "run `npm run check`; fix until clean". Predictable retry loop, and pressure to do the one thing fin-build is forbidden to do (edit tokens to please the checker). |
| 5 | `check_voice` contiguous `0.4 + clip + 1.0` welding | **PASSES** at 28 paragraph-lines | pipeline_check.py:182–192, ±0.02 s per line and ±0.05 s on the total. **BREAKS the documented MEDIUM architecture**: firaun's tiered gaps (0.20 intra / 0.40 segment / 1.0–3.0 at marked beats) violate the hardcoded weld on nearly every line. Separately, at 4.5 s lines the fixed 1.4 s of lead+tail would make **31% of the video silence**. |
| 6 | `check_render` runtime tolerance | **PASSES** | ±1.0 s absolute (pipeline_check.py:312). Measured drift at 3:00 was **+0.025 s / +0.006 s with zero accumulation** (FACT, milestone note), and the cause is a single 21.3 ms AAC priming frame — constant, not cumulative. Still comfortable at 510 s. |
| 7 | `check_render` new PUBLISH requirement | **PASSES** | `loudnorm.py` stream-copies video (`-c:v copy`), 3 audio passes → ~60 s at 8:30. Cost is **+803 MB per cut** of disk (already counted in §2.3). |
| 8 | `doctor --tier medium` | **DEGRADES** | `need_gb = 2 × disk_gb_per_pair` = 6 GB against a ~8 GB peak. Passes preflight, then risks the ledger's documented ENOSPC-at-56% failure. |
| 9 | `fin-script.md` "Format by tier" | **BREAKS** | Lines 29–34: MEDIUM/LONG → per-line chapters, *"None of the 9-segment constants apply"*, pointing at `firaun-ka-anjaam/build.py` — a **history-channel** design system (Nastaliq, museum/sepia/bw era grades, verse cards, RTL text). It contradicts #1 and #5 and would send a finance script into a build that cannot check. |
| 10 | `fin-storyboard.md` + the template | **DEGRADES** | Agent prose is N-agnostic and §4a already reads the architecture from run.json — good. But there is no MEDIUM shape (chapters, mid-roll beat), the `-en` divergence-list requirement now spans 28 scenes, and `vault/templates/storyboard-template-finance.md:14` still says **"English 15 chars/s"** (format.json is 16.1). |
| 11 | `fin-build.md` | **DEGRADES** | Line 74 hardcodes `sceneTransitions(["s1"…"s9"], S)`. The helper itself is array-driven (`motion.js:168–175`) so it **passes** at any N — one line of doc. Also `ken`'s own comment (motion.js:117): *"on a scene over ~22s consider two opposed half-moves"* — fine at 28×18 s; a 9-scene 8:30 cut would be 55 s/scene and **break visually**. And `tools/scaffold/package.json` declares `"build": "node build.mjs"` while the scaffold ships **no `build.mjs`** — every cut writes its own (credit-history's is 602 lines). |
| 12 | `fin-render.md` | **DEGRADES** | "gate two, the last check before an **~18-minute** encode" — it is ~50–62 min at MEDIUM. Gate two is one snapshot + one vision pass per scene → 28 per cut, now the second-largest model cost after assets. |
| 13 | `fin-package.md` / `check_package` | **PASSES** | `check_package` needs ≥1 thumbnail (pipeline_check.py:329–332); the ONE-per-cut rule satisfies it. **DEGRADES**: no mid-roll/ad-placement instruction — which is the *entire* reason to cross 8:00 — and the "REAL chapter timestamps" requirement now needs ≥3 chapters starting at 0:00. |
| 14 | Orchestrator confirm block + stage counter | **DEGRADES** | Hardcodes `tier SHORT · target 2:45`, `hi ~2,060 · en ~2,656`, `est. TTS chars ~4,500`, `est. wall clock ~2h–3h (≈36 min ffmpeg)`, and `<n>/18`. Cosmetic, but it is the creator's only cost preview and at MEDIUM every figure is ~3× low. |
| 15 | `tiers.medium` shape | **DEGRADES** | No `lines` key (short has `lines: 9`), no `range_seconds`, and `target_seconds` vs short's `default_target_seconds` — nothing reads them, but fin-script's budget formula has no `n` to work from. |
| 16 | `check_assets` | **PASSES** | Manifest-driven, ≥10 KB + a CREDITS line per named file. Non-adjacent background reuse = one entry, two scenes. Unchanged. |
| 17 | `fin-assets.md` contact-sheet flow | **PASSES** mechanically (per-slot, N-agnostic); **DEGRADES** on pool depth — see §2.2, the real constraint. |
| 18 | `budget.max_elevenlabs_calls: 30` | **BREAKS** at 56 | Prose-only; see §2.1. |

---

## 4. Chapters vs scenes — the modelling answer

**Keep 1 VO line = 1 scene = 1 *timing anchor*. Break 1 scene = 1 *image*.**

- **Do not go to firaun granularity.** ~4.5 s lines mean 100+ TTS calls per cut, 31% of the
  runtime as fixed lead/tail silence, and a `check_voice` rewrite to support tiered gaps.
  The current 18 s paragraph-per-scene model is *already* the finance model and it is fine;
  the drift trap the vault warns about (2026-07-22) only bites when **multiple images sit
  under one clip with guessed weights** — blockframe puts exactly one background under one
  clip, and cut-ins fire on whisper-verified keyword cues.
- **28 scenes, ~18 s each.** `timing.json` grows from 9 to 28 entries — same shape, same
  writer (`batch.py`), no schema change. The four timing copies stay derived from it by the
  per-cut `build.mjs`, which already does exactly this
  (`build.mjs:1–3`: *"The four homes of every timing number … are ALL derived here from
  timing.json, so they cannot drift apart"*). `sceneTransitions()` takes an array and is
  N-agnostic (motion.js:168) — **no change**.
- **Chapters exist only as a beat structure in the storyboard**, not as separate
  compositions: 5 chapters × ~5–6 scenes, with a scene boundary landing near 5:00 so a
  mid-roll never cuts mid-sentence. Zero code implications.
- **Images: ~14 uniques serving 28 scenes**, placed so no two adjacent scenes share one.

**Is a 25–30-scene single composition near a browser/render limit? No — and the repo says
so twice.** I grepped the gotcha ledger (`vault/skills/hyperframes_production.md` §6, 28
entries) and the design doc: **there is no recorded scene-count ceiling.** The recorded
render limits are the 10-min single-process ffmpeg encode timeout (already mitigated by
chunked encode), `work-*` scratch disk, `<html dir="rtl">` rendering black, and a CDN gsap
reference blanking frames. Positive evidence in the other direction:

- **FACT:** `firaun-ka-anjaam/index.html` on disk is **28 sections / 137.61 s / 27 KB**, and
  its chapter renders (115–181 s, 64–166 MB) exist. A 28-scene composition renders.
- **FACT:** Pompeii's full-timeline build was **one composition, 19:55, 35,873 frames**,
  rendered in ~55 min draft (`vault/videos/video-hist-01-pompeii/index.md`).

28 scenes / 15,300 frames sits comfortably inside both.

---

## 5. Recommendation — smallest viable path

### Take **(a) extend blockframe to ~28 scenes in ONE composition**, with two riders

1. Keep the **18 s paragraph-per-scene VO model** — so `check_voice`, `batch.py` and
   `timing.json` are untouched.
2. **Reuse each background across 2–3 non-adjacent scenes** (~14 uniques) — so the image
   pool survives, and `motion.js`, `check_build` and `check_assets` are untouched.

**Reject (b) per-line-chapters + concat.** It needs: a new concat tool (the old
`assemble.py` was deleted), multi-composition awareness in `check_build` *and*
`check_render` (both assume one `index.html` and one `FINAL-*.mp4` whose duration matches
`timing.json total`), per-chapter stage tracking in `run.json`, tiered-gap support in
`check_voice`, and a design-system port from a Nastaliq history build. ~2–3 days. What it
buys is a cheap per-chapter re-render after a **human proof-watch** — a loop finance does
not run. Its one genuine benefit (a fix costs 12 min instead of a 62-min re-encode) is
worth roughly one avoided re-encode per run; gate two's `snapshot --at` catches layout
defects with no render at all.

**(c) 3–4 chapter compositions of ~8 scenes** is the worst of both: it still needs concat
plus multi-composition checks, and its scenes are the same size as (a)'s.

### File-by-file change list

| File | Change |
|---|---|
| `tools/format.json` | `tiers.medium`: `architecture: "blockframe-28"`, `lines: 28`, `range_seconds: [480, 600]`, `default_target_seconds: 510`, **`disk_gb_per_pair: 6.0`**, `max_elevenlabs_calls: 70`; drop the firaun `reference` for finance. `tiers.short`: `disk_gb_per_pair: 3.0` (measured 2.81), `max_elevenlabs_calls: 30`. `architectures`: add `"blockframe-28": {tier: "medium", lines: 28, body_class: "", …}` (and optionally `ledger-rail-28` so MEDIUM has a rotation of two, not one). |
| `tools/pipeline_check.py` | `next_architecture(tier)` — filter `architectures` by `tier`; thread `--tier` through `main()`'s `architecture` mode (~4 lines). Add one assert in `check_voice`: `len(lines) <= tiers[<run tier>].max_elevenlabs_calls` — the cap becomes code, not prose. |
| `.claude/commands/finance-video.md` | Confirm block derives every figure from `format.json` for the chosen tier instead of printing the SHORT constants; init `budget` from `format.json`; `<n>/18` → `<n>/<total>`; per-tier encode estimate; add `FFMPEG_ENCODE_TIMEOUT_MS=3600000` next to `PRODUCER_ENABLE_CHUNKED_ENCODE`; pass `--tier` to the `architecture` command. |
| `.claude/agents/fin-script.md` | Replace "MEDIUM/LONG → per-line chapters (firaun)" with **MEDIUM = blockframe-28**: ~28 paragraph-lines of ~18 s in 5 chapters, budget `rate × (target − 1.4n)`. Keep the firaun pointer for LONG only, flagged as not-yet-supported. |
| `.claude/agents/fin-storyboard.md` | MEDIUM shape: 28 scenes grouped into 5 named chapters (beats, not compositions); a scene boundary near 5:00 for the mid-roll; **declare the background reuse map** (~14 uniques, no two adjacent scenes sharing one). |
| `.claude/agents/fin-build.md` | `sceneTransitions(Object.keys(S), S)` instead of the 9-id literal; `ken` = two opposed half-moves above 22 s; state that the scene array is generated in `build.mjs` from `timing.json`. |
| `tools/scaffold/build.mjs` | **New** — a generic generator (credit-history's 602-line one, minus its video-specific ₹ math), since `scaffold/package.json` already declares `"build": "node build.mjs"` and ships no such file. This is the one piece of real work, and it is what makes 28 scenes tractable *and* kills the "read a previous video's index.html" relapse the 2026-07-29 audit named. |
| `.claude/agents/fin-render.md` | Per-tier encode estimate (~50–62 min at MEDIUM, not "~18-minute"); gate two = 28 frames/cut. |
| `.claude/agents/fin-package.md` | Add mid-roll placement (the reason for 8:00+) and ≥3 chapter timestamps at MEDIUM. |
| `vault/templates/storyboard-template-finance.md` | Rate 16.1 (not 15); MEDIUM header shape. |
| `vault/workflows/finance-video.md` | MEDIUM = blockframe-28, not per-line-chapters; **ONE thumbnail per cut** (still says 3 variants, twice). |
| `vault/knowledge/design-finance-blockframe.md` | New MEDIUM section: 28 scenes, the background-reuse rule, the chapter beat map. |

### Effort, honestly

- format.json + the `pipeline_check` tier filter + the cap assert: **~45 min**.
- The eight agent/doc/vault edits: **~2 h**.
- `tools/scaffold/build.mjs`: **~3 h** (generalise, keep the four-timing-copies contract,
  add the reuse map, leave a `--selftest`-style assert that the four copies agree).
- One `FIN_FAKE_APIS=1 --dry-run` rehearsal + a **draft-quality** render of one cut to
  confirm 28 scenes/27 dissolves survive `npm run check`: **~1 h**.
- **Total ~6–7 h of work before the first real MEDIUM pair** — which then costs ~5–7 h of
  wall clock, ~13,500 TTS chars, ~110 stock fetches and ~5.2 GB.

### Do this before anything else (it is not tier-specific)

`check_build`'s overlap assertion **fails every composition ever shipped** (measured:
credit-history-hi, exit 1, 8 problems). The next build must emit the overlap *and* survive
`hyperframes` lint's overlapping-clip complaint. Prove that on a SHORT cut first — a
28-scene MEDIUM run is the wrong place to discover that the linter and the checker disagree
27 times.

---

## 6. Contradicts what the vault currently documents

1. **`vault/workflows/finance-video.md`** — frontmatter and "What a run produces" both say
   **3 thumbnail variants** (`thumbnail-{hi,en}-v{1..3}.png`). Retired 2026-07-29: ONE per
   cut. Also says MEDIUM/LONG use per-line chapters "a different production architecture" —
   which `format.json architectures` cannot select (§3 item 1).
2. **`vault/templates/storyboard-template-finance.md:14`** — "English **15** chars/s".
   `format.json` is **16.1**, changed because 15.0 budgeted every en script ~7% long.
3. **`vault/knowledge/finance-audit-2026-07-29/02-script.md`** — says the MEDIUM build cost
   is *"already written and proven. ~zero"* and that `max_elevenlabs_calls: 30` is *"the
   single blocking item"*. Both wrong as stated: the firaun build is a per-chapter
   history-design generator whose output fails `check_build` (one `index.html`),
   `check_render` (one `FINAL-*.mp4` matching `timing.json total`) and `check_voice`
   (tiered gaps vs the hardcoded `0.4 + clip + 1.0` weld). Its own "images scale with
   visual beats, not lines" holds *only* via the same-image invisible-CUT grouping, which
   the 2026-07-29 overlap assertion forbids. The call cap is real but it is the **second**
   constraint; the image pool is the first.
4. **`tools/format.json` `tiers.short.disk_gb_per_pair: 1.0`** — measured **2.81 GB** for
   the credit-history pair (2.8× understated). `medium: 3.0` is ~1.7× understated at steady
   state and ~2.7× at peak.
5. **`vault/videos/credit-history/index.md:116`** — "Thumbnails (3 variants per cut)".
   Correct as history, but it is the note `fin-package`'s sameness check reads back; the
   one-thumbnail rule should be stated there so the trail doesn't argue with itself.
6. **`.claude/agents/fin-render.md`** and the orchestrator both quote **"~18-minute
   encode"** — accurate for SHORT (measured 16 m 48 s – 21 m 39 s), ~3× low for MEDIUM.
7. **`tools/scaffold/package.json`** declares `"build": "node build.mjs"`; the scaffold
   ships no `build.mjs`, and `fin-build.md` never mentions one — yet every shipped cut has
   one (credit-history's is 602 lines). The generator is the pipeline's real build step and
   it is undocumented.
