---
summary: Terminal acceptance pass on en ch4's 13 PROMOTED full-res photographs — IMAGES-ch4.jpg built and read, all 13 re-read at full resolution (plus 10x crop-zooms on six suspect regions), and every luma clause re-decided on measured files through TWO instruments. 13/13 accepted, 0 re-fetched, 0 dropped, 2 candidate sheets spent testing findings rather than assuming them. Unlike hi ch4, attempt 1's number table REPRODUCES (max |Δ| 2.45 on the same instrument, nothing >3) — what moves the chapter is the INSTRUMENT, not the files: the composed chain (field+scrim, the one hi ch4 attempt 2 used) reorders median ranks 4-11 and, decisively, dissolves attempt 1's claim that payoff clause 4 depends on a build knob. Three findings escalated with evidence: the §3 outlier limb is TRIGGERED on s44 and its only remedy is measured to be worse; the tank object family cannot carry the ch4 callback (a storyboard decision, said once, no rounds burned); s45 does not obey its storyboard override and a fresh 6-cell sheet reproduces attempt 1's reason why.
updated: 2026-08-10
source: measured from studio/videos/passive-income-number-en-ch4/assets-ch4/final/ through the layer stack read out of tools/scaffold/assets/blockframe.css + chapter-design.css + the DOM order in passive-income-number-en-ch3/build.mjs:422-432; sheet at assets-ch4/final/IMAGES-ch4.jpg
stage: fin-assets, cut en, chapter 4, attempt 2
---

# fin-assets — passive-income-number en ch4, attempt 2 (TERMINAL ACCEPTANCE)

Attempt 1 promoted all 13 files. This pass is the acceptance read that became this stage's
job on 2026-08-09 and that attempt 1 predates. **No image was replaced.** Two candidate
sheets were spent, both to TEST a finding rather than to assert one; neither produced a
better cell, and both are reported with what they returned.

---

## Ran

1. `python3 tools/image_sheet.py passive-income-number --cut en --chapter 4` → built
   `assets-ch4/final/IMAGES-ch4.jpg`, **13 promoted images**, HOLDS reported as `s42`.
   **Read it.** This is what cleared the reported `check assets` failure; nothing else was
   needed for that.
2. **Read all 13 promoted jpgs at full resolution**, one at a time.
3. **10 crop-zooms at 4-10×** on every region that could hide type: the s41 and s42 door
   plaque, the s43 drafting stencil and pencil tin, the s47 copper riser stamp, the s50
   masthead flourish, the s45 phone top and bottom bezels, the s49 right-hand strokes.
4. Read `passive-income-number-en-ch2/assets-ch2/final/s10.jpg` at full resolution — the
   tank constant s46/s47 inherit — so the through-line verdict is against the FILE, not
   against the brief's description of it.
5. **Re-measured every promoted file through TWO instruments** (§1). Script:
   `scratchpad/measure_en_ch4.py` (throwaway, outside the repo).
6. Swept **seven `background-position` values on s44** to test whether the floor is fixable
   without a fetch.
7. Rendered a **composed/graded 13-cell sheet** (grade + field + scrim + ken, the
   recommended bgpos applied) and read it — the plain sheet is ungraded and cannot show
   whether two frames collapse together under `grayscale(.32) brightness(.62)`.
8. Two candidate sheets, `--candidates 6 --only`: one for **s44** (hazard stripes), one for
   **s45** (screen-away). Both restored to their original manifest queries afterwards; both
   `_cand/` sheets are throwaway and not shipped.
9. The mandated cross-project md5 sweep (`find studio/videos vault/videos … | uniq -Dw32`).
10. `python3 tools/pipeline_check.py check assets --slug passive-income-number --cut en
    --chapter 4` → **PASS assets-en**.

## Failed

**Nothing was re-fetched, replaced or dropped. 13/13 accepted.** Three findings are
declared rather than fixed, each with the measurement and the reason the fix is worse:

- **F1 — the §3 OUTLIER LIMB IS TRIGGERED on s44** (the chapter floor). Not waved away:
  tested with a 7-position bgpos sweep and a 6-cell re-fetch, and the remedy is measurably
  worse than the defect (Evidence §3).
- **F2 — the tank object family CANNOT carry the ch4 callback.** s46 and s47 were asked for
  *the lever at a different angle plus flow*; neither frame contains a lever handle at all,
  neither contains a vessel, and s46's flow is a thin trickle under a line that says
  *"12% is a wider tap"*. Per `chapters._carry_forward_en_ch2_to_ch4_ch5` this is a
  STORYBOARD decision about the object family, so it is stated once and **no round was
  burned on it** (Evidence §5).
- **F3 — s45 does NOT obey its storyboard override.** The override says *screen turned away,
  only the glow on the fingers*; the file is a black screen facing camera. Attempt 1
  justified it by the 2026-08-08 ch1 amendment — which names s1/s3/s4 and extends to s79,
  **not s45**, and whose structural argument does not transfer here (Evidence §6).

Two corrections to attempt 1's record are in Evidence §7. Neither changes a verdict.

## Evidence

### 1 · MEASURED — and the instrument, not the file, is what moved

Two columns, deliberately:

- **RAW** = attempt 1's instrument exactly (cover-fit into the `.bg` `inset:-8%` box at the
  scene's `background-position`, the visible container window, no ken, then CSS
  `grayscale(.32) brightness(.62) contrast(1.05)` in sRGB, then BT.601 luma percentiles).
- **COMP** = the instrument hi ch4 attempt 2 used, and the one a viewer actually sees: the
  same crop **plus ken 1.08 at mid-scene**, then `.field` at `opacity:.38` carrying the
  scene's `--f1` two-stop ground over it, then the **four `.scrim` layers verbatim**
  (`--tint` is unset in this cut, so the top radial is transparent). Layer order taken from
  `passive-income-number-en-ch3/build.mjs:422-432` — `.bg`, then `.field`, then `.scrim`.
  `.grain` (5% overlay) is not modelled.

`p90 − p50` is reported beside the median and **ranks nothing** (p90 is retired for ranking).
`d-med` is the COMP median step entering the scene. These are measurements OF THE FILE and
still predictions OF THE ENCODE.

| Scene | line | ground | sec | **COMP med** | **COMP p10** | p90−p50 | d-med | RAW med | attempt 1 said | Δ (same instrument) |
|---|---|---|---|---|---|---|---|---|---|---|
| s40 `center 35%` | 4.1 | `#2a2113` | 7.304 | **33.23** | 13.52 | 12.20 | — | 72.75 | 71.1 | +1.65 |
| s40 `center` | 4.1 | | | 34.70 | 13.57 | 10.76 | — | 85.64 | 84.1 | +1.54 |
| **s41** | 4.2 | `#0f3a20` | 7.749 | **33.92** | **25.95** | 12.19 | **+0.69** | 79.17 | 79.6 | −0.43 |
| s42 ⟵ crop of s41 | 4.3 | `#0f3a20` | 6.469 | 35.32 | **26.48** | 11.80 | +1.40 | 85.11 | 85.4 | −0.29 |
| s43 | 4.4 | `#1c2027` | 7.200 | 30.64 | 14.42 | 11.90 | −4.68 | 72.60 | 73.0 | −0.40 |
| **s44** | 4.5 | `#2b1418` | 5.711 | **14.91** | **12.15** | 16.96 | **−15.73** | 8.75 | 11.2 | **−2.45** |
| s45 | 4.6 | `#301519` | 6.834 | **37.82** | 20.01 | **8.12** | +22.91 | 102.49 | 102.3 | +0.19 |
| s46 | 4.7 | `#38151a` | 4.744 | 30.19 | 15.59 | 13.52 | −7.63 | 72.60 | 72.4 | +0.20 |
| s47 | 4.8 | `#301519` | 6.233 | 29.01 | 19.57 | 13.76 | −1.18 | 67.36 | 67.2 | +0.16 |
| s48 | 4.9 | `#2b1418` | 5.946 | **21.90** | 13.92 | 18.47 | −7.11 | 33.88 | 34.6 | −0.72 |
| s49 | 4.10 | `#301519` | 7.383 | 25.83 | 18.23 | **18.62** | +3.93 | 50.99 | 50.9 | +0.09 |
| s50 | 4.11 | `#38151a` | 7.801 | 29.03 | 14.63 | **19.34** | +3.20 | 73.02 | 73.0 | +0.02 |
| s51 `center bottom` | 4.12 | `#301519` | 7.435 | 27.98 | 14.52 | 12.13 | −1.05 | 65.23 | 65.2 | +0.03 |
| s51 `center` | 4.12 | | | 24.11 | 13.69 | 15.89 | −4.92 | 47.66 | 47.7 | −0.04 |
| s52 | 4.13 | `#38151a` | 6.469 | 25.62 | 13.72 | 11.06 | −2.36 | 52.76 | 53.5 | −0.74 |

**Chapter duration-weighted COMP median 29.14 over 87.278 s.** Floor→ceiling 14.91 → 37.82.

```
COMP MEDIAN  s45 37.8 · s42 35.3 · s41 33.9 · s40 33.2 · s43 30.6 · s46 30.2
             · s50 29.0 · s47 29.0 · s51 28.0 · s49 25.8 · s52 25.6 · s48 21.9 · s44 14.9
COMP p10     s42 26.5 · s41 26.0 · s45 20.0 · s47 19.6 · s49 18.2 · s46 15.6
             · s50 14.6 · s51 14.5 · s43 14.4 · s48 13.9 · s52 13.7 · s40 13.5 · s44 12.2
RAW  MEDIAN  s45 102.5 · s42 85.1 · s41 79.2 · s50 73.0 · s40 72.8 · s43 72.6 · s46 72.6
             · s47 67.4 · s51 65.2 · s52 52.8 · s49 51.0 · s48 33.9 · s44 8.8
```

⚠ **THE CALIBRATION RESULT IS THE OPPOSITE OF hi ch4's, and that is worth more than a
match.** The brief warned that attempt 1's numbers were predictions and that predictions had
been wrong five times by 7-8 points. **On this chapter they were not predictions.** Measured
on the same instrument, all 15 rows reproduce within **|Δ| ≤ 2.45** (s44), 13 of 15 within
0.75, and **not one row moved 3 points**. attempt 1's §0 validation was real: it measured the
promoted files, it did not simulate them.

**What DOES move is the instrument.** RAW and COMP agree on the top 3 (s45, s42, s41) and the
bottom 2 (s48, s44) and disagree everywhere between: **s50 falls 4th → 7th, s40 rises 5th →
4th, s43 6th → 5th, s46 7th → 6th, s52 and s49 swap at 10/11.** No clause verdict flips, but
one *dependency* does — see §2 clause 4. **Downstream must quote this table.** The RAW column
is kept only so the en lineage (ch2 s21, ch3 s31, and attempt 1's own ch3 cross-check) stays
comparable; COMP is what a viewer sees.

**Every margin under ~3 points, flagged as the brief requires** (COMP, tie band = 1.0):

| Comparison | margin | status |
|---|---|---|
| payoff s41 vs #4 on median (s40) | **+0.69** | **TIED** — inside the band; s41 is in the top 4 either way |
| payoff s41 vs #5 on median (s43) | +3.28 | safe |
| payoff s41 vs #1 on p10 (s42) | −0.53 | **TIED** — and s42 is s41's own HOLD child |
| payoff s41 vs #3 on p10 (s45) | **+5.94** | safe |
| **payoff clause 4 step-in, s40→s41** | **+0.69** | **TIED at zero** — non-negative, but with no separation. See §2 |
| s43 vs s46 on median | +0.45 | **TIED** |
| s50 vs s47 on median | +0.02 | **TIED** |
| s46 vs s50 on median | 1.16 | outside band, under 3 — **unsafe ordering** |
| s47 vs s51 on median | 1.03 | outside band by 0.03 — **unsafe ordering** |
| s51 vs s49 on median | 2.15 | **unsafe** |
| s49 vs s52 on median | +0.21 | **TIED** |
| s52 vs s48 on median | 3.72 | safe |
| **s48 vs s44 on median** | **6.99** | **safe — and it is the finding, see §3** |
| p10 middle cluster s50·s51·s43·s48·s52·s40 | spans **1.11** | **all six TIED** — the p10 middle of this chapter ranks nothing |

### 2 · THE PAYOFF — s41 (4.2), PEAK 1, `$1,500,000`, `hero`, `.sub`, ground `#0f3a20`

The chapter's most substantive beat by construction: the rung-four corpus, the storyboard's
own PEAK 1, and the only scene whose formula completes across an unbroken push into s42.
Scored on **measured COMP numbers**, with the two bgpos recommendations of §4 applied:

| clause | requirement | result |
|---|---|---|
| **Sound-off gate** (binary, runs FIRST) | type covered, name a concrete object | **PASS** — two bank-vault doors set in a brick wall: locking bars, gearwork, rivets, a spoked handwheel and a combination dial. "A bank vault," with no help |
| **Top quartile on MEDIAN** | `ceil(13/4)` floored at 3 → **top 4** | **PASS — #3 of 13.** +0.69 over #4 (TIED with s40, so ranks 3-4 are one tie), **+3.28 over #5** |
| **#1 or #2 on p10** | | **PASS — #2 of 13**, +5.94 over #3. #1 is s42, s41's own continuation crop; on fetched photographs alone s41 is #1 |
| **Non-negative median step in** | s40 → s41 | **PASS — +0.69**, i.e. **inside the tie band, a step of zero, not a rise** |

⚠ **ATTEMPT 1'S §3.1 DEPENDENCY IS DISSOLVED, and this is the one verdict the new instrument
changes.** Attempt 1 wrote: *"clause 4 DEPENDS on one measured bgpos knob handed to fin-build;
without it the step is −4.5 and the clause FAILS… if fin-build does not apply it, the payoff
clause fails and this must come back to assets."* On the composed chain the same two frames
measure **34.70 → 33.92 = −0.78** at `center` and **33.23 → 33.92 = +0.69** at `center 35%`.
**Both are inside the 1.0 tie band**, so under `separation_not_rank_2026-08-09` §2 the step is
TIED at zero either way and the clause is satisfied either way. The knob is a **should**, not a
**must**, and ch4 does not have to come back to assets if it is missed. It is still
recommended, on two independent grounds that survive the instrument change (§4.1).

**Near-zero spread is explicitly NOT claimed as a credit.** The narrowest spread in the
chapter is **s45's 8.12**, not the payoff's; s41's 12.19 is 6th of 13. The payoff did not win
by being empty.

**The chapter's OPENING frame passes the gate on its own** (gate, not rank): s40, type
covered, is a fan of four US twenty-dollar bills raking out of black — nameable in two words,
`p90−p50 = 12.20`, not a collapsed field.

### 3 · THE FLOOR — clause §1 discharged on content, and the §3 OUTLIER LIMB, which BITES

**The floor is s44: COMP median 14.91, p10 12.15, line 4.5, 5.711 s.**

**§1, the live clause — *a substantive beat must not be left in the chapter's darkest
frame*.** I am not answering it with *"satisfied by construction"*; that phrase quotes the
retired converse and is not an available answer.

The clause is discharged **on the content of the beat that actually sits there**, checked
against the chapter's own figures. Line 4.5 is *"Now the warning, and it is the reason most
people never reach any of these rungs"* — `stmt`-only (`This is where the ladder breaks.`),
**no figure, no mechanism, no citation, no `foot:`**, `arch A`, and the second-shortest scene
in the chapter. It is the least argumentatively loaded beat ch4 has. Everything that must be
READ sits in the top half: `$5,000 A MONTH` s40 **#4**, `$1,500,000` s41 **#3**, its completion
s42 **#2**, `13.84%` s50 **#7**. There is no inversion between argumentative weight and
legibility anywhere in this chapter.

**§3, the outlier limb — TRIGGERED, stated rather than buried.**

- Is the bottom the **payoff**? No — s41 is, at #3.
- Is it the **longest-held**? No, and the margin is not close, which matters because §3
  dissolved a "second-longest" escape on 0.76 s: s50 is 7.801 s, s41 7.749 s, s51 7.435 s,
  s49 7.383 s; **s44 is 5.711 s, 12th of 13.**
- Is it an **OUTLIER against its own chapter**? **YES.** s44 is alone at the bottom by
  **6.99 COMP points** — the largest gap anywhere in the chapter, **1.88×** the next largest
  (s52→s48, 3.72) — and by **25.13 RAW points**, **5.4×** the next largest. Both instruments
  agree in kind: one stranded frame, not a cluster. This is the *opposite* of the hi ch4
  worked example, where 2.29 below the band was ruled not-an-outlier **because the bottom was
  a six-frame cluster**. Here it is one frame.

**So the limb bites. It was tested twice, not argued away, and both remedies are worse:**

1. **The knob cannot move it.** Seven `background-position` values on s44:

   | bgpos | COMP med | COMP p10 | RAW med |
   |---|---|---|---|
   | `center 0%` | 15.05 | 12.22 | 9.74 |
   | `center 25%` | 15.11 | 12.20 | 9.53 |
   | `center 35%` | 15.03 | 12.18 | 9.36 |
   | `center` | 14.91 | 12.15 | 8.75 |
   | `center 65%` | 14.71 | 12.14 | 7.96 |
   | `center 75%` | 14.52 | 12.12 | 7.42 |
   | `center bottom` | 14.07 | 12.07 | 6.04 |

   Total span **1.04 COMP points — inside the tie band.** The whole photograph is wet black
   asphalt; there is no brighter part of it to point at. The only lever is a re-fetch.

2. **The re-fetch relocates the floor onto a SUBSTANTIVE beat — the exact defect §1 exists to
   prevent.** Lift s44 out of the bottom and the new floor is **s48 at 21.90**, line 4.9:
   *"The number on the screen is usually real, because a yield is a payout divided by a
   price"* — `stmt: payout DIVIDED BY price`, the chapter's **mechanism** beat, the storyboard's
   own declared **5:00 beat**, and the frame attempt 1 itself named as *"the one I would put in
   front of the gate."* Its separation from the next frame up (s51, 24.11) is **2.21 points —
   outside the tie band**, so it would be a separated single bottom, not a tie member: the
   s21 / s31 shape, on a mechanism beat, replacing an outlier on a transition beat.
   **The limb's remedy creates the §1 violation the ruling's live clause forbids.** §1 governs;
   §3 is the stopping rule, and stopping is what it says to do when continuing costs more.

3. **The pool was checked anyway, not assumed.** One sheet spent
   (`black and yellow diagonal hazard warning stripes painted on a concrete wall
   daylight@pexels`): **4 of 6 cells tiled** — cells 1 and 2's previews failed silently, and
   `_cand/s44.json` confirms all six exist and all six are diagonal-stripe frames but one.
   Cells 1, 2, 3, 4 and 6 are all **diagonal stripes**, which is the one thing in ch4 I must
   not add: **s49 (4.10) already is white diagonal strokes on dark boards**, and two
   diagonal-stripe frames six scenes apart is sound-off rule 4. Cell 5 is a high-voltage
   warning triangle on a flat grey plate — a near-empty field, which is the artefact the
   brief warns every numerical measure eventually crowns, and it names *electricity*, not
   risk. A second sheet in a non-colliding direction
   (`frayed rope under tension about to snap macro hard daylight@pexels`, **6/6 cells**)
   returned two usable cells — a hemp rope with a worn splice against **green bokeh** (a
   third green-bokeh frame after s46 and s47, so a new collision) and a frayed splice against
   **bright blue water** (which would land near s45's 37.8 and put the chapter's *brightest*
   pair on its warning turn, deleting the tonal step §11 asks for). Neither is better.

**s44 is KEPT and DECLARED. It is not the failure mode the sourcing rule names:** per
`stock-photo-sourcing.md` BOX §6 the failure is contrast collapse and emptiness, not darkness.
s44 measures `p10 12.15 / p90 31.87`, spread **16.96 — 4th widest in the chapter**, with source
`YHIGH 144` against the ≥110 gate: full-width crosswalk bars and red/teal/amber/blue light
laid into the water. **It is dark and full, not dark and empty**, and the composed render
(§8) confirms that by eye. If fin-review wants the floor lifted anyway, the honest lever is a
re-fetch of s44 **plus** an accepted relocation of the floor onto s48 — that is a judgement
about which defect the cut prefers, and it belongs to review, not to me.

### 4 · What fin-build should do — two bgpos knobs, both re-measured

#### 4.1 `bgpos: "center 35%"` on s40 — **RECOMMENDED (downgraded from REQUIRED)**

Attempt 1 made this a hard requirement because clause 4 failed without it. On the composed
chain it no longer does (§2), so the requirement is downgraded — but the recommendation
stands on two grounds that survive:

- **It passes on BOTH instruments.** RAW: `center` gives a step of **−6.47** (a real,
  separated failure); `center 35%` gives **+6.42**. COMP: −0.78 vs +0.69, both tied. Applying
  it is the only choice that is correct under either reading.
- **It is the better layout, independently.** s40 is `arch B`, `ctr Y`, carrying
  `$5,000 A MONTH` at `.huge` plus a `foot`. `center 35%` puts black negative space in the
  upper left under the type stack and the notes in the lower right under nothing. Verified in
  the composed render.

#### 4.2 `bgpos: "center bottom"` on s51 — **RECOMMENDED**, both grounds re-verified

COMP median 24.11 → **27.98**, p10 13.69 → 14.52, spread 15.89 → 12.13. And it crops the
photograph's two largest text blocks out of frame: the painted banner
`FREE ⟨SO⟩UP COFFEE & DOUGHNUTS FOR THE UNEMPLOYED` and the `ALBERT HORAN / BAILIFF` sign both
sit above the crop line, as does `PARKING 25¢`. I re-derived the crop geometry from the source
rather than taking it on trust — source 2939×2392, cover to 16:9 keeps 1653 of 2392 rows, and
with `.bg`'s `inset:-8%` the visible window starts at source row **≈853** at `bottom` against
**≈483** at `center`; the banner ends at ≈575 and the HORAN sign at ≈603. What survives is the
queue, the wet pavement and a small `FREE SOUP &` on the shop glass. **Rendered the composed
crop and looked at it** (§8): it still reads unmistakably as a Depression breadline.

#### 4.3 s42 is a DERIVED CROP and it has a parent

`ffmpeg crop=1600:900:280:186` on `s41.jpg`, recorded in `s42.jpg.src`, in `manifest.json`, and
with s41's credit row **re-keyed onto s42.jpg** (same page URL, same author, annotated as a
derived crop). ⚠ **If s41 is ever re-fetched, s42 must be re-derived with the same rect and its
credit row re-keyed in the same move** — an orphaned crop passes every check and shows an
unrelated photograph.

⚠ **The crop is weaker than the storyboard asked for, and it shows on the composed sheet.**
§7 specifies *"the same vault door, tighter on the dial."* The crop is a **1.18× push on the
whole frame** — both doors and most of the brick are still in it, and at composed scale s41
and s42 are all but indistinguishable. Chained with `plateKen` 1.00→1.08 and 1.08→1.16 the
pair will still read as one continuous slow push (which is §6b's requirement, and it is met);
what it will not read as is *arriving at the dial*. Declared for the editor. Not re-cropped:
tightening onto the dial now would need a rect the 1880×1253 source cannot give at ≥1600 px.

### 5 · THE TANK — the object family cannot carry the callback. Said once; no round burned.

Read `en-ch2/assets-ch2/final/s10.jpg` at full resolution first, as instructed. It is **seven
aged brass tap valves with turned brass LEVER handles bolted along a horizontal steel manifold**
over a long copper-brown trough, white tiled wall, raking indoor daylight. Heavy, industrial,
interior.

The sharpened brief for ch4 was **the lever visible at a DIFFERENT ANGLE, plus FLOW.** Measured
against the two files that shipped:

| what was asked | s46 (4.7) | s47 (4.8) |
|---|---|---|
| a brass **LEVER** handle, at a readable angle | **NO** — an ornate cast **cross/rosette knob** on a slim bibcock | **NO** — a white-painted **cross/wheel** handle |
| **flow** | yes, but a **thin twisted trickle** | none (correct for 4.8 — the beat is *it ran out*) |
| a **tank / vessel** | none | none |
| the ch2 constant: *brass tap on a plain steel body under workshop light* | **weak** — an ornamental cast-iron park standpipe, outdoors, trees, a road | **partial** — brass gate valve on a copper riser, but outdoors against foliage |

**Neither frame contains a lever. Neither contains a vessel.** The pair does state a legible
two-beat argument with the sound off — *water running* → *dry mouth, dry second pipe* — and on
the composed sheet they do **not** read as the same photograph (§8), so they are not a
repetition defect. But the thing the through-line is load-bearing FOR — *how much can you draw
each year without emptying it* — is carried by the type, not by the picture, at both 4.7 and
4.8. **Per `chapters._carry_forward_en_ch2_to_ch4_ch5` that is a STORYBOARD decision about the
object family, not another fetch round.** ch2 spent 6 sheets / 36 candidates on it and ch4
spent 4 more; the pools do not hold a tank-with-a-tap. Stating it, and stopping.

⚠ **AND s46 HAS ALREADY SPENT s57'S STATEMENT.** §10's four-frame ladder is *low flow → wide
open, water running out → level low, still open → **barely cracked, a thin stream into a tin
cup***. s46 shipped as **a thin trickle**, so ch5's s57 has nothing left to escalate *down*
to, and 4.7's own line — *"12% is a **wider** tap"* — is under-supported by a narrow stream in
the frame beneath it. This is the single most useful thing in this section for whoever briefs
ch5: **re-brief s57 against the FILE, not against §10's text**, exactly as the container-ladder
correction had to be made on the hi cut.

### 6 · s45 — verified against the override, and it does NOT obey it

The storyboard's §10 override for s45 (4.6) reads: *"hand holding a phone with the **screen
turned away**, only the glow on the fingers — same rule, and **this is the most tempting
violation in the cut** because the frame is *about* a feed."*

**The promoted file is a hand holding an iPhone with the screen FACING CAMERA**, switched off,
in bright outdoor daylight against sunlit foliage. So the override is not obeyed. Everything
below is measured, and the disposition is *declare and escalate*, not *re-fetch*:

- **No hard-rule violation.** The standing rejection targets *a lit screen carrying someone's
  brand and being the brightest thing in frame*. This screen is black, carries nothing, and is
  **not** the brightest thing — the sunlit leaves are. 10× crop-zooms on the top and bottom
  bezels found **no wordmark and no model name**; the only brand signal is the silhouette
  itself (a home-button iPhone), which carries no readable text.
- **The amendment attempt 1 leaned on does not cover this slot.** The 2026-08-08 ch1
  amendment approves a black-screen phone on **s1 / s3 / s4**, extends to **s79**, and says
  *"applied identically to all three, which is what makes it a decision and not an
  exception."* It does not name s45, and s45 has its **own, separate, unamended** override row
  in the same table. More importantly its *structural* justification — *a face-down phone in a
  dark room has no highlights **by construction** and cannot clear `YHIGH ≥ 110`* — **does not
  transfer**: s45 is an outdoor daylight frame at source `YHIGH 209`, where a screen-away
  phone clears the gate trivially. So the pool had not been proven empty for THIS slot.
- **So I proved it, this session.** One sheet, `hand holding up a phone seen from behind
  screen turned away from camera no logo daylight@pexels`, **6/6 cells**: cell 1 a green-screen
  mock plus hair, cell 2 a man's face, cell 3 an identifiable man at half-length, cell 4 the
  **only** true screen-away frame — and it carries a distinctive triple-camera island (brand
  identifiable by design) plus a partly visible person, cell 5 **the promoted file itself**,
  cell 6 a green-screen mock on a café table. Attempt 1's finding reproduces exactly: this
  pool answers *screen turned away* with a brand mark or a person.
- **The residual risk is a sound-off one, and it is the reason this is escalated rather than
  closed.** Sound-off rule 2 asks whether the image *argues* with the line. Line 4.6 is
  *"Somewhere on your **feed** there is a payout advertised at ten percent…"* over three chips
  `10% · 12% · "monthly income"`. A phone that is plainly **switched off**, held in a garden,
  says *there is nothing on this screen* — which is nearer to contradicting the line than
  supporting it. The storyboard's *glow on the fingers* exists precisely to say *there IS
  something on the screen, we are just not showing it*.
- **Second, smaller conflict, measured.** §10 routes the five chip cascades (s2, s6, s26,
  **s45**, s64) to *near-flat, low-key* subjects. s45 is the chapter's **brightest** frame
  (COMP median 37.82, #1 of 13) and the only one with a large saturated green mass surviving
  the grade. Its spread is the chapter's *narrowest* (8.12), so it is flat — but it is not
  low-key, and on the composed sheet it is the one cell that jumps out of the run.

**Disposition: KEPT, and routed to fin-review as a storyboard-override decision** — the same
class of question as the tank, not a sourcing failure. If review wants the override honoured,
the only frame the pool offers is a phone back with a brand-identifiable camera module, which
trades a declared deviation for a rule violation.

### 7 · The full-resolution read, per image — including two corrections to attempt 1

**No legible text, readable brand mark, currency error, repeated serial, readable
denomination, lit phone screen, face-as-subject or fabricated source document in any of the
13.** Specifically hunted at 4-10×:

| what was checked | verdict |
|---|---|
| **s41 / s42 door plaque** | A two-line engraved maker's plate on the left door, out of focus in the source. At 10× the letterforms do **not** resolve; the shape is consistent with `…SAFE & LOCK CO.` and no word can be read. **KEPT — but attempt 1's size figure is wrong and the correction matters**: it called this *"~1-1.5% of frame width."* Measured, it is **~9.6% of s41's width and ~7.5% of s42's**, i.e. **~145-185 px at 1920 output**, on the chapter's two highest-stakes frames. It survives on FOCUS, not on size — a sharp plate at that size would have been a kill |
| **s47 copper riser** | A raised/printed mark low on the riser, ~7% of frame width, badly out of focus; resolves to nothing readable at 9× |
| **s43 drafting stencil + pencil tin** | Embossed geometric template, no maker's name legible; pencils are plain blue/yellow with no printed brand in frame |
| **s50 masthead** | One decorative blackletter flourish and a `1`/`+` register mark on the top sheet; **no word, no headline, no date** anywhere. Era-neutral, not era-wrong |
| **s45 phone bezels** | No wordmark, no model name (§6) |
| **s40 currency** | Genuine current-series US $20s — correct intaglio, security-thread ghost, Jackson watermark in the second note. **Only one serial is in frame and it is clipped by the frame edge (`JF 1822…`)**, so there is no two-notes-one-serial to check and no complete serial to be a liability. Four notes are fanned, not the storyboard's five — cosmetic |
| **s51 archival signage** | `FREE SOUP COFFEE & DOUGHNUTS FOR THE UNEMPLOYED`, `ALBERT HORAN / BAILIFF`, `PARKING 25¢`, `FREE SOUP &` — all legible at full size, the first three removed by the §4.2 crop. Public domain (NARA), so no licence exposure; the front-row faces ARE distinct against §10's *"faces indistinct"*, and the subjects are 1931 and the claim is historical, not personal |

⚠ **CORRECTION 1 — s49 is not what attempt 1 says it is.** attempt 1 recorded *"a weathered
board wall with peeling paint, raking light across it."* At full resolution and at 5× it is
**white SPRAY PAINT on dark blue-black weathered planks** — soft-edged strokes with overspray
speckle and discrete droplets, not light and not peeling paint. Three consequences, all
declared: (a) no word or letterform resolves, so there is **no text defect**; (b) it is the
chapter's most **graphic** frame, `p90−p50 = 18.62`, 2nd widest — and s49 is the chapter's one
`art-forward` scene carrying the drawn `yield-fraction` at `opacity:.52`, which §10 routes to
the *calmest* subject. Strong white diagonals under a drawn mechanism is a legibility risk
fin-build and fin-review should look at on the encode; (c) the manifest/`.src` query
(`peeling paint on a weathered wooden wall…`) is the record of what was *asked for*, not of
what arrived, and is left unchanged.

⚠ **CORRECTION 2 — s48's frame is a Chinese herbal apothecary**, not a generic herbalist's:
a brass pan on chains loaded with dried root slices, with a dou-cheng counterweight on a wooden
beam and apothecary jars behind. No signage, no language, no character in frame, so a viewer
reads *an old brass scale*; kept and declared under *every frame is American*, as attempt 1
did — but named precisely here so the next reader is not surprised. Note also that only **one**
pan is in frame against §7's *"a two-pan balance where the right pan has dropped"*: the frame
shows the machine that compares, it does not show a comparison. Weakest gate-3 in the chapter
alongside s43 and s49.

**US-market sweep:** no non-US currency, signage, plate, plug or vehicle in any accepted
frame. Currency-neutral-and-declared: s46 (an ornamental cast-iron park standpipe, no mark),
s47 (outdoor copper pipework), s48 (above), s52 (bare dirt). s51 is the one identifiably
American frame and it is the archival exception.

**Hands:** the chapter carries **two** hand frames, s43 and s45. §10 enumerates s18, s33, s45,
s53, s58 as the only frames with a hand, so **s43 is an addition** (attempt 1 flagged this; it
survives). No face, no wrist brand, hands only — the *rule* holds, only the enumeration moves.

### 8 · What the SHEETS showed that no per-image read could

Two sheets were read, and they answer different questions.

**`IMAGES-ch4.jpg` (the mandated one, ungraded).** 13/13 cells, `s42` correctly labelled
`HOLD crop of s41` and **not** raised as repetition per the tool's own instruction.

**A composed/graded 13-cell render** (grade + field + scrim + ken, with the §4 bgpos applied)
— built because the mandated sheet is ungraded and cannot show whether two frames *collapse*
under `grayscale(.32) brightness(.62)`. Findings, all from the composed look:

- **NO TWO CELLS SAY THE SAME THING.** The only near-identical pair is s41/s42, which is the
  labelled HOLD.
- **The s46 / s47 adjacency worry is RESOLVED, not merely argued.** Ungraded they look alike —
  adjacent scenes, both a metal tap against green bokeh in daylight. **Composed they do not:**
  s46 is a dark ornate column with a bright road strip on the left, s47 a flat grey wall panel
  with copper verticals. Different masses, different compositions, and the flow/no-flow
  difference survives the grade. Kept.
- **s45 is the one cell that jumps out of the run** — brightest, and the only large surviving
  chroma mass (§6).
- **s44 reads by eye exactly as it measures**: a near-black frame with the crosswalk bars and
  the coloured reflections as its only content. Full, not empty — but visibly a hole in the
  tone run.
- **Three pale-paper-dominant frames** — s43 (4.4), s50 (4.11), and s49's white strokes (4.10).
  s49 and s50 are adjacent. Checked and **cleared**: a stack of folded newsprint shot edge-on
  and a spray-painted plank wall share a tone band and nothing else — different objects,
  different depth, different direction. Reported because it is the kind of thing only the
  grid shows, not because it is a defect.
- **s51 at `center bottom` still reads as a breadline** with the two big banners gone.

### 9 · Licence, dedupe, gates — each actually run

- **md5 sweep across `studio/videos` + `vault/videos`, both layouts, the mandated command
  verbatim: EMPTY. 205 files hashed.** No collision anywhere on either channel. ⚠ Note for the
  record: attempt 1's declared s48 collision with
  `passive-income-number-hi-ch1/assets-ch1/**style-a**/s7.jpg` **does not appear**, and
  correctly so — the mandated `find` filters to `*/final/*.jpg` and `*/assets/img/*.jpg`, and
  `style-a/` is a retired working copy under neither. The deviation attempt 1 escalated is
  therefore **outside the check's declared scope by design**, not passing it by accident. Left
  as attempt 1 declared it; hi ch1's **live** `final/s7.jpg` is a different photograph, so no
  viewer can see this frame twice.
- **`CREDITS.txt` = 13 rows, 13 distinct keys; `manifest.json` = 13 keys; 13 files on disk;
  `.src` present for all 13 and byte-matching its manifest query** (asserted programmatically
  after the two temporary re-queries were reverted — 0 mismatches). The one hand-placed file
  (s42) carries s41's row re-keyed onto its own filename.
- **≥1600 px**: all 13, min 1600 (s42 by construction); s45 is 1733×1300, the narrowest
  fetched.
- **Source `YHIGH ≥ 110`**: all 13 per attempt 1's per-file measurements, min 144 (s44).
- `pipeline_check check assets --slug passive-income-number --cut en --chapter 4`:
  **PASS assets-en** (it failed at hand-off for the stated reason — no `IMAGES-ch4.jpg`; step 1
  is what fixed it).

## Changed

- `studio/videos/passive-income-number-en-ch4/assets-ch4/final/IMAGES-ch4.jpg` — built (this
  is what cleared the reported `check assets` failure).
- `studio/videos/passive-income-number-en-ch4/assets-ch4/final/IMAGES-ch4.json` — built.
- `studio/videos/passive-income-number-en-ch4/assets-ch4/final/_cand/s44.jpg` + `s44.json`,
  `_cand/s45.jpg` + `s45.json` — **overwritten** by the two test sheets of §3 and §6.
  Throwaway: not in the manifest, not shipped, and attempt 1's own candidate sheets for those
  two slots are consequently gone. Recorded so nobody looks for them.
- This log.

**No image was fetched into a slot, replaced, cropped, renamed or deleted. All 13 jpgs, all 13
`.src` files and `CREDITS.txt` are byte-unchanged from attempt 1.** `manifest.json` was
temporarily re-queried on `s44.jpg` and `s45.jpg` to build the two test sheets and **restored**;
it is byte-equivalent in content to attempt 1's (13 keys, same queries, verified against every
`.src`). Nothing was written to `assets/img/`, `assets/lottie/`, `tools/` or `.claude/`. The
storyboard asked for **no lottie** in this chapter and none was sourced.

## Owed

1. **fin-build and fin-render must quote §1's COMP table, not attempt 1's.** The files did not
   move (max |Δ| 2.45 on the matched instrument) but the *instrument* did, and median ranks
   4-11 are reordered. The RAW column is kept only for lineage comparability with ch2/ch3.
2. **Attempt 1's §3.1 "REQUIRED, the payoff clause rides on it" is superseded.**
   `bgpos: "center 35%"` on s40 is now a **recommendation** — clause 4 is satisfied with or
   without it under `separation_not_rank_2026-08-09` §2. **ch4 must not be sent back to assets
   if fin-build omits it.** Apply it anyway: it is correct under both instruments and it is
   the better layout for a `.huge` + `foot` stack.
3. **`bgpos: "center bottom"` on s51 — still recommended**, and now on re-verified geometry
   (visible window starts at source row ≈853 vs ≈483; the two big banners end at ≈575 and
   ≈603).
4. **s44 carries a TRIGGERED §3 outlier limb** (6.99 COMP / 25.13 RAW below the next frame,
   the largest gap in the chapter by 1.9× / 5.4×). §1 is clean — 4.5 is the chapter's least
   substantive beat — and the only remedy relocates the floor onto **s48**, the mechanism beat,
   at a separation of 2.21, i.e. outside the tie band. **This is a judgement for fin-review
   about which defect the cut prefers**, and both options are now measured rather than
   asserted.
5. **THE TANK: a storyboard decision is owed, not a fetch round.** s46/s47 contain no lever and
   no vessel; the callback is carried by type at 4.7 and 4.8. ⚠ **And s46 has already spent
   s57's statement** — §10's ladder ends on *"barely cracked, a thin stream into a tin cup"* and
   s46 already IS a thin stream. **Re-brief s57 against the FILE, not against §10's text**, the
   same correction the hi cut needed on its container ladder.
6. **s45 is escalated as a storyboard-override decision** (§6), with a fresh 6-cell sheet
   proving the pool answers *screen turned away* with a brand mark or a person. The sound-off
   risk — an off phone under *"somewhere on your feed"* — is the part worth a decision, not the
   policy wording.
7. **s49 is graphic, not calm, and it is the chapter's one `art-forward` frame.** Strong white
   spray-paint diagonals under the drawn `yield-fraction` at `opacity:.52` is a legibility risk
   that only the encode settles. Look at it once.
8. **s42's crop is a 1.18× push on the whole frame, not the dial** (§4.3). The continuous-push
   requirement is met; *arriving at the dial* is not. Design call for the editor.
9. **fin-review still owes the encoded look at ch4** — this stage judged image SELECTION on the
   promoted files and has no idea what the composition will do with them.
