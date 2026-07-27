---
summary: How to write the English (`-en`) cut of a finance video. Core rule — an `-en` cut is a US rewrite, not a translation of the Hindi one. Currency, institutions, examples, register, voice.
updated: 2026-07-27
source: Creator direction 2026-07-27 ("for english version we always have to use price in $ and all the script will be according to us standard"), applied on emergency-fund-en. Numbers live in [[money-facts-2026]].
---

# US-English script style — the `-en` cut

Every finance video ships as a pair: a Hindi/₹ cut for India
([[niches/india-finance-market]]) and an English/$ cut for the US.

## Rule zero: rewrite, never translate

**The `-en` cut is a different video with the same spine.** The first
emergency-fund-en (2026-07-23) was a line-for-line English translation of the
Haryanvi script and shipped with **rupees, lakh, "the bike breaks", "skip two
takeaways", "reach it in minutes"** — every one of which is wrong for a US
viewer. Creator caught it 2026-07-27 and the whole script was rebuilt.

What actually has to change when the market changes — a currency swap covers
none of it:

| Layer | India cut | US cut |
|---|---|---|
| Currency & scale | ₹, lakh, `1,20,000` grouping | $, thousand, `9,000` grouping |
| The shock in the hook | bike breaks, phone gone | **car won't start, layoff email, 22% credit card** |
| The emergency examples | hospital bill, urgent repair | **ER visit, layoff, transmission going out** |
| The "not for" examples | a sale, a trip | **a Black Friday deal, a vacation** |
| The small-money anchor | two takeaways | **two DoorDash orders** |
| Where the money sits | separate account, UPI, instant | **high-yield savings, a different bank, FDIC insured, 1–2 days away** |
| How saving happens | "put it in every week" | **automate it — transfer the day after payday** |
| The authority stat | RBI / PLFS | **Federal Reserve SHED, BEA, NY Fed** |

## Fixed decisions

- **Currency:** `$` everywhere, US comma grouping, no lakh/crore. Round numbers
  ($50, $1,000, $3,000, $9,000) — never a converted rupee figure.
- **Voice:** ElevenLabs **Brian** `nPczCjzI2devNBz1zQrb`, `eleven_multilingual_v2`,
  defaults. Locked alongside the Hindi voices in [[niches/india-finance-market]].
- **Speech rate ≈ 15 chars/s** (vs Hindi 12.5) — the same script runs ~25–30%
  shorter in English. Budget length per cut; never reuse the Hindi timing table.
- **Titles + descriptions:** English (unchanged channel rule, both cuts).
- **Stock photography is part of the localization.** A motorcycle in a workshop,
  a Swiss 5-franc coin and a pile of euro coins all shipped in the first `-en`
  cut. Sweep every photo for non-US currency, signage and vehicles.
- **Institutions named generically:** high-yield savings account, checking
  account, ACH transfer, FDIC. Never a specific bank, app or fund.

## Register

Direct, second-person, a little blunt — the same voice as the Hindi cut, not a
softer "American finance channel" register. Contractions, short sentences, one
idea per line. Mild self-aware humor lands ("automatically, not heroically";
"not there when you're bored at midnight"). Keep the mock-scold sign-off beat
("then don't say nobody warned you") — it's channel signature and it survives
translation.

## Compliance note

[[niches/us-market-2026]]: YouTube's 2026 clarification makes **AI "expert"
personas in finance ineligible** for monetisation regardless of added value.
The `-en` cuts narrate general, sourced consumer-money facts and name no
products — keep it that way, and never let the narrator claim credentials.

Related: [[money-facts-2026]] (every number) · [[niches/india-finance-market]]
(the Hindi counterpart) · [[haryanvi-hindi-script-style]] (its style note).
