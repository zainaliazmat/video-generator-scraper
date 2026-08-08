# fin-build · passive-income-number · hi · chapter 2 · attempt 3

STATUS: ok

Finishes attempt 2, which stalled mid-decision on a watchdog and wrote nothing. Its work was
in `build.mjs` only (15:45) and `index.html` / `assets/audio.json` were both still 12:48 —
so the outputs on disk were the ATTEMPT 1 build against six photographs that no longer exist.
Both are now regenerated and both are newer than `build.mjs`.

⚠ `fin-build-hi-ch2-2.md` is dated 2026-08-07 and is an EARLIER SESSION's file. It was not
read as a record of attempt 2 and it has not been touched.

---

## 1 · What attempt 2 had actually left half-done

Verified rather than assumed, by reading `build.mjs` end to end and running it.

| item | state found | state now |
|---|---|---|
| six replaced images (s9 s14 s15 s16 s19 s20) | `.src` notes rewritten in the SCENES table, correct | shipped — `index.html` regenerated against them |
| s18 `countUp` 1.2 → 0.45, foot +3.61 → +3.11 | `countDur: 0.45, footAt: 3.11` **declared in the spec and read by nothing** — the emitter still hard-coded `1.2` and `numAt + 0.80` | wired; emitted as `countUp(…, 0.45, …)` and `fade("#s18-foot", S.s18 + 3.11, 0.5)` |
| the drawn layer at s20 | `art: "months", ctr: false, forward: true, artAt: 1.75, artStep: 0.11` declared — and **the build threw**: the art assert still said "chapter 2 declares zero drawn layers", the emitter hard-coded `art-off centred`, and there was no generator | implemented (§3) |
| the dead local CSS patch | `.scene.centred.arch-b .huge/.foot { max-width: 1500px }` still in the composition's `<style>` | deleted (§5) |

So the stalled agent's last words — "now s19 and s20 — the drawn-layer decision" — were accurate
about where it stopped. Everything before s18's cue wiring was done and correct.

---

## 2 · THE DRAWN-LAYER DECISION — s20's twelve months. Two claims declined.

**Taken: (b), twelve marks at s20.** §8's density budget is ONE and it is spent here.

**Declined (a), the `÷12` at s17→s18** — fin-editor's own first choice, so this needs a reason
and not a preference. The division is already asserted **three times in type** on those two
frames: s17 prints `₹10,00,000 AT 3.0% IS ₹30,000 A YEAR`, s18 prints `₹2,500`, and s18's foot
prints `₹30,000 divided by 12`. A drawn `÷12` would be the fourth statement of an arithmetic
the frame already carries in full. s20 has **zero** statements of its count. One budget, and
the difference between "said a fourth time" and "said at all" decides it.

**Declined (c), the wifi arc at s19** — recommended by fin-assets, and cheap. The frame carries
one of its two named subjects (the phone); the internet is absent from the photograph but IS
present in the sentence set over it, `The phone recharge / and the home internet`, at 88px. A
scene whose second subject is carried by its own focal is not in the same condition as a scene
that asserts nothing at all. It is the weaker of two claims on one budget, not a bad idea — if
a later ruling raises ch2's budget to two, this is the one to add.

**Why s20 could not simply stay `art-off`.** §8 refused the twelve stubs on a stated premise —
"the photograph *is* the count" — and that premise is dead twice over: fin-editor ruled from
the encode that the card-index drawer states no count (and graded to folded green cloth), and
fin-assets then established over twelve sheets and ~66 cells that a countable twelve is not
buyable on these pools in any acceptable form. Its replacement is an **admitted host**, a
near-flat cool grey wall. Drawing the count is `vector_art.reach_for_it_when` on the merits
(a COUNT is a FAIL as a flat photograph) and it is ADDITIVE under rule 8 **by construction** —
there is nothing countable in the picture to re-draw.

The override of §7's `art: off` / `ctr: Y` row for scene 20 is declared here and in the
generated document's own comment, not silently taken.

---

## 3 · How the layer is built

- Archetype **C**, `.p-c` (1046, −60, 934×1200), so the scene loses `.centred`: type left in
  C's 880px column, art full-height right, cropped by the frame edge as C intends.
  `.centred` would have set `.plate { display: none }` and rendered the svg into nothing with
  every check green — asserted against in `build.mjs` now.
- **Authored in the plate's own 934×1200 space**, and laid out against the VISIBLE part of it
  (x 0–874, y 60–1140) rather than the nominal box, because the plate hangs 60px off three
  edges. A 3×4 grid of 150px cells at 56px gaps, centred in that window.
- **Solid fills, not outline scaffolding** (`chapter_design.gotchas`): each month is a ghost
  cell at **fill-opacity .2** — up from frame one, so the frame says TWELVE before it says
  PAID — with a solid `--fund` square arriving inside it. No strokes anywhere, so the
  `stroke-width` attribute no-op cannot bite.
- `.art-forward` (52%), not the default 30%. This is the hybrid case the modifier exists for:
  the drawn mechanism is the content and the photograph is a host. **No `.art-lift`** — s20 is
  the chapter's darkest frame (predicted encoded p90 30.3), so the aperture is already dark and
  the lift would only mute the green. **No `.band`**, same reason. The photograph is not
  darkened per scene anywhere in this cut (rule 9).
- **Truth bar:** 30,000 ÷ 12 = 2,500 exactly, twelve equal cells, no remainder — the equality
  the two preceding frames just printed. The comment in the svg says so.
- Motion: **one `popEach`**, `S.s20 + 1.75`, stagger 0.11, arriving left-to-right (= Jan→Dec in
  DOM order). The twelfth cell starts at **+2.96** and is fully in at **+3.36** — on
  `chapter_design.gotchas`' +3.3 sheet mark to within two frames, so `chapter_sheet.py` samples
  a finished grid rather than a half-built one that reads as a defect it is not. The
  photograph keeps the ken; the plate does not move. One motion per scene.

---

## 4 · The cascade question (brief item 3) — this chapter has none

`clauses.py` was not needed and was not run, and the reason is worth stating so the next
chapter does not skip it out of imitation. 2.12 is a **single clause** («सैलरी में से एक रुपया भी नहीं»)
with no enumerated nouns — there are no clause onsets to anchor to and nothing for
`clauses.py` to measure. The twelve marks are a **visual count under one spoken sentence**,
which is what a stagger is for; the hi ch1 s6 defect (a cascade finishing 0.20s before its
first noun) is a different shape and does not apply.

**And ONE popEach, not twelve pop() calls, is a SOUND decision as much as a motion one.**
`tools/audio/cues.py` now emits one chip per `pop()` call at that call's own time — twelve
calls would be twelve chips 0.11s apart, straight through the 0.80s gap floor. The single
`popEach` derives to exactly one `chip`.

⚠ **Declared deviation from storyboard §7's sfx column:** s20's row says `reveal`. It now
derives `chip` at 68.359 (was `reveal` at 67.709 on the statement rise), because the scene now
has a real cascade in it and `chip` is the kit's cue for a cascade. Cue count is unchanged at
**17**; min gap **1.100s** against the 0.8 floor. `cues.py` exits 0 on the project with empty
stderr. The `hero`→`reveal` downgrade at s14 is unchanged and still recorded in `_hero`.

---

## 5 · Two things deleted, and one assert added

**Deleted: the local `.scene.centred.arch-b .huge/.foot { max-width: 1500px }` patch.** Both it
and the `padding-left: 0` reset were ported into `tools/scaffold/assets/chapter-design.css` on
2026-08-08 (lines 189 and 203-204). The project's `assets/chapter-design.css` and
`assets/blockframe.css` were diffed byte-for-byte against the scaffold — **identical** — before
deleting. Keeping a local copy "for safety" is exactly how a system file and five compositions
drift apart. The only remaining local CSS is `.v-rate` (a genuine one-off: `pulse` is a
transform and transforms do not apply to a non-replaced inline box) and the four plate rects.

**Added: a settled-time assert**, because fin-editor's finding #6 is a class of defect, not an
incident. A figure still rolling when the cross-dissolve starts has not been read, and the
quantity that matters is **settled time** — scene duration minus (anchor + roll) — not roll
length. Floor 1.20s, plus a second assert that a figure scene's foot finishes fading in at
least 0.80s before the scene ends.

| scene | anchor | roll | lands | **settled** |
|---|---|---|---|---|
| s14 `3.0%` (`pop`, no countUp) | +4.49 | 0.60 | +5.09 | 1.326s |
| s16 `₹10,00,000` hero | +1.90 | 1.20 | +3.10 | **2.245s** (the editor's benchmark, untouched) |
| s18 `₹2,500` | +2.81 | **0.45** | +3.26 | **1.380s** (was 0.629s) |

The spoken anchor (+2.81, 0.2s ahead of «ढाई हज़ार») is NOT moved and `timing.json` is NOT
touched. Negative control: reverting `countDur` to 1.2 makes the assert throw on s18 with
`settled 0.63s`; the s14 branch caught its own bug on first run (it was measuring an uncounted
`.mega` against a countUp duration it does not have).

---

## 6 · The max-density snapshot pass — 15 frames, 3 batches, 3 separate `-o` dirs

`snapshots/qa3/b1`, `b2`, `b3`. **One directory per batch** — `snapshot` wipes its `-o` on every
run, so a shared dir would have left only the last five frames on disk. **Fifteen frames were
actually looked at** (three contact sheets), plus **two read at full resolution** (s12 at
19.482s, s20 at 69.969s). All thirteen scenes are covered; s20 and s21 twice. No CLI timeout
this run — the retry loop was in place and fired zero times.

Each `--at` is that scene's LAST cue END, not its start:
1.80 · 7.693 · 13.353 · 19.482 · 27.335 | 36.336 · 40.862 · 47.932 · 53.277 · 59.032 |
62.462 · 68.100 · 69.969 · 74.825 · 81.400

Result: every `.stack` inside the safe area, nothing overflowing, the `cut-hi` watermark on
every frame. Specifically confirmed by eye:

- **s16's hero** is the new current-series ₹500 still — `6HP 962971` legible in frame, no
  repeated serial. The prop-money file is gone.
- **s14→s15** is one continuous push on the pencil-and-notebook photograph; the crop registers.
- **s18 at +3.61** is fully settled: rate `.sub`, `₹2,500`, and the foot all up and readable
  1.03s before the dissolve. This is the frame the editor could not read.
- **s20** now states its count: twelve cells countable at a glance, green marks legible at 52%
  over the grey wall, type left with room.
- **s12** is genuinely centred at full resolution (the downscaled contact sheet reads as
  left-aligned; it is not).

---

## 7 · For fin-render and fin-editor

1. **s21's recess is visible at both sampled times** (74.825 and 81.400) — editor #10 said it
   was gone by 79.5s. The photograph and its ken are unchanged from attempt 1, so this is worth
   re-ruling from the encode rather than pre-emptively retargeting. Not touched.
2. **The un-inversion must be settled from the encode**, not from the predictor: s16 (54.2)
   leads s11 (52.8) by 1.4 inside a method that over-predicted en ch2 by 7. If s11 wins, s11's
   photograph is the lever (fin-assets §12), not the ground, the scrim or the grade.
3. **`s20-plate` reports `panel_out_of_canvas` / `container_overflow` at INFO level.** That is
   archetype C doing exactly what format.json says it does — "artefact full-height right,
   cropped by the frame edge" — and it is the same class of finding every `.bg` already
   reports under the −8% ken inset. Not marked with `data-layout-allow-overflow`, because no
   build in this system marks the `.bg` either and a one-off exception would be the drift.
4. Two money still-lifes now sit seven scenes apart (s9's ₹5 coin, s16's notes) — fin-assets
   declared it; nothing in the build changes that reading.

No system gap found this run. Nothing was added to `assets/icons/` — the twelve cells are a
count in a plate, not a reusable icon.

---

## 8 · Gates

| gate | result |
|---|---|
| `npm run check` (`hyperframes check` 0.7.66) | **PASS** — 0 errors. **13/13 text checks pass WCAG AA.** 4 lint warnings + 13 infos, all pre-existing structural notes (file size, track density, heavy-overlay count, `pointer-events:none`, `.bg` overflow) plus the two new s20-plate infos at #7.3 |
| `tools/check_vo_frame.py --cut hi --chapter 2` | **PASS** — 13 scenes cross-checked against their VO lines |
| `tools/audio/cues.py <project>` | **exit 0**, empty stderr, 17 cues, min gap 1.100s, music `bed-resolve` |
| `pipeline_check check build --cut hi --chapter 2` | **PASS build-hi** |

13 scenes s9–s21 · root **81.531s** · offset **42.475s** (= hi ch1's root, so the chapters abut)
· 12 dissolve joints at +0.45, tracks alternating 1/2 · no re-time, no token edited.

## NEXT

fin-render: draft-encode ch2 and measure s16 against s11 for the un-inversion (fin-assets §12
hedge 1), then re-rule s21's recess and s20's drawn count from the mp4.
