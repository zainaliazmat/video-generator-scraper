# editor · japanese-money-methods · hi · chapter 2 · attempt 1
VERDICT: REWORK

Reviewed `renders/DRAFT-ch2-v6.mp4` via `tools/chapter_sheet.py` (12 frames, one
per scene, multi-framing scenes sampled per framing), with each cell read against
its VO line from `script-hi.md` §Chapter 2.

## Findings

| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s13, s15 | blocker | the drawn table is illegible — thin grey bars over a dense photo of app icons (s13) and a windowed office facade (s15) | the art asserts "a table of figures" and the viewer cannot see a table. A frame that fails to communicate its own device is worse than not having it: it reads as render noise, and on s13 it sits directly on the Facebook and LinkedIn logos | s13: drop the table entirely — the photo says "the internet", the `37.8%` says the number, the `foot` cites the source; the table was solving a problem that no longer exists. s15: keep it but darken only the lower band behind the art (a gradient scrim), not the whole frame |
| 2 | s14, s15, s16, s17 | should-fix | four consecutive scenes are grey institutional building exteriors, 19.8s→44.3s — a quarter of the chapter | each is individually correct and defensible (Diet, Statistics Bureau, Cabinet Office, Kasumigaseki). Together they are a flat stretch with no change of scale, subject or register. This is the failure that only a contact sheet exposes | change SCALE, not subject: take one of s15/s16 to a detail — a nameplate, a doorway, a facade fragment — so the run reads as four different things rather than four of the same photograph. s16 is the best candidate: its wide shot carries the least information |
| 3 | s19 | should-fix | the household grid is very faint over the Tokyo crossing's first framing; it only becomes legible after the swap to the shopfront at +5.200 | the subset-vs-everyone distinction is the chapter's whole argument and it is unreadable for the first half of the scene it lives in | lift the dot opacity for the first framing, or start the crossing framing at a slightly deeper grade — the shopfront framing already works and must not change |
| 4 | s11 | note | noticeably darker than every other cell after the 60% grade softening | inconsistent within the chapter; the Kyoto street's detail is the reason it was chosen | brightness .80 → ~.86 to sit with its neighbours |

## What is working

- **Every scene now carries its own picture, and the picture says the line.** The
  internet claim is a phone of social apps; the government line is the Diet with
  the flag; the survey is the Statistics Bureau; «बुज़ुर्ग … दुकानदार» is a real
  Japanese shopfront. No image is used twice. This passes the sound-off test at
  the per-line level for the first time.
- **s17's bars are the chapter's best frame** — 37.8% a solid column, ~1.1% a
  sliver, drawn to scale from the real figures, with no decoration competing.
- The grade softening landed: these are photographs again, not grey mush.

LOG: vault/videos/japanese-money-methods/logs/editor-hi-ch2-1.md
