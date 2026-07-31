---
summary: Storyboard for «The First $10,000» en cut — MEDIUM tier, 92 scenes (one VO line = one clip = one scene), swiss-band architecture. Ports the -hi skeleton (ID scheme, DOM, cue ladder, aperture vocabulary) and declares 15 explicit divergences. US colour semantics, one music bed + 23 SFX cues, 100 image slots backed by 93 fetched files.
updated: 2026-07-31
source: script-en.md (fin-script attempt 1) + studio/videos/first-lakh-first-thousand-en/assets/voice/timing.json (measured, 505.561s) + storyboard-hi.md (the ported skeleton) + knowledge/design-finance-blockframe.md + knowledge/finance-audit-2026-07-29/11-swiss-vignelli.md Direction 1 + tools/format.json + tools/audio/kit.json
stage: fin-storyboard, cut en, attempt 1
---

# STORYBOARD — «The First $10,000 Is The Hardest» · **en** cut

**Project:** `studio/videos/first-lakh-first-thousand-en/` · **Script:** `script-en.md`
**Design:** [[../../knowledge/design-finance-blockframe]] (the **dark** system) with the
`.swiss-band` divergences of [[../../knowledge/finance-audit-2026-07-29/11-swiss-vignelli]] §4 D1 + §8.
Do **not** use `design-techtooltester` — that is the bright, non-finance system.
**Channel:** @moneymavens101 $ · **Tier:** MEDIUM, per-line chapters · **Architecture:** `swiss-band` (run.json creator pick, 2026-07-31)
**Runtime:** **505.561s (8:26)** measured — `timing.json` is the only home for every duration.
**VO:** Brian `nPczCjzI2devNBz1zQrb` · **Scenes:** 92 · **Image slots:** 100 (92 bg + 8 mosaic minors), **93 files** fetched.
**Ported from:** `storyboard-hi.md` §3 DOM, §4 cue ladder, `s<n>-<part>` ID scheme, aperture vocabulary. Divergences: §8.

---

## 1. Colour semantics for THIS video (derived from the thesis — mandatory)

The thesis: *the first $10,000 is hard because 100% of it is you; after it, a mechanism
you built starts carrying the load.* Roles are fixed, meanings are per-video.

| Token | This video means | Because |
|---|---|---|
| `--warn` red `#ef4444` | **the stretch nobody helps you with** — the first $10,000, the 12.5 months, the half-month the market buys, the 2.7% national saving rate, six months spent not starting, the one emergency that ends it | the obstacle is not a villain or a leak; it is an interval you cross alone |
| `--fund` green `#22c55e` | **the mechanism that works without you once it exists** — the standing transfer, the escalator, the separate account, the coal bed, the habit; and *only later* the tenth $10,000 | ⚠ green is **NOT** "returns doing the work". It marks the viewer's own behaviour first (4.9, 4.11, 5.10, 7.5, 7.6, 8.2, 8.5, 8.7, 9.2, 9.4). **5.10 exists to deny that returns take over at the first milestone** — reading green as "returns" makes the palette argue against the video |
| `--target` amber `#f59e0b` | **a rate or a threshold under examination** — ~10%/yr, 0.38%, the Fed target range, the ~$96,000 crossover, $100,000, the word CROSSOVER itself, the three open questions | amber is the thing being weighed, never the thing being recommended (persona rule: no product picks, no APY on screen) |
| `--pop` orange `#ff5c39` | the call to action | fixed — **exactly once**, scene 91 (9.9) |

**The inversion trap.** needs-vs-wants ran amber = "wants" and red = "the leak alone".
Neither meaning applies here. Any element rendering the tenth $10,000 in red, or the
first $10,000 in green, argues against the script.

**Swiss constraint on top of the above: ONE role colour visible per scene, ever**
(11-swiss-vignelli §5.1). Colour appears as a **filled square module or a rule**, never
as coloured text on the photograph and never as a rounded pill. Per-scene `--tint` is
**retired** in `.swiss-band` — a 0.10–0.13 alpha wash is pictorial colour, the one use
Vignelli names as wrong (Canon p.78). There is no `tint` column in this storyboard, on purpose.

Scene colour counts: **17 warn · 15 fund · 10 target · 1 pop · 49 uncoloured.** Uncoloured
is the majority and is correct: a signifier used on half the frames signifies nothing.

---

## 2. Audio — one bed, 23 cues

**Music bed: `bed-resolve`.** The argument of this video is a **habit / a fix**, not a trap
or a cost: it ends on one automatic transfer and a mechanism that keeps running. Chapters
2–4 and 6 have a cost *register*, but the thesis they serve is constructive, and the bed is
chosen for the video, not for a chapter. (Same bed as the hi cut — this is one video in two
markets, and the bed is not a variance axis.)

> ⚠ **Loop hazard — WORSE HERE THAN ON THE HI CUT. Load-bearing for fin-build.**
> `bed-resolve` is **248s** on disk (`kit.json _music_on_disk`); this cut is **505.561s**.
> `mix.py` stream-loops and both beds fade in from / out to silence, so an audible dip to
> silence lands at **≈248s** (the s46/s47 boundary — on `~$100,000`, the video's real turn)
> and **≈496s** (the s90/s91 boundary — **on the CTA itself**). The hi cut's second dip at
> least landed mid-recap; this one lands on the one `--pop` block in the video, which is the
> single worst frame in the cut to go silent. Fix before mixing: trim the head/tail silence
> off `bed-resolve.mp3` and crossfade the loop point, or source a ≥520s bed and re-normalise
> it through the same two-pass loudnorm to −20 LUFS (mix.py's 0.16 gain and 6 dB duck are
> calibrated against that figure). Do **not** run `sfx.py --kit --music --force` — it would
> destroy the creator-supplied beds, which are not regenerable and live only in gitignored
> `studio/`.

**SFX budget: 23 cues across 8:26** — one per ~22s. The kit's stated ceiling (≤10) is a
**SHORT-cut** figure; scaling it by runtime would give ~56, which is exactly the "every
reveal has one, so none of them means anything" failure. 23 is a deliberate ceiling, not a
derivation — the hi cut's 22 plus **one**, because the BEA 2.7% beat (4.6) is the strongest
US-only number in the packet and has no hi counterpart. **No two cues inside 0.8s** —
verified below; the closest pair is **2.84s**.

| # | scene | line | sound | helper | absolute t | f | why this beat |
|---|---|---|---|---|---|---|---|
| 1 | s1 | 1.1 | `hero` | the big number | **3.36** | 0.70 | `12.5 MONTHS` lands on "twelve and a half" — frame-one figure |
| 2 | s2 | 1.2 | `hero` | the big number | **9.47** | 0.88 | `6 MONTHS` — the pair IS the video; both get the impact |
| 3 | s16 | 2.6 | `hero` | the big number | **84.72** | 0.84 | `½ MONTH` — what the best long-run return in the country bought |
| 4 | s19 | 2.9 | `stamp` | verdict module | **100.87** | 0.69 | `100% savings · 0% returns` — the thesis stated |
| 5 | s28 | 3.8 | `hero` | the big number | **151.73** | 0.83 | `6½ MONTHS` — the other half of the thesis |
| 6 | s29 | 3.9 | `stamp` | verdict module | **157.44** | 0.74 | "That is the whole video" |
| 7 | s36 | 4.6 | `hero` | the big number | **194.21** | 0.44 | `2.7%` — the published national rate, the one HARD US number |
| 8 | s39 | 4.9 | `reveal` | rise | **213.10** | 0.77 | "Not the return rate. The savings rate." |
| 9 | s44 | 5.3 | `reveal` | rise | **235.50** | 0.55 | the word CROSSOVER arrives |
| 10 | s47 | 5.6 | `hero` | the big number | **249.97** | 0.16 | `~$100,000` — where the arithmetic actually turns |
| 11 | s50→s51 | 5.9→5.10 | `transition` | shove | **272.49** | fixed | **SHOVE #1** — the turn from "not interest" to "the habit" |
| 12 | s51 | 5.10 | `stamp` | verdict module | **277.05** | 0.77 | "the HABIT takes over" (4.56s after cue 11 ✓) |
| 13 | s57 | 6.5 | `hero` | the big number | **309.16** | 0.50 | `$800` — the one input every figure in the video runs on |
| 14 | s62→s63 | 6.10→7.1 | `transition` | shove | **340.71** | fixed | **SHOVE #2** — into the fire-pit re-frame (~67% mark) |
| 15 | s68 | 7.6 | `reveal` | rise | **367.33** | 0.51 | "The same log. Far more heat." |
| 16 | s69 | 7.7 | `stamp` | verdict module | **375.99** | 0.79 | "long AFTER the first armful" |
| 17 | s71 | 8.1 | `tick` | pulse | **385.98** | 0.46 | "Three things" — opens the three-rung set |
| 18 | s72 | 8.2 | `chip` | pop | **389.19** | 0.04 | rung ONE |
| 19 | s74 | 8.4 | `chip` | pop | **400.71** | 0.04 | rung TWO |
| 20 | s77 | 8.7 | `chip` | pop | **416.51** | 0.04 | rung THREE — the three `chip`s are one set, which is why repeating is legible here and nowhere else |
| 21 | s82 | 8.12 | `stamp` | verdict module | **449.85** | 0.84 | "It dies from one emergency." |
| 22 | s90 | 9.8 | `reveal` | rise | **493.85** | 0.64 | the closing statement |
| 23 | s91 | 9.9 | `cta` | closing block | **496.69** | 0.05 | the single `--pop` block |

`f` is the fallback fraction: absolute t = `audio_start + f × duration`. Per script handoff
§10, fin-build resolves each anchored cue against **faster-whisper word timings** and uses
`f` only if the word fails to align.

**In `.swiss-band` the `chip` sound is not bound to a `.chip` component** — there are no
chip rows in this architecture (11-swiss-vignelli §7 bans them). The three rungs are three
whole scenes, and `chip` fires on the rung scene's `bar` hang, on the enumerating word
("One:", "Two:", "Three:"). The helper binding (`pop`) is unchanged; only the host element is.

**Declared DRY beats** (silence is the choice, not an omission):
- **1.3–1.10** — after the two hero hits the hook runs dry; the three questions land on voice alone.
- **2.1–2.5, 2.7–2.8, 2.10** — the arithmetic chapter. A sound on every step turns a sum into a game show.
- **All of chapter 3 except 3.8 / 3.9** — the sum builds in silence so its payoff pair lands.
- **All of chapter 4 except 4.6 / 4.9** — the accusation chapter. Punctuating "tabs open, comparisons printed, nothing opened" would make it a joke instead of an indictment.
- **5.7–5.9 — the Munger block is DRY on purpose.** The quote is *colour, not evidence*: 5.5 reaches ~$96,000 without it. A `stamp` under a folk attribution with no reachable primary would sell it as proof.
- **All of chapter 6 except 6.5** — the honesty chapter (BLS $1,251/wk, the SHED $400, "then the first $10,000 is further away"). Punctuating a hard truth reads as showmanship.
- **7.1–7.5** — the fire-pit analogy is built in silence so 7.6 / 7.7 can land.
- **9.1–9.7, the whole action block and recap** — dry, so the `cta` at 496.69 is the first sound in **44 seconds**.

**Mixed in post, never in the composition.** `assets/audio.json` cue list → `tools/audio/mix.py`
(sidechain duck) → `tools/loudnorm.py` to −14 LUFS. The composition stays voice-only: one
`<audio>` row per line, track index 10.

---

## 3. The `.swiss-band` frame — DOM and the aperture

**Ported verbatim from `storyboard-hi.md` §3.** A fix made to this DOM travels to both cuts.

`<div id="root" class="swiss-band">`. Grid 12 × 8 on 1920 × 1080: side margins 100px,
column 125px, gutter 20px (col *n* left edge `x = 100 + (n−1)×145`); top/bottom trim 60px,
row pitch 120px (row *m* top `y = 60 + (m−1)×120`).

### Per-scene DOM (identical every scene — the aperture IS the identity)

```html
<section class="scene" id="s12" data-track-index="2" data-duration="…">
  <div class="titlebar">                        <!-- row 1: x 0→1920, y 60→180, solid --bg -->
    <h2  id="s12-bar">…</h2>                    <!-- 84px/800, tracking -1, --ink, x=100, hung 26px below bar top -->
    <span id="s12-mark">$ · CH 2</span>         <!-- 26px/200 --muted, uppercase, tracking +4, flush right x=1820 -->
  </div>
  <div class="band" id="s12-band">              <!-- rows 2–6: x 0→1920, y 180→780, 1920×600, 3.2:1 -->
    <div class="bandimg" id="s12-img"></div>    <!-- background-image: assets/img/s12.jpg, cover -->
    <div class="minor"  id="s12-min"></div>     <!-- MOSAIC scenes only -->
    <div class="tone"   id="s12-tone"></div>    <!-- REVERSED scenes only: hard-edged rgba(13,16,23,.74), cols 1–6 -->
  </div>
  <hr class="rule" id="s12-rule">               <!-- 3px --ink, x 100→1820, y=780 -->
  <p  class="stmt" id="s12-stmt">…</p>          <!-- 54px/500, x=100, top y=812, ≤3 lines, measure cols 1–9 (x 100→1405) -->
  <p  class="num"  id="s12-num">…</p>           <!-- OR: 200px/900 tabular, same hang point; currency mark 0.5em/400 -->
  <p  class="foot" id="s12-foot">…</p>          <!-- 26px/200 --muted, x=100, y=1020 -->
  <span class="idx" id="s12-idx">12 / 92</span> <!-- 26px/200 --muted tabular, flush right x=1820, y=1020 -->
</section>
```

**ID scheme: `s<n>-<part>`, n = 1…92 in script order.** Identical to the hi cut's scheme;
only the range and the `mark` / `idx` strings differ (`$` not `₹`, `/ 92` not `/ 86`).
Line-id ↔ index mapping is the `#`/`line` columns of §6.

**Numerals:** `Intl.NumberFormat("en-US")` — `$100,000`, `$1,251`, `$9,600`. The hi cut's
`en-IN` grouping (`1,00,000`) is **wrong here** and a plain `\B(?=(\d{3})+(?!\d))` regex is
correct for this cut only. `tabular-nums` on `.num`, `.stmt`, `.foot`.

**Copy is NOT restated here.** `bar:`, `stmt:`/`num:` and `foot:` strings live in the
script's `[ap …]` cue block for each line and have exactly one home. This storyboard owns
the DOM, the cues, the transitions, the audio and the images.

### Load-bearing divergences from `design-finance-blockframe.md` (11-swiss-vignelli §8)

Identical to the hi cut. Restated because fin-build reads one storyboard, not both.

| Blockframe rule | `.swiss-band` |
|---|---|
| four-layer radial scrim | **deleted** — hard-edged tone block on a column line, on `R` scenes only |
| grade `grayscale(.32) brightness(.62)` | `grayscale(.85) brightness(.55) contrast(1.25)` — photo as tonal mass, not a window |
| per-scene `--tint` | **retired** (§1) |
| `text-shadow` on every text class | **off** — contrast is geometric |
| radii (chip 999px, cta 14px…) / rotation (`.stamp` −4°) | **all → 0**. `.stamp` becomes a filled grid module |
| 16-size ladder used freely | **two sizes per scene** + the 26px foot as the permitted third. Weight (900/800/500/200) carries hierarchy, not size |
| centred stack | flush left, ragged right, everywhere |
| `back.out(1.7)`, `breathe`, `drift` | unused. `power2/3/4.out` and `expo.out` only |
| ken `1.0↔1.16` | half amplitude `1.0↔1.06`, `xPercent ∓1.2` inside the band; **full** amplitude on `R` (full-bleed) and `C` (tall block) apertures |
| `dissolve` 0.45s | **hard directional wipe, 0.45s** — same duration, so the scene arithmetic and the cut-detector argument both hold. ⚠ **still unproven**: re-measure with `ffmpeg scdet` on chapter 1's master before locking (§10) |
| "no scene may hold a **static photo** beyond ~2s" | restated: **no frame may be motionless beyond ~2s**. Rules, blocks and apertures can carry the motion; the photo need not |

**Element budget.** `mark` and `idx` are **furniture** — identical, muted, weight 200, in
every frame; they are the aperture, not content. Content elements per scene: `bar`, `rule`,
focal (`stmt` **or** `num` — never both, blockframe §5 rule 4 survives), `foot`, plus the
mosaic `minor`. **Max 5 content elements**, against the format.json ceiling of 6. ✓
**Chips: zero** — banned in `.swiss` — so `max_chips_per_row` 3 / `max_chip_chars` 22 are
satisfied vacuously, not by luck.

---

## 4. The cue ladder — one canonical assembly, declared as a cascade

**Ported verbatim from `storyboard-hi.md` §4.** Every scene animates identically. Offsets
are **relative to `scene_start`** (§6 column `start`, verbatim from `timing.json`), so every
absolute cue time is `scene_start + offset` and is derived, never hand-typed.

| # | element | offset | class | helper | spec |
|---|---|---|---|---|---|
| 1 | `s<n>-band` | **+0.00** | fixed | `bandOpen` | `clip-path: inset(50% 0 50% 0)` → `inset(0)`, 0.60s `power4.out` — the aperture irises open |
| 2 | `s<n>-bar` | **+0.15** | fixed | `hang16` | rise **16px** only, 0.45s `expo.out` (Unigrid: type hangs from the bar) |
| 3 | `s<n>-rule` | **+0.55** | fixed | `ruleDraw` | `scaleX 0→1`, `transform-origin: left`, 0.45s `power2.out` — the gesture of ruling a line |
| 4 | focal | **+0.70** *(stmt)* / **anchored** *(num)* | see below | `hang12` / `scaleArrive` | statement hangs 12px, 0.40s `expo.out` |
| 5 | `s<n>-foot` | **+1.10** | fixed | `fade` | opacity only, 0.40s `power1.out` |
| — | `s<n>-img` | **+0.00 → scene end** | anchored | `ken` | half amp in `B`/`M`, full in `R`/`C`; direction alternates by scene parity (odd `in`, even `out`) |
| — | `s<n>-tone` | **+0.05** | fixed | `wipeX` | `R` scenes only, 0.50s `power4.out`, hard edge on the col-7 line |
| — | `s<n>-min` | **+0.85** | fixed | `wipeY` | `M` scenes only, hard wipe along its long axis |

> **Declared cascade — "the assembly".** Items 1–5 are **one gesture** (aperture → bar →
> rule → type → source), not five independent reveals, and they run at 0.15/0.40/0.15/0.40s
> gaps. This is **below** `format.json layout.cue_min_gap_seconds` 0.8 and below
> `layout.cascade.gap_seconds` 0.6–0.7, and it is declared here so the audit reads it as a
> decision rather than drift. It obeys `cascade.max_items` **5** exactly. Justification: the
> Unigrid frame assembles as a unit; spacing its parts 0.8s apart would spend 4s of a 5.5s
> average scene building furniture. Every *content* cue that is not part of the assembly
> (the anchored `num`, the `stamp` module, the SFX-bearing beats) keeps the ≥0.8s rule — the
> closest such pair in the whole cut is **2.84s**.
>
> `layout.first_cue_by_seconds` 0.5 ✓ — the band opens at +0.00 in every one of the 92 scenes.

**Anchored vs fixed.** Items 1, 2, 3, 5 and the tone/minor wipes are **fixed**: constant
regardless of clip length. The `ken` push and the `num`/`stamp` arrivals are **anchored**:
they land on a word and scale with the clip. **Surplus time from a longer clip goes into the
hold after the assembly — never into the cascade.** Concretely: the assembly always finishes
at +1.50s; the longest scene (s69, 8.14s) holds a finished frame for 6.6s with only the ken
push running, and that is correct.

**The 19 `num` scenes take an anchored arrival instead of the +0.70 fixed hang** — putting
the figure on screen 4s before the voice says it spoils the hook. `stmt` scenes keep the
fixed +0.70 because a statement paraphrases the whole line and cannot spoil it.
`num` scenes: **s1 s2 s12 s13 s15 s16 s25 s26 s28 s33 s36 s37 s44 s46 s47 s54 s57 s78 s91.**

**Track index alternates 1 / 2 by scene parity** (odd → 1, even → 2), because
`hyperframes check` rejects two overlapping clips on one track and every non-final scene
overlaps its successor by 0.45s.

**`data-duration` = `timing.json` `scene_duration` + 0.45** on scenes 1–91; s92 carries its
`scene_duration` bare. Root duration is unaffected: **505.561s**.

**Headroom note (better than the hi cut).** `scene.max_scene_seconds` is 9.0. The longest
scene here is **s69 at 8.140s → 8.590s with the transition**, so this cut passes whether
`check_build` measures `scene_duration` or `data-duration`. The hi cut needed that ambiguity
resolved (its s16 reads 9.191s as `data-duration`); this cut does not depend on the outcome.

---

## 5. The aperture programme (the anti-sameness engine — mandatory)

Canon p.84: a declared *cycle* of apertures, never one frame repeated. Four apertures,
one grid, one type system, one motion vocabulary.

| ap | aperture | count | where |
|---|---|---|---|
| **B** | BAND (D1) — 1920×600 full-bleed band, rows 2–6 | **57** | the default, 62% of scenes |
| **C-R / C-L** | COLUMN (D2) — 950×1080 photo block, cols 7–12 (R) or `x 0→950` (L); type in the complementary columns | **18** | one scene in every five, alternating side |
| **R** | REVERSED FIELD (D4) — full bleed, type reversed on a hard-edged tone block | **9** | the hardest-milestone line (1.5), the thesis (2.9), the sentence the video is named for (3.8), the only-thing-that-moved line (4.9), the real turn (5.6), the habit correction (5.10), the coal bed (7.6), how it actually breaks (8.12), the closing statement (9.8) |
| **M** | MOSAIC (D3) — major photo rectangle + minor rectangle carrying the second figure | **8** | every two-figure comparison: 1.3, 2.6, 3.2, 3.9, 4.8, 5.5, 6.7, 9.6 |

57 + 18 + 9 + 8 = 92 ✓

**Cycle offset: this cut opens on `B`; its first `R` is scene 5.** The hi cut opens on `R` at
scene 1. The two sequences are not synchronised at any structural landmark: hi runs
56/13/10/7 over 86 scenes, en runs 57/18/9/8 over 92. Do not "harmonise" them — a pair that
lands on the same aperture at the same index reads as one template with the language swapped,
which is the exact failure the sequence layer exists to prevent (11-swiss-vignelli §7).

### Zero corrections to the script's `ap` column — stated so the audit does not hunt for one

The hi cut needed two (a broken C-R/C-L alternation and two prose/table count mismatches).
This script has neither. Verified at this stage:

1. **The column alternation is clean.** All 18 `C` scenes in script order run
   `R L R L R L R L R L R L R L R L R L`, starting `C-R` exactly as the script's own rule
   states: 1.4·1.8·2.2·2.10·3.4·3.10·4.3·4.7·4.11·5.4·5.9·6.3·6.9·7.3·8.2·8.7·8.11·9.2.
2. **The script's prose counts match its own table.** Prose says "exactly 9" reversed-field
   and "the 8 scenes" mosaic; the table lists 9 and 8. ✓
3. **Band count derives, it does not need declaring:** 92 − 9 − 8 − 18 = 57, and the script
   says 57. ✓

---

## 6. Scenes

One row per VO line. `start` = `scene_start`, verbatim from `timing.json` (the only home);
every fixed cue is `start + offset` from §4. `focal` names which of `stmt`/`num` carries the
frame and its single role colour. Copy lives in the script.

**Legend.** ken: `i` = in, `o` = out (parity-alternating) · trk = `data-track-index` ·
trans: `wipe` = the 0.45s hard directional wipe (the `dissolve` slot), `SHOVE` = a real turn
in the argument, `hold` = matched-frame boundary inside the continuous-zoom pair (§7).

| # | line | start | ap | ken | trk | trans | focal | bg file — search subject | minor | anchored cue · SFX |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1.1 | 0.000 | B | i | 1 | wipe | num · warn | `s1.jpg` — enamel mug, coins and bills, counter | — | num "twelve and a half" **3.36** · `hero` |
| 2 | 1.2 | 5.241 | B | o | 2 | wipe | num · fund | `s2.jpg` — glass jar full of bills and coins | — | num "six months" **9.47** · `hero` |
| 3 | 1.3 | 10.586 | M | i | 1 | wipe | stmt · warn | `s3.jpg` — two iron weights on a scale | `s3m.jpg` — folded pay stub | — |
| 4 | 1.4 | 16.637 | C-R | o | 2 | wipe | stmt | `s4.jpg` — two binders on a shelf, spines to camera | — | — |
| 5 | 1.5 | 23.288 | **R** | i | 1 | wipe | stmt · warn | `s5.jpg` — coin standing on edge, dark wood, raking light | — | — |
| 6 | 1.6 | 28.869 | B | o | 2 | wipe | stmt | `s6.jpg` — hand-crank drill on a workbench | — | — |
| 7 | 1.7 | 32.176 | B | i | 1 | wipe | stmt · target | `s7.jpg` — three sealed envelopes on a blotter | — | — |
| 8 | 1.8 | 37.391 | C-L | o | 2 | wipe | stmt · target | `s8.jpg` — printed rate sheet, macro | — | — |
| 9 | 1.9 | 41.796 | B | i | 1 | wipe | stmt · target | `s9.jpg` — empty lunch container, break room | — | — |
| 10 | 1.10 | 46.854 | B | o | 2 | wipe | stmt | `s10.jpg` — longhand arithmetic, legal pad, pencil | — | — |
| 11 | 2.1 | 52.251 | B | i | 1 | wipe | stmt | `s11.jpg` — paper pay stub folded on a table | — | — |
| 12 | 2.2 | 57.649 | C-R | o | 2 | wipe | num | `s12.jpg` — twelve coin stacks in a row, dark | — | num "ninety-six hundred" **58.63** |
| 13 | 2.3 | 62.811 | B | i | 1 | wipe | num · warn | `s13.jpg` — wall calendar, months crossed off | — | num "twelve and a half" **66.11** |
| 14 | 2.4 | 67.974 | B | o | 2 | wipe | stmt · target | `s14.jpg` — newspaper markets page, macro, folded | — | — |
| 15 | 2.5 | 75.304 | B | i | 1 | wipe | num | `s15.jpg` — calendar page torn free, falling | — | num "twelve" **77.55** |
| 16 | 2.6 | 78.456 | M | o | 2 | wipe | num · warn | `s16.jpg` — hourglass, sand at the neck, macro | *recalls* `s15.jpg` | num "half a month" **84.72** · `hero` |
| 17 | 2.7 | 86.387 | B | i | 1 | wipe | stmt | `s17.jpg` — empty white plate, bare table, raking light | — | — |
| 18 | 2.8 | 91.367 | B | o | 2 | wipe | stmt | `s18.jpg` — printed spreadsheet, cells circled in pen | — | — |
| 19 | 2.9 | 96.842 | **R** | i | 1 | wipe | stmt · warn | `s19.jpg` — hand dropping bills into a steel cash box | — | stamp module **100.87** · `stamp` |
| 20 | 2.10 | 103.102 | C-L | o | 2 | wipe | stmt | `s20.jpg` — rack of blank forms, no signage | — | — |
| 21 | 3.1 | 108.630 | B | i | 1 | wipe | stmt | `s21.jpg` — adding-machine tape running off a desk | — | — |
| 22 | 3.2 | 114.341 | M | o | 2 | wipe | stmt | `s22.jpg` — two glass jars, the second fuller | `s22m.jpg` — printed rate card, macro | — |
| 23 | 3.3 | 120.758 | B | i | 1 | wipe | stmt | `s23.jpg` — two nails of different height in a plank | — | — |
| 24 | 3.4 | 124.718 | C-R | o | 2 | wipe | stmt | `s24.jpg` — toolbox, lid propped open, compartments full | — | — |
| 25 | 3.5 | 129.959 | B | i | 1 | wipe | num · warn | `s25.jpg` — parked handcart, loading dock, long shadow | — | num "twelve and a half" **131.83** |
| 26 | 3.6 | 135.801 | B | o | 2 | wipe | num · fund | `s26.jpg` — station platform clock, hands mid-sweep | — | num "six months" **139.84** |
| 27 | 3.7 | 141.042 | B | i | 1 | wipe | stmt | `s27.jpg` — a wide sail catching wind, low angle | — | — |
| 28 | 3.8 | 146.622 | **R** | o | 2 | wipe | num · fund | `s28.jpg` — two coiled mooring ropes, one small one huge | — | num "six and a half" **151.73** · `hero` |
| 29 | 3.9 | 153.300 | M | i | 1 | wipe | stmt | `s29.jpg` — page torn from a bound book, gap visible | *recalls* `s28.jpg` | stamp module **157.44** · `stamp` |
| 30 | 3.10 | 159.350 | C-L | o | 2 | wipe | stmt | `s30.jpg` — stack of unopened mail on a hall table | — | — |
| 31 | 4.1 | 163.337 | B | i | 1 | wipe | stmt | `s31.jpg` — printed comparison sheets spread on a couch | — | — |
| 32 | 4.2 | 168.317 | B | o | 2 | wipe | stmt | `s32.jpg` — closed laptop on printouts, cold coffee | — | — |
| 33 | 4.3 | 174.733 | C-R | i | 1 | wipe | num | `s33.jpg` — short steel ruler against a long plank | — | num "half a month" **180.76** |
| 34 | 4.4 | 182.064 | B | o | 2 | wipe | stmt · warn | `s34.jpg` — unopened envelope, dust, windowsill | — | — |
| 35 | 4.5 | 187.278 | B | i | 1 | wipe | stmt | `s35.jpg` — government statistical release, stapled, macro | — | — |
| 36 | 4.6 | 192.336 | B | o | 2 | wipe | num · warn | `s36.jpg` — nearly empty coin tray at a checkout | — | num "two point seven percent" **194.21** · `hero` |
| 37 | 4.7 | 196.793 | C-L | i | 1 | wipe | num | `s37.jpg` — small stack of bills beside a much larger envelope | — | num "one hundred and eight" **199.38** |
| 38 | 4.8 | 201.851 | M | o | 2 | wipe | stmt · warn | `s38.jpg` — long empty highway to the horizon **(densest scene → calmest bg, §9)** | *recalls* `s13.jpg` | — |
| 39 | 4.9 | 208.581 | **R** | i | 1 | wipe | stmt · fund | `s39.jpg` — faucet running into a bowl, water column, dark | — | stmt **213.10** · `reveal` |
| 40 | 4.10 | 214.893 | B | o | 2 | wipe | stmt · target | `s40.jpg` — stone facade of a federal building, low angle | — | — |
| 41 | 4.11 | 221.492 | C-R | i | 1 | wipe | stmt · fund | `s41.jpg` — hand on a brass valve wheel | — | — |
| 42 | 5.1 | 225.531 | B | o | 2 | wipe | stmt | `s42.jpg` — the first envelope, now open | — | — |
| 43 | 5.2 | 229.701 | B | i | 1 | **hold** | stmt | `s43.jpg` — two-pan balance almost level, one coin short | — | — |
| 44 | 5.3 | 234.498 | B | i | 2 | wipe | num · target | *holds* `s43.jpg` — **one continuous zoom into the pivot** | — | num "crossover" **235.50** · `reveal` |
| 45 | 5.4 | 236.682 | C-L | o | 1 | wipe | stmt | `s45.jpg` — currency strap around a bundle of bills, macro | — | — |
| 46 | 5.5 | 243.752 | M | i | 2 | wipe | num · target | `s46.jpg` — municipal water tower against flat sky | *recalls* `s43.jpg` | num "ninety-six thousand" **246.79** |
| 47 | 5.6 | 248.758 | **R** | o | 1 | wipe | num · target | `s47.jpg` — weathered highway mile marker at dusk | — | num "one hundred thousand" **249.97** · `hero` |
| 48 | 5.7 | 255.487 | B | i | 2 | wipe | stmt | `s48.jpg` — hardback book face-down, open, lamp-lit desk | — | — |
| 49 | 5.8 | 259.527 | B | o | 1 | wipe | stmt | `s49.jpg` — empty chair at the head of a long table | — | — *(dry — see §2)* |
| 50 | 5.9 | 267.144 | C-R | i | 2 | **SHOVE** | stmt | `s50.jpg` — longhand sums, one line double-underlined | — | `transition` **272.49** |
| 51 | 5.10 | 272.490 | **R** | o | 1 | wipe | stmt · fund | `s51.jpg` — worn wooden stair tread, centre polished smooth | — | stamp module **277.05** · `stamp` |
| 52 | 5.11 | 278.854 | B | i | 2 | wipe | stmt | `s52.jpg` — long empty stairwell seen from the bottom | — | — |
| 53 | 6.1 | 283.259 | B | o | 1 | wipe | stmt | `s53.jpg` — thumb opening an envelope | — | — |
| 54 | 6.2 | 287.820 | B | i | 2 | wipe | num | `s54.jpg` — bus stop at dawn, bags and shoes only, no faces | — | num "twelve hundred and fifty" **291.36** |
| 55 | 6.3 | 293.949 | C-L | o | 1 | wipe | stmt · warn | `s55.jpg` — repair invoice on a car hood, figures out of focus | — | — |
| 56 | 6.4 | 300.261 | B | i | 2 | wipe | stmt | `s56.jpg` — pie cut into visibly unequal slices | — | — |
| 57 | 6.5 | 305.894 | B | o | 1 | wipe | num | `s57.jpg` — single squared stack of dollar bills, top light | — | num "twenty percent of a four thousand dollar take-home" **309.16** · `hero` |
| 58 | 6.6 | 312.728 | B | i | 2 | wipe | stmt | `s58.jpg` — target drawn in pencil on butcher paper | — | — |
| 59 | 6.7 | 319.197 | M | o | 1 | wipe | stmt | `s59.jpg` — small coin pile beside a far larger one | *recalls* `s11.jpg` | — |
| 60 | 6.8 | 324.542 | B | i | 2 | wipe | stmt · warn | `s60.jpg` — straight two-lane road, horizon, heat shimmer | — | — |
| 61 | 6.9 | 329.887 | C-R | o | 1 | wipe | stmt · warn | `s61.jpg` — desk calendar, every square blank | — | — |
| 62 | 6.10 | 334.867 | B | i | 2 | **SHOVE** | stmt | `s62.jpg` — two forms side by side, one signed, one blank | — | `transition` **340.71** |
| 63 | 7.1 | 340.709 | B | o | 1 | wipe | stmt | `s63.jpg` — cold stone fire ring, frosted ground, ash only | — | — |
| 64 | 7.2 | 344.460 | B | i | 2 | wipe | stmt | `s64.jpg` — matches and a bundle of split kindling | — | — |
| 65 | 7.3 | 348.317 | C-L | o | 1 | wipe | stmt · warn | `s65.jpg` — hands feeding one stick into a small flame | — | — |
| 66 | 7.4 | 354.733 | B | i | 2 | wipe | stmt | `s66.jpg` — thin flame on bare ground, wind in the smoke | — | — |
| 67 | 7.5 | 359.896 | B | o | 1 | wipe | stmt · fund | `s67.jpg` — shallow bed of glowing coals, macro | — | — |
| 68 | 7.6 | 364.901 | **R** | i | 2 | wipe | stmt · fund | `s68.jpg` — one heavy log on a deep coal bed, dark surround ⚠ | — | stmt **367.33** · `reveal` |
| 69 | 7.7 | 369.959 | B | o | 1 | wipe | stmt · target | `s69.jpg` — wide established fire at dusk, wood pile untouched | — | stamp module **375.99** · `stamp` |
| 70 | 7.8 | 378.100 | B | i | 2 | wipe | stmt · warn | `s70.jpg` — rained-out fire ring, wet ash, standing water | — | — |
| 71 | 8.1 | 383.863 | B | o | 1 | wipe | stmt | `s71.jpg` — three galvanised buckets in a row, shed wall | — | `tick` **385.98** |
| 72 | 8.2 | 388.738 | C-R | i | 2 | wipe | stmt · fund | `s72.jpg` — date circled in pen on a paper wall calendar | — | `chip` **389.19** |
| 73 | 8.3 | 394.684 | B | o | 1 | wipe | stmt · warn | `s73.jpg` — open wallet lying flat and empty | — | — |
| 74 | 8.4 | 400.317 | B | i | 2 | wipe | stmt | `s74.jpg` — cut end of a log, growth rings, macro | — | `chip` **400.71** |
| 75 | 8.5 | 404.722 | B | o | 1 | wipe | stmt · fund | `s75.jpg` — measuring cup topped up to the next mark | — | — |
| 76 | 8.6 | 409.832 | B | i | 2 | wipe | stmt | `s76.jpg` — the same kitchen shelf, softer evening light | — | — |
| 77 | 8.7 | 416.065 | C-L | o | 1 | wipe | stmt · fund | `s77.jpg` — padlock on a steel cabinet latch | — | `chip` **416.51** |
| 78 | 8.8 | 421.698 | B | i | 2 | wipe | num · target | `s78.jpg` — **blank rate-disclosure sheet, raking light** (calmed, §9) | — | num "a third of one percent" **424.45** |
| 79 | 8.9 | 429.211 | B | o | 1 | wipe | stmt | `s79.jpg` — kitchen timer showing five minutes | — | — |
| 80 | 8.10 | 434.452 | B | i | 2 | wipe | stmt | `s80.jpg` — three stone steps rising, morning light | — | — |
| 81 | 8.11 | 438.596 | C-R | o | 1 | wipe | stmt | `s81.jpg` — wide-mouth jar on a low shelf beside a sealed crate | — | — |
| 82 | 8.12 | 444.594 | **R** | i | 2 | wipe | stmt · warn | `s82.jpg` — cracked ceramic jar, coins spilled, concrete, dark | — | stamp module **449.85** · `stamp` |
| 83 | 9.1 | 451.376 | B | o | 1 | wipe | stmt | `s83.jpg` — wall clock reading five past the hour | — | — |
| 84 | 9.2 | 455.102 | C-L | i | 2 | wipe | stmt · fund | `s84.jpg` — paper transfer authorisation form and pen **(NOT a phone)** | — | — |
| 85 | 9.3 | 461.283 | B | o | 1 | wipe | stmt | `s85.jpg` — a small coin and a large coin side by side | — | — |
| 86 | 9.4 | 468.170 | B | i | 2 | wipe | stmt · fund | `s86.jpg` — wall switch in the on position, dust on the plate | — | — |
| 87 | 9.5 | 472.026 | B | o | 1 | wipe | stmt · warn | `s87.jpg` — the enamel mug, now noticeably fuller (new photograph) | — | — |
| 88 | 9.6 | 479.122 | M | i | 2 | wipe | stmt · fund | `s88.jpg` — the full glass jar (new photograph) | *recalls* `s28.jpg` | — |
| 89 | 9.7 | 483.683 | B | o | 1 | wipe | stmt · target | `s89.jpg` — roadside distance marker, later light (new photograph) | — | — |
| 90 | 9.8 | 490.230 | **R** | i | 2 | wipe | stmt · fund | `s90.jpg` — settled fire burning steadily at night, wide, unattended ⚠ | — | stmt **493.85** · `reveal` |
| 91 | 9.9 | 496.307 | B | o | 1 | wipe | num · **pop** | `s91.jpg` — closed ledger and capped pen laid down | — | num "SUBSCRIBE" **496.69** · `cta` |
| 92 | 9.10 | 499.798 | B | i | 2 | *(final)* | stmt | `s92.jpg` — highway sign gantry from below, no place names | — | — |

**`foot:` lines are verbatim from the script's cue block.** The 14 scenes that MUST carry the
`ILLUSTRATIVE · $800/mo · <rate> · monthly compounding` foot — a fact-integrity requirement,
not a design one — are **1, 2, 13, 15, 16, 22, 25, 26, 28, 29, 33, 37, 38, 46**. The 17
source-bearing feet are **4, 12, 14, 18, 36, 40, 45, 47, 49, 54, 55, 58, 70, 78, 80, 81, 85**.
A `num` frame without its foot is a months-to-milestone figure spoken as a statistic (script
§THE SIX THINGS #5) — **fail the build, do not fix it in the audit.**

⚠ **Rounding.** `12.5` is exact by construction ($10,000 ÷ $800) and renders as `12.5`, never
`13`. Every months figure is round-to-nearest, never `ceil` (script handoff §4).

---

## 7. The continuous-zoom pair and the `hold` boundary

**Exactly one pair** in this cut (script handoff §5), against the hi cut's three.

| pair | scenes | combined | fix |
|---|---|---|---|
| 5.2 + 5.3 | s43 + s44 | **6.981s** | ONE ken tween spanning both scenes, tightening into the pivot; never a self-dissolve (creator rule, firaun 2026-07-23) |

**`trans: hold` means a matched-frame boundary.** The outgoing and incoming scenes show the
same photograph at the same zoom phase, so the 0.45s wipe is invisible and the move reads as
one push. This keeps `data-duration = scene_duration + 0.45` on **every** non-final scene —
the blockframe §5 rule-0 assert holds with no exception carved into it, which is what makes it
safe. **Build requirement:** phase-match the ken tween across the boundary; a phase
discontinuity is exactly the flicker the creator rejected.

Combined 6.981s is inside `max_scene_seconds` 9.0, so no build-time re-crop is needed.

**Five scenes re-photograph an earlier object from a new crop and are NOT holds** — they get
their own files: **s87 ← s1** (the mug), **s88 ← s2** (the jar), **s89 ← s47** (the marker),
**s50 ← s10** (the legal pad), **s76 ← s75** (the kitchen shelf). A recall inside the mosaic
`minor` slot (s16, s29, s38, s46, s59, s88) *does* re-use the file, because a minor rectangle
is a memory device pointing at a frame the viewer already saw — that is not the cross-video
repeat the design doc forbids.

---

## 8. Divergence list — what this cut deliberately does NOT port from `storyboard-hi.md`

**Ported unchanged** (so a fix travels between cuts): the `s<n>-<part>` ID scheme, the §3
per-scene DOM, the §4 cue ladder and its declared assembly cascade, the aperture vocabulary
(B / C-R / C-L / R / M), the `.swiss-band` divergence table, the four colour *roles*, the
parity rules for `ken` and `data-track-index`, and the `data-duration + 0.45` contract.

**Deliberately divergent, with a reason each:**

| # | scene(s) | diverges how | why |
|---|---|---|---|
| 1 | all | **Cycle offset.** hi opens `R` at s1; en opens `B` and its first `R` is s5. Aperture mix 57/18/9/8 over 92 vs hi's 56/13/10/7 over 86 | 11-swiss-vignelli §7: the cycle offset must vary by video. Two cuts landing on the same aperture at the same index is the pair reading as one template with the language swapped |
| 2 | all | **92 scenes, not 86** | one line = one clip = one scene, and the US rewrite is a different script. Scene count is emergent (`format.json scene._scene_seconds_note`), never a constant |
| 3 | s1, s2 | **The hero pair is 12.5 / 6 months on $10,000**, not 20 / 7 months on ₹1,00,000 | a US rewrite, not a conversion. hi compares the FIRST lakh to the SECOND; en compares the first $10,000 to the **tenth** — a different comparison, and the reason en's second figure is 6 and not 7 |
| 4 | **s48, s49, s50** (5.7–5.9) | **The Munger block — three scenes with no hi counterpart at all.** New apertures (B, B, C-R), new image slots, and declared DRY | "the first $100,000 is a bitch" is US-only folk attribution with no ₹ equivalent; the hi cut has no such beat. Dry because the quote is *colour, not evidence* — 5.5 reaches ~$96,000 without it, and a `stamp` under an unsourceable line sells it as proof |
| 5 | **s63–s70** (all of ch 7) | **The ~70% re-frame is a fire pit, not a rooftop water tank.** Every image keyword in the chapter diverges; the structural job is identical, so IDs and cue ladder port unchanged | a US rewrite gets a US object (`us-english-script-style.md`). A rooftop poly water tank is an Indian domestic fixture and reads as foreign b-roll to a US viewer |
| 6 | **s36** (4.6) | **BEA 2.7% national personal saving rate** — a scene with no hi counterpart, and it takes the **23rd SFX cue** (`hero`) | the strongest US-specific HARD number in the packet. hi's honesty chapter used PLFS/RBI figures and ran fully dry; this one number earns a cue, which is the entire reason en runs 23 cues to hi's 22 |
| 7 | **s54, s55** (6.2, 6.3) | **BLS $1,251/wk median weekly earnings; Fed SHED "~4 in 10 couldn't cover $400"** replace hi's PLFS/RBI evidence scenes | US institutional evidence. Structural divergence, not a copy change — the sources, the framing and the images are all different |
| 8 | **s40** (4.10) | **Fed funds target range, unchanged since Dec 2025**, replaces hi's DEA quarterly small-savings notification | different institution, same job ("the rate is not worth waiting for"). The federal-building facade replaces the notification-page macro |
| 9 | **s78** (8.8) | **FDIC national savings rate 0.38% + the "roughly ten times" ratio** replaces hi's AMFI ₹500 SIP-minimum scene | US price evidence, and the ratio (never an APY) is the standing HYSA rule. hi's ₹500 entry-ticket beat has no US analogue |
| 10 | s43+s44 | **One hold pair, not three.** hi holds at 1.1+1.2, 1.5+1.6 and 5.2+5.3 | different clip lengths. 5.3 measures **1.384s** — far too short to establish its own image — so the hold is structurally required there and nowhere else. hi's hook clips are long enough to carry one zoom across two scenes; en's 4.4s clips are not |
| 11 | s50→s51, s62→s63 | **Shove placement.** hi shoved 5.8→5.9 and 6.10→7.1; en shoves **5.9→5.10** and 6.10→7.1 | the turn line moved: en's chapter 5 has 11 lines and the "not interest — the habit" sentence is 5.10, one later than hi's 5.9. The second shove is the same structural turn and is ported as-is |
| 12 | **s84** (9.2) | **A paper transfer-authorisation form**, where hi used a bank passbook | same guard (never a phone-screen photo — it has shipped wrong three times), different US object. A passbook is not a US retail-banking artefact |
| 13 | s87, s88, s89, s50, s76 | **Five deliberate re-photographs get their own files**, where the hi cut re-used three files as recalls (s82, s83) | the script's own decision (handoff §5): "same object, new crop" at 1920×600 inside a fixed aperture needs a genuinely different frame, not a re-crop of a 1920-wide jpg |
| 14 | timing | **No `max_scene_seconds` ambiguity.** hi's s16 reads 9.191s if `check_build` measures `data-duration`; en's longest (s69) reads **8.590s** either way | measured, not designed — but it means this cut does not depend on resolving that check, and fin-build should not carve an exception for it here |
| 15 | audio | **The bed's second loop dip lands on the CTA**, not on a recap line as it does in hi (§2) | 505.561s vs 514.789s runtime shifts ≈496s from mid-scene into the s90/s91 boundary. Same defect, strictly worse placement — the fix is more urgent on this cut |

Zero divergences would be a translation wearing a layout costume. Fifteen is what a genuine
US rewrite of a shared spine produces: one shared skeleton, one shared motion vocabulary,
and every market-specific claim, object and beat replaced.

---

## 9. Images — 100 slots, 93 files

`assets/img/manifest.json` carries the 93 fetch queries. The 7 slots with no query are the
**1 continuous-zoom hold** (s44) and the **6 mosaic-minor recalls** (s16, s29, s38, s46, s59,
s88 minors), each of which re-uses a file from *this* video — a memory device, not the
cross-video repeat the design doc forbids.

- **Every scene carries a photograph.** `photo_free_scene_ratio` = 0 (creator rule
  2026-07-28), `image_per_scene: true`. Zero exceptions in this cut.
- **Cut-ins have a structural home, not a floating one.** In `.swiss-band` a floating overlay
  timed to a word is the anti-Swiss move — it dissolves the edge, and the edge is the design.
  The Unigrid answer is the **mosaic minor rectangle** (§2.1 method 3, "major and minor
  pictorial themes"), so the 8 `M` scenes carry the cut-in as a *module*, wiping in at +0.85.
  On the other 84 scenes the keyword rule is satisfied by the bg itself: every query is
  object-led and names the concrete thing its VO line names (mug, jar, pay stub, calendar,
  faucet, coal bed, padlock, wallet, timer, mile marker).
- **Densest scene, calmest background.** **s38 (4.8)** is the densest frame in the cut —
  mosaic major + minor + a two-figure statement ("7.7 years · 5.7 years") + an ILLUSTRATIVE
  foot + `--warn`. Its image is a **long empty highway to the horizon**, which is already a
  flat tonal mass and a literal reading of "almost eight years". Kept as-is.
- **The one image changed at this stage: s78 (8.8).** The script asks for "a printed rate
  disclosure sheet, macro on the fine print" — the busiest frame in the script, behind a
  200px `0.38%` and a two-clause FDIC foot. **Changed to a quiet texture reading of the same
  keyword: a blank rate-disclosure sheet in raking light.** The fine print's meaning is
  carried by the copy; the frame does not need to shout it. (Same move the hi cut made on its
  s37.)
- **Reversed type is MEASURED, not assumed.** The 9 `R` scenes put type on the photograph
  behind a tone block. Measure the left third's mean luminance at fetch time and **reject any
  image above 25%** — there is no scrim to rescue it. ⚠ **Two are high-risk and are flagged
  in the table: s68 (7.6, a coal bed) and s90 (9.8, a night fire).** Fire is the brightest
  object in a frame by construction. Both queries force a dark surround; if either still
  measures above 25%, **demote it to `B` and ship 8 `R` scenes** — the `R` count is a design
  choice, not a checked constant, and reversed type on a bright image is unreadable in a way
  no later fix repairs.
- **Never a phone-screen photo as a background** — **s84 (9.2)** is the trap and the script
  pre-empts it: a paper transfer form, not a phone. This has shipped wrong three times.
- **Faces fight the typography and are a licence problem.** Hands and objects only: s6, s19,
  s41, s53, s54, s65 are explicitly hands / feet / objects with no identifiable face.
- **US localisation sweep on every frame** (`us-english-script-style.md`): reject any image
  with non-US currency, non-US plates, non-US signage, right-hand-drive vehicles or
  foreign-language packaging. Every currency query says "dollar bills" for exactly this
  reason — the first `-en` cut shipped a Swiss franc and a pile of euro coins.
- **Cross-cut repeat risk is the live hazard on this pair.** 30+ subjects overlap the hi cut
  (envelopes, wall calendars, coin stacks, legal pads, ledgers, ropes, stone steps, padlock,
  wall clock, dusty switch, mile marker, measuring vessel, kitchen shelf, growth rings). The
  manifest **deliberately alternates provider** against the hi cut on every overlapping
  subject (`@pexels` where hi used the pixabay default, and vice versa), because Pixabay's
  top hit is deterministic and different queries collapse to it. That is a mitigation, not a
  guarantee: **md5 every file against the ledger and refuse any hash used anywhere on either
  channel.**
- **Repeat-risk pairs inside this cut** — check md5 before accepting: s2 vs s88 (two full
  jars), s1 vs s87 (two mugs), s47 vs s89 vs s92 (three roadside/highway markers), s63 vs
  s66 vs s67 vs s68 vs s69 vs s70 vs s90 (seven fire frames), s10 vs s50 (two legal pads),
  s75 vs s76 (the kitchen shelf), s13 vs s61 vs s72 (three calendars). Different shots of the
  same subject are wanted; the same file twice is not.
- Write `assets/img/*.src` prompts and `CREDITS.txt` — the archive rule depends on them
  (`vault/CLAUDE.md` finished-video rule, gotcha 2).

---

## 10. Deliberate placeholders (must be real before publish)

- **The hard-wipe boundary is still unproven against `ffmpeg scdet`.** It replaces a
  cross-dissolve that exists for a measured reason (boundary frame-delta 5.85–10.72; five of
  eight boundaries tripped a generic cut detector). Measure chapter 1's master before locking
  chapters 2–9. If it reads as a hard cut, fall back to `dissolve` for the same 0.45s — the
  scene arithmetic is identical either way. **Measure it on ONE cut and apply the result to
  both**; this is not a per-cut question.
- **`bed-resolve` is 248s against a 505.561s cut** (§2), and the second dip lands on the CTA.
  Unfixed, the video goes silent on its one `--pop` frame.
- **Word-level anchoring is not yet wired.** The `f` fractions in §2/§6 are fallbacks; run
  faster-whisper.
- **Left-third luminance measurement does not exist in the pipeline yet** (11-swiss-vignelli
  §9). Without it, the 9 `R` scenes are a coin flip. It is a small tool — PIL crop + mean
  luminance at fetch time — and s68 / s90 are the two that will expose its absence.
- **The two-sizes-per-scene rule met a real script for the first time on the hi cut and has
  not yet met a render.** Same open question here; first real evidence either way comes out
  of chapter 1's master.

---

## 11. Sign-off

- [x] Colour semantics table filled and consistent with the script (§1, incl. the "green ≠ returns" trap)
- [x] Cue times derived from measured `timing.json`, never estimated
- [x] Cue classes declared (anchored vs fixed); the sub-0.8s assembly declared as a cascade with its reason; closest non-assembly pair 2.84s
- [x] Transitions declared: 88 wipes, 2 shoves, 1 hold, 1 final
- [x] One music bed named + 23 SFX cues, no pair inside 0.8s, dry beats declared
- [x] Every scene has a bg photo; densest scene (s38) has the calmest bg; the one busy image (s78) calmed; cut-ins have a structural home
- [x] Divergence list from `storyboard-hi.md` — 15 entries, one reason each (§8)
- [ ] No image hash reused from any prior video on either channel, or from the hi cut of this video — **fin-assets to verify by md5**
- [ ] Left-third luminance measured on all 9 `R` scenes; s68 / s90 demoted to `B` if above 25%
- [ ] `scdet` re-measured on the hard wipe
- [ ] Creator approved (Gate ②) — date: __
