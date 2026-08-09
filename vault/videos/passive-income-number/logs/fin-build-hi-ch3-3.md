# fin-build · passive-income-number · hi · ch3 · attempt 3

Scope: the single blocker from `ceo-hi-ch3-2.md` finding 1 (raised as
`editor-hi-ch3-1.md` finding 3) — grant s24 the chapter's second drawn layer, a
12-segment strip built from ₹60,000 with exactly one segment lit = ₹5,000. All
edits in `build.mjs`; `index.html` regenerated, never hand-patched
(`method_learned.an_asset_swap_needs_a_REBUILD_not_only_a_re-render_2026-08-09`).
One text-only carry taken in the same pass: CEO finding 2 (s27's false
"stamp mid-press" comment), declared under **Changed**.

## Ran

- `node build.mjs` — 4 times (2 throws on my own new asserts, 2 emits)
- `npm run check` — twice (`hyperframes check`, after each emit)
- `npx hyperframes snapshot` — **5 batches, 5 separate `-o` dirs**, 22 frames total,
  all 22 looked at (contact sheets for b4/b5, individually for the rest):
  - `snapshots/qa-s24/b1` — 8 frames, the joint + the pre-lift layer. **Discarded
    as a design read**: my sample times were computed against the wrong phase
    (`artAt` is the fade START, so +1.70 shows nothing), and it is the batch that
    showed the layer failing without `.art-lift`.
  - `snapshots/qa-s24/ref` — 2 frames on s28, the CEO-approved model, for calibration
  - `snapshots/qa-s24/b2` — 4 frames, first lifted build
  - `snapshots/qa-s24/b3` — 4 frames, the three beats at their COMPLETION times
    (13.75 / 14.30 / 16.05) + the scene's last frame
  - `snapshots/qa-s24/b4` — 4 frames across the s23→s24 joint (11.20 / 11.55 / 11.90 / 12.60)
  - `snapshots/qa-s24/b5` — 8 frames, every OTHER scene at its own last cue time
    (3.10 / 8.62 / 20.00 / 26.79 / 36.15 / 44.88 / 51.89 / 57.28)
  - the CLI's `Navigation timeout of 10000 ms` did not fire this session; the retry
    loop (6 attempts per batch) was in place for all five.
- `python3` + PIL — graded-luma statistics of s24.jpg and s28.jpg inside the `.p-b`
  rect, at both ends of the ken. This is the measurement that was **wrong** (below).
- a node re-read of the emitted `index.html` asserting all four timing homes against
  `timing.json`

## Failed

**One real failure, mine, caught by snapshot and not by any check.** The first
build of the layer shipped `.band` only, **no `.art-lift`**, and I justified it
with a number:

| | plate-rect graded luma, mean | median | p90 |
|---|---|---|---|
| s24.jpg (abacus) | 45.6 | **19.0** | **134.6** |
| s28.jpg (balance) | 53.1 | 52.3 | 66.0 |

I read the **median** — 19.0 vs s28's 52.3 — as "dark still, keep the aperture,
`.art-lift` would paste a card over a dark photograph", and wrote that into the
scene note as measured fact. It is the wrong statistic. s24's plate rect is a
**bead grid**: forty large bright objects on a dark ground, so the median
describes the *gaps between the subject* and the mean (45.6) and p90 (134.6)
describe the subject. s28's still is uniform, which is the only case where the
median is the right summary. Snapshotted at +3.30 without the lift
(`snapshots/qa-s24/b1/frame-05-at-14.85s.png`): the twelve cells read as a ghost
over the beads and both word labels sat on bead highlights. `hyperframes check`
was green on that frame — 0 errors, 0 warnings, 20/20 AA — which is exactly the
class of defect the max-density snapshot pass exists to catch.

Corrected by adding `lift: true`, and the whole episode is written into s24's
emitted note so the next build does not re-derive it from the same number.

Two throws on the way, both from asserts I added, both doing their job during the
re-layout: the drawn layer's `+3.4` assembly deadline and the band-before-art
ordering.

Nothing outstanding.

## Evidence

### The strip's computed geometry (viewBox `0 0 860 610` = `.p-b`'s own w/h, 1:1 to screen px)

```
X    = 40                        left edge          (screen x = 1120 + 40 = 1160)
CELL = 51    GAP = 9   N = 12    one month, the cut, the count
PITCH= 60                        CELL + GAP
BARW = 12*51 + 11*9 = 612 + 99 = 711        strip spans vx 40 .. 751
BARY = 260   BARH = 110                     the eleven-twelfths, fill-opacity .5
LIT  = x 40  y 238  w 51  h 154             OVER = 22 above and below the strip
CAPY = 210   LABY = 440                     caption 40px · two labels 30px
```

Asserted in `build.mjs`, so none of it can drift silently:

- `60000 / 12 === 5000` — the line's own division, the real figures
- `CELL / (N*CELL) === 1/12` — 51 / 612 **exactly**, not a drawn approximation
- `GAP >= 9` — `chapter_design.gotchas` 5, the minimum that survives the grade
- `X + BARW = 751 <= 800` — off-canvas guard; `.p-b` is at left 1120 on a 1920
  canvas, so anything past vx 800 is off the frame (`gotchas` 8)
- `artAt[last] + 0.5 <= 3.4` — the `+3.3` sheet-sample mark the CEO briefed;
  s24 assembles at **+3.30**, s28 at **+3.30**
- `bandAt < artAt[0]` — the band lifts before the art it backs

Off-canvas margin: 49px of the usable 800 remain to the right of the strip.

### Rule 8 — why it is additive, on the merits

The photograph is a soroban at rest. An abacus is a device for calculating; what
it cannot do at any bead setting, in any photograph, is assert that **one whole
divides into twelve equal parts and one part is taken**. That is a proportion —
which `format.json` `scene_modifiers.art-forward` is reserved for and
`vector_art.lottie.reach_for_it_when` names outright ("a subset inside a set …
these are FAILS as flat photos"). Nothing drawn re-draws anything photographed,
so the s27 ghost-envelope objection does not reach it. The scene carries
`art-forward` for that reason (.30 → .52).

Three beats, in the order the sentence runs, each verified on its own frame:

| beat | at | complete | frame | what it reads |
|---|---|---|---|---|
| a1 the WHOLE | +1.70 | +2.20 (13.75s) | `b3/frame-00` | one undivided bar, captioned **₹60,000 A YEAR** |
| a2 the CUT | +2.25 | +2.75 (14.30s) | `b3/frame-01` | eleven 9px gaps knocked through it → twelve cells, **TWELVE EQUAL MONTHS** |
| a3 the PART TAKEN | +2.80 | +3.30 (14.85s) | `b2/frame-02` | cell 1 in `--fund`, standing 22px proud, **ONE MONTH** |

Settled frame at 16.05s (`b3/frame-02`): the left column reads PER MONTH · AT A
3.0% WITHDRAWAL RATE · **₹5,000** · ₹60,000 divided by 12 · ILLUSTRATIVE
ARITHMETIC, and the right plate carries the strip with the green cell. The green
of the answer and the green of the taken month are the same token.

**No figure is printed twice.** The art carries ₹60,000 — which the type states
only in the 26px foot the CEO called unread at 1.5× — plus two word labels.
₹5,000 is the `.huge` and appears exactly once in the frame. Same discipline as
s28's labels (`artLabels` is scanned by the build's ₹-token guard, so both new
figures had to be in the rate assert's CORPUS list; ₹60,000 already was).

**Three signals for one fact**, because hue is the first thing an encode spends:
the lit cell is the only *filled* cell, it is `--fund` where the rest are ink at
fill-opacity .5, and it overhangs the strip by 22px top and bottom — a shape
difference, which survives anything.

### The s23→s24 hold is unbroken

`snapshots/qa-s24/b4`, the CEO's own three times plus one:

- `plateKen("#s23-bg", S.s23, D.s23, 1.000, 1.090)` and
  `plateKen("#s24-bg", S.s24, D.s24, 1.000, 1.065)` — **byte-identical to attempt 2**
- `<div class="bg" id="s24-bg" style="background-image:url(assets-ch3/final/s24.jpg)">`
  — plain `cover`, no window, unchanged
- 11.20 → 11.55 → 11.90 → 12.60: the abacus grows smoothly across the joint, no
  jump, no self-dissolve ghost of the photograph. Only the type cross-fades. The
  lifted plate is imperceptible at the joint and the strip does not begin until
  +1.70 (13.25s), well clear of it.

### Timing is byte-identical — root **61.143s**

Re-read out of the emitted document and re-derived from `timing.json`,
scene by scene, not asserted:

```
root data-duration = 61.143   (= 3.9 scene_start + scene_duration − offset 124.007)
scene timing drift: 0        (all 9 data-start / data-duration / data-framings)
S map, D map, 9 <audio> rows: 0 drift
```

| | start | dur | d-dur | framings | track |
|---|---|---|---|---|---|
| s22 | 0 | 5.424 | 5.874 | 5.424 | 2 |
| s23 | 5.423 | 6.129 | 6.579 | 6.129 | 1 |
| **s24** | **11.552** | **6.051** | **6.501** | **6.051** | **2** |
| s25 | 17.603 | 6.782 | 7.232 | 6.782 | 1 |
| s26 | 24.385 | 8.219 | 8.669 | 8.219 | 2 |
| s27 | 32.604 | 8.976 | 9.426 | 8.976 | 1 |
| s28 | 41.580 | 8.506 | 8.956 | 8.506 | 2 |
| s29 | 50.086 | 5.398 | 5.848 | 5.398 | 1 |
| s30 | 55.484 | 5.659 | 5.659 | 5.659 | 2 |

Every one identical to the attempt-2 table. The layer is assembled entirely
inside s24's own 6.051s and finishes at +3.30, 2.75s before the cut.
`assets/audio.json` re-emitted **identically**: 12 cues, `bed-resolve`. s24 is on
storyboard §2's declared DRY list and the three art beats use `fade`, which
`tools/audio/cues.py` does not ring — so the layer assembles in silence by
construction, not by an edit to the derived cue list.

### Cap check

`format.json vector_art.lottie.max_per_chapter` = **4**. Chapter 3 goes **1 → 2**.
Within cap. The build now asserts the drawn-scene LIST (`"s24,s28"`), not just the
count, so a later edit that moves a layer has to come back through that line.

### `npm run check`

```
Lint      0 error(s), 3 warning(s), 2 info(s)
Runtime   0 errors, 0 warnings
Layout    0 error(s), 0 warning(s), 18 info(s)
Contrast  20/20 text checks pass WCAG AA
◇  Check passed
```

- **The 3 lint warnings are pre-existing, not introduced**, and I verified rather
  than assumed it: `MAX_COMPOSITION_LINES = 300` in
  `node_modules/hyperframes/dist/cli.js`, and the file was already **463** lines
  before this change (now 521) — the threshold was passed long ago. The two
  `timeline_track_too_dense` warnings count scenes per track (2:5, 1:4) and no
  track assignment changed. They are warnings, not errors, so the layout and
  contrast passes still ran — which the `known_benign` note warns an ERROR would
  have skipped.
- Layout infos went **13 → 18**. The five new ones are all on s24 and all the same
  kinds s28 already produces: 3 × `text_occluded` on the new svg labels (they sit
  under `.scrim`, exactly like s28's CORPUS / A MONTH), `container_overflow` +
  `panel_out_of_canvas` on `#s24-plate` (60px — `.p-b` is 1120+860 = 1980 on a
  1920 canvas, which is the archetype's declared geometry and the reason the
  build asserts vx ≤ 800). Nothing new in kind.
- Contrast **17/17 → 20/20**, the three extra checks being the new svg labels, all
  passing AA.
- **No token was touched.** `known_benign` is still empty and I added nothing to it.

### Regression pass — the eight untouched scenes

`snapshots/qa-s24/b5`, each sampled at its own last cue time, all 8 looked at:

- **s22** @3.10 — gullaks fill the frame as round clay containers, coin slits
  countable, `₹20,00,000` settled in `en-IN` grouping, plain `cover` window intact
- s23 @8.62 — the sum, centred, unchanged
- s25 @20.00 · s26 @26.79 — fan and meter, unchanged
- **s27** @36.15 — amber `3.0%` on the stamp desk, unchanged
- **s28** @44.88 — `corpus-doubles` on its lifted plate, both pairs and the rate
  rule, unchanged
- **s29** @51.89 — cable tangle edge to edge, red `stmt`, unchanged
- **s30** @57.28 — bullock cart, bare 5.659s tail, unchanged

Every stack inside the safe area, no overflow, watermark on `#root::after`
bottom-right on all frames.

## Changed

`studio/videos/passive-income-number-hi-ch3/build.mjs` — nine edits:

1. **SCENES row `3.3` (s24)** — `art: "off", ctr: true` → `art: "divide12",
   ctr: false, forward: true, lift: true`, plus `artLabels`, `bandAt: 1.40`,
   `artAt: [1.70, 2.25, 2.80]`. `.centred` had to go: `.scene.centred .plate` is
   `display:none`, so a centred scene renders the svg into nothing with every
   check green. The type moves to archetype B's left column (`.arch-b .huge/.foot`
   cap at 900px; the focal ends at x≈565 and the foot at x≈897, both clear of the
   plate's 1120 edge). No timing field touched.
2. **s24's note** — the ruling, the rule-8 argument, the three beats, the
   arithmetic, the `.art-lift` mistake and the median-vs-mean lesson, and the
   explicit statement that the `.bg`, its plateKen endpoints and all three timing
   attributes are byte-identical.
3. **s23's note** — the paragraph declining a drawn ÷12 was false as of this
   ruling. Replaced with why the layer lands at the RIGHT end of the hold (the
   abacus is fresh for the first 6.6s; the argument is about the second six
   seconds) and that s23 itself keeps nothing drawn.
4. **s27's note** — **CEO finding 2, taken in the same pass.** "The photograph IS
   a stamp mid-press" → "two stamps standing at rest", with the disposition the
   CEO confirmed (the through-line ships two states, not three; s77 carries the
   missing change) recorded inline. Also "the second claim on §8's one-layer
   budget" → refused on the merits, not on a count, which my change makes
   necessary anyway. Comment-only: **zero rendered pixels change**.
5. **`ART.divide12`** — the new generator, with the geometry, the four asserts and
   the reasoning above it.
6. **The density assert** — `!== 1` → an assert on the drawn-scene LIST
   (`"s24,s28"`) plus the `max_per_chapter` = 4 ceiling.
7. **`artJs` / `artDone`** — de-hardcoded from `sc.find(...)` (one art scene) to
   `sc.filter(...)`, and given the two new asserts (assembly ≤ +3.4, band before
   art). This is the line that would have silently emitted cues for only one of
   the two layers.
8. **The `.v-notch` local CSS comment** — it claimed one use (s28's midpoint
   notch); it now has two, and s24's eleven gaps ARE the cut beat. The class is
   reused, not duplicated. `--bg` is read, never redefined.
9. **The emitted document's header comment and the art cue block** — "ONE DRAWN
   LAYER" → both layers described, and the spec-table comments at the top of
   SCENES (`art` and `ctr` rows) rewritten to match.

`studio/videos/passive-income-number-hi-ch3/index.html` — **regenerated**, not
hand-edited. `assets/audio.json` re-emitted identically.

Nothing written outside the cut directory except this log. No asset byte changed,
no system file touched, no token edited, nothing added to `assets/icons/`
(the strip is composition-specific geometry, not a reusable icon).

## Owed

- **`fin-render` must re-render ch3.** The mp4 in `renders/` predates this change
  and has no drawn layer at s24.
- The three findings that can only be judged on the encode belong to that pass:
  the s23→s24 push read at speed rather than on four stills, whether the twelve
  cells hold together at 1.5× on a phone, and whether the strip's `fill-opacity`
  of .5 survives h.264 over the bead texture. The stills say yes; the encode is
  the authority.
- **A standing note for every future chapter build, from this session's own
  mistake:** to decide `.art-lift`, do not read the plate rect's MEDIAN luma. On a
  high-variance still (beads, coins, type, foliage) the median describes the gaps
  between the subject. Read the mean and p90 together, and then look at the frame —
  the snapshot is the authority and `hyperframes check` is green either way.
  Belongs in `design-chapter-archetypes.md` §"The gotchas that cost renders" as a
  ninth gotcha; I do not write vault knowledge notes from this stage, so it is
  raised here for whoever owns that edit.
- s30's bare tail, s28's `corpus-doubles` and s27's payoff are untouched and
  verified unchanged on stills; they need no further attention from this stage.
