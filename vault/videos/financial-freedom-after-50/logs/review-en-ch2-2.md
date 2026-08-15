# review · financial-freedom-after-50 · en · chapter 2 · attempt 2
VERDICT: PASS
PASS 1: 0 blockers, 4 should-fix
PASS 2: 0 blockers, 2 should-fix

Sheet rebuilt this pass: `studio/videos/financial-freedom-after-50-en-ch2/renders/SHEET.jpg`
(19 cells, s12–s28, two-framing cells for s12 and s23), from `renders/DRAFT-ch2.mp4`,
108.672 s encode / 108.659 s root. 11 additional frames sampled from the **encoded mp4**
at 15.6 / 17.8 / 22.5 / 26.5 / 31.5 / 39.6 / 66.5 / 69.5 / 105.0 / 107.0 s.

## Attempt-1 blockers — all four verified fixed on the encode

| row | scene | verdict | evidence |
|---|---|---|---|
| 1 | s17 cue order | **FIXED** | Frame @39.6 s carries the full ladder: `WORKING AGAINST YOU` → **North of 20%** → `VERIFIED · FEDERAL RESERVE G.19 · AS OF AUGUST 2026`. `index.html:336-337` — `pop("#s17-num", 37.991)`, `fade("#s17-foot", 38.991)`. Gaps 3.206 / 1.000, both ≥0.8; first cue still +0.30. The **num did not move** — the build slid the foot instead, which is exactly what I asked for and keeps the pop on its voice anchor. The 1.4 s of an attribution citing a hole is gone. |
| 2 | s15 selection | **FIXED** | Rusted pipe with a **curtain of drips** falling into grass. Verified at 22.5 s and 26.5 s: the drips are individually legible at composition scale, and the source is colour (green grass, yellow flowers survive the grade). The frame now says *water escaping where it should not*, which is the beat — the old puddle-by-a-drain said water *arriving*. Storyboard's test (*"the leak must be legible, not implied"*) is met. |
| 3 | s22 selection | **FIXED, and it is now one of the best frames in the chapter.** | Verified at 66.5 s and 69.5 s: a snow roller mid-slope with a **long track sweeping across the hillside behind it**. The track is the assertion and it is unmissable. Sound-off it reads *momentum*, not *Christmas*. Licence: `assets-ch2/final/CREDITS.txt` carries `s22.jpg · commons.wikimedia.org/wiki/File:Snow_Roller_in_Rocky_Mountain_National_Park.jpg · by Perduejn · CC BY-SA 4.0`. The credit row **is present** — see P2-6 for the one thing still owed on it. |
| 4 | s28 grade | **FIXED** | Verified at 105.0 s and 107.0 s: the man, the glasses, the mug, the sweatshirt, the porch posts and the daylight foliage through the left window all read. `index.html:272` inline `grayscale(0.32) brightness(0.92) contrast(1.05)` — grayscale and contrast restated unchanged, brightness the only moved value, 0.00% clipping. Wide ken `plateKen(0.90→0.98)` holds the daylight in frame for all 5.998 s. Mean luma @105 s is 38.9 (was 36.0) and the subject-level lift is larger than the mean lift, which is the right shape. The SHOVE #1 frame is no longer wasted. |

**The two declines are both correct and I am not re-litigating either.**
- **No drawn layer at s15.** Rule 8. A drawn leaking pail over a photograph of water escaping a pipe is a second drawing of the subject — it asserts no proportion, comparison, measurement or count. The build's reasoning is right, and it correctly held the density budget I already spent by name on s21 and s25.
- **s14's ken re-frame is genuinely not implementable.** I verified this in the file rather than taking it: `assets/js/motion.js:133-137` `ken()` hard-codes `xPercent: -2.5 → +2.5`, and `plateKen()` (`:256-259`) is scale-only. There is **no horizontal lever on a `.bg`**. My attempt-1 row 5 asked for something the system cannot do; that is a finding about my review, not about the build. Restated below as P1-1 with a lever that *does* exist.

## Findings
| # | pass | scene/span | severity | what | why it fails | fix |
|---|------|-----------|----------|------|--------------|-----|
| 1 | P1 | s14 (15.2–21.2 s) | should-fix | the darkest frame left in the chapter, under the kicker `THE BUCKET`. At 15.6 s the galvanized bucket reads cleanly; by 17.8 s the push has cropped its rim and it competes with a wooden barrel at centre-right. Mean luma 35.9 at 18 s — the chapter's floor | **new measured evidence, not a re-file:** s14.jpg source mean luma is **53.96**. s28.jpg is **53.81**. They are the same photograph brightness, and the build's own note says a source at that level *"crushes against a grade calibrated for the median (~105)"* — which is why it lifted s28 and left s14 at the locked 0.62. s14 is the last instance of the class the build just fixed. Not a blocker: the bucket does read at the wide end of the ken, and the barn register is coherent with the cold leaks run | the build already armed and guarded the lever: inline **`brightness: 0.92`** on `#s14-bg` via the `.bg` emitter in `build.mjs` (grayscale/contrast restated, floor assert already in place). Optionally plus **`background-position: 50% 72%`**, which the build measured as spending s14's 15.6% vertical crop slack on the bucket's base and dropping the empty barn ceiling. Do **not** brief "re-frame the ken" again — it has no implementation |
| 2 | P1 | s25 | should-fix | carried from attempt 1 row 6, unchanged and out of the round-2 brief. On-screen text `3–6 months of ESSENTIAL expenses`; picture is a stack of $50s. The beat is a **COUNT (3 of 6)** and the count is on screen in no form at all | sound-off the frame says "money", which is true of half this video. The storyboard's own answer to this count was a photograph that shows it | fetch the declared frame (six envelopes/jars, three visibly fuller) **or** a drawn 3-of-6 band in the D plate. If drawn: schematic, a count only, no dollar amounts, and the `OPINION / CONVENTION` foot stays exactly as it is |
| 3 | P1 | s21 | should-fix | carried from attempt 1 row 7, unchanged. Five ticked checkmarks under *"The freed payment goes to the next line."* | checkmarks assert *done*; the line asserts *transfer*. The roll-down is the mechanism the whole snowball rests on and it is the one thing the frame does not show. Also breaks the same-legal-pad continuity the script wanted with s20 | a single drawn arrow from one row to the next over the existing pad, in the C plate. Additive (the photograph cannot say *moves to*) and cheaper than a re-fetch |
| 4 | P1 | s24 | should-fix | carried from attempt 1 row 8, unchanged. A corridor of safe-deposit boxes under `THE WORST OPTION · Never the retirement account.` | a vault reads as somewhere money is **safe** — the opposite of the line's warning. Only 3.9 s and the type carries it, which is why it is still not a blocker | a statement/withdrawal form on a table, figures illegible (the storyboard's own slot). **New fetch** — I have not opened any candidate file, so do not treat any filename as verified |
| 5 | P2 | s19–s21 (46.5–62.8 s) | should-fix | **the flat stretch has moved, not vanished.** Attempt 1's 15–34 s run is genuinely fixed — s14→s15→s16 now reads brown → dark green → hot ochre and s16 introduces the chip row. What is left is **16 s of three consecutive pale-warm paper close-ups**: hand writing, legal pad, marker on checked circles. Luma 42.7 / 43.8 / 55.7, same geometry, same register, same kind of picture | this is the only place left where three scenes in a row change nothing but the words. It is where I would leave, if I left | **not more layouts.** It resolves with P1-3 alone: give s21 the roll-down arrow and one of the three scenes is doing something the other two cannot. With P1-2 as well the chapter goes from one drawn layer to three, inside the 3–4 ceiling. Do not manufacture a fourth |
| 6 | P2 | s22 | should-fix — **for `fin-package`, not for `fin-build`** | the CC BY-SA 4.0 attribution lives only in `assets-ch2/final/CREDITS.txt`, which is a repo file. Nothing in `tools/format/*.json` or the package pack requires photo credits to reach the video description | attribution is a **licence condition** on this file, not a courtesy. Every other image in the chapter is Pexels (no attribution required); s22 is the only one with an obligation, so there is no existing habit that would catch it. Not a chapter defect and not worth a render — the picture is correct and the row exists | `fin-package` must carry the `CREDITS.txt` rows (at minimum the s22 row: *Snow Roller in Rocky Mountain National Park, by Perduejn, CC BY-SA 4.0, via Wikimedia Commons*) into the YouTube description. Worth closing as a default in the package stage rather than as a note on this cut |
| 7 | P1 | s14→s15→s16 | note | the vessel changes three times across one metaphor: bucket → rusted pipe → brass tap. VO 2.3–2.5 says *bucket* and *holes in the bottom* | the storyboard wanted one bucket in three states. `fin-assets` ran 24 cells across 3 pools and no leaking pail exists in stock; the build correctly refused to draw one over the photograph. Each frame does say *leak*, the on-screen type never promises a pail (`TWO HOLES`, not `THE BUCKET`, at s15), and the argument is legible. **Filed as the accepted cost of a search that was actually exhausted, not as work** — there is no executable fix left, and naming one would be inventing it | none. Do not brief another fetch on this run |
| 8 | P1 | s16 | note | the re-pick traded *count* for *leak*: the old frame had two spigots and no drip, the new one has one tap and a visible drip | the right trade. The chips `1 High-interest debt` / `2 No emergency fund` carry the count honestly and always did; *leak* is the assertion no chip can make. Recording it so it is not read as a regression | none |

## Honesty check
Unchanged from attempt 1 and still clean, now with the ordering exception closed.
- **s17** — `North of 20%` · `VERIFIED · FEDERAL RESERVE G.19 · AS OF AUGUST 2026`, and the source
  line now lands **after** the figure. Traces to `facts-staging.md` row 11, which is HARD on the
  shape and SOFT on every decimal; the frame obeys it exactly — no decimal, no period label. The
  VO does not speak the figure.
- **s20** `OPINION — A WIDELY USED METHOD, NOT AN AGENCY RULE` and **s25**
  `OPINION / CONVENTION — THE STANDARD ADVICE, NOT A STATISTIC` are both intact and both correct
  (`facts-staging` §2 forbids an agency card at s25). None of the three foot lines was touched.
- No invented agency, seal or legible figure. Every lettered surface is composition type; nothing
  is lettered by a photograph. No non-US currency, signage or plate.
- Nothing here contradicts ch1 as locked.

## Craft check
- Root `data-duration="108.659"`, last scene `s28` carries a **bare** `data-duration="5.998"`
  (no +0.45, correct — the overlap comes back on concat with ch3). Encode 108.672.
- 17 scenes, first cue on every one at +0.30. No cue-ladder gap below 0.8 s; the tightest is now
  s17's 1.000 s foot, which is the fix, not a symptom.
- `data-framings` intact on both declared two-framing scenes: **s12** `4.7,4.825` (one continuous
  ken on a single file — the near-identical sheet cells are the declared device, not a repeat) and
  **s23** `4.8,4.908` (real photo swap `s23.jpg` → `s23b.jpg`, still fading in under the word *roof*).
- The s18 icon still paints and is still the chapter's only drawn layer. Additive, `warnc`, finishes
  before the cut. **No rule-8 violation anywhere in the chapter.**
- No type collisions, nothing outside the safe area, no `.rail`, no scene counter. `blackdetect`
  clean. Warnings unchanged and still non-defects; `known_benign` is still `[]`.

## Would I keep watching?
**Yes, and the place I named last time is gone.** At 0:21 the screen now shows a rusted pipe raining
a curtain of drips over grass while the voice says the water runs out of the holes — the pictures
confirm the voice instead of contradicting it — and 0:28 opens on hot ochre with the two chips
popping, which is the first real change of temperature in the chapter and it lands exactly where the
argument turns. s17 then arrives with the figure and the citation in the right order, and s22's snow
roller with its track is now the payoff frame the sequence was written for.

**The one place attention is still at risk is 0:46–1:03** — s19, s20, s21, three pale paper
close-ups in a row. It is a soft spot, not a cliff: the voice is doing the highest-rate-first
mechanism there and the lines are concrete. Give s21 its roll-down arrow and it closes.

The chapter still ends on a genuine loop opener — *"Now you can go on offense."* — and it is now on a
frame you can actually see. That is the single biggest gain of this round.

## Regressions vs my last pass
**None.** I checked every item I listed as working in attempt 1 and all five survived:
the temperature arc still turns where the argument turns (and s16's re-pick strengthened it), the
figure discipline and all three foot lines are byte-unchanged, s23's photo swap and s18's icon are
untouched (the `index.html` diff is 5 lines and names neither), and s26/s27 still carry the green run.
The two re-picks did not cost anything they replaced — see notes 7 and 8, which record the two
trades honestly rather than as losses.

## What is working
- **Every re-pick landed and two of them are now among the chapter's strongest frames.** s22's snow
  roller with its track and s16's dripping brass tap over ochre both assert their line sound-off.
  Neither should be touched again.
- **The s17 fix was made at the generator, not at the scene.** `FOOT_AFTER_NUM` derived from the
  focal, plus a build-time assert that reads the times back out of the written `index.html`. That is
  the correct shape — it tests the artifact, and any future anchored+footed scene inherits it.
- **s28's lift used the one knob the grade already exposes and moved nothing else.** brightness
  0.92 with grayscale and contrast restated unchanged, 0.00% clipping, and a guard that refuses any
  inline value below the locked 0.62. The 2026-08-04 rejection cannot come back through that door.
- **The build declined two things for the right reasons and proved both.** Rule 8 on the s15 art,
  and a measured demonstration that no horizontal pan lever exists for s14. I verified the second in
  `motion.js` myself rather than accepting the claim.
