# fin-build — en PRE-ASSEMBLY BATCH, attempt 1

Three projects touched: `passive-income-number-en-ch2`, `-ch4`, `-ch5`. ch1, ch3 and ch6 untouched.
All four items landed in one pass. `hyperframes check` PASSES in all three.

## Ran

- Read `vault/CLAUDE.md`, `tools/packs/fin-build.md`, `tools/format/fin-build.json` (`chapter_design`, `layout`,
  `known_benign`), and the two code homes the pack points at as authoritative:
  `tools/scaffold/assets/chapter-design.css` and `tools/scaffold/assets/js/motion.js`.
  **No knowledge-note body was opened** — nothing needed was missing from the pack, the CSS or the JSON,
  so there is no `OPENED-BODY:` line to report.
- Read the `owed.*` and `rulings_binding_on_both_cuts.*` entries in `notes.md` that govern this batch
  (`en_ch2_s10_tank_layer`, `en_preassembly_batch`, `..._GAINS_A_FOURTH_ITEM_2026-08-12`,
  `en_tank_becomes_a_drawn_layer_2026-08-10`, `s61_ratio_becomes_a_drawn_device...`).
- Edited `build.mjs` in each of the three projects and regenerated `index.html` with `node build.mjs`.
  No `index.html` was hand-edited — all three are generated files.
- `npx hyperframes snapshot` in four batches per project, **each into its own `-o` directory**
  (`snapshots/qa/pre1`, `b1`, `b2`, `b3`, `final`), never a shared one. No timeout retries were needed
  on this run — every invocation succeeded first time.
- `npm run check` in each project.
- **Frames actually looked at, not just captured:** ch2 25 captured → 5 opened as images
  (`pre1` 8.0s and 13.0s, `b1` 8.56s, `b2` 8.56s and 13.66s) and 6 measured numerically;
  ch4 10 captured → 3 opened (`pre1` 44.22s, `b1` 44.22s and 61.20s) and 7 measured;
  ch5 6 captured → 3 opened (`pre1` 27.80s, `b1` 56.50s, `final` 27.80s) and 6 measured.
  Every frame quoted below was measured on a rendered PNG, not computed from CSS.

## Failed

Nothing blocked. Four things went wrong mid-pass and were fixed inside it; they are recorded because
two of them are the kind that would otherwise ship:

1. **`brule: 400` struck through `#s10-sub`.** Inherited from s18, which has a two-element stack;
   s10's is three deep (kicker, a two-line 76px focal, the sub). The rule crossed the sub's glyphs on
   the first frame of the pass (`snapshots/qa/b1/frame-01-at-8.56s.png`). Same shape as the
   `.measure-lab` UA-margin bug the creator caught on the encode. Moved to 450 against a measured last
   baseline of y412; clears by 38px, still 154px above the vessel.
2. **The tank's first origin (x130) hung the vessel wall 20px left of the type column.** Moved to
   x150, which is both the type's left margin and s18's own bill-block edge in the same plate, so the
   chapter's two `p-d` mechanisms and the focal now hang off one line.
3. Two build-script self-inflicted syntax errors (unescaped `"` inside a double-quoted note string;
   unescaped backticks inside the html template literal). Caught by `node build.mjs`, fixed, no output
   was ever wrong.
4. `const ART_OP` was declared *after* the tank assert that calls `tank()` — TDZ error at build.
   Moved above it.

## Evidence

Method note first, because it decides everything below. **Contrast was measured on rendered PNGs, on the
same timestamp before and after, with the same ken position** — never computed pre-scrim, which is the
error that produced the original miss. The method was validated before it was trusted: run against ch5's
*shipping* frames it returned **s57 1.69:1** and **s61 2.15:1** against `fin-review`'s independently
measured **1.70:1** and **2.13:1**. Medians over a region; ΔRGB reported alongside because two of the
five layers are `--warn`/`--target` fills whose signal is chroma, not luminance.

### Item 1 — en ch2 s10, the tank is PLANTED (`owed.en_ch2_s10_tank_layer`)

- `studio/videos/passive-income-number-en-ch2/build.mjs`, `studio/videos/passive-income-number-en-ch2/index.html`.
- ch4's parameterised layer **copied, not redrawn**: `const TANK` + `function tank(id, o)` lifted from
  `../passive-income-number-en-ch4/build.mjs` with **one moved origin** (`x: 600 → 150`) and **one added
  option** (`stream: false`). ch5 already carries the same function with its own one option
  (`slice:false`) and its own moved origin, so the three sites now share one geometry and cannot drift
  into three different tanks.
- Scene spec: `art: "off", ctr: true` → `art: "tank", ctr: false, band: true, brule: 450`.
  `.centred` comes off because `.scene.centred .plate` is `display:none` — a centred scene structurally
  cannot hold a drawn layer. Same trade s14, s17, ch4's 4.7 and ch5's 5.5/5.9 all made.
- **Nothing timed moved.** `data-start="5.162"`, `data-duration="11.046"`,
  `data-framings="6.81,3.786"`, root `data-duration="105.518"` — byte-identical to the locked file.
  Same photograph, same two framings, same `plateKen` 1.00 → 1.06 → 1.16, same swap at +6.810.
- **Placement, measured not preferred.** ch4's x600 puts the vessel on the centre of *this* frame, where
  the photographed brass runs screen x950-1350 — a drawn tap over a photographed tap is rule 8's
  depictive failure. At x150 the mechanism is screen **x150-824 / y604-960**: over the copper trough,
  below the band's start, above the 970 bottom safe line, 948px clear of the watermark box
  (x1772-1856 / y956-1040). That region measures **p50 L 0.0097 / p90 0.0172** in framing 1 and
  **p50 0.0120 / p90 0.0169** in framing 2 — dark and flat in *both*, which a `data-framings` swap makes
  hard to get. ch4's own rect (x600-1297) measures no darker, so this is a subject decision, not a
  luminance one.
- **The level is decorative and asserts no quantity** (`no_return_promise`). ch4's assert came with the
  function and now runs in ch2 too: it strips comments first, then throws on `<text>`, on
  `tick|scale|gauge`, on `ghost|prev|before`, and on a missing `-lvlx`. A fourth clause was added here —
  it throws if a `-stream` rect is emitted, because **2.2 fills, it does not draw**.
- **The direction is the mirror of 4.7, and it is a state change, not a distance.** Same two rects; at
  4.7 the upper slice `exit`s, here it `fade`s IN. Nothing slides and nothing marks where the level was.
  Verified on frames at three times:

  | t | scene | vessel wall | upper slice `#s10-lvlx` | base water `#s10-lvl` |
  |---|---|---|---|---|
  | 6.66s | +1.50 | rgb 17 on gnd 16 — **absent** | absent (27 ≈ gnd) | absent |
  | 7.40s | +2.24 | rgb 84 — arrived | **still absent** (27 ≈ gnd) | rgb 50 — present |
  | 8.56s | +3.40 | rgb 84 | **rgb 53 — arrived** | rgb 50 |

- Cues, anchored on this scene's own already-measured word rather than a template offset: the file
  records "tank" at 1.960-2.140s into `2.2.mp3` = scene +2.21 to +2.39. Band at +1.10; the vessel's
  0.55s fade at +1.65 **completes at +2.20**, the instant the word arrives; the level's 0.70s rise runs
  +2.60 → +3.30, inside "slowly, over years". Assembled at +3.30.
- **No new sound.** `assets/audio.json` regenerated by `cues.py`: s10 still carries only its joint
  `transition` at 5.162 and its framing-swap `transition` at 11.972, exactly as before.
- Density is now **five drawn layers in a fifteen-scene chapter**, which is *above* the archetype note's
  stated top-of-range. Declared in the file rather than hidden, with the reason: the tank is a
  cut-level device planted once, not this chapter's fifth idea. §8's ch3-6 budgets are unchanged.

### Item 2 — en ch4 s49, the bars are NAMED

- `PAYOUT` / `PRICE` / `YIELD`, three `.measure-lab` labels in a column at x780, on the bars' own screen
  centres (600-680, 744-824, 864-944 → tops 629 / 773 / 893). They arrive with the art at +1.30.
- The fraction itself is **untouched** — same numerator, same 14px divisor rule, same ghost track, same
  halving denominator, same doubling quotient, same `FALL`/`RISE` constant and its assert. Still a
  fraction, still deliberately not three parallel bars.
- ⚠ **They live OUTSIDE the plate on purpose.** `.measure-lab` is z-index 2, i.e. *above* the scrim; a
  22px glyph authored inside the `.art` would have landed at exactly the contrast items 3 and 4 exist to
  escape, and glyphs are what does not survive there. Reuse of the system's own bar-label component, not
  a new one.
- Verified on frames: at 58.90s the label boxes max out at rgb (51,35,42) — background, labels absent;
  at 61.20s both read rgb (152,162,179), the full `.measure-lab` colour. The fix reads on the frame:
  the doubling bar is now captioned YIELD directly under «Smaller tank.»

### Item 3 — the silent no-op is fixed upstream, and it lands on ch4

- Confirmed the upstream state: `chapter-design.css` now has
  `.has-photo .art { opacity: var(--art-op, .30) !important }` + `.has-photo.art-forward .art { --art-op: .52 }`,
  and both chapter projects symlink `assets/chapter-design.css` to `tools/scaffold/`.
- ⚠ **The CSS fix is necessary but not sufficient, and this is the part worth carrying.** `fade()` in
  `motion.js` tweens `opacity`, and `opacity` is still `!important`, so **`fade("#sN-art")` is STILL a
  no-op after the fix.** What the fix buys is that a tween on `--art-op`, written on the `.art` element
  itself, now drives it. ch4 therefore needed a real edit, not just a rebuild.
- ch4's two calls became `artOp("#s46-art", …)` and `artOp("#s49-art", …)` — two lines of
  `tl.fromTo(sel, {"--art-op": 0}, {"--art-op": ART_OP, …})` declared in that composition's own script.
  **Not a redefinition of a system helper**: `motion.js` has nothing that writes a custom property. See
  Owed.
- Both layers now ARRIVE rather than standing from frame 0, measured at the same pixels:

  | scene | before its cue | at settle |
  |---|---|---|
  | s46 vessel wall | 41.80s — rgb 37 on gnd 38 (**absent**) | 44.22s — rgb 90 on gnd 31 |
  | s49 numerator | 58.90s — rgb 47 on its own gnd 45 (**absent**) | 61.20s — rgb 100 on gnd 45 |

- ch5 fades its child rects and is genuinely unaffected; ch6 fades no art. Confirmed by reading, not
  assumed: ch5's calls are `fade("#s57-art rect", …)` and `fade("#s61-art rect", …)`.

### Item 4 — the scrim eats drawn ink, so the resting opacity is lifted

**The knob is `--art-op` and the z-order was NOT touched.** `.plate` stays z-index 0, `.scrim` stays
z-index 1. One constant, `ART_OP = 0.74`, byte-identical in all three `build.mjs` files.
Applied as a tween end-value on ch4 (where it also does item 3's job) and as an inline
`style="--art-op:0.74"` on the `.art` element in ch2 and ch5 (whose children already fade).

Measured, same timestamp before and after, same ken:

| scene | element | at `.52` | at `.74` | ΔRGB `.52 → .74` |
|---|---|---|---|---|
| ch2 s10 fr.1 (8.56s) | vessel wall | 1.80:1 * | **2.48:1** (rgb 84 on 16) | 47.8 → 66.0 |
| ch2 s10 fr.2 (13.66s) | vessel wall | — | **2.49:1** (rgb 83 on 15) | — |
| ch2 s10 | floor rail | — | **2.08:1** (rgb 73 on 18) | — |
| ch4 s46 (44.22s) | vessel wall | **1.73:1** (rgb 72 on 31) | **2.27:1** (rgb 90 on 31) | 39.7 → 57.0 |
| ch4 s49 (61.20s) | numerator | 1.85:1 * | **2.36:1** (rgb 100 on 45) | 39.4 → 56.0 |
| ch5 s57 (27.80s) | vessel wall | **1.69:1** (rgb 75 on 37) | **2.18:1** (rgb 91 on 37) | 39.3 → 52.7 |
| ch5 s57 | floor rail | **1.60:1** | **2.06:1** | — |
| ch5 s61 (56.50s) | mark 3 vs wood | **2.15:1** (rgb 76 on 15) | **3.12:1** (rgb 100 on 15) | 61.0 → 86.8 |
| ch5 s61 | mark 1 vs the gap | **1.93:1** | **2.73:1** | — |

`*` = the two `.52` values marked with an asterisk are the only ones not separately rendered; they are
solved from that scene's own measured line (the layer is linear in `--art-op` in sRGB byte space, which
is where the browser composites). Every other number in the table is two rendered frames.

**ch5 s61 now clears WCAG 1.4.11's 3:1 for a non-text graphic. Nothing else can, and that is the finding.**
Solving the measured line for 3.0:1 on ch4 s46 needs `--art-op` **0.97**; for the design's own predicted
4.3:1 it needs **1.21** — more than fully opaque cream. The scrim floors the ground and ceilings the ink
at the same time (measured transmission through scrim + grain + field ≈ **38%**), so **the 4.3:1 and 5:1
figures in the s57 and s61 build notes are not reachable at any opacity**. They were computed pre-scrim;
that is exactly the error, and it is corrected in both notes rather than left to be re-derived.

**Why 0.74 and not more.** Both limits in the brief were measured, not asserted:

| | ch2 s10 | ch4 s46 | ch4 s49 | ch5 s57 | ch5 s61 |
|---|---|---|---|---|---|
| drawn ink, L | 0.089 | 0.087 | 0.110 | 0.086 | 0.120 |
| the frame's focal type, L | 0.427 | 0.229 | 0.229 | 0.229 | 0.229 |
| photograph p99 / p99.9, L | 0.026 / 0.145 | 0.042 / 0.174 | 0.044 / 0.161 | 0.057 / 0.144 | 0.077 / **0.358** |

The ink sits **between the photograph's own p99 and its p99.9 on every scene** — brighter than 99% of
the picture, dimmer than the picture's highlights — and never above 52% of the quietest type on the
frame (21% on ch2). Rule 9 never comes up: no photograph was darkened anywhere, the only darkening is
`.band` at z-index 0 *under* the plate, which ch2 s10 gained and ch4 already had.
For calibration: **ch6's rungs passed review on the encode at ΔRGB 38.8-40.7 — which is exactly where
`.52` was sitting on these five layers.** 0.74 is a real lift above a band already shown to survive an
encode, not a rescue. **ch6 was not touched.**

⚠ **Two of the five layers are chroma, not luminance, and a WCAG ratio badly undersells them.** ch4
s49's denominator reads rgb 86 against its own ghost track's 41 in the **red channel** and 35-vs-34 /
40-vs-39 in the other two; the quotient scores 1.32:1 on luminance and is plainly a solid bar on the
frame. ch2 s10's water is rgb 53 on 33 (+20 red, +13 green, −1 blue) and scores 1.19:1. Recorded in both
build files at the point of edit so nobody re-measures these as defects. **Judge a `--warn`/`--target`
fill on ΔRGB or on the frame, never on the ratio.**

⚠ **ch2's other four drawn layers (s14, s16, s17, s18) were deliberately NOT lifted.** They were
reviewed and locked on their own encode at `.52`, and re-lighting frames nobody complained about is not
what a pre-assembly pass is for. Declared in that file's header.

### What did not move, verified

- No `data-start`, `data-duration` or `data-framings` changed in any of the three projects; the three
  root durations are unchanged (ch2 105.518, ch4 87.279, ch5 unchanged). Every one is still generated
  from `timing.json` by the build script — nothing was hand-typed.
- No image swapped, no `.src`, `manifest.json` or `CREDITS.txt` touched.
- No rail anywhere. Every scene keeps `has-photo` and a real full-bleed `.bg`.
- ch5's settled results are untouched: s59 PEAK 2, the s54 floor discharge, s63/s68 comma clearance —
  none of those scenes was opened.
- The only `.centred` change is ch2 s10, which item 1 requires (a centred scene `display:none`s its own
  plate).

### `npm run check`

| project | result |
|---|---|
| `passive-income-number-en-ch2` | **Check passed** — 0 lint errors, 4 warnings, 0 runtime, 0 layout errors, 11/11 contrast AA |
| `passive-income-number-en-ch4` | **Check passed** — 0 lint errors, 4 warnings, 0 runtime, 0 layout errors, 15/15 contrast AA |
| `passive-income-number-en-ch5` | **Check passed** — 0 lint errors, 4 warnings, 0 runtime, 0 layout errors, 14/14 contrast AA |

The four warnings are identical in all three and all pre-existing: `composition_file_too_large`, two
`timeline_track_too_dense`, and `composition_heavy_overlay_count_high`. **No design token was edited to
satisfy any checker**, and `known_benign` is still `[]`.

### Total composition durations

| project | root `data-duration` | chapter offset |
|---|---|---|
| en ch2 | **105.518s** | 46.420s |
| en ch4 | **87.279s** | 248.539s |
| en ch5 | unchanged by this pass | — |

## Changed

**`studio/videos/passive-income-number-en-ch2/build.mjs`** → regenerates `index.html`
- New `const ART_OP = 0.74`, `const TANK`, `function tank(id, o)` and the four-absence assert (ch4's,
  plus a fifth clause forbidding a stream rect).
- `ART` dispatch gains `tank: (id) => tank(id, { stream: false })`.
- s10 spec: `art: "off" → "tank"`, `ctr: true → false`, `+ band: true`, `+ brule: 450`.
- Three new cues for s10; the drawn-layer header rewritten (four → five, with the density declaration).
- s10's note extended with the ruling, the ordering argument, the measured frames and the `.centred` trade.

**`studio/videos/passive-income-number-en-ch4/build.mjs`** → regenerates `index.html`
- New `const ART_OP = 0.74` with the full measurement and the unreachability finding.
- New `artOp()` in the composition's own script; `fade("#s46-art")` and `fade("#s49-art")` replaced by it.
- s49 spec gains `artlab: [["PAYOUT",780,629],["PRICE",780,773],["YIELD",780,893]]`; `scene()` gains a
  five-line emitter for it; one new `fade()` for the three labels.
- s46 and s49 notes extended with the no-op story and the before/after numbers.

**`studio/videos/passive-income-number-en-ch5/build.mjs`** → regenerates `index.html`
- New `const ART_OP = 0.74`; `style="--art-op:${ART_OP}"` on the `v-tank` and `v-marks` `<svg>` tags.
- s57 and s61 notes extended with the measured before/after and a correction of their own pre-scrim
  predictions.

Snapshots written: `…-en-ch2/snapshots/qa/{pre1,b1,b2,b3}`, `…-en-ch4/snapshots/qa/{pre1,b1,final}`,
`…-en-ch5/snapshots/qa/{pre1,b1,final}`. Nothing was written to `assets/icons/`, `tools/` or `.claude/`.

## Owed

1. **`motion.js` has no helper that tweens a CSS custom property, and after the `--art-op` fix that is
   the ONLY way to make a drawn layer arrive on a `.has-photo` scene without fading its children.**
   ch4 now carries a two-line `artOp()` in its own composition. That is the documented fallback (name
   the gap, use the nearest thing) but it is a system gap, not a chapter's business: the next chapter
   that draws will re-derive it or, worse, call `fade("#sN-art")` and ship a silent no-op again.
   Proposed correct default (`fix-defaults-not-gates`, top rung): give `motion.js` an `artOp(sel, at,
   dur, to)` — or better, make `fade()` detect a `.art` target on a `.has-photo` scene and drive
   `--art-op` instead of `opacity`, which makes the wrong call unrepresentable rather than merely
   documented. I may not write `tools/`, so it is routed here.
2. **The z-order compensation is now measured and should be written down where the next build reads it.**
   `chapter-design.css:96` says "Opacity 26-58%: below that the scrim and grain eat it in" — true, but
   it does not say the transmission is **~38%**, nor that a pre-scrim contrast target of 3:1 or above is
   unreachable at any opacity. Every one of the five layers in this batch was authored against a
   pre-scrim prediction and every one missed by roughly 2×. That sentence should carry the number.
3. **`.52` is now the odd one out.** Five layers ship at 0.74 and ch2's other four, plus every layer in
   ch1/ch3/ch6, ship at `.art-forward`'s `.52`. That is deliberate for this pass (locked frames,
   reviewed on their own encodes) but it is a split the next video should not inherit — either `.52` is
   the right resting value or it is not, and this run now has nine measurements that say what it buys.
4. **Item 4 as listed in `notes.md` — `owed.overlay_count_in_the_assembled_master` — is NOT discharged
   here; it is the orchestrator's call and I did not make it.** The arithmetic it needs, measured on the
   shipping files today: **en ch2 = 30, en ch4 = 26, en ch5 = 32** heavy overlays.
   ⚠ The note records ch5 at **34**; it is **32** on the current file, so the note's figure is stale
   (ch5 was rebuilt after that count for the s61 photo swap). This pass added **zero** heavy overlays —
   s10's new `.band` is a linear-gradient and its `.plate` carries neither blur, radial-gradient nor
   clip-path, so ch2 is still exactly the 15 `.scrim` + 15 `.glow` the note describes.
5. **`fin-review` will want the encode, not these frames.** Every number above is a `snapshot` PNG.
   Seven-for-seven on this run, a predicted rank has been a shortlist and never a verdict — the two
   things most likely to move are ch2 s10's amber water (a chroma edge on a warm ground) and ch4 s49's
   two `--warn` bars, for the same reason.
