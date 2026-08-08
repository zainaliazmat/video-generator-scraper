# editor · passive-income-number · hi · chapter 1 · attempt 2 (STYLE E, ROUND 2)
VERDICT: REWORK

Reviewed `renders/DRAFT-ch1.mp4` (08-08 13:34, 1275f / 42.500s / 30fps). I
regenerated the contact sheet myself rather than trust the 13:35 timestamp — it
came back byte-identical (183603 B) to `SHEET-ch1.jpg`, so the shipped sheet is
honest. My temp copy is deleted, so `renders/` still holds exactly one sheet.

**Round-1 blocker: CLOSED, and I confirm it from the encode, not from the
construction argument.** At 12.45s (the mid-dissolve) the picture does not
change across the s3→s4 joint, only its scale; exactly one headline is up. At
10.17s the frame under "Money lands in the account." now holds a glass of amber
tea AND a whole face-up phone with a dead-black screen on one table. Round-1
findings 1, 2 and 3 are all genuinely closed by that one change. Housekeeping
(finding 9) is done — the style-A artefacts are in `retired-styleA/`.

## Findings

| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s4 | **blocker** | **`.band` erases the phone on the payoff beat.** s4 carries `<div class="band"></div>`; s3 does not. `chapter-design.css:231` makes that a full-width gradient over the bottom **54%** of the frame ramping to `rgba(13,16,23,.72)`. The phone lives at the very bottom of this photograph (source y75–87%), i.e. in the band's darkest zone | **Measured from the encode, and it is not the ken and not the crop.** At 10.17s (s3, no band) the tabletop reads luma ~40 against the phone at ~16 — the phone reads as a phone. At 14.9s and 18.1s (s4, band on) the same tabletop is 22–27 and the phone 15–19, and across the card's own box (x627–1267, y780–1080) the field is a flat **15–27 with no phone/table edge anywhere in it**. So on 1.4 — «फ़ोन उस दिन सिर्फ़ एक बार बजता है», the one beat a 42.5s cold open exists to deliver — the ₹ banner floats on an undifferentiated dark field and the subject the line NAMES is not readable. It also drags s4 to **p90 40.3**, the chapter's second-darkest scene, on the beat that should be its lift. And it makes `index.html`'s own claim ("~100 of its 132px on the phone body throughout") false on screen | **Delete `<div class="band"></div>` from s4.** The notify card does not need a darkened field: at 1:1 from the encode at 17.0s it is an **opaque slate panel with its own light border** and it reads at a glance against the raw photograph. If it must stay, *size it at the call site* — which is what `chapter-design.css:230` already instructs and s4 is not doing — start it at y≈700 and cap the alpha at ~.35. **Do not re-time, do not re-fetch, do not touch s3, do not touch s6's band.** Secondary, only if the phone still sits too low after the band goes: flatten the chain to `1.08→1.18` (the `pk` assert still passes, s3 keeps `1.00→1.08`). Do not do both blind |
| 2 | s3 + s4 | should-fix | **The European tea service — ruling the declared deviation from the encode, as asked. ACCEPTED for this chapter, with one thing to carry forward.** | It does not reach blocker. After the locked grade the gold rim is a dull brass, not gold; the frame carries no currency, no text, no signage, no face and no flag, so it **asserts no country** — unlike a $ note or a demonetised ₹500, it is not a factual error. The object that carries the beat — a clear glass of amber tea plus a dark-screen phone — is the brief's own family and survives the grade as the second-most-legible thing in frame. **I also checked whether it could simply be cropped out, and it cannot:** cover fits by WIDTH (2227.2 ÷ 1880 = 1.1847), so the full source width is in frame at scale 1.0 and `background-position-x` is a **no-op**; excising the porcelain (source x55–90%) needs a ~1.9–2.9× upscale, above the 1.63× this chapter already stretched on s8. fin-assets' choice was a real one and it took the right side of it | **Nothing in this chapter.** But fin-assets flagged that this same file is the antecedent for **s80 (7.7)**, the chai-glass callback. One European tea service in an INR cut is a tolerated near-miss; the same one **book-ending** the video is a different problem. Re-read s80's brief against this file before ch7 is briefed — if the callback rhymes, it must rhyme on the **GLASS**, not on the service |
| 3 | s7 | should-fix | **Re-ruling round-1 finding 4 (five drawn rungs), as asked: HELD at should-fix, NOT escalated, and I am naming why.** The count is real — «पाँच सीढ़ियों» / `FIVE RUNGS` over a photograph whose visible treads number about nine. Sound-off it says *climbing*, not *five* | **But storyboard §8 refuses this by name, and that is a governing decision, not an oversight.** "*4.10 — three drawn rungs* → `off`. The photograph *is* the count — depictive", and "**No icons beyond s6** … an arrow over a staircase … the rule-8 depictive failure". §8 also declares ch1's drawn density as **2**, which is exactly what it has (s6's icon row + s4's Lottie). Escalating this to a blocker would be me forcing a taste call over an argued design decision, which is not checkpoint one's job. Nor is it a cap problem — `max_per_chapter` is 4 | **None in this pass. Flagged for the CEO as the chapter's one open design disagreement.** If it is ever actioned, the §8-compatible route is a staircase frame where **five treads are the readable unit**, not a drawn overlay — that answers the count without breaching the depictive rule |
| 4 | s1 | note | **Ruling the second declared deviation: KEEP the textile frame. Do not ping-pong this slot again.** 1.1 names the phone and the frame has none | **I opened the alternative before saying so.** `assets-ch1/retired-attempt6/s1.jpg` is a black phone face-up on a dark wooden table — a near-black macro. Restoring it would make s1, s3 and s4 **three consecutive frames of a dark phone lying on a surface**: the repeat I moved s1 to break, just relocated, because the blocker fix changed what s4 is. So the reason for my round-1 should-fix has inverted, and the honest answer is that the current frame is the better one. A photograph cannot show a phone *not* ringing in any case; the bed photographs the CONSEQUENCE of the negation — nobody had to get up — which is 1.1's main clause («सोचिए, एक ऐसा दिन…»), and the phone thread lands 8.4s later at s3 and pays off at s4. Verified at full resolution: no people, no face, no brand, no text, no lit screen | None |
| 5 | tone | note | **The measurement nobody had taken.** Per-scene p90 luma from the encode, 7 samples per scene inside the scene body | | See below |

### ch1's tonal curve

| scene | dur | p90 | |
|---|---|---|---|
| s1 | 4.222 | 45.9 | |
| s2 | 4.144 | **55.0** | brightest |
| s3 | 3.856 | 46.0 | |
| s4 | 5.763 | 40.3 | ⚠ the payoff — see finding 1 |
| s5 | 3.674 | 48.9 | |
| s6 | 8.166 | **37.7** | darkest, and longest-held |
| s7 | 5.346 | 43.7 | |
| s8 | 7.304 | 49.9 | |

**Duration-weighted p90 = 45.1.** Opens 45.9, closes 49.9 — **arc +4.0**.

**ch1's shape is CORRECT and must not be flattened to match ch2.** The inversion
I ruled on ch2 does not occur here: ch1's longest-held frame (s6, 8.17s, the
three household costs) is also its **darkest**, and its brightest (s2, 55.0, the
alarm clock) is a 4.14s throwaway. Tonal weight sits on the substantive beat and
the chapter lifts into its close. That is the right way round.

**ch1 + ch2 as one 124-second opening.** Combined duration-weighted p90 ≈ **47.0**
(45.1 over 42.5s, then 48.0 over 81.5s). The shape is: a correct climb through
ch1 (45.9 → 49.9), a **−6.4 step down** into ch2's open at 43.5, then 81.5
seconds with no direction, closing at 43.0. The −6.4 chapter joint is *not* the
problem — ch1's own internal steps run −11.2 (s5→s6) and +9.1 (s1→s2), so a 6-point
step is inside this chapter's normal grammar. **The arc work is all in ch2**: it
needs a direction and it needs its brightest longest-held frame to stop being a
blank notebook page. Whoever takes that must leave ch1 alone. Note also that
fixing finding 1 lifts s4 off 40.3 and deepens ch1's climb, which helps.

## What is working

- **The hold is real and it is the chapter's best structural move.** One file,
  one `background-position`, one chained `plateKen` across 10.07s, no transition
  SFX at the joint. At 12.45s the picture is continuous and exactly one headline
  is up. `rise("#s4-stmt", …)` reads correctly against a crop, as claimed.
- **The ₹ is unambiguous at 1:1.** I re-checked the card at 17.0s at full
  resolution: five round-capped strokes on the app tile, legible, amount left as
  a masked bar. That ruling holds and the corrected comment now matches the art.
- **s6 is still the best frame in the chapter** and s5, s7, s8 are untouched and
  still read as photographs, not grey mush. Every joint I sampled (4.45 / 12.45 /
  18.21 / 21.88) paints exactly one headline. s8 carries a bare `data-framings`
  equal to its duration. Whatever the fix pass does, it must not disturb these —
  and it must not touch **s6's** band, which is load-bearing for the icon row.
