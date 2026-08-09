# fin-build · passive-income-number · en · chapter 3 · attempt 4

Single-blocker fix pass: `editor-en-ch3-2` finding 1, the `.art-lift` panel on s30 (3.7).
Nothing else in the chapter was opened.

## Ran

- Read `vault/CLAUDE.md`, `editor-en-ch3-2.md`, `tools/format/fin-build.json chapter_design` +
  `known_benign`, and `design-chapter-archetypes.md` (BOX, §"The plate — the load-bearing
  idea", §"What a drawn layer has to look like to survive the encode", §"The gotchas that
  cost renders").
- Grepped the three `art-lift` users the editor named and confirmed the class lives in
  **`tools/scaffold/assets/chapter-design.css`**, reached from every project by SYMLINK
  (`assets/chapter-design.css -> ../../../../tools/scaffold/assets/chapter-design.css`,
  identical md5 `0beda639…` in all ten `passive-income-number-*` projects).
- Baseline snapshot batch `snapshots/qa/r3-base` (3 frames, t=39.0 / 41.0 / 42.9) —
  reproduced the editor's measurement on my own chain before changing anything.
- Wrote a temporary sharp-based measuring harness (edge profiles + bar-band RGB),
  used it on 8 frames, deleted it. Sample rects are stated below so any pass can redo it.
- Fix batch `snapshots/qa/r4b1` (3 frames, same three times).
- ch2 batch `snapshots/qa/r4-ch2s16` (2 frames, t=52.8 / 54.8, `snapshot
  ../passive-income-number-en-ch2 -o snapshots/qa/r4-ch2s16` — output written into THIS
  cut so nothing is created inside ch2).
- `node build.mjs`, `npm run check`.
- **8 frames captured across 3 batches, 6 opened and looked at** (r3-base@41.0;
  r4b1@39.0, 41.0, 42.9; r4-ch2s16@54.8; plus r3-base@39.0 as the before/after pair).
  The other 2 were measured numerically only. One `-o` directory per batch, never reused.
- Snapshot CLI needed no retries this pass (3 invocations, 3 successes).

## Failed

- **The editor's constraint 1 is wrong on the measurement, and that is the finding of
  this pass.** It predicted a feather would be a **no-op over ch2 s16's dark ground**.
  It is not. Measured on `snapshots/qa/r4-ch2s16` at t=54.8, the same three edges of the
  same `.p-b` rect:

  | edge | ch3 s30 (before fix) | **ch2 s16 (untouched)** |
  |---|---|---|
  | left, across x=1120 | 14.60 luma | **13.55 luma** (15.11 at t=52.8) |
  | top, across y=150 | 10.63 | **8.42** |
  | bottom, across y=760 | −5.13 | **−7.02** |

  s16's panel edge is the same order of magnitude as s30's — the ground under it is not
  dark, it is a pale birch/paper still. What differs is **occupancy, not luminance**: s16's
  `survival-grid` fills plate-local x 16–84%, y 1.5–98.5%, so the panel reads as the grid's
  backing panel. s30's bar+tick fill x 8–92% but only y 34.6–65.4%, so ~65% of the box is
  empty. A feather shaped to s30's content (plateau y 34–66%) would strip the lift from
  s16's top and bottom grid rows. **s16 would move.** Per the editor's own fallback branch,
  the softening is therefore scoped to `#s30-pin`.
- Independently, this stage may not write `tools/`, so the class-level edit was not
  available to it in any case. Both roads lead to the same scope; the measurement is what
  makes the scoping correct rather than merely permitted. See **Owed**.
- No other failure. `bgpos` was not touched (constraint 2), the photograph was not
  re-fetched (constraint 3), s34 was not opened.

## Evidence

All numbers from 1920×1080 PNG snapshots of this project, sRGB luma `0.2126R+0.7152G+0.0722B`.
Sample rects, so this is re-derivable: left edge = mean of x1108–1118 minus mean of x1122–1132,
both over y170–740; top = y138–148 minus y152–162 over x1140–1900; bottom = y748–758 minus
y762–772 over x1140–1900; fill = x1200–1415 / y405–505; ghost = x1445–1900 / y405–505.

**s30 panel edges — the blocker, before → after** (`snapshots/qa/r3-base` → `snapshots/qa/r4b1`):

| | t=39.0 | t=41.0 | t=42.9 |
|---|---|---|---|
| left step x=1120 | — → **0.39** | 14.60 → **0.26** | — → **0.24** |
| top step y=150 | — → **−0.39** | 10.63 → **−1.36** | — → **0.38** |
| bottom step y=760 | — → **2.67** | −5.13 → **1.96** | — → **1.30** |

The residual 1–2.7 at y=760 is the photograph's own vertical falloff across a 14px window,
not an edge: the raw profile at t=41.0 runs `37.7 37.0 37.2 36.9 37.1 36.3 36.4 | 35.6 35.7
34.7 35.0 34.8 34.9 34.0` — monotone, no discontinuity. Before the fix the same profile ran
`30.2 29.4 … 29.3 | 35.6 35.7 …`, a 5-luma jump across one pixel. Left edge before:
`…51.5 52.3 | 36.9 37.4…`; after: `…51.5 52.3 | 51.7 52.0…` — continuous.

**The drawn layer survives the feather and reads slightly better** (t=41.0):

| | before | after |
|---|---|---|
| fill RGB / L | (86.9, 64.0, 25.2) / 66.1 | (85.8, 63.0, 24.4) / **65.1** |
| ghost RGB / L | (62.2, 60.2, 59.2) / 60.5 | (59.3, 57.8, 57.2) / **58.1** |
| fill−ghost hue sep (R) | +24.7 | **+26.5** |
| fill−ghost luma gap | 5.6 | **7.0** |
| ground above bar (y300–380) | 31.6 | **31.2** |
| ground left of bar (x1130–1185) | 39.8 | 46.6 |

The plateau holds the lift where the art is (ground above the bar moves 0.4 luma); the only
region that brightens is x1130–1185, i.e. the 70px strip left of the bar that is inside the
horizontal ramp and carries nothing drawn. That is the trade, and it is the right one.

**Geometry the fix is built on** (plate `.p-b` = 1120,150,860,610; art viewBox 800×610 under
`meet`, so 1:1 with a 30px x-offset):
- bar `art x40–760, y245–365` → plate-local x70–790, y245–365
- tick `art x270.48–280.48, y211–399` → plate-local x300–310, y211–399
- ⇒ everything drawn lives in x 8.1–91.9%, y 34.6–65.4%. Plateau set to x ≥ 8%, y 34–66%.
- The plate's RIGHT edge is at x=1980 on a 1920 frame — off-canvas, no feather needed. This
  is the same declared geometry `check` reports as `container_overflow #s30-plate right 60px`
  and the same rect the editor's note 3 ruled not to move.
- Falloff budget: 211px above the tick, 207px below, 70px to its left — the empty 80% of the
  box the editor counted is exactly what the feather spends.

**Implementation** (`build.mjs` inline `<style>`, emitted to `index.html`):
`#s30-pin { background: none }` + a `#s30-pin::before` carrying a 12-stop vertical
`linear-gradient` (0 → .62 → 0, smoothstep-approximating stops) masked by an 8-stop
horizontal `mask-image` (0 → 1 over 0–8%). Two decisions worth recording:
- **`::before`, not the element.** A `mask-image` on `#s30-pin` masks its CHILDREN — the bar
  would fade at its own left end and misreport where the fill starts (the fill's left edge IS
  the zero of the proportion). The pseudo-element is first in DOM order with `z-index:auto`,
  so it paints under `.hatch` and `.art` without a stacking declaration.
- **Eased stops, not linear.** A linear ramp leaves a first-derivative kink at each end that
  reads as a faint Mach line on a flat sky — the same failure in softer form.
- `#s30-pin` carries no `plateKen` (only `ken("#s30-bg", …)`), so this layer is static and
  cannot drift under motion.

**Regression surface is provably nil.** `git diff` on `index.html`: **one hunk at line 70,
inside `<style>`, 53 lines added, 0 removed.** Every scene element, `data-start`,
`data-duration`, `data-framings`, `data-track-index`, the `S`/`D` maps, the 16 `<audio>` rows,
`assets/audio.json` (24 cues) and all JS are byte-identical to the reviewed encode. That
covers everything the editor verified clean: the 0.334 fill / 275.48 tick / BLS CE 2024
33.4% of $78,535, s27 `$332,950`, s31 `$656,650`, both Trinity quotes, s39's bare 3.543s tail,
s26's `brule` and four chip anchors. `node build.mjs` re-asserted its own timing block
(root 96.601s, offset 151.938s, 16 scenes) on the way through.

**ch2 s16 did not move.** Three independent proofs:
1. `tools/scaffold/assets/chapter-design.css` md5 `0beda63925497ae471220f89039d7bcc` —
   identical before and after this pass; `blockframe.css` `b17fdc01…` likewise.
2. `passive-income-number-en-ch2/index.html` md5 `91fb45d6a2f9a28f7c41373a36dfe9bd`,
   untouched; `git status` shows no modification under `videos/passive-income-number-en-ch2`.
3. The new rule is keyed on `#s30-pin`, an id that exists only in this chapter.
   Re-sheeted anyway (`snapshots/qa/r4-ch2s16`, 2 frames): s16 renders with its panel exactly
   as reviewed, 95 amber cells of 100, five ghosts, focal `95%` and the Trinity foot intact.

**`npm run check`: passed.** 0 errors. 4 warnings, all four pre-existing and structural, none
new: `composition_file_too_large` (556 lines), `timeline_track_too_dense` ×2 (8 clips on each
of tracks 1 and 2 — 16 scenes alternating, which is the required pattern),
`composition_heavy_overlay_count_high` (32 — unchanged, the new rule uses `linear-gradient`
only, no blur / radial-gradient / clip-path). Runtime 0/0, Motion 0/0, **Contrast 14/14 AA**.
10 layout infos, all `container_overflow` on `.bg` elements under ken plus the declared
`#s30-plate right 60px`. `known_benign` is `[]` and stayed `[]`; no token was edited.

**Composition duration: 96.601s** (root `data-duration`), 16 scenes, s24–s39, chapter offset
151.938s. Unchanged from attempt 3.

## Changed

- `studio/videos/passive-income-number-en-ch3/build.mjs` — +57 lines in the inline `<style>`
  block: the `#s30-pin` / `#s30-pin::before` feather and its rationale, including the
  plate-space arithmetic and the pointer to where the rule really belongs.
- `studio/videos/passive-income-number-en-ch3/index.html` — regenerated; +53 / −0, one hunk.
- `snapshots/qa/r3-base`, `snapshots/qa/r4b1`, `snapshots/qa/r4-ch2s16` — 8 frames.
- Nothing else. No asset, no timing, no token, no file outside this cut, no `assets/icons/`
  addition (none was needed).

## Owed

1. **Promote the feather to `tools/scaffold/assets/chapter-design.css` — but not this
   version.** `.art-lift` has three users and two of them (en-ch2 s16, hi-ch3 s28) have a
   drawn layer that fills most of the plate, while s30's fills a third of it. A class-level
   rule must be **content-agnostic** — a fixed inset feather (~48px on left/top/bottom, none
   on the right where `.p-b` is off-canvas) — which would kill the hard line on all three
   without gutting a full-height mechanism. It would NOT, on its own, fix s30, whose second
   defect is the empty 65% of the box; s30 keeps its scoped plateau on top. This stage cannot
   write `tools/`, so the scaffold edit is a deliberate one for the creator or a stage that
   may.
2. **`hi-ch3` s28 still ships the hard-edged panel.** Measured here only by inference (same
   class, same `.p-b` rect, `art-lift` plus an inner `#s28-band`); it has not been snapshotted.
   Whoever builds or fixes hi-ch3 next should run the same three-edge measurement before its
   editor pass, because the ground there is a specular brass balance — bright, and the same
   trap. It is NOT fixed by this pass.
3. **The editor's "over a dark ground a feather is a no-op" heuristic should not be reused.**
   The variable that decides whether an `.art-lift` panel reads as a card is how much of the
   plate the drawn layer OCCUPIES, not how dark the still is. s16 and s30 have the same edge
   step and opposite verdicts. Worth a line in `design-chapter-archetypes.md` §"What a drawn
   layer has to look like" if it survives another chapter.
4. s34 untouched by instruction (editor: "no action required this attempt"); its should-fix
   stands for whoever next opens the photograph pool.
