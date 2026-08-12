# review · passive-income-number · en · chapter 5 · attempt 1
VERDICT: REWORK
PASS 1: 1 blockers, 2 should-fix
PASS 2: 0 blockers, 1 should-fix

Read from ONE sheet (`renders/SHEET-ch5.jpg`, 18 cells, s53–s68 + the two swap
framings), then 30 sampled frames from the ENCODE `renders/DRAFT-ch5.mp4`. No verdict
below quotes an assets- or build-stage rank table.

## The three questions the build left open — all three settled here, on the encode

**1 · PEAK 2 (s59, 5.7, `$5,555,556`) — PASS, not a blocker.**
Measured at t=44.9 (count-up complete). The figure renders at the *identical* geometry
to every other `.huge` payoff in the chapter — ink band y535–634 (100px tall), x677–1244
— pixel-for-pixel the same box as s63 and s68. Glyph-core against local ground:
**4.97:1** (glyph RGB 247,87,71 · ground 43,28,31), clearing WCAG AA-large (3:1) and
AAA-large (4.5:1). Peers on the same instrument: s68 5.34, s66 6.49, s63 7.90. s59 is
lowest of the four, but s59↔s68 separates by 0.37 and both are the same `--warn` red on
the same class of dark ground — inside the noise of the instrument, so not a rank claim.
Cue chain: rate +1.10, count-up +4.95 running 1.20s → completes +6.15 against a 7.383s
body, **1.23s of settle before the cut**; foot +5.75. The build's predicted three-of-four
limb failure does not reproduce. Seventh measurement of the prediction-vs-encode gap on
this run, and again it did not favour the prediction.

**2 · The floor (s54) — discharge UPHELD, on measurement, not on construction.**
Encode luma, 3 frames per scene, dissolve zones excluded:

| rank | scene | mean | median |
|---|---|---|---|
| 1 (floor) | **s54** | **23.52** | 12.00 |
| 2 | s67 | 25.50 | 22.67 |
| 3 | s62 | 26.09 | 21.00 |
| 4 | s59 | 26.84 | 25.00 |
| 5 | s58 | 29.33 | 26.67 |

s54→s67 separates by **1.98 points**, outside the 1.0 band, so s54 is genuinely and
uniquely the darkest frame — a real floor, not a tie. (Build predicted 7.66 composed
points; encode measures 1.98. Rank holds, magnitude does not.)

Now the hard half — what 5.2 *asserts*. Nothing. No figure, no rate, no source, no
comparison, no cascade, no measure bar. `DIVIDENDS ONLY` names the route and *"A real
strategy. With a real price tag."* is a promissory signpost that 5.3–5.7 then pay in
full. Its only rivals for emptiest beat are 5.6 (*"Change only the rate"* — states the
method) and 5.13 (*"The whole month"* — redefines the denominator), and both sit well
above the floor (s58 29.33, s65 40.50). **No inversion anywhere**: the three frames
next-darkest after s54 — s67, s62, s59 — each carry a figure, a rate and a sourced foot,
and all three sit ABOVE it. Any lift of s54 relocates the floor onto s67 ($1,963,375 +
the full-scale measure bar), s62 (ABOUT 3% + its three-read source) or s59 (PEAK 2) —
a MORE substantive beat into the darkest frame, which is FORBIDDEN. And s54's own type
is the most legible in the chapter (white on near-black, nothing to lose). This is the
invariant WORKING. No finding, no fix, no knob spent.

**3 · Comma clearance (s68 `$7,271,759`, `.huge` 112px over a 26px foot) — PASS, measured.**
At t=105.5: number ink lowest row **634** (digit baseline 625; the two comma tails run
626–634), foot ink topmost row **662**. Clear space **27px** at 1080p — wider than the
foot's own 25px ink height. Peer on the same class: s63 `$1,929,260` (also `.huge`, also
two commas) measures 635 / 662 = **26px**, so s68 is *not* this chapter's tightest — s63
is, by 1px, i.e. they are the same within measurement, and both clear. No collision, no
clipping, no fix. `comma_fix_protects_the_wrong_class` remains true about the fix's
scope, but at 112px the `.huge` comma descender does not reach the foot on either frame.

## Findings
| # | pass | scene/span | severity | what | why it fails | fix |
|---|------|-----------|----------|------|--------------|-----|
| 1 | P1 | s61 (5.9) | **blocker** | the photograph is not "four crates against one" — `assets-ch5/final/s61.jpg` is a ~14-crate block against a wall with one low crate at the right end, and the default-centre cover crop + ken push that lone crate to the frame edge, so the shipped frame reads as an undifferentiated crate wall with no count in it at all | storyboard §8 declines drawn art on 5.9 **on the explicit ground that "the photograph is four crates against one"**. That premise is not what shipped, so the beat that IS the chapter's argument — `ROUGHLY 4 TIMES` — is carried by type alone with the picture contributing nothing. Compounding: §10 declares the crates as a three-beat visual rhyme (s61 four-against-one → s75/s76 a line of five increasing → s77 one far larger, alone); if s61 never establishes the count, the ch6 recap rhymes with nothing. This is a selection defect that escaped `fin-assets` | re-frame first, it is the cheap fix: set `background-position` on `#s61-bg` and re-cut the ken so a countable near group AND the isolated crate are both in frame for the whole scene (the lone crate sits at roughly x 0.48–0.63, y 0.36–0.47 of the source). If no crop of this file yields a readable 4-vs-1, **it needs a new fetch** — I have not opened a substitute and am naming none. ⚠ Do NOT solve this by adding drawn art; §8 declined that by name and this cut's declared drawn device is the measure bar, which §9a rules off this frame |
| 2 | P1 | s64 (5.12) | should-fix | two faults, one fix. (a) the photo is not "three parallel painted lanes converging" — it is a top-down of 5–6 lanes carrying a left-turn arrow, two straight arrows and two merge arrows, so "three routes" is nowhere in the picture; (b) the scene is `art-off` **and** not `centred` (storyboard `ctr: N`), so the three chips sit in the top-left corner and ~70% of the frame is empty asphalt | box item 7: once `.art-off` retires the drawn layer the split is a hole. §7 gave 5.12 `ctr: N` on the assumption of a photograph that would sit *beside* the chips; this photograph does not, so the declared layout is holding nothing. It lands on the chapter's thesis line — *"the rate you assume is the entire difference"* | add `centred` to s64 — box 7 prescribes exactly this once art is off, it keeps the three chips, adds no drawn layer and contradicts no declared device — and re-frame the ken onto three adjacent straight lanes so the picture at least reads as parallel routes. No new asset needed for (b) |
| 3 | P1 | s57 (5.5) | should-fix | the tank callback has no tank. 4.7 (s46) now carries a DRAWN tank (`en_tank_becomes_a_drawn_layer_2026-08-10`); 5.5 is *the same tank at a smaller tap* and ships `art-off centred` over a photograph of a galvanised tub with a small wall valve above it — **no visible stream at all**, no cup, and no vessel that reads as the s46 tank | the VO says *"same tank"* and the kicker says `SAME TANK, SMALLER TAP`; neither the tank nor the tap change is in the frame. ch4's own s46 comment records this against you by id — `chapters._carry_forward_en_ch4_to_ch5_s57`: "§10's four-frame flow ladder has nothing left to escalate DOWN to at 5.5". A drawn layer is in-family on **en** (`chapters.hi.4.s40_measure_bar_declined_2026-08-10` runs the other way on this cut) | give s57 the same `v-tank` layer at a narrower tap — `art-forward` on a `.band` at z-index 0 under the plate (rule 9), decorative level only, and the four s46 prohibitions carried verbatim: no tick marks, no scale, no numeral, no ghost of the previous level (`no_return_promise`). ⚠ **If the pre-assembly pass that owns `owed.en_ch2_s10_tank_layer` is running anyway, s57 belongs in that batch** — it is the third tap position of the same device and re-rendering ch5 twice for it would be waste. Route it there in preference to a ch5 round |
| 4 | P2 | s64 (5.12) | should-fix | this is where I would leave — see below. Same fix as #2, filed here because the cost is retention, not craft | after the payoff run ends at s63, the chapter's thesis line arrives at its lowest information density: three ~28px pills in a corner over an empty murky frame, unreadable at 1.5× on a phone | discharged entirely by finding #2. No second render |
| 5 | P1 | s59 (5.7) | note | §9c limb 3 declares "the calmest, emptiest photograph in the cut — a bare warehouse floor, one pallet, wide." Shipped is a loading bay: a tall pallet stack filling the left third, an EXIT sign, wall signage, a roller shutter | the declared device and the photograph disagree — but the number wins the frame on measurement (4.97:1, above) and nothing is false or unreadable | leave it. Taste, and it costs no viewer. Recorded only so nobody re-litigates it at gate two |
| 6 | P1 | s60 (5.8) | note | the stmt line breaks as `$1,500,000 AT 4.0% ·` / `$5,555,556 AT 1.08%`, leaving the `·` separator orphaned at the end of line one | typographic wart, not a defect | if s60 is touched for any other reason, drop the trailing `·` or move it to the head of line two. Not worth a render on its own |
| 7 | P2 | s62 (5.10) | note | giant wooden numerals stand in for "a printed fund factsheet". Generic — it says "figures", not "high-dividend fund" | does not argue with its line, and the never-a-screen/never-a-document override in §D11 plausibly forced it | none. Recorded so a future cut does not repeat it by default |

## Everything else I checked, and where it landed
- **§3c NO RAIL — clean.** 18 sheet cells + 12 sampled frames: no chapter title, no scene
  counter, no slide number. The only persistent mark is the channel watermark.
  s67's `THE LADDER` label is §9a's declared measure-bar label, not a rung count.
- **The measure bar is exactly right.** s67 measured on the encode: fill x500–1419 =
  **920px** at 7px tall, rows 910–916, centred on `calc(50% - 460px)` — scaleX 1.0000,
  the full-scale rung-five value §9a declares. Its deliberate ABSENCE on s59 is correct
  ($5,555,556 would need 2,603px on a 920px track) and I am not raising it.
- **Every figure carries its assumption** (`no_return_promise` /
  `derived_income_carries_assumption`). `$5,555,556` → AT A 1.08% DIVIDEND YIELD +
  "$60,000 divided by 0.0108 · ILLUSTRATIVE ARITHMETIC"; `$1,929,260` → AT A 3.11% YIELD
  + illustrative; `$1,963,375` → AT A 4.0% WITHDRAWAL RATE + illustrative + $6,545 a
  month; `$7,271,759` → AT A 1.08% DIVIDEND YIELD + illustrative; s60 carries both rates
  as inline spans; `ABOUT 1%` / `ABOUT 3%` carry their two- and three-read sources;
  `$78,535` is a published BLS figure and correctly carries a citation rather than a
  rate. **Zero bare numbers.**
- **Arithmetic re-derived against `facts-staging.md`.** 60000/0.0108 = 5,555,555.6 ✓ ·
  60000/0.0311 = 1,929,260.5 ✓ · 78535/0.04 = 1,963,375 ✓ · 78535/12 = 6,544.6 ✓ ·
  78535/0.0108 = 7,271,759.3 ✓. **`ROUGHLY 4 TIMES` is honest**: the true ratio is 3.70×
  (4.0/1.08), and facts-staging line 232 authorises it verbatim — *"Safe to show as
  'roughly four times'. Do not speak '3.7' — it is a ratio of two SOFT decimals"* — which
  is precisely what the frame and the VO do. The `$1,833,750` visible on the s63 sheet
  cell is a mid-count-up frame, not a wrong figure; the settled value is `$1,929,260`.
- **Cue ladder clean on all 16 scenes.** First cue at +0.30 everywhere (≤0.5 ✓), no gap
  under 0.8s anywhere, and the last cue leaves ≥1.59s of tail on every scene. s68 carries
  a bare `data-duration` 7.096 = `data-framings` 7.096 with no transition tail — correct
  for a chapter's last scene. Both declared swap points fire and both use genuinely
  different files (s56/s56b and s67/s67b are md5-distinct).
- **Ground temperature moves and lands where the argument turns.** Built grounds match
  §7 row-for-row, and the three coldest in the video — `#131f2c` → `#0e1c2e` → `#0c1a2c`
  — run s57→s58→s59 straight into peak 2, then s61 snaps to `#3b1219` for the gap and
  s67 to `#12351f` for rung five. §2.6's temperature question passes on measurement.
- **Flat-strip check, and why it is NOT a finding.** 15 of 16 scenes are `centred` stacks
  at one geometry. Read as a strip that is monotonous — but ch2 (11/15), ch3 (14/16) and
  ch4 (10/13) shipped the same way and are locked, §7 declares the `ctr` column per
  scene, and box item 7 forbids fixing flatness by adding layouts. The correct remedy is
  to give scenes something real on the other side, which findings #1–#3 do on the three
  frames that actually have something to hold. I am not opening a fourth front.

## Would I keep watching?
Yes, and the chapter earns its place — but there is one clear leaving point and it is
**73.1–80.4s (s64, line 5.12)**. The payoff run s59→s63 is genuinely good television:
the shove into peak 2, the count-up on an empty room, then the two-number comparison and
the middle route. Then 5.12, which is the chapter's *thesis* — "the rate you assume is
the entire difference between them" — arrives as three small pills in the top-left corner
of a murky, 70%-empty asphalt frame. That is the lowest information density in the
chapter landing on its most important sentence, immediately after the adrenaline stops.
Fix #2 and the drop closes.

The second risk, 25.2–43.1s (s57→s58→s59), is ~18 seconds of three cold near-empty
frames before peak 2's number lands, and I am explicitly NOT raising it: §9c declares
the temperature approach ("the drop is a temperature event before it is a number") and
the 4.95s hold before the count-up is dictated by the VO's own word order — the payoff
word is the last word of the sentence. That is the device working, not a defect. Fix #3
would make that stretch materially stronger by giving s57 something to watch.

The first six seconds are strong: s53 opens on the title's own question with the kicker
in at +0.30, warm amber against ch4's closing red, and the line *"Spend only what it
pays. Never sell a share."* is the thing the viewer clicked for. No note there.

The chapter ends on `$7,271,759` — the largest figure in the video — over a chain fence
at dusk. It closes its own argument rather than opening a loop, which for the last
chapter before a PEAK-END recap is the right hand-off, not a fault.

## Regressions vs my last pass
n/a, attempt 1.

## What is working — the next pass must not break these
- **The `.mega` on s55.** `ABOUT 1%` at ~1490px is the single largest type in the video
  and it lands on the RATE, not on a corpus. §9c's whole argument for why peak 2 lands
  depends on that ordering. Do not shrink it, do not move it, do not add a second `.mega`.
- **s54 is the floor and must stay there.** It is measured, it is the emptiest beat, and
  every lift relocates the floor onto a figure-bearing frame. Any attempt to "improve"
  s54's exposure is a regression, and I will call it one.
- **The measure bar at s67** — 920px, scaleX 1.0000, the top of a five-frame climb the
  viewer has watched assemble since 2.13. One arithmetic, numerator and denominator are
  a pair (gotcha 7). Do not touch the track or the fill while fixing anything else.
- **s59's cue chain.** Count-up completes 1.23s before the cut and the number lands just
  ahead of the spoken words. Nothing about the s59 fixes above should move that timing.
- **The two swap points** (s56 at +2.50, s67 at +4.80) both fire on real second files.
