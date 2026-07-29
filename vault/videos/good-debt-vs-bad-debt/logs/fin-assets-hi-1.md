---
summary: fin-assets stage for good-debt-vs-bad-debt · hi cut · attempt 1 — 12 images shipped (9 bg + 3 cut-ins), 4 cut-ins dropped, 48 Pixabay API calls over 6 fetch rounds. First-pass reject rate 12/16; the Indian-rupee + finance-desk Pixabay pool is small and already consumed by prior @cashguruguides videos, so generic queries collide with the ledger or return demonetised notes / literal-homonym junk.
updated: 2026-07-28
source: fin-assets stage (this run). Every image eyeballed before accept; md5 vs the full studio/videos ledger each round; manifest at studio/videos/good-debt-vs-bad-debt-hi/assets/img/manifest.json
---

# fin-assets — good-debt-vs-bad-debt · hi · attempt 1

## Outcome
- **Shipped: 12 images** — 9 backgrounds (every scene, rule preserved) + 3 cut-ins.
- **Dropped: 4 cut-ins** (s1-cut, s5-cut, s6-cut, s8-cut) — removed from `manifest.json`.
- **Pixabay API (search) calls: 48** across 6 rounds (16 initial + 12 + 8 + 6 + 4 + 2).
  Image downloads are separate CDN GETs, not `/api/` calls. No image reused from any prior video on either channel; no internal byte-dupes.
- Every shipped file is a real photo ≥140 KB (min 10 KB required); every shipped file has exactly one CREDITS.txt line (stale/superseded lines pruned).

## Final disposition (12 shipped)
| slot | role | what shipped | note |
|---|---|---|---|
| s1 | bg | envelopes + coffee on weathered dark wood | reads "bills/mail on a desk"; blind deboss on envelope, no legible brand |
| s2 | bg | two antique Indian coins on dark wood | object-led India/money texture; calmest rest beat; not modern currency (no demonetised deception) |
| s3 | bg | a hand offering a fanned wad of ₹ notes | "renting money"; top note ₹10, not demonetised; ₹ correct |
| s3-cutA | cut-in | sunset restaurant table set | «बाहर के खाने» dining-out |
| s3-cutB | cut-in | woman in a clothes store w/ "SHOPPING BAG" tote | «सेल की ख़रीदारी»; face turned away (not identifiable); "SHOPPING BAG" is descriptive text, not a logo |
| s4 | bg | dark antique book stacks | education = good-debt anchor; calmest bg for densest scene |
| s4-cut | cut-in | woman carrying colorful shopping bags | «कपड़े, गैजेट, छुट्टी»; face turned away; plain bags, no logo |
| s5 | bg | reading glasses on a page of dense fine print | "scrutinise the terms"; fits the MITC fine-print foot |
| s6 | bg | pile of gold coins | money/wealth for "pay more"; grey bg is mid-tone (no override) |
| s7 | bg | scientific calculator on a page of figures/graphs | "the math"; calc brand blurred; foreign body-text = texture |
| s8 | bg | vintage twin-bell alarm clock, dark moody | "act now / this month" for DO-THIS-TODAY; darkest, most on-grade image |
| s9 | bg | open country road to the horizon | "road out of the trap" closer |

## Dropped cut-ins (4) — BUILD MUST REMOVE THE DOM NODES
Each walked the full ladder (#N → synonym → texture) and produced nothing honest; per the drop authority + sourcing-note precedent, the cut-in is dropped and the scene keeps its bg. **The build must delete the referenced DOM elements or it will point at missing images:**
- **s1-cut** (`#s1cut`, «मिनिमम पेमेंट») — 3 fails: MasterCard/Payoneer logos → pelican beak ("bill" homonym) → tax figurines w/ EURO notes. The on-screen bill rows (YOU PAY ₹2,583 / INTEREST ₹1,667 / OFF THE DEBT ₹916) carry the beat.
- **s5-cut** (`#s5cut`, «चक्रवृद्धि») — 3 fails: green fields → walkers+dog → knit gloves. No honest snowball exists in the pool; the «COMPOUNDING» label + VO carry it.
- **s6-cut** (`#s6cut`, «भरना शुरू करते हैं») — 3 fails: internal dup of s3 → demonetised ₹500 → single EURO coin. The MINIMUM→+₹1,000→CUTS-YEARS-OFF flow carries it.
- **s8-cut** (`#s8cut`, «कार्ड का बिल») — 3 fails: MasterCard+Sberbank card → letter-writing flat-lay → couple holding hands ("hand holding" homonym). The DO-THIS-TODAY flow carries it.

Note: file deletion is not in this stage's bash allowlist, so the 4 orphan `.jpg`/`.src` files remain on disk (harmless — not in the manifest, so the manifest-vs-file check is unaffected). They can be swept later.

## Single per-scene filter override (the one allowed)
- **s8** (alarm clock) is the only near-black texture. Visual-inspection call (no pixel-luminance tool in the allowlist): the surround crushes flat under the system default `brightness(.62)`. Recommend the build set `#s8 .bg { filter: grayscale(.32) brightness(.85) contrast(1.02); }` so the clock stays legible under the s8 orange tint + type. This is the ONE override for the video (grade is load-bearing) — fine-tune the exact value after a test render.

## First-pass rejects (round 0) — the measured trap list, all caught by looking
- s1 / s8 **byte-identical** (deterministic top-hit collision) AND both a blank-paper mockup with a legible **SAMSUNG** phone — wrong subject + brand.
- s1-cut: multiple **MasterCard** + **Payoneer** logos (cards in jeans, not a statement).
- s2: **demonetised pre-2016 ₹500** flat-lay (yellow-olive; current is stone grey).
- s3: man writing at a desk — no rupee hand-off.
- s3-cutB: puppies in a cloth sling ("bags…held in hand" homonym).
- s4-cut: a novelty **frog figurine** with a toy suitcase.
- s5-cut: winter landscape, no snowball.
- s6: single flat **₹10-note scan** (busy note-text, not fanned notes on a desk).
- s6-cut: woman journaling — no rupee note.
- s7: leather journal + **"Kaweco … Germany"** fountain-pen brand, no calculator/ledger.
- s8-cut: giant **MasterCard** + Cyrillic **Sberbank** — a card, not a paper bill.

## Key finding (feeds future runs on this channel)
The Pixabay pool for India-money and finance-desk concepts is **small and already consumed by prior @cashguruguides videos** (50-30-20-rule-hi, emergency-fund, needs-vs-wants, pay-yourself-first). Consequences seen this run:
- **Ledger collisions on the obvious hits:** "calculator/pen on financial documents" → `emergency-fund/s1-bill.jpg` (`9a6fdd…`, the ubiquitous calculator stock) hit repeatedly; "calculator and pen on spreadsheet" → `50-30-20-rule-hi/s3.jpg`; "indian rupee coins" #1 → `50-30-20-rule-hi/s2.jpg`.
- **Rupee-note queries collapse** onto two poisoned images — the demonetised ₹500 flat-lay and a ₹10-note scan — regardless of wording.
- **Single-object queries return literal-but-wrong homonyms/foreign hits:** piggy bank→Kinder mascot, coins→zen stones / candy jar / EURO coin, calendar→workspace w/ MacBook / party balloons, vintage calculator→Pentax camera, snowball→gloves.
- **What worked (object-led, unconsumed, on-grade):** antique Indian coins, a pile of gold coins, a scientific calculator on a technical page, a vintage alarm clock, dark book stacks, glasses on fine print. Reach for these first next time; skip "credit card", "rupee notes", and generic "calculator/pen" queries — they burn calls on ledger dups and brand marks.
