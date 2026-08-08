# fin-assets · japanese-money-methods · en · attempt 3 (ch1+ch2 re-source)

Filed under `-en-ch1ch2-3` because `fin-assets-en-3.md` already exists from the original
en run and is evidence for a different pass — not overwritten.

**Addendum (coordinator re-pick): s8 replaced.** The first s8 (hands typing, blank white
laptop screen) was rejected downstream as a mockup mark and as showing no statement. Nine
sheets later the slot landed on a **hand tracing rows on a printed family budget sheet** —
JAN…SEPT column headers, small household figures, a fingertip on a row, genuine current
US $1/$5 with distinct serials, no brand, no screen (`1782×1300`, mean L 190, credited,
md5-unique). What failed on the way, all caught at full resolution: a `Platinum Credit Card`
cardmember agreement with a legible `Prime Rate + 12.74%`; a sole-proprietor tax *textbook*
page; an `acer` bezel plus a Windows lock screen reading `Saturday, May 29` and Hungarian
notes; a hiking **trail register** (rows, but the entries read `Summit`); an unrolled receipt
strip in Polish (`KWOTA PTU`, `WALUTA EWIDENCYJNA PLN`); and a corporate `Executive Dashboard`
printout (`MTD Revenue`, `16.16%`) that reads as an analyst at work, not a household. Pixabay
was tried once for this slot and answered a bank-statement query with Mastercard logos, Indian
rupees and a money-plant. Note for the composition: s8 is now the **second bright frame** in a
dark chapter (with s3-fix) and carries dollar bills two scenes after s6's dollar bills — the
objects and framing differ, but if the chapter reads repetitive, s8 is the one to darken.

Targeted re-source for the -hi-parity fix round. Scope: **chapters 1 and 2, `source new:` rows only.**
Work order: `logs/editor-en-ch1-3.md`, `logs/editor-en-ch2-3.md`.
Manifest: `studio/videos/japanese-money-methods-en/assets/img/manifest-fix.json` (new file;
the shipped `manifest.json` was not touched). No existing `sN.jpg` was overwritten.

**Chapter 2 needed nothing from this stage.** Every ch2 finding is `reuse hi:`, a Lottie wire,
a plate/geometry edit or a cue-ladder change — no `source new:` anywhere in that log.

## Landed (6 accepted, all Pexels, all ≥1733 px)

| slot | file | what it shows | mean L |
|---|---|---|---|
| s1 (bg) | `s1-fix.jpg` | phone lying face-up, screen **off**, on a dark table, warm night light behind, shallow DOF; no brand, no text | 57 |
| s3 framing 1 | `s3-fix.jpg` | unopened window envelopes + US coins (cent/dime/quarter/half) + calculator + coffee on a marble counter; `PRESORTED STANDARD U.S. POSTAGE` is the only legible text | 195 |
| s5 framing 2 | `s5b-fix.jpg` | kraft delivery bag + kraft food box handed across a dark kitchen counter at night, torso only, no face, no brand | 96 |
| s5 framing 3 | `s5c-fix.jpg` | TV remote alone on a grey sofa, dim living room, no screen anywhere in frame, no brand on the remote | 89 |
| s6 | `s6-fix.jpg` | small stack of worn **one-dollar** bills on weathered wood, soft focus, no legible serial | 92 |
| s8 | `s8-fix.jpg` | hands typing on a laptop at night, blue key light, screen blank (text illegible by construction), no face | 53 |

CREDITS.txt carries a line for each of the six (verified by grep).
md5 swept across `studio/videos/*/assets/img/*.jpg` — no collision inside the cut and none
cross-project. (The `-ch1…-ch8` dirs symlink the parent `assets/img`, so their identical
hashes are one file, not duplicates.)

## Rejected at FULL RESOLUTION — the reads that earned the pass

1. **s1, first pick** (phone face-up on wood, notification on the lock screen — perfect on the sheet):
   at full res the banner reads `MESSAGES · My Bank · FRAUD ALERT MESSAGE — We need you to verify
   transaction. Did you just try to make a purchase in amount of 100$?` VO 1.1 is *the direct deposit
   lands*. A fraud alert is the opposite claim, legibly printed. Rejected.
2. **s5b, first pick** (paper bags at apartment door 12 — the editor's literal framing): a
   `STOP THE SPREAD` COVID poster on the left wall dates the frame. Rejected; took the counter
   handover instead, which has no era marker.
3. **s6, twice** (`pile of paper receipts`, `grocery store receipt`): Pexels' receipt pool is
   dominated by one Polish shoot — `PARAGON FISKALNY`, `SUMA PLN`, `NIP 527-010-33-85`, an IKEA line
   item, and one cell mirror-flipped. Wrong-market legible text on a US cut. Another pick from that
   family carried two $20s reading the same serial number. Fixed the way rule 3 says to: stopped
   querying the country-blind object ("receipts") and named the denomination — `one dollar bills
   scattered on a wooden table` returned six clean cells, no foreign text in any of them.
4. **`GST 7%` receipt** (s6 sheet 2, cell 4) — legible non-US tax line.

Rejected at sheet stage, for the record: McDonald's-branded delivery bags (2 cells), a DeepSeek
chat screen, a Chrome icon, an Apple logo, mockup crosshair marks, a child's face lit by a phone,
a woman collapsed over her bills, two payment terminals, and every "hand holding phone" cell whose
screen carried app chrome.

Sheets built: 11 (6 first pass + 5 re-queries: s1 ×4, s6 ×2). Cell counts were 6/6 everywhere
except the first s1 sheet, which came back 5/6.

## Note on s1 — what four sheets proved

"Phone face-up on a counter at night with a banking notification" is not sourceable clean. Every
cell with legible notification text was a scam alert, an AI-chat app or a branded lock screen; the
one that read right on the sheet was the fraud alert above. The delivered file is the honest
version of the beat: a phone at rest, screen off, night — the notification is the -hi drawn
`#s1-note` bar / `phone-on-counter-night` Lottie, which is where the editor's finding 1 puts it
anyway. Nothing legible to redact.

## For the composition (not my writes)

- **s1 wants the one per-video `filter:` override.** mean L 57; under the stock
  `grayscale(.32) brightness(.62)` it lands near 35 and the drawn note bar will have nothing to sit
  on. `brightness(1.3)` on that one `.bg` is the recommendation. s8 (mean L 53) is the second-darkest
  but carries its own key light from the screen and does not need one.
- **s3-fix is the brightest frame in a dark chapter** (mean L 195, white marble). If it reads as a
  sticker next to the ch1 grade, darken it per-scene rather than re-sourcing — it is the only cell
  that carries both US postage and current US coinage.
- s3-fix has a calculator reading `42565` bottom-left. Not a claim and it contradicts nothing, but
  if the ken burns wide it is a number on screen next to real ones — crop it out if convenient.
- s5c is object-led on purpose: the "one auto-renewal" beat asked for a phone screen, and every
  screen cell in that pool carried a brand. The remote says *subscription* with nothing to redact.
- s8's screen is blank white. That is the "text illegible" the editor asked for, but it is the
  brightest object in frame — keep the type out of the left third.
