# review · passive-income-number · en · chapter 4 · attempt 1
VERDICT: PASS
PASS 1: 0 blockers, 1 should-fix
PASS 2: 0 blockers, 1 should-fix

Sheet built once (`tools/chapter_sheet.py`) and read as a grid, then 24 frames sampled from the
encode `renders/DRAFT-ch4.mp4` (2619 frames / 87.317s / 30fps, 0 black stretches ≥0.4s, 0 `₹`).
All luma below is MEASURED ON THE ENCODE by me, one frame per scene at the sheet's own sample
times — not inherited from fin-assets. Ranks are read under `separation_not_rank_2026-08-09` §2
(band = 1.0 luma point).

## The three ruled questions — NOT re-opened, and the two left to me are SETTLED

**s44's floor — not re-opened, and my own measurement corroborates the ruling.** s44 median 20.0,
next-lowest s48 26.0: alone at the bottom by **6.0 points** against a 1.0 tie band, so the §3
outlier limb does fire on my numbers too. Ruled NO FIX under
`outlier_limb_is_subordinate_to_the_invariant_2026-08-10` and I am not spending a round on it.
Recorded because it is the useful half: **§1 is maximally satisfied here.** Everything that must
be READ sits above the floor — s41 `$1,500,000` #3 on median / #2 on p10, s42 #1 on p10,
s50 `13.84%` mid-pack at 32.0/17.0 — and s48, the mechanism beat the ruling protects, sits at
26.0 inside a three-frame band with s49 (27.0) and s46/s52 (29.0), i.e. **not** the floor and not
an outlier. There is no inversion between argumentative weight and legibility anywhere in the
chapter.

**s45's sound-off question — SETTLED ON THE ENCODE: PASS, no fix, no fetch, no storyboard change.**
The build instruction worked. At 36.0s and 38.5s the phone is pushed hard right and clipped by the
frame edge; the thumb and the heel of the hand carry the left-centre mass, and the dark screen is
graded down into the vignette rather than reading as a lit empty rectangle. Sound-off a viewer
names *a hand holding a phone* — a concrete object — not *an empty screen*, so the frame supports
«somewhere on your feed» as the feed's vehicle rather than contradicting it. The three chips
(`10% · 12% · "monthly income"`, speech-anchored at +2.67/+3.57/+5.31) carry the content, and
correctly **nothing is drawn on the glass**. Observed and NOT a defect: the physical home button is
legible, which is a design cue and not a wordmark, and fin-assets already cleared the glass at 10×.
`chapters.en.4.s45_accepted_with_the_sound_off_question_left_open_2026-08-10` can be closed.

**The tank at 4.7 — SETTLED: reads as a tank, and the level is unmistakably DECORATIVE. No
`no_return_promise` violation.** Sound-off, at 40.5 / 42.5 / 44.5 it is an open-topped vessel —
two 22px walls and a floor — with an inflow at the left and a tap (outlet, down-turn, stem,
crossbar) on the vessel's *own* right wall, and a stream that broadens. Nameable as a tank.
On decorative-vs-measurement I checked the source, not just the picture: `#s46-art` carries **no
tick, no scale, no numeral and no ghost of the previous level**, and the water is TWO rects where
the upper slice EXITS (`exit("#s46-lvlx", +2.45)`) rather than one rect sliding — so the change
reads as a state and not as a distance travelled down a scale. There is nothing on screen a level
could be measured against. Rule 8 is satisfied the strong way: a photograph of a standpipe cannot
assert that there is a FINITE VESSEL behind the tap, and finiteness is the whole beat.

## Findings
| # | pass | scene/span | severity | what | why it fails | fix |
|---|------|-----------|----------|------|--------------|-----|
| 1 | P1 | s49 | should-fix | the yield fraction's three bars are unlabelled, and the bottom bar DOUBLES directly under a statement whose third clause is "Smaller tank." | The type reads `Same payout. Smaller price. Smaller tank.` and the art reads bar-1 unchanged, bar-2 halved, bar-3 doubled. Two of three map perfectly onto the words, which trains the eye to map the third — and the third inverts. The quotient is the YIELD, the words' third item is the TANK, and nothing on screen says so. The proportions themselves are CORRECT (`den ×0.5 ⇒ quo ×2.0`, storyboard §8) — this is a labelling failure, not an arithmetic one | one micro-label on the quotient (`YIELD`) or drop `#s49-quo` and let the fraction assert only what §8 says it exists to assert — that the payout did not move. **Do not spend a round on it**: batch it into the pre-assembly pass that is already reopening en compositions for `owed.en_ch2_s10_tank_layer` |
| 2 | P2 | s47–s48 (46.0–58.2s) | should-fix | 12.9s of two consecutive `art-off centred` scenes, same geometry, same register, both near the bottom on p10 (22.0 and 16.0), between the tank and the fraction | This is the chapter's one flat stretch and it sits immediately after its strongest beat. s48 is additionally the murkiest frame-to-line fit in the chapter — a hanging herb scale with ONE pan under «payout DIVIDED BY price», where the storyboard asked for a two-pan balance with one pan dropped, so the asymmetry that carried the idea is gone | ⚠ **the fix is NOT drawn art.** §8 refuses 4.8 (a depletion schedule this video has no source for) and the storyboard declares s48 `art off · ctr Y` — asking for either would be a finding about the review. The only lever that contradicts nothing is a `background-position` on `#s48-bg` to lift the pan and chain out of the murk into the lower third. One string, same batch as #1 |

## Would I keep watching?
Yes, and the first six seconds are the strongest opening of any chapter I have seen on this cut:
a $20-bill macro, a gold count-up landing on `$5,000 A MONTH`, and a line that names the figure
before it justifies it. The green peak at s41/s42 is properly built — the count-up to `$1,500,000`
lands at +4.95 on its own spoken word, the ladder bar fills to 0.764 with it, and s42 picks the
push up tighter on the dial with the bar HELD, so the formula completes across one unbroken shot.
The turn into red at s44 is legible as an argument turning and not as a palette change.

The timestamp where attention is at risk is **~0:50 (s48, 52.2–58.6s)** — finding 2. It is the
chapter's mechanism beat and its declared 5:00 beat, and it is carried by type over the frame with
the least to look at, one scene after the tank has just spent the viewer's attention. It recovers
immediately at s49.

The chapter closes a loop rather than opening one (`A very big yield is very often a very small
price.`). Noted, not raised: 4.13 is a locked verdict line, the `pop`/back.out slam is the declared
§2 device for it, and in the assembled cut ch5 follows across a 0.45s dissolve, so there is no gap
for a viewer to leave in.

## Regressions vs my last pass
n/a, attempt 1.

## What is working — the next pass must not break these
- **The s41→s42 matched-frame HOLD is correct and built right the first time.** Verified across the
  joint at 14.60 / 15.02 / 15.60: s41 holds wide, s42 resumes visibly tighter on the handwheel
  (`s42.jpg` is a real `crop=1600:900:280:186` derivative, md5-distinct, 1.18× in), and the measure
  bar holds 0.764 across the joint without re-animating. It reads as one push, not as two files
  dissolving. This is what s3/s4 cost three rounds to learn — do not "tidy" it.
- **Every figure is traceable and every assumption is on the frame.** `$6,545`, `4.21% / 4.19%`,
  `13.84% June 1932` and `multpl.com, read 5 Aug 2026` all match `facts-staging.md` (rows 201, 204,
  214); `$60,000 / 0.04 = $1,500,000` is stepped and carries `ILLUSTRATIVE ARITHMETIC`; the ladder
  bar's 0.764 is `1,500,000 / 1,963,375` and 1,963,375 derives from the ANNUAL `$78,535`, not from
  the rounded monthly. `derived_income_carries_assumption` and `no_return_promise` both clean.
- **s50 refuses to fabricate.** The newsprint resolves no headline, no date and no word anywhere in
  the encode, on the one frame whose foot names 1871 and 1932, and `13.84%` takes a bare `pop`
  rather than a count-up (which would have rounded to `14%` — a different figure from the one the
  foot cites). Declaring the scene DRY so a June-1932 yield is not sold as a prize is the right call.
- **The three inherited gate questions all clear.** (a) `s48` is **not** a duplicate — verified by
  md5: the byte-identical twin is `hi-ch1/assets-ch1/style-a/s7.jpg`, and hi ch1's LIVE composition
  references `assets-ch1/final/s7.jpg`, which is a different file (`699ef5b0…` vs `35ff3cb0…`), so
  it ships in exactly one place. (b) `s51`'s distinct front-row faces are **not** a defect: it is
  the NARA/Wikimedia public-domain Chicago breadline, Feb 1931, the exact event the line names, and
  the faces are what makes the frame land. The frame asserts no date, so the Feb-1931 photograph
  under a June-1932 figure overclaims nothing. (c) both `⚠ REQUIRED` build instructions are applied
  and verified in the emitted HTML — `#s40-bg background-position:center 35%` and `#s51-bg
  background-position:center bottom`.
- Craft clean: first cue at +0.30 on all 13 scenes, every ladder gap ≥0.80s, `data-framings` matches
  every duration, s52 carries a bare duration, no type collisions, no md5 duplicates inside the
  chapter, NO RAIL, `$` only.

## Notes (taste — do NOT spend a round)
- `payoff clause 4`: fin-assets predicted the s40→s41 median step at **+8.5**; I measure it at
  **+1.0** on the encode (34.0 → 35.0). Still non-negative, and inside the 1.0 tie band either way,
  so the clause is satisfied — but it is the sixth time on this run that a predicted composed number
  missed the encode by a wide margin, in this case by 7.5 points. `p90 − p50` beside the median, as
  asked: s40 18 · s41 **15** · s42 14 · s43 13 · s44 17 · s45 12 · s46 19 · s47 12 · s48 19 ·
  s49 21 · s50 20 · s51 16 · s52 11.
- s46 is the SHORTEST scene in the chapter (4.744s hold) and carries its most complex mechanism,
  assembled by +2.95 — so the tank is fully formed for under two seconds. Not fixable here (the 4.7
  clip is voice-locked at 3.944s) and it is the right architecture anyway: the slow build belongs at
  2.2, which `owed.en_ch2_s10_tank_layer` is already going to draw on a 10.596s scene.
- s46's drawn inlet overlaps the photographed standpipe's own downpipe, so at contact-sheet size the
  vessel's left wall and the pipe merge into one shape. Reads fine at full size.
- s50's foot lands 1.95s before the figure it defends, leaving a visible gap mid-frame from ~67.7s
  to ~68.9s. Declared and deliberate (provenance first). Correct call, slightly awkward frame.
- Density is 2 drawn layers in 13 scenes against a cap of 4. That is healthy, not thin — rule 9 says
  3–4 is the top of the range and the approved ch1 ships one. I am not asking for more.
