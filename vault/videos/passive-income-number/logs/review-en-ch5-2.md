# review · passive-income-number · en · chapter 5 · attempt 2
VERDICT: PASS
PASS 1: 0 blockers, 2 should-fix
PASS 2: 0 blockers, 0 should-fix

Read from ONE sheet rebuilt at this attempt (`tools/chapter_sheet.py` → `renders/SHEET.jpg`,
18 cells, s53–s68 + both swap framings), then 26 sampled frames from the ENCODE
`renders/DRAFT-ch5.mp4`. Every number below is measured on the encode; nothing quotes a
build-chain prediction.

## THE TWO QUESTIONS THE BUILD DECLARED — both settled, neither deferred

**1 · Do the five marks read as a COUNT? YES.**
Measured on the encode at t=58.00, column x1690–1745: five runs at y240–294, 320–374,
400–454, 480–534, **gap**, 632–686. Inter-mark spacing **26px** inside the group and
**98px** to the fifth — the declared 24/96 within a pixel. Four-grouped-plus-one-apart is
the only available reading: the marks are identical in size and fill (no active/inactive
distinction, so they cannot be a pagination or scene counter — box item 8 does not fire),
and squares over a photograph of ovoids cannot be misread as drawn eggs. **Downscaled to
420px wide (phone at 1.5×) I still counted 4+1 without effort.** The photograph carries
five eggs and the device carries five marks, so nothing on the frame states a competing
multiple — ruling (b) is satisfied on the encode, not just on the spec.
⚠ The `.src`-vs-file discrepancy (five eggs ALL inside the bowl, not four-beside-one on a
table) is already declared in the build comment and authorised by the ruling's own
"nobody re-searches". Not re-raised.

**2 · Do the drawn tank and the photographed bucket read as ONE argument? YES, weakly —
and the weakness is the declared form of the archetype, not a defect.**
The frame reads as *a photograph with a diagram lifted onto it*, which is exactly what box
item 2 asks a plate to be ("a LIFTED PANEL, not a transparent window"). The binding is real
and legible: the photograph shows an outlet above a catching vessel, the drawing shows the
finite supply BEHIND an outlet, and `SAME TANK, SMALLER TAP` names the relation. Round 1's
defect — *"a tank callback with no tank"* — is **closed**: there is a tank, a level, a tap
and a stream on screen. The residual is a scale mismatch (drawn vessel ≈ half the
photographed bucket's height, no shared axis), which costs no viewer and which I am not
asking anyone to fix. See finding #2 for what *is* worth fixing on this frame.

**3 · Do both drawn layers ARRIVE? YES — the `fade()` no-op is genuinely gone.**
s61 at t=54.20 (+1.20, art cue is +2.00): marks **absent**. At t=55.60 (+2.60): present.
s57 at t=26.00 (+0.78, art cue is +1.10): tank **absent**, band absent. At t=29.20: present.
And the one state change animates on the encode — the s57 stream measures x1650→**1706**
(56px, scaleX 2.4) at t=28.60 and x1650→**1673** (24px, scaleX 1.0) at t=29.60, completing
at 29.591 with 3.75s of scene left. `span()` is doing what it says.

## Findings
| # | pass | scene/span | severity | what | why it fails | fix |
|---|------|-----------|----------|------|--------------|-----|
| 1 | P1 | s57 + s61 | should-fix | **the drawn-layer ink lands at roughly half its predicted contrast, on both layers, for one shared reason.** Measured on the encode: s61 marks (77,72,74) against local ground (21,13,18) = **2.13:1**, where the build computed ≈5:1. s57 tank walls (78,65,68) against band-darkened ground (38,28,34) = **1.70:1**, where the build computed ≈4.3:1. The band is working (interior ground is genuinely dark) and `--art-op:.52` is resolving — what neither prediction accounted for is that **`.scrim` sits ABOVE `.plate` in the DOM**, so it multiplies ink and ground together and compresses the ratio | below the 3:1 floor for a graphical object, on the two frames whose whole justification is that a drawing asserts what the photograph cannot. It is **not a blocker**: I downscaled both frames to 420px (phone at 1.5×) and read the 4+1 count and the tank/level/tap without effort — big solid shapes tolerate what glyphs do not, and both meanings are also carried by type. But it is the ninth prediction-vs-encode gap on this run and it will recur on every future `art-forward` scene | **route to `owed.en_preassembly_batch`, do not spend a third ch5 render on it.** That batch already reopens en ch2 (s10 tank) and en ch4 (s46 tank) for this same device, so the knob gets turned once for three chapters: either lift `--art-op` on `.art-forward` to compensate the measured scrim factor, or move `.scrim` below `.plate` for `art-forward` scenes only. ⚠ Whoever does it must **re-measure on an encode**, not recompute — that is the habit this finding exists to break |
| 2 | P1 | s57 (5.5) | should-fix | the ONE declared state change is invisible. `span(#s57-stream, 2.4→1.0)` is *measurably* correct (56px → 24px, verified above) but the stream rect measures ≈**1.35:1** against its ground, and the change is a 32px width delta on a dim rect in the bottom-right quadrant while 88px red type is arriving top-left. I could not see it by eye across two sampled frames — I had to measure it | `SAME TANK, SMALLER TAP` promises a change of aperture; with the taper imperceptible, "smaller" is carried by the kicker alone and the layer is effectively a static drawing, which drifts toward rule 8's depictive reading of a vessel drawn over a photographed vessel | same root cause and same batch as #1 — the ink lift fixes this too, and the stream is `.flw` so it gains the most. **No re-timing:** +3.67 is measured against «only take what it hands you» and must not move. If the lift alone proves not enough at the batch's re-measure, thicken the stream rect from 24 to ~34 rather than brightening it past the tank walls |
| 3 | P1 | s61 (5.9) | note | for the 2.55s between the marks arriving (+2.00) and `ROUGHLY 4 TIMES` (+4.55), the frame is a soft bowl of eggs, a disclaimer about decimals, and five grey squares with nothing on screen to bind them to a count | the marks are at their least legible-as-an-argument in exactly the window before the type explains them. Not a blocker: identical fill defeats the counter reading, and +4.55 is a measured VO anchor that must not move | if s61 is ever reopened for anything else, move the art cue to **+3.70** — gaps become 2.60 (foot→art) and 0.85 (art→num), both clear of 0.8, and the marks then land as the setup for the word rather than as furniture. Not worth a render on its own |
| 4 | P1 | s57 (5.5) | note | the cue ladder shows a sub-0.8 pair: kick +0.30, **band +0.90, art+stmt +1.10**, span +3.67 → gaps of 0.60 and 0.20 | not a defect. `.band` is a darkening behind the art at z-index 0, not an element the viewer reads as an arrival, and the art and statement fire together at +1.10. The reader-visible ladder is 0.30 → 1.10 → 3.67, i.e. 0.80 / 2.57 | none. Recorded so gate two does not re-flag it as a ladder violation. Every other scene: first cue +0.30, no reader-visible gap under 0.8, tail ≥1.59s |
| 5 | P1 | s61 (5.9) | note | box item 2 asks a plate to be a lifted panel; s61's marks sit on the photograph with no band and no visible panel edge — visually a transparent window | defensible and I am not asking for it to change: the wood under the column measures graded ≈0, so a band there would darken nothing visible, and rule 9 forbids the alternative of darkening the photograph. It is the same knob as #1 | none separately. If the batch lifts `--art-op` it is discharged |

## Everything else I checked, and where it landed
- **The floor (s54) SURVIVED the s61 image swap.** Re-measured on this encode, 3 frames per
  scene, dissolve zones excluded: **s54 23.42** · s62 26.65 · s67 27.23 · s59 27.41 · s58
  28.99 · s63 29.23 · **s61 30.76 (rank 7 of 16)** · s56 30.93 · s68 31.84 · s57 33.41 ·
  s64 33.90 · s53 36.09 · s55 40.48 · s65 40.70 · s66 42.59 · s60 43.03. s54→s62 separates
  by **3.23 points**, well outside the 1.0 band, so s54 is still uniquely the darkest frame
  and 5.2 is still the emptiest beat. The invariant holds and the build's prediction was
  right this once.
- **Round 1's should-fix #2/#4 (s64) is DISCHARGED and it is the biggest single improvement
  in this draft.** `centred` is on; at t=79.50 the three chips are large centred pills
  (white numerals in navy with an amber ring) at frame centre under `THREE ROUTES`, and the
  photograph now reads as parallel/diverging arrow lanes. The 70%-empty corner frame is gone.
- **`no_return_promise` — clean on both drawn layers, verified in markup and on the frame.**
  s61's svg holds exactly five `<rect class="fl">` and nothing else: no `<text>`, no scale,
  no ticks, no numerals, no axis, no track, no baseline. s61 restates «roughly four times»,
  an audited VO figure. s57 holds one static water rect (`slice:false`), no ghost, no tick,
  no numeral, and the level never moves. ⚠ **I did consider whether the 2.4→1.0 taper
  asserts a measured 2.4× against a true 3.7× ratio, and it does not**: there is no marker,
  no before/after pair on screen at once, and nothing to measure the moving edge against —
  no viewer extracts a number from it. Cleared, recorded so it is not reopened at gate two.
- **NO RAIL — clean.** 18 sheet cells + 26 sampled frames: no chapter title, no scene
  counter, no slide number. s61's mark column appears on one scene for 5.65s and carries no
  active/inactive state, so it is not a counter; a rail is persistent and nothing here is.
- **Drawn-layer density: 2 in a 16-scene chapter.** Cap is 4 (`vector_art.lottie.max_per_chapter`);
  box item 9 calls 3–4 in a 12–14 scene chapter the top of the range. Comfortably under. I am
  **not** opening a third front on the six figure-over-photo scenes — §8 declares this
  chapter's budget and round 1 already declined it.
- **Last scene carries a bare duration.** s68 `data-duration` 7.096 = `data-framings` 7.096,
  no transition tail. Correct.
- **Ground temperature still moves and still lands where the argument turns.** s57/s58/s59
  are the three coldest in the video running into peak 2, s61 snaps to the hottest frame in
  the video (#3b1219) for the gap, s67 to green for rung five. Archetype strip is
  A,A,B,C,D,D,B,B,B,B,B,D,A,C,B,B — the five-B run is the payoff argument held deliberately
  (box item 1), and s57 and s61 are now the two non-`centred` scenes, so the strip is less
  monotonous than round 1's 15-of-16.

## Would I keep watching?
**Yes, and I no longer have a leaving point to name.** Round 1's was 73.1–80.4s (s64) and it
is closed — that beat is now the chapter's thesis on three large centred chips instead of
three pills in a corner, and the frame's information density went from the lowest in the
chapter to mid-pack.

The softest remaining stretch is **53.0–57.5s (s61 before its headline)**: 4.5 seconds of a
soft, shallow-focus bowl of eggs carrying a kicker and a disclaimer about decimals. I am
**not** raising it as a finding — the +4.55 anchor is measured against «roughly» in the VO
and the payoff word is where the sentence puts it, which is the same structure I passed on
s59 in round 1. Finding #3 names the one cheap thing that would improve it if the scene is
ever reopened anyway.

The first six seconds are unchanged and still strong. The chapter still ends on $7,271,759,
closing its own argument into the recap — right for the last chapter before PEAK-END.

## Regressions vs my last pass
**None.** All five of round 1's "must not break" items re-verified on this encode:
- **s55's `.mega`** — `ABOUT 1%` intact at t=17.60, still the largest type in the video,
  still on the RATE, still over the two-read source foot. Untouched.
- **s54 is still the floor** — 23.42, separation 3.23 to the next scene. Nobody lifted it.
- **s67's measure bar** — re-measured at t=98.06: fill **x500–1419 = 920px**, rows 910–916,
  7px tall. Pixel-identical to round 1. scaleX 1.0000.
- **s59's cue chain** — ladder unchanged (0.30 / 0.80 / 3.85 / 0.80, tail 1.63 on a 7.383s
  body); s59's luma moved only 0.57 (26.84 → 27.41), inside the instrument's noise.
- **The two swap points** — both still fire; s56/s56.2 and s67/s67.2 are visibly distinct
  framings on the sheet.
Nothing that was working came back broken, and the two repairs did not touch a third scene.

## What is working — the next pass must not break these
- **The s61 device is the right answer to the right problem.** Squares over ovoids, identical
  fill, four-and-one, no scale and no numeral, on the hottest ground in the video, with the
  photograph's cardinality matching the marks. Do not add a numeral, do not make them discs,
  do not add a track or a baseline, and do not "restore" §10's crate rhyme.
- **s64's `centred` chips.** This is now the clearest frame in the chapter and it lands on the
  chapter's thesis. Do not put it back in a corner.
- **Everything round 1 listed** — s55's `.mega`, s54 as the floor, s67's 920px bar, s59's cue
  chain, the two swap points. All five re-measured above; the list carries forward unchanged.
