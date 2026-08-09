---
summary: hi ch3 attempt 2 reviewed from the encode. PASS. Both blockers cleared — s22's gullak yard reads as containers at every point of the ken and lands 4 median points UNDER the payoff instead of 1 over, and s29's cable tangle carries the internet without a screen. Both declared questions ruled in the build's favour on measurement, not on the account: the AMR-Bld 8 tag is an anonymous asset tag, and the relocated floor is not a defect (the median floor did not move at all, and s29 is the chapter's SHORTEST scene). One live tidy-up survives — s22's stale inline background window and the comment justifying it.
updated: 2026-08-09
source: studio/videos/passive-income-number-hi-ch3/renders/DRAFT-ch3.mp4 (the 9-cell sheet + 12 frames + a 9-scene luma population), assets-ch3/final/ + CREDITS.txt + the two .src files, index.html, storyboard-hi.md, script-hi.md, logs/ceo-hi-ch3-1.md
stage: fin-editor, cut hi, chapter 3, attempt 2
---

# editor · passive-income-number · hi · chapter 3 · attempt 2
VERDICT: PASS

Scenes s22–s30, lines 3.1–3.9. Sheet rebuilt and read as a grid, every cell put beside its
VO line, twelve frames pulled from the encode at 1920×1080, and a fresh luma population
measured off the encode for the two ranking questions I was asked to rule.

**Both blockers are cleared.** Neither fix introduced a new defect. Four should-fix items,
two of them carried unchanged from attempt 1 and two of them new and both on s22's
composition rather than its photograph.

## Findings

| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s22 | should-fix | the stale inline background window was **not** dropped | `#s22-bg` still carries `style="background-size:2781.37px auto;background-position:38.74px 79.00px"` — the window hand-fitted to the deleted 1880×740 sheesham file. Two consequences. (a) It sizes the new 1880×1058 file at 2781×1565 inside a 2227×1253 `.bg` box, i.e. **1.249× tighter than `cover`** and shifted — so the frame that ships is not the frame fin-assets ran the sound-off gate on. It happens to pass anyway (I checked, below), but that is luck, not method. (b) The window leaves the top 79 element-px of `.bg` **uncovered**, and at the ken's loosest scale (1.0, reached at the end of the scene) that uncovered band's lower edge sits at frame y **−7.4px**. I looked for it rather than assuming: row 0 of all 52 sampled frames carries texture with a min per-row σ of 6.03, so nothing is visible in this encode. But the chapter's opening frame is 0.35% of a frame height away from a black band across its top edge, and any future touch to the ken endpoints or the render height exposes it silently. | Delete the inline `style` from `#s22-bg` and let `.bg` take plain `cover` — which is exactly what `s22.jpg.src` asked for ("it is now moot — DROP IT"), and it makes the shipped frame the gated frame. |
| 2 | s22 | should-fix | the composition comment now describes a photograph that is not in the build | `index.html` l.99 still reads "The photograph is a carved sheesham money box with a brass coin slot and a brass hasp" and then spends a paragraph justifying the `win` window against that file's 2.541 aspect and its out-of-focus lid centre. The photograph is a stacked yard of terracotta gullaks. This comment is rung 1's description in the **only artefact the archive keeps** (`index.html` survives, the jpg does not), and ch4–ch7 read it for the ladder. | Rewrite l.99's photograph paragraph to the gullak yard, and record the declaration `s22.jpg.src` makes and the build did not carry up: **rung 1 is MANY small containers where rungs 2–4 are one each**, so the escalation is read on the size of the vessel (fist-sized clay pot → s31's iron-bound trunk), not on the count. Delete the `win` justification with the window. |
| 3 | s24 | should-fix | *(carried, attempt 1 finding 3 — the CEO's ch3 ruling explicitly left it open: "finding 3 (s24's drawn layer) and findings 4–7 are untouched by this ruling")* the chapter's two arithmetic beats run over a photograph that does not move and cannot state either operation | 3.2 is ₹20,00,000 × 3.0% = ₹60,000 and 3.3 is ÷12 = ₹5,000, both stated only in type over one abacus whose beads never change and are not set to any value. `vector_art.lottie.reach_for_it_when` names this case by name. Cap is **4 per chapter and the chapter uses 1** (`corpus-doubles` at s28). The CEO refused a third slot at s29 and priced this one at 2 of 4 while declining to spend it — a deferral, not a decision. | Grant s24 a second layer, briefed as the **operation** and not the number: a 12-segment strip built from ₹60,000 with **one** segment lit = ₹5,000, assembled inside the scene's 6.05s. It sits over the photograph, so the s23→s24 hold (one continuous push, re-confirmed unbroken) is untouched. If the answer is still no, it should be recorded as a refusal with a reason the way the s29 layer was — not carried a third time. |
| 4 | s27 | should-fix | *(carried unchanged, attempt 1 finding 4)* the stamp through-line ships two states, not three | §10 specifies s8 at rest on the pad → s27 **mid-press, the percent mark just inked** → s77 five stamped receipts. The shipped s27 is two stamps standing at rest. The middle term of the arc is missing. | **Same disposition as attempt 1 — do not re-fetch on my account.** s27 is the payoff and the only brighter window pulls legible Latin type into frame. Record on the run that the stamp ships as two states and brief **s77** to carry the missing change (five *freshly* stamped receipts, ink wet). |
| 5 | s29 | note | *(RULED, no action)* the `AMR-Bld 8` equipment tag | Measured at full resolution on the encode, not on the sheet. The label spans **~120px of 1920 (6.2% of frame width)** in the upper-right quadrant, away from the `stmt` block, and its letterforms **do not resolve at any point in the 5.398s** — I cropped 420×200 around it and upscaled 4× with lanczos and got a pale rectangle with an unreadable smear; the lower closure's `01 2 (W)` / mirrored `(W) 2 10` is the same. It is an equipment inventory tag: it names no company, no product and no country, and even if it resolved it would read as a pole number. **A different class from the `TOA` kill** — that was a consumer audio brand, dead centre, sitting where the type sits. Same class as s26's retained `KILOWATT-HOURS`. | none — it may ship. |
| 6 | s29 | note | *(RULED, no action)* the relocated darkest-frame floor | Measured off the encode rather than inherited. **The median floor did not move at all**: s26 **19**, s29 **23** — four points clear, so s26 remains the chapter's darkest frame exactly as it was, and fin-assets' predicted ~21.5 was pessimistic. On p10 s29 (**14**) ties s23 (**14**) with s24 and s26 at **15**, so the "new bottom" is a four-frame band one point wide, i.e. inside the 1.0-point noise floor — there is no bottom to relocate. Against all three clauses of the stopping rule: **not the payoff** (s27 is), **not the longest-held** (s29's 5.398s framing is the chapter's *shortest*), **not an outlier** (1 point inside a four-frame band against a chapter range of 17). The clause was written for en ch2's s21 sitting 25 points below its neighbours; nothing here is that shape. | none. |
| 7 | s29 | note | the object names the venue, not the claim | Sound-off with the type covered, the frame says *telecom cable / network infrastructure* — the coiled slack loops, the four aerial splice closures and the stainless banding are the giveaway that this is not power. "The internet" is a one-step read from there and it is the ruled answer; the second half of 3.8 ("बहुत बड़ा और बहुत जल्दी") is carried by the over-provision rather than stated, which is supporting and not contradicting. Recording the honest limit so it is not rediscovered as new work: this frame names *where*, and no photograph can name *exaggeration*. | none — the CEO ruled the subject and the execution delivers it. |
| 8 | — | note | *(carried)* `storyboard-hi.md` §9c (l.859) and §12 (l.968) still carry the retired five-rung ladder starting at s16, with "two cash boxes" at s22 | Both were flagged in attempt 1 and **ch4 assets has already run against them** (`fin-assets-hi-ch4-1.md` exists). `notes.md` l.870 has the correct gullak record, so the vault is right and the storyboard is stale — the two disagree and the storyboard is the one an agent reads by path. | Fix both rows to the four-rung ladder (s22 → s31 → s58 → s62) before ch5 briefs assets. |
| 9 | s23/s24 · s25 · s28 | note | *(carried unchanged)* | Two consecutive calculating devices (ch2's adding machine, ch3's abacus) — **binding on ch4: s32/s33's counterfoil must be paper**. s25's absent electricity bill is a declared device, satisfied across s25+s26. s28's drawn layer at peak luma 87 is `.art-forward` by design and at the low end of readable. | none of the three is a ch3 defect. |

## Blocker 1 — s22 — CLEARED

The gullak yard reads. I judged it where the gate lives, on the encode: at **+0.40** (the
opening frame, which is what the hi ch2 ruling gave standing over), at **+4.50**, and at
**+5.10** where the ken has zoomed back to its loosest and the frame is at its most
vulnerable. All three read the same way — round clay vessels filling the frame, each
carrying an unmistakable narrow black **coin slit** on its dome, eight or nine of them
sharp enough to count. Type covered, I name *savings pots* without hesitation. The `.src`'s
structural argument is correct and I can confirm it from the pixels rather than the account:
the read does not depend on one silhouette against one ground, so `brightness(.62)` scales
the slits and the inter-pot shadow gaps but has nothing to flatten them against.

**The brightness constraint is met with room, and in the right direction.** I asked for not
more than 1.0 median point over s27. Measured: **s22 27, s27 31** — s22 comes in *four
points under* the payoff, so s27 gains a rank on median exactly as the `.src` predicted
(26.6 predicted against 27 measured, the most accurate prediction on this run).

**No coin, no denomination, no signage, no text, no hand, no face.** The shoot's country is
not provable from the frame, which the `.src` declares — but a currency-neutral, signage-free
clay vessel asserts no place, and asserting the wrong place is what the country rule catches.
Nine md5-distinct files; no reuse anywhere in the chapter.

## Blocker 2 — s29 — CLEARED

The horn loudspeakers are gone, the credit row went with them, and the replacement is the
subject the CEO ruled. Read at **+3.4** and **+4.9**: a pole crossarm carrying two hundred
coiled loops of telecom cable, splice closures, cable ties, no sky band, the tangle edge to
edge. Not a screen, not a page, no currency, no face, no script. The red `stmt` holds against
it at both ends of the ken including the end, where the ken opens onto a paler wall behind —
`p90−p50` of 32 is the chapter's busiest texture by double and the scrim still wins.

**I accept the CEO's collision ruling.** My attempt-1 routing to print was built on s52's
scene-local wording read as though it were the chapter override, and the override's actual
text is "never a **lit** phone-screen photo". Print answered a layout requirement 3.8 does
not have. The ruling is right and the finding was mine.

## The payoff clause — now decided on a real separation

The reason to record this: attempt 1's ruling needed the 1.0-point tie qualifier because the
top four frames sat inside **0.39** points. That is no longer the situation, because s22 came
down 4 points.

| | s22 | s23 | s24 | s25 | s26 | s27 | s28 | s29 | s30 |
|---|---|---|---|---|---|---|---|---|---|
| median | 27 | 26 | 27 | 31 | **19** | **31** | 28 | 23 | 31 |
| p10 | 17 | 14 | 15 | 16 | 15 | **20** | 19 | 14 | 20 |

*Whole-frame luma at 320×180, 6 fps, dissolves excluded, 29–50 frames per scene. Integer
because 8-bit medians over a large population land on integers — this is the quantisation
grain the tie qualifier was written for, and it is a different method from fin-build's
in-bin interpolation, so read these as ranks and gaps, not as replacements for its decimals.*

s27 is **tied #1 on median** (with s25 and s30, 3 clear of s28) and **tied #1 on p10** (with
s30, 1 clear of s28). Top-quartile and #1-or-#2 are both satisfied without the qualifier
having to do any work. The qualifier still stands on its own merits and the three ruling-text
items from attempt 1 are still live for the CEO — they are just no longer load-bearing here.

The corrected-direction question on s26 is unchanged from attempt 1 and I am still not
raising it: s26 is the median floor at 19 and is load-bearing, it passes the binary sound-off
gate without hesitation (a rusted kWh meter, dials and KILOWATT-HOURS legible, sitting
directly behind the type), its subject is the brightest thing in its own frame, and its p10
sits inside a four-frame tie rather than alone at the bottom. Its median is low because the
meter sits in a large dark surround, which is a framing property and not a legibility one.

## What is working

- **s22 is the fix I asked for and better than the brief.** I asked for one whole box with a
  silhouette; fin-assets found that thirteen sheets could not buy one and shipped forty
  instead, then argued from the failure mode rather than from taste why forty cannot fail the
  same way. The prediction landed within 0.4 of the measurement. Do not touch this frame.
- **`corpus-doubles` at s28 is still the model** — a real ratio (2.000× on both pairs, read
  off the rendered pixels), computed from the real figures, over an empty level balance that
  could not have asserted it. Additive under rule 8. Unchanged and it must stay unchanged.
- **The s23→s24 hold, the rate discipline** (every corpus and every derived figure carries
  its 3.0% or its ILLUSTRATIVE marker in frame, all nine scenes), **s26's warm ground under
  the chapter's one human beat, and the craft ladder** — nine clips, s30 alone carrying a bare
  5.659s, every other boundary overlapping 0.45s, tracks alternating 2/1, first cue up before
  +0.40, no type collision at any dissolve. None of these should change in a fix pass.
