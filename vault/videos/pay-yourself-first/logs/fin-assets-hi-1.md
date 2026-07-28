---
summary: fin-assets run for pay-yourself-first-hi attempt 1 — 9/9 slots filled, 12 rejections across 4 slots, zero drops, one grade-override note (s8).
updated: 2026-07-28
source: pixabay_fetch.py runs + eyeball review of every image, this session
---

# fin-assets — pay-yourself-first · hi · attempt 1

## Result: OK — 9 accepted, 0 dropped, 12 rejected fetches

Photo-free cap: s2 + s7 photo-free by design = 2 of 9; cap 0.23 × 9 ≈ 2. No
slots dropped, cap untouched.

## Accepted (final source in CREDITS.txt last-line-per-file)

| Slot | Image | Attempt |
|---|---|---|
| s1-a | dark leather wallet flat-lay, brand-free | #3 |
| s1-b | planner calendar + pen flat-lay | #2 |
| s1-c | macro of Indian rupee note (Gandhi/INDIA, current legal tender) | #3 |
| s3 | calculator + notebook + rising bar chart, no brand | #1 |
| s4 | open book under warm wicker lamp | #1 |
| s5 | Indian market, hands + tomatoes, face cropped above eyes | #1 |
| s6 | white alarm clock + cup, high-key ("QUARTZ" generic, not a brand) | #1 |
| s8 | barn-wood planks with warm ember glow (reworded query, texture-first rule) | reword |
| s9 | Mumbai Marine Drive skyline at dusk (reworded from generic "india") | reword |

## Rejected (why the 12 fetches died)

- s1-a #1 readable Mastercard logo + wallet full not empty; #2 embossed "kalibrado" brand.
- s1-b #1 balloons (zero relevance).
- s1-c #1 flat scan of worn ₹10 note, dense readable text; #2 US dimes/buffalo nickels + Thai baht cutout collage ($ answering ₹).
- s8 original query "piggy bank" was poisoned: #1 coin cutout collage, #2 Kinder-egg mascot (brand), #3 child's face on the dense climax scene, #4 Swiss 5-franc filling frame (foreign currency). Reworded to "glass jar savings": #1 candy jar, #2 US pennies ("ONE CENT" readable), #3 light bulbs. Applied the vault rule — densest scene gets the calmest background — and went plain dark-wood texture: #1 charred wood was md5-identical to 50-30-20-rule-en/s8 (dedupe reject), #2 Google logo, #3 accepted.
- s9 #1 was md5-identical to the s9 already shipped in THREE projects (50-30-20-en, emergency-fund, emergency-fund-en) — dedupe reject; #2 and #3 were Prague. Reworded to "mumbai skyline sunrise" — accepted first try.

## md5 dedupe

Final sweep across `studio/videos/*/assets/img/*.jpg`: no pay-yourself-first-hi
hash collides with any other project. (Pre-existing hi/en pair dupes in older
projects are not from this run.)

## Grade override — the ONE per video

**s8** (barn-wood): right half is dark grey and falls near-black under the
system `grayscale(.32) brightness(.62)`. Set inline on that scene's `.bg`:
`filter: grayscale(.32) brightness(.9)`. No other scene needs an override
(s6 is high-key and the standard grade tames it).

## Notes for fin-build

- grain.png copied from needs-vs-wants (build asset, not a fetched photo).
- s1-c is a note macro, not scattered coins — treat as texture; it carries the
  "India" signal per the object-led rule.
- CREDITS.txt is append-only and includes rejected fetches; the last line per
  filename is the shipped image's credit.
