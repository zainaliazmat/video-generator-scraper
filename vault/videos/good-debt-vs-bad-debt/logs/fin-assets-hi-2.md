---
summary: fin-assets attempt 2 for good-debt-vs-bad-debt · hi cut — re-sourced the 5 backgrounds the render frame-gate (gate two) failed at full-frame res (s2 deity coin, s5 German text, s6 medieval gold, s7 Polish book, s9 US road). All 5 replaced and accepted; 7 shipped images + their CREDITS untouched. 30 additional Pixabay search calls over 13 fetch rounds — the India-money / finance-desk pool is small and its clean images are already consumed by prior @cashguruguides/@moneymavens101 videos, so nearly every obvious hit was a demonetised note, a foreign-language/brand image, or a byte-dupe.
updated: 2026-07-28
source: fin-assets stage (attempt 2). Every candidate eyeballed at full size; md5 vs the full studio/videos ledger each round. Manifest + CREDITS at studio/videos/good-debt-vs-bad-debt-hi/assets/img/.
---

# fin-assets — good-debt-vs-bad-debt · hi · attempt 2 (frame-gate rescue)

## Scope
Gate two failed 5 backgrounds that read fine as thumbnails but wrong at full-frame
resolution. Re-sourced ONLY those 5 (s2, s5, s6, s7, s9). The other 7 shipped
images (s1, s3, s3-cutA, s3-cutB, s4, s4-cut, s8) and their CREDITS lines were
left byte-untouched (the tool skipped them every round — unchanged query → skip).

## Outcome — 5/5 replaced and accepted
| slot | attempt-1 defect (gate two) | what shipped now | src |
|---|---|---|---|
| **s2** | antique coin depicting a **Hindu deity** (revered-figure violation) | four rolled **₹10/₹20/₹50/₹100** notes on black (₹ symbol; none demonetised; monuments/Gandhi, no deity) | rupixen 4508838 |
| **s5** | **German legal text** | **magnifying glass over an accounts ledger** of figures — literally "scrutinise the terms"; handwritten Latin/numbers, no foreign print | Tumisu 4190945 |
| **s6** | medieval-European gold | **ascending silver coin stacks** (small→tall) = "pay more than the minimum"; generic edge-on coins, NO legible currency/brand | kschneider2991 2180330 |
| **s7** | **Polish metallurgy book** | **financial-calculator keypad macro** (INV/LN/DEPR/BRKEVN/% + digits; brand blurred out of frame) | Curious_Collectibles 4607653 |
| **s9** | **US road** (cross-market leak) | **green seedling in soil** — market-neutral, finance-positive closer; zero geography/currency/text | qimono 8130367 |

Every shipped file is a real photo ≥84 KB (10 KB floor). CREDITS.txt pruned from
42 appended lines to exactly the 12 shipped (7 kept originals + 5 new). Manifest =
12 slots, final s6 query `coins stack money finance dark`.

## Pixabay cost
**30 additional search calls** across 13 rounds (skips don't hit the API):
5+5+4+3+2+2+2+2+1+1+1+1+1 = 30 (5 accepted, 25 rejected). s9 accepted R2, s7 R3, s2 R4, s5 R8, s6 R13.

## md5 dedupe (full ledger, both channels)
All 5 new hashes unique — each appears once, only as its own file:
s2 `75d1b504`, s5 `177ea7cb`, s6 `9016248e`, s7 `b323e2aa`, s9 `989c1d4b`.
Byte-dupes caught and rejected en route: s7-euro = the dropped s6-cut (`981f6c71`);
s5-contract = 50-30-20-en/s7 (`0d48ed1f`); s5-calc-statement = emergency-fund/s1-bill
+ -en (`9a6fdd20`, hit 3×); s5-MacBook = needs-vs-wants/-en s5-bank (`f51f7021`);
s6-rupee-hand = this project's kept s3 (`23fa73a9`); s6-rolled = s2 (`75d1b504`).

## Filter override — unchanged
The one allowed per-video override stays on **s8** (from attempt-1, near-black
alarm clock). s2 (black surround) and s6 (white ground) were luminance-checked:
s2's bright notes and s6's high-key coins keep mean luminance mid/high, so neither
needs a grade override. No second override introduced.

## Why 13 rounds — the poison map (feeds future @cashguruguides runs)
The India-money and finance-desk Pixabay pools are small and their clean images
are already in the ledger, so obvious queries collapse onto a handful of poisoned
or duplicated hits. Confirmed this run:
- **One famous demonetised ₹500 pile (`rupixen 4395462`) is the immovable #1 for
  EVERY "indian rupee note" phrasing** — "200 rupee", "100 rupee", "2000 pink" all
  returned it. Escape only via `#N`. The clean rupee images are exactly three:
  the rolled ₹10–100 (now s2), the hand-fan ₹10 (= kept s3), and nothing else —
  every other rupee query returns ₹500, a deity coin, newsprint, or a dupe of s2/s3.
  **A second clean rupee scene is not sourceable** without duping s2/s3 → s6 had to
  leave rupee-cash for a market-neutral coin-stack texture (authority-ladder endpoint).
- **The ubiquitous "calculator on a figures statement" (`9a6fdd`) and "contract
  signing hands" (`0d48ed1f`) are the only clean English finance-doc images — and
  both are ledger dups.** Non-dup retries drift to German/Polish books, camera
  lenses (a "numbers close-up" macro → a lens distance scale), or Indian newsprint.
  A magnifying-glass-over-ledger finally gave a clean, on-keyword, non-dup s5.
- **Homonym + foreign traps recur:** "bill" → a spoonbill **bird**; "paid stamp" →
  a German **"Bezahlt"** stamp (fixed #1); "paying…desk" → a POS **terminal** with a
  lit screen + `.cz` receipt; "piggy bank" → a **Kinder®**-branded mascot and a
  novelty euro-coin piggy; "coins" → a legible **1 EURO** coin. Skip these queries.
- **What worked (reach for first next time):** `#N` past the ₹500 pile for rupee
  notes; "audit/accounting ledger figures" or a magnifier for a statement;
  "calculator keypad numbers close up" for the math beat; a plant/seedling for a
  positive closer; and — when the on-market money pool is exhausted — a generic
  edge-on coin-stack (no legible denomination) as a currency-neutral money texture.

## Note for the build
Filenames unchanged, so wiring is stable. The 4 attempt-1 orphan cut files
(s1-cut/s5-cut/s6-cut/s8-cut) remain on disk, not in the manifest (harmless;
file deletion isn't in this stage's allowlist).
