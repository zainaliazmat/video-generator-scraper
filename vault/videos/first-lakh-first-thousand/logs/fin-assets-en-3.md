# fin-assets — first-lakh-first-thousand · en · attempt 3

Targeted fix pass. Three files replaced in place (filenames kept), 90 siblings untouched.
Every promoted pick read at FULL RESOLUTION before acceptance — the rule this video earned.

## What gate two blocked, and what shipped

| Slot | Rejected (attempt 2) | Defect measured at 1:1 | Replacement | Query |
|---|---|---|---|---|
| s21 | Pexels 7680744 (receipt + calculator) | Polish fiscal receipt `SUMA PLN`, 63×34px, contrast 38/255, at ken max | Pexels 37252652 — dark desk, **blank** open ledger, abacus behind, rotary phone in shadow | `soroban abacus dark background close up@pexels` |
| s57 | Pixabay 499481 (stack of bills) | two notes sharing serial `E 34112707 E` — reproduction/prop money on the hero `$800` frame | Pexels 4386374 — fanned **$20** notes on black, one partial serial (`JF 1822…`), all distinct | `twenty dollar bills on table@pexels` |
| s91 | Pixabay 4806076 (ledger + pen) | `Kaweco AL Sport Germany` engraved, 270×90px at 157/255, held through the whole CTA | Pexels 97076 — blank ruled notebook + unmarked silver click pen on dark wood | `closed blank notebook on dark wooden table@pexels` |

Accepted 3 · rejected 15 cells across 4 sheets · dropped nothing (all three are backgrounds).

## Rejections applied, in order

- **s91 sheet 1 failed all six** on the CTA rule: cells 1/2/5 carried `FIELD NOTES` and a
  debossed cover logo, 3 was an unreadable blur, 4 a leather flatlay with a pen, 6 off-palette.
  Re-queried rather than settle — brand marks are held longest on the subscribe frame.
- **s21 first promotion reverted at 1:1.** `wooden abacus beads close up@pexels` cell 3 came
  back clean of text but the Pexels title read *wooden misbaha prayer beads* — a religious
  object dressed as an abacus, under a US money claim. Re-picked cell 2 (soroban), then found
  faint black-on-black embossing on its rail; re-queried and took the dark-desk ledger instead.
  Zero text, zero brand, currency-neutral, and it matches "same arithmetic" better than the
  receipt roll ever did.
- **s57 cell 4 rejected on the new serial rule** — `MB77999921K` appeared to repeat across
  notes in the same frame. Cell 5 mixed $5/$50 into a "20% of $4,000" frame. Took cell 3:
  black left two-thirds, denominations `20` only, no repeated serials at 1:1.

## Checks

- md5 across all studio projects (`studio/videos/*/assets/img/*.jpg`, 3 cuts): the only
  collision is the pre-existing `hi/s5.jpg` ↔ `thumbs/s5.jpg` pair. None of the three new
  files collide with the 90 en siblings, the hi cut, or the thumbs set.
- CREDITS.txt: 93 lines for 93 jpgs, one per file, no missing, no duplicate slot. The six
  stale/superseded lines from the append-only writes were removed by hand.
- `.src` sidecars and `manifest.json` both carry the shipped query for all three.
- All three from Pexels (~1880px) — s21 carries the 1.0→1.16 zoom and now clears the
  ≥1600px rule that the old 1280px Pixabay file did not.
- No per-scene `filter:` override added. The one allowance is already spent on s90; s21 is
  dark but its cream ledger pages sit dead-centre in the band crop, which is what carries it.

## Noted, no action (for the next run's per-file audit)

Gate two found `assets/img/s11.jpg` used twice — s11's full-bleed bg AND s59's 630px minor.
In a mosaic `#sN-min` can point at another scene's file, so a per-FILE audit catches what a
per-scene audit misses. Left as-is: both uses are keyword-correct and it is not a defect
this pass was authorised to touch.
