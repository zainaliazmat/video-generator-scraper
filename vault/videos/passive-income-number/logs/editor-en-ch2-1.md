---
summary: fin-editor en ch2 attempt 1 — REWORK. 3 blockers, 4 should-fix. The rate constraint is MET ON SCREEN on all four figure frames (verified in the encode, not from the assert). The tank/tap ruling LANDS. Three photographs fail the sound-off test against their own lines: s17 (no date under "a finding with a date"), s14 (card catalogue under "50% stocks · 50% bonds" — the one ratio in the chapter with no picture and no drawing), s20 (a person's torso in a cut declared objects-and-hands-only, and the chapter's darkest frame). s22's `tick` is RULED: keep it.
updated: 2026-08-08
source: renders/DRAFT-ch2.mp4 + renders/SHEET.jpg (rebuilt) · assets-ch2/final read at full resolution · script-en.md ch2 · storyboard-en.md §6/§7/§8/§10/§11 · logs/fin-build-en-ch2-1.md · logs/fin-render-en-ch2-1.md · tools/format.json
stage: fin-editor, cut en, chapter 2, attempt 1
---

# editor · passive-income-number · en · chapter 2 · attempt 1
VERDICT: REWORK

Sheet rebuilt (`tools/chapter_sheet.py`, 16 cells) and read as a grid before anything
else; every cell placed beside its VO line; nine frames pulled from the **encoded**
mp4 for the calls the sheet could not settle. Fifteen finals opened at full
resolution, plus ch1's `s8.jpg` to test the ladder callback.

## The constraint, verified on screen

`withdrawal_rate_on_screen` + the 2026-08-07 `derived_income_carries_assumption`
extension. **Met, on the frame, in the encode** — not merely asserted:

| frame | figure | what carries the assumption, measured in the mp4 |
|---|---|---|
| s19 @70.7 | `$10,169` | foot: *Average annual food spending per consumer unit, 2024 — BLS Consumer Expenditures, released 19 Dec 2025, USDL-25-1586* |
| s20 @81.3 | `$847` | foot: *$10,169 divided by 12 — arithmetic, not a separate statistic* |
| s21 @89.6 | `$254,225` | `.sub` **AT A 4.0% WITHDRAWAL RATE** at 40px directly above the figure, plus foot *$10,169 divided by 0.04 · ILLUSTRATIVE ARITHMETIC* |
| s22 @96.4 | `$254,225` | inline span **at 4.0%** inside the focal |

No corpus figure is bare, no derived income figure is bare, and no published
numerator is bare. The new BILL branch is doing real work on s19/s20. This is the
chapter that had to prove it and it proves it.

## The tank — the mitigation LANDS

Ruled from the encode at 7.76s and 12.60s, and from `s10.jpg` / `s10b.jpg` at full
resolution. There is no vessel in either file; fin-build did not pretend there was.
Framing 1 is a receding row of seven brass lever taps over a copper trough; framing 2
pushes onto **one** tap, front and centre, and holds it. On screen at the moment
"tank" is spoken: kicker `THE TAP`, statement *How much can you draw each year
without emptying it*, sub `THE TANK IS WHAT YOU SAVED · THE TAP IS WHAT YOU DRAW`
complete at +2.40 against the word at +2.21–2.39.

The frame never claims to be a tank. It names the pair and points at its own half of
it, so a viewer with the sound on gets a definition rather than a contradiction, and a
viewer with the sound off gets *drawing from a supply* — which is what 2.2 is about.
**Pass.** One carry-forward below.

## Findings

| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s17 | **blocker** | A wooden box of alphabet rubber stamps on kraft paper. The line is *"four percent is the working number here, and it is a finding **with a date**, not a promise"*; on-screen `THE WORKING NUMBER` / `4.0% — a finding with a date. Not a promise.` | Sound-off failure on the line's whole content. There is no date, no calendar, no year, nothing temporal in the frame. Worse, a box of stamps connotes *stamped, approved, official* — the register of the word the line exists to deny (`Not a promise`). `format.json` `vector_art.lottie.reach_for_it_when` names **"a date being circled"** as a FAIL as a flat photo, verbatim. The script's own cue was *"a calendar page from an old desk diary, one date circled in pencil"*; s17 is **not** in storyboard §10's eight declared overrides, so this is undeclared drift, not a decision. Under the grade it also renders as an unreadable brown mass — at 7.5s you cannot tell what the object is | The beat is a DATE, so **draw it**. `assets/lottie/calendar-20th-circled.json` already exists in the library (reuse before fetch) — retarget/redraw as **October 1994 and February 1998, the two publication dates already on screen at s13 and s15, ringed** over a quiet paper still. That is additive under rule 8: the photograph cannot say *these two dates, and no promise about tomorrow*. Fallback if art density is refused: re-fetch to the script's cue — an old desk-diary page, one date ringed in pencil, hard side light, dark ground. Do **not** keep the stamp box |
| 2 | s14 | **blocker** | A pale birch library card-catalogue wall, one drawer pulled. The line is *"He tested a portfolio split **half in stocks and half in bonds**, across retirements starting in 1926"*; on-screen `WHAT HE TESTED` / `50% stocks · 50% bonds` | Sound-off failure and a motion failure in one frame. A card catalogue says *a lookup system exists* — it does not say stocks, bonds, a split, historical returns or 1926. Nothing in it argues the ratio the type asserts. **50/50 is the only ratio in this chapter with neither a photograph nor a drawing behind it** — s16 got the 95/100 grid, s18 got ÷4% = ×25, s21 got the measure bar, and the beat that is *literally a proportion* got a filing cabinet. §8's refusal table does not refuse a layer here; this slot was simply never considered. The delivered image is also off the script's cue (*"a printed table of historical returns, columns of figures, one row lit"*) and off §10, which lists s14 among the frames photographed with no legible figure — i.e. a table was expected | Add the chapter's **third** drawn layer: a single full-width bar split **exactly at 0.500**, `--target` left / ghost rect at ~.2 right, on `p-c` or `p-b` in the plate's own coordinate space, solid fills, nothing under 9px, assembled by +3.3. It asserts what the photograph structurally cannot — *half, and half*. Density check: ch2 would go 2 → 3 drawn layers over 15 scenes, inside §8's own "three or four in a twelve-to-fourteen scene chapter" calibration and nowhere near `max_per_chapter: 4`. Keep the card catalogue as the still underneath, or swap it for the script's printed table; the still is not the load-bearing part once the split is drawn |
| 3 | s20 | **blocker** | A seated person — torso, both arms, both hands, a brown/grey/red plaid shirt across ~45% of frame — hugging a paper bag of vegetables on a deck. No face (cropped above the shoulders) | Breaks storyboard §10's **own standing rejection**, restated there so a re-fetch could not lose it: *"No faces. **Hands and objects only** — s18, s33, s45, s53, s58 are the only frames with a hand and every one is specified hands-only."* s20 is not on that list and it is not a hand, it is a body. Passing it hands chapters 3–6 a precedent that the rule was written to prevent. It is also **off the storyboard's own spec** (*"two paper grocery bags on a car's back seat, daylight, no plates visible"*), it is the darkest frame in the chapter (p90 **35**, floor of a 35–59 range), and it is the far side of the chapter's largest joint — s19→s20, Δp90 **−23**, produce → produce. **Ruled on the joint separately: it is two pictures, not one place with the lights off** (different location, different framing, a human present in one and not the other), so the joint is not itself the defect. But the single re-fetch that fixes the rule breach also removes the produce adjacency and lifts the chapter's floor | Re-fetch to the storyboard's declared spec: **two paper grocery bags on a car's back seat, daylight through the window, no plates, no people**. It says *"walked out of a store in bags"* more plainly than a person holding one, it is object-only, and a lit car interior clears `YHIGH ≥ 110` comfortably. **Needs a new fetch — do not reuse any file in this chapter or ch1 for this slot** |
| 4 | s19 | should-fix | An egg carton, two carrots and a bowl of greens on a kitchen table, under `FOOD, ONE YEAR` / `$10,169` | It says *food*. It does not say *a household's food for a whole year* — a dozen eggs and two carrots under a five-figure annual total is a quiet argument against the number's scale. The script's cue (*"a full US grocery cart at a checkout lane, no faces, no readable brand marks"*) exists for that reason: a loaded cart reads as **a bill**, which is what the line is about, and a checkout lane is unambiguously American where a wooden table is placeless. Not a blocker — the frame is on-topic and the foot carries the provenance — but it is the third produce still in a four-scene run | Re-fetch to the script's cue: a **full** cart at a checkout lane, brand marks out of focus, no faces. Do this after #3 and check the pair on a fresh sheet — cart / bags-in-car / loaf is three clearly different statements about the same bill |
| 5 | s15 | should-fix | A **closed** thick white book, macro on the corner, on dark wood — under *"three Trinity University professors ran it again and **published** it"* | Off spec (§7/§10 asked for *a bound journal volume open flat, spine cracked, on a library table*) and the substitution costs the beat: a closed anonymous book says *a book exists*, not *a second paper was published*. It is also the **second near-abstract white-paper macro in three scenes** — s13 is an open book spread shot the same way, same white block on black, same scale. On the sheet the C-run's declared device (artefact changes, layout holds) is doing its job at s12 and s14; s13/s15 are the pair that reads as one idea twice | Re-fetch s15 **open flat**, spine cracked, on a library table, warm lamp, no legible title — an open volume beside s13's open page still differs by scale and context, and it restores the "published" reading. Cheapest of the four re-fetches |
| 6 | s18 | should-fix | Cue ladder: joint `transition` @62.658, `reveal` @63.258 — **0.600s apart** | Under `tools/format.json` `layout.cue_min_gap_seconds` = **0.8**. It is the only sub-0.8 gap in the chapter's 25 cues (every other gap is 1.1s or more) and neither the build nor the render pass caught it — both counted cues and checked density, neither differenced adjacent `at` values. s18 is also the chapter's biggest semantic step (amber finding → green method), so two sounds inside 0.6s at exactly that moment blur the arrival | Move s18's content cue from +0.60 to **+1.10**, the ladder position every other reveal in this chapter uses. Then add the gap check to whatever runs the cue list, so the constant in `format.json` is enforced rather than documented |
| 7 | s9–s10 | should-fix | Tone. The lighter open is real (p90 **57** vs ch1's 45) but it lasts **5.16s**, then s10 — the chapter's **longest** scene at 10.596s, 10% of its runtime — sits at p90 **44**, back inside ch1's 40–49 band, for ten seconds | Ruling asked for: **the arc is the right answer, the open is not long enough to establish it.** Descending 50.0 → 49.5 → 50.2 → 47.9 → 44.7 into the green corpus close is dramatically correct and it is what ch1 lacked; do not flatten it. But an opener that is measurably lighter for 5s and then hands ten seconds to the darkest thing in the first third does not read as "this chapter is lighter", it reads as one bright frame. The lever is **not** `.scrim` (the p10 floor is 15–24 on all fifteen scenes — raising the floor greys the photographs, and §11 already warns the field ink makes a chapter colder, not warmer). The lever is s10's photograph: a dark industrial interior is what is spending the opening | Either brighten s10's source — same brass-tap material family, **daylight-side** exposure with the tiled wall carrying more of the frame (a raking-daylight crop of the same Pexels source may get most of the way there without a fetch) — or accept it and say so explicitly to the CEO as a deliberate contrast. Do not touch the scrim |

## Rulings you asked me to make

**s22's `tick` — KEEP IT. Do not change the scene, and do not change the rung for this
chapter.** Three reasons. (1) It is bound to a real motion call: `pulse("#s22-rate")`
at +1.90, which lands on `at 4.0%` — the one token in the frame the video's honesty
rests on, and the one worth a sound. (2) s21 immediately before it fires `hero`, a
`pop` on `$254,225`. A second `reveal` 3.5s later would put the same register twice
across the chapter's payoff and flatten the green run; a small click under the rate is
the correct *smaller* sound after the big one. (3) `kit.json` binds `pulse` → `tick`
and declares "each sound bound to ONE motion helper", so the emission is
kit-consistent — the docstring gloss ("a measure bar draining") is narrower than the
binding, and a docstring is not the contract.

The genuine defect the render pass surfaced is the **inverse** one and it is not
mine to fix here: `span("#s21-mf")`, the chapter's one real measure bar, emits nothing
because s21 matched `hero` at priority 3 and the loop takes one content cue per scene.
That is right for s21 — the hero pop on the chapter's payoff figure is the sound that
frame wants — so nothing should change in ch2. But `cues.py`'s rung 5
(`find("span","#{sid}-mf") or find("pulse","#{sid}-.*")`) is one rung doing two
unrelated jobs, and its docstring describes only the first. Whoever owns `cues.py`
should split them and re-word the docstring; re-check at s60 (ch5, two rate spans, of
which the rung will sound at most one). **Scope confirmed as reported: s22 fires, s42
is in `dry` and structurally cannot, s60 predicted.**

**The four flagged joints — ruled by eye, scdet ignored as instructed.**

- **s19→s20** (Δp90 −23, produce→produce): **two pictures, not one place with the
  lights off.** Different location (kitchen table / outdoor deck), different framing
  (overhead still-life / over-shoulder held object), a human body in one and not the
  other. The joint survives on its own. Finding #3 is about the frame, not the cut —
  and fixing it retires the question anyway.
- **s9→s10** (Δp90 −15): **two pictures.** No shared object, no shared depth (flat-lay
  → receding row), no shared light direction. Same call as hi ch1 s3→s4. Passes.
- **s13→s14** (Δp90 −18): **two pictures.** Passes as a cut. s14's frame fails for its
  own reasons — finding #2.
- **s17→s18** (peak 0.137, the gentlest joint, the biggest semantic step): **the green
  reads as an arrival, not a drift.** Confirmed at 62.85 and 65.26 in the encode —
  type flips amber → green, the ground flips `#2a2113` → `#0f2a1a`, and the drawn
  division block enters under it in the same second. Three simultaneous changes carry
  it even though no measurement will. Passes, and this is the joint most at risk from
  finding #6: fix the 0.6s cue gap and it gets cleaner still.

## Notes (no rework required)

- **The `.scene.centred .stack` local patch in `build.mjs` is dead code and its comment
  is now false.** The upstream fix is in `tools/scaffold/assets/chapter-design.css`
  (verified byte-identical). Drop the emit before ch3 builds, or chapters 3–6 each
  carry a redundant declaration under a "SYSTEM GAP, patched locally and reported"
  comment describing a gap that no longer exists — the next reviewer will chase it.
  Measured centring in this encode is correct (all four centred arch-b scenes within
  1.5px of 960; s21's ladder track at 959.5 agreeing with the figure to 1.0px).
- **Tank carry-forward, sharpened.** fin-build is right that the noun s46/s47/s57
  inherit is THE TAP, and s10b proves the rhyme unit is *one big brass lever tap front
  and centre*, not a row. But **neither s10 nor s10b shows a lever in a readable
  position** — s10 has the handles small and receding, s10b crops them off the top. §10
  asks tap position and flow to carry those three beats. Brief s46/s47/s57 explicitly
  for **the lever visible and at a different angle in each**, plus flow (wide open /
  running / barely cracked / a thin stream into a tin cup). Otherwise ch4 and ch5
  inherit a rhyme they cannot articulate.
- **s21's loaf renders green.** `--fund` + ground `#12351f` turn the bread into a dark
  green mass; it is still legible as bread and §11's role-deepening is a declared
  device approved through ch1, so this is taste, not a defect. Worth the CEO's eye on
  the sheet, since s21 is the chapter's payoff frame.
- **s9** is a large near-flat kraft plane (fin-build flagged it). It carries the tone
  step and 5.16s under a pull-back is short enough. Leave it.
- s23's ladder is **not** a reuse of ch1's s8 — opened both; s8 is a ladder against an
  adobe wall and sky, s23 is three weathered rungs flat against dark planks. Different
  photographs, different statements. Clean.
- Craft, checked and clean: all 15 `data-framings` present and summing to
  `scene_duration`; s23 carries its bare 7.749; first cue at 0.000 (inside
  `first_cue_by_seconds` 0.5); s16's grid counted from the encode at 53.30 — **10 × 10,
  95 solid, 5 ghost at ~.22**, arithmetic correct against Trinity Table 3; s18's
  division block resolves left-pinned to a 25.00× corpus block. No type collisions at
  any sampled frame; the three explicit line breaks (s11, s17, s18) all read.

## What is working

- **The rate discipline is now visibly, not just structurally, in place** — four figure
  frames, four assumptions on screen, one of them (`ILLUSTRATIVE ARITHMETIC`) doing
  exactly the job the 2026-08-07 constraint extension was written for. This is the
  chapter that had to demonstrate it and it does. Do not weaken any of those four foots
  to make room for something else.
- **Both drawn layers pass rule 8's additive test.** The 95/100 grid states a share no
  photograph of a printed page can state; the division block states that ÷4% *is* ×25,
  which the hand writing on a napkin cannot. Neither is depictive, both assemble well
  before the cut, both are computed from the real figures. This is the standard
  chapters 3–6 should be held to.
- **The tank/tap resolution is a genuinely good save** — a copy fix that turns a missing
  object into the metaphor's own definition, measured against whisper rather than
  argued. Keep the `#s10-sub` and keep the +1.90 timing.
- **The C evidence run's device works at s12 and s14's layout level** and the s10 framing
  swap reads as one continuous push, not a flash. Neither should be disturbed by the
  four re-fetches above.
