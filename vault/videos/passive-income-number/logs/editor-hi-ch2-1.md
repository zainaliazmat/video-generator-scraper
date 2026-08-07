---
summary: Chapter 2 first review. REWORK on 4 blockers. The hero corpus frame (s15, RUNG ONE, the video's first corpus figure) is a pile of DEMONETISED pre-2016 Mahatma Gandhi Series ₹500 notes - the exact defect storyboard-hi.md §9 names s15 by number and forbids. Three more pictures say the wrong thing: s11 is a pottery-market pile of clay gullaks under "SIP puts in, SWP takes out", s19 is a brickyard of hundreds of blocks under the kicker THE FIRST BRICK, and s17 is a bare ethernet patch lead under "the phone recharge and the home internet". s17 and s19 both break motifs script 7.6 is written to pay off. s11b was checked and CLEARED - those are current stone-grey notes.
updated: 2026-08-07
source: renders/SHEET.jpg (rebuilt), renders/DRAFT-ch2-v2.mp4 encoded frames at 13 sample points, assets-ch2/final/*.jpg at native res, index.html, script-hi.md §Chapter 2, storyboard-hi.md §6/§8/§9, facts-staging.md B.3, run.json constraints
---

# editor · passive-income-number · hi · chapter 2 · attempt 1
VERDICT: REWORK

Reviewed from the rebuilt sheet first, then 13 frames pulled from `DRAFT-ch2-v2.mp4`,
then every `assets-ch2/final/*.jpg` opened at native resolution. **Every image named
below I opened myself**; where I could not identify something with confidence I say so
rather than naming a file to reuse.

The three fixes handed to me are verified good and I did not re-audit them: the s15
comma clearance, the `#s16-afunnel` opacity and s17's ILLUSTRATIVE foot are all correct
on the encode. s16's flat graph-paper background is being re-sourced in parallel and I
reviewed the rest on that basis. No image is used twice in this chapter (md5-checked,
zero collisions).

## Findings

| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s15 | **blocker** | The corpus frame is a scatter of **demonetised pre-2016 Mahatma Gandhi Series ₹500 notes** — pale olive-green, the guilloche rosette disc behind the numeral, ascending serial `6UK 649…`. Not legal tender since 8 Nov 2016. | This is RUNG ONE, the first corpus figure in the video, under `₹10,00,000`. The frame asserting today's money is nine-year-dead currency, and an Indian viewer clocks it instantly. `storyboard-hi.md` §9 names this scene: *"₹ frames must be the current stone-grey ₹500 series — **s15**, s20, s29… A demonetised pre-2016 note is the wrong era and has shipped before."* It shipped again. The composition is also wrong to spec — the storyboard asked for *a small steel cash box, lid open, notes squared inside*; what shipped is a loose heap with coins and a **magnifying glass**, which reads as "investigation", an idea this scene is not about. | **Needs a new fetch.** Current stone-grey MG-New-Series ₹500 only, in a closed/squared arrangement, no magnifier. Use the `#N` offset on `pixabay_fetch.py` (`finance-audit-2026-07-29/index.md` #7) — the demonetised pile is the deterministic top hit for every rupee query and `#1` will return it again. Verify the fetched note against s11b.jpg, which I checked and which **is** the correct current series: side by side the difference is stone-grey vs olive, and no rosette. |
| 2 | s11 | **blocker** | Under *"एस आई पी में पैसा हर महीने अंदर जाता है"* / **SIP puts in. SWP takes out.** the picture is a wholesale pile of ~30 unsold clay gullaks at a pottery market. | Sound-off with the text stripped this says *"piggy banks for sale"*. There is no money, no hand, and nothing going in. It is also the wrong register — a gullak is a child's coin jar, not a monthly investment plan. And `storyboard-hi.md` §6 declares the device: the swap is *"**the same steel box**, a note being drawn out"* — one container, filled then emptied. What shipped is a pot market at +0.0 and an unrelated man counting cash outdoors at +3.30, so the IN→OUT contrast the swap exists to make never lands; it reads as two stock photos. | **Needs a new fetch for s11 only** — keep s11b, it is a good frame and the currency is correct. Fetch the same-object partner to s11b: a hand pushing a note **into** a slot, shot on the same kind of container and in the same warm outdoor light so the pair reads as one box. If a matching container cannot be found, this is a two-frame beat that a drawn layer serves better than two photographs — the chapter is at 1 of `max_per_chapter: 4`. |
| 3 | s19 | **blocker** | Under the kicker **THE FIRST BRICK** and a line whose whole argument is *"यह छोटा लगता है, और है भी छोटा"*, the picture is a brickyard: **hundreds** of hollow blocks stacked to the horizon. | The picture asserts the opposite of its line. The line says *one small step*; the frame says *a completed stockpile*. That is the contradiction case, which is worse than a bland frame. It also destroys a booked motif: `script-hi.md` **7.6** is written as *"the single brick from 2.12, **now with two more set beside it**"* — if rung one is hundreds of blocks, chapter 7's payoff reads as a reduction, and the running device is dead at its first appearance. | **Needs a new fetch.** Literally the storyboard's line: *a single brick set down at the foot of a stone staircase* — one brick, isolated, with the step behind it so the ladder metaphor is in frame. This shot must be composed so 7.6 can restage it with three. |
| 4 | s17 | **blocker** | Under **WHAT ₹2,500 BUYS — "The phone recharge and the home internet"**, the picture is a bare RJ45 ethernet patch lead coiled on black. | The line names two subjects and **neither is present**: there is no phone and no recharge at all, and "home internet" is a loose cable, not a service and not its cost. There is no bill, so nothing in frame says *this is what money pays for*. This is the chapter's payoff frame — the one that has to make ₹2,500 land as a win rather than a disappointment — and it is a computer accessory on a black background. It also breaks the second booked motif: **7.6** points back at *"उस ढाई हज़ार के पहले रिचार्ज बिल"*, the first ₹2,500 recharge bill. There is no bill here for chapter 7 to point at. | **Needs a new fetch.** The storyboard's own spec: *a broadband bill and a recharge receipt overlapping on a table* — paper, printed amounts not legible, warm domestic light. Two documents in one frame is what makes the line's "and" true and gives 7.6 its callback object. |
| 5 | s17→s18→s19 | should-fix | The chapter's closing 20.4 s is three flat, desaturated textures in a row: a cable on black, a wall of tied paper bundles, a brickyard. | This is the run where the win has to land. Everything before it works — the ladder is set up, the sum closes in green, the rate holds — and then the payoff is delivered on three frames that all read as *storage, paperwork, building material*. The format twins price each rung against a named household bill precisely because the arithmetic is emotionally small; here the arithmetic is stated and then buried in beige. **Rung one currently does not land as a win.** | Fixing 3 and 4 does most of this. For the third frame, whichever of s17/s18 is re-fetched should come back **warm and domestic** (a lit room, a table, a hand) rather than archival, so the three-frame run has at least one frame a viewer wants to be in. |
| 6 | s18 | should-fix | **ALL TWELVE MONTHS** over hundreds of uncountable tied paper bundles in what reads as a municipal record room. | The assertion of this beat is a **COUNT** — twelve — and nothing in the frame counts. `format.json` `reach_for_it_when` names a COUNT as a FAIL as a flat photo, not a missed opportunity. The `index.html` comment rejects a drawn layer as depictive *"Twelve filed stubs; drawing twelve of anything over them is depictive"* — but the delivered photo is **not** twelve filed stubs, it is an archive, so the rule-8 rejection rests on an asset that was never fetched. Emotionally it is also the worst possible read of the line: *bureaucratic backlog* under *"not one rupee out of your salary"*. | Cheapest first: fetch **twelve countable stubs pinned in a row**, as specified, and keep `art-off`. If that cannot be sourced, the rule-8 rejection no longer applies and twelve drawn marks earn their place — the chapter is at 1 drawn layer of a cap of 4. |
| 7 | s16 | should-fix | The drawn layer's funnel reads as a **rising growth curve**: the wedge's hypotenuse runs up from left to right and lands on a row of twelve green bars. | Sound-off with the text stripped, a green line rising left-to-right over twelve bars is the universal grammar of *growth over twelve months* — which is the one thing `run.json` `no_return_promise` forbids the video from implying. The art is otherwise correct and genuinely additive (the sliver measures 21/700 = 3.000% and asserts a proportion no photograph can), so this is geometry, not concept. | Anchor the sliver **over the centre** of the tick row and fan the funnel out symmetrically both ways, so the dominant vector is *downward and outward* (one thing divided) instead of *upward and rightward* (one thing growing). Same elements, same arithmetic, no new asset. Also nudge the art ~19 px left inside the plate — the sliver currently sits flush against the plate's right edge with zero margin while the plate has empty space below. |
| 8 | s10 | should-fix | Under *"a fixed amount, a **fixed date**"* the frame shows **four** red push-pins on four different dates (5, 11, 17, 23) and the one circled date — the 30 — is sliced off at the very bottom edge for the whole scene. I sampled both ends of the ken; the circle never enters frame. | The picture says *many dates*, the line says *one*. The single element that would make the frame true is cropped away. This also matters upward: `storyboard-hi.md` §8 rejects the `calendar-20th-circled` Lottie on rule 8 *because the photograph is already a date circled in ballpoint* — the source file does have that circle, but what the composition renders does not, so the rejection's premise is not delivered on screen. `format.json` names *"a date being circled"* as a FAIL as a flat photo. | **No re-fetch needed** — this is a crop. Reframe s10 so the circled 30 sits in the lower third and inside the ken at both ends, and push the pins out of frame or down to one. That satisfies the storyboard's own rule-8 argument rather than breaking it. If the crop cannot hold both the circle and the type, then the Lottie's rejection has lapsed and it becomes the honest option. |
| 9 | s9 | note | The card-index drawer grades to indistinct brown; on the encode you cannot tell what the object is. | The metaphor is actually sound — the kicker is **THE NAME** and a card index is where names are filed — but sound-off it currently reads as nothing at all, which fails the rule for a different reason than the subject. | Lift exposure or crop tighter on the open drawer so the cards read as cards. Not worth a re-fetch. |
| 10 | s15 | note | `countUp("#s15-num", 46.318, 0, 1000000, …, 1.2, "₹")` starts at +1.90 and lands at +3.10; `chapter_sheet.py` samples at **+2.60**, so the sheet — and therefore every downstream reviewer and the CEO — sees **₹8,36,874**, a plausible-looking corpus figure that is not the video's number. Confirmed correct at ₹10,00,000 on the encode at t=48.5. | Not a defect in the video, a defect in the review instrument, and every rung in chapters 3–7 has this beat so it will recur five more times. `storyboard-hi.md` §8 already states the principle for drawn art — *assemble so the contact sheet's +2.6 s sample is not a half-built frame* — and the count-up is not held to it. | Set the count-up duration to **0.70 s** so it lands exactly at +2.60. Same cue slot, same ladder, no timing moves. Worth doing at the archetype so chapters 3–7 inherit it. |
| 11 | s8 | note | Two antique travel trunks in a sunlit room, not *a locked steel almirah with a key in the lock*. | Reads as *old luggage / heirlooms* rather than *saved money*. Defensible as the same metaphor family (a closed container = the corpus) and it is the warmest, most inviting frame in the chapter, so it is doing tonal work. | Leave it unless something else on the fix list happens to surface a better container shot. Do not spend a fetch on this. |

## The four questions

**1. Does rung one land as a win?** Not yet — see finding 5. The arithmetic lands
(s15→s16 is the strongest pair in the chapter) and then the three frames that have to
sell it are a cable, an archive and a brickyard. Fix 3, 4 and 6 and it lands; the
script already does its half of the job.

**2. Is the ladder legible as a ladder here?** Yes, and this is the chapter's real
achievement. s16's bar-sliver-ticks assembly teaches the measure-bar scale in one
frame without a single label, and it is genuinely additive — the photograph states the
sum, the drawing states the proportion. Chapters 3–7 can inherit it as-is once the
funnel geometry (7) stops implying growth.

**3. Pacing across 77.6 s / 12 scenes.** One scene could go without the viewer
noticing: **s8**. *"First, the mechanism / How saved money pays a monthly amount"* is a
table-of-contents entry — it announces that an explanation is coming instead of
explaining, and s9 gives the name 5.4 s later. It is not worth re-cutting locked VO for
in a fix pass, but if a tighten pass ever happens this is the scene. Everything else
earns its place; s10 and s11 are the closest pair in meaning and s11 is the weaker of
the two, which finding 2 already covers.

**4. The rate habit — rigour or nagging?** It reads as rigour through s13→s15, which is
exactly where it should: s13/s14 exist to teach the habit and the amber grade marks the
rate as *under examination* rather than recommended. It tips once, on **s16**, which
carries `3.0%` at 76 px in the green statement **and** again in the grey foot six lines
below — the same token twice in one frame. Trim the foot to
`ILLUSTRATIVE · arithmetic, not a return promise`. The rate assert is safe: it tests
`#s16-rate`, which is the span inside the statement, not the foot. As the general rule
for chapters 3–7: the rate belongs on the **corpus** frame and the **sum** frame; the
*what-it-buys* frame carries the ILLUSTRATIVE marker alone, which the extended
`derived_income_carries_assumption` assert already permits. Two mentions per rung
instead of four keeps it honest without it grating.

## What is working

- **s15 → s16 is the chapter's spine and it is right.** The count-up lands on
  ₹10,00,000 with the rate already on screen above it, and s16's drawn layer then does
  something no photograph can — cuts 3.0% out of a bar and splits that sliver twelve
  ways. Do not touch the sliver arithmetic (21/700 = 3.000%) or the twelve equal ticks.
- **The s13→s14 hold is invisible and the amber is doing real work.** One continuous
  push across a joint you cannot see, on the only two frames in the video where a rate
  is being argued rather than applied. The colour semantics (amber = under examination,
  green = closed) are legible without explanation.
- **s11b is a good frame and its currency is correct** — current stone-grey MG-New-Series
  ₹500, `MAHATMA GANDHI` microtext visible, hands only, no face. I opened it at native
  resolution specifically to check this. Keep it; it is the reference for what s15's
  replacement has to match.
