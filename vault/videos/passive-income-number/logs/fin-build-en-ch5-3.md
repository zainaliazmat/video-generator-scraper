# fin-build — passive-income-number · en · chapter 5 · attempt 3

## Ran

- Read `vault/CLAUDE.md`, `tools/packs/fin-build.md` (BOX + both body sections), `tools/format/fin-build.json`
  (`layout`, `chapter_design.archetypes`, `known_benign`), and the two rulings this pass exists for in
  `notes.md`: `rulings_binding_on_both_cuts.s61_ratio_becomes_a_drawn_device_over_a_consenting_photograph_2026-08-12`
  and `en_tank_becomes_a_drawn_layer_2026-08-10` + `chapters._carry_forward_en_ch4_to_ch5_s57`.
  No knowledge-note body was opened — nothing was needed that the pack, the CSS or fin-build.json did not answer.
- Read the shipping tank layer at source: `studio/videos/passive-income-number-en-ch4/build.mjs`
  (`TANK` + `tank()`), and `.../en-ch4/index.html` `svg.art.v-tank#s46-art` to confirm what actually renders.
- Read both photographs at full resolution (`assets-ch5/final/s61.jpg`, `s57.jpg`) and measured their geometry
  and tone with ffmpeg + node before placing anything.
- Measured word onsets for 5.5 and 5.9 with faster-whisper (`base.en`, word timestamps).
- Measured focal string widths with fontTools on the shipped `NotoSansFinance-var.woff2` at wght 900.
- Edited `build.mjs` only (the composition is generated); rebuilt with `node build.mjs` (which re-derives
  `assets/audio.json` through `tools/audio/cues.py`), then `npm run check`, then four snapshot batches.
- Did **not** touch `studio/videos/passive-income-number-en-ch6/` (fin-assets re-fetch in flight).

## Failed

- **One real defect found by my own snapshot pass, mid-build, and fixed:** `fade("#sN-art", …)` on the `<svg>`
  is a **silent no-op**. `chapter-design.css:259` sets `.has-photo.art-forward .art { opacity: .52 !important }`,
  so GSAP's inline opacity never reaches the screen and the drawn layer stands there from the scene's first
  frame with `hyperframes check` green. Caught at `snapshots/qa3/b3` frame `53.30s`, where s61's five marks were
  already fully up **1.70s before their own cue** and while s60 was still cross-dissolving out. Fixed by
  targeting the child rects (`fade("#s61-art rect", …)`, `fade("#s57-art rect", …)`) — the rects carry no
  `!important`, and their `fill-opacity` is a separate property, so element opacity is free to run 0→1.
  Re-verified at `snapshots/qa3/b4`: 53.30s no marks · 55.00s (+2.00, cue) nothing yet · 55.60s (+2.60) fully up.
  ⚠ **en ch4's s46 carries the same no-op** (`fade("#s46-art", …)`) — its tank is up from the scene's first
  frame; its `.band` fade and its stream `span` still animate, so the scene is not broken, only un-staged.
  Not patched here: ch4 is locked and this is a one-line change to that build's own template. **Owed upward.**
- Two `SyntaxError`s of my own making while writing template-literal comments (backticks inside the emitted
  HTML template). Caught by `node build.mjs`, fixed, no artefact shipped in that state.
- Nothing else failed. `npm run check`: **0 errors, 4 warnings, 2 infos · Runtime 0/0 · Layout 0 errors
  (9 `container_overflow` infos, all `#sN-bg` under `.bg`'s inset -8%) · Motion 0/0 · Contrast 14/14 WCAG AA.**
  The four warnings are the standing family for this cut (file length, track density ×2, and
  `composition_heavy_overlay_count_high` at **32** elements — unchanged by this pass, still
  `owed.overlay_count_in_the_assembled_master`). `known_benign` is `[]` and stays `[]`; no token was edited.

## Evidence

### 1 · s61 (5.9) — the ratio becomes a drawn device over the new photograph

**The photograph, read at full resolution — and it is not quite its own caption.**
`assets-ch5/final/s61.jpg`, 1880×1253, credited `pexels.com/photo/white-raw-eggs-in-bowl-on-table-4488336/`
(Mateusz Dach, Pexels License, CREDITS.txt line 18). The `.src` query reads *"four eggs in a bowl and one egg
beside it on a dark table"*. **What ships is five eggs ALL INSIDE the bowl** — four in a ring plus one lying
across them, whitest and plainly on top. The cardinality the ruling turns on is intact (four grouped + one
distinct = five) and so is its recorded weakness (correct ratio, **no separation**), so nobody re-searched;
but it is *not* four-beside-one on a table, and §10 / the ruling's own wording should say so.

**Measured geometry (why the marks are where they are).** Thresholded column/row profile of the source:
the bowl runs **source x 260–1430 / y 110–1223**. Through `.bg`'s `inset:-8%` box (2227×1253) `cover` is
width-limited at scale **1.1847** with a −153.6px x-origin, so at ken 1.0 the bowl covers **screen x 154–1541
and the full frame height** — the frame has no clear horizontal channel, only two wood crescents.
`ken(…, false)` runs scale 1.16→1.00 with xPercent +2.5→−2.5, so the bowl's right edge sweeps
**1618 (at the marks' entrance, +2.50s) → 1483 (scene end)**.
The column sits at **screen x1680–1736**: 55px clear of the eggs at the worst instant, ~200px by the end,
184px inside the frame edge (the 150px scene padding is the reference), and clear of the watermark box
(x1772–1856 / y956–1040). Vertically **y240–688**, i.e. plate `vy 90–538` of a 610-tall rect.

**Measured ground (why there is no band and no darkening).** The marks' own region, source x1477–1642 /
y422–734: **src p10 2 / median 9 / p90 27 → graded p10 0 / median 0 / p90 11** (grade = grayscale .32,
brightness .62, contrast 1.05). Cream ink at `.art-forward`'s .52 lands ≈127 against ≈5 → **≈5.0:1**.
Rule 9 never comes up: the photograph is not darkened anywhere and a `.band` would have darkened the bottom
of a frame to solve a problem that does not exist. The generator now demands a `.band` **or** a measured
`darkGround` string per drawn scene, so the exemption is in the file, not in a build's head.

**The device.** Five identical 56×56 squares in one column, four at 24px spacing, the fifth **96px apart**,
authored in the **p-b plate's own space** (`viewBox 0 0 860 610` → screen +1120/+150; gotcha 8's vx>800 cliff
is 240px away). It states a COUNT only: **no scale, no ticks, no numerals, no axis, no track, no baseline**,
and every element is the same size — a build assert throws if the five ever stop being identical, because an
unequal mark states a magnitude. It is **not** §9a's measure bar (§10 rules that off this frame).
**Squares, not discs, on purpose:** over a photograph of eggs a disc is a drawing of an egg — rule 8's
depictive failure; a square can only be a mark.
`no_return_promise`: «roughly four times» is an audited figure already in the locked VO; the device restates a
sourced comparison and forecasts nothing.

**Layout cost, measured, not estimated.** A drawn layer needs the plate and `.scene.centred .plate` is
`display:none`, so `.centred` came off (the same trade ch4's 4.7 made). The focal therefore moves into
archetype B's left column, where `.arch-b .huge` caps at 900px. fontTools on the shipped face at wght 900,
`.huge` letter-spacing −2px: `ROUGHLY 4 TIMES` = **1001.9px** (reproduces the build's own 1002 table entry),
so it is **hard-broken as ROUGHLY (544.1) / 4 TIMES (430.6)** rather than left to wrap greedily into
ROUGHLY 4 (634.8) / TIMES (339.9). **Type size is untouched at 112** — nothing was shrunk to fit.
Foot lines 714 / 770 both clear the 900 cap. Motion: **one** `fade` at +2.00 (complete +2.60, the contact
sheet's own sample time), 1.95s before the figure lands on its unchanged +4.55 anchor — the photograph keeps
the scene's only real motion (the ken).

### 2 · s57 (5.5) — ch4's tank layer applied, not a second tank drawn

`TANK` + `tank()` copied from `../passive-income-number-en-ch4/build.mjs` with **one added option and one
moved origin**, so the two sites cannot drift into two different tanks.

- **`slice:false`** — the water is ONE rect at the level 4.7's `exit` already left it on. No upper slice,
  therefore no second drop, **no ghost of a previous level, no tick, no scale, no numeral**; a build assert
  strips comments and then greps the emitted markup for all four. The level does not move at all.
- **The one state change is the tap CLOSING**: `span("#s57-stream", +3.67, 0.70, 2.4 → 1.0)` — the exact
  reverse of 4.7's widening, same rect, same **measured** `transform-origin:0% 50%` (ch4 caught the 50%/0%
  form rendering ~860px left of its own x). Verified on frames: `b4/26.92s` wide → `b4/29.59s` narrow.
- **Origin 600 → 1000, measured.** The photographed bucket occupies **screen x166–889** (source x260–880
  through cover). At ch4's x600 the drawn vessel would have been drawn *on* it. At x1000 the mechanism runs
  **screen x1000–1674 / y604–960**: clear of the bucket, above the 970 bottom safe line, left of the 1770
  right safe edge and left of the watermark box.
- **Ground measured, band justified:** that region of the source is the whitewashed wall — src median 128 →
  **graded 77**, the light-on-light case rule 9 forbids fixing on the photograph. The `.band` at `z-index:0`
  **under** the plate darkens behind the mechanism only (alpha .22 at y604 → .63 at y960), taking the ground
  to ≈50 against cream at .52 → **≈4.3:1**.
- **Anchors measured** on `5.5.mp3` (+0.25 lead-in): «same tank» 1.480–2.140 → scene **+1.73–2.39**, and the
  art's 0.60s fade at +1.10 completes at **+1.70**, the instant the words arrive; «only take what it hands
  you» 3.420–4.700 → **+3.67–4.95**, and the stream closes over +3.67→+4.37, inside its own clause.
  Assembled at +1.70 on a 7.67s scene, so the +2.6 sheet shows a finished mechanism.
- **Rule 8 on the object:** the photograph is an outlet plus a *catching* vessel. What no photograph of a
  spigot can assert is the **supply** behind it — a finite reservoir being metered. §8's aperture refusal is
  honoured: **one** tap is drawn and no second tap beside it.
- `.centred` off; archetype D's stack is top-left either way, so **no type moved** — both focal lines
  (1247.1 / 441.3px at 88) sit inside `.arch-d .huge`'s 1480 cap.

### 3 · The floor, re-checked after the image swap (asked for, and it holds)

Crude comparable proxy (cover window 16:9, locked grade, BT.601 percentiles, no field/scrim — so absolute
values are not the build's composed chain, but the **bottom-three order reproduces it exactly**: s54 · s62 · s67,
matching 13.03 / 20.69 / 22.26):

`s54 0 · s62 4.04 · s67 22.27 · s68 32.03 · s58 32.68 · s59 32.68 · s61 33.34 · s63 33.34 · s56 39.19 ·
s64 57.42 · s53 76.30 · s57 77.60 · s55 78.91 · s66 106.25 · s60 108.20 · s65 127.73`

**s54 is still alone at the bottom by a wide margin; the new s61 lands mid-pack (rank 7 of 16).** The
discharge in the INVARIANT block stands unchanged and **no knob was spent** — no bgpos, no per-scene grade,
nothing re-ordered. The INVARIANT assert still re-derives the census at every build (s54 load 0, chapter
max load 4).

### 4 · Snapshot pass — 28 frames, four batch directories, every one looked at

One `-o` per batch, never reused. All contact sheets reviewed cell by cell; the two changed frames also read
at full resolution.

| Batch | `-o` | Frames | What it was for |
|---|---|---|---|
| b1 | `snapshots/qa3/b1` | 8 | s53–s60 at each scene's LAST cue (1.80 / 9.235 / 16.42 / 22.31 / 29.59 / 34.69 / 44.36 / 49.79) |
| b2 | `snapshots/qa3/b2` | 8 | s61–s68 at each scene's LAST cue (58.15 / 65.01 / 71.57 / 76.87 / 81.77 / 87.07 / 97.55 / 105.0) |
| b3 | `snapshots/qa3/b3` | 6 | entrance/state checks — **this is the batch that caught the `!important` no-op** |
| b4 | `snapshots/qa3/b4` | 6 | the same six states re-shot after the fix |

Every `.stack` sits inside the safe area; nothing overflows; the watermark rides bottom-right on all 28.
Frame notes worth carrying: `b2/87.07s` renders `$78,533` — that is the s66 countUp three units from its end
at exactly the sample time, not a wrong figure. `b2/76.87s` confirms **s64 is still centred** with the chip row
at frame centre.

### 5 · Confirmed unchanged (the five things that had to survive)

- **s64 centred**, chip row at frame centre — `b2/76.87s`. The attempt-2 generator exemption stays **deleted**
  (`if (s.art === "off" && !s.ctr) throw` has no exception), so ch6 cannot inherit it.
- **PEAK 2 (s59) untouched** — no art, no re-tone, no re-timing, no lift; `b1/44.36s`. Nothing was added near
  it, and the density note in the generator says so by name.
- **The floor (s54) discharge upheld** — re-measured above; s54 still the floor, no knob spent.
- **Comma clearance** — s68 and s63 are byte-identical to attempt 2 apart from being re-emitted.
- **No re-timing anywhere.** `S`, `D`, every `data-start` / `data-duration` / `data-framings`, the sixteen
  `<audio>` rows and the root `106.084s` are still generated from `timing.json` and still assert on GAPS:
  s57 25.221 / 7.67, s61 53.003 / 7.2, s56 swap 2.500, s67 swap 4.800, s61 num anchor +4.55 — all unchanged.
  Tracks still alternate 1/2; `sceneTransitions(IDS, S, {acts:["s59"]})` unchanged.
- **§10's crate rhyme is NOT restored** and the generator + composition both say why: it was already
  one-legged (ch6's s77 shipped as a steel shipping container), so the rhyme is **s75/s76 only** and §10's
  text is what is wrong. No chapter should re-fetch toward that description.

### 6 · Density and scope, mechanised

`storyboard §8` budgets this chapter ZERO drawn layers; two now exist, both from rulings dated after the
storyboard. The generator asserts the **list**, not the count: `if (drawn !== "s57,s61") throw`, with both
citations inline, so a third layer — or a quiet deletion of one of these — has to come back through that line.
Two in sixteen scenes is half the archetype note's "three or four in a twelve-to-fourteen scene chapter is the
TOP of the range". Still refused, by name, in the file: 5.6's dial, 5.12's lanes, any layer on s55/s59, and a
§9a measure bar on 5.9. **Both layers are en-only by the text of both rulings — do not port either to hi.**

## Changed

- `studio/videos/passive-income-number-en-ch5/build.mjs`
  - 5.5 row → `art:"tank"`, `ctr:false`, `band:true`, `brule:400`, `artOpts:{slice:false}`; note rewritten to
    state the reversal, the re-origin arithmetic, the measured ground and the measured anchors.
  - 5.9 row → `art:"marks"`, `ctr:false`, `num:"ROUGHLY\n4 TIMES"`, `darkGround:"…"`; note rewritten to carry
    the ruling, the full-resolution read of the new photograph (including the caption discrepancy), the
    placement arithmetic and the §10 correction.
  - New drawn-layer section before the validation loop: `TANK` + `tank(id, o)` (ch4's, plus `slice`),
    `MARK` + `marks(id)`, `ART`, and the markup-level absence asserts (comments stripped first, so the assert
    cannot be silenced by deleting the note that explains it).
  - Guards added: unknown art name; **drawn art requires a `.band` or a measured `darkGround`** (rule 9);
    density assert flipped from `""` to `"s57,s61"` with citations.
  - `scene()`: `art-forward` class, `.band` (z-index 0, before the plate), `.plate`/`.plate-in`/art, `.brule`;
    `PLATE` map added; a `\n` in a `num` now emits `<br>` exactly as a `stmt` does.
  - Template: the two art cue blocks (`#s57-band` +0.90, `#s57-art rect` +1.10, `#s57-stream` span +3.67;
    `#s61-art rect` +2.00), plus the `!important` no-op warning written where the next build will read it.
  - Header + emitted composition header rewritten: art off on 14 of 16, the two drawn layers named with their
    rulings, the crate-rhyme correction, and the plate-rect comment corrected (two rects are now on screen).
- `studio/videos/passive-income-number-en-ch5/index.html` — regenerated (709 lines).
- `studio/videos/passive-income-number-en-ch5/assets/audio.json` — re-derived by `tools/audio/cues.py`
  (29 cues, `bed-tension`); the hero on s55/s59/s61 survives, s61's at 57.553.
- `studio/videos/passive-income-number-en-ch5/snapshots/qa3/{b1,b2,b3,b4}` — 28 QA frames + 4 contact sheets.
- Nothing written to `assets/icons/` (no icon was drawn — five squares are not a reusable icon).

## Owed

1. **`owed.en_ch4_s46_art_fade_is_a_no_op`** — en ch4's `fade("#s46-art", …)` never runs: `.art`'s 52% is
   `!important`. Its tank is on screen from the scene's first frame instead of arriving at +1.00. One-line
   fix in that build's template (`#s46-art` → `#s46-art rect`) whenever ch4 is next opened — e.g. in the
   pre-assembly batch, which already reopens en ch2 and en ch4-adjacent compositions. Not patched from here:
   ch4 is locked and this is not my composition.
2. **`owed.en_ch2_s10_tank_layer` still stands** — item 2 of `owed.en_preassembly_batch` is now discharged
   (s57 landed here), but item 1 is not. With both landed the device reads plant (2.2) → callback (4.7) →
   callback (5.5), which is the only order that works. When applying it, take THIS build's `tank()` (it has
   the `slice` option) and give 2.2 `{slice:true}` — at 2.2 the tank is being filled and nothing has moved.
3. **§10's text is wrong twice and should be corrected in the storyboard, not worked around** — the crate
   rhyme (`s61 → s75/s76 → s77`) is s75/s76 only, and the ruling's own description of s61.jpg
   ("one egg beside it") does not match the file (five eggs, all in the bowl).
4. **A `spanY()` is the honest gap in `motion.js`**, carried forward from ch4 unchanged: there is no scaleY
   helper, so a genuinely sliding level is not expressible. It was not needed here (the level does not move),
   but the gap is real and adding to the system is a deliberate edit to `tools/scaffold/`.
5. **Two things the encode settles, declared rather than predicted** (`method_learned.the_encode_overturned_
   the_build_on_all_three_open_questions_2026-08-12` — a predicted rank is a shortlist, never a verdict):
   (a) whether the five marks read as a COUNT at video scale in the right-hand crescent, where the geometry
   left the only clear region; (b) whether the drawn tank and the photographed bucket read as one argument
   rather than as two vessels.
