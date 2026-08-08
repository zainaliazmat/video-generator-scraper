---
summary: en ch2 attempt 3 chapter draft, re-rendered and re-measured from scratch. 3166 frames / true CFR 30 / 0 black. Both one-line fixes CONFIRMED on the encode (s20 kicker ratio 2.67 last-of-15 -> 6.56 second-of-15; s14 grey-vs-amber +22.1 -> +0.7 luma). The definitive composed legibility table says s21 is #1 on p10, #3 on median, #3 on mean, #7 on p90 — so "never the least" is satisfied on every measure and "the most legible" is satisfied on none, missing by 2.7 points on the fairest one.
updated: 2026-08-08
source: measured from studio/videos/passive-income-number-en-ch2/renders/DRAFT-ch2.mp4 (rendered 16:44:02 this pass, inputs index.html/build.mjs 16:26) · tools/format.json qa + layout · run.json rulings_binding_on_both_cuts · logs/fin-build-en-ch2-3.md · logs/fin-render-hi-ch2-2.md
stage: fin-render, cut en, chapter 2, attempt 3, CHAPTER DRAFT MODE
---

# fin-render · passive-income-number · en · ch2 · attempt 3 (chapter draft)

**MODE: CHAPTER DRAFT (§3b step 4).** Gate two was not run as a gate and no
full-quality encode was run. The draft was re-rendered from the 16:26 build,
the sheet rebuilt, and everything below measured off that new encode.

    npx hyperframes render . -c index.html -o renders/DRAFT-ch2.mp4 -q draft -f 30
    python3 tools/chapter_sheet.py studio/videos/passive-income-number-en-ch2 \
            renders/DRAFT-ch2.mp4 -o .../renders/SHEET-ch2.jpg

## 0 · Freshness — both artifacts overwritten, confirmed by mtime

| File | mtime | bytes |
|---|---|---|
| `index.html` / `build.mjs` (inputs) | 16:26:58 / 16:26:46 | — |
| **`renders/DRAFT-ch2.mp4`** | **16:44:02** | 25,623,349 |
| **`renders/SHEET-ch2.jpg`** | **16:44:25** | 428,091 |
| `renders/SHEET-ch2.json` | 16:44:25 | 876 (16 entries: 15 scenes + s10 framing 2) |

The 13:41 draft of the pre-fix build is gone. Render took 3m 07.9s, 1 worker,
`beginframe` capture, artifact validated.

## 1 · Structure — PASS on all four

| Quantity | Expected | Measured |
|---|---|---|
| frames | ceil(105.518 x 30) = **3166** | **3166** |
| video duration | 3166/30 | **105.533333s** (container 105.536000) |
| resolution / codec | — | 1920x1080 h264 |
| **CFR** | true 30 | **true CFR 30** |
| black segments | 0 | **0** |

**CFR proven from PACKET TIMESTAMPS, not the fps tag.** 3166 packets → 3165
inter-packet deltas taking exactly **two** values: `0.033333` (x2110) and
`0.033334` (x1055). 2110 + 1055 = 3165, no third value, first pts 0.0, last 105.5.
Frame counts sum with the sibling chapters.
`blackdetect=d=0.05:pic_th=0.98:pix_th=0.10` → no output, **0 segments**.

## 2 · THE MEASUREMENT THAT DECIDES THE GATE — definitive composed table

Method: the encode decoded once at **full 1920x1080** on a 10 fps grid, each scene
measured over its **settled span** (`start + 0.45` → next scene's start, so no
blended frame is inside any figure), percentiles interpolated from pooled 256-bin
histograms. This is the same method as `fin-render-hi-ch2-2.md`, so the two cuts
are directly comparable. (It is NOT the method of `fin-render-en-ch2-2.md`, which
pooled a 192x108 downscale — averaging 100 pixels into one suppresses exactly the
highlight decile that is under argument here. p90 figures below run up to 8 points
above that log's; the full-resolution ones are the real ones.)

| scene | settled span | **p10** | **median** | **p90** | **mean** | p90−p50 |
|---|---|---|---|---|---|---|
| s9  (2.1) | 0.45–5.16 | 20.7 | **45.4** | 57.0 | 44.3 | 11.6 |
| s10 (2.2) | 5.61–15.76 | 17.5 | 27.4 | 41.8 | 32.4 | 14.4 |
| s11 (2.3) | 16.21–23.92 | 18.6 | 37.0 | 51.7 | 38.3 | 14.7 |
| s12 (2.4) | 24.37–27.78 | 21.0 | 27.2 | 47.6 | 33.5 | 20.4 |
| s13 (2.5) | 28.23–34.67 | 16.4 | **45.2** | 56.1 | **44.9** | 10.9 |
| s14 (2.6) | 35.12–41.74 | 23.8 | 31.1 | 41.5 | 37.5 | 10.4 |
| s15 (2.7) | 42.19–48.81 | 16.8 | 29.9 | **61.4** | 37.8 | **31.5** |
| s16 (2.8) | 49.26–55.17 | 15.8 | 33.6 | 57.3 | 34.8 | 23.7 |
| s17 (2.9) | 55.62–62.66 | 20.6 | 29.8 | 46.6 | 34.5 | 16.8 |
| s18 (2.10) | 63.11–70.28 | 19.4 | 34.7 | 50.2 | 36.5 | 15.5 |
| s19 (2.11) | 70.73–76.82 | 16.8 | 38.2 | 58.3 | 39.5 | 20.1 |
| s20 (2.12) | 77.27–84.31 | 14.7 | 22.6 | 43.8 | 27.3 | 21.2 |
| **s21 (2.13) PAYOFF** | 84.76–90.39 | **27.1** | **42.5** | **51.5** | **41.8** | **9.0** |
| s22 (2.14) | 90.84–97.77 | 15.4 | 33.0 | 45.2 | 33.7 | 12.2 |
| s23 (2.15) | 98.22–105.52 | 16.1 | 29.8 | 44.4 | 31.6 | 14.6 |

Duration-weighted whole chapter: **p90 49.8 · median 33.4 · mean 36.2 · p10 18.5.**

### The four rankings, and s21's place on each

    p90     s15 61.4 · s19 58.3 · s16 57.3 · s9 57.0 · s13 56.1 · s11 51.7 · [s21 51.5]
            · s18 50.2 · s12 47.6 · s17 46.6 · s22 45.2 · s23 44.4 · s20 43.8 · s10 41.8 · s14 41.5
    median  s9 45.4 · s13 45.2 · [s21 42.5] · s19 38.2 · s11 37.0 · s18 34.7 · s16 33.6
            · s22 33.0 · s14 31.1 · s15 29.9 · s23 29.8 · s17 29.8 · s10 27.4 · s12 27.2 · s20 22.6
    mean    s13 44.9 · s9 44.3 · [s21 41.8] · s19 39.5 · s11 38.3 · s15 37.8 · s14 37.5
            · s18 36.5 · s16 34.8 · s17 34.5 · s22 33.7 · s12 33.5 · s10 32.4 · s23 31.6 · s20 27.3
    p10     [s21 27.1] · s14 23.8 · s12 21.0 · s9 20.7 · s17 20.6 · s18 19.4 · s11 18.6
            · s10 17.5 · s19 16.8 · s15 16.8 · s13 16.4 · s23 16.1 · s16 15.8 · s22 15.4 · s20 14.7

| statistic | s21 | rank of 15 | above it |
|---|---|---|---|
| **p10** | 27.1 | **#1**, 3.3 clear | — |
| **median** | 42.5 | **#3** | s9 (+2.9) · s13 (+2.7) |
| **mean** | 41.8 | **#3** | s13 (+3.1) · s9 (+2.5) |
| **p90** | 51.5 | **#7** | s15 · s19 · s16 · s9 · s13 · s11 (+9.9 to +0.2) |

**Stated plainly. Against `ground_and_payoff_legibility_2026-08-08`:**

- *"never the least"* — **satisfied with room, on every measure.** Worst rank is
  #7 of 15; on the floor it is first by 3.3 points. Nothing here is close to last.
- *"the most legible in its chapter"* — **not satisfied on any measure.** Nearest
  miss is median/mean, where it is **#3, 2.7 points short of #1** (~6%).
- The `≥ 55` p90 target from the same brief: **measured 51.5. It is a miss of 3.5.**
  fin-build's composed snapshot said 52.9 and I am not rounding either of them up.

**Two photographs stand between s21 and #1, not four** (hi ch2 had four): **s9**,
the blank notebook cover that opens the chapter (median 45.4), and **s13**, the
open journal (median 45.2). Either both come down below 42.5, or s21's photograph
goes up past 45.4. Per the ruling, the lever is the photograph.

### The predictor was RIGHT this time, and the reason is worth keeping

| s21 statistic | fin-assets (source) | fin-build (composed snapshot) | **encode** |
|---|---|---|---|
| p10 | — | 26.8 | **27.1** |
| median | — | 42.9 | **42.5** |
| mean | #1 of 15 | 43.0 (#3) | **41.8 (#3)** |
| p90 | 53–55 | 52.9 (#7) | **51.5 (#7)** |

fin-build's composed numbers predicted the encode to within **1.4 points on all
four**, and got the RANK exactly right on three. The three ~8-point misses this
run (en s20 50/43, hi s16 54.2/47.1, hi s14 44.7/53.3) were all **source-based**
predictions pushed through an assumed grade. The rule that falls out: a composed
snapshot is worth ~1 point of error, a source measurement ~8, and the two are not
interchangeable evidence. That is now measured three times against once.

### THE LIVE METRIC QUESTION — median, with the spread beside it, and a caveat

**p90 is the wrong measure for this chapter, and this chapter proves it harder
than hi ch2 did.** On hi, the p90-inflated frame (s10, black desk + white lamp)
ranked 8th, so it distorted the middle of the table. Here the p90-inflated frame
is **at the top of it**:

1. **s15 is #1 of fifteen on p90 (61.4) and #10 on median (29.9).** It is a nearly
   black library desk carrying one blank pale page in the left third. Its
   **p90−p50 spread is 31.5, the widest in the chapter by 7.8 points** over the
   next. p90 ranks the chapter's most lopsided frame first.
2. **The joints catch the same error twice, in opposite directions.**
   - `s14→s15`: **Δp90 +18.2** but **Δp50 +2.3**. p90 reports the picture getting
     dramatically brighter; nothing enters the frame but one white page.
   - `s15→s16`: **Δp90 −16.5** but **Δp50 +6.1**. p90 reports the picture getting
     darker at the exact joint where a viewer sees it get *clearer* — s16 is an
     evenly lit desk with the amber grid.
   Any measure that is wrong about the direction of a joint cannot rank the frames.
3. **p90 structurally penalises what the ruling is trying to reward.** s21 has the
   **narrowest spread in the chapter (9.0)** — it is the most uniformly lit frame
   here. A rule written on p90 asks the payoff frame to grow a hot spot.

**Caveat, against my own recommendation, because it is real:** median alone rewards
a featureless field. The chapter's #1 on median is **s9 (45.4), a blank notebook
cover** — tonally even, and it says almost nothing sound-off. So the honest
formulation for the CEO is:

> **Judge legibility on the MEDIAN (mean corroborates: same top three, same
> ordering of s21), report `p90 − p50` beside it as the spikiness check, and keep
> the sound-off read as the qualifying gate — a frame with no subject cannot be
> "the most legible" no matter how even it is.**

On that formulation s21 is **#3 behind s9 and s13**; and of the three, s21 is the
only one that is simultaneously top-3 on the floor (p10 #1), top-3 on the middle
(median #3) and the narrowest in spread. If the CEO wants a single composite the
numbers already support, "median with spread under 15" ranks **s21 first**
(s9 spread 11.6 and s13 10.9 also qualify — so it does not, quite; s21 leads only
on p10 and on evenness). I am not going to invent a statistic that makes it #1.

## 3 · THE TWO FIXES — both confirmed from the encode

### 3a · s20 `PER MONTH` vs the price card's `$5.` ink — FIXED, and by more than reported

`background-position: center bottom` on `.bg`. Measured at three points across the
ken (78.0 / 80.5 / 83.0), in the kicker's own column span (x 845–1075):

| t | max luma anywhere in y200–400 (the old card row) | kicker glyph max (y438–458) | kicker local backdrop |
|---|---|---|---|
| 78.0 | **63** | 185 | **23.2** |
| 80.5 | **64** | 185 | **23.1** |
| 83.0 | **65** | 184 | **23.0** |

There is **no card ink above luma 65 anywhere in the kicker's columns at any point
in the ken** — the price-card row has moved wholly clear, and the kicker now sits
on the dark shelf lip. The three price cards remain in frame (they sit at y≈230–390
in the frame's left and right thirds), so the scene still reads as a store, and the
five US price tags ($1.99, $3.99, $5.99, $1.99, and the hot-pepper card) are all
correct currency for `-en`.

fin-build reported backdrop 40.9 → 18.3 and ratio 3.78 → 8.52 on its own box. My
box is the one used in attempt 2 (glyph mask vs non-glyph, y430–466, x845–1075):
**backdrop 60.4 → 24.2, ratio 2.67 → 6.56.** Both agree the backdrop falls ~2.5x.

**The kicker's rank against the others — the question asked.** All fifteen kickers
measured identically (glyph mean over the >140 mask, backdrop mean over the same
box padded ±8px):

    s16 6.68 · [s20 6.56] · s23 4.78 · s10 4.37 · s14 4.23 · s17 4.19 · s18 4.10
    · s11 3.71 · s22 3.64 · s12 3.48 · s21 3.28 · s13 2.96 · s19 2.91 · s15 2.79 · s9 2.77

**s20 goes from LAST (2.67 of eight) to SECOND of fifteen (6.56), against a chapter
median of 3.71.** It is now 1.77x the median. The lowest kickers in the chapter are
now s9 (2.77) and s15 (2.79) — both grey-on-pale-paper, both legible, neither a
collision. Nothing was made worse: every other kicker is unchanged within noise.

### 3b · s14's bar — FIXED, and the two halves are now equal to within 1 luma

`fill-opacity: 0.55` (which `fade()` cannot clobber) in place of the dead
`opacity=".22"`. Measured on the encode at t=41.0 over the bar's interior
(y 490–589), ground sampled 30px above and below:

| | RGB | luma | vs ground |
|---|---|---|---|
| amber FILLED half (x1096–1466) | (79.1, 57.3, 24.6) | **61.0** | +24.4 |
| grey UNFILLED half (x1516–1875) | (58.8, 59.9, 64.8) | **61.7** | +25.1 |
| ground above / below | — | 36.6 / 33.6 | — |

**The +22.1 inversion is gone: the gap is now +0.7 in luma**, i.e. 1.1%, below any
perceptual threshold and inside the encode's own quantisation. fin-build predicted
60.0 / 61.0; the encode says 61.0 / 61.7 — agreement to 1 luma.

Asked precisely: *does the filled half now read at least as loud as the empty one?*
**On luma, it is 0.7 short of equal, not above it** — I am reporting that rather
than rounding it to "at least". **On chroma it is decisively louder:** amber
|R−B| = **54.5** against the grey's **6.0**, so the filled half is the only
chromatic object in the bar and is what the eye lands on. Net: the two halves now
read as equal quantities with the target-coloured half carrying the salience,
which is what a "50% / 50%" frame needs. Still a solid filled rect, never an outline.

**The split still measures 0.5000–0.5006 — unchanged.** Track x span **1086–1885**
(len **800**, viewBox 1:1). Tick `#s14-mid` bright spike at x **1481–1490**, centre
**1486.0**; track continuous midpoint **1486.0**. That is **0.5000** on a
continuous-coordinate convention and **0.5006** on attempt 2's pixel-centre
convention — the same measurement to half a pixel, and `SPLIT = 0.5` in source.
Bar geometry y 480–599 (h 120), unchanged.

## 4 · s15 — survives its 1.16x ken and says its own scene SOUND-OFF · BLOCKER CLOSED

`ken: "o"`, so **42.19 is the tightest instant** (1.16x) and it widens from there.
Read at 42.19, 44.34 (last cue), 46.5 (the timestamp the CEO called an
unidentifiable pale curve) and 48.5:

- **46.5 and 48.5: unambiguous.** An open bound volume fills the left half — the
  blank recto page curving away from the gutter, the text block's cut edge visible
  at the bottom left — and a stack of two cracked-spine hardbacks sits at frame
  right with the page block's frayed edges and the headband readable. Cover the
  type and the frame says *old bound papers on a desk / a library*. That is exactly
  what "PAPER TWO — Three Trinity University professors" needs.
- **44.34: same read, marginally tighter.**
- **42.19, the tightest instant: it holds, but this is its weakest second.** The
  crop pushes the right-hand stack toward the edge and the pale page dominates; the
  frame reads as "a big pale sheet and something stacked beside it" before it reads
  as books. It becomes unambiguous by roughly 43.5s. The scene is 7.5s long and the
  statement does not rise until 42.837, so nothing is being asserted over the weak
  second. **Not a blocker; recorded for fin-editor as the one place the ken costs
  something.**
- `Breton 75` at bottom-left is faint (≈8% of frame width, luma under the kicker's
  backdrop) — agreeing with fin-assets and fin-build, not legible text under §10.

The other side of s15 is §2: this photograph is the chapter's **p90 #1 and median
#10**, the one that makes p90 unusable as the ranking statistic.

## 5 · Every joint — scdet peak, Δp90, Δmedian, and what it SHOWS

scdet peak taken in `start−0.10 .. start+0.55`. Δ measured outgoing scene's last
0.8s BEFORE the overlap against incoming's first 0.8s AFTER it, so no figure
contains a blended frame.

| joint | at (s) | scdet | Δp90 | Δp50 | what it SHOWS |
|---|---|---|---|---|---|
| s9→s10 | 5.162 | 0.179 | **−15.4** | −16.6 | blank notebook cover, evenly lit → a dark row of brass tap valves. Empty ground into hardware; the chapter's second-largest light step. |
| s10→s11 | 15.758 | 0.167 | +11.3 | +10.3 | second framing of the same taps → the warm out-of-focus verdict frame. Same subject, so the step is grade, not cut. |
| s11→s12 | 23.924 | 0.149 | −4.6 | −9.7 | warm blur → dark desk with two pale documents. Smallest visual event of the eight amber joints. |
| s12→s13 | 27.781 | **0.243** | +8.7 | **+19.5** | two papers → the open journal. Median jumps 19.5, p90 only 8.7 — a whole-frame brightening, the honest kind. |
| s13→s14 | 34.667 | 0.198 | **−17.7** | −14.1 | open journal → the dark type-case with the 50/50 bar. **The chapter's largest light step**, and it is where the drawn layer lives. |
| s14→s15 | 41.737 | 0.211 | **+18.2** | **+2.3** | type-case → library desk. **p90 says +18, median says +2.** One white page enters; the frame does not brighten. The clearest single proof against p90. |
| s15→s16 | 48.806 | 0.191 | **−16.5** | **+6.1** | library desk → the amber 95% grid on an even desk. **p90 says darker, median says clearer** — the two measures disagree in SIGN. |
| s16→s17 | 55.170 | 0.180 | −14.2 | −0.8 | grid → the stamp box with the drawn date axis. p90 falls 14 while the median is flat: the grid's amber cells leave, the ground does not move. |
| s17→s18 | 62.658 | 0.145 | +1.9 | +8.5 | stamp box → the green method frame. The chapter's amber→green turn, and tonally the quietest joint in it. |
| s18→s19 | 70.276 | 0.230 | +8.4 | +6.1 | green method → the warm overhead food table. Green→amber for one scene, then back. |
| s19→s20 | 76.822 | 0.180 | **−13.7** | −13.6 | food table from above → produce shelf at eye level. Still the run's big step down (was −17 in attempt 2 on the coarser method), and the compositional change (flat-lay → shelf) is larger than the light change. |
| **s20→s21** | 84.310 | **0.248** | **+7.8** | **+20.4** | **produce shelf → the bread loaf, the payoff.** In attempt 2 this was **+0 / +3** — a plateau into the hero. With the new photograph the hero **rises out of it: +7.8 on p90 and +20.4 on median, the largest median rise in the chapter.** The chapter now arrives at its first corpus on a step up, not a flat. |
| s21→s22 | 90.387 | 0.159 | −6.3 | −9.5 | bread → green-tinted receipts. Payoff into evidence, gentle. |
| s22→s23 | 97.769 | 0.143 | −1.6 | −4.1 | receipts → the dark green crate. The chapter's flattest joint; it closes on tone, not on a cut. |

**scdet cannot rank any of this and the encode says so numerically.** Joint peaks
span **0.143–0.248**. The file's global scdet maximum is **0.473 at t=35.8** — mid-scene
in s14, the bar filling. Of the fifteen highest scdet frames in the chapter, **thirteen
are in-scene rises** (35.8 s14 bar 0.473 · 100.0 s23 statement 0.359 · 73.53 s19 0.328 ·
83.33 s20 0.308 · 63.8 s18 0.293 …) and only two are joints (84.6 = 0.248, 27.9 = 0.243).
Every text rise outscores every dissolve, exactly as in attempt 2.

## 6 · Cross-dissolves — sampled INSIDE the overlap at BOTH `qa.dissolve_sample_offsets`

`start+0.225` and `start+0.380`, per `format.json`. Residual alpha of the OUTGOING
scene's type recovered by linear unmix on a mask of that type
(`bright at start−0.10` AND `dark at start+0.60`):
`α = (observed − incoming_only) / (outgoing_clean − incoming_only)`.

| joint | mask px | clean out | in only | @+0.225 | @+0.380 | **α@.225** | **α@.380** |
|---|---|---|---|---|---|---|---|
| s9→s10 | 44,726 | 164.3 | 34.0 | 93.7 | 36.3 | 45.8% | **1.7%** |
| s12→s13 | 39,524 | 234.6 | 57.4 | 126.7 | 63.6 | 39.1% | **3.5%** |
| s14→s15 | 59,274 | 229.0 | 62.4 | 143.7 | 66.6 | 48.8% | **2.5%** |
| s15→s16 | 58,253 | 163.8 | 43.8 | 105.4 | 47.2 | 51.3% | **2.9%** |
| s19→s20 | 29,040 | 163.3 | 27.2 | 85.7 | 29.0 | 42.9% | **1.3%** |
| s20→s21 | 18,082 | 212.8 | 51.3 | 113.3 | 56.3 | 38.4% | **3.1%** |
| s21→s22 | 10,684 | 152.3 | 40.1 | 89.2 | 41.3 | 43.8% | **1.0%** |
| s22→s23 | 8,351 | 148.3 | 38.9 | 93.0 | 41.7 | 49.4% | **2.5%** |

**No stacking-context defect.** The `japanese-money-methods-hi` signature is the
outgoing text at ~100% for the full 0.45s. Here it is 38–51% at the midpoint —
which is what a cross-dissolve is — and **1.0–3.5% by +0.380**, i.e. gone before
the overlap ends, at all eight sampled joints (attempt 2 measured all fourteen at
1.2–3.5% and the type stack is byte-unchanged since).

⚠ Same eye-vs-measurement note as attempt 2, and it is now on the payoff joint: at
`s20→s21 +0.380` the outgoing `$847` IS faintly visible over s21's rising
"RUNG ONE". I read the frame; it looks like a double-paint. It measures **3.1%** —
the correct tail of a dissolve, visible only because s21's first frames are the
darkest ground in the chapter. The measurement is right and the eye is wrong.

## 7 · Comma clearance — on `.huge`, and there is still no `.mega` to protect

    grep -c 'class="mega' index.html  →  0
    grep -c 'class="huge' index.html  →  15   (3 plain · 4 .fundc · 8 .targetc)

`.arch-b .mega { padding-bottom: .11em }` has **zero elements to apply to in this
chapter.** Every focal here is `.huge`.

Ink-to-ink clearance measured from the encode (threshold 110, ≥6px per row, at each
scene's last cue) for every `.huge` that has a following sibling:

| scene | focal | focal ink band | next ink top | **clearance** |
|---|---|---|---|---|
| s10 | `How much can you draw…` | 466–615 | `.sub` 639 | **24px** |
| s13 | `William Bengen, Journal of…` (comma L1 + `g` L2) | 465–**640** | `.foot` 665 | **25px** |
| s14 | `50% stocks / 50% bonds` | 428–623 | `.foot` 670 | **47px** |
| s15 | `Three Trinity University professors.` (`y`) | 447–622 | `.foot` 647 | **25px** |
| s16 | `95%` | 240–321 | `.foot` 363 | **42px** |
| **s19** | **`$10,169`** | 481–**581** | `.foot` 607 | **26px** |
| s20 | `$847` (no comma) | 499–590 | `.foot` 625 | **35px** |
| **s21** | **`$254,225`** | 535–**634** | `.foot` 662 | **28px** |

`.huge` is last child in s9, s11, s12, s17, s18, s22, s23 — no sibling, no clearance
to measure. **Nothing collides anywhere. Tightest is s10 at 24px**, then s13/s15 at
25. (s13 reads 25px here against attempt 2's 45px purely because this pass threshold
at 110 catches the dim descender ink down to y640 that a higher threshold missed —
same geometry, stricter measurement, still 25px clear.) The two comma focals, s19
and s21, sit at 26px and 28px, both above the tightest number in the chapter.

## 8 · `cues.py` — exit 0, read-only, unchanged

    python3 tools/audio/cues.py studio/videos/passive-income-number-en-ch2   →  exit 0

**25 cues**, 5 `_dry` scenes (s12, s14, s16, s19, s20), `music: bed-tension`.
Recomputed independently from the emitted `at` list: **minimum gap 1.100s**,
occurring 7 times (each `+1.10` statement rise against its own scene joint), against
`cue_min_gap_seconds` = 0.8. The derived output is byte-identical to attempt 2's —
neither photograph swap nor either one-line fix touches a cue.

## 9 · Draft audio (informational; master QA still owed)

| Quantity | Measured | Gate |
|---|---|---|
| max sample level | **−3.5 dBFS** | — |
| **true peak** (`loudnorm`) | **−3.2 dBTP** | below −1 dBTP ✓ |
| integrated | −21.2 LUFS | — |
| LRA | 3.2 LU | — |

## 10 · What was NOT measured at this stage

Per-line VO drift against the `data-start` table, faster-whisper coverage, and
runtime vs `timing.json` belong to the master QA pass on
`renders/FINAL-1080p-en.mp4`, not to a chapter draft. When that pass runs, subtract
`qa.vad_onset_latency_seconds` **0.101** from every raw Silero onset before
comparing against the 0.1s target (it quantises to 0.032s and reports late; raw
values read as a false FAIL), and use Whisper for coverage only.

**Chapter total for the joint arithmetic: 3166 frames @ 30fps = 105.5333s.** s23
carries its bare `scene_duration`, so `cut_assemble.py` adds +0.45 back at fold-in.
