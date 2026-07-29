---
stage: fin-assets
slug: good-debt-vs-bad-debt
cut: en
attempt: 1
date: 2026-07-29
status: ok
---

# fin-assets — good-debt-vs-bad-debt · en · attempt 1

US ($) cut for @moneymavens101. 16 slots planned (9 bg + 7 cut-ins). Every image
eyeballed at full resolution; every kept hash md5-checked against the full
cross-project ledger. Heavy rejection round — the top-hit pool for these
concepts is polluted with foreign currency, bank/card brands, and a handful of
"hero" images already used across the channel.

## Outcome
- **Accepted / shipped: 12** (all 9 bg + 3 cut-ins).
- **Dropped: 4 cut-ins** (s1-cut, s5-cut, s6-cut, s8-cut) — removed from manifest.
- **Pixabay fetches: 66** across 8 manifest passes (16 + 14 + 13 + 8 + 5 + 4 + 3 + 3).
- Every shipped hash is unique across ALL projects on both channels and distinct
  from the hi cut. No per-scene `filter:` override needed (no near-black texture;
  the bright ones — s1/s2/s4 — are handled by the standard grade + scrim).

## Shipped images (final)
| slot | md5 | what it is |
|---|---|---|
| s1.jpg | 40b7cf88 | US $1 Great-Seal (pyramid/eye) macro — money, hook |
| s2.jpg | 042d417f | banded stacks of US $1 bills — calm roadmap texture |
| s3.jpg | d6357dce | US $20/$10/$5 flat-lay — «renting money» |
| s3-cutA.jpg | 8363c4e7 | restaurant dinner, wine pour — «a dinner» |
| s3-cutB.jpg | a2ede540 | kraft gift/shopping bags on a rock — «a sale» |
| s4.jpg | e580ecba | stack of textbooks — good debt = a degree (calmest, densest) |
| s4-cut.jpg | 62f3e48a | two people (from behind) carrying shopping bags — consumption |
| s5.jpg | d8901eaf | black calculator + finance doc — how the minimum works |
| s6.jpg | e631375b | US $100 (Franklin) macro — pay more than the minimum |
| s7.jpg | 9fa70223 | fountain pen on a lined notepad, dark wood — the math |
| s8.jpg | a8569e36 | US $1 planted in soil — action / positive money beat |
| s9.jpg | e4b1c93 | Monument Valley open highway — the road out (closer) |

## Dropped cut-ins (nothing usable — dropped rather than faked)
- **s1-cut** (statement on «minimum payment»): 4 tries → Mastercard-cards-in-pocket
  (brand), German legal textbook (legible foreign text), a dollar image, and a
  notepad that byte-collided with s7. No clean brand-free statement exists.
- **s5-cut** (snowball on «compounding»): 3 tries → a skiing child, green
  farmland hills, frost-covered grass. Pixabay has no clean "snowball rolling
  downhill"; the "snowball" query trap is real.
- **s6-cut** (hand + bill on «add a little on top»): 3 tries → the dollar hero
  pile, the hi-cut's s8-cut (dup), a dollar-with-pills (medical). Hands never
  matched.
- **s8-cut** (reach for a card on «open your card's app»): 3 tries → a blank-sign
  man, a Mastercard debit card (brand), a Canon camera (brand). Cards are a brand
  minefield.

Each scene keeps its full-bleed bg; the chip/row TYPE carries what the dropped
cut-in would have shown. Consistent with the hi cut (which also shipped fewer
than the planned cut-ins).

## Rejections caught by looking (the point of this stage)
- **Foreign currency** answering a US ($) query: Moroccan dirham (Arabic script),
  €20 euro note — both hard-rejected.
- **Wrong-market content**: bundled **Indian newspapers** (BJP / Rahul / Dimapur
  / Bengal headlines) returned for "printed documents" — exactly the India/hi
  material this cut must stay clear of.
- **Legible brand marks**: Mastercard (×several), VISA + Sparkasse (German bank
  card), a POS payment terminal + app screen, a Samsung phone, a Canon camera.
- **Legible foreign-language document**: a German legal textbook (glasses shot).
- **Homonym traps**: "snowball" → skiing/frost, "rubber band" → loom bands,
  "coins" → hazelnuts, "bills" → zen pebbles / apple-on-books.
- **Faces as the subject of a negative-claim scene**: a Vietnamese graduate
  (front-facing, + foreign sash text) and a woman at a desk — both on scenes that
  render "BAD DEBT" / the interest trap.

## md5 dedupe (byte-identical collisions rejected)
- The dollar-pile hero `aaa3bc15` (= `pay-yourself-first-en/s8`) was returned for
  s2/s3/s6/s6-cut at once — rejected everywhere.
- `4d9b6f40` (shopping bags) = **hi cut's s4-cut** — rejected.
- `9e38f45b` (= emergency-fund-en/s5), `3d6c9143` (= pay-yourself-first-en/s1-c),
  `9ec5654a` (= hi s8-cut) — all caught and rejected.
- Escaped the exhausted shallow dollar pool by harvesting consecutive indices of
  one base query (`us dollar bills` #5/#6/#7) → three distinct, unused, clean US
  shots for s1/s3/s8.

## Minor notes carried (not defects; brief cut-ins under grade+scrim)
- s3-cutA: faint etched "PUREZZA" on a water bottle (no dominant brand).
- s4-cut: faint generic print on blue plastic bags (not a legible brand).
- s5: partial English word "Busin[ess]" + a generic stock table (English, benign).
- s8: money-in-soil reads slightly "growth" vs the paying beat — kept because it
  sits on the positive/escape action beat and is clean US currency.

## ORPHAN FILES — need deletion by orchestrator (outside this stage's rm-less allowlist)
The 4 dropped cut-ins are removed from `manifest.json` + `CREDITS.txt` but their
bytes remain on disk (this stage may only run `pixabay_fetch.py` / `md5sum`):
- `assets/img/s1-cut.jpg` (+ `.src`) — hash 9fa70223 (byte-identical to shipped s7)
- `assets/img/s5-cut.jpg` (+ `.src`) — hash 02a63a73
- `assets/img/s6-cut.jpg` (+ `.src`) — hash 8dff7285
- `assets/img/s8-cut.jpg` (+ `.src`) — hash b0e316ee
Build reads the manifest, so these will not composite; delete for tidiness/ledger.
