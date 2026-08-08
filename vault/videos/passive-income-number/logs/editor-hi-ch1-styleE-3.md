# editor · passive-income-number · hi · chapter 1 · attempt 3 (STYLE E, ROUND 3)
VERDICT: PASS

Reviewed `renders/DRAFT-ch1.mp4` (08-08 14:37, 1275f / 42.500s / 30fps). I regenerated
the contact sheet myself rather than trust the timestamp: it came back **md5-identical**
(`0cba85fc…`, 185083 B) to `SHEET-ch1.jpg`, so the shipped sheet is of this draft. My
temp copy (`SHEET.jpg` / `SHEET.json` — the exact bare-name landmine round 1 flagged) is
deleted; `renders/` again holds one sheet.

**Zero blockers. This chapter is ready for the CEO gate with s7 as its single open
question.**

## Round-2 blocker: CLOSED — verified from the encode, not from the numbers

I did not take fin-build's measurements on trust; I re-shot the frames and looked.

- **The phone is a phone, at playback speed.** Crops of the lower frame at 13.30 / 14.90 /
  17.00 / 17.90s show a whole dark phone slab lying across the lower-left of the table:
  the bright specular line along its top edge, the black screen, the warm body/table
  return, and the second device edge at right. At 13.30 — s4's first second, the moment
  round-1 finding 3 said opened on nothing — the phone is *already* readable. Under the
  band this whole span was an undifferentiated 22–27.
- **The ₹ card sits ON the device.** At 17.00 and 17.90 the slate panel overlaps the phone
  body with the phone's edge and corner reading clearly below and to its left. So 1.4
  («फ़ोन उस दिन सिर्फ़ एक बार बजता है») now has its named subject in shot with the banner
  on top of it, which is the whole claim the beat exists to make. `index.html`'s own
  comment about the card sitting on the phone body is now true on screen.
- **The card needed no scrim.** At 1:1 it is an opaque slate panel with its own light
  border against the raw photograph; the ₹ tile is legible and the amount stays a masked
  bar. Deleting the band cost the card nothing, which is what I said it would.
- **The deletion is surgical.** `index.html` carries `<div class="band"></div>` at line 208
  under **s6 only**; s4 has none. `art` takes exactly three values (`off`/`lottie`/`ticks`)
  and only s6 is `ticks`, so the guard is "s6 only" by construction and cannot silently
  catch a future scene. s6's band is intact and visibly stepping its lower half back
  behind the icon row.

## Findings

| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s7 | should-fix (CARRIED, not escalated) | Five drawn rungs still not built. «पाँच सीढ़ियों» / `FIVE RUNGS` runs as a flat photograph of a stone staircase, `art-off` | The count is real and a photograph cannot count — but **nothing in this draft changes the picture**, so per my own round-2 reasoning I am not escalating. Storyboard §8 refuses drawn rungs by name and bans icons beyond s6; ch1 sits exactly at its declared drawn density of 2 (s4's Lottie, s6's icon row) against a `max_per_chapter` of 4, so it is not a cap problem, it is a design disagreement | **None in this pass. CEO gate owns it — my recommendation below.** |
| 2 | s3/s4 | should-fix (CARRIED, settled) | European tea service in an INR cut | Accepted for this chapter in round 2: after the locked grade it asserts no country, and the porcelain cannot be cropped out (cover fits by width, so `background-position-x` is a no-op) | **Nothing here.** The live obligation is ch7: re-read **s80**'s callback brief against this file before ch7 assets are sourced. One European tea service mid-cut is tolerable; the same one **book-ending** the video is not |
| 3 | tone | note | Curve re-measured — see below | | None |

## ch1's tonal curve, re-measured (my own sample, 7 p90 reads inside each scene body)

| scene | dur | r2 p90 | now | |
|---|---|---|---|---|
| s1 | 4.222 | 45.9 | 45.7 | |
| s2 | 4.144 | 55.0 | 54.4 | brightest |
| s3 | 3.856 | 46.0 | 46.7 | |
| **s4** | **5.763** | **40.3** | **47.9** | **+7.6, the band's whole cost — now in line with its own photograph (s3 46.7) and s5 (48.3)** |
| s5 | 3.673 | 48.9 | 48.3 | |
| s6 | 8.167 | 37.7 | 37.7 | darkest, longest-held, untouched |
| s7 | 5.345 | 43.7 | 44.6 | |
| s8 | 7.304 | 49.9 | 49.6 | |

**Duration-weighted p90 45.1 → 46.1. Opens 45.7, closes 49.6 — arc +3.9.** My figures agree
with fin-build's to within rounding (they read 46.3 weighted, 55.0 on s2); the one scene that
moved is the one the ruling named.

**The arc is still RIGHT and must still not be flattened to match ch2.** The inversion I ruled
on ch2 does not occur here and the band fix strengthened the case, it did not weaken it: the
chapter's darkest frame (s6, 37.7) is still its longest-held and most substantive, its brightest
(s2, 54.4) is still a 4.1s throwaway, and the payoff beat that used to *dip* to 40.3 now sits at
47.9 and lifts. The chapter climbs 45.7 → 49.6 with its trough on the beat that earns one. The
new numbers are the ones the CEO should reason from; the −6.4 step into ch2's open is still
inside ch1's own grammar (its internal steps run −10.6 and +8.7) and the arc work still belongs
entirely to ch2.

## My recommendation on s7, for the CEO gate

**Uphold storyboard §8: ship s7 as it is.** The count is unclaimed, but §8 rejected drawn rungs
with an argument (rule 8 — the photograph *is* the staircase, so an outlined rung over a
photographed tread is depictive, not additive), and a drawn overlay would be the same defect the
first photo pass on the reference chapters was rebuilt to remove. If the CEO wants the count
answered anyway, the §8-compatible route is **a re-fetch, not an overlay**: a staircase frame
where exactly five treads are the readable unit. That answers *five* with the photograph and
breaches nothing. Do not ping-pong this a fourth time — decide it at the gate and record it.

## What is working

- **The payoff beat is finally whole.** One photograph, one `background-position`, one chained
  `plateKen` across 10.07s, no transition SFX at the joint, and now a legible phone under an
  opaque ₹ card for the full 5.76s. Round-1 findings 1–3 and the round-2 blocker are all closed
  by two changes and nothing was broken to get there.
- **Every joint still paints exactly one headline.** Re-checked at 12.45 / 18.21 / 21.88 /
  29.95 / 35.35s from this encode. `assets/audio.json` is byte-identical to the pre-fix build —
  11 cues, the s3→s4 `_hold` intact, the buzz still anchored at 15.702s on «बजता है».
- **s6 remains the chapter's best frame and its band is load-bearing.** Three drawn cells over
  three real jars, genuinely additive under rule 8. s5, s7, s8 are untouched and still read as
  photographs. Nothing in a future pass may disturb s5, s6, s8 or s6's band.
