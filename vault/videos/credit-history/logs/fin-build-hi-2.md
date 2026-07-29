---
summary: Gate ④ rebuild for credit-history hi — s7's car-fob cut-in deleted as fin-render prescribed, so the blueprint `.bg` carries "SAME HOUSE. DIFFERENT NUMBER." alone. npm run check passes (0 errors, 22/22 contrast), duration unchanged at 177.642s; 4 dead cut-in files removed. One correction to fin-render's prediction: the blueprint plate is slightly BRIGHTER than the cropped key photo, so #s7q's contrast fell rather than rose.
updated: 2026-07-29
source: own edit of studio/videos/credit-history-hi/build.mjs + snapshots/qa4/ (10 frames) · prescription in logs/fin-render-hi-1.md · [[../../../knowledge/design-finance-blockframe]] §1
---

# fin-build — credit-history · hi · attempt 2 (hard-gate fix pass)

**Result: `npm run check` PASSED.** 0 errors · 2 warnings · 1 info ·
Runtime 0/0 · Layout 0 issues / 9 samples · Motion 0/0 · **Contrast 22/22 WCAG AA**.
**Total composition duration: 177.642s** — unchanged, still exactly `timing.json total`.
Findings are the same three as attempt 1 (file size, track density, `.grain`
pointer-events); **no new finding**, and no design token was touched.

## The fix — exactly the prescription, in the generator

`index.html` is generated, so all three deletions are in `build.mjs`:

1. `s7: ["s7cut:s7-cut.jpg"]` removed from the `CUTS` map → the `#s7cut` div is
   no longer emitted.
2. `#s7cut { background-position: 22% center; }` + its comment removed (the
   attempt-1 crop that treated the symptom).
3. `fade("#s7cut", …)` and `ken("#s7cut", …)` removed.

`node build.mjs` regenerated `index.html`; **0 occurrences of `s7cut` / `s7-cut`
remain** in either file. A one-line comment now sits on the `CUTS` map recording
why s7 has no cut-in, so the next editor does not re-add one unlooked-at.

s7 keeps its full-bleed `#s7 .bg` (`s7.jpg`, blueprint) with `ken` running the
whole scene — `photo_free_scene_ratio` stays **0** and no static hold appears
(the deleted cut-in was a plate swap, never the only motion).

## Timing — untouched, re-verified from `timing.json`

All four homes regenerated and compared programmatically: 9 `<section>`
`data-start`/`data-duration`, the JS `S` map, the 9 `<audio>` `data-start`s, and
the root `data-duration`. Every scene butt-joins the next; root = last scene end =
`timing.json total` = **177.642**. No hand-typed number.

## Dead assets removed

`s3-cut.jpg`, `s4-cut.jpg`, `s6-cut.jpg` (dropped at the asset stage) and
`s7-cut.jpg`, plus their four `.src` sidecars — 8 files. `s7-cut.jpg` was also
dropped from `assets/img/manifest.json`; `pipeline_check.check_assets` fails on a
manifest name that is not on disk, so the manifest and the disk had to move
together. Cross-checked after: index.html references 14 image files, all present;
manifest holds no unreferenced name; no reference points at a missing file.
**`CREDITS.txt` was left alone** — it is fin-assets' append-only search log and
already carries rows for candidates that never shipped; the check only walks
manifest → credits, never credits → disk.

## Max-density snapshot pass — `snapshots/qa4/`

Ten frames: the nine last-cue times plus **137.50** (where the fob used to fade in).

- **s7 @ 137.50 and 139.05** — blueprint under both. The punch reads over
  drafting lines and the "580" dimension; no vehicle object anywhere in the scene.
- **Safe area** — s7's red elements (billrow panel + border + the 88px punch) span
  **x 460→1459, y 329→671**, inside the 192→1728 / 108→972 title-safe box. Layout
  is byte-for-byte what fin-render measured; the cut-in was never in the `.stack`.
- **The other eight frames are unchanged.** Six are byte-identical to fin-render's
  own PNGs; the 28.8 and 175.4 pairs differ by a **max channel delta of 1 and 2**
  (rasteriser noise, 0 pixels differing by >8). Nothing regressed, and the build
  re-renders deterministically across runs.

## Correction — the blueprint is not the darker plate

fin-render expected `#s7q`'s contrast to rise once the key photo went. **It fell.**
Measured on my own PNGs with sharp, identical method on both frames — WCAG 2.x
relative luminance of the non-glyph pixels inside the punch's box, counting only
windows that actually sit under type:

| Frame | backdrop under glyphs (mean) | worst 48px glyph-bearing window |
|---|---|---|
| attempt 1 (car key, cropped 22%) | 46,36,37 → **4.01** | 67,59,62 → **2.89** |
| attempt 2 (blueprint) | 59,48,52 → **3.35** | 79,67,70 → **2.51** |

The key photo's left two-thirds happened to be darker than the blueprint's paper.
`s7.jpg` is bright and even — a 9×5 tile map reads ~200/255 nearly everywhere, the
only dark patch being the pen at the right edge, so **reframing cannot help**.

**Nothing legal moves this number, and I did not fake it:**

- lightening/darkening `--warn` is a token edit — forbidden, and red is this
  video's thesis (same reasoning that fixed `#s5ctr` structurally in attempt 1);
- a second per-scene `filter:` override is forbidden by design §1 — *"permitted
  only for a near-black texture the grade crushes flat, and never more than once
  per video"*, and s8 already holds that one;
- the photo has no darker region to frame into.

The remaining lever is a different s7 photo, which is fin-assets' call, not this
stage's. Standing evidence that it is not a defect: `hyperframes check` scores
**22/22 AA** with its own sampler, `.huge` carries
`text-shadow: 0 2px 22px rgba(0,0,0,.7), 0 1px 4px rgba(0,0,0,.55)` that the
formula cannot see, and fin-render already declined to gate this element at 2.66.
**Flagging it rather than burying it — the subject defect is fixed; this number is
the honest cost.**

## Sign-off

- [x] `#s7cut` div, `fade`, `ken` and the `background-position` rule all gone; 0 refs left
- [x] `npm run check` passes — 0 errors, 22/22 contrast, 0 layout, 0 motion, no new finding
- [x] Duration exactly 177.642s; four timing copies regenerated from `timing.json` and verified equal
- [x] 8 dead files removed + manifest kept consistent; every referenced asset on disk
- [x] Snapshot pass re-run (10 frames); s7 safe-area measured; other 8 frames proven unchanged
- [x] No design token edited; `--warn` untouched
- [ ] Render (fin-render's stage — gate ② re-run)
