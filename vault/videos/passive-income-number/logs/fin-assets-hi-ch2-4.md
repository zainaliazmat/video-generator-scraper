---
summary: Chapter-2 hi asset pass 4. Four photographs changed (s11, s14, s15-crop, s16); two changed and then REVERTED because the round-2 CEO ruling retired the statistic that justified them; one killed at full resolution for dollar signs. Against the new clause the hero s16 is #1 of 13 on MEDIAN, #1 of 13 on p10, spread 10.8, median step in +13.8 — all four hero requirements pass.
updated: 2026-08-08
source: measured from studio/videos/passive-income-number-hi-ch2/assets-ch2/final/, predicted through a render simulator calibrated on the 13 encoded scenes in fin-render-hi-ch2-2.md
---

# fin-assets — passive-income-number hi ch2, attempt 4

## 0 · The ruling landed mid-pass, and it changed two of my verdicts

The round-2 en-ch2 CEO ruling arrived after I had already promoted six files. Two of
them existed only to serve the retired `p90 >= 55` target, so they went back:

| Slot | Bought this pass because… | Re-judged against MEDIAN + the gate | Outcome |
|---|---|---|---|
| **s19** | it was the p90 trough (38.6, 13th) on a consequence example, failing clause 1 | on MEDIAN it is **29.2, 7th of 13 — mid-pack**. It was never the trough on a live measure | **REVERTED** to the phone |
| **s12** | p90 52.7 sat above the hero's 47.1 | p90 no longer ranks; median 36.9 is *below* the hero and it passes the gate | **REVERTED**, and now DECLARED (§4) |

Said plainly, as instructed: **s19 did not need to move and I moved it.** The mast I
promoted is a worse sound-off object than the phone (you recharge a phone, not a mast)
and it would have broken the ch1→ch7 phone callback. Reverting costs nothing and
restores both.

Everything aimed at the hero was re-aimed at MEDIAN + p10 before promotion, so no
promoted file is justified by a retired number.

---

## 1 · Why the last two attempts missed by ~8 points in both directions

Before sourcing anything I built a render simulator — 16:9 cover crop, the `inset -8%`
bleed, the mid-scene ken zoom, the locked `grayscale(.32) brightness(.62) contrast(1.05)`,
the four-layer `.scrim`, then Y' as stored — and fitted it against **all thirteen measured
scenes** in `fin-render-hi-ch2-2.md`. That turns "predict, ship, discover" into "predict,
check the residual, ship".

| Measure | Affine fit | RMS | max abs residual | rho |
|---|---|---|---|---|
| **median** | `0.791x − 6.34` | **1.15** | 2.2 | **0.986** |
| **p10** | `0.818x − 6.83` | **1.23** | 3.1 | **0.976** |
| mean | `0.740x − 0.14` | 1.27 | 3.1 | 0.960 |
| **p90** | `0.605x + 8.11` | **3.75** | **5.8** | **0.672** |

**p90 is not a property of the photograph in this cut, and that is the whole explanation
for both failed attempts.** Two mechanisms, both measurable:

1. **The type sets a floor.** Every dark scene lands 38–45 on p90 regardless of its
   picture — s10 is a near-black night desk (median 21.5) yet reads p90 44.6, and s13
   is 21.0 median / 42.9 p90. The top decile of those frames is the white headline, not
   the photograph.
2. **The draft encode smooths speculars, so texture is taxed and flatness is paid.**
   Residuals sort perfectly by frequency: textured frames run −2.8 to −5.3 (s9 coins,
   s16 notes, s19, s13, s21) and flat frames run +3.8 to +5.6 (s11 sky, s14/s15 paper,
   s12 wall, s20 wall). That is a **~9-point systematic swing that has nothing to do
   with legibility** — and it is why a money close-up can never out-p90 a mid-grey wall.

So the ±8 error attempt 3 reported was not carelessness: it was predicting a statistic
whose photograph-independent component is larger than the effect being chased. Median
and p10 are predictable to ~±1.2. The ruling and this measurement agree, arrived at
independently.

Blurring the simulation before the percentile (box 1→32 px) does not rescue p90 —
RMS only moves 3.78 → 3.56. There is no version of p90 that is briefable here.

---

## 2 · The chapter after this pass — MEDIAN ranks, p10 and p90−p50 beside it

Measured values are from the encode; the four changed files are predicted through the
fits above (so ±1.2 median, ±1.2 p10).

| Scene | line | **MEDIAN** | **p10** | **p90−p50** | (p90) | source | sound-off gate |
|---|---|---|---|---|---|---|---|
| s9  | 2.1 | 24.5 | 15.7 | 16.4 | 40.9 | measured | pass — ₹5 coin stacks |
| s10 | 2.2 | 21.5 | 16.0 | 23.1 | 44.6 | measured | pass — lamp, paper files |
| **s11** | 2.3 | **22.8** | **15.0** | **24.5** | 47.4 | **NEW** | pass — a stepped water tank |
| s12 | 2.4 | 36.9 | 21.7 | 15.8 | 52.7 | measured | pass — two taps |
| s13 | 2.5 | **21.0** | 15.2 | 21.9 | 42.9 | measured | pass — a brass tap |
| **s14** | 2.6 | **25.6** | **16.7** | **18.5** | 44.1 | **NEW** | pass — sharpened pencils |
| **s15** | 2.7 | **26.6** | **16.7** | **17.8** | 44.4 | **NEW crop** | pass — same pencils |
| **s16** | 2.8 | **40.4** | **27.6** | **10.8** | 51.2 | **NEW · HERO** | pass — ₹500 notes + coins |
| s17 | 2.9 | 32.8 | 17.0 | 16.1 | 48.9 | measured | pass — adding-machine keys |
| s18 | 2.10 | 34.0 | 19.0 | 16.0 | 50.0 | measured | pass — same keys |
| s19 | 2.11 | 29.2 | **13.0** | 9.4 | 38.6 | measured | pass — a phone, screen off |
| s20 | 2.12 | 31.0 | 24.0 | 12.0 | 43.0 | measured | ⚠ **FAIL** — a blank grey wall |
| s21 | 2.13 | 35.0 | 23.0 | 8.9 | 43.9 | measured | pass — one proud brick |

    MEDIAN  s16 40.4 · s12 36.9 · s21 35.0 · s18 34.0 · s17 32.8 · s20 31.0 · s19 29.2
            · s15 26.6 · s14 25.6 · s9 24.5 · s11 22.8 · s10 21.5 · s13 21.0
    p10     s16 27.6 · s20 24.0 · s21 23.0 · s12 21.7 · s18 19.0 · s17 17.0 · s14 16.7
            · s15 16.7 · s10 16.0 · s9 15.7 · s13 15.2 · s11 15.0 · s19 13.0

### The hero, clause by clause

| Clause | Requirement | Result |
|---|---|---|
| Sound-off gate (binary, first) | name a concrete object with the type covered | **PASS** — ₹500 banknotes and a coin stack |
| MEDIAN | top quartile = **top 3** of 13 | **#1 of 13**, 40.4, +3.5 on s12 |
| p10 | **#1 or #2** | **#1 of 13**, 27.6, +3.6 on s20 |
| Median step in | s15 → s16 must not fall | **+13.8** |

Honest margin note: the s16 prediction carries the family's known −2.2 median residual,
so the encode will likely read ~38.2 against s12's measured 36.9 — **#1 still, but by
~1.3, which is ~1σ.** p10 is safer: worst-case ~26.7 against s20's 24.0. If fin-render
measures s16 second on median, the lever is s12 (median 36.9), not the hero.

### Clause 1 — the darkest longest-held frame

- **Darkest on MEDIAN is s13 at 21.0** — line 2.5, *«अब मुख्य सवाल, और यही पूरा वीडियो
  है»*, the chapter's own stated central question. That is the substantive placement the
  invariant asks for, reached by construction rather than by argument.
- **Longest-held is s14+s15 at 12.6s**, median 25.6/26.6 (9th/8th) — line 2.6/2.7, the
  one assumed number the whole video carries. Substantive, and no longer the bright
  empty plateau.
- **s19, the frame fin-render flagged, is now 7th of 13 on median** — mid-pack. The
  clause-1 failure closes on the s11 and s14 replacements plus the metric change, with
  s19 untouched.
- ⚠ s19 holds the chapter's lowest p10 (13.0) — the black screen sits centre frame,
  where the type lands. Reported as a floor, not a rank; the p10 clause binds the hero only.

### One thing the gate catches that I cannot fix here

**s20 fails the binary sound-off gate** — a blank grey plaster wall names no object.
It is not leading (median 31.0, 6th) so it disqualifies nothing, but it is only
legible *because fin-build draws twelve cells on it*, and its p10 24.0 is second in the
chapter purely from being empty — the exact "even and empty" artefact the CEO named.
It was deliberately chosen as a calm host for drawn art (see its `.src`). **Flagging
for a ruling: does an art-hosting background have to pass the photograph gate?** If yes,
s20 needs re-sourcing and the drawn grid needs a nameable surface under it.

---

## 3 · Every file changed, declared

| File | Was | Now | Why |
|---|---|---|---|
| `s11.jpg` | rooftop tank on pale sky | ancient Indian stepped water tank | the ruling names the pale-sky field **ineligible to lead**; it was leading on all three |
| `s14.jpg` | dotted notebook, pencil + pen | fan of sharpened pencils on dark cloth | still ~70% blank bright paper, median 2nd/3rd, above the hero, held 12.6s |
| `s15.jpg` | crop of the OLD s14 | **re-derived** crop of the NEW s14 | a derived crop must be re-derived when its parent moves |
| `s16.jpg` | ₹500 + two coin stacks | ₹500 note field, evenly lit | p10 was **14.0, last of 13**; the new clause needs no crushed shadow |
| `s12.jpg` | (unchanged) | (unchanged) | re-examined, KEPT, and the bare-`.src` provenance defect fixed |
| `s17/s18` | (unchanged) | (unchanged) | a promoted replacement was killed at full res, see §5 |
| `s19.jpg` | (unchanged) | (unchanged) | promoted a mast, then reverted — §0 |

`s15` geometry: centre crop **1725×970 from 1880×1057 at +77+43, ratio 0.917553**
against the 0.91754 spec; aspect 1.77835 vs s14's 1.77862. Read side by side at full
resolution — the same pencils, the same diagonal, tighter. ⚠ It must be encoded
`format=yuvj444p` *before* the crop: at yuvj420p the crop filter snaps the width to even
and yields 1724 (ratio 0.917021), a 1 px miss on the spec.

⚠ **s14/s15 changed aspect** — 1880×1245 → 1880×1057 (1.51:1 → 1.78:1). `background-size:
cover` absorbs it, but it means the s14/s15 frames now discard nothing vertically, which
is part of why the plateau is gone.

All four new/changed files are **≥1600 px wide** (1880, 1880, 1725, 1880).

---

## 4 · s12 — the undeclared change, now declared

fin-render was right on both counts: the file changed at 13:50 without declaration, and
it was the only replacement in that pass carrying a bare query string instead of a
rationale. Re-examined on the merits: **KEEP.** It shows two *distinct* wall taps on one
pipe run — a cross-handle bib tap and a hose-fitting outlet — which is exactly 2.4's
"one tap in, one tap out". Its superseded-r1 predecessor is a Turkish ablution fountain
with five identical brass taps and running water: more taps, no in/out reading, wrong
place. A full rationale is now in `s12.jpg.src` and in the manifest.

⚠ Declared: the file is natively monochrome, so `grayscale(0.32)` leaves it fully
desaturated while twelve colour photographs around it keep 68% of theirs.

---

## 5 · Rejections — ~145 cells over 24 sheets in 8 rounds

**The one that would have shipped.** `s17` was replaced with an ornate brass cash
register that read beautifully on the contact sheet and measured well. At full
resolution its keys read **`$60 $50 $40 $30 $20 $10 $9 … $1`** — **dollar signs, large
and legible, on an INR cut, under the line "दस लाख का तीन परसेंट यानी साल का तीस
हज़ार"**. Killed and reverted. Invisible at grid size; caught only by the mandatory
full-resolution read, which is the entire reason that rule exists. The whole cash-register
pool is dollar-denominated, so that direction is retired for this cut.

**The known-bad shoot resurfaced.** Cells 1 and 3 of the final s16 sheet both carry
`6UW 643492` — the prop-money shoot the brief names — and cell 3 shows it on **two notes
in one frame**. Rejected on sight; the promoted cell 6 is from the separately verified
6HP shoot.

Also rejected: an industrial backflow preventer with a legible **BERMAD** brand and two
text warning tags (s12); a Dutch **"Koud / Warm"** hand-lettered two-tap (s12); a
Chinese phone number on a banner and a branded jerrycan (s11); US desert water towers, a
road tanker and brewery silo rows — the "one tank" object does not exist in these pools
(s11, ~29 cells); ceremonial brass puja kalash with identifiable people (s11); high-key
white shavings and colour-pencil craft stock (s14); an **Underwood** typewriter and two
QWERTY/QWERTZ letter keyboards sold as arithmetic (s17); children's toy abacuses with
children's faces (s17, 6/6); and for s19 across ~42 cells, lit screens and brand marks
without exception — **Skype**, **TikTok**, Apple logos, the word "iPhone", a Wacom
tablet, a **PEXELS** watermark, a lock screen reading "HARD WORK FOREVER PAYS", a German
QWERTZ keyboard and a newspaper headline "BURGLARY SHOCK".

Two candidates were rejected purely on **tone under the new measure**: a two-tap dark-brick
frame at median 17.1 (would have made the chapter's second-longest scene its trough by
4 points) and a flat ₹5/₹20/₹50/₹100 fan on white — high-key, old series, and low
denominations arguing *down* against "ten lakh".

⚠ **Tooling note for the next run.** The contact sheet's `drawtext` number badge sits on
the `#111111` letterbox pad, so a naive bounding-box crop of a cell drags in ~50 px of
black and reads every cell **5–10 points too dark**. I shipped two rounds of picks off
those numbers before catching it against a cell whose full file was already on disk.
Find the x-extent below the badge and the y-extent to its right. Two sheets also came
back **1-of-6** with no warning (`s12`), exactly as the brief documents.

---

## 6 · Checks

- `python3 tools/pipeline_check.py check assets --slug passive-income-number --cut hi --chapter 2` → **PASS assets-hi**
- **md5 across all of `studio/`, sweeping sibling chapters** (64 shipping asset jpgs,
  `_cand/`, `renders/`, `snapshots/`, `superseded-*` and `style-a` excluded):
  **0 duplicate hashes.** The only collisions anywhere under `studio/videos` are three
  render contact sheets aliased to themselves (`SHEET-ch1.jpg` / `SHEET.jpg`), which are
  not assets.
- `s17`'s credit reads "by Pixabay" on a Pexels result — the documented cross-pool
  duplicate tell. Hash-checked against every asset image on both channels: **no match.**
- **CREDITS.txt rebuilt 13/13 against the files actually on disk.** Three rows had been
  left naming the wrong photographer by the revert (`--pick` writes a credit row, the
  revert moves the pixels back), and **`s15` was still crediting MESSALA CIULLA for a
  crop of Yeşim Çolak's photograph** — re-keyed in the same move, as was `s18` from `s17`.
- Every changed file read at **FULL RESOLUTION** before acceptance: s16 (serial `962971`,
  `भारतीय रिज़र्व बैंक`, Devanagari `५००`, Indian coins, no second serial in frame so the
  two-notes-one-serial test cannot fire, and the adjacent frame of this shoot was verified
  last pass with two distinct serials), s11, s14, s15, and the two that were killed.
- All 13 slots in `manifest.json`, all 13 with a `.src` rationale — including s12 and
  s19, which had 55-byte and 69-byte bare query strings before this pass.

## Owed to fin-build

- `s14`/`s15` are a new photograph at a new aspect; the 91.755% hold geometry is
  unchanged and re-verified.
- The **drawn wifi arc at s19 is still owed** — only one of that line's two named
  subjects is in frame.
- `s20`'s twelve drawn cells remain load-bearing: without them that scene states no
  count *and* names no object (§2).

## Verdict

**PASS.** 13/13 scenes carry a real photograph; 3 fetched, 1 re-derived, 9 unchanged.
The hero satisfies all four clauses of the round-2 ruling — gate, **#1 of 13 on MEDIAN**,
**#1 of 13 on p10**, step in **+13.8** — and the chapter's darkest frame is now its
stated central question rather than a consequence example. The two frames the brief
suspected of not deserving their place (s11's empty pale sky, s14/s15's blank page) are
gone, and the ruling has since made the first of those mandatory rather than a judgement
call. The one number I would not defend as safe is the hero's ~1.3-point median lead over
s12 after the known residual; if the encode inverts that pair, move s12.
