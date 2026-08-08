# editor · japanese-money-methods · hi · chapter 2 · attempt 2
VERDICT: REWORK

Reviewed `renders/DRAFT-ch2-v7.mp4` (30 fps, 2205 frames, 73.479s) via
`tools/chapter_sheet.py` — 12 cells, one per scene, s19 sampled per framing —
then full-res frames pulled from the encoded mp4 at 16.2 / 24.0 / 29.8 / 30.6 /
30.8 / 33.5 / 41.0 / 53.7 / 58.8 / 64.5 / 71.5s, each read against its VO line
from `script-hi.md` §Chapter 2. s15 was additionally checked downscaled to
440px wide (phone scale) and zoomed.

## Attempt-1 findings — all four verified fixed

1. **BLOCKER, s13/s15 illegible table — RESOLVED.** s13 without the table is now
   the most legible frame in the chapter: `37.8%` in `--target` orange over the
   dark navy of the app grid, the Table I-2-2 foot clean underneath, the stack
   properly centred. s15's `.band` works: at phone scale the art now reads as a
   table — eight rows, five columns, one row picked out in green with its marker
   bar — where in v6 it read as render noise. The drawn table appears exactly
   once in the chapter. 3 Lottie instances against a cap of 4.
2. **SHOULD-FIX, s14–s17 four grey exteriors — RESOLVED by s16 alone.** See the
   answer below; no second scene needs changing.
3. **SHOULD-FIX, s19 faint dot grid — RESOLVED.** The grid is fully legible over
   the crossing from the moment it starts drawing, and the band is gone before
   the shopfront arrives — the shopfront framing is untouched, as required.
4. **NOTE, s11 dark — RESOLVED.** s11 now sits with its neighbours on the sheet.

## The two specific checks

**Grade restorations (s13 .72→.84, s15 .70→.84).** Both are safe. s13 has no
type-contrast problem at all — the orange number and white foot sit on the
screen's dark navy field, and nothing important lands on a bright icon. s15's
kicker and number are fine against the sky. The one marginal element in the
chapter is s15's `foot` ("FIES 2024, salaried-worker households…"): grey type
whose right half crosses the sunlit facade. It reads, but it is the weakest
type on screen. Not worth a re-render on its own.

**Does s15's band separate the table from the facade, or just dim?** It
separates — mostly. The gradient is uniform across the width while the
photograph is not, so the sunlit facade in the middle-right stays bright and the
building's diagonal cornice cuts through table rows 3–4. The table survives that
because its rows are a regular repeating rhythm the eye locks onto and the green
row anchors it. Verdict: good enough to ship, not perfect. If s15 is ever
re-touched for another reason, angling the gradient to follow the facade would
finish the job. No action asked for now.

**Is the s14–s17 run fixed by one scene?** Yes. The run now reads as monument
(s14, wide, stone, dusk, fountains) → tower (s15, steep low angle, single
subject, cold blue) → street-level detail (s16, warm brick, human scale, a
person, a legible 内閣府 directory board) → city block (s17, eye-level
cityscape). Four different scales and two different colour temperatures. It no
longer reads flat and **does not need a second scene changed.** The s16 crop was
the right call: it is the only warm frame between 19.8s and 44.3s and the
Japanese directory board does real work the wide elevation never did.

## Findings

| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s20 | blocker | the photo is a stack of **German** newspapers — "Institut für Stadtgeschichte", "Frankfurter Schule", "Kartenvorverkauf", "Kölsche Karnevals-", Frankfurt phone numbers — all legible in the lower third, directly under the type | two failures at once. (a) **Wrong place**: a chapter built entirely on Japan's own two published figures puts legible German print on screen. Same class of error as the Indian shopkeeper for Japan's national accounts. (b) **Fails sound-off**: the line is «इंटरनेट सिर्फ़ बड़ा वाला उठाता है» — *the internet* picks up only the big one. A side-on stack of classified listings says "old newsprint archive", not "one number travels and the other doesn't". No headline is even visible, which the storyboard's own `img` note asked for. It is the least-working picture in the chapter | this beat is a COMPARISON that no photograph states — one number spreading, the other sitting still — and the chapter is at 3 of `max_per_chapter: 4`. **Spend the fourth Lottie here**: the 37.8% multiplying out across a field while the ~1.1% stays put, in `--warn`. If a photograph is preferred instead, it must be a screen mid-share (a post being reposted / a figure being screenshotted) — but note s12 and s13 are already phone/screen frames, so a third would repeat the register. Do not re-source another newspaper |
| 2 | s17 | should-fix | the photograph is `File:Keishicho.jpg` — the **Tokyo Metropolitan Police Department headquarters** in Kasumigaseki, identifiable by its red-and-white radio mast (one of the most-photographed buildings in Tokyo) | the head says ONE GOVERNMENT and the line is about the *national* government publishing both figures. The police HQ is (a) a different institution entirely and (b) the *metropolitan* government, not the national one. The frame quietly asserts the wrong arm of the state under a line whose entire point is that it is the same one. Caught by reading `CREDITS.txt`, not by looking — which is why it survived attempt 1 | re-source from `@commons` to a national-government subject that is neither of the two agencies already used: Kasumigaseki's ministry row, or the Ministry of Finance / Central Government Building No. 1. Keep the wide eye-level scale — that is what makes the s14–s17 run work now. The bars keep their room either way |
| 3 | s19 | should-fix | now that the grid is legible, its proportion is readable: 44 lit of 108 ≈ **41%**, sitting directly beneath a stmt that reads "37.8% counts salaried households only" | a decorative proportion that looks like a statistic. The generator's own docstring says 44/108 "is NOT a published statistic and must never be read as one" — but that caveat lives in a Python comment, and on screen a viewer maps ~41% onto the 37.8% two lines above it. Making it *equal* 37.8% would be worse (37.8% is a share of income, not of households), so the fix is the other direction | in `assets/lottie/src/who-is-counted.py`, move `LIT = 44` far enough from ~38% that no one can read it as the number on screen — ~28 or ~60 of 108. Regenerate, re-vendor. No layout change, no re-fetch |
| 4 | — | should-fix | `assets-ch2/final/CREDITS.txt` has no entry for **s18.jpg, s19.jpg or s20.jpg** — nine files listed, twelve on disk | the chapter's credits file is the one that travels with the chapter. All three are Pixabay Content License so no licence is being breached, but three images currently have no provenance in this project and the vault's archive rule depends on CREDITS shipping complete | copy the three lines from the shipped cut's `assets/img/CREDITS.txt` (s18 = andibreit opinion-poll, s19 = B_Me pedestrians, s20 = moritz320 newspaper — replace s20's line if finding 1 changes the image). File edit only, no re-render |
| 5 | s13 | note | the app grid is the ~2014 icon set: Google+ (dead since 2019), the Twitter bird (X since 2023), the old Instagram camera, Vimeo, Tumblr | dates the frame under a line about what "the internet says" *now*. It still reads as social media at a glance, which is all the scene needs, so this is taste, not error | leave it unless s20 sends you back to the stock providers anyway — if so, look for a current-era feed while you are there |

## What is working

- **Every scene carries its own picture and no image is used twice.** s13's app
  grid, s14's Diet, s15's tower, s16's Cabinet Office entrance, s19's crossing
  and shopfront, s21's rupee coins are six distinct subjects doing six distinct
  jobs. Do not let the s20 fix disturb any of them.
- **s17's bars remain the best frame in the chapter** — 37.8% a solid column,
  ~1.1% a hairline, drawn to scale from the real figures, nothing competing.
  Finding 2 changes the photograph underneath and must not touch the art.
- **s16's crop is the fix that made the chapter breathe** — warm brick, human
  scale, a legible 内閣府 board. It is the only warm frame in a 25-second
  stretch and it is carrying the whole run.
- **s21 is clean**: modern Indian coins, the old note cropped to an unreadable
  edge, ₹30,000 caveated in the foot. Last scene carries a bare duration, cue
  ladder is 0.30 / 1.10 / 1.90 throughout, all three Lotties render in the
  encoded file and finish inside their framings.

LOG: vault/videos/japanese-money-methods/logs/editor-hi-ch2-2.md
