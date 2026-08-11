---
summary: Terminal acceptance pass on ch4-hi's 12 PROMOTED full-res photographs — the sheet built and read, all 12 re-read at full resolution, and every luma clause re-decided on MEASURED files rather than on attempt 1's simulator predictions. 12/12 accepted, 0 re-fetched, 0 dropped. Four frames moved >3 median points against attempt 1's table (s40 −5.1, s33 −4.8, s38 −4.3, s37 −3.4) and the median ORDER changed at ranks 3–8, so attempt 1's rank table must not be quoted downstream; no clause verdict flips. Clause 1 is discharged WITHOUT the retired "by construction" phrase, and the residual exposure it exposes (s33, the chapter's ₹10,000 beat, sits inside a 1.08-point four-way floor tie) is escalated, not buried.
updated: 2026-08-09
source: measured from studio/videos/passive-income-number-hi-ch4/assets-ch4/final/ through the layer stack read out of tools/scaffold/assets/blockframe.css + chapter-design.css; sheet at assets-ch4/final/IMAGES-ch4.jpg
---

# fin-assets — passive-income-number hi ch4, attempt 2 (TERMINAL ACCEPTANCE)

Nothing was fetched. Attempt 1 promoted the 12 files; this pass is the acceptance read that
became this stage's job on 2026-08-09 and that attempt 1 predates.

---

## Ran

1. `python3 tools/image_sheet.py passive-income-number --cut hi --chapter 4` → rebuilt
   `assets-ch4/final/IMAGES-ch4.jpg`, **12 promoted images**, HOLDS reported as `s33, s34b`.
   **Read it.**
2. **Read all 12 promoted jpgs at full resolution**, one at a time — the second, different
   question the sheet cannot answer.
3. Read the two files the ch4 briefs depend on and that no ch4 log has looked at since they
   changed: `assets-ch3/final/s22.jpg` + `.src` (container-ladder rung 1) and
   `assets-ch2/final/s11.jpg` (the tank the 4.7 callback must return to).
4. **Re-measured every promoted file** through the composition chain, read out of
   `tools/scaffold/assets/blockframe.css` (`.bg` `inset:-8%` cover, `grayscale(.32)
   brightness(.62) contrast(1.05)`; the four `.scrim` layers verbatim) and
   `chapter-design.css` (`.has-photo .field { opacity:.38 }`, ground = the storyboard row's),
   ken at mid-scene 1.08, luma BT.601. Script:
   `scratchpad/measure_ch4.py` (throwaway, outside the repo).
5. The mandated cross-project md5 sweep (`find studio/videos vault/videos … | uniq -Dw32`).
6. `python3 tools/pipeline_check.py check assets --slug passive-income-number --cut hi
   --chapter 4` → **PASS assets-hi**. (It failed at task hand-off for the stated reason —
   no `IMAGES-ch4.jpg`. Step 1 is what fixed it; nothing else was needed.)

## Failed

**Nothing was re-fetched and nothing was dropped. 12/12 accepted.** Two findings and one
clause exposure are declared below rather than fixed, each with the reason and the lever.

The one thing that did fail is **attempt 1's number table**, and it fails by exactly the
amount the brief warned about — see Evidence §1.

## Evidence

### 1 · MEASURED, on the promoted files — and where attempt 1's PREDICTION was wrong

`d-med` is the measured median step entering the scene. `p90 − p50` is reported beside the
median and ranks nothing. These are measurements OF THE FILE and still predictions OF THE
ENCODE; only fin-render settles tone.

| Scene | line | ground | sec | **MEDIAN** | **p10** | p90−p50 | d-med | attempt 1 said | Δ |
|---|---|---|---|---|---|---|---|---|---|
| s31 | 4.1 | `#1c2027` | 4.56 | 26.50 | 16.74 | 13.60 | — | 27.1 | −0.6 |
| s32 | 4.2 | `#17291f` | 6.18 | 24.52 | 19.52 | 16.53 | −1.98 | 24.8 | −0.3 |
| s33 | 4.3 | `#17291f` | 6.50 | 24.28 | 19.59 | 15.87 | −0.24 | 29.1 | **−4.8** |
| **s34** | 4.4a | `#291f13` | 5.02 | **44.10** | **28.93** | 10.89 | **+19.82** | 42.0 | +2.1 |
| **s34b** | 4.4b | `#291f13` | 4.14 | **44.23** | 28.06 | 11.69 | +0.13 | 43.4 | +0.8 |
| s35 | 4.5 | `#2d2214` | 7.98 | **23.89** | 18.13 | 10.52 | −20.34 | 24.4 | −0.5 |
| s36 | 4.6 | `#1c2027` | 5.71 | 26.27 | 17.74 | 12.30 | +2.38 | 26.6 | −0.3 |
| s37 | 4.7 | `#301519` | 5.29 | 32.17 | 20.88 | 16.98 | +5.90 | 35.6 | **−3.4** |
| s38 | 4.8 | `#2a2113` | 6.18 | 33.45 | 26.62 | **5.62** | +1.28 | 37.7 | **−4.3** |
| s39 | 4.9 | `#191f28` | 8.40 | 34.61 | 23.41 | 10.95 | +1.16 | 34.0 | +0.6 |
| s40 | 4.10 | `#2e2411` | 5.53 | 24.97 | 16.37 | **25.43** | −9.64 | 30.1 | **−5.1** |
| s35b | cut-in | — | — | 21.93 | 15.55 | 18.20 | — | 23.0 | −1.1 |

    MEDIAN  s34b 44.2 · s34 44.1 · s39 34.6 · s38 33.4 · s37 32.2 · s31 26.5
            · s36 26.3 · s40 25.0 · s32 24.5 · s33 24.3 · s35 23.9
    p10     s34 28.9 · s34b 28.1 · s38 26.6 · s39 23.4 · s37 20.9 · s33 19.6
            · s32 19.5 · s35 18.1 · s36 17.7 · s31 16.7 · s40 16.4

Duration-weighted chapter median **30.25** over 65.50 s.

⚠ **FOUR of eleven frames moved more than 3 points against attempt 1's simulator, and the
median ORDER changed at ranks 3–8**: s38 and s39 swap, s37 drops one, and **s40 falls from
6th to 8th on a −5.1 disagreement**. That is the run-wide warning reproducing itself a sixth
time, on this chapter, in both directions. **Downstream must quote this table, not attempt
1's.** The likeliest cause of the s40 disagreement is visible in its own row: `p90 − p50 =
25.43`, by far the widest in the chapter (sunlit white limestone against deep shadow), so its
median is the one most sensitive to any method difference — and the one most likely to move
again at the encode. fin-render should expect s40 to be the volatile row.

Every margin under ~3 points, flagged as the brief requires:

| Comparison | margin | status |
|---|---|---|
| payoff s34 vs #2 on MEDIAN | **+9.55** | safe |
| payoff s34 vs #2 on p10 (s38) | **+1.92** | **unsafe** — exceeds the 1.0 tie band, under 3; cannot flip the verdict, because the clause says "#1 **or** #2" |
| floor s35 vs s33 | +0.39 | **TIED** (inside 1.0) |
| s33 vs s32 | +0.24 | **TIED** |
| s32 vs s40 | +0.45 | **TIED** |
| s31 vs s36 on median | +0.23 | **TIED** |
| s40 vs s31 on p10 | +0.37 | **TIED** |
| s38 vs s39 on median | 1.16 | outside the band, under 3 — unsafe ordering, and it already flipped once against attempt 1 |

### 2 · The payoff — s34 (4.4, «घर का पूरा राशन»), all four clauses on measured numbers

Weighted across its two framings (5.02 s + 4.14 s): **median 44.16 · p10 28.54.**

| Clause | Requirement | Result |
|---|---|---|
| **Sound-off gate** (binary, first) | type covered, name a concrete object | **PASS** — nine ceramic bowls filled to the brim with red lentils, rajma, chickpeas, basmati, brown rice, black lentils, sesame, wild rice |
| **Top quartile on MEDIAN** | `ceil(10/4)` floored at 3 → top 3 of 10 | **PASS — #1**, +9.55 over s39. Top 3 = s34 44.2 · s39 34.6 · s38 33.4 |
| **p10 #1 or #2** | | **PASS — #1**, +1.92 over s38 |
| **Non-negative median step in** | s33 → s34 | **PASS — +19.82**, the largest step in the chapter |

**Near-zero spread is explicitly NOT claimed as a credit here.** The lowest spread in the
chapter is **s38's 5.62**, not the payoff's; s34's 10.89 is mid-pack (5th of 11). So s34's
win is not the bright-empty-field artefact the CEO sharpening was written against — which is
the check that had to be run, because s34 IS a high-key frame (white marble) and that is the
one failure mode `assets._min_source_yhigh_note` says luma cannot predict.

⚠ **One correction to attempt 1's record.** It called s34 "nine full bowls of **Indian**
staples: urad, rajma, chana, basmati, masoor dal". At full resolution five of the nine are
that; the other four are **wild rice** (a North American aquatic grass, in no Indian ration),
sesame, brown rice and a fourth pulse, on **Carrara marble in a Western food-styling
flatlay**. The frame is still currency-neutral, text-free, brand-free and person-free, and
every bowl is FULL — so it does not argue with "what ₹10,000 buys", which is the test that
killed the previous candidate for showing six near-empty canisters. But the identification
was an overclaim and the place is not India. Kept; declared.

### 3 · Clause 1 — `separation_not_rank_2026-08-09` §1, discharged WITHOUT the retired phrase

The clause is now one-directional: **a substantive beat must not be left in the chapter's
darkest frame.** I am not answering it with "satisfied by construction" — that phrase quoted
the retired converse and is not available.

**Measured, this chapter has no single darkest frame.** The bottom is a **four-way tie
spanning 1.08 points**: s35 23.89 · s33 24.28 · s32 24.52 · s40 24.97. Under §2 those frames
are TIED, so "the chapter's darkest frame" has no unique referent at this separation and the
clause cannot be aimed at one of them.

**What the rule was written to stop is measurably absent.** The chapter's payoff sits
+19.8 above that band and is #1 on both metrics; the longest SCENE (34, 9.159 s) is the
brightest; there is no inversion between argumentative weight and legibility at the top.

**The residual exposure, stated rather than buried.** Of the four tied frames, the one with
a real claim to "substantive" is **s33 — 4.3, «महीने के दस हज़ार रुपये», `num ₹10,000` on the
`--fund` ground, the chapter's hero number.** It measures 24.28, i.e. 6.0 under the chapter's
duration-weighted median and 19.8 under the payoff. Three things bound how bad that is, and
I would not have the editor take my word for any of them:

- **It is not the failure mode.** Per `stock-photo-sourcing.md` BOX §6 the failure is
  contrast collapse and emptiness, not darkness: s33 measures `p10 19.59 / p90 40.15`, spread
  15.87 — real edges, real falloff, the layered edges of a paper stack. It is dark, not empty.
  Dark also helps the white `num` type that is the point of the scene.
- **It cannot be raised without a re-fetch of a slot that is documented unbuyable.** s33 is a
  HOLD crop of s32 — one photograph across 4.2→4.3 as one continuous push — so s33 and s32
  move together, and attempt 1 spent **14 sheets / ~80 cells** proving the storyboard's object
  (a handwritten sum on paper) does not exist in either pool without foreign currency, a brand
  mark or English/European handwriting.
- **It is not a stopping-rule defect** (below), so the rule does not require the round.

If fin-review wants the number beat lifted anyway, the honest lever is a re-fetch of the
s32 parent, not a filter, and it costs the s32/s33 hold geometry (`HOLD_A`, recorded in
`s33.jpg.src`) unless the crop is re-derived in the same move.

### 4 · Floor, stopping rule and the outlier limb

- **Median floor: s35, 23.89, 7.98 s** — 4.5, the ration itemised.
- **Is it the payoff?** No (s34).
- **Is it the longest-held frame?** No under any of the three readings, and I am stating the
  margins because §3 of the ruling dissolved a "second-longest" escape on 0.76 s: scene 34 is
  the longest SCENE at 9.159 s, s39 is the longest single file at 8.40 s, s35 is 7.98 s. s35
  is 0.42 s off s39 — a margin I would call unsafe if the clause turned on it. It does not:
  s35 is third on every reading.
- **Is it an OUTLIER against its own chapter?** **No, and this is the clearest of the three.**
  s35 is 0.39 below the 10th frame and the bottom five span 2.4 points (23.89 → 26.27). A
  dense cluster is the opposite of an outlier. The limb added today does not bite.
- **p10 floor is s40 (16.37), TIED with s31 (16.74).** Reported, not chased — neither is the
  payoff nor the longest-held, and neither is an outlier (s36 sits 1.4 above them).
- **The chapter's OPENING frame, s31, passes the sound-off gate on its own** (gate, not rank):
  type covered, a domed iron-banded chest with a hasp, whole object against a stone wall, a
  broom beside it for scale. Nameable in one word. Measured `p10 16.74 / p90 40.10`, spread
  13.60 — not the collapsed pale slab that failed this gate at ch3's s22.

### 5 · The container ladder — which rung s31's ACTUAL FILE satisfies

Per `container_ladder_2026-08-09` the ladder is **FOUR rungs, s22 → s31 → s58 → s62**, and
**s31 is rung 2**. `storyboard-hi.md` §9c/§10/§12 still carry the retired five-rung ladder
starting at s16; I followed the ruling.

⚠ **Rung 1 is no longer the file the ruling describes, and no ch4 log has said so.** The
ruling was reached by reading a carved sheesham money box with a brass coin slot. That file
was superseded: **`assets-ch3/final/s22.jpg` now ships a stacked yard of terracotta gullaks**
— dozens of fist-sized clay pots, each with a cut coin slit and a vent hole (re-fetched at
ch3 attempt 2 after the encode read as a pale slab; `s22.jpg.src` records it). I read both
files.

**s31 satisfies rung 2 against the file that actually ships.** Rung 1 = a fist-sized clay pot,
many of them; rung 2 = **one** iron-bound domed wooden chest, whole object, filling the frame,
with a floor and a broom for scale. The escalation is read on size and it is unmistakable —
and it is a *larger* step than the one the ruling's own text implied, because the outgoing
rung 1 was a box, not a pot. No text, no brand, no currency, no hand, no face in either.
Declared, as attempt 1 did: s31's painted floral cartouches are Central-Asian/Rajasthani folk
in style — currency-neutral and signage-free, but not provably Indian.

### 6 · What the SHEET showed that no per-image read could — repetition across the chapter

Two labelled HOLD crops (`s33` of s32, `s34b` of s34). Per the tool's own warning and
`storyboard-hi.md` §6b these are one continuous push, **not** repeats, and were not raised.

**Finding A — s37 and s40 are the closest unlabelled pair in the chapter.** Both are sunlit
grey stone with repeated horizontal ledges, three scenes apart, and the desaturation takes a
third of what separates them. This is the chapter-level collision of two *different* declared
returning families meeting for the first time — the tank (ch2 s11 → s37) and the staircase
(ch1 s7 → s40) — and it is a storyboard consequence, not a fetch error. **Kept, declared, not
re-picked**, on four measured/observed grounds:
- their sound-off answers differ, which is the actual test: s37 reads *a water tank with the
  level down*, s40 reads *steps rising*;
- opposite composition — a sunken square pit shot down into vs treads rising away from a low
  angle;
- opposite colour temperature: s37 is cream granite with ochre water, s40 cold blue-grey;
- different grounds (`#301519` vs `#2e2411`) and two loud unrelated scenes between them (a
  chrome tap, a wall of paper);
- and the only cheap fix would take s40 off stone, which breaks a whole-video constant
  (`s7 → s21 → s40 → s61 → s79`) to solve a within-chapter adjacency. That trade is worse.

**Finding B — paper appears twice: s32/s33 and s39, five scenes apart.** Attempt 1 declared
it; on the composed sheet I agree it holds. A warm raking macro of a dozen board edges is not
a cool square-on wall of hundreds of string-tied bundles.

**Not a repeat, checked and cleared:** s34/s34b/s35/s35b are four food cells, but across two
lines with a declared swap and a cut-in, in three different containers (white ceramic on
marble → jute sacks → a steel thali) under three different lights. 4.5 itemises the list, so
the multiplicity is the argument.

**The 4.7 callback verified against the file, not the brief.** ch2's s11 is a red-brick
stepped tank, water low, shot down at an angle; s37 is a pale granite stepped tank, water low,
shot down at an angle. Same object idea, plainly a different photograph — which is exactly
what the storyboard asked for ("a different frame of the same object, never the same file").

### 7 · Full-resolution read, per image — what the sheet could not show

No legible text, brand mark, currency, repeated serial, readable denomination, phone screen,
face or identifiable person in **any** of the 12. Specifically checked and clean: the s38 tap
body (attempt 1 killed a `TESTED 20KG` cast mark on an earlier candidate — this file's body
is plain chrome with a blue tape wrap and no lettering); the s36 signpost (blank on the
visible face, and it is the only sign in the chapter); the s39 bundles (printed rules on the
paper edges, nothing resolvable as words); the s31 chest panels (painted florals, no script).
s37 and s40 carry no plaque or notice.

Place, era and currency: **s35b (a steel thali of carrots, green chillies and coriander) and
s37 (a stepwell) are unmistakably South Asian.** Declared as not-India, currency-neutral and
signage-free: **s36** (a subalpine conifer forest — the second such frame on the books after
ch1's s3), **s40** (weathered ancient stone seating; the Pexels title is the generic "ancient
stone steps", and a viewer reads worn steps, not a country), **s34/s34b** (§2 above), and
**s35's pinto beans** in an otherwise generic sack-shop frame.

### 8 · Licence, dedupe, gates

- **md5 sweep across `studio/videos` + `vault/videos`, both layouts: EMPTY.** No collision
  anywhere on either channel. (Attempt 1 found three here; nothing has re-collided.)
- **CREDITS.txt carries 12 rows for 12 files**, including both derived crops re-keyed onto
  their new filenames with the parent named. **manifest.json carries the same 12 keys.** No
  hand-placed file exists outside either.
- `pipeline_check check assets --chapter 4`: **PASS**.

## Changed

- `studio/videos/passive-income-number-hi-ch4/assets-ch4/final/IMAGES-ch4.jpg` — rebuilt
  (this is what cleared the reported `check assets` failure).
- `studio/videos/passive-income-number-hi-ch4/assets-ch4/final/IMAGES-ch4.json` — rebuilt.
- This log.

**No image was fetched, replaced, cropped, renamed or deleted. `manifest.json`, `CREDITS.txt`
and all 12 jpgs + 12 `.src` files are byte-unchanged from attempt 1.** Nothing was written to
`assets/img/`, `assets/lottie/`, `tools/` or `.claude/`. No lottie was requested by the
storyboard for this chapter and none was sourced. `_cand/` sheets left in place as throwaway.

## Owed

1. **fin-build and fin-render must use §1's table, not attempt 1's.** Four rows moved >3
   points and the median order changed at ranks 3–8. Attempt 1's rank list is superseded.
2. **s40 is the volatile row** — widest spread in the chapter (25.43) and the largest
   prediction disagreement (−5.1). If any measured verdict is going to move at the encode,
   expect it there.
3. **s33 sits inside the floor tie carrying the chapter's ₹10,000 beat** (§3). Escalated to
   fin-review as a judgement it should take deliberately; the only lever is a re-fetch of the
   s32 parent plus re-deriving the s33 crop in the same move.
4. **`owed.storyboard_hi_ladder_stale_in_three_places` is still open**, and this pass adds a
   fourth stale fact to it: **the ruling's own description of rung 1 is now stale too** — s22
   ships terracotta gullaks, not the carved sheesham money box the ruling read. The ladder
   itself is unaffected; the description is not. Worth one edit before s58/s62 are briefed off
   it.
5. **fin-review still owes the encoded look at ch4** — this stage judged image SELECTION on
   the promoted files and has no idea what the composition will do with them.
