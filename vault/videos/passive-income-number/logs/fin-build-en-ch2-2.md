---
summary: en ch2 attempt 2 — targeted fix pass, not a rebuild. Both build-owned blockers fixed by DRAWING (s14 a bar split at exactly 0.500 on p-c; s17 the chapter's own two publication dates ringed on p-a), the s18 cue gap moved 0.600s -> 1.100s, and both dead local CSS patches removed now that the scaffold carries them. check 0 errors, cues.py exit 0, check_vo_frame PASS. No timing, no data-framings, no rate-assert and no s20/s10/s22 edit.
updated: 2026-08-08
source: logs/editor-en-ch2-1.md · run.json chapters.en.2 · tools/format.json chapter_design + vector_art + layout · storyboard-en.md §7/§8/§10 · vault/knowledge/design-chapter-archetypes.md · 16 snapshot frames read in 4 batch dirs
stage: fin-build, cut en, chapter 2, attempt 2
---

# build · passive-income-number · en · chapter 2 · attempt 2 (targeted fix)

Chapter unchanged at **105.518s, 15 scenes, s9–s23**. Nothing in the timing block was
touched: every `data-start` / `data-duration` / `data-framings`, the `S`/`D` maps, the
fifteen `<audio>` rows and the root duration still come from `timing.json` through the
same asserts, and all of them still pass. `npm run check` **0 errors**, contrast
**11/11 AA**, runtime 0/0, motion 0/0.

## 1 · s17 — the date, drawn (blocker #1)

The frame had no date under a line whose whole content is *"a finding with a date"*.
`assets/lottie/calendar-20th-circled.json` was read and **rejected as the vehicle**: it
circles the 20th of a generic month, so it would have put a number on screen that means
nothing here, and it would have needed `lottie.min.js` plus a wrapper vendored into a
project that has neither. The library rule is *reuse before fetch*, not *reuse before
think* — the honest asset was a drawing, and it costs no fetch either.

`date-axis`, authored in **p-a's own space (`0 0 1920 1080`)**, sits below the centred
stack: a short time line, two ticks, and **OCTOBER 1994** / **FEBRUARY 1998** each ringed
by an ellipse that is **drawn** (`draw()`, 12px stroke set inline — gotcha 1) rather than
faded, so the *circling* is the motion. Both dates are the chapter's own citations,
already on screen at s13 and s15, so nothing is invented (truth_bar). The line **stops**
120px past the second date and nothing follows it; that emptiness is the second sentence.
Assembled by **+3.20**.

- The archetype is unchanged. A is "centred stack, one motif full-bleed behind", and A
  declares no stack rules, so removing `.centred` moved the type by nothing measurable —
  it only stops `display:none`-ing the plate. Verified on the frame.
- **`.band`, not `.art-lift`.** The plate here *is* the frame, so a lift would darken the
  whole photograph (rule 9). Measured reason it needed one at all: the kraft paper under
  the motif is the brightest ground in the chapter (**p50 97** after the grade), where
  amber at .52 would have read at ~133 against 97.
- **Residual, for fin-editor:** the stamp box is still the photograph. The parent stage
  ruled draw-don't-refetch, so the *"stamped / approved"* connotation the editor flagged
  is mitigated (the drawn dates now own the lower half and the type denies the promise)
  but not removed. If that connotation is still the objection, it is a fetch, not a build.

## 2 · s14 — the 50/50 split (blocker #2)

`split-bar` on **p-c (`0 0 934 1200`)**: one track filled to **exactly 0.500**. `SPLIT`
is written once and drives both the drawn midpoint marker and the `span()` endpoint, so
the picture and the animation cannot disagree — `fill()` was wrong here because it always
runs to scaleX 1. Ghost is a **filled rect at .22**, never an outline; nothing thinner
than 10px. Track ends at screen x 1886 (s16's own right edge), fully on canvas.
Assembled by **+2.95**. s14 is on the DRY list, so this adds **zero** cues.

Two consequences, both deliberate and both visible in the snapshots:

- **The scene leaves `.centred`.** A centred scene structurally cannot hold a drawn layer
  (`.scene.centred .plate { display:none }`), and `.centred` exists for a split with
  *nothing* opposite — which is no longer true. It returns to archetype C's own layout,
  which is what §7 assigned it before rule 8 turned the art off.
- **`50% stocks · 50% bonds` becomes a line break, not a smaller focal.** C's column is
  880px and 22 characters at 112px is ~1364px. The focal stays at the **top** of the
  ladder; the two items are typeset as two lines instead of joined by this cut's `·`.
  Restructured, not shrunk — the ladder floor was never approached.

**`.art-lift` was tried and rejected on the frame** (`snapshots/qa/r2b1` vs `r2b2`). §8's
trigger fires — the source is pale birch — but p-c is 934×1200, a full-height quarter of
the frame rather than s16's 860×610 corner, and the lift painted a hard-edged near-black
panel that erased the photograph it exists to preserve. **Carry-forward: `.art-lift` is a
corner-plate mechanism. Do not reach for it on p-c or p-a.**

## 3 · Drawn-layer density is now AT the top of the range

Two planned (§8) plus these two = **four in fifteen scenes**. The archetype note's
calibration is "three or four in a twelve-to-fourteen scene chapter is the **top** of the
range, not the target", so ch2 is at the ceiling and **chapters 3–6 must not read this as
a new baseline** — §8 budgets ch3 1, ch4 1, ch5 0, ch6 3 and those numbers stand. Both
additions pass rule 8's additive test: a card catalogue cannot say *half and half*, and a
box of stamps cannot say *these two dates and nothing after them*.

## 4 · The s18 cue gap (should-fix #6)

`fade("#s18-band")` moved **+0.60 → +1.10**, and the four mechanism cues shifted with it
(bill 1.60, div 1.95, eq 2.25, corpus fill 2.50/0.80) so the band still precedes what it
darkens behind and the whole thing still lands at **+3.30**, inside chapter_design's
"about +3.3". The band fade *is* this scene's derived `reveal`, so the gap against its own
joint is now **1.100s**. Every gap in the chapter's 25 cues is ≥1.100.
`python3 tools/audio/cues.py studio/videos/passive-income-number-en-ch2` **exits 0**.
Cue count, names and the `bed-tension` bed are unchanged.

## 5 · Both dead CSS patches removed

`.scene.centred .stack { padding-left: 0 }` and the `.arch-b .v-widefocal` cap are gone
from the emit, with their "SYSTEM GAP" / "ONE-OFF" comments. `tools/scaffold/assets/
chapter-design.css` and this project's copy are byte-identical (diffed), and both rules
are in it. The `v-widefocal` **class** went with the rule rather than being left as an
unstyled hook — the upstream fix is selector-scoped (`.scene.centred.arch-b .huge/.foot`).

One real rendering change falls out of that port and I checked it rather than assuming:
upstream lifts the **`.foot`** cap too, so s19–s22's foots now wrap at 1500px instead of
900px. All four re-read clean on the frame (`snapshots/qa/r2b3`), s21's ladder track still
agrees with its figure, and s19's provenance foot sets as two lines.

## 6 · What was NOT touched, as instructed

s20 (fin-assets re-fetch, same filename — the slot is untouched), the rate assert block,
s22's `tick`, s10/s10b, and every timing. `check_vo_frame` still **PASS**.

## Snapshots actually read — 16 frames, 4 batch dirs

One `-o` per batch, because `snapshot` wipes its output directory.

| dir | frames | what |
|---|---|---|
| `snapshots/qa/r2b1` | 3 | s14 @37.7 (with `.art-lift`), s17 @58.5, s18 @66.0 |
| `snapshots/qa/r2b2` | 1 | s14 @37.7 again, `.art-lift` removed — the A/B that settled it |
| `snapshots/qa/r2b3` | 4 | s19 @73.6, s20 @80.0, s21 @88.1, s22 @93.0 — the four scenes the CSS port re-wraps |
| `snapshots/qa/r2b4` | 8 | s9, s10, s11, s12, s13, s15, s16, s23 at their last cue times — the unchanged eight |

All fifteen scenes are therefore covered at or after their last cue. Every `.stack` sits
inside the safe area; no overflow, no collision, no half-built mechanism.

## System gaps found (reported, not improvised)

1. **`cues.py` reads `cue_min_gap_seconds` from the TOP level of format.json, where it
   does not live** — it is under `layout`. `fmt.get("cue_min_gap_seconds", 0.8)` therefore
   always returns the *default*, which happens to equal the real constant today. Change
   `layout.cue_min_gap_seconds` and the new check silently keeps enforcing 0.8. One-line
   fix in a file this stage may not write.
2. **`cues.py` validates the SHIPPED `audio.json` as well as the one it just derived, and
   exits 1 on either** — so the build run that FIXES a gap dies on the artefact it is
   fixing, before it can write the replacement. Worked around inside `build.mjs` (it
   `rmSync`s `assets/audio.json` immediately before invoking the tool, and regenerates it
   two lines later). The tool-side fix is to validate the shipped list only when it is not
   about to be overwritten.
3. **No motion helper scales a bar on the Y axis.** `fill`/`span` are scaleX only, so a
   vertical proportion — which is the natural shape for a tall p-c plate — cannot be
   animated with the system as it stands. s14 used the horizontal form (also §8's own
   shape for s30), which is the nearest thing that exists. Worth a `spanY` in
   `tools/scaffold/assets/js/motion.js` before ch6's ladder work.
