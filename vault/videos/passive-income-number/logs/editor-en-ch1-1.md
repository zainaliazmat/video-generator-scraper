# editor · passive-income-number · en · chapter 1 · attempt 1
VERDICT: REWORK

**BLOCKERS: 2 · SHOULD-FIX: 3 · NOTES: 1**

Sheet rebuilt (`renders/SHEET.jpg`, 8 cells), every cell read against its VO line,
ten frames sampled from the encoded `DRAFT-ch1.mp4` including a 7-frame strip
across the Lottie stage. Technical layer not re-verified, per handoff.

**No rail — confirmed.** Ten sampled frames carry nothing but the channel
watermark bottom-right. No chapter title, no counter, no numbering, no progress
mark. Nothing on screen reveals that the video is chapter-based.

---

## Rulings on the four escalated items

**1. Black-screen phones on s1 / s3 / s4 — APPROVED, no change.**
fin-assets' reading is right. §10's standing rejection exists against *a lit
screen carrying someone's brand and being the brightest thing in frame*. On all
three frames the screen is the darkest object, carries nothing, and states the
beat more plainly than face-down would: you can see the phone is off. Applied
consistently across all three, which is what makes it a decision rather than an
exception. Keep it, and amend §10's override table so the next chapter does not
re-argue it.

**2. s5's brass table-tent stamped `5` — REJECTED.** fin-assets is right that a
blank tag fails gate 3, and wrong about the replacement. See finding 3.

**3. fin-build's three image concerns — all upheld.** s6 as a blocker (finding
2), s3/s4's mug-dominance as a blocker (finding 1), s8 as should-fix (finding 4).
fin-build was right that 2–4 are `fin-assets` territory and not fixable in a
build.

**4. Lottie at +1.13 instead of storyboard §8's +1.85 — APPROVED, +1.13 stands.**
Measured in the encode, not argued from the source: at s4+1.25 nothing is drawn;
the card outline appears ≈+1.50; **at +1.85 the `$` badge and the first masked
line are on screen and the card is visibly building**; the amount bar fills
through +3.6 and the whole thing lands 3.3s before the cut. So the `buzz` at
+1.85 will fire on a banner that is lighting, which is precisely what §8's
diegetic argument requires. Firing the Lottie at +1.85 instead would put the
first drawn pixel at ≈+2.25 and let the sound precede the picture by ~0.4s —
the failure §8 is written to prevent. Amend storyboard §8 to +1.13 (SFX stays
+1.85) so chapter 2 inherits the corrected number.
*Knock-on checked and accepted:* `s4-stmt` at +2.75 now lands while the amount
bar is still filling rather than after the banner completes. The card's identity
(`$` + line 1) is fully established by ≈+2.0, so the words still read as the
consequence. No change.

---

## Findings

| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s3 + s4 | **blocker** | The payoff beat of the whole cold open — "that one buzz is the money arriving" — plays as a banking banner floating in front of a **coffee mug**. The face-down phone is a clipped dark sliver at the extreme right edge, and s3's source is a **café table with a red duffel bag, a wallet, a card holder and sunglasses** on it, not a home kitchen counter. | §10's derived-crop table says `s4.jpg` must land on *"the phone lying face-down beside the mug"*; the delivered `crop=1600:900:133:290` lands on the mug and pushes the phone further out of frame. Sound-off, s4 says *"someone got a bank notification next to a coffee"* with no visible sender. And the s3 source **cannot be re-cropped to fix it** — I opened it: the phone is cut off by the right edge of the original photograph, so no crop of this file can make it a whole, dominant object. Separately, the café furniture argues with 1.3: the chapter's premise is that you are at home and nothing is asking for you, and a duffel bag and a wallet on the table say the opposite. | **Re-fetch `s3` (fin-assets), then re-derive `s4` from the new source.** One action. The new s3 must carry a mug **and** a whole dark-screen phone, phone large enough that a right-hand crop makes it the dominant object under the `.p-d` band (stage occupies x 550–1370, y 602–902). A domestic counter or table, nothing that reads as a café or as travel. This keeps the declared s3→s4 HOLD (§6b) intact — do not break the hold by fetching a second photograph for s4. |
| 2 | s6 | **blocker** | A blank kraft grocery bag standing against a wooden plank wall on a wooden table. No groceries, no car keys, no house keys — the frame shows one empty unmarked bag and nothing else. | The line names **three** things — groceries, gas and the car, rent or the mortgage — and the storyboard specified *"a paper grocery bag, car keys and a set of house keys laid in a row on wood, top-down."* Two of the three named subjects are absent, so the chips are carrying the whole statement and the photograph is carrying none of it. Sound-off, with the chips stripped, this is a pale rectangle on brown wood. It also breaks §10's own material rule 3 by name — *kraft* is on the list of materials that cannot survive the locked grade — and it landed exactly as predicted: a flat featureless slab in the right half against near-black in the left. | **Re-fetch (fin-assets).** Build the storyboard's shot: top-down flat-lay, paper grocery bag + car keys + house keys in a row, on **dark slate or dark stone, not wood**. The keys are polished metal and give the specular ceiling the gate wants; they also put the car and the home in frame, which is what makes the picture say the line. |
| 3 | s5 | should-fix | A brass **restaurant table tent stamped `5`** on a polished restaurant table, café bokeh behind. | Two problems. (a) The object's real-world meaning is *"table five"* — it reads as restaurant service, not as a financial target, and with s3/s4 also shot in a café that is three of eight scenes away from the "you are at home" premise the cold open is built on. (b) A legible `5` plants a specific figure at the exact beat the chapter is designed to **withhold** the number (the reveal is `$1,500,000` at 4.2, and `$5,000/month` is the hero pair) — the storyboard's override was explicitly *a **blank** white enamel tag on dark oak*. fin-assets is right that a blank tag has no number and fails gate 3; the answer is not a wrong number. | **Re-fetch (fin-assets).** Find an object that means *one exact figure* without asserting one: a gauge or dial with the needle resting on a single mark, a set of stamped steel number punches with one lifted out, a machinist's dial indicator. Specular material (brass, enamel, polished steel) so it survives the grade; **not** on a restaurant table and not on warm wood. |
| 4 | s8 | should-fix | The ladder is a weathered wooden ladder against **wooden siding** — wood on wood — with the right two-thirds falling to a near-black shadow, and the centred statement lands across the middle rung. | The storyboard asked for the lowest rungs *"against a plain exterior wall"*; the delivered wall is the same material and tone as the subject, so under the locked grade the rungs only just separate. The ladder is the spine of the whole video (§10's returning objects: s8 → s23 → s74), and this is the frame the other two return to — it has to read instantly. It currently takes a beat, and once `s8-stmt` rises it covers a rung. Not false, so not a blocker, but it is the weakest frame in the chapter. | **Re-fetch (fin-assets).** Same shot, contrasting ground: a ladder against **plaster, stucco, brick or open sky**, so the rails and rungs separate from the wall. Do not ask fin-build to shift the stack off-centre — s8 is `arch A · ctr Y` in the storyboard's own scene table and `.centred` is declared for it. |
| 5 | s2 | should-fix | The chip row sits directly on top of the alarm clock and the book stack, while the right 55% of the frame is empty near-black. | The clock is the one object in the frame that serves the first chip, *"No alarm"* — and *"No alarm"* is the chip covering it. Meanwhile the archetype's other half is a void. The photograph and the mechanism are fighting for the same third of the frame. | **Layout (fin-build).** Shift `.v-chiprow` right — set a left offset or change `justify-content` on `#s2-chips` only — so the row occupies the empty right half and the clock stays clear. s6 has the mirror-image version of this (the third chip straddles the wood/bag boundary); it resolves itself when s6 is re-fetched as a top-down flat-lay. |
| 6 | chapter | note | **Six of eight frames are an object on warm brown wood** — s1 (table), s3 + s4 (table), s5 (table), s6 (table *and* plank wall), s8 (siding). | fin-assets self-flagged four of eight; on the sheet it is six, and it makes a 46-second cold open read as one long tabletop still-life. Individually defensible, collectively monotonous — this is what the sheet exists to catch. | No separate action. Findings 1–4 already re-fetch four of the six; the directions above deliberately move s5, s6 and s8 off wood (dark slate, stone, plaster, sky). Hold the new picks to that. |

---

## What is working

- **The cue ladder and the type are clean.** Kicker +0.30 / statement +1.10 on
  every scene: first cue at 0.30s beats the 0.5s gate, every gap is exactly
  0.80s, the declared 0.6s cascade on s2/s6 is ladder C's own constant, and s8
  carries its bare 8.271s duration with no dissolve pad. Nothing collides with
  the watermark box. Do not re-time any of this.
- **The Lottie is genuinely additive and it reads.** A masked `$ • • • •` banner
  states *money arrived* — the one thing §10 structurally forbids the photograph
  from saying — without naming a figure and breaking the open loop. It builds,
  lands, and holds well inside the scene. Six of eight scenes correctly sit
  `art-off + centred`, which is rule 8 applied properly; do not add drawn layers
  to them.
- **s7 is right and should not be touched.** Hands typing, screen not visible,
  no face, warn-red slam on the verdict. It looks thin next to the line *"everyone
  asks"*, but §10's override table declares this shot for exactly this scene with
  a stated reason (never a screen photo; a search page is someone's brand). The
  device governs; the kicker `THE QUESTION` plus hands on keys carries it.
- **s1 and s2 both say their lines.** A phone alone with a dead screen in first
  light; an alarm clock, an unmade empty bed and nothing switched on. Keep both
  photographs — s2 needs a chip-row move, not a new picture.
