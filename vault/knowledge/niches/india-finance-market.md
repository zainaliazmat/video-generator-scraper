---
summary: The India pivot for the personal-finance channel — audience, currency (INR ₹), language, and the money context for 20-28yo Indians. Retarget of the earlier Pakistan/PKR framing. ⚠ LANGUAGE CORRECTED — the hi cut is **Standard Hindi** (creator 2026-07-28), not the Haryanvi-flavoured Hindi this file was written for; §"Language" below is the live rule and everything above it that says Haryanvi is superseded. Voice and rate live in tools/format.json, never here.
updated: 2026-07-22
source: creator direction 2026-07-22 + deep-research run wf_388d2df8-2e0. INR salary/expense figures below are LOW-confidence (that half of the research returned no verified claims) — verify before publishing.
stage: ADOPTED — niche research; figures carry their own dates
---

# India finance market — channel retarget

Creator direction (2026-07-22): the finance videos move to **India**. Currency **INR (₹)**, audience **young Indian adults 20-28** (first salaries), narration in **Hindi with a Haryanvi accent** (funny, attention-grabbing, real-person). See [[haryanvi-hindi-script-style]] for how to write it and [[indian-business-culture-slang]] for flavor. Replaces the Pakistan/PKR/Rs. framing in the earlier scripts.

## Language — the live rule (creator 2026-07-28)

**The hi cut is written in Standard Hindi.** Haryanvi was tried on one video and
retired: it did not survive contact with the finance register, and every cut since
50-30-20 is standard. [[../haryanvi-hindi-script-style]] and
[[../indian-business-culture-slang]] are kept as reference if a Haryanvi lane ever
returns — **do not read them for a finance script.** This decision previously lived
only in `.claude/agents/fin-script.md`, which is procedure, not memory; it belongs
here (`vault/CLAUDE.md`, the two-home rule).

## Fixed decisions

- **Currency:** ₹ / INR everywhere. On-screen text stays **English/Hinglish** (₹40,000, SAVE, 3 MONTHS) — clearest, matches the English-titles rule. Narration = Standard Hindi.
- **Voice and rate:** `tools/format.json cuts.hi` is the only home — it changes when the voice does, and a copy here would go stale the day it did. (It already had: this line named the retired Haryanvi voice.)
- **Business-culture flavor:** lean on Marwari/Gujarati thrift + dhandho framings for credibility and humor.
- **Titles/descriptions:** English (unchanged rule).

## Money context for 20-28yo Indians

**Now sourced — see [[money-facts-2026]]** (PLFS 2025 earnings, RBI savings rate,
AMFI SIP minimums, metro rents). That note is the only place numbers live; don't
restate them here. Headlines: salaried avg **₹24,217/mo** (PLFS, official), net
household financial savings **7% of GNDI** (RBI FY25), metro needs eat **60-70%**
of income, SIP floor **₹500** (₹250 Chhoti SIP).

Vehicles to reference **generically** (never a specific product): RD, FD, SIP,
PPF, savings account, **UPI** for instant transfers.

## Language decision (2026-07-27)

Creator direction: the 50-30-20 pair is scripted in **standard Hindi, not
Haryanvi** — Haryanvi stays available for other videos but the default finance
register is now clean Hindi with a Hindi voice. [[haryanvi-hindi-script-style]]
remains the flavor guide when Haryanvi is wanted.

## Voices (locked 2026-07-27)

| Register | Voice | ID |
|---|---|---|
| **Standard Hindi — LOCKED channel identity for @cashguruguides (2026-07-28)** | Harsh — Clear & Calm Documentary Narrator (`hi`, standard accent, informative_educational) | `HTUuC7OeeEt6OL5fViVe` |
| Haryanvi — RETIRED for finance | Prayan — Haryanvi Customer Care Agent | `9BHTbeEKC5ZqMmvZfLW6` |
| US English (all `-en` cuts) | Brian | `nPczCjzI2devNBz1zQrb` |

**Narrator identity settled (creator decision 2026-07-28).** The channel had drifted
to two narrators across three uploads — `needs-vs-wants` and `50-30-20-rule-hi` on
Harsh, `emergency-fund` on Prayan. **Standard Hindi (Harsh) is the channel voice.**

Consequences:
- Every future `-hi` script uses Harsh. [[haryanvi-hindi-script-style]] is no longer
  the default style guide for finance — it stays available for other work only.
  A Haryanvi-marked script read by a standard-Hindi voice is the failure to avoid.
- The scheduled `emergency-fund` upload ("…Explained in Haryanvi") is genuinely
  Haryanvi, so it is internally honest and does **not** need retitling or
  re-rendering. It stands as the one-off; the channel converges on Harsh from here.

Harsh was picked over Ranbir Merchant / Ranga (both narrative_story, more
"brand-film" than explainer) and Bunty (characters_animation — too cartoonish to
carry money advice). A/B samples of the same line for all four sit in
`studio/videos/50-30-20-rule-hi/assets/voice/_voice-samples/`.

**Settings:** ElevenLabs defaults (stability 0.5 / similarity 0.75 / **style 0**).
Style 0.25 was tested and rejected — it slows delivery ~10% with no gain in warmth.

**Hindi speech rate ≈ 12.5 chars/s** (vs English ≈ 15 chars/s at the same
settings). Budget Hindi script length accordingly — a 1:1 translation of an
English script runs ~30% longer. Sister fact to the 12.0–12.2 chars/s Urdu rate
in [[../workflows/voiceover-tts]].

## Open items

- Native-Haryanvi proof of the first full Haryanvi script.
- Note Indian number formatting: **lakh** (₹1,20,000 = "एक लाख बीस हजार"), and the `1,20,000` comma grouping if we ever localize on-screen numerals.
