---
summary: First fetch for hi ch5 — 17 scenes (s41–s57) plus the two framing-swap crops s52b/s57b, 19 files, all promoted, all read at full resolution, sheet built and read, `check assets --chapter 5` PASS. 12 contact-sheet rounds across 8 slots; 5 promoted files were killed AFTER promotion (s48 a Philippine government notice board priced in PESOS, s55 legible Turkish newsprint under the India beat, s50 a 95%-empty white ceiling, s51 source YHIGH 96, s47 a Twitter logo — cropped out rather than re-fetched). s41 re-briefed off terracotta onto glass, discharging `owed.ch5_s41_collides_with_the_new_ch3_opener`.
updated: 2026-08-10
source: measured on the promoted files in studio/videos/passive-income-number-hi-ch5/assets-ch5/final through the layer stack read out of tools/scaffold/assets/blockframe.css + chapter-design.css; sheet at assets-ch5/final/IMAGES-ch5.jpg
---

# fin-assets — passive-income-number hi ch5, attempt 1

Seventeen scenes, the biggest chapter in either cut. Nothing existed; this was a real fetch.

---

## Ran

1. Read `vault/CLAUDE.md`, `tools/format/fin-assets.json`, `tools/packs/fin-assets.md`,
   `vault/videos/passive-income-number/notes.md` (owed items + all five
   `rulings_binding_on_both_cuts` entries), `script-hi.md` ch5, and `storyboard-hi.md`
   §6b/§9c/§10/§12 + the scene table rows 41–57.
2. Read the three shipping sibling sheets before briefing anything —
   `assets-ch1/final/IMAGES-ch1.jpg`, `assets-ch2/final/IMAGES-ch2.jpg`,
   `assets-ch3/final/IMAGES-ch3.jpg`, `assets-ch4/final/IMAGES-ch4.jpg` — so the
   returning objects (the tank, the staircase, the container ladder, the ledger) are
   briefed against **the files**, not the storyboard's stale descriptions.
3. **12 contact-sheet rounds, ~71 candidate cells**, over 8 of the 17 slots
   (`--manifest … --candidates 6 --only …`). Slot cost: s48 ×5, s54 ×6 (round 6 was the
   one that landed), s47 ×3, s50/s51/s55/s57 ×2, s41/s42/s45/s49/s52 ×2–3.
4. **Read all 19 promoted jpgs at FULL RESOLUTION**, one at a time.
5. Cross-project md5 sweep (`find studio/videos vault/videos … | uniq -Dw32`) — twice,
   before and after the late re-picks. Empty both times.
6. Measured every promoted file through the composition chain
   (`.bg` inset:-8% cover + `grayscale(.32) brightness(.62) contrast(1.05)`, `.field` at
   `.38` over the storyboard's ground, the four fixed `.scrim` layers, ken 1.08 at
   mid-scene, luma BT.601). Script: `scratchpad/measure_ch5.py`, throwaway, outside the repo.
7. `ffmpeg` for three crops: the s47 brand-mark removal and the two framing-swap
   derivations s52b / s57b.
8. `python3 tools/image_sheet.py passive-income-number --cut hi --chapter 5` → 19 cells,
   HOLDS reported as `s52b, s57b`. **Read it**, then read it again after the two late
   re-picks.
9. `python3 tools/pipeline_check.py check assets --slug passive-income-number --cut hi
   --chapter 5` → **PASS assets-hi**.

## Failed

**19/19 accepted, 0 dropped, 0 cut-ins dropped.** Nothing is owed to fin-build.

What failed is the *picks*, five times, and every one was caught by a different check —
that is the whole content of this section.

| # | slot | what was promoted | what killed it | which check |
|---|---|---|---|---|
| 1 | **s48** | a rusty glass-fronted notice board, anonymous warm texture on the sheet | `Republic of the Philippines / Dumaguete City / City Economics Enterprises Department` + `MEAT VENDORS CHRISTMAS PARTY` + **`200.00 PESOS WORTH OF FOODS`** — a foreign agency and a foreign currency, on the one frame whose job is an Indian sovereign rate | **full-resolution read** (invisible at grid size) |
| 2 | **s55** | a glass teacup on a printed page — the chapter's PAYOFF frame | the page is legible **Turkish** newsprint (`Japon komedi oyunu`, `General Tsuchida`) under «भारत के अपने आँकड़ों पर हुई रिसर्च», i.e. the wrong place asserted on the beat where place *is* the argument | **full-resolution read** |
| 3 | **s50** | a bare bulb on a white ceiling | the bulb is ~5% of the frame; the other ~95% is a featureless white field. It clears YHIGH trivially and would have measured near the top on median — the exact trap `payoff_clause_and_metric_2026-08-08` §2 names, and it would have put `₹5,550 A MONTH` on the chapter's emptiest photograph | **full-resolution read + the emptiness clause** |
| 4 | **s51** | a dark vaulted room with a blown-out doorway | **source YHIGH 96 < 110** | **`check assets`** |
| 5 | **s47** | the Surathkal post office | a **Twitter bird logo + @handle** on a banner across the top — a readable brand mark | **full-resolution read**; fixed by cropping, not by re-fetching (below) |

Two more never reached promotion but are worth the line: the `blank blue enamel plate`
shortlisted for s48 is a flat panel filling 85% of the frame and reads as a **UI element
behind the type** (the high-key flat-texture failure named in
`format.json assets._min_source_yhigh_note`); and every `calendar` cell for s48 carried a
legible month (`November`, `JUNHO`, `SAT 18 MAY`, `January`) — the ch4 wrong-date failure.

## Evidence

### 1 · `owed.ch5_s41_collides_with_the_new_ch3_opener` — DISCHARGED

The storyboard briefs s41 as *"a hairline crack running across a dry clay pot"*. ch3's
shipping `s22.jpg` is a stacked yard of **terracotta gullaks** (`container_ladder_CORRECTION_2026-08-09`),
so the collision is the **material**, not the crack. **The crack is kept and the material
is changed to GLASS**: a window pane with cracks radiating from one point over blurred
tiled roofs. Verified at full resolution that it is a *building* window and not a device
screen (there is a putty line and a timber sill at the bottom edge) — the never-a-screen
rule is the one that has shipped three times undetected.

Round 1's re-brief attempt (a loose thread unravelling from knitted cloth) returned five
flat knit **textures** and one ball of yarn: no object, no unravelling, all six refused.
That round is why the glass answer exists.

### 2 · The storyboard's stale ladder — read, and not followed

`owed.storyboard_hi_ladder_stale_in_three_places` holds. **ch5 contains no container-ladder
rung** (the live ladder is s22 → s31 → s58 → s62), and §10's five-rung text was not allowed
to pull a rung into this chapter. What §10 *did* govern here is the **tank**, and it was
briefed against the shipping files rather than its own text:

- §10 says the tank's constant is *"the plain steel body under workshop light"*. **It is not.**
  ch2 `s11.jpg` is a brick stepped water tank and ch4 `s37.jpg` is a granite stepwell — the
  hi cut took §10's own declared fallback and the stepped stone tank is what shipped twice.
  s44 and s45 continue **that** object, not the steel one.
- §10 assigns *"wide open"* to s44. The script's own cue for **5.2** is *"a tap opened wide,
  water hitting a bucket hard enough to splash out"* — the same statement two scenes earlier.
  Both cannot ship. **Water was moved off s42 entirely** (it is now a pressure gauge with the
  needle high) and s44/s45 keep the whole arc: outlet running hard → the tank dry.

### 3 · MEASURED, on the promoted files

`d-med` is the measured median step entering the scene. `p90 − p50` is reported beside the
median and **ranks nothing**. These are measurements OF THE FILE and still predictions OF
THE ENCODE — `method_learned.predictions_missed_a_sixth_time_2026-08-10` applies to the
step from here to fin-render, not to the numbers themselves.

| scene | line | ground | sec | **MEDIAN** | **p10** | p90−p50 | d-med | src YHIGH |
|---|---|---|---|---|---|---|---|---|
| s41 | 5.1 | `#1a1e24` | 4.09 | 40.92 | 26.10 | 18.02 | — | 249 |
| s42 | 5.2 | `#301519` | 5.82 | 21.84 | 14.37 | **32.96** | −19.08 | 225 |
| s43 | 5.3 | `#1c2027` | 8.09 | 22.35 | 15.82 | 9.77 | +0.51 | **117** |
| s44 | 5.4 | `#38151a` | 6.23 | 24.06 | 18.00 | 15.09 | +1.71 | 164 |
| s45 | 5.5 | `#3b1219` | 4.22 | 35.42 | 21.96 | 13.93 | +11.36 | 211 |
| **s46** | 5.6 | `#38151a` | 3.99 | **44.43** | **33.53** | 8.60 | +9.01 | 217 |
| s47 | 5.7 | `#1a1e24` | 6.78 | 27.32 | 17.20 | 15.66 | −17.12 | 175 |
| s48 | 5.8 | `#2a2113` | 6.36 | 22.26 | 14.71 | **8.24** | −5.06 | **112** |
| **s49** | 5.9 | `#191f28` | 5.95 | **43.79** | **31.21** | 9.41 | +21.53 | 222 |
| s50 | 5.10 | `#2e2411` | 8.09 | 23.12 | 16.58 | 17.38 | −20.67 | 183 |
| s51 | 5.11 | `#1c2027` | 6.08 | 24.99 | 18.85 | 13.97 | +1.87 | 160 |
| s52 | 5.12a | `#301519` | 5.09 | 31.85 | 18.69 | 14.87 | +6.86 | 182 |
| s52b | 5.12b | `#301519` | 4.51 | 31.78 | 17.10 | 15.79 | −0.07 | 207 |
| s53 | 5.13 | `#131f2c` | 7.93 | 34.57 | 17.02 | 20.84 | +2.79 | 223 |
| s54 | 5.14 | `#0c1a2c` | 7.93 | 23.95 | 16.63 | 11.17 | −10.62 | 203 |
| **s55** | 5.15 | `#372a0c` | 5.95 | **41.15** | **25.73** | 13.99 | **+17.20** | 225 |
| s56 | 5.16 | `#38151a` | 7.02 | 25.21 | 17.01 | 12.03 | −15.94 | 196 |
| s57 | 5.17a | `#2e2411` | 5.28 | 20.88 | 15.98 | 12.54 | −4.33 | **121** |
| s57b | 5.17b | `#2e2411` | 3.91 | 19.91 | 16.04 | 11.17 | −0.97 | **117** |

```
MEDIAN  s46 44.4 · s49 43.8 · s55 41.1 · s41 40.9 · s45 35.4 · s53 34.6 · s52 31.8
        · s52b 31.8 · s47 27.3 · s56 25.2 · s51 25.0 · s44 24.1 · s54 24.0 · s50 23.1
        · s43 22.4 · s48 22.3 · s42 21.8 · s57 20.9 · s57b 19.9
p10     s46 33.5 · s49 31.2 · s41 26.1 · s55 25.7 · s45 22.0 · s51 18.8 · s52 18.7
        · s44 18.0 · s47 17.2 · s52b 17.1 · s53 17.0 · s56 17.0 · s54 16.6 · s50 16.6
        · s57b 16.0 · s57 16.0 · s43 15.8 · s48 14.7 · s42 14.4
```

Duration-weighted chapter median **28.75** over 113.32 s. Every source clears
`min_source_yhigh` 110; the four thin margins are **s48 112, s43 117, s57b 117, s57 121**
and they are named because a re-crop or a re-encode downstream could move them.

### 4 · The PAYOFF clause, on s55 (5.15) — three limbs clear, one is a judgement

`payoff_clause_and_metric_2026-08-08` §1, decided on 17 scenes (`ceil(17/4)` = **top 5**):

| limb | result |
|---|---|
| sound-off pass | **PASS** — *a thick stack of clipped documents* is a nameable object |
| top quartile on MEDIAN | **PASS** — #3 of 17 (41.15), inside the top 5 |
| non-negative median step in | **PASS** — s54 23.95 → s55 41.15 = **+17.20**, the second-largest step in the chapter |
| **#1 or #2 on p10** | **raw rank #4** (25.73). See below. |

Raw p10 order at the top: s46 33.53 · s49 31.21 · s41 26.10 · **s55 25.73**.

- **s41 is TIED with s55** under `separation_not_rank_2026-08-09` §2: separation **0.37**,
  well inside the 1.0-point band. That makes s55 **#3**.
- The two frames genuinely above it, s46 (+7.80) and s49 (+5.48), are the **two flattest
  frames in the chapter after s48** — `p90 − p50` of **8.60** and **9.41** against s55's
  13.99. Both are the same picture: *one small object on a large plain pale wall*
  (a blank warning sign on painted brick; a letterbox on a peach wall). They rank high on
  p10 because they have no shadows, which is exactly the artefact
  `floor_stopping_rule_and_p10_comparator_2026-08-09` §3 excludes — *a near-flat host frame
  is not a valid comparator on the p10 clause* — and which
  `separation_not_rank_2026-08-09` §2 generalises rather than repeals.

**Verdict: the clause is met**, with s55 reading #1 among valid comparators and #3 on the
raw list. ⚠ **This is the one clause decision in the chapter that turns on a judgement
rather than a clear gap, and it is flagged, not buried.** If fin-review disagrees that
s46/s49 are host frames, s55 is #3 raw and the limb misses by one position. The lever if it
ever has to move is s46 or s49, never s55 — both are supporting frames.

### 5 · The INVARIANT (§1, rewritten form): *a substantive beat must not be left in the chapter's darkest frame*

Discharged on the numbers, **not** with the retired "satisfied by construction" phrase.

**The bottom, in order:** s57b 19.91 · s57 20.88 · s42 21.84 · s48 22.26 · s43 22.35 ·
s50 23.12 · s54 23.95 · s44 24.06 · s51 24.99 · s56 25.21 — then the first separation that
**exceeds** the 1.0-point band, s47 at 27.32 (**+2.11**).

1. **There is no outlier, so §3's outlier limb does not fire.** Ten frames sit inside 5.30
   points and *every adjacent gap is ≤ 0.97* — i.e. every one of them is inside the noise
   band. Calibrated against the two worked examples: en ch4's genuine outlier was **alone by
   6.99 points, 1.88× the next-largest gap**; hi ch4's non-outlier was 2.29 below the band
   *because the bottom was a six-frame cluster*. This is that second shape, with ten.
2. **The bottom frame is not uniquely identifiable.** s57 (20.88) and s42 (21.84) are
   **0.96 apart — inside the band** — so under §2 they are TIED and the clause is satisfied
   by any member. **s42 is 5.2**: a rhetorical question whose whole content the type already
   prints (`10% OR 12% WITHDRAWAL INSTEAD OF 3.0%`), no citation, no mechanism, no derived
   figure — the chapter's least loaded beat after the kicker-only opener. A low-load beat
   genuinely sits at the bottom; that is the clause met on the merits.
3. ⚠ **The residual, stated plainly.** The *other* member of that tie is **5.17**, which is
   substantive — `num 5%`, the RBI MPC citation in the `foot:`, the chapter's closing
   mechanism, and its second-longest scene (9.185 s vs s52's 9.603 s, i.e. tied for
   longest-held on the en-ch3 precedent that a 0.76 s difference is not a difference). The
   0.96-point margin that saves it is **inside the band by 0.04**, and the run's own record
   is that *the rank ORDER moves at the encode* (hi ch4 at ranks 3–8, en ch4 at 4–11). **If
   this chapter produces one P1 look for fin-review, it is this row.**
4. **I tried the fix rather than arguing it.** One round on s57 for a brighter market
   (`sunlit vegetable market stall with baskets of produce@pexels`) returned people in four
   of six cells, **handwritten French price cards** in one and electronic scale displays in
   another — no candidate that was both brighter and clean. Recorded so the next agent does
   not re-spend it.
5. **And the amendment was checked before any of this.** Under
   `outlier_limb_is_subordinate_to_the_invariant_2026-08-10`, a fix is forbidden if it moves
   a *more* substantive beat to the bottom. Here it would not — a lift on s57 relocates the
   floor onto s42 (5.2), which is *less* loaded — so a fix is **permitted**, just not
   currently **available**. That is a different sentence from ch4's and it is the honest one.

⚠ Note the floor **moved during this run**: the killed s51 measured 16.26 and was the
chapter's floor by 3.65 points; its replacement measures 24.99, which is what put 5.17 at
the bottom. The analysis above is written against the shipping file. Do not quote any
earlier number.

### 6 · The OPENING-frame gate (`floor_stopping_rule…` §2)

s41, type covered: **a cracked window**. A concrete, nameable object, so the frame is
eligible to lead. Contrast hi ch2's pale-sky field, which had no object at all. It also
measures near the top (median #4, p10 #3), so nothing is being carried by the gate alone.

### 7 · The promoted-images sheet — what it answered that the per-image reads could not

`IMAGES-ch5.jpg`, 19 cells in play order, read twice (once before and once after the late
s51/s55/s50/s48 changes). **No two cells say the same thing.** `s52b` and `s57b` carry the
HOLD label and are correct by construction.

Four *soft* resemblances the sheet did surface, all declared rather than re-fetched:

1. **s46 and s49 rhyme compositionally** — one small object on a large plain pale wall, three
   scenes apart. Different objects (a blank warning sign / an overfull letterbox) and
   different statements (a warning / a cap). This is the same fact as their p10 ranking in
   §4, seen from the other side.
2. **s48 and s54 are both a regular grid on a wall** — pale stone window grids / blue glass
   blocks with gaps. Six scenes apart, opposite colour temperature, and they read as
   *architecture* vs *texture*.
3. **Four stone-architecture frames in eight scenes** — s44 (brick tank + spout), s45 (ochre
   stepwell), s48 (pale marble facade), s51 (grey stone doorway). Distinct in colour, light
   and subject, and two of them are the declared tank arc.
4. **Paper twice: s53 and s55**, two scenes apart. This is the storyboard's own design for
   5.13–5.15 (their paper → what it excluded → our research) and s54 was deliberately taken
   *off* paper to break the run — see §8.

### 8 · The two most expensive slots, and what the pools actually hold

- **s54, 6 rounds / ~33 cells.** The storyboard asks for *a printed methodology page with
  two lines struck through in ink*. Every query family failed on the same two things —
  legible English and hands: typewriters printing `Grammar` / `Contract` / `DAMN YOUR EYES!`;
  `censored` returning `Coronavirus`, a **`Royal Mail`** mark and `CANCEL CULTURE`;
  `crossed out in red ink` returning six cells of hands filling US forms *including a
  1040-NR*; `sifting flour` returning six cells of people; and one **Quran page**, refused
  outright. It also mattered that s53 and s55 are both paper. What ships states the
  exclusion structurally instead — a wall of blue glass blocks with several broken out,
  leaving hard gaps — and its cool blue is deliberate against `#0c1a2c`, the coldest ground
  in the cut, spent only here.
- **s48, 5 rounds / 30 cells**, and §10 forbids any legible title, figure or agency name on
  it. Killed: the Philippine notice board (§Failed #1), the blank blue plate (UI panel),
  every calendar (a legible month), a Chinese ticket window with a person, an `ATELIER`
  shopfront. What ships is three arched barred windows in a pale stone facade — text-free,
  people-free, institutional.

### 9 · Standing rejections swept, per frame

- **No faces / identifiable people** in any of the 19. Refused for exactly this: two cells at
  the tank (s44), four at the tap round (s42), three in the doorway round (s51), two in the
  market rounds (s57), six hands (s54).
- **No `$`, no `€`, no non-₹ currency, no prices anywhere.** Killed on this ground:
  `200.00 PESOS` (s48), `$12.00 KILO` on a Mexican market sign (s57 round 1),
  `$10,000 / $25,000` on a chart (s55 round 2), `PRICE TEN RUPEES` on a stamp sheet (s47).
- **No readable brand marks.** Killed: the Twitter logo (s47, cropped out), `Royal Mail`
  (s54), `MILAN` (s57), `ALGIDA` (s57), `Apple` (s52 round 2).
- **No demonetised notes, no prop money, no repeated serials** — no currency appears in any
  ch5 frame at all.
- **No screens.** s52 is the slot the never-a-screen rule was written for (5.12 is *about*
  what the internet shows) and it ships with no screen, no monitor and no phone; the
  storyboard's own override is honoured and then over-satisfied.

### 10 · Attribution

`CREDITS.txt` carries **19 rows for 19 files**, and `check assets` asserts it. Two are
hand-placed and were re-keyed in the same move rather than left behind: **s52b** and
**s57b**, each carrying its parent's row plus `(derived crop of sNN.jpg)`. **s47** is
`CC BY-SA 4.0` — attribution is a licence *condition*, not a courtesy — and its row now
also records the modification (`cropped: top 400px removed by fin-assets`), which CC BY-SA
requires. Both derived crops are in `manifest.json`, so the licence assertion reaches them.

## Changed

- **Created** `studio/videos/passive-income-number-hi-ch5/assets-ch5/final/` with
  **19 promoted jpgs** (s41–s57 + s52b + s57b), 19 `.src` sidecars, `manifest.json`,
  `CREDITS.txt`, `IMAGES-ch5.jpg` + `IMAGES-ch5.json`, and the throwaway `_cand/` sheets.
- **`assets-ch5/originals/s47-original.jpg`** — the uncropped Commons file, kept outside
  `final/` so it is neither an orphan nor a shipped image.
- **Three ffmpeg crops.** `s47` = `crop=4096:2672:0:400` from 4096×3072 (brand-mark removal).
  `s52b` = `1600×900 at +140+250` from 1880×1253 and `s57b` = `1600×900 at +260+351` from
  1880×1251 — both `format=yuvj444p` **before** the crop, per ch3's finding that yuvj420p
  snaps the width to even and misses the spec by a pixel, and both a **1.175× push**, i.e.
  ch4 s34b's verified two-framing geometry. s57b additionally crops the parent's only soft
  residual (packaging along the top edge) out of frame.
- **Overrides against the storyboard's `img:` cues, all declared in the `.src`:** s41
  (material, per the owed item), s42 (gauge, not a wide tap — it duplicated s44), s43
  (padlocked gate, not a painted `STOP`), s49 (a full letterbox, not a deposit form),
  s50 (a roof from below, not a bare bulb), s52 (loudspeakers, not a search-results page),
  s54 (a grid with pieces missing, not an ink-struck page), s56 (a broken road slab, not a
  stair tread — the staircase is the ladder's metaphor and ch4's s40 already spent treads),
  s57 (the market, not a chalk price slate).
- **Every image query, cell number, rejection and declaration is written into
  `manifest.json` and mirrored into the `.src` sidecars**, ch4's convention.
- Nothing under `.claude/`, `tools/`, `assets/lottie/` or any other chapter was touched. No
  lottie was needed: ch5's storyboard rows ask for none.

## Owed

1. **⚠ P1 LOOK FOR fin-review, ON THE ENCODE — 5.17 sits at the chapter floor.**
   `s57 20.88 / s57b 19.91` against `s42 21.84`: a **0.96** separation, inside the 1.0 band
   **by 0.04**, and 5.17 is the substantive beat of the pair. It survives §1 only because
   the tie makes s42 an equally valid bottom. Settle it on the encode; if the order moves
   the wrong way, the lever is s57's photograph (one round already spent and recorded in
   §5.4), never the ground.
2. **⚠ The p10 limb of the payoff clause is a judgement, not a gap** (§4). s55 is #3 raw,
   #1 among valid comparators. If fin-review rejects the near-flat-host reading of s46/s49,
   the limb misses by one position.
3. **s42 is the volatile row at the encode.** `p90 − p50 = 32.96`, two and a half times the
   chapter median spread (a white gauge dial against a dark red ground), so its median is
   the one most sensitive to any method difference — the same shape as ch4's s40.
4. **Four thin YHIGH margins to re-check if anything downstream re-encodes the stills:**
   s48 112, s43 117, s57b 117, s57 121, against a floor of 110.
5. **Density is not honoured on s50** (§Changed): the chapter's densest type frame
   (`num ₹5,550 A MONTH` + span + `foot:` + stmt) sits on red roof trusses rather than on a
   calm ground. The trade was made knowingly against a candidate that was calm and empty.
   If it reads busy on the draft, the fix is a quieter roof, not a darker grade.
6. **`owed.storyboard_hi_ladder_stale_in_three_places` is still open**, and this is now the
   **fourth** agent to work around §9c/§10/§12 rather than fix them. ch5 additionally proves
   §10's *tank* row stale in the same way its ladder row is: it names *"the plain steel body
   under workshop light"* as the recognisable constant, and **no hi frame has ever shipped
   it** — ch2 s11 and ch4 s37 are stepped stone tanks. **s58 and s62 are next and they are
   ladder rungs**; brief them against `assets-ch3/final/s22.jpg` (terracotta gullaks) and
   `assets-ch4/final/s31.jpg` (the iron-bound chest), never against §12's row.
7. **Declared for the editor, in one place so it is not discovered:** s48 (Ottoman
   architecture), s49 (a European decorative letterbox), s53 (Polish body text), s55
   (nothing in the frame says India — on the payoff of the India-vs-America beat), s57 (a
   market that is not provably Indian). Every one is currency-neutral, signage-free and
   brand-free; the Indian-ness of the chapter is carried by s45 (an Indian stepwell), s47
   (an India Post office) and the VO.
