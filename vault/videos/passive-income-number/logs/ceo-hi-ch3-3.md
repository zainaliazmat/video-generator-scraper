---
summary: hi ch3 attempt 3 — SHIP, 0 blockers. My one attempt-2 blocker is cleared on the encode, not on report: I counted the twelve cells off a single row profile of the mp4 (51,51,51,52,51,51,51,51,51,50,50,51 px on 9px gaps, twelve, uniform) and watched the three beats build. The 12.63s abacus hold now has motion and an assertion inside it from +1.70, and s24's move out of `.centred` into a left column + right plate incidentally fixed a second thing — the chapter's two plate scenes are now s24 and s28, evenly spaced, where before every scene but s28 was a centred stack. Both new editor notes confirmed as standing constraints, with one measurement of my own added to note 1: the lit cell and the grey cells are at the SAME luma, so the 22px proudness is not decoration, it is the only non-colour cue a colour-blind viewer has.
updated: 2026-08-09
source: studio/videos/passive-income-number-hi-ch3/renders/DRAFT-ch3.mp4 (13 frames pulled fresh: 0.35, 2.60, 11.45/11.65/11.80/11.95 across the joint, 12.10, 13.30/13.90/14.40/15.70/17.40 across the build, 15.75/15.90/16.10/16.50 across the countUp) + rebuilt SHEET.jpg, index.html l.81/141-183, logs/editor-hi-ch3-3.md, logs/ceo-hi-ch3-2.md
stage: fin-ceo, cut hi, chapter 3, attempt 3 — FINAL ROUND, SHIPPED
---

# CEO · passive-income-number · hi · chapter 3 · attempt 3
VERDICT: SHIP

Nothing in this log may hold the chapter. Findings 1–4 are notes and carries.

## Would I keep watching?

Yes, and **I can no longer name a timestamp I would leave at.** That is the change.

At attempt 2 I named 0:11.5–0:18.1 — the second six seconds of an unchanging abacus, carrying
an operation the viewer could not check, with the ÷12 alive only as 26px foot type. I went back
to that exact span first and it is a different scene now. From **+1.70** a bar appears; at
**+2.25** it splits into twelve; at **+2.80** one part goes green and stands proud with ONE
MONTH under it and TWELVE EQUAL MONTHS against it. There is something moving and something
being *claimed* for the whole second half of the hold, and the claim is the one the line makes.

I checked the two things a fix like this usually breaks:

- **The joint holds and the type does not collide.** At 11.45 / 11.65 / 11.80 / 11.95 the
  abacus is continuous and unmistakably one push; s23's centred block fades down the middle
  while s24's `PER MONTH` comes up top-left, and at no frame do the two stacks overlap. The
  crossfade is clean.
- **The cells are real at 1920 and at 480.** Off a single row profile of the encode at y=450 I
  get twelve runs — 51,51,51,52,51,51,51,51,51,50,50,51 px on 8–10px gaps — no dropout, no
  merge, the count is right without counting. Downscaled to 480px wide (a phone at arm's
  length) the green cell, ONE MONTH and TWELVE EQUAL MONTHS all still read, and the strip sits
  at mean luma ~42 against ~21 for the photograph band above it, so it separates from the frame
  rather than sinking into it.

**The chapter also got less templated on the way past.** s24 leaving `.centred` was a mechanical
necessity, not a design choice, but the result is that the chapter's layout string is now
centred ×2 → **plate** → centred ×3 → **plate** → centred ×2. Two art scenes, evenly spaced,
in a chapter that was otherwise nine centred stacks. That is a better strip than the one I
passed on rhythm grounds last round.

Back half unchanged and still the best run on the cut. s26's rusted meter, s27's amber desk,
s28's doubling bars, s29's cable tangle. I did not re-open any of it.

## Findings

| # | scene/span | severity | what | fix |
|---|-----------|----------|------|-----|
| 1 | s24 | **note — confirming the editor's note 1 as a standing constraint, with a reason they did not have** | The lit cell is 1/12 on width and 1.4× on height. The editor ruled it a selection marker and correct here; I agree, and I am adding the measurement that makes the proudness **load-bearing rather than decorative**: sampled on the encode, the lit cell is rgb(14,60,41) and its neighbours are rgb(38,48,49) — **the same luma, ~L46**. Hue is the *only* colour difference. For a deuteranopic viewer the strip is twelve identical grey cells unless something non-colour marks the one. The 22px proudness and the ONE MONTH label under it are that something. | **Binding both ways, and record both in `build.mjs` beside the 1/12 assert.** (a) The proudness **stays** while the cells are equal-width with no baseline and no axis — removing it would cost the read for ~8% of male viewers. (b) It **must go** the moment a variant gives the cells unequal widths or adds a baseline/axis, because at that point height reads as magnitude and the marker becomes a false claim. If a future variant needs both, the marker becomes a rule or a caret **outside** the strip, not a taller cell. |
| 2 | s24 | **note — confirmed binding** | `.art-lift` is load-bearing here: this is the chapter's busiest photograph (plate rect p90 134.6, a grid of forty bright beads) under its most detailed layer, and the build's own no-lift snapshot had the cells ghosting over the beads. | **Do not remove it, and do not let the owed content-agnostic ~48px inset feather be promoted into `chapter-design.css` on the assumption that it is a no-op here.** Whoever promotes it re-measures **on s24 specifically** — s24 is the worst case in either cut and the en-cut editor's warning applies here with the most force. Same if s24.jpg is ever re-fetched: this layer is re-checked, never inherited. |
| 3 | s24 · +3.30 → +4.55 | note (**no render**) | The `.huge` slot sits empty for ~1.2s between the art completing and the ₹5,000 countUp settling, and the settled number then has 1.95s before the cut — about 1.3s at 1.5× speed, thin for the chapter's headline monthly figure. | **None, and I do not want this touched.** The order is right — the operation resolves, then the answer lands — and the figure gets a second, longer look immediately at s25's `WHAT ₹5,000 BUYS`. Filling the gap would mean printing ₹5,000 before the strip finishes saying where it comes from, which is the thing we just fixed. |
| 4 | s27 / s32-s33 / storyboard §9c+§12 / s28 | carried, unchanged | The three should-fix items the editor carries: s27's missing mid-press state (s77 carries it), ch4's counterfoil must be paper, `storyboard-hi.md` l.859 + l.968 still carry the retired five-rung ladder. Plus s28's quiet `corpus-doubles`. | **All four dispositions stand exactly as written in earlier rounds. None of them is a ch3 defect and none may re-open this chapter.** The storyboard rows are the only one with a deadline: fix them before ch5 briefs assets, since the storyboard is what an agent reads by path. |

## Honesty

Unchanged from attempt 2 and re-checked on the new frame. 20,00,000 × 3.0% = 60,000;
60,000 ÷ 12 = 5,000; the strip's 51/612 is 1/12 exactly. The drawing carries the whole and the
words, the type carries the answer once, `AT A 3.0% WITHDRAWAL RATE` is now a 40px `.sub` in
the role colour rather than a droppable foot, and `ILLUSTRATIVE ARITHMETIC` is in frame. No
invented source, no seal, no agency, nothing rounded and presented as precise. I would be
comfortable with the source author watching this chapter.

## Regressions vs editor pass

**None.** The two places a regression could have hidden are the joint and the strip, and I
measured both on this encode rather than inheriting the editor's numbers — the s23→s24 push is
continuous with no step or collision at 11.45–11.95, and the twelve cells resolve individually
at native resolution and survive the downscale. s22's edges, s26–s30 and s28's `corpus-doubles`
are untouched and stay untouched.

## Budget

One REWORK spent on this chapter, one returned clean. **Chapter 3 hi is locked.** ch4's opening
scene s31 still carries the brief from attempt 2 finding 3: s30 closes its loop and hands ch4
no pull, so s31 must earn the cut in its own first two seconds.
