---
summary: s65 recut sourcing, attempt 4, both cuts. hi landed on rung 3 (file on disk kept, lum 93); en landed on rung 3 with a new fetch (dollar fan on black, lum 50). No candidate in either pool carried a ruled column-heading band at ≤140 mean luminance — the two criteria are mutually exclusive in stock, and that is the finding.
updated: 2026-08-01
source: fin-assets stage, Pexels contact sheets (8 sheets, 48 cells read), storyboard-hi/en §12.1
---

# fin-assets — s65 recut, attempt 4 (hi + en)

Scope was exactly two files: `s65.jpg` in each cut. Nothing else touched, nothing else
re-verified.

## Result

| Cut | Rung | File | Width | **Mean luminance** | Action |
|---|---|---|---|---|---|
| **hi** | **3** — the file already on disk | `s65.jpg` (₹500 fan + ₹20 coin, Ravi Roshan) | 1880 | **93** | **kept, unchanged** |
| **en** | **3** — new fetch, dark-surface money frame, no ledger | `s65.jpg` ($100 + fanned $20s on black, Sergei Starostin) | 1880 | **50** | **replaced** (was 226) |

Luminance measured, not eyeballed: `ffmpeg -vf format=gray,scale=1:1:flags=area` →
the single remaining byte is the area-weighted mean of the whole frame, 0–255.
The en file it replaced measured **226** by the same method (the storyboard records
212 from a different measurement; both are far past the 140 ceiling).

Global md5 dedupe over `studio/videos/*/assets/img/*.jpg`: **no duplicate hashes.**

## The finding: ruled column headings and ≤140 luminance do not co-occur in stock

This is the reason both cuts ended on rung 3, and it is worth writing down because it
will recur the next time a storyboard asks a photograph to carry legible structure.

**A page of ruled column headings is, physically, a large sheet of pale paper.** For
the headings to be legible at the size s66's crop needs, the page must fill a large
fraction of the frame. A frame dominated by cream ledger paper measures 190–210 mean
luminance no matter how dark the table under it is. The two acceptance criteria —
"a band of ruled column headings, legible as writing" and "mean luminance ≤140" — are
in direct mechanical opposition, and no query resolves it. Measured, not inferred:

| Candidate | What it was | Width | Mean lum |
|---|---|---|---|
| en rung 1, cell 6 | $1 bills on a columnar ledger sheet, dark wood, hands | 1782 | **200** |
| en rung 2, cell 1 | genuine columnar bookkeeping ledger, red/blue rules, handwritten entries | 1880 | **200** |
| en rung 3, cell 2 | $20 edges on black, no page at all | 1880 | 100 |
| en rung 3, cell 5 ✅ | $100 + $20 fan on black, no page | 1880 | **50** |

The two cells that actually satisfied the headings criterion measured 200 — identically,
from two unrelated shoots. That is the constraint, not bad luck.

**Consequence, and the log is required to say so (§12.1 rung 3, both cuts):**
s66's push-in now lands on **one note's printed panel** instead of a heading band.
For en that is the `100` / `FEDERAL RESERVE NOTE` / `LD 33979666 D` field of the $100;
for hi it is the `₹500` / `6UW 643492` field. Weaker than the recut intended, shippable,
and — worth noting — **now identical in construction across the pair**, which is what
D24 asked for even though it arrives via the floor rung rather than the top one.

## Sheets read — 8 sheets, 48 cells, all at grid size, then the pick at full res

### hi — 4 sheets, 24 cells, zero replacements earned

1. **Rung 1** `indian rupee notes lying on an open ruled account book top down on a dark wooden table@pexels`
   → 6/6 cells. **All six are ₹ note macros with coins. Not one contains a book, a page,
   or a ruled line.** Pexels has no photograph of Indian currency on an account book.
2. **Rung 1, `#7`** (next six results, same query) → 6/6 cells, same pool, same failure:
   ₹500/₹20 close-ups, no paper of any kind. Rung 1 is exhausted, not unlucky.
3. **Rung 2** `open ruled account book on a dark wooden desk top down@pexels` → 6/6.
   Cell 1 (open ruled spiral notebook on dark wood, top-down) is genuinely dark and
   genuinely ruled — but carries **horizontal rules only, no column headings**, plus
   handwritten "DESIGN YOUR LIFE". Cells 2/4/6 are laptop-and-calculator desks (brand-mark
   risk), cell 3 a blank book, cell 5 a mind-map notebook with a phone in frame.
4. **Rung 2, synonym** `vintage bookkeeping ledger book open printed column headings dark wood@pexels`
   and a further `old accounting ledger page with columns low key moody dark@pexels`
   → the real columnar ledgers surface here (cell 1, and an Italian 1813 `ENTRATA` book),
   but they are bright, and their handwriting is Cyrillic/Italian — a **non-market signal**
   that would be a second defect on top of the luminance one.
5. One extra shot at money-plus-page-plus-dark
   (`indian rupee notes on an open lined notebook dark wooden table low key top down@pexels`)
   → the pool splits cleanly into *dark empty notebooks with no money* and *bright ₹ macros
   with no notebook*. It does not contain the intersection.

**→ rung 3.** The on-disk file already satisfies every criterion rung 3 can satisfy, and
re-fetching would have traded a passing dark frame for a failing bright one.

### en — 4 sheets, 24 cells, one replacement landed

1. **Rung 1** `us dollar bills lying on an open ruled accounting ledger top down on a dark wooden table@pexels`
   → 6/6. Cells 1 and 6 are the only true ledger frames in the whole run's en pool
   (columnar sheet, heading band, $1 bills, hands). **Cell 6 promoted and measured: 1782 px
   — under the 1880 floor — and 200 luminance. Double reject.** Cell 5 carries a readable
   `CASIO`; cells 2/3/4 have no ruled page.
2. **Rung 1, `#7`** → 6/6. Three cells (2, 5, 6) put a **lit phone-screen calculator** in
   frame — the standing "never a phone screen" trap — and none has a ledger. Rung 1 exhausted.
3. **Rung 2** `open ruled accounting ledger book on a dark wooden desk top down@pexels` → 6/6,
   and it returns **the same two objects the hi rung-2 sheet returned** (the columnar ledger,
   the spiral notebook on dark wood). Cell 1 promoted and measured: **1880 px, luminance 200
   — reject.** Its handwriting is also non-Latin-market, which §12.1 criterion 4 forbids here.
4. A dark-money-plus-page attempt
   (`dollar bills on an open lined notebook on a dark wooden table low key moody top down@pexels`)
   → 6/6, no headings anywhere; cell 5 additionally carries a **printed receipt**, the exact
   prop that produced the `PARAGON FISKALNY` catch earlier in this run.
5. **Rung 3** `twenty dollar bills spread top down on a dark wooden table@pexels` → 6/6.

## The dedupe catch on the en rung-3 pick — worth recording

Rung 3 cell 2 ($20 note edges on black) passed everything: 1880 px, luminance 100, current
series, one partial serial, no brand marks. It was promoted, then

    md5sum studio/videos/*/assets/img/*.jpg | sort | uniq -d -w32
    a71a51d0744fd28d555c9be47204ef0a  .../japanese-money-methods-en/assets/img/s21.jpg
    a71a51d0744fd28d555c9be47204ef0a  .../japanese-money-methods-en/assets/img/s65.jpg

**Byte-identical to s21 — the same photograph already shipping four minutes earlier in the
same cut.** Nothing in the query, the sheet, or the vision pass could have caught this; the
md5 sweep is the only instrument that sees it. Re-picked to cell 5 (`--pick s65=5`, no new
fetch, no API call), which is a different exposure from the same photographer — full notes
fanned including a $100 with Franklin, versus s21's tight macro of $20 edges. Different
composition, different denomination reading, and 4 minutes of runtime apart.

## Full-resolution reads of both final files

Both were read at native 1880 px before landing, per the standing rule.

**en — $100 + fanned $20s on black.**
- $100: serial **LD 33979666 D**, Series 2009A, Geithner/Rios signatures — current
  Federal Reserve issue, not the old small-portrait design.
- $20s: front note **MB 77999934 K**. The neighbouring $20 in the rung-3 sheet's cell 4
  read `MB 77999921 K` — **sequential, not repeated**: a strap of consecutive bank-fresh
  notes, which is the honest case, and specifically *not* the reproduction/prop-money
  signature (identical serials on every note) that this run has been rejecting.
- Latin script only. No brand marks, no screens, no second currency, no receipts, no
  identifiable person. Engraved Franklin/Jackson are currency artwork, not a licensable
  likeness, and 6.7 makes no negative claim about a person.
- The left third of the frame is near-pure black — a clean field for the RAIL OFF light
  type, which the rejected 226-luminance predecessor could not offer anywhere.

**hi — ₹500 fan with a ₹20 coin (unchanged, re-verified this attempt).**
- **Current stone-grey ₹500 series** (2016+): Gandhi portrait, `भारतीय रिज़र्व बैंक`,
  Devanagari `५००`. No demonetised pre-2016 note in frame.
- **Three distinct serials** legible: `6UW 643492`, `…36 7832`, `…5WU 3678…`. Not prop money.
- ₹20 coin reads `TWENTY RUPEES` / `20`, dated 2020 — current, and the correct currency.
- No brand marks, no screens, no dollars, no faces beyond the engraving.
- On criterion 4's "no Devanagari on the page": that clause governs *the account book's
  heading band*, which rung 3 does not deliver at all. Every Indian banknote carries
  Devanagari by law, and §12.1 rung 3 names this exact file as acceptable, so the criterion
  is waived by construction at this rung. The 97-codepoint subset constrains **rendered
  on-screen type**, not script photographed on an object.

## Grade note (fin-build)

en `s65.jpg` at **mean luminance 50** is the darkest full-bleed hero in that cut. It needs
**no `filter:` override**: the notes themselves sit at ~180–200 and survive `brightness(.62)`
as the bright subject, exactly as s79 (37.8) and s14 (47.4) do per `fin-assets-hi-1.md`.
The one permitted override per video stays unspent in the en cut.

## Writes

- `studio/videos/japanese-money-methods-en/assets/img/s65.jpg` — **replaced**
- `studio/videos/japanese-money-methods-en/assets/img/s65.jpg.src` — `twenty dollar bills spread top down on a dark wooden table@pexels`
- `studio/videos/japanese-money-methods-en/assets/img/manifest.json` — s65 query moved to the rung-3 string, so manifest == `.src` == disk
- `studio/videos/japanese-money-methods-en/assets/img/CREDITS.txt` — **pruned from 5 s65 lines to 1.** Four were promotion attempts (the tool appends per pick and never retracts) plus one stale attempt-3 line. Kept: `paper-dollar-bills-6590651` by Sergei Starostin, restored to its original line-67 position so the file stays in slot order.
- `studio/videos/japanese-money-methods-hi/assets/img/manifest.json` — s65 query reverted from the aspirational rung-1 recut string to `indian rupee notes and coins in separate piles top down@pexels#6`, the query that actually produced the file on disk. **The manifest is the provenance record; at rung 3 it must describe what shipped, not what was hoped for.**
- hi `s65.jpg`, `.src`, CREDITS line — **untouched.**
- Two throwaway one-slot manifests were used to keep the API calls to this one slot instead of re-searching all 94/93; both removed.

Final state, both cuts: manifest slots == jpgs on disk, zero orphans, zero missing,
exactly one CREDITS line per image, no md5 collision anywhere on either channel.

**Counts: 2 slots, 1 accepted-as-replacement (en), 1 accepted-as-kept (hi), 47 cells
rejected across 8 sheets, 0 dropped.**
