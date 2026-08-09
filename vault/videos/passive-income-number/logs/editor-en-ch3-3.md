# editor · passive-income-number · en · chapter 3 · attempt 3
VERDICT: PASS

Reviewed from the current encode (`renders/DRAFT-ch3.mp4`, 96.601s, s24–s39) plus a rebuilt
sheet. The attempt-2 blocker is measurably closed on my own chain, and the build's challenge to
my premise is correct — I verified it against ch2's own encode, not against its log.

## The attempt-2 blocker: CLOSED

I re-ran the three edge measurements the last log named, on the new encode, at four times across
the scene (the ken moves the photograph under a static feather, so one frame would not have
proved it):

| t | left step, x=1120 | top step, y=150 | bottom step, y=760 |
|---|---|---|---|
| 37.5 | **0.48** | **−0.65** | **1.23** |
| 39.5 | **0.30** | **−1.00** | **2.61** |
| 41.0 | **0.26** | **−1.36** | **1.96** |
| 42.8 | **0.15** | **0.19** | **1.24** |

Against 14.60 / 10.63 / −5.13 before. I also swept for the *worst* single-pixel step anywhere in
a 100px band around each declared edge rather than only at the declared coordinate — max |Δ| is
**0.83 luma** (left), **0.63** (top), **0.70** (bottom). There is no edge left to find. Opened
the frame at 41.0 full-size before measuring anything: the bar and the ghost sit on the roof and
the sky with no card behind them, and the drawn layer still reads — amber fill against neutral
ghost, fill stopping at the tick, the tick on the boundary. The lift still does its rule-9 job
where the art is (ground above the bar 31.2 luma). **Blocker closed.**

## My attempt-2 constraint was wrong, and the scoped fix is right

I wrote that a class-level feather "should be a no-op over ch2 s16's dark ground". I did not
measure that; I inferred it. I have now measured it, on `passive-income-number-en-ch2`'s own
`DRAFT-ch2.mp4` at t=54.8, with the same rects:

- s16 panel edges: **left 13.51 · top 9.41 · bottom −6.34** — the same order as s30's pre-fix
  14.60 / 10.63 / −5.13, and within 0.1–1.0 of the build's independently-taken numbers.
- s16's ground is **not dark**: the plate interior means 50.3 luma and the strip outside its left
  edge means 49.4. The lift is darkening a *locally* bright paper diagonal, which is why the
  region means match while the edge step is 13.5.

So a feather shaped to s30 would have moved s16, and the build's diagnosis of *why* is the part
worth keeping: the variable is **how much of the plate the drawn layer occupies**, not how dark
the still is. I opened s16's frame to confirm — the 95/100 grid fills the plate corner to corner,
so its panel reads as the grid's backing; s30's bar occupies only y34.6–65.4%, so its panel read
as an empty card. A plateau at y34–66% would have stripped the lift from s16's top and bottom
grid rows. **Scoping to `#s30-pin` is correct, my class-level instruction was wrong, and I am
recording that so no later pass re-derives the bad heuristic.** ch2 is confirmed untouched three
ways (shared CSS md5, ch2 `index.html` md5, and the id not existing there); I re-rendered nothing
in ch2 and its frame is exactly as reviewed.

## The owed scaffold promotion: agreed, and correctly deferred

A content-agnostic **fixed inset** feather (~48px, left/top/bottom, none on the right where
`.p-b` is off-canvas) in `tools/scaffold/assets/chapter-design.css` is the right shape — it is
the only version that can serve a full-plate mechanism and a third-plate one from the same rule,
and s30 rightly keeps its scoped plateau on top of it. Deferring is right: this stage may not
write `tools/`, ch2 is locked and encoded, and no shipped frame depends on it today.
**One caveat for whoever promotes it:** 48px is 7.9% of the 610px plate, and s16's grid starts at
plate-local y1.5%, so its outermost cell row sits inside the ramp and will lose part of its lift.
Re-measure ch2 s16's AA and its outer-row cell/ghost separation after the promotion — do not
assume a no-op, which is the exact mistake this log is correcting.

## Findings

| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s34 | should-fix | payoff photograph still resolves `9. Insurance`, `The Contractor`, `10. Assignment`, `the prior written consent of the` at 1080p, under a foot citing *Cooley, Hubbard and Walz, AAII Journal, February 1998* | A viewer who reads the frame is reading a services agreement while being told it is a finance paper. §10's letter is met (no title, no figure, no agency name), so it is not a fabricated source — a mismatch, not a falsehood | **Carried, not blocking, and unchanged from attempt 2 by my own instruction.** The crop lever is measured dead; only a re-fetch moves it (journal-style two-column body, no headings, no clause numbers, must land p10 ≥ 80 against today's 92.1). Worth one fetch if fin-assets opens the pool for another reason. Do NOT re-open the German-Bible or 1040-NR-EZ families |
| 2 | s30 | note | ghost track's 100% end lands at x=1910 of 1920 | It terminates visibly so the denominator is bounded, but 10px is inside any safe margin | **Leave it.** `.p-b` is the shared archetype rect; moving it moves every B scene in every chapter for 10px. Recorded so no later reviewer re-derives it |
| 3 | s26 | note | extreme tread macro — a surface where the storyboard cue was four slips on a dashboard | Not a defect: it says car, and one car, and the chips enumerate. But it is a texture on the chapter's longest scene | Accept for this cut. Flag only so ch4 does not add a second texture-macro at length |
| 4 | hi-ch3 s28 | note (carry-forward, out of scope) | still ships the unfeathered `.art-lift` panel over a specular brass balance | Same class, same `.p-b` rect, brighter ground — the same trap this chapter just paid two attempts for | Run the three-edge measurement on hi-ch3 s28 **before** its editor pass, not after. Not this chapter's to fix and not blocking here |

## Verified clean this pass

- **The diff is one hunk.** `index.html` +53/−0 inside `<style>`. Every scene element, `data-start`,
  `data-duration`, `data-framings`, `data-track-index`, the S/D maps, the 16 `<audio>` rows and all
  JS are unchanged from the encode I passed on those points at attempt 2, so those verifications
  stand rather than needing re-derivation. I still re-checked the load-bearing ones on this encode.
- **Numbers settle correctly.** s27 resolves `$332,950` at t=23.0 (the sheet samples at 21.424,
  mid-countUp — a sampling artefact, not a defect); s31 resolves `$656,650`. s30's `33.4%` is still
  a literal string, not a countUp, which is right — a rounded `33%` would be a different published
  figure. Fill 0.334 with the tick at 275.48, matching BLS CE 2024 housing share of $78,535.
- **The drawn layer assembles by +2.90 on a 7.101s scene** — track fades at +1.55, fill spans
  +1.90→+2.80, mark at +2.50→+2.90. It finishes well before the cut and does not fight the roof.
- **No repeat.** 35 files in `assets-ch3/final/`, zero duplicate md5s. The four consecutive
  residential exteriors (s29 street / s30 roof / s31 door / s32 porch) are four different objects
  at four different scales; ch4 should not extend the run to five.
- **One drawn layer is the storyboard's declared budget** (§8 budgets ch3 exactly one), not a
  shortfall — the cap in `fin-editor.json` is 4, but a device the storyboard declares is not a
  finding about the chapter. Raising it on round 3 would be inventing work.

## What is working

- The rung ladder still reads as a ladder — s27 and s31 are the only green frames, both carry
  `AT A 4.0% WITHDRAWAL RATE` above the figure, and the 156px/308px measure bar makes rung three
  visibly twice rung two without copy. Do not touch the scale pair.
- s30's photograph is the right photograph and the bar now sits *on* it rather than on a card.
  The next pass must not swap this file and must not re-open the panel.
- The fine-print run (s33 → s34 → s35 → s36 → s37) is still the best-argued stretch in the cut,
  and s36's clock breaking the paper run is what stops it becoming one texture. Keep the ordering.
