---
summary: Storyboard for «पहला एक लाख» hi cut — MEDIUM tier, 86 scenes (one VO line = one clip = one scene), swiss-band architecture. Declares the colour semantics, the aperture programme, the assembly cue cascade, transitions, one music bed + 22 SFX cues, and 93 image slots backed by 87 fetched files.
updated: 2026-07-31
source: script-hi.md (fin-script attempt 1) + studio/videos/first-lakh-first-thousand-hi/assets/voice/timing.json (measured, 514.789s) + knowledge/design-finance-blockframe.md + knowledge/finance-audit-2026-07-29/11-swiss-vignelli.md Direction 1 + tools/format.json + tools/audio/kit.json
stage: fin-storyboard, cut hi, attempt 1
---

# STORYBOARD — «पहला एक लाख» (The first ₹1 lakh is the hardest) · **hi** cut

**Project:** `studio/videos/first-lakh-first-thousand-hi/` · **Script:** `script-hi.md`
**Design:** [[../../knowledge/design-finance-blockframe]] (the **dark** system) with the
`.swiss-band` divergences of [[../../knowledge/finance-audit-2026-07-29/11-swiss-vignelli]] §4 D1 + §8.
Do **not** use `design-techtooltester` — that is the bright, non-finance system.
**Channel:** @cashguruguides ₹ · **Tier:** MEDIUM, per-line chapters · **Architecture:** `swiss-band` (run.json creator pick, 2026-07-31)
**Runtime:** **514.789s (8:35)** measured — `timing.json` is the only home for every duration.
**VO:** Harsh `HTUuC7OeeEt6OL5fViVe` · **Scenes:** 86 · **Image slots:** 93 (86 bg + 7 mosaic minors), 87 files fetched.

---

## 1. Colour semantics for THIS video (derived from the thesis — mandatory)

The thesis: *the first lakh is hard because 100% of it is you; after it, a mechanism
you built starts carrying the load.* Roles are fixed, meanings are per-video.

| Token | This video means | Because |
|---|---|---|
| `--warn` red `#ef4444` | **the stretch nobody helps you with** — the first lakh, the 20 months, the 2 months the market buys, the month-end zero, the one emergency that breaks it | the video's obstacle is not a villain or a leak; it is an interval you cross alone |
| `--fund` green `#22c55e` | **the mechanism that works without you once it exists** — the standing instruction, the habit, the escalator, the separate account; and *only later* the tenth lakh, the 7 months, the rain | ⚠ green is **NOT** "returns doing the work". It marks the viewer's own behaviour first (4.6, 4.8, 5.9, 8.2, 8.5, 8.7, 9.2, 9.4) — 5.9 exists to deny that returns take over at the first lakh |
| `--target` amber `#f59e0b` | **a rate or a threshold under examination** — 7.1%, ~12%, the ₹5,00,000 crossover, the word CROSSOVER itself, the ₹500 entry ticket, the three open questions | amber is the thing being weighed, never the thing being recommended (persona rule: no product picks) |
| `--pop` orange `#ff5c39` | the call to action | fixed — **exactly once**, scene 85 (9.9) |

**The inversion trap.** needs-vs-wants ran amber = "wants" and red = "the leak alone".
Neither meaning applies here. Any element rendering the tenth lakh in red, or the first
lakh in green, argues against the script.

**Swiss constraint on top of the above: ONE role colour visible per scene, ever**
(11-swiss-vignelli §5.1). Colour appears as a **filled square module or a rule**, never
as coloured text on the photograph and never as a rounded pill. Per-scene `--tint` is
**retired** in `.swiss-band` — a 0.10–0.13 alpha wash is pictorial colour, the one use
Vignelli names as wrong (Canon p.78). There is no `tint` column in this storyboard, on purpose.

---

## 2. Audio — one bed, 22 cues

**Music bed: `bed-resolve`.** The argument of this video is a **habit / a fix**, not a
trap or a cost: it ends on one auto-transfer and a mechanism that keeps running. Chapters
2–4 have a cost *register*, but the thesis they serve is constructive, and the bed is
chosen for the video, not for a chapter.

> ⚠ **Loop hazard — load-bearing for fin-build.** `bed-resolve` is **248s** on disk
> (`kit.json _music_on_disk`); this cut is **514.789s**. `mix.py` stream-loops, and both
> beds fade in from / out to silence, so an audible dip to silence lands at **≈248s**
> (inside s42 / 5.5, on the crossover figure) and **≈496s** (inside s83 / 9.7, on recap
> three). Both are the worst possible places. Before mixing: trim the head/tail silence
> off `bed-resolve.mp3` and crossfade the loop point, or source a ≥520s bed and
> re-normalise it through the same two-pass loudnorm to −20 LUFS (mix.py's 0.16 gain and
> 6 dB duck are calibrated against that figure). Do **not** run
> `sfx.py --kit --music --force` — it would destroy the creator-supplied beds, which are
> not regenerable and live only in gitignored `studio/`.

**SFX budget: 22 cues across 8:35** — one per ~23s. The kit's stated ceiling (≤10) is a
**SHORT-cut** figure; scaling it by runtime would give ~57, which is exactly the "every
reveal has one, so none of them means anything" failure. 22 is a deliberate ceiling, not
a derivation. **No two cues inside 0.8s** (verified below; the closest pair is 2.4s).

| # | scene | line | sound | helper | absolute t | why this beat |
|---|---|---|---|---|---|---|
| 1 | s1 | 1.1 | `hero` | the big number | **4.95** | `20 MONTHS` lands on «बीस महीने» — frame-one figure |
| 2 | s2 | 1.2 | `hero` | the big number | **10.42** | `7 MONTHS` — the pair IS the video; both get the impact |
| 3 | s17 | 2.7 | `hero` | the big number | **101.67** | `2 MONTHS` — what the best return in the country bought |
| 4 | s19 | 2.9 | `stamp` | verdict module | **112.82** | `100% savings · 0% returns` — the thesis stated |
| 5 | s26 | 3.7 | `hero` | the big number | **153.72** | `13 MONTHS` — the other half of the thesis |
| 6 | s27 | 3.8 | `stamp` | verdict module | **159.72** | "This is the video" |
| 7 | s33 | 4.6 | `reveal` | rise | **195.81** | "Not the return rate. The savings rate." |
| 8 | s40 | 5.3 | `reveal` | rise | **236.77** | the word CROSSOVER arrives |
| 9 | s43 | 5.6 | `hero` | the big number | **256.26** | `~₹5,00,000` — the correction to the flagged error |
| 10 | s45→s46 | 5.8→5.9 | `transition` | shove | **269.27** | **SHOVE #1** — the turn from "not interest" to "the habit" |
| 11 | s46 | 5.9 | `stamp` | verdict module | **271.97** | "the HABIT takes over" (2.70s after cue 10 ✓) |
| 12 | s53 | 6.6 | `hero` | the big number | **311.81** | `₹5,000` — the one input the whole video runs on |
| 13 | s57→s58 | 6.10→7.1 | `transition` | shove | **340.08** | **SHOVE #2** — into the ~70% re-frame |
| 14 | s63 | 7.6 | `reveal` | rise | **371.76** | "the rain puts in what your bucket used to" |
| 15 | s64 | 7.7 | `stamp` | verdict module | **376.81** | "That day is the crossover" |
| 16 | s66 | 8.1 | `tick` | pulse | **391.14** | «तीन चीज़ें» — opens the three-rung set |
| 17 | s67 | 8.2 | `chip` | pop | **396.06** | rung ONE |
| 18 | s69 | 8.4 | `chip` | pop | **411.06** | rung TWO |
| 19 | s72 | 8.7 | `chip` | pop | **428.64** | rung THREE — the three `chip`s are one set, which is why repeating is legible here and nowhere else |
| 20 | s76 | 8.11 | `stamp` | verdict module | **455.13** | "By one emergency." |
| 21 | s84 | 9.8 | `reveal` | rise | **501.43** | the closing statement |
| 22 | s85 | 9.9 | `cta` | closing block | **507.17** | the single `--pop` block |

**Declared DRY beats** (silence is the choice, not an omission):
- **Chapters 1.3–1.10** — after the two hero hits the hook runs dry; the questions land on voice alone.
- **All of chapter 4 except 4.6** — the accusation chapter. Adding sound to "weeks of research and the account never opens" would make it a joke instead of an indictment.
- **All of chapter 6 except 6.6** — the honesty chapter (PLFS/RBI figures, "then the first lakh is further away"). Punctuating a hard truth reads as showmanship.
- **7.1–7.5** — the analogy is built in silence so 7.6/7.7 can land.
- **9.5–9.7, the whole recap** — dry so the `cta` at 507.17 is the first sound in 45s.

**Mixed in post, never in the composition.** `assets/audio.json` cue list → `tools/audio/mix.py`
(sidechain duck) → `tools/loudnorm.py` to −14 LUFS. The composition stays voice-only: one
`<audio>` row per line, track index 10.

---

## 3. The `.swiss-band` frame — DOM and the aperture

`<div id="root" class="swiss-band">`. Grid 12 × 8 on 1920 × 1080: side margins 100px,
column 125px, gutter 20px (col *n* left edge `x = 100 + (n−1)×145`); top/bottom trim 60px,
row pitch 120px (row *m* top `y = 60 + (m−1)×120`).

### Per-scene DOM (identical every scene — the aperture IS the identity)

```html
<section class="scene" id="s12" data-track-index="2" data-duration="…">
  <div class="titlebar">                        <!-- row 1: x 0→1920, y 60→180, solid --bg -->
    <h2  id="s12-bar">…</h2>                    <!-- 84px/800, tracking -1, --ink, x=100, hung 26px below bar top -->
    <span id="s12-mark">₹ · CH 2</span>         <!-- 26px/200 --muted, uppercase, tracking +4, flush right x=1820 -->
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
  <span class="idx" id="s12-idx">12 / 86</span> <!-- 26px/200 --muted tabular, flush right x=1820, y=1020 -->
</section>
```

**ID scheme: `s<n>-<part>`, n = 1…86 in script order.** This is the skeleton the `-en`
cut ports (§8). Line-id ↔ index mapping is the `#`/`line` columns of §6.

**Copy is NOT restated here.** `bar:`, `stmt:`/`num:` and `foot:` strings live in the
script's `[ap …]` cue block for each line and have exactly one home. This storyboard owns
the DOM, the cues, the transitions, the audio and the images.

### Load-bearing divergences from `design-finance-blockframe.md` (all from 11-swiss-vignelli §8)

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
| `dissolve` 0.45s | **hard directional wipe, 0.45s** — same duration, so the scene arithmetic and the cut-detector argument both hold. ⚠ **unproven**: re-measure with `ffmpeg scdet` on the first chapter master before locking (11-swiss-vignelli §9) |
| "no scene may hold a **static photo** beyond ~2s" | restated: **no frame may be motionless beyond ~2s**. Rules, blocks and apertures can carry the motion; the photo need not |

**Element budget.** `mark` and `idx` are **furniture** — identical, muted, weight 200, in
every frame; they are the aperture, not content. Content elements per scene: `bar`, `rule`,
focal (`stmt` **or** `num` — never both, blockframe §5 rule 4 survives), `foot`, plus the
mosaic `minor`. **Max 5 content elements**, against the format.json ceiling of 6. ✓

---

## 4. The cue ladder — one canonical assembly, declared as a cascade

Every scene animates identically. Offsets are **relative to `scene_start`** (§6 column
`start`, verbatim from `timing.json`), so every absolute cue time is
`scene_start + offset` and is derived, never hand-typed.

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
> decision rather than drift. It obeys `cascade.max_items` **5** exactly. Justification:
> the Unigrid frame assembles as a unit; spacing its parts 0.8s apart would spend 4s of a
> 5.9s average scene building furniture. Every *content* cue that is not part of the
> assembly (the anchored `num`, the `stamp` module) keeps the ≥0.8s rule — the closest such
> pair in the whole cut is 2.40s.
>
> `layout.first_cue_by_seconds` 0.5 ✓ — the band opens at +0.00 in every one of the 86 scenes.

**Anchored vs fixed.** Items 1, 2, 3, 5 and the tone/minor wipes are **fixed**: constant
regardless of clip length. The `ken` push and the `num`/`stamp` arrivals are **anchored**:
they land on a word and scale with the clip. **Surplus time from a longer clip goes into
the hold after the assembly — never into the cascade.** Concretely: the assembly always
finishes at +1.50s; a 8.7s scene (s16) holds a finished frame for 7.2s with only the ken
push running, and that is correct.

**The 15 `num` scenes take an anchored arrival instead of the +0.70 fixed hang** — putting
the figure on screen 4.5s before the voice says it spoils the hook. `stmt` scenes keep the
fixed +0.70 because a statement paraphrases the whole line and cannot spoil it.

**Anchored cue resolution.** The absolute times in §2 and §6 are computed as
`audio_start + f × duration` with the target word named. **`f` is a fallback.** Per
script handoff §8, fin-build resolves each one against **faster-whisper word timings** and
uses the fraction only if the word fails to align — character-offset interpolation drifts
worst on Hindi.

**Track index alternates 1 / 2 by scene parity** (odd → 1, even → 2), because
`hyperframes check` rejects two overlapping clips on one track and every non-final scene
overlaps its successor by 0.45s.

**`data-duration` = `timing.json` `scene_duration` + 0.45** on scenes 1–85; s86 carries its
`scene_duration` bare. Root duration is unaffected: **514.789s**.

---

## 5. The aperture programme (the anti-sameness engine — mandatory)

Canon p.84: a declared *cycle* of apertures, never one frame repeated. Four apertures,
one grid, one type system, one motion vocabulary.

| ap | aperture | count | where |
|---|---|---|---|
| **B** | BAND (D1) — 1920×600 full-bleed band, rows 2–6 | **56** | the default, 65% of scenes |
| **C-R / C-L** | COLUMN (D2) — 950×1080 photo block, cols 7–12 (R) or `x 0→950` (L); type in the complementary columns | **13** | one scene in roughly every four |
| **R** | REVERSED FIELD (D4) — full bleed, type reversed on a hard-edged tone block | **10** | the hook (1.1, 1.2), the thesis (2.7), the sentence the video is named for (3.7), the savings-rate line (4.6), the crossover term (5.3) and its correction (5.9), the rain (7.6), how it actually breaks (8.11), the closing statement (9.8) |
| **M** | MOSAIC (D3) — major photo rectangle + minor rectangle carrying the second figure | **7** | every two-figure comparison: 2.3, 3.2, 4.10, 5.5, 6.5, 8.8, 9.6 |

56 + 13 + 10 + 7 = 86 ✓ · **Cycle offset: this cut opens on `R`. The `-en` cut must not.**

### Two corrections to the script's `ap` column (storyboard stage, with reasons)

1. **The C-R/C-L alternation was broken twice.** The script's own rule is "alternating
   photo side L/R across the whole video, so the swap reads as a rhythm", but its sequence
   ran `R L R L R L **L** R L **R R** L R` — doubling at 4.9→5.6 and 7.3→8.2. Re-derived
   strictly from the rule, starting `R`. **Five scenes flip: 5.6 → C-R, 6.3 → C-L,
   6.8 → C-R, 7.3 → C-L, 8.2 → C-R.** No content consequence; the alternation is the point.
2. **Two counts in the script's prose disagree with its own table** — prose says "exactly 9"
   reversed-field scenes then lists 10, and "the 8 scenes" for mosaic then lists 7. The
   **table is authoritative**: 10 `R`, 7 `M`. Recorded here so the audit does not
   re-discover it as a defect.

---

## 6. Scenes

One row per VO line. `start` = `scene_start`, verbatim from `timing.json` (the only home);
every fixed cue is `start + offset` from §4. `focal` names which of `stmt`/`num` carries
the frame and its single role colour. Copy lives in the script.

**Legend.** ken: `i` = in, `o` = out (parity-alternating) · trk = `data-track-index` ·
trans: `wipe` = the 0.45s hard directional wipe (the `dissolve` slot), `SHOVE` = a real
turn in the argument, `hold` = matched-frame boundary inside a continuous-zoom pair (§7).

| # | line | start | ap | ken | trk | trans | focal | bg file — search query | minor / cut-in | anchored cue · SFX |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1.1 | 0.000 | R | i | 1 | hold | num · warn | `s1.jpg` — coin jar dark low light | — | num «बीस महीने» **4.95** · `hero` |
| 2 | 1.2 | 6.678 | R | i | 2 | wipe | num · fund | *holds `s1.jpg`* — one continuous zoom | — | num «सात महीने» **10.42** · `hero` |
| 3 | 1.3 | 11.736 | B | i | 1 | wipe | stmt · warn | `s3.jpg` — brass weights balance scale | — | — |
| 4 | 1.4 | 19.249 | C-R | o | 2 | wipe | stmt | `s4.jpg` — stacked ledger books shelf | — | — |
| 5 | 1.5 | 26.919 | B | i | 1 | hold | stmt · warn | `s5.jpg` — rupee coin standing on edge wood | — | — |
| 6 | 1.6 | 32.264 | B | i | 2 | wipe | stmt | *holds `s5.jpg`* — one continuous zoom | — | — |
| 7 | 1.7 | 35.886 | B | i | 1 | wipe | stmt · target | `s7.jpg` — three closed envelopes desk | — | — |
| 8 | 1.8 | 43.190 | C-L | o | 2 | wipe | stmt · target | `s8.jpg` — printed interest rate chart macro | — | — |
| 9 | 1.9 | 47.882 | B | i | 1 | wipe | stmt · target | `s9.jpg` — empty steel tiffin box open | — | — |
| 10 | 1.10 | 54.194 | B | o | 2 | wipe | stmt | `s10.jpg` — handwritten arithmetic lined paper pencil | — | — |
| 11 | 2.1 | 60.454 | B | i | 1 | wipe | stmt | `s11.jpg` — pay slip thin paper folded | — | — |
| 12 | 2.2 | 66.635 | B | o | 2 | wipe | num | `s12.jpg` — twelve coin stacks in a row | — | num «साठ हज़ार» **67.75** |
| 13 | 2.3 | 71.745 | M | i | 1 | wipe | num · warn | `s13.jpg` — wall calendar months crossed off | `s13m.jpg` — coin jar macro | num «बीस महीने» **74.18** |
| 14 | 2.4 | 76.072 | C-R | o | 2 | wipe | num · target | `s14.jpg` — post office counter brass grille | — | num «सात दशमलव एक» **82.70** |
| 15 | 2.5 | 84.291 | B | i | 1 | wipe | num | `s15.jpg` — calendar page torn falling | — | num «उन्नीस» **85.89** |
| 16 | 2.6 | 87.546 | B | o | 2 | wipe | num · target | `s16.jpg` — newspaper market page macro folded | — | num «अठारह महीने» **94.78** |
| 17 | 2.7 | 96.287 | R | i | 1 | wipe | num · warn | `s17.jpg` — hourglass sand neck macro dark | — | num «दो महीने» **101.67** · `hero` |
| 18 | 2.8 | 104.219 | B | o | 2 | wipe | stmt | `s18.jpg` — empty steel plate bare table raking light | — | — |
| 19 | 2.9 | 109.016 | B | i | 1 | wipe | stmt · warn | `s19.jpg` — hand placing note into steel box | — | stamp module **112.82** · `stamp` |
| 20 | 3.1 | 114.256 | B | o | 2 | wipe | stmt | `s20.jpg` — long ruled ledger paper strip | — | — |
| 21 | 3.2 | 120.516 | M | i | 1 | wipe | stmt | `s21.jpg` — two coin jars side by side | `s21m.jpg` — printed rate card macro | — |
| 22 | 3.3 | 127.951 | B | o | 2 | wipe | stmt | `s22.jpg` — two nails different height plank | — | — |
| 23 | 3.4 | 132.095 | B | i | 1 | wipe | stmt | `s23.jpg` — steel trunk lid propped open | — | — |
| 24 | 3.5 | 136.735 | C-L | o | 2 | wipe | num · warn | `s24.jpg` — bullock cart wheel still dust | — | num «बीस महीने» **138.72** |
| 25 | 3.6 | 143.334 | B | i | 1 | wipe | stmt · fund | `s25.jpg` — railway platform clock hands | — | — |
| 26 | 3.7 | 149.411 | R | o | 2 | wipe | num · fund | `s26.jpg` — two coiled ropes different length dark deck | — | num «तेरह» **153.72** · `hero` |
| 27 | 3.8 | 154.991 | B | i | 1 | wipe | stmt | `s27.jpg` — page torn from bound book gap | — | stamp module **159.72** · `stamp` |
| 28 | 4.1 | 161.538 | B | o | 2 | wipe | stmt | `s28.jpg` — printed comparison sheets spread | — | — |
| 29 | 4.2 | 166.831 | B | i | 1 | wipe | stmt | `s29.jpg` — blank forms wooden rack rows | — | — |
| 30 | 4.3 | 172.594 | C-R | o | 2 | wipe | stmt · warn | `s30.jpg` — half filled form capped pen | — | — |
| 31 | 4.4 | 178.593 | B | i | 1 | wipe | num | `s31.jpg` — short ruler against long plank | — | num «दो महीने» **182.83** |
| 32 | 4.5 | 184.251 | B | o | 2 | wipe | stmt · warn | `s32.jpg` — unopened envelope dust window sill | — | — |
| 33 | 4.6 | 191.033 | R | i | 1 | wipe | stmt · fund | `s33.jpg` — tap water falling into bucket dark | — | stmt **195.81** · `reveal` |
| 34 | 4.7 | 197.162 | B | o | 2 | wipe | stmt | `s34.jpg` — envelope with notes pulled clear | — | — |
| 35 | 4.8 | 202.821 | B | i | 1 | wipe | stmt · fund | `s35.jpg` — hand on brass tap handle | — | — |
| 36 | 4.9 | 207.618 | C-L | o | 2 | wipe | stmt | `s36.jpg` — government notification page seal macro | — | — |
| 37 | 4.10 | 214.949 | M | i | 1 | wipe | stmt · target | `s37.jpg` — **weathered painted board flat texture** (calmest bg — densest scene) | `s37m.jpg` — quarterly calendar page | — |
| 38 | 5.1 | 222.253 | B | o | 2 | wipe | stmt | `s38.jpg` — opened envelope on desk | — | — |
| 39 | 5.2 | 228.199 | B | i | 1 | hold | stmt | `s39.jpg` — two pan balance almost level | — | — |
| 40 | 5.3 | 235.713 | R | i | 2 | wipe | num · target | *holds `s39.jpg`* — **tighter crop into the pivot**, zoom continues | — | num «क्रॉसओवर» **236.77** · `reveal` |
| 41 | 5.4 | 238.315 | B | o | 1 | wipe | stmt | `s41.jpg` — note bundle paper band | — | — |
| 42 | 5.5 | 244.914 | M | i | 2 | wipe | stmt · target | `s42.jpg` — full rooftop water tank wide | `s42m.jpg` — interest rate card macro | — |
| 43 | 5.6 | 253.420 | **C-R** | o | 1 | wipe | num · target | `s43.jpg` — road bend marker stone weathered | — | num «पाँच लाख» **256.26** · `hero` |
| 44 | 5.7 | 258.400 | B | i | 2 | wipe | stmt · warn | `s44.jpg` — printed page line struck through ink | — | — |
| 45 | 5.8 | 264.111 | B | o | 1 | **SHOVE** | stmt · warn | `s45.jpg` — idle hand pump dry ground | — | `transition` **269.27** |
| 46 | 5.9 | 269.273 | R | i | 2 | wipe | stmt · fund | `s46.jpg` — worn stone doorstep polished dark | — | stamp module **271.97** · `stamp` |
| 47 | 5.10 | 274.018 | B | o | 1 | wipe | stmt | `s47.jpg` — long flight of stone steps up | — | — |
| 48 | 6.1 | 278.658 | B | i | 2 | wipe | stmt | `s48.jpg` — envelope opened with thumb | — | — |
| 49 | 6.2 | 283.951 | B | o | 1 | wipe | stmt | `s49.jpg` — bus stop queue feet and bags | — | — |
| 50 | 6.3 | 290.916 | **C-L** | i | 2 | wipe | stmt · warn | `s50.jpg` — hundred rupee note flat grey card | — | — |
| 51 | 6.4 | 298.299 | B | o | 1 | wipe | stmt | `s51.jpg` — chapati unequal pieces steel plate | — | — |
| 52 | 6.5 | 302.939 | M | i | 2 | wipe | stmt | `s52.jpg` — three unequal grain piles cloth | `s52m.jpg` — pay slip macro | — |
| 53 | 6.6 | 310.008 | B | o | 1 | wipe | num | `s53.jpg` — stack of five notes squared table | — | num «पाँच हज़ार» **311.81** · `hero` |
| 54 | 6.7 | 315.249 | B | i | 2 | wipe | stmt | `s54.jpg` — small coin pile beside large pile | — | — |
| 55 | 6.8 | 320.882 | **C-R** | o | 1 | wipe | stmt · warn | `s55.jpg` — long straight road horizon | — | — |
| 56 | 6.9 | 327.063 | B | i | 2 | wipe | stmt · target | `s56.jpg` — five hundred rupee note and coins counter | — | — |
| 57 | 6.10 | 334.446 | B | o | 1 | **SHOVE** | stmt · warn | `s57.jpg` — blank calendar no marks | — | `transition` **340.08** |
| 58 | 7.1 | 340.078 | B | i | 2 | wipe | stmt | `s58.jpg` — black plastic water tank rooftop morning | — | — |
| 59 | 7.2 | 345.711 | B | o | 1 | wipe | stmt | `s59.jpg` — steel bucket at foot of ladder | — | — |
| 60 | 7.3 | 349.437 | **C-L** | i | 2 | wipe | stmt · warn | `s60.jpg` — bucket carried up ladder rung hands | — | — |
| 61 | 7.4 | 355.435 | B | o | 1 | wipe | stmt | `s61.jpg` — raindrops on small tin lid | — | — |
| 62 | 7.5 | 361.094 | B | i | 2 | wipe | stmt · fund | `s62.jpg` — rain rings spreading water surface | — | — |
| 63 | 7.6 | 367.092 | R | o | 1 | wipe | stmt · fund | `s63.jpg` — heavy rain on full open tank dark | — | stmt **371.76** · `reveal` |
| 64 | 7.7 | 373.561 | B | i | 2 | wipe | stmt · target | `s64.jpg` — empty bucket beside full tank | — | stamp module **376.81** · `stamp` |
| 65 | 7.8 | 379.820 | B | o | 1 | wipe | stmt · warn | `s65.jpg` — dry cracked field beside water channel | — | — |
| 66 | 8.1 | 387.804 | B | i | 2 | wipe | stmt | `s66.jpg` — three plain steel vessels row | — | `tick` **391.14** |
| 67 | 8.2 | 393.750 | **C-R** | o | 1 | wipe | stmt · fund | `s67.jpg` — date circled on wall calendar pen | — | `chip` **396.06** |
| 68 | 8.3 | 401.917 | B | i | 2 | wipe | stmt · warn | `s68.jpg` — empty wallet lying open | — | — |
| 69 | 8.4 | 409.352 | B | o | 1 | wipe | stmt | `s69.jpg` — timber growth rings cross section | — | `chip` **411.06** |
| 70 | 8.5 | 413.809 | B | i | 2 | wipe | stmt · fund | `s70.jpg` — measuring jug topped to next mark | — | — |
| 71 | 8.6 | 419.703 | C-L | o | 1 | wipe | stmt | `s71.jpg` — kitchen shelf jars soft light | — | — |
| 72 | 8.7 | 426.250 | B | i | 2 | wipe | stmt · fund | `s72.jpg` — padlock on small steel cupboard | — | `chip` **428.64** |
| 73 | 8.8 | 433.737 | M | o | 1 | wipe | stmt | `s73.jpg` — three stone steps rising | `s73m.jpg` — closed steel box | — |
| 74 | 8.9 | 439.918 | B | i | 2 | wipe | stmt | `s74.jpg` — open wide mouthed jar low shelf | — | — |
| 75 | 8.10 | 445.133 | B | o | 1 | wipe | stmt | `s75.jpg` — sealed clay pot cloth tie | — | — |
| 76 | 8.11 | 450.348 | R | i | 2 | wipe | stmt · warn | `s76.jpg` — cracked earthen pot spilled dark | — | stamp module **455.13** · `stamp` |
| 77 | 9.1 | 456.816 | B | o | 1 | wipe | stmt | `s77.jpg` — wall clock five past the hour | — | — |
| 78 | 9.2 | 460.986 | C-R | i | 2 | wipe | stmt · fund | `s78.jpg` — bank passbook open beside pen | — | — |
| 79 | 9.3 | 467.402 | B | o | 1 | wipe | stmt | `s79.jpg` — small coin and large coin side by side | — | — |
| 80 | 9.4 | 473.166 | B | i | 2 | wipe | stmt · fund | `s80.jpg` — switch in on position dusty plate | — | — |
| 81 | 9.5 | 478.276 | B | o | 1 | wipe | stmt · warn | `s81.jpg` — coin jar full of coins shelf | — | — |
| 82 | 9.6 | 486.129 | M | i | 2 | wipe | stmt · fund | *recalls `s23.jpg`* — the full steel trunk | *recalls `s26.jpg`* — the two ropes | — |
| 83 | 9.7 | 490.403 | B | o | 1 | wipe | stmt · target | *recalls `s43.jpg`* — the bend marker, later light (new crop + warmer grade) | — | — |
| 84 | 9.8 | 497.917 | R | i | 2 | wipe | stmt · fund | `s84.jpg` — full water tank at dusk roofline silhouette | — | stmt **501.43** · `reveal` |
| 85 | 9.9 | 504.647 | B | o | 1 | wipe | num · **pop** | `s85.jpg` — open ledger and pen laid down | — | num «सब्सक्राइब» **507.17** · `cta` |
| 86 | 9.10 | 508.607 | B | i | 2 | *(final)* | stmt | `s86.jpg` — stone milestone marker open road distance | — | — |

**`foot:` lines are verbatim from the script's cue block.** The 12 scenes that MUST carry
the `ILLUSTRATIVE · ₹5,000/mo · <rate> · monthly compounding` foot — a fact-integrity
requirement, not a design one — are **1, 2, 13, 15, 16, 21, 24, 31, 42** plus the
condition-bearing feet on **4, 11, 14, 17, 37, 41, 43, 49, 50, 52, 53, 56, 65, 73, 79**.
A `num` frame without its foot is a months-figure spoken as a statistic (script §THE FIVE
THINGS #3) — fail the build, do not fix it in the audit.

---

## 7. Continuous-zoom pairs and the `hold` boundary

Three lines re-use their predecessor's photograph (script handoff §5). Creator rule
(firaun 2026-07-23): the same image across lines is **ONE continuous zoom**, never a
self-dissolve.

| pair | scenes | combined | fix |
|---|---|---|---|
| 1.1 + 1.2 | s1 + s2 | **11.736s** | one ken tween spanning both scenes |
| 1.5 + 1.6 | s5 + s6 | **8.966s** | one ken tween spanning both scenes |
| 5.2 + 5.3 | s39 + s40 | **10.115s** | s40 takes a **tighter crop of the same source**, the zoom continuing into the pivot — the script's own remedy, and 5.3 is the CROSSOVER scale-contrast punch, which wants the tighter frame anyway |

**`trans: hold` means a matched-frame boundary.** The outgoing and incoming scenes show the
same photograph at the same zoom phase, so the 0.45s crossfade is invisible and the move
reads as one push. This keeps `data-duration = scene_duration + 0.45` on **every**
non-final scene — the blockframe §5 rule-0 assert holds with no exception carved into it,
which is what makes it safe. **Build requirement:** phase-match the ken tween across the
boundary; a phase discontinuity is exactly the flicker the creator rejected.

`scene.max_scene_seconds` 9.0 is a **per-scene** check and every one of the 86 scenes
passes individually (longest: s16 at 8.741s). ⚠ **If `check_build` measures
`data-duration` rather than `scene_duration`, s16 reads 9.191s and fails** — resolve that
in `check_build`, not by trimming a measured clip.

---

## 8. Port contract for the `-en` cut

This file is the skeleton `storyboard-en.md` ports: **the `s<n>-<part>` ID scheme, the §4
cue ladder, the §3 DOM, and the aperture vocabulary** — so a fix made in one cut travels to
the other. What the `-en` cut MUST change, and must list as explicit divergences with a
reason each:

- **Cycle offset.** This cut opens on `R`. The `-en` cut must open on a different aperture
  (11-swiss-vignelli §7: "the cycle offset must vary by video"). A `-en` storyboard that
  reproduces this aperture sequence is a translation wearing a layout costume.
- **The hero pair.** $10,000 / the second $10,000, not ₹1,00,000 — a US rewrite, not a
  conversion, and a different scene count follows from a different script.
- **Munger's "the first $100,000 is a bitch"** is a US-only beat with no ₹ equivalent; it
  appears nowhere in this cut and will need its own scene, aperture and image slot there.
- **Every rate scene (2.4, 4.10, 6.9)** is Indian institutional evidence — PPF, the
  post-office TD, the AMFI ₹500 SIP minimum, the DEA quarterly notification. None has a US
  counterpart; those scenes diverge structurally, not just in copy.
- Image slots must not reuse a file from this cut. **No image may repeat across videos or
  channels** — key the ledger by md5 and refuse a hash used anywhere.

---

## 9. Images — 93 slots, 87 files

`assets/img/manifest.json` carries the 87 fetch queries. The 6 slots with no query are the
3 continuous-zoom holds (s2, s6, s40) and the 3 deliberate recalls (s82 major, s82 minor,
s83) — a recall re-uses a file from **this** video, which is a memory device, not the
cross-video repeat the design doc forbids.

- **Every scene carries a photograph.** `photo_free_scene_ratio` = 0 (creator rule
  2026-07-28), `image_per_scene: true`. Zero exceptions in this cut.
- **Cut-ins have a structural home, not a floating one.** In `.swiss-band` a floating
  overlay timed to a word is the anti-Swiss move — it dissolves the edge, and the edge is
  the design. The Unigrid answer is the **mosaic minor rectangle** (§2.1 method 3, "major
  and minor pictorial themes"), so the 7 `M` scenes carry the cut-in as a *module*, wiping
  in at +0.85. On the other 79 scenes the keyword rule is satisfied by the bg itself: every
  query above is object-led and names the concrete thing its VO line names (tiffin box,
  post office counter, ₹100 note, chapati, ladder, passbook, padlock).
- **Densest scene, calmest background.** s37 (4.10) is the densest frame in the cut —
  mosaic major + minor + a long statement + a two-clause DEA source foot + amber. Its
  script image ("a wall of identical post office rate boards") is the busiest in the
  script. **Changed to a quiet texture reading of the keyword: a weathered painted board,
  flat even light.** The rate boards' meaning is carried by the copy; the frame does not
  need to shout it. Second densest, s42 (5.5), keeps its tank — it is already calm.
- **Reversed type is MEASURED, not assumed.** The 10 `R` scenes put type on the photograph
  behind a tone block. Measure the left third's mean luminance at fetch time and **reject
  any image above 25%** — there is no scrim to rescue it (script handoff §7,
  11-swiss-vignelli §9). Every `R` query above is already biased dark.
- **Never a phone-screen photo as a background** — s78 (9.2) is the trap, and the script
  pre-empts it: a bank passbook, not a phone. This has shipped wrong three times.
- **Faces fight the typography and are a licence problem.** Hands and objects only; s19,
  s35, s60, s49 are explicitly hands/feet/objects.
- **Repeat-risk pairs inside this cut** — check the md5 before accepting: s42 vs s58 vs s63
  vs s84 (four water tanks), s1 vs s13m vs s21 vs s81 (four coin jars), s43 vs s86 (two
  roadside stone markers). Different shots of the same subject are wanted; the same file
  twice is not.
- Write `assets/img/*.src` prompts and `CREDITS.txt` — the archive rule depends on them
  (`vault/CLAUDE.md` finished-video rule, gotcha 2).

---

## 10. Deliberate placeholders (must be real before publish)

- **The hard-wipe boundary is unproven against `ffmpeg scdet`.** It replaces a
  cross-dissolve that exists for a measured reason (boundary frame-delta 5.85–10.72; five
  of eight boundaries tripped a generic cut detector). Measure chapter 1's master before
  locking chapters 2–9. If it reads as a hard cut, fall back to `dissolve` for the same
  0.45s — the scene arithmetic is identical either way.
- **`bed-resolve` is 248s against a 514.789s cut** (§2). Unfixed, the video dips to silence
  twice, both times mid-argument.
- **Word-level anchoring is not yet wired.** The `f` fractions in §2/§6 are fallbacks; run
  faster-whisper.
- **The two-sizes-per-scene rule has never met a real script.** 11-swiss-vignelli §9 flags
  exactly this. This storyboard resolves it as `bar` + one focal + a 26px foot, with weight
  (900/800/500/200) carrying the rest of the hierarchy — first real evidence either way
  comes out of chapter 1's render.

## 11. Sign-off

- [x] Colour semantics table filled and consistent with the script (§1, incl. the "green ≠ returns" trap)
- [x] Cue times derived from measured `timing.json`, never estimated
- [x] Cue classes declared (anchored vs fixed); the sub-0.8s assembly declared as a cascade with its reason
- [x] Transitions declared: 83 wipes, 2 shoves, 3 holds, 1 final
- [x] One music bed named + 22 SFX cues, no pair inside 0.8s, dry beats declared
- [x] Every scene has a bg photo; densest scene has the calmest bg; cut-ins have a structural home
- [ ] No image hash reused from any prior video on either channel — **fin-assets to verify by md5**
- [ ] `scdet` re-measured on the hard wipe
- [ ] Creator approved (Gate ②) — date: __
