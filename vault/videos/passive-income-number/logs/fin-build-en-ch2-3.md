---
summary: en ch2 attempt 3 — regenerate over the two replaced photographs (s21, s15) plus the two free editor should-fixes. Both one-line fixes landed, and ONE of the two turned out to be a different defect than reported: `.band` is geometrically incapable of reaching s20's kicker (band starts y 497, glyphs are at y 438-459) so the ken-offset route was the only one of the two that works, and s14's grey half was not at `.22` at all — `fade()` had been overwriting that attribute to 1.0 since the layer was drawn. Chapter unchanged at 105.518s / 15 scenes. check 0 errors + 11/11 AA, check_vo_frame PASS, cues.py exit 0, pipeline_check PASS build-en. 29 frames read across 7 batch dirs.
updated: 2026-08-08
source: run.json chapters.en.2 (read in full) · logs/ceo-en-ch2-1.md · logs/editor-en-ch2-2.md · logs/fin-assets-en-ch2-3.md · logs/fin-build-en-ch2-2.md · tools/format.json chapter_design + vector_art + layout · assets/blockframe.css .bg/.band/.stack · assets/js/motion.js fade/ken · 29 snapshot frames measured with PIL, 7 batch dirs
stage: fin-build, cut en, chapter 2, attempt 3
---

# build · passive-income-number · en · chapter 2 · attempt 3 (two images, two one-liners)

**105.518s · 15 scenes · s9–s23 · unchanged.** Every `data-start`, `data-duration`,
`data-framings`, the `S`/`D` maps, the fifteen `<audio>` rows and the root duration still
come from `timing.json` through the same asserts. The rate-assert block, s14's 0.5006
split geometry, s17's two ringed dates, s22's `tick`, s10/s10b, s9 and everything between
s9 and s20 are byte-unchanged, and no local CSS patch and no `v-widefocal` hook came back
(`assets/chapter-design.css`, `blockframe.css` and `motion.js` all diff clean against
`tools/scaffold/`).

| gate | result |
|---|---|
| `npm run check` | **0 errors, 0 warnings**, 12 info (the `known_benign` `.bg` ken overflows), Contrast **11/11 AA**, Runtime 0/0, Motion 0/0 |
| `tools/check_vo_frame.py … --chapter 2` | **PASS** — 15 scenes cross-checked |
| `tools/audio/cues.py …-en-ch2` | **exit 0** — 25 cues, unchanged |
| `tools/pipeline_check.py check build …` | **PASS build-en** |
| mtimes | `s15.jpg` 16:07:27 · `s21.jpg` 16:08:35 · `build.mjs` 16:26:46 · `index.html` 16:26:58 — strictly ordered |

## 1 · The two replaced photographs — regenerated and read, both blockers closed on the frame

Nothing in the composition pointed anywhere new; the value of the rebuild was reading the
frames. Both hold, and both were checked at the ken's TIGHTEST instant, which is where the
old s15 failed (both scenes are `ken: "o"`, so frame one is 1.16×).

- **s21 @ 88.16 and @ 90.0 — the payoff frame now reads as bread**, unmistakably: crumb,
  crust, flour, board grain, the cut slices at left. Cover the type and the frame says
  *food / the grocery bill*. The CEO's "green mossy mass … reads as a rock or a cabbage"
  is gone.
- **s15 @ 42.0 (tightest), 44.14 and 46.5** — 46.5 is the exact timestamp the CEO called an
  unidentifiable pale curve; it is now an open volume with a stack of three cracked-spine
  bound volumes at frame right, frayed headbands visible. Sound-off holds through the whole
  ken. `Breton  75` sits faint at bottom-left as fin-assets declared, ~8% of frame width;
  I am not treating it as legible text under §10 and I agree with the reasoning filed.
- **`build.mjs`'s stale s15 note is fixed** (fin-assets' rebuild note 1). It described the
  replaced file. s21's note carried no image description, so it needed nothing.

## 2 · s20 `PER MONTH` — the `.band` route is GEOMETRICALLY IMPOSSIBLE here

The brief offered `.band` or a ken offset, "whichever is smaller". `.band` is smaller to
type and cannot work, and I measured that before choosing rather than after:

- `.band` is `bottom: 0; height: 54%` with its gradient at **alpha 0 at its own top edge**,
  so it begins at **y 497** and only reaches .45 at y 718.
- s20's kicker glyphs measure **y 438–459** (scanned off the encode-equivalent frame at
  80.5). The band has **zero overlap with the collision** and would darken only the foot.
  Moving the type down to meet the band would move a reviewed, centred layout.

**So the ken offset, and it is one line.** `.bg` is `background-size: cover` inside an
`inset: -8%` box (2227×1253). s20's source is 1880×1253 — aspect 1.50 against the box's
1.78 — so cover scales it to 2227×1484: **231.6px of vertical slack and exactly zero
horizontal**, which `background-position: center` was throwing away symmetrically.
`center bottom` spends 115.8px of it and lifts the whole price-card row **116–134 frame px**
clear of the kicker across the ken's full 1.00→1.16. Verified at **78.0 / 80.5 / 83.0** —
clear at all three, and the three price cards stay in frame, so the scene still reads as a
store. Same file, same grade, same `ken` call, same direction, same stack, no new layer.

`bgpos` is emitted as an optional inline style beside `background-image`, the same shape
the `.bg` line already had.

**The ratio question, answered: yes, and by a lot.** Measured on identical boxes
(y 434–464, x 845–1075), glyph vs backdrop mean luma:

| | glyph | backdrop | backdrop max | luma ratio |
|---|---|---|---|---|
| before | 154.6 | **40.9** | 99.9 | 3.78 |
| after | 155.9 | **18.3** | 99.3 | **8.52** |

My box is not fin-render's box (it read 161.1 / 60.4 = 2.67), so read the **change**, not
my absolute: the backdrop mean falls **2.24×**. Scaling fin-render's own figure by that
puts the kicker near **6.0** against the chapter median of 2.95 — it goes from the lowest
of eight to comfortably above the median. Fin-render should settle the number from the
encode; the direction is not in doubt. Scene tone barely moves: composed p90 42.9 → 43.9,
p10 14.0 → 14.5, so the s19→s20 and s20→s21 joints are as fin-editor left them.

## 3 · s14 — the reported number was DEAD CODE, and that was the whole defect

The finding was "drop the grey track below its current `.22`". **It was never at `.22`.**
The ghost carried `opacity=".22"` as an SVG attribute and its own cue is
`fade("#s14-track", …)`, which animates **opacity 0 → 1**. GSAP overwrote the attribute on
its first frame, so the track has rendered at **1.0** since the layer was drawn — `--ink`
at full weight against `--target`, which is a dark gold. That is why the empty half was
21.7 luma louder than the filled half on the frame whose job is to say the two are equal.
Lowering `.22` to `.13`, which is what the finding literally asked for, changed **nothing**:
I built it, snapshotted it, measured it, and got the identical 82.1 / 60.0.

**Fix: `fill-opacity`, which `fade()` does not touch and cannot clobber.** The entrance
still fades. Compositing is linear in alpha over a fixed backdrop, so the value is a ratio
and not a guess: (60.0 − 32.5) / (82.1 − 32.5) = **.554** → `GHOST_A = 0.55`.

| s14 @ 41.0 | amber (filled) | grey (unfilled) | ground | delta |
|---|---|---|---|---|
| before | 60.0 | 82.1 | 32.5 | **+22.1** |
| after | 60.0 | **61.0** | 32.5 | **+1.0** |

Still a SOLID FILLED rect and never an outline, which is what format.json's "~.2" line is
actually protecting: a 28-luma step across 800×120px survives any encode; a 3px stroke at
.4 does not. `SPLIT`, the tick and `art-forward .52` are untouched, and the split still
computes from the one constant.

**Checked for siblings before editing, per root-cause discipline:** `s16-r10`'s five grid
ghosts also carry `opacity=".22"`, but their cue targets the parent `<g>`, not the rects,
so those are live and correct. `#s14-track` is the only element in the chapter faded on
itself. Nothing else in the chapter has this bug.

## 4 · Evidence for the CEO's open metric question (declared, not settled here)

The CEO owns whether clause 2 is judged on p90 or on median/mean. fin-assets computed its
table on the RAW sources through the grade. I can offer the next step in — the same four
statistics on **composed frames** (grade + `--fund` tint + scrim + type + grain), one per
scene at its last cue:

| statistic | s21 value | s21 rank of 15 | top of the ranking |
|---|---|---|---|
| p10 (the floor) | **26.8** | **#1**, 2.9 clear of #2 | s21 · s14 · s12 |
| p50 (median) | 42.9 | **#3** | s9 · s13 · s21 |
| mean | 43.0 | **#3** | s13 · s9 · s21 |
| p90 | 52.9 | #7 | **s15** (61.2) · s16 · s19 |

Two honest corrections to fin-assets' framing, in opposite directions:

1. **Its p90 finding is confirmed on composed frames.** s15 — a dark photograph with one
   white page — ranks **#1 of fifteen on p90** while ranking #10 on median. The statistic
   really does select the spiky mostly-dark still.
2. **But "s21 is #1 on mean" does not survive composition.** On the raw source it was #1;
   composed it is **#3**, behind s9 and s13, because the `--fund` tint, the scrim and the
   green type all pull it down and the amber scenes are not tinted the same way. It is #1
   only on the floor. That is still a move from **last of fifteen to first** on p10 and the
   defect the CEO actually described is closed — but the ranking should be quoted from the
   composed frame, not the source, and fin-render should re-derive all of it from the
   encode.

**And the miss stays a miss.** My composed p90 for s21 is **52.9** against the ruling's
`≥ 55`, consistent with fin-assets' 53–55 prediction and at its low end. I am not rounding
it. s21's type reads fine on it — kicker 3.37, rate 3.39, focal 3.69, foot 3.47 luma-ratio,
all above the chapter's 2.95 median, because the scrim keeps the type band at ~44 while the
photograph's highlights sit outside it.

## 5 · Snapshots actually read — 29 frames, 7 batch dirs

One `-o` per batch, because `snapshot` wipes its output directory. The CLI threw
`Navigation timeout` on two invocations; both were retried until they succeeded.
Also learned: **multiple `--at` flags do not stack — only the last is honoured.** It is
`--at 1.0,2.0,3.0`. Four flags produced one frame, silently. Worth the next stage knowing.

| dir | frames | what |
|---|---|---|
| `snapshots/qa/m0` | 2 | s20 @80.5 BEFORE — the measurement that killed the `.band` route |
| `snapshots/qa/m1` | 2 | s14 @41.0 BEFORE — the amber/grey/ground baseline |
| `snapshots/qa/r3b1` | 5 | s20 @78.0/80.5/83.0 (ken start, mid, end) + the failed `.13` s14 attempt |
| `snapshots/qa/r3b2` | 3 | s14 @38.0/41.0 with `fill-opacity` — the A/B that settled it |
| `snapshots/qa/r3b3` | 9 | s9 s10 s11 s12 s13 s14 s15 s16 at their last cue |
| `snapshots/qa/r3b4` | 8 | s17 s18 s19 s20 s21 s22 s23 at their last cue |
| `snapshots/qa/r3b5` | 5 | s15 @42.0 (1.16× tightest) / @46.5 · s21 @84.6 (dissolve) / @90.0 |

All fifteen scenes covered at or after their last cue; six opened at full resolution, the
rest read as contact-sheet cells and measured numerically. Every `.stack` inside the safe
area, no overflow, no collision, no half-built mechanism.

## 6 · System gaps found (reported, not improvised)

1. **`fade()` silently clobbers an SVG `opacity` attribute** and there is nothing in
   `motion.js`, `chapter-design.css` or `format.json` that says so. Any drawn element given
   a resting opacity AND a `fade` cue renders at 1.0, with every check green — the frame
   just looks wrong, which is exactly the class of defect this pipeline keeps paying two
   rounds to catch. Two candidate fixes for `tools/scaffold`: have `fade()` animate to the
   element's authored opacity instead of a hard `1`, or a `format.json chapter_design.gotchas`
   entry saying **a resting alpha under a `fade` must be `fill-opacity`/`stroke-opacity`,
   never `opacity`**. The gotcha is the cheaper of the two and cannot break an existing cut.
2. **`.band` has no top-anchored sibling.** It is the one prescribed mechanism for "darken
   behind" and it only reaches the bottom 54%, so a collision above frame centre — which is
   where every `.centred` kicker sits — has no system answer at all. Both times this chapter
   reached for `.band` it worked because the target was low in frame; s20 is the first case
   where it did not, and the composition had to go to the photograph instead. A `.band.top`
   in `chapter-design.css` is the obvious shape.
3. Carried unchanged from attempt 2 and still true: `cues.py` reads `cue_min_gap_seconds`
   from the top level of format.json where it lives under `layout`; `cues.py` validates the
   shipped `audio.json` as well as the derived one (still worked around by `rmSync` in
   `build.mjs`); no motion helper scales a bar on the Y axis.

## 7 · What was NOT touched

Timing, framings, the `S`/`D` maps, the audio rows, the root duration, the 25 cues, the
rate-assert block and all four figure foots, s14's split geometry and tick, s17's rings and
`.band`, s18, s22's `tick`, s10/s10b, s9, the grade, every ground hex, every `.scrim`, the
type ladder, and both removed local CSS patches. Drawn-layer count stays at **4**, the cap.
