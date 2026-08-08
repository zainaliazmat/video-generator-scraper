# editor · passive-income-number · en · chapter 1 · attempt 2
VERDICT: REWORK

**BLOCKERS: 1 · SHOULD-FIX: 2 · NOTES: 3**

Sheet read (`renders/SHEET-ch1.jpg`, 8 cells, the fresh one — stale `SHEET.jpg`
ignored), every cell put beside its VO line, and fourteen frames sampled from the
encoded `DRAFT-ch1.mp4` including a four-frame strip across the s3→s4 joint.
Technical layer not re-verified, per handoff.

**No rail — confirmed again.** Every sampled frame carries the watermark and
nothing else. No chapter title, counter, numbering or progress mark.

**Round-1 findings 1–5 are all closed.** s3 is a whole dominant black-screen phone
on a domestic terrazzo table, no café furniture; s4 is a real 16:9 crop and the
banner now lands **on the phone** instead of on a mug; s6 carries actual
groceries; s8 is off wood and separates from its ground; s2's chip row is clear of
the alarm clock. Wood is down from six frames to three. Nothing that passed in
round 1 has broken.

---

## Rulings on the three escalated items

**1. s6 arrived as a doorstep shot, gas/car absent — UPHELD as a should-fix, and
it is NOT a sixth contact sheet.** See finding 2. Five sheets is sufficient
evidence that the storyboard's bag-plus-two-key-sets flat-lay does not exist in
either pool; I am not going to send fin-assets back for a sixth. The answer is the
one the **hi cut already shipped for this exact beat** — draw the count.

**2. s5's arrow sits off the bullseye — NOT a defect. Do not re-fetch.** I opened
the file and sampled the frame bare (22.35s, after the dissolve, before the
statement rises). The arrow is buried in the **inner gold**, its point at the edge
of the innermost ring, one ring off the X. At 1920×1080 and at speed it reads
*on target*, which is both halves of the line. This slot has burned eight-plus
sheets; the idea survives and the marginal gain does not justify a ninth. There
**is** a real problem in that frame, but it is layout, not sourcing — finding 3.

**3. "The chapter reads cold" — NOT a defect. I am not taking a `--bg` change to
the creator, and this chapter is not the evidence that would justify one.**
I measured the encoded frames of this chapter against the encoded frames of
**hi ch1** — the chapter the creator has already seen and passed, i.e. the channel's
actual reference for what this look is:

| | encoded R−B | chroma | luma |
|---|---|---|---|
| **en ch1** (this draft, 8 frames) | **−3.74** | **9.6** | 31.7 |
| **hi ch1** (approved, 6 frames) | −4.73 | 7.1 | 32.7 |

This chapter is **warmer and more saturated than the approved reference**, at the
same luma. So the coldness is not something this pass introduced and not something
the off-wood instruction cost — it is the locked channel grade, and this cut sits
on the warm side of it. fin-render's pass-through model and fin-build's backwards
opacity fix are both moot: there is nothing to fix. If the creator ever wants the
whole channel warmer that is a separate conversation started from the shipped
videos, not from a chapter that measures better than the one they approved.

---

## Findings

| # | scene | severity | tag | what | why it fails | fix |
|---|-------|----------|-----|------|--------------|-----|
| 1 | s3 → s4 | **blocker** | layout (fin-build) | **The hold ghosts.** Across the joint the frame carries **two phones, two mugs and two vases** — a visible double exposure. At 14.90s (0.30s into the 0.45s dissolve) the incoming s4 phone and the outgoing s3 phone sit side by side, offset ~200px horizontally and ~180px vertically, at different magnifications. Visible ≈14.65–15.05s, peaking 14.85–14.95. | This is the payoff transition of the whole cold open and it reads as a rendering glitch. It also breaks the storyboard's own declared device: §6b and `index.html`'s own comment say *"the two scenes read as one uninterrupted push on one image"* and §11 note 1 says *"a hold pair shares ONE ground"* — the entire purpose of a hold is that the joint is **invisible**. Here it is the most visible cut in the chapter. Root cause is arithmetic, not taste: `#s3-bg` is the 1880×1253 (3:2) file covered into 16:9 — scaled to 1920×1280 and pushed up 140px by `background-position:center 70%` — while `#s4-bg` is a 1600×900 file that is *exactly* 16:9, so it covers with no slack and its `background-position` is a no-op. `crop=1600:900:280:320` is simply not the rectangle s3 is showing when its push ends, and s3's 70% shift has no counterpart on s4. The scale chain (1.00→1.08→1.16) is continuous; the **framing** is not, and only the framing makes a hold. | **Point s4 at s3's file and let the push continue.** `#s4-bg` → `background-image:url(assets-ch1/final/s3.jpg); background-position:center 70%`, and `plateKen("#s4-bg", S.s4, D.s4, 1.08, 1.30)` for the tighter 1.4 framing. The two layers are then pixel-identical at the joint **by construction**, the dissolve is a no-op, and the derived crop stops being a moving part. The "never a self-dissolve back to the same file" note (firaun 2026-07-23) is about **flicker**; identical framing across the joint is precisely the no-flicker case and is what §6b asks for. If fin-build reads that note as forbidding it, the alternative is to compute s4's start scale and `background-position` from s3's end framing (s3@1.08 shows source-x 70–1810, source-y ≈176–1155) — same result, more arithmetic, more ways to be wrong. Verify from the encode at 14.90s, not the browser. ⚠ **The same mechanism will ghost at s41/s42 and s75/s76** — fix the mechanism now, in the storyboard, or pay for it twice more. |
| 2 | s6 | should-fix | layout (fin-build) + storyboard amendment | Three named costs; the photograph carries **groceries** and a **home threshold**, and **nothing at all for "gas and the car"** — that chip floats over a doormat. `index.html`'s own comment claims *"All three are IN the photograph's subject family"*; two of the three are. | Sound-off, with the type stripped, this is *a grocery delivery on a porch* — the enumeration is carried entirely by type over a flat photo, which is the thing the creator keeps asking us to move past. **The hi cut already ruled this exact beat and fixed it properly.** hi-ch1 `s5` ("बिजली का बिल, राशन, किराया") had the identical shape — three named costs, photograph carried one — and after five fetch attempts returned nothing, the count and the verb were **drawn**: `.v-ticks`, three inline `<svg class="icon">` cells (bulb / sack / house), each with a checkbox ticking. Rule 8 holds because a *count being paid* is not something the photograph shows. The en cut solves the same beat with three chips and no motion. Same script beat, weaker solution, and it happens to be the one that leaves the car off screen. | **Copy the mechanism, not a photograph.** Replace `#s6-chips` with a `v-ticks` row modelled on `passive-income-number-hi-ch1/index.html` s5: three inline SVG icons — a **grocery bag**, a **fuel pump** (this is what puts gas and the car on screen), a **house with its door** — each with a tick drawn on the 0.6s cascade the chips already ride. Inline `draw()`, no Lottie, no cap consumed, no re-fetch. `ctr` stays N; the ticks own archetype D's band as the chips do now. **No sixth contact sheet** — five is proof enough that the flat-lay does not exist. |
| 3 | s5 | should-fix | crop (fin-build) | The focal type lands **on the subject**: `NOT RICH` sits on the centre cross and `One specific number.` runs straight through the arrow's shaft. The one object the frame exists for is bisected by the one line it is meant to illustrate. | The frame's whole argument is *the arrow at the mark*. Burying the arrow and the bullseye under the stack throws away the only reason this photograph was chosen, after eight sheets of choosing it. The scene is `arch A · ctr Y` so the stack cannot move — but the **background** can, and this is the identical lever already used on s3. | **Layout, one line.** `#s5-bg` currently carries no `background-position`; give it one (start at `center 32%`, verify in the encode) so the bullseye and the arrow sit **above** the stack band and the type lands on the empty lower red/blue. Do not re-fetch and do not re-crop the file. Do not touch `.centred`. |
| 4 | s8 | note | — | The delivered ladder shows its **top** going over the wall with the **base out of frame** — the inverse of §10's spec (*"the lowest rungs with the top out of frame"*), under a line that says *"starting with the smallest"*. | Not false and not misleading — it reads as *a ladder, climbing*, which is the family — so it is not worth a re-fetch on its own. Round 1's actual complaint (wood on wood, no separation) is fixed: the rails and rungs now read cleanly against adobe and sky. | No action this chapter. **Carry it forward:** §10's returning-object plan has s8 → s23 (macro of one rung) → s74 (the whole ladder, full height). s8 now eats some of s74's territory; when ch6 is built, make s74 unmistakably the *full-height* statement or re-plan the family there. |
| 5 | chapter | note | — | **One Lottie against a cap of four** — and that is correct, not a shortfall. | Chapter 1 is a what-if cold open that deliberately carries **no figure at all** (the number is withheld to 4.2), so there is no NUMBER, SHARE, COUNT or DATE here for drawn art to assert. The one process beat — 1.8's *"one rung at a time"* — is owned by §9's measure bar from chapter 2 on; drawing a ladder at s8 would pre-echo it. Finding 2 adds inline-SVG motion where it is genuinely additive without touching the Lottie budget. | None. Recorded so this does not get read as a deficiency downstream. |
| 6 | s5 | note | — | s5 is the chapter's only chroma peak (16.9 against a chapter mean of 9.6). | It is the one bright frame in a 46-second dark run, and it lands on the line that turns the cold open. | **Leave it.** Do not grade it down to match.

---

## What is working

- **s4 is the best frame in the cut so far.** The masked `$ • • • •` banner lands
  squarely **on the phone**, states *money arrived* without naming a figure, builds
  from ≈+1.50 and holds 3.3s before the cut. The +1.13 fire and the +1.85 buzz are
  correct — do not re-time them, and do not let finding 1's fix move the banner off
  the device.
- **s3 is fixed and the photograph is right.** Whole black-screen phone, dominant,
  clear of every edge, domestic terrazzo, no travel props. Keep this file; finding 1
  is about how s4 registers to it, not about the picture.
- **s2 is resolved.** The chip row now sits in the empty right half and the alarm
  clock — the object that serves *"No alarm"* — is clear. Do not move it back.
- **The cue ladder and type are still clean** (kicker +0.30, statement +1.10, every
  gap 0.80s, s8 on a bare duration), s7 stands exactly as ruled in round 1, and the
  chapter's grade measures **warmer than the approved hi ch1**. Nothing here needs
  a colour pass.
