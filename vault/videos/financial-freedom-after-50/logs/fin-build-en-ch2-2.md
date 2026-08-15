# fin-build · financial-freedom-after-50 · en · chapter 2 · attempt 2
STATUS: ok — 2 blockers fixed (s17 cue order, s28 grade+ken), 0 re-timing, `hyperframes check` 0 errors

## Ran
- Read `logs/review-en-ch2-1.md`, `logs/fin-assets-en-ch2-2.md`, `vault/CLAUDE.md`,
  `tools/packs/fin-build.md` (archetype BOX + the two body sections), and
  `tools/format/fin-build.json` (`known_benign`, `chapter_design`, `vector_art`).
  **No note body opened** — the pack and `blockframe.css` / `chapter-design.css`
  answered everything, including the one value that mattered (see Evidence, the grade
  comment at `assets/blockframe.css:69-77`).
- Edited **`build.mjs`**, not `index.html`. The chapter is generated; a hand-edit to the
  html is erased by the next `npm run build` and every attempt-1 comment says so.
  `node build.mjs` → self-asserts pass, `index.html` rewritten.
- 5 snapshot batches, **one `-o` dir per batch**, 23 frames captured:
  `snapshots/qa/r2-s17` (5), `r2-s28` (5), `r2-green` (4), `r2-s28-before` (4),
  `r2-repick` (5). **11 eyeballed at full size** (3 of b1, 2 of b2, 1 of b4, all 5 of b5
  via its contact sheet); **13 measured numerically** for mean/p90 luma (b2, b3, b4).
  The CLI did not throw the navigation timeout on any of the 5 invocations.
  Note for the next stage: `--at` repeated as separate flags is **silently ignored
  except the last one** (the first b1 invocation captured 1 frame from 4 flags);
  `--at 37.0,38.5,39.5` comma-separated captures all of them.
- `npm run check`.

## Failed
- **The reviewer's s14 fix (row 5, should-fix) cannot be executed as written, and it is
  not because s14 was out of scope.** "Re-frame the ken onto the bucket itself" needs a
  HORIZONTAL pan and the system has no lever for one on a `.bg`: `motion.js` `ken()`
  hard-codes `xPercent -2.5 → +2.5` (`assets/js/motion.js:133-137`) and `plateKen()` is
  scale-only (`:256-259`); redefining either inline is forbidden. The remaining native
  lever is `background-position`, and for s14 it is vertical-only — measured: s14.jpg is
  1880×1253 (aspect 1.500) inside a `.bg` box of 2227.2×1252.8 (aspect 1.778), so `cover`
  scales it to 2227.2×1484.4 and crops **231.6px = 15.6% of the image height, zero of its
  width**. The bucket sits at image x 0.06–0.51: any tighter push crops its left edge
  (at k=1.26 the window is x 0.158–0.842) rather than favouring it. Left untouched and
  filed in Owed with the two honest options.
- Nothing else. Both briefed fixes landed on the first build.

## Evidence

### 1. s17 — the source line now follows the figure (P1 row 1)
The root cause was not the foot's time, it was the **rung**: `+2.10` was authored for
scenes whose focal lands at `+1.10`, and s17's focal is ANCHORED to the voice
(`audio_start + 0.45 × duration`). The generator applied the flat rung to an anchored
scene and inverted the ladder. Fixed at the generator, not at the one scene —
`FOOT_AFTER_NUM = 1.00`, derived from the focal, so any future anchored+footed scene in
this chapter inherits it.

| cue | attempt 1 | attempt 2 |
|---|---|---|
| `rise("#s17-head")` | 34.785 | 34.785 (unchanged) |
| `pop("#s17-num")` | 37.991 | **37.991 (unchanged — the anchor is the point)** |
| `fade("#s17-foot")` | **36.585** (1.406 s BEFORE the figure) | **38.991** (1.000 s after) |

- Ladder gaps now 3.206 / 1.000 — both over the 0.8 minimum, first cue still at +0.30.
- Foot finishes 39.391; s17 is on screen to 43.421, so the attribution holds for 4.03 s.
- `assets/audio.json` is **byte-unchanged**: its `hero` cue is bound to the same anchor
  (37.991), so the sound still hits the number and not the citation.
- Eyeballed, `snapshots/qa/r2-s17/`: `frame-00-at-37s` = kicker alone over the card, **no
  orphan attribution**; `frame-01-at-38.5s` = kicker + `North of 20%`, no foot;
  `frame-02-at-39.5s` = the full kicker → figure → source ladder. The 1.4 s of
  "VERIFIED · FEDERAL RESERVE G.19" over a hole is gone.
- Guard against recurrence: `build.mjs` now throws if any scene carrying both a focal and
  a foot emits them less than 0.8 s apart in the wrong order, or if the foot's 0.40 fade
  would run past the scene. It reads the two times back out of the written `index.html`,
  so it tests the artifact, not the intention.

### 2. s28 — the closer, lifted (P1 row 4)
Two levers, **neither of them a token edit and neither darkening anything**.

**(a) Per-image brightness, the knob the grade explicitly exposes.**
`assets/blockframe.css:69-72`: *"Brightness may be calibrated per image (a near-black
texture crushes flat at 0.62) — set it inline on that one `.bg`."* This is the one value
I needed that the pack did not carry, and the CSS carried it, so no note body was opened.
grayscale(0.32) and contrast(1.05) are restated **unchanged** (an inline declaration
replaces the class rule wholesale, so the locked half has to be re-written to stay locked).

Measured source luma, `assets-ch2/final/*.jpg`, mean over the full file:

| | s25 | s26 | s27 | **s28** | ch2 median |
|---|---|---|---|---|---|
| source mean | 111.5 | 93.1 | 70.4 | **53.9** | ~105 |
| through `grayscale(.32) brightness(.62) contrast(1.05)` | 69.1 | 54.2 | 39.5 | **29.5** | — |
| through the same at **brightness(0.92)** | — | — | — | **46.7** | — |

s28 is the darkest photograph in the chapter, against a grade calibrated for the median —
that is why it, and not its neighbours, crushed. 0.92 puts it **between** s26 and s27
instead of 10 below the darker of the two. Headroom check: s28's brightest source pixel is
**219/255**, so at 0.92 exactly **0.00%** of pixels exceed 250. This is unused headroom
being spent, not a crushed frame being stretched.

**(b) `ken: [0.90, 0.98]` — a wide push, replacing the stock `ken(…, true)` 1.00→1.16.**
The daylight is the autumn foliage and open porch at image x 0.02–0.33. The stock ken ends
at a 74.3%-of-width window starting at x 0.109 and spent the shove on the man's shadowed
side. At k=0.90 the window is 95.8% of the image width, at k=0.98 it is 87.9% — the
daylight is in frame for all 5.998 s. Same device as s16 (`ken: [0.90, 0.95]`), inside the
0.8621 coverage floor the ch1 build derived, and the direction parity is unchanged
(s27 pulls back, s28 still pushes in).

**Measured on rendered frames** (PNG snapshot, same pipeline both sides — the absolute
numbers sit below the reviewer's ffmpeg figures, the delta is what is comparable):

| frame | before | after | Δ |
|---|---|---|---|
| s28 @103.0 s | 22.1 mean / 32 p90 | 25.5 / 39 | +15% / +22% |
| s28 @105.0 s | 23.2 / 33 | **26.7 / 41** | +15% / +24% |
| s28 @108.5 s (the shove frame) | 23.8 / 33 | **27.1 / 42** | +14% / +27% |
| s26 @94.0 s (reference) | — | 25.2 / 40 | — |
| s27 @101.5 s (reference) | — | 28.0 / 42 | — |

s28 was the darkest frame of the green run; it now sits **between s26 and s27 on both mean
and p90**, which is the parity target — not an invented bright frame. p90 rising faster
than the mean is the point: the lift lands on the subject, the mug and the porch, not on
the shadows. A/B eyeballed at 108.5 s (`r2-s28-before/frame-02` vs `r2-s28/frame-03`): the
face was a silhouette against black and is now legible with the glasses, the mug, the
porch posts and the foliage reading.

Guard: `build.mjs` throws if an inline `.bg` filter moves anything other than brightness,
or if an inline brightness is ever set **below** the locked 0.62 (that would be rule 9,
the 2026-08-04 rejection, arriving through the back door).

### 3. Constraints held
- **No re-timing.** Full diff of `index.html` against attempt 1 is **5 lines**: two scene
  comments, the s28 `.bg` filter, the s17 foot time, the s28 ken call. Every
  `data-start`, `data-duration`, `data-framings`, `<audio>` row, the `S` map and the root
  `data-duration="108.659"` are **byte-identical**. `build.mjs`'s own asserts re-verify
  all four homes agree, the 0.45 overlaps, and 1/2 track alternation (`12121212121212121`).
- `data-framings` comma-separated (s12 `4.7,4.825`, s23 `4.8,4.908`); no rail; no counter;
  17/17 scenes keep `has-photo` and a real `.bg` on a file that exists.
- s23 and s18 untouched — verified by the diff, which does not name either.
- The re-picked images render correctly in the composition (`r2-repick`, 5/5 eyeballed):
  s15 the leaking pipe with the drip curtain legible, s16 the brass tap mid-drop over
  orange, s22 the snow roller **with its track**. The s14→s16 run reads brown → green →
  orange as fin-assets measured.

### 4. `npm run check`
**0 errors, 4 warnings, 2 infos (lint) · runtime 0/0 · layout 0 errors, 10 infos ·
motion 0/0 · contrast 12/12 pass WCAG AA · CHECK PASSED.**
`known_benign` in `tools/format/fin-build.json` is `[]` and stays `[]` — nothing was
silenced. The four warnings are `composition_file_too_large` (376 lines),
`timeline_track_too_dense` ×2 (9 and 8 elements — that is the mandatory 1/2 alternation),
and `composition_heavy_overlay_count_high` (34), which the reviewer ruled a non-defect on
the encode; per its explicit ruling the overlay stack was **not** thinned globally. The
ten layout infos are all `container_overflow` on a `#sN-bg`, i.e. `.bg { inset: -8% }`
doing exactly what the ken needs it to do. **No new finding of any kind.**
Total composition duration: **108.659 s** (chapter 2 alone; last scene bare, the 0.45
comes back on concat with ch3).

## Changed
- `studio/videos/financial-freedom-after-50-en-ch2/build.mjs`
  - SPEC s28: `ken: [0.90, 0.98], bright: 0.92` + the measured rationale in comment.
  - New `FOOT_AFTER_NUM = 1.00` and the cue emitter derives an anchored scene's foot from
    its focal instead of the flat `+2.10` rung.
  - `.bg` emitter takes an optional inline grade (brightness only).
  - Two new build-time asserts (cue order + foot inside the scene; inline-grade shape and
    the 0.62 floor). Both read the written `index.html` back.
  - Two scene NOTEs rewritten so the generated html explains both fixes in place.
- `studio/videos/financial-freedom-after-50-en-ch2/index.html` — regenerated (5-line diff).
- `assets/audio.json` — regenerated, byte-unchanged.
- `snapshots/qa/r2-*` — 5 new batch dirs.
- Nothing written to `assets/icons/`: no new icon was drawn (see Owed).

## Owed

### The open question: no drawn layer at s15. The re-picked photograph carries it.
**Answer: do not draw it.** Three independent reasons, in order of weight:
1. **Rule 8.** A bucket-with-holes drawn over a photograph of water escaping a pipe is a
   second drawing of the subject — depictive, not additive. It asserts no proportion, no
   comparison, no measurement, no count. That is the exact failure the rule names, and
   "the metaphor needs continuity" is not an exemption from it.
2. **The reviewer already spent the budget, by name.** Row 11: *"Give **two** scenes
   something real on the other side, and they are already named: s25 (the 3-of-6 count)
   and s21 (the roll-down arrow). That is enough; do not manufacture a third."* s15 is not
   one of the two. Density calibration says 3–4 drawn layers in a 12–14 scene chapter is
   the TOP of the range; ch2 currently ships one (s18) and the two named would take it to
   three. A fourth at s15 would spend the ceiling on the weakest of the four candidates.
3. **The picture already says the line.** VO 2.4 is *"it doesn't matter how much water you
   pour in if there are holes in the bottom"* and the storyboard's test was *"the leak must
   be legible, not implied."* The new s15 is water visibly escaping through a rusted pipe,
   in daylight colour — eyeballed at 23.0 s, the drip curtain reads at composition scale
   under `stmt: Pouring faster does not fix a leak.` The container the water escapes is not
   named by the on-screen type (`TWO HOLES`, not `THE BUCKET`), so nothing on screen
   promises a pail that is not there. s14 establishes *a container*, s15 states *the leak*;
   they are one argument told in two states, which is what the D-D-D run is for.
   fin-assets' third path was the right one and I am not adding art on top of it.

### Still open, not mine this round
- **s14's ken re-frame (review row 5)** — see Failed. Two honest options, both cheap, and
  the choice belongs to whoever owns the next brief: (i) `background-position: 50% 72%`
  inline on `#s14-bg`, which spends the 15.6% vertical crop slack on the bucket's base and
  drops the empty barn ceiling — no helper is redefined and no timing moves; or (ii) a
  re-pick, since no lever in the system can move the frame horizontally onto a subject that
  sits at x 0.06–0.51. Do **not** brief "re-frame the ken" again without picking one — the
  instruction as phrased has no implementation.
- **The system gap behind it:** `ken()`'s ±2.5% pan is a constant and `plateKen()` has no
  pan at all, so a `.bg` cannot be recomposed onto an off-centre subject. Three reviewer
  findings across this chapter reduce to that one missing lever. If it is worth closing, it
  is a deliberate edit to `tools/scaffold/assets/js/motion.js` (a `panKen(sel, at, dur,
  from, to, xFrom, xTo)`), not something a build improvises — flagged, not attempted.
- s21 roll-down arrow, s25 3-of-6 count, s24 statement frame — reviewer should-fix rows 6,
  7, 8, all outside this brief. Rows 6 and 7 are the two the reviewer authorised drawn art
  for; if they are briefed, they are the third and fourth drawn layers and the chapter is
  then at its ceiling.
- SHOVE #1 still belongs to chapter 3: it emits `sceneTransitions(IDS, S, {acts: ["s29"]})`.
  Nothing in this file can carry it. The `transition` SFX at abs 177.332 s likewise belongs
  to ch3's cue list at t=0, not to this chapter's last instant.
