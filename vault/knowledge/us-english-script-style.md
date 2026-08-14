---
summary: How to write a finance video for the US market — the only finance lane since 2026-08-15. Core rule — write FOR the US from scratch, never translate or localise. Currency, institutions, examples, register, voice.
updated: 2026-07-27
source: Creator direction 2026-07-27 ("for english version we always have to use price in $ and all the script will be according to us standard"), applied on emergency-fund-en. Numbers live in [[money-facts-2026]].
stage: ADOPTED — the register for every -en cut
---

# US-English script style

**Since 2026-08-15 this is the only finance lane.** Every finance video is a
single US/$ cut for @moneymavens101 ([[channels]] §E).

## Rule zero: write for the US, never translate or localise

**A US video is not a generic money video with the currency swapped.** The first
emergency-fund-en (2026-07-23) was a line-for-line English translation of the
Haryanvi script and shipped with **rupees, lakh, "the bike breaks", "skip two
takeaways", "reach it in minutes"** — every one of which is wrong for a US
viewer. Creator caught it 2026-07-27 and the whole script was rebuilt.

What actually has to change when the market changes — a currency swap covers
none of it:

The table below is kept as the worked example of that failure — left column =
what shipped and was wrong, right column = the US-correct choice.

| Layer | ❌ what was wrong | ✅ US |
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
  defaults. Voice id and rate live in `tools/format.json`, never here.
- **Speech rate ≈ 17.6 chars/s** for MEDIUM/LONG (`tools/format.json`; a SHORT
  cut runs ~9% long on that key — re-measure). Budget length before writing.
- **Titles + descriptions:** English.
- **Stock photography is part of the localization.** A motorcycle in a workshop,
  a Swiss 5-franc coin and a pile of euro coins all shipped in the first `-en`
  cut. Sweep every photo for non-US currency, signage and vehicles.
- **Institutions named generically:** high-yield savings account, checking
  account, ACH transfer, FDIC. Never a specific bank, app or fund.

## Register

Direct, second-person, a little blunt — not a soft "American finance channel"
register. Contractions, short sentences, one
idea per line. Mild self-aware humor lands ("automatically, not heroically";
"not there when you're bored at midnight"). Keep the mock-scold sign-off beat
("then don't say nobody warned you") — it's channel signature and it survives
translation.

## Compliance note

[[niches/us-market-2026]]: YouTube's 2026 clarification makes **AI "expert"
personas in finance ineligible** for monetisation regardless of added value.
The `-en` cuts narrate general, sourced consumer-money facts and name no
products — keep it that way, and never let the narrator claim credentials.

Related: [[money-facts-2026]] (every number)
· [[channels]] (§E @moneymavens101).
