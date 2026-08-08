---
summary: CEO gate, hi chapter 1, attempt 2 — SHIP, 0 blockers. The round-1 blocker is closed and I verified it the way I found it: my own RMS envelope of 1.6.mp3 reproduces the same four pauses, the three cells now pop at 24.159 / 25.609 / 26.759 against clause onsets 24.159 / 25.609 / 26.759, and ten frames off the new encode show one item per clause in order with the dead tail down to 2.27s. No regressions — the s3/s4 crop joint, the deleted s4 band and s7 stand. Two carried notes, neither gating. Adds one line of input (not a ruling) to the cross-cut declared-device question being settled at the en ch2 gate.
updated: 2026-08-08
source: renders/DRAFT-ch1.mp4 (1275f/42.500s, 15:04) + SHEET-ch1.jpg regenerated and md5-matched (629a6654…) + 22 frames sampled off the encode + independent RMS envelope of assets/voice/1.6.mp3 + assets/voice/timing.json + index.html motion block + assets/audio.json sfx list + 8-scene ground re-measure + fin-build-hi-ch1-6.md + ceo-hi-ch1-1.md
stage: fin-ceo, cut hi, chapter 1, attempt 2
---

# CEO · passive-income-number · hi · chapter 1 · attempt 2
VERDICT: SHIP

**BLOCKERS: 0 · NOTES: 3**

## Would I keep watching?

Yes, and I can no longer name the timestamp I would leave at — which is the answer
I could not give at attempt 1.

The chapter I gated last time was strong for twenty-four seconds and then handed the
viewer five seconds of a finished picture while the voice did the work. That window is
gone. **24.16 → 27.11 now carries six events where it carried none**, and the run of s6
reads the way the storyboard always claimed it did: premise, then bulb, then sack, then
house, each on its own word, each ticked 0.35s later.

**Verified against the voice, not against the build's claim.** I re-measured `1.6.mp3`
from scratch (0.05s RMS, −26 dB gate) and got the same four internal pauses as round 1
— 1.65–2.25 / 3.35–3.70 / 4.55–4.85 / 5.75–6.15 — so with the clip anchored at 21.909
(`timing.json`) the list clauses open at **24.159 / 25.609 / 26.759**. The three `pop()`
calls fire at `S.s6 + 2.50 / 3.95 / 5.10` = **24.159 / 25.609 / 26.759**. Dead on all
three, not 0.05 early; the build's small residual is quantisation in its own pause-end
read, and it errs in the safe direction anyway. The three `chip` cues moved with them.

**Verified in the picture, not in the source.** Ten frames across s6: 22.20 empty ·
23.90 still empty · 24.30 bulb up, its box drawing · 25.00 bulb ticked and nothing else ·
25.75 sack up, box empty · 26.30 both ticked · 26.90 house up, box drawing · 27.60 all
three ticked · 28.80 and 29.70 unchanged. One item per clause, in order, on screen.

**The tail is now a settle.** Last pixel moves at 27.559; the s7 cut is at 29.825, so
**2.27s**, and C5 «चुपचाप भरते रहना» (28.059–28.809) plays over the completed row. That is
the row being paid off, not the row waiting for the list to begin. The 2.5s at the scene
head is not a new hole — the kicker rises at +0.30, the ken is running, and C1 «उस नंबर का
काम एक ही है» is the premise the count answers. Setup then count is the right order.

Everything else I praised at attempt 1 is intact: the cold open still beats both study
twins to the withheld noun (enamel **275** under «एक ख़ास नंबर» at 18.0s), and 1.8 still
closes on an open loop rather than an answer.

## Findings

| # | scene/span | severity | what | fix |
|---|-----------|----------|------|-----|
| 1 | s8 foot, 37.07– | note (carried, **not** taken) | Round-1 note 3 was offered as a free ride on this render and was not taken: `A corpus without its withdrawal rate is a promise, not arithmetic` still uses **corpus** and **withdrawal rate** at 0:37 with no setup, and still answers on screen the question the VO is deliberately refusing to answer. I said it did not gate the next pass and I am not going back on that — it is 26px and the VO carries the beat. | none in ch1. **But it is now an obligation on ch2:** the foot has told the viewer the condition is a withdrawal rate before ch2 opens. ch2 must not spend its opening minute arriving at a fact ch1's small type already gave away. Carry to the ch2 gate. |
| 2 | s3/s4, 8.37–17.99 | note (carried) | European café tea service in an INR cut. Unchanged, still accepted after the grade, still not an Indian chai glass. | none — **the live obligation stands: re-read s80's chai-glass callback against this exact file before ch7 is briefed.** Two European tea services book-ending an INR cut is a worse problem than one in the middle. |
| 3 | whole chapter | note | Re-measured from the new encode, 4 samples per scene body: **46 · 55 · 46 · 47 · 49 · 38 · 42 · 50**. Reproduces round 1 to within a point. Not flat — range 17 points, archetypes still alternate A/D/A/A/A/D/B/A, and the trough (s6, 38) is still both the longest-held frame (8.17s) and the most substantive beat, which is now *more* true than it was, because s6 finally does in the picture what its 8.17s were bought for. | none |

## Regressions vs editor pass

**None.** I checked the expensive ones from the new encode rather than from the argument
that only three numbers changed:

- **s3/s4 crop joint** — at 12.45s exactly one headline is on screen (s3's, dimming, with
  its BEFORE NOON kicker); s4's is absent. `#s3-bg` and `#s4-bg` still resolve to one file
  under one chained `plateKen` 1.00→1.08→1.30. fin-render's double-headline defect has not
  come back.
- **s4's deleted band** — at 17.00s the phone slab reads under the ₹ card: lit top edge,
  dark screen, body returning either side of the card. The banner is on a device.
- **s6's own `.band`** — still present at index.html:208, still scoped to s6 only. The
  cascade edit did not reach it.
- **s7** — five rungs, no overlay, no re-fetch. Upheld, untouched.
- 1275 frames / 42.500s / 30fps unchanged; SHEET-ch1.jpg regenerated independently and
  md5-matches the shipped file, so the sheet is provably of this draft (temp copies deleted).

## The pipeline note — closed, and better than I asked for

I asked for the cascade default to be derived from measured clause boundaries instead of a
constant. Two tools now exist and both are the right shape: `tools/tts/clauses.py`
reproduces my by-hand envelope to within 0.05s **and asserts that agreement in its own
selftest**, which is the part that matters — the measurement that justified the tool cannot
silently drift away from it. And `tools/audio/cues.py` no longer has to invent a uniform
stagger it cannot observe; one chip per `pop()` at that call's own time is the general case,
with `popEach` falling out of it. That closes the class, not the instance. **en ch1's milder
2.9s version stays closed** — I am not reopening a locked chapter for 0.6s — and ch3–7 in
both cuts will not reproduce it.

## On the cross-cut ground question — input, not a ruling

That gate rules it; I am recording one thing so my invariant is not widened on my behalf.

**A declared device is not an exception to the invariant, because en does not need one.**
The invariant asks where the eye rests longest and darkest, and whether that frame is the
chapter's most substantive beat. en ch2 puts `$254,225` — the hero corpus — in its darkest
frame at p90 44. That **satisfies** the invariant on its face. The `--fund` ground being a
declared device explains *how* the frame got dark; it does not need to excuse anything,
because nothing needs excusing. Reaching for an exception there would create a doorway that
hi ch2 would then walk through, and hi ch2 is the actual defect: a **blank notebook page**
holding a 59.0 plateau while the hero sits in the 37.3 trough is the inversion, and no
declaration makes an empty frame substantive. If the gate wants a formulation: *a device may
set a ground; only content can justify holding it.*

None of this bears on ch1, which satisfies the invariant either way, and nothing here changes
what I want recorded for this chapter.

## Honesty

Unchanged and clean. Still no figure on screen anywhere in the chapter, so both rate asserts
remain positively vacuous; the one numeral is a house-number plaque; `₹ • • • •` names no
amount. No return implied, no institution or place implied, no "retire early". The three new
chip cues carry no claim. I would be comfortable if either study twin's author watched this.
