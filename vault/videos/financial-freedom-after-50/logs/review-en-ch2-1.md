# review · financial-freedom-after-50 · en · chapter 2 · attempt 1
VERDICT: REWORK
PASS 1: 4 blockers, 5 should-fix
PASS 2: 0 blockers, 3 should-fix

Sheet: `studio/videos/financial-freedom-after-50-en-ch2/renders/SHEET.jpg` (19 cells, s12–s28,
two-framing cells for s12 and s23). Draft: `renders/DRAFT-ch2.mp4`, 108.672 s.
Source sheet cross-read: `assets-ch2/final/IMAGES-ch2.jpg` (1:1, pre-grade) — used only to tell a
GRADE defect apart from a SELECTION defect, not to re-run the sound-off sweep.

## The build's two flagged questions, answered on the encode

**"Does the first half render solid black?" — No.** `blackdetect d=0.1 pix_th=0.10` over the whole
108.7 s returns **zero hits**. Mean luma sampled every 3 s runs **34.5–56.2** with the first half at
35–46 and the back half at 43–56. The first half is the darker half *by design* (§10: ch2 opens
neutral-cold and crests red at s17) and that arc is intact. What is real is narrower and is filed
below as P1-5: **s14–s16 is a 19-second run of three dim, desaturated frames, two of which are
already black-and-white in the source file**, stacked under `grayscale(.32) brightness(.62)`. That
run does not render black; it renders *dead*, which is the thing the creator rejected on 2026-08-04.

**`composition_heavy_overlay_count_high` (34 overlays) — not a render failure.** Every declared
layer paints: field, scrim, glow, grain and the s18 icon are all present in the encode and nothing
is dropped or occluded. The warning is a symptom, not a defect: the overlay stack is only visibly
costly on the four scenes whose *source* is already low-key or monochrome (s14, s15, s16, s28), and
the fix belongs on those four scenes, not on the stack. Do not thin overlays globally.

## Findings
| # | pass | scene/span | severity | what | why it fails | fix |
|---|------|-----------|----------|------|--------------|-----|
| 1 | P1 | s17 @ 36.6–38.0 s | blocker | the source line paints **1.4 s before the figure it sources**. Cue ladder is `#s17-head` +0.30, `#s17-foot` +2.10, `#s17-num` at 37.991 (= +3.506) | the chapter's only figure frame spends 1.4 s reading `WORKING AGAINST YOU / VERIFIED · FEDERAL RESERVE G.19 · AS OF AUGUST 2026` with a **hole where the claim should be** — an attribution citing nothing. This is what the sheet cell caught at +2.6. It also inverts the declared kicker→figure→source ladder | in `index.html`, move `pop("#s17-num", …)` **before** `fade("#s17-foot", …)`: num at `S.s17 + 2.10`, foot at `S.s17 + 3.10` (gap 1.0 ≥ 0.8). Keep the pop landing under a spoken beat if it currently does; slide the foot, never the num, to keep it |
| 2 | P1 | s15 | blocker | a **black-and-white rain puddle beside a storm drain**. No bucket, no hole, nothing draining. VO 2.4 is *"it doesn't matter how much water you pour in if there are holes in the bottom"* and the storyboard's own image note says **"the leak must be legible, not implied"** | the picture argues *against* its line: a puddle by a drain is water **arriving** in rain, not water **escaping** a container. s14 establishes the bucket and s15 abandons it one scene later, so the metaphor the whole first half rests on is built and dropped in 6 s. **This escaped `fin-assets`.** Second-order: it is also the first of two consecutive monochrome frames | needs a **new fetch** — the bucket from s14 (or any galvanized pail) with water visibly running out of a hole near the base, in colour. If no such stock exists, the honest alternative is the *same* s14 bucket re-framed tight on its base with the leak asserted by drawn art in the D plate; do **not** accept another water-adjacent near-miss |
| 3 | P1 | s22 | blocker | a **snowman** — hat, carrot nose, stick arms — standing still in a forest | the line is *"a debt-crushing snowball… clears your slate faster"* and the storyboard says in terms **"the frame must show the track, not just the ball"**. A snowman is the one snow object that asserts the opposite of the beat: it is finished, static and decorative, and sound-off it reads *Christmas*, not *momentum*. This is the chapter's payoff beat for the whole payoff-order sequence. **This escaped `fin-assets`** | needs a **new fetch**: a snowball or boulder of snow part-way down a slope with a widening track behind it. The track is the assertion — a close-up of a snowball with no track is the same failure |
| 4 | P1 | s28 | blocker | the closer is crushed to near-black. The subject (man, mug, porch) is barely legible; the porch and the daylight behind him are gone | **not a selection defect** — at 1:1 in `IMAGES-ch2.jpg` this is a correct, well-lit porch frame. The composition killed it: an already low-key source × `grayscale(.32) brightness(.62)` × `--f1:#12351f` at 38% × scrim × grain. The chapter's **last frame carries SHOVE #1 into ch3** and it lands on a dead frame. Mean luma at 105 s is 36.0, the lowest in the entire green run | build fix, no fetch. Re-frame the ken onto the **left/window side** where the daylight is, and lift this scene: either drop the per-scene contribution to the stack or brighten the `.bg` for s28 only. Do **not** darken anything further and do not add a per-scene filter that goes darker (that is the 2026-08-04 rejection) |
| 5 | P1 | s14–s16 (15.2–34.5 s) | should-fix | three consecutive dim, near-colourless frames: a bucket buried among tools in a dark barn, a B&W puddle, a B&W brick wall with two taps. **s15 and s16 are monochrome in the source file**, before any grade | `grayscale(.32)` on an already-monochrome jpg has nothing left to take, so both land as flat grey under a 38% red field — the photographs stop being photographs. Together with s14's dim source this is 19 s where the picture layer contributes nothing. This is the honest content of the build's "first half black?" worry | fixing s15 (row 2) removes one. For s16, prefer a **colour** frame; the tap wall is acceptable as a count-of-two but it is the third grey frame in a row and nothing on it is leaking. For s14, re-frame the ken onto the bucket itself — at 1:1 the bucket is competing with a barrel and a fistful of tools |
| 6 | P1 | s25 | should-fix | the on-screen text says `3–6 months of ESSENTIAL expenses`; the picture is a **stack of $50s in one envelope**. The storyboard specified *"six identical envelopes in a row, three of them thicker"* | the beat is a **COUNT** (3 of 6) and the count is on screen in **no form at all** — not photographed, not drawn. Sound-off the frame says "money", which is true of half this video. Note this is not me second-guessing the device: the storyboard's own answer to this count was a photograph that *shows* it, and the delivered frame does not execute it | either fetch the declared frame (a countable row of envelopes/jars/packets, three visibly fuller) **or** give the D plate a drawn 3-of-6 band. If drawn, it must be schematic — a count, no dollar amounts, and the `OPINION / CONVENTION` foot stays exactly as it is |
| 7 | P1 | s21 | should-fix | five **ticked checkmarks** under *"The freed payment goes to the next line."* The storyboard specified *"the top row struck through and an arrow drawn to the second row"* | checkmarks assert *done*; the line asserts *transfer* — a payment moving from one row to the next. The roll-down is the mechanism the whole snowball rests on and it is the one thing the frame does not show. Also breaks continuity with s20, which the script wanted to be the **same** legal pad | re-frame or re-fetch to a list with one row struck and an arrow to the next; a single drawn arrow over the existing pad in the C plate is the cheaper honest fix and is additive (the photo cannot say *moves to*) |
| 8 | P1 | s24 | should-fix | a corridor of **safe-deposit / PO boxes** under `THE WORST OPTION · Never the retirement account.` | sound-off this says *bank vault*, not *retirement account* — and a vault reads as somewhere money is **safe**, which is the opposite of the line's warning. The scene is only 3.9 s and the type carries it, which is why this is not a blocker | a statement/withdrawal form on a table, figures illegible (the storyboard's own slot). Reuse of any existing file would need opening first — treat this as a **new fetch** |
| 9 | P1 | s16 | note | two spigots on a wall, neither leaking, under `THE TWO LEAKS` | the chips carry the count honestly; the picture supplies *two* but not *leak*. Filed as taste, not error | folds into row 5 if s16 is re-picked; otherwise leave it |
| 10 | P2 | 15 s – 34 s (s14→s16) | should-fix | **this is where I would leave.** Three scenes at the same pace, the same centred geometry and the same grey-to-black register, carrying a metaphor the pictures do not deliver | the flat stretch is real, but every cause of it is already a P1 row (2, 5). Recording it here so the fix pass knows the three rows are one problem, not three | fix P1-2 and P1-5 and this resolves; no separate work |
| 11 | P2 | s12–s28 | should-fix | **16 of 17 scenes are the identical layout** — centred kicker over a centred statement. The A/B/C/D archetypes are declared per scene but every scene is `.centred art-off`, which drops the plate, `crule`, `vrule` and `brule`, so the declared geometry never reaches the screen. Only s18 (the icon) differs | this is the flat read, seen as a strip. Ground temperature *does* move correctly (neutral → `#38151a` crest at s17 → amber → green), so the argument is legible; the frames just never change shape while it happens | **not more layouts** — a layout with nothing in it is a hole. Give **two** scenes something real on the other side, and they are already named: **s25** (the 3-of-6 count, row 6) and **s21** (the roll-down arrow, row 7). That is enough; do not manufacture a third |
| 12 | P2 | s12 (0–10 s) | note | the chapter opens with its **longest scene, 9.975 s**, on a slow continuous ken across a worker walking a slab, under *"Not a hot stock. A foundation."* | it is not a bad opening — the line does earn the next minute and the ken is genuinely moving — but 10 s is a lot to spend immediately after a chapter break, and it sets the unhurried register that s14–s16 then fails to break | leave it. The scene length is the VO line's length and is not a build lever. Flagged only so the fix pass does not *lengthen* anything in the first 35 s |

## Honesty check — the chapter where the rule first has teeth
Clean, with the one ordering exception in row 1.
- **s17** — `North of 20%` · `VERIFIED · FEDERAL RESERVE G.19 · AS OF AUGUST 2026`. Traces to
  `facts-staging.md` row 11 (*"north of 20%/yr"*, Federal Reserve G.19). Row 11 is **HARD on the
  shape, SOFT on every decimal**, and the frame obeys it exactly: no decimal, no period label, no
  `21.52%`. Agency and publication month both present. The VO does **not** speak the figure, as the
  chapter's script note requires.
- **s20** — `OPINION — A WIDELY USED METHOD, NOT AN AGENCY RULE`, no source card. Correct: the
  highest-rate-first order is a method, not a rule.
- **s25** — `OPINION / CONVENTION — THE STANDARD ADVICE, NOT A STATISTIC`, no agency card and no
  source line. Correct per `facts-staging` §2, which explicitly forbids an agency card here.
- No invented agency, seal or legible figure anywhere in the chapter. Every lettered surface is
  composition type; nothing is lettered by a photograph. No non-US currency, signage or plate.
- Nothing here contradicts ch1 as locked.

## Craft check
- Last scene `s28` carries a **bare** `data-duration="5.998"` (no +0.45). Root 108.659, encode
  108.672. Correct.
- First cue on every scene at **+0.30 s** (≤ 0.5). No cue-ladder gap below 0.8 s — the tightest is
  s17's 1.4 s, which is the *symptom* of row 1, not a gap violation.
- `data-framings` matches the declared two-framing scenes: **s12** `4.7,4.825` is one continuous
  ken 1.00→1.075→1.16 on a single file, so the two near-identical sheet cells are the declared
  device and **not** a repeat. **s23** `4.8,4.908` is a real photo swap (`s23.jpg` → `s23b.jpg`,
  rain off a roof edge) fading in under the word *roof*, kenned from the value `s23-bg` holds at
  that instant — well built, the picture changes and the move does not.
- The s18 icon reads: a red descending stair-arrow on its own lifted dark panel, sitting inside the
  empty wallet. It is **additive** (the wallet cannot say *guaranteed negative*), it is `warnc` so
  it takes the role colour, it finishes well before the cut, and it does not fight the photo. No
  rule-8 violation anywhere in the chapter — 16 of 17 scenes are `art-off` and that is correct.
- No type collisions, no element outside the safe area, no `.rail`, no scene counter.

## Would I keep watching?
Through s12–s13, yes — the foundation line is concrete and the ken is moving. **I would leave at
about 0:21**, on s15. The narration has just promised me a bucket with holes in it and the screen
shows a grey puddle by a storm drain; that is the moment the pictures stop confirming the voice,
and it is followed by two more frames of the same temperature before s17 finally arrives with a
number. s17 onward the chapter recovers well and the last four green scenes are the best run in it —
except that the very last frame is too dark to see, which wastes the shove.

The chapter **does** end on a reason to continue: *"Now you can go on offense."* is a genuine loop
opener and SHOVE #1 is correctly placed on it. That is worth protecting.

## Regressions vs my last pass
n/a, attempt 1.

## What is working
- **The temperature arc is right and it lands where the argument turns.** Neutral through the
  foundation, `#2b1418`/`#301519` as the leaks open, the chapter's hottest frame `#38151a` on the
  one figure, amber for the method under examination, one red spike at the surprise repair, and
  four green scenes out. The strip reads the argument even where individual pictures fail.
- **The figure discipline is exactly right** — shape only, agency and month on the card, opinion
  labelled as opinion twice, and the number deliberately unspoken. Do not "improve" any of the
  three foot lines in the fix pass.
- **s23's photo swap and s18's icon are the two best-built things in the chapter.** The swap changes
  the picture without changing the move, and the icon is the only drawn layer and it earns its
  place. Neither should be touched.
- **s26 and s27** are the two frames that survive the grade intact and give the green run its colour.
