# fin-build · financial-freedom-after-50 · en · chapter 1 · attempt 2

REWORK fix pass on the existing project. Three fixes, all of them framing values or
layout classes. **No timing value changed anywhere** — every `data-start`,
`data-duration`, `data-framings`, `<audio>` row and the root duration is byte-identical
to attempt 1 (Evidence 5).

## Ran

1. Read `vault/CLAUDE.md`, `tools/packs/fin-build.md`, `tools/format/fin-build.json`
   (`chapter_design`, `known_benign`, `layout`), both prior logs. **No note body opened** —
   the pack + the two stylesheets + `motion.js` answered everything, so there is no
   `OPENED-BODY:` line to widen the pack from.
2. Read `assets/js/motion.js` `ken` / `plateKen` and `assets/blockframe.css` `.bg`, and
   `assets/chapter-design.css` `.arch-d` / `.scene.centred`, to find the actual mechanism
   behind blockers 1, 3 and 4 rather than guessing at scale numbers.
3. Measured the two subjects that must not leave frame, in image pixels (Evidence 1, 3).
4. Simulated the `.bg` transform chain offline (`scratchpad/visible.py`) to pick ken
   endpoints from numbers instead of from a re-render, then validated the simulator against
   `hyperframes check`'s own `container_overflow` measurement (Evidence 2).
5. Edited `build.mjs` (the generator — it owns the design spec; `index.html` is output),
   `node build.mjs`.
6. `npm run check` → **passed**.
7. Two snapshot batches into **two separate `-o` directories**, 17 frames, all 17 looked at
   (Evidence 6). Both invocations succeeded first try; no `Navigation timeout` retry needed
   on this run.

## Failed

- Nothing blocked. Two things were tried and rejected on measurement before they reached a
  render:
  - **`plateKen(…, 1.00, 1.05)` on s3** — the obvious "gentle push, start at the widest".
    Rejected: at scale 1.00 the widest frame the stock ken can reach still leaves only
    **24 px** of margin to the right of the `5` (Evidence 1), and at 1.05 the `5` clips.
    The zoom-in direction had no room at all; the fix had to go *below* scale 1.0.
  - **A larger push on s11 to make the aperture dominate the frame.** To fill 45 % of frame
    width the 347 px-wide aperture needs scale ≈ **2.10**, i.e. a 771 px source region
    upscaled 2.5× from an 1880 px JPEG. Rejected as a softness defect traded for a darkness
    one; the aperture is a narrow slot in the photograph fin-assets picked and the framing
    cannot change that.
- `node build.mjs` threw once — `SyntaxError: Unexpected identifier 'centred'`. The chapter
  header comment lives *inside* the generator's template literal, so a backtick in prose
  terminates it. Fixed with straight quotes. Worth knowing before editing that comment again.

## Evidence

**1 — s3, blocker 1: the mechanism, in pixels.** `s3.jpg` is 1880×1253. Thresholding the tan
numerals against the red ground over the top 62 % of the frame puts the numeral row at
**x 206…1726** (10.96 %…91.81 %), y 255…743.

`.bg` is `inset:-8%` + `background-size:cover`, so the element is 2227.2×1252.8 and a 3:2
source is cover-fitted by width — i.e. **at scale 1.00 only 86.2 % of the image width is on
screen**, and `ken(sel, at, dur, false)` *starts* at scale 1.16 with `xPercent:+2.5`.

| framing | visible image window (px) | verdict |
|---|---|---|
| old `ken(false)` start, k=1.16 x=+2.5 | 201 … **1598** | **128 px of the `5` off-canvas** — the right third of the glyph, for the first ~2 s |
| old `ken(false)` end, k=1.00 x=−2.5 | 177 … 1797 | all five, 29/71 px margin |
| k=1.00 x=0 (stock ken's widest, centred) | 130 … 1750 | all five, **24 px** right margin |
| **new** `plateKen(0.94)` start | 78 … 1802 | all five, 128/76 px margin |
| **new** `plateKen(0.87)` end | 9 … 1871 | all five, 197/145 px margin |

So the count was countable only in the *back half* of the scene. That is blocker 1's actual
cause and it is a ken value, not a picture: fin-assets' replacement image is fine.

**2 — the scale floor is 0.8621, not 1.0, and the simulator is exact.** Because `.bg` is
`inset:-8%`, the element only stops covering 1920×1080 below **1/1.16 = 0.8621**. At 0.87 it
is 1937.7×1090.0 — 8.85 px and 5.0 px of overscan per side, so no `--bg` can leak. This is
what buys s3 a real 7.5 % move while staying wider than the stock ken's widest frame.
The offline model was checked against the renderer: `hyperframes check` reports
`container_overflow #s3-bg … left 82.21px, right 82.21px` at t=11.45 s; the model predicts
k=0.9357 ⇒ 82.0 px. Agreement to 0.3 %.

**3 — s11, fix 3: the aperture bbox.** Luminance > 90 over the whole file puts the doorway at
**x 674…1021, y 78…1233** — 18.5 % of image width, and taller than any framing, so vertically
it crosses the frame at every scale. New endpoints: k=1.08 ⇒ window 190…1690, k=0.98 ⇒
113…1767. The aperture clears both edges by ≥ 476 px throughout the 3.621 s.
Note for the record: the *old* `ken(false)` window (201…1598 at its tightest) also contained
the aperture — the risk fin-assets named was the **±2.5 % `xPercent` pan**, which walks the
slot 111 px across the frame during a 3.6 s scene. `plateKen` has no pan, so it is gone.
Direction is still a pull-back, so s10-in → s11-out alternation holds.

**4 — s9 / s10, blocker 3.** Both were `arch-d has-photo art-off` with no `centred`.
`chapter-design.css` `.arch-d .stack` is `align-self:start; margin-top:34px`, so the chip row
renders at the TOP of the frame and `.brule` at `top:424px` sat under it with the whole
656 px band empty. Took fin-assets' Owed 2 = the reviewer's own fallback: `centred: false`
deleted from both SPEC rows, which makes the generator (a) emit `centred` and (b) skip the
`brule` line entirely. `grep 'brule' index.html` now returns **0 element matches** (3 hits,
all inside prose comments) and **0 of 11** scenes lack `centred`. Verified on frames, not
just in source: 53.79 s and 59.70 s (Evidence 6) show both chip rows at frame centre with no
rule and no empty band.

**5 — nothing was re-timed.** All eleven `data-start` / `data-duration` / `data-framings`
triples and the root `68.672` are identical to the file the reviewer saw:

```
s1  0      5.377  4.927      s7  36.931 5.038 4.588
s2  4.927  6.579  6.129      s8  41.518 9.923 4.6,4.873
s3  11.056 6.396  5.946      s9  50.991 6.344 5.894
s4  17.002 6.631  6.181      s10 56.885 8.617 8.167
s5  23.184 8.721  8.271      s11 65.051 3.621 3.621
s6  31.455 5.926  5.476
```

Tracks `1 2 1 2 1 2 1 2 1 2 1`, 11 `<audio>` rows, `assets/audio.json` unchanged
(`bed-resolve` + 4 cues at 1.1 / 12.156 / 57.985 / 66.151). `build.mjs`'s own read-back
assertions — start, duration, framings-sum, the 9.0 s single-framing cap, track alternation
and the 0.45 s overlap at every boundary — all passed on the rebuild; they are what makes
"do not re-time" checkable rather than promised.

**6 — snapshots: 17 frames, 2 batches, 2 directories, 17 looked at.**
- `snapshots/qa/rw-b1/` — **11 frames**, every scene at its last cue (`+1.8 s`, the
  `rise(stmt)` landing): 1.8, 6.727, 12.856, 18.802, 24.984, 33.255, 38.731, 43.318, 53.391,
  59.285, 66.851. Read as 2 contact sheets plus full-res reads of `frame-02` (s3) and
  `frame-10` (s11).
- `snapshots/qa/rw-b2/` — **6 frames** at the ken extremes and the true full-density chip
  frames: 11.2, 16.9, 53.79, 59.70, 65.2, 68.6. Read as 1 contact sheet.
- **A sampling error I made and corrected, not a build defect:** batch 1's s10 frame at
  59.285 s shows only 2 of 3 chips. `popEach(at, stagger, dur)` is 1.10 / 0.65 / 0.40, so the
  third chip *starts* at +2.40 and lands at +2.80 — 59.285 is the frame where it is still at
  opacity 0. Re-shot at 59.70 in batch 2: all three chips present. Max-density for a 3-chip
  row is `+2.80`, not `+1.8`; batch 1's time was the stmt ladder's.
- What the frames show: s3 at 12.856 s and 16.9 s — five numerals *and* five blocks fully in
  frame, the row reading `1 2 3 4 5` left to right, deep maroon under the locked grade as
  fin-assets predicted. s11 at 66.851 s and 68.6 s — the open door, both jambs, the sunlit
  tree and paving, `Step one.` in `fundc` legible against the mid-tone aperture; nothing like
  the near-black texture of attempt 1. s9/s10 centred, no empty band. `.stack` inside the
  safe area on all 11, nothing overflowing, watermark `cut-en` painted bottom-right on every
  frame including the dissolve frames at 11.2 s and 65.2 s.

**7 — `npm run check` (hyperframes 0.7.66, pinned via the committed lockfile): PASSED.**

```
Lint      0 errors, 2 warnings, 2 infos
Runtime   0 errors, 0 warnings
Layout    0 errors, 0 warnings, 21 infos
Motion    0 errors, 0 warnings
Contrast  12/12 text checks pass WCAG AA
```

`known_benign` is `[]` and stays `[]` — nothing was silenced and **no design token was
touched**. The 2 warnings are `timeline_track_too_dense` on tracks 1 and 6 elements / 2 and 5
elements; they are structural and pre-existing — 11 scenes alternating across two tracks is
exactly what the transition rule *requires*, and the suggested fix (split into
sub-compositions) contradicts `chapter_design.one_root_html`. The 21 layout infos are the
usual `container_overflow` on each `.bg` (that is what `inset:-8%` is for) plus `text_occluded`
/ `content_overlap` inside cross-dissolve windows, i.e. two scenes legitimately on screen at
once. Both categories were present on attempt 1's passing check.

## Changed

`studio/videos/financial-freedom-after-50-en-ch1/build.mjs` — the generator's SPEC table and
its comments. `index.html` and `assets/audio.json` are its regenerated output.

| # | scene | before | after | fix |
|---|---|---|---|---|
| 1 | s3 | `ken("#s3-bg", S.s3, 6.396, false)` — 1.16→1.00 with ±2.5 % pan | `plateKen("#s3-bg", S.s3, 6.396, 0.94, 0.87)` | blocker 1 — all five numerals hold frame for the whole 6.396 s, ≥76 px margin |
| 2 | s9 | `arch-d has-photo art-off` + `.brule` at 424 px | `+ centred`, no `brule` | blocker 3 — the reviewer's fallback |
| 2 | s10 | same | `+ centred`, no `brule` | blocker 3 |
| 3 | s11 | `ken("#s11-bg", S.s11, 3.621, false)` | `plateKen("#s11-bg", S.s11, 3.621, 1.08, 0.98)` | blocker 4 — the pan that could walk the aperture is gone; direction still alternates with s10 |

One generator addition, 2 lines: a SPEC row may carry `ken: [from, to]`, which emits a
`plateKen` over the scene's full on-screen length instead of the stock `ken`. It exists for
exactly these two scenes and is documented in place with the 0.8621 scale floor, so the next
chapter that has a subject which must not leave frame does not re-derive it.

Nothing else was touched: s1–s2, s4–s8 are unchanged, no scene lost `has-photo` or its `.bg`,
no rail, no chapter/scene counter, no drawn layer added — **chapter 1 is still 0 of 4**, as
storyboard §8 declares and as fin-assets' re-pick preserved. No file written to
`assets/icons/`; no icon was needed.

## Owed

1. **To fin-review — review finding 7 (`2 Maximize` → `2 Maximize savings`) was deliberately
   NOT taken.** It is 18 chars, inside `max_chip_chars` 22, and it would have cost one line.
   I left it because this pass was scoped to framing values and layout classes and a chip
   string is on-screen copy, and because the reviewer's own instruction was "not worth a
   render on its own / if the chip row is rebuilt" — the row was re-*positioned*, not rebuilt.
   If the next review still wants it, it is a one-word edit to `SPEC[8].chips[1]`.
2. **To fin-review — s11 is still a mostly-black frame**, by construction: the doorway is
   18.5 % of the photograph's width and no framing changes that without a 2.5× upscale
   (Failed). What changed is that the light is unambiguously a *door standing open onto a
   sunlit park* rather than an abstract texture, and the green verdict now reads against the
   aperture. If the closing frame is still judged too dark, the lever left is the photograph,
   not the ken.
3. **To whoever edits `build.mjs` next:** the chapter header comment is inside a template
   literal. A backtick in that prose is a syntax error, and the generator is the only thing
   that writes `index.html`.
4. **Not verified by me:** `pipeline_check check_build` is not on my allowlist, and no
   re-render was run — the draft mp4 and `SHEET-ch1.jpg` in `renders/` are still attempt 1's
   and will disagree with `index.html` until the orchestrator re-renders.
