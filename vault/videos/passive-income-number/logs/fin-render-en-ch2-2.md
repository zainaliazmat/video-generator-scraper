---
summary: en ch2 attempt 2, MEASURE-ONLY re-pass over the existing draft (no re-render). Confirms 3166 frames/CFR 30/zero black, re-measures the whole tone curve after four changes, and settles the s20 photograph trade — s19>s20 narrowed to -17 and s20>s21 did NOT steepen (+0). Comma clearance measured on all 15 `.huge`; zero `.mega` in the chapter.
updated: 2026-08-08
source: measured from studio/videos/passive-income-number-en-ch2/renders/DRAFT-ch2.mp4 (mtime 13:41) — inputs index.html/build.mjs 13:15, assets-ch2/final/s20.jpg 13:27
---

# fin-render · passive-income-number · en · ch2 · attempt 2

**MODE: CHAPTER DRAFT, MEASURE ONLY.** Gate two was not run, no encode was run, and
**nothing was re-rendered**. Attempt 1's dispatch rendered the draft and died before
logging; this pass measures that draft.

## 0 · Freshness re-verified independently

| File | mtime | vs inputs |
|---|---|---|
| `renders/DRAFT-ch2.mp4` (25,364,946 B) | **13:41** | newer than all |
| `renders/SHEET-ch2.jpg` (419,280 B) | **13:42** | newer than all |
| `renders/SHEET-ch2.json` (876 B, 16 entries) | 13:42 | — |
| `index.html` / `build.mjs` | 13:15 | older |
| `assets-ch2/final/s20.jpg` (441,236 B) | 13:27 | older |
| every other `assets-ch2/final/*.jpg` | 06:38–07:06 | older |

The draft postdates every input. Re-rendering would have measured the same file.
`SHEET-ch2.json` carries 16 entries (15 scenes + s10's second framing).

## 1 · Structure, frame count, CFR — PASS

| Quantity | Expected | Measured |
|---|---|---|
| scenes | 15, s9–s23 | **15, s9–s23** (`data-start` table read from `index.html`) |
| root duration | 105.518 | **105.518** |
| frames | ceil(105.518 x 30) = **3166** | **3166** |
| video duration | 3166/30 = 105.5333 | **105.533333s** (container 105.536000, aac 4947 frames) |
| resolution / codec | — | 1920x1080 h264, 1.92 Mb/s |

**True CFR 30 confirmed from PACKET TIMESTAMPS, not the fps tag.** 3166 packets → 3165
inter-packet deltas, taking exactly **two** values: `0.033333` (2110x) and `0.033334`
(1055x). 2110 + 1055 = 3165, no third value, first pts 0.0, last 105.5. Frames will sum
with the sibling chapters.

## 2 · Black scan — PASS, zero

- `blackdetect=d=0.05:pic_th=0.98:pix_th=0.10` → **0 segments** (no filter output).
- `blackframe=amount=95:threshold=32` → **0 frames**.

## 3 · Cue gaps — PASS, `cues.py` exit 0

`python3 tools/audio/cues.py studio/videos/passive-income-number-en-ch2` → **exit 0**,
25 cues, 5 `_dry` scenes (s12, s14, s16, s19, s20), `music: bed-tension`.

Independently recomputed from the emitted `at` list: **minimum gap 1.100s**, occurring
7 times (every `+1.10` statement rise against its own scene joint). Floor
`format.json cue_min_gap_seconds` = **0.8**. The s18 reveal is at 63.758 against the
s18 joint at 62.658 — **1.100s**, so the 0.600s breach is gone and the check that would
have caught it now exists and is green.

## 4 · The four changes since the last measured draft

### 4a · s14 — the drawn bar split at 0.500 · PASS

Source constant: `build.mjs:334  const SPLIT = 0.5, TRACK_X = 40, TRACK_W = 800`.

Measured off the encode at three rows through the bar (screen coords, 1920x1080):

| Quantity | Measured |
|---|---|
| track x span | **1086–1885** (len **800**) — viewBox 1:1, offset +1046 |
| track midpoint | **1485.5** |
| split tick (`#s14-mid`, viewBox x435 w10) | screen **1481–1491**, centre **1486.0** |
| tick vs track midpoint | **+0.5px** → split **0.5006** |
| amber fill (`#s14-fill`) right edge | reaches **1479–1481** with *no* grey gap before the tick |

The tick is opaque and 10px wide, so it occludes the fill's exact right edge; what is
provable from the encode is that the fill runs continuously up to the tick's left edge
(≥0.494) and that the **marker** is at 0.500 to half a pixel. Combined with `SPLIT = 0.5`
in source, the split renders at 0.500.

**Drawn layer vs the ~.2 fill-opacity floor — clears it.** s14 is `art-forward`, so
`.has-photo.art-forward .art { opacity: .52 }` applies, not the `.30` floor and well clear
of ~.2. Measured luma steps over the graded still (still = 35.6):

| element | luma | delta over still |
|---|---|---|
| grey track (`.fl`, `opacity=".22"`) | **81.0** | **+45.4** |
| amber fill (`.flt`) | **59.3** | **+23.7** |

⚠ **Observation for fin-editor, not a fail.** The *unfilled* grey half reads **21.7 luma
brighter** than the amber half. The focal is "50% stocks / 50% bonds", so both halves are
real quantities rather than fill-vs-remainder and the inversion is defensible — but the
target-coloured half is the dimmer one, and at a glance the right (bonds) side dominates
the bar.

### 4b · s17 — OCTOBER 1994 / FEBRUARY 1998 · PRESENT AND LEGIBLE, but the dimmest type in the chapter

Both dates render and both read. Measured on the same frame (t 61.5):

| element | peak L | local bg L | Weber | Michelson | peak RGB |
|---|---|---|---|---|---|
| headline `.huge targetc` | **171.3** | 22.7 | 6.55 | 0.77 | (255,165,64) |
| kicker | 170.6 | 23.1 | 6.38 | 0.76 | (169,170,189) |
| **OCTOBER 1994** (art) | **57.2** | 26.2 | **1.18** | 0.37 | (77,56,39) |
| **FEBRUARY 1998** (art) | **56.1** | 25.0 | **1.24** | 0.38 | (76,54,38) |
| ring stroke | 58.8 | 28.3 | 1.08 | 0.35 | (81,57,35) |
| axis rule | 66.4 | 23.3 | 1.85 | 0.48 | (68,66,67) |

The dates render at **33% of the luminance of the same `--target` colour used by the
headline in the same frame** (57 vs 171). Cause is structural, not a bug: the SVG lives
inside `.plate` (z-index 0), `.scrim` (z-index 1) paints over it, and `.has-photo
.art-forward .art` caps it at .52. `#s17-band` at `z-index:0` is what makes them readable
at all — it darkens behind the art without touching the frame, exactly as
`chapter-design.css` prescribes.

**Ruling: the fix landed** — the previous version showed no date anywhere; both dates are
now on screen and both survive the encode at 46px. They are comfortable at 1080p and will
be marginal on a 360p phone. If fin-editor wants them stronger the lever is the band's
opacity or an `art-lift`, never the frame grade.

### 4c · s20 — the new photograph, and BOTH joints

Source: `grocery store produce display with dollar price signs@pexels`, a US produce
shelf with handwritten $/LB tags. Correct currency for `-en`; no ₹ anywhere.

**Source vs encoded p90 for the three scenes in play:**

| scene | source p90 | encoded body p90 | ratio |
|---|---|---|---|
| s19 | 228 | 59 | .259 |
| **s20 (new)** | **195** (was 138) | **43** (was 35) | .221 |
| s21 | 144 | 44 | .306 |

fin-assets predicted encoded ~50. **Actual 43.** Source p90 rose +41% (138→195); encoded
p90 rose only **+23%** (35→43), because `.bg`'s grade plus the scrim compress harder the
brighter the source is — the ratio column above falls monotonically as source p90 rises.
Both of fin-assets' joint predictions inherit that miss.

**The two joints, measured exactly** (scdet peak in `start-0.10 .. start+0.55`; luminance
step = outgoing scene's last 0.8s before the overlap vs incoming's first 0.8s after it, so
neither figure contains a blended frame):

| joint | at (s) | scdet peak | @t | Δp90 | Δmed | previous | predicted |
|---|---|---|---|---|---|---|---|
| **s19→s20** | 76.822 | **0.182** | 76.933 | **−17** | **−15** | −23 / −14 (0.173) | ≈ −8 |
| **s20→s21** | 84.310 | **0.225** | 84.600 | **+0** | **+3** | +7 / +3 (0.200) | ≈ −15 |

Body-to-body corroborates: s19 59 → s20 43 = −16; s20 43 → s21 44 = **+1**.

**What each joint SHOWS.**

- **s19→s20** is still the chapter's largest light step, but it is no longer the
  lights-going-out step it was. OUT: an overhead kitchen table of vegetables, bread and
  eggs, warm and amber-graded, p90 59 — still the brightest scene in the chapter. IN: a
  produce shelf shot straight on, dark aisle above, lit crates below, p90 43. The two
  frames are still both "food", back to back, and that adjacency is unchanged by the swap.
  What changed is that the incoming frame no longer reads as a different room with the
  lights off: the step is −17 instead of −24, and the new frame carries its own internal
  highlights (the white price cards at L164) so the eye has somewhere to land immediately.
  It also changes the joint's *shape*: flat-lay-from-above → eye-level shelf, which is a
  larger compositional change than the old bag-on-plaid it replaced. Editor's ruling.
- **s20→s21 did not become the steep step into the hero.** Δp90 **+0**, Δmed **+3** — the
  flattest luminance joint in the green run apart from s21→s22. The predicted −15 into the
  hero does not exist, because s20 landed at 43 rather than 50 and s21 is 44. What the
  joint does now is arrive at the hero on a *plateau*: two consecutive scenes at
  essentially identical brightness (43, 44) with the grade turning neutral→green across
  them. scdet rose 0.200→0.225, which registers the compositional change (shelf → macro
  loaf) and not a light step; the chapter's joint band is 0.124–0.243 and every text
  `rise` in the chapter still outscores every dissolve, so that number ranks nothing.
- **The trade is favourable and cost nothing at the hero.** s19→s20 improved by 6 p90;
  s20→s21 went from +7 to +0, i.e. *flatter*, not steeper. fin-assets was right about the
  direction at s19→s20 and wrong about both magnitudes; the feared regression at s20→s21
  did not materialise in either direction.

⚠ **Two new things the photograph brings, both worth a ruling:**

1. **The kicker lands on the photograph's brightest object.** "PER MONTH" sits directly
   over the ITALIAN EGGPLANT price card. Glyph mean **161.1** against an immediate
   backdrop of **60.4** → ratio **2.67**, the lowest of the eight well-formed kickers in
   the chapter (median 2.95; s16 high 4.27; s21 2.88, s22 2.98, s23 2.96). It reads, but
   the card's own printed type — "ITALIAN EGGPLANT", "$5.", "LB" — crosses the kicker's
   baseline. A small ken offset or a `.band` would clear it.
2. **Three dollar amounts that are not the scene's number** are legible in the frame
   ($1.99, $3.99, $1.99). Measured, they do **not** compete: Weber 0.28–1.55 against the
   focal `$847` at **21.57** and the foot at 12.40. They read as "grocery prices", which is
   the scene's subject, and they are correct US currency. Recording it because it is the
   kind of thing that reads worse on a contact sheet than in motion.

### 4d · Dead CSS removed — the geometry SURVIVED · PASS

`diff tools/scaffold/assets/chapter-design.css studio/.../assets/chapter-design.css` →
**byte-identical**. Both local patches and the `v-widefocal` hook are gone from
`index.html`/`build.mjs`; the rules now come from the scaffold. Measured from the encode
(frame centre x = 960.0):

| scene | element | x span | midspan | off-centre |
|---|---|---|---|---|
| s19 | focal `$10,169` | 756–1164 | **960.0** | **+0.0** |
| s20 | focal `$847` | 836–1084 | **960.0** | **+0.0** |
| s21 | focal `$254,225` | 724–1194 | **959.0** | **−1.0** |
| s21 | rate `.sub` | 664–1254 | 959.0 | −1.0 |
| s22 | focal (2 lines) | 239–1681 | **960.0** | **+0.0** |
| s17 | focal (2 lines) | 334–1584 | 959.0 | −1.0 |
| s23 | focal | 315–1606 | 960.5 | +0.5 |

All four centred arch-b scenes (2.11–2.14) are within **1.0px** of 960 — inside the 1.5px
requirement. Kickers read −2.0 to −2.5px, which is letter-spaced-caps glyph asymmetry, not
layout.

**s21's ladder track, against `.measure.under { left: calc(50% - 460px); top: 910px;
width: 920px; height: 7px }`:**

| Quantity | Spec | Measured |
|---|---|---|
| x span | 500–1419 | **500–1419** |
| length | 920 | **920** |
| midspan | 959.5 | **959.5** (off-centre **−0.5**) |
| y span | 910–916 | **910–916** (h 7) |
| `THE LADDER` label left edge | 500 | **500** |
| green fill | 0.1295 → 119.1px | 123px = **0.1337** (AA edges) |

The track agrees with the figure above it to **0.5px**. The 31px disagreement the local
patch was written for is still gone with the patch removed — the scaffold rule is doing
the work.

## 5 · Comma clearance — measured on `.huge`, and the `.mega` fix is IRRELEVANT HERE

**`grep -c 'class="mega' index.html` → 0. `grep -c 'class="huge' index.html` → 15.**
Every focal in this chapter is `.huge`. `.arch-b .mega { padding-bottom: .11em }` has
**no element to apply to in ch2** and protects nothing here; the credit it carries for the
lakh/crore rungs is misplaced for style E.

**The arithmetic, taken from the scaffold comment's own measured numbers.** The comment
states that at 300px/lh .84 the line box ends 9.5px under the baseline while comma ink
descends 42.19px. Solving those two for the font gives `ascent − descent = 0.7767em`.
Applied to `.huge` at 112px/lh .98 (line box 109.76px):

- line box ends **11.39px** below the baseline
- comma ink descends 0.1406em = **15.75px**
- → **overhang 4.36px = 0.039em**, i.e. the ~**.04em** figure, against arch-b's **18px**
  stack gap. Real, but incidental, and roughly a quarter of the gap.

Measured comma descent below the digit baseline in the encode: s19 **15px (0.134em)**,
s21 **16px (0.143em)** — matching the derivation.

**Actual ink-to-ink clearance, every `.huge` that has a following sibling:**

| scene | focal | arch (gap) | focal ink | next ink top | **clearance** |
|---|---|---|---|---|---|
| s10 | `How much can you draw…` (descenders) | D (18) | 466–615 | `.sub` 639 | **24px** |
| s13 | `William Bengen, Journal of…` (comma L1, `g` L2) | C (28) | 465–620 | `.foot` 665 | **45px** |
| s14 | `50% stocks / 50% bonds` | C (28) | 538–623 | `.foot` 670 | **47px** |
| s15 | `Three Trinity University professors.` (`y`) | C (28) | 447–622 | `.foot` 647 | **25px** |
| s16 | `95%` | B (18) | 240–321 | `.foot` 363 | **42px** |
| **s19** | **`$10,169`** | **B-ctr (18)** | 481–**581** | `.foot` **607** | **26px** |
| s20 | `$847` (no comma) | B-ctr (18) | 499–590 | `.foot` 625 | **35px** |
| **s21** | **`$254,225`** | **B-ctr (18)** | 535–**635** | `.foot` **662** | **27px** |

`.huge` is the last child in s9, s11, s12, s17, s18, s22 and s23 — nothing follows, so no
clearance exists to measure. s22's `$254,225 at 4.0% · …` wraps to two lines inside one
element (ink band 501–652) with no intra-element collision.

**Nothing collides. The tightest comma figure is s19 at 26px of clear ink**, against hi
ch2's reported 12px. The margin here comes from the `.foot`'s own half-leading, not from
the `.mega` rule.

## 6 · Cross-dissolves — all 14 joints, BOTH `qa.dissolve_sample_offsets` · PASS

Sampled at `start+0.225` **and** `start+0.380` per `format.json`. Residual alpha of the
**outgoing** scene's text measured as a linear unmix: a mask of the outgoing type
(bright at `start−0.10`, dark at `start+0.60`), then
`(observed − incoming_only) / (outgoing_clean − incoming_only)` on that mask.

| joint | mask px | clean out | in only | +0.225 | +0.380 | **α@.225** | **α@.380** |
|---|---|---|---|---|---|---|---|
| s9→s10 | 46,025 | 162.0 | 32.6 | 92.1 | 34.9 | 45.9% | **1.7%** |
| s10→s11 | 71,070 | 161.0 | 41.1 | 94.6 | 43.0 | 44.6% | **1.6%** |
| s11→s12 | 46,932 | 162.7 | 39.9 | 93.5 | 42.0 | 43.6% | **1.7%** |
| s12→s13 | 40,324 | 231.1 | 55.8 | 124.4 | 62.0 | 39.2% | **3.5%** |
| s13→s14 | 73,096 | 162.6 | 35.8 | 96.5 | 38.2 | 47.9% | **1.9%** |
| s14→s15 | 61,507 | 223.7 | 37.1 | 127.8 | 41.7 | 48.6% | **2.5%** |
| s15→s16 | 61,807 | 160.3 | 42.1 | 103.1 | 45.7 | 51.6% | **3.1%** |
| s16→s17 | 24,529 | 157.7 | 36.1 | 98.0 | 38.7 | 50.9% | **2.1%** |
| s17→s18 | 59,589 | 162.7 | 39.2 | 93.3 | 40.9 | 43.8% | **1.4%** |
| s18→s19 | 52,082 | 136.6 | 42.9 | 78.0 | 46.0 | 37.5% | **3.3%** |
| s19→s20 | 30,611 | 160.2 | 24.2 | 83.2 | 25.9 | 43.3% | **1.2%** |
| s20→s21 | 19,485 | 204.9 | 34.6 | 100.0 | 39.8 | 38.4% | **3.1%** |
| s21→s22 | 36,805 | 138.2 | 39.8 | 81.9 | 41.3 | 42.8% | **1.5%** |
| s22→s23 | 53,578 | 135.3 | 36.6 | 85.2 | 39.5 | 49.3% | **2.9%** |

**No stacking-context defect.** The `japanese-money-methods-hi` signature is the outgoing
text at ~100% for the full 0.45s at every boundary. Here it is 37.5–51.6% at the midpoint
— which is what a cross-dissolve *is* — and **1.2–3.5% by +0.380**, i.e. gone before the
overlap ends, at all fourteen. `isolation: isolate` on `.scene` is present at
`assets/blockframe.css:63`.

⚠ **Read this before reading the frames.** At `s20→s21 +0.380` the outgoing `$847` and its
foot ARE faintly visible over s21's rising "RUNG ONE" and ladder track, and it looks like a
double-paint. Measured, it is **3.1%** — the tail of a correct dissolve, visible only
because s21's opening frame is the darkest ground in the chapter so a 3% residual has
somewhere to show. This is the one place where the eye and the measurement disagree, and
the measurement is right.

## 7 · The full tone curve — four things changed in it

Method unchanged from attempt 1 so the numbers are comparable: decoded once to 192x108
greyscale on a 10fps grid (1055 samples), each scene measured over its BODY only
(`start + 0.45` to the next scene's start), percentiles over pooled pixels.

| scene | body (s) | samples | p10 | p50 | **p90** | mean | p90 was |
|---|---|---|---|---|---|---|---|
| s9  (2.1 open) | 0.00–5.16 | 52 | 21 | 46 | **57** | 44.0 | 57 |
| s10 (2.2) | 5.61–15.76 | 101 | 18 | 28 | **44** | 32.2 | 44 |
| s11 (2.3) | 16.21–23.92 | 77 | 18 | 37 | **53** | 38.1 | 53 |
| s12 (2.4) | 24.37–27.78 | 34 | 21 | 27 | **47** | 33.3 | 47 |
| s13 (2.5) | 28.23–34.67 | 64 | 16 | 46 | **57** | 44.7 | 57 |
| **s14** (2.6) | 35.12–41.74 | 66 | 24 | 31 | **44** | 37.8 | **40** |
| s15 (2.7) | 42.19–48.81 | 67 | 23 | 37 | **53** | 39.6 | 53 |
| s16 (2.8) | 49.26–55.17 | 59 | 16 | 34 | **55** | 34.6 | 55 |
| **s17** (2.9) | 55.62–62.66 | 70 | 20 | 30 | **46** | 34.4 | 46 (mean was 36.7) |
| s18 (2.10) | 63.11–70.28 | 71 | 19 | 35 | **51** | 36.3 | 51 |
| s19 (2.11) | 70.73–76.82 | 61 | 17 | 39 | **59** | 39.3 | 59 |
| **s20** (2.12) | 77.27–84.31 | 71 | 15 | 22 | **43** | 26.4 | **35** |
| s21 (2.13) | 84.76–90.39 | 56 | 15 | 25 | **44** | 28.5 | 44 |
| s22 (2.14) | 90.84–97.77 | 69 | 15 | 33 | **46** | 33.5 | 46 |
| s23 (2.15) | 98.22–105.52 | 72 | 16 | 30 | **44** | 31.5 | 44 |

Duration-weighted by scene `data-duration`, same segmentation as attempt 1:

| segment | dur (s) | p90 range | **p90 dur-wtd** | was | mean dur-wtd |
|---|---|---|---|---|---|
| amber head s9–s11 | 25.27 | 44–57 | **50.0** | 50.0 | 36.8 |
| C evidence run s12–s15 | 26.68 | 44–57 | **50.6** | 49.5 | 39.5 |
| amber verdict s16–s17 | 14.75 | 46–55 | **50.2** | 50.2 | 34.5 |
| green method + bill s18–s20 | 23.00 | 43–59 | **50.7** | 47.9 | 33.8 |
| green corpus close s21–s23 | 22.11 | 44–46 | **44.7** | 44.7 | 31.3 |
| **whole chapter** | **105.52** | **43–59** | **49.2** | **48.4** | **35.4** |

Last 30s (s18–s23) weighs **47.7** (was 42.1).

**What fin-editor needs to know: the chapter's tonal FLOOR is gone, and with it the arc.**

1. **Range span collapsed from 24 to 16.** 35–59 → **43–59**. s20 was the darkest scene in
   the chapter by 9 points; it is now tied for third-brightest of the last five.
2. **The descending slope is now a plateau and a step.** The segment curve was
   50.0 → 49.5 → 50.2 → 47.9 → 44.7 — the shape fin-editor ruled "right". It is now
   **50.0 → 50.6 → 50.2 → 50.7 → 44.7**: flat within 0.7 of a point for the first 84
   seconds, then one drop of 6 into the green close. The chapter is no longer a slope with
   a spike at the front; it is a level plateau with a single terminal step.
3. **The open is unchanged and fin-editor's earlier objection stands verbatim.** s9 is
   still 57, s10 still drops to 44 at 5.16s. But the open is now only **+7 over the
   plateau** it sits on, where it was +7 over a 48.4 average that contained a 35 floor. The
   open reads *less* distinct than it did, not more, without a single pixel of s9 changing.
4. **s14 (+4) and s20 (+8) both moved up; nothing moved down.** Duration-weighted p90 rose
   48.4 → 49.2, against ch1's reported band of 36–48. The chapter now sits fully above
   ch1's ceiling rather than at it, which is the "lighter chapter" reading — achieved, but
   achieved by removing contrast rather than by adding light at the top.
5. **The p10 floor is still flat at 15–24 and s20 proves fin-editor's lever ruling.**
   Swapping one photograph moved that scene's p90 by **+8** and its p10 by **0** (15 → 15).
   The photograph owns the highlights; `.scrim`'s four stacked gradients own the shadows.
   If the chapter needs to READ lighter rather than peak lighter, the scrim floor is still
   the only control, exactly as ruled.

## 8 · Draft audio (informational — master QA still owed)

| Quantity | Measured | Gate |
|---|---|---|
| overall peak level | **−3.48 dBFS** | — |
| **true peak** (`loudnorm`) | **−3.22 dBTP** | below −1 dBTP ✓ |
| integrated | −21.18 LUFS | — |
| LRA | 3.20 | — |

## Reference numbers for the next gate

Not measured at this stage (chapter draft mode): per-line VO drift against the `data-start`
table, faster-whisper coverage, runtime vs `timing.json`. Those belong to the master QA
pass on `renders/FINAL-1080p-en.mp4`, and the VAD onsets there must have
`qa.vad_onset_latency_seconds` **0.101** subtracted before comparison (Silero quantises to
0.032s and reports late; raw values read as a false FAIL).

Chapter total for the joint arithmetic: **3166 frames @ 30fps = 105.5333s**. s23 carries
its BARE `scene_duration` (no successor in this project), so `cut_assemble.py` adds +0.45
back at fold-in.
