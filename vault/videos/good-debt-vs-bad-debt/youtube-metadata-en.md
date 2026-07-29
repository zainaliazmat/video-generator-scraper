---
summary: Publish pack for the US/English ($) cut of «Good Debt vs Bad Debt — the minimum-payment trap». Title options (US English), description with real chapter timestamps from timing.json, verified-autocomplete tags, 3 thumbnail variants + chosen line, Gate 2 compliance. Fresh YouTube-autocomplete pull was possible this run (tools/autocomplete.py, 2026-07-29, gl=us hl=en) — both `credit card minimum payment trap` and `good debt vs bad debt` are verified live US strings. Channel-sameness: this is the 5th consecutive blockframe-9 on @moneymavens101 — enforcement line crossed.
updated: 2026-07-29
source: Chapter times = scene_start per line in studio/videos/good-debt-vs-bad-debt-en/assets/voice/timing.json (total 178.582s; master FINAL-1080p-en.mp4 = 2:59). On-screen numerals verified against the built render vault/videos/good-debt-vs-bad-debt/src/en/index.html (build-calculator locked). Search evidence = fresh tools/autocomplete.py pulls 2026-07-29 (gl=us, hl=en), recorded below. Numerals traced to [[script-en]] fact-trace + the s7 build output.
---

# YouTube publish pack — Good Debt vs Bad Debt (English / USA cut)

**Channel:** @moneymavens101
**Video:** `studio/videos/good-debt-vs-bad-debt-en/renders/FINAL-1080p-en.mp4` (2:59 · 1920×1080 · 178.6s)
**Thumbnails (creator picks at upload):** `vault/videos/good-debt-vs-bad-debt/src/thumbs/thumbnail-en-v1.png` · `-v2.png` · `-v3.png` (source: `vault/videos/good-debt-vs-bad-debt/src/thumbs/index.html` §env1/§env2/§env3 — the hi §v1/v2/v3 sections are untouched in the same project)

| Variant | Composition | Numerals (all on-screen in the en render) |
|---|---|---|
| **v1 — recommended** | THE PUNCH — centred red mega **$9,506** over the en calculator/notepad texture (en s7). Amber "JUST INTEREST" tag, sub "on a $6,000 card · minimum only". Centred → breaks the channel's left-aligned streak. | $9,506 · $6,000 (s7) |
| v2 | THE TIME TRAP — left, white "215 MONTHS" + red mega "18 YEARS" over the en statement texture (en s5). "MINIMUM = TRAP" tag. The channel-continuity option (closest to the last-3 family). | 215 · 18 · $6,000 (s7) |
| v3 | THE SPLIT — left, red mega **$110** over the en $1-bill texture (en s1). "MINIMUM $170" tag, sub "is just interest · debt drops only $60". The month-1 anatomy. | $170 · $110 · $60 (s1) |

**chosen:** v2 _(creator pick, scheduled 2026-07-29 — youtu.be/gC2QlQiLqhw; fin-archive reads this back)_

Legibility: all three clear the assert (largest line ≥40% of width at 320×180 — v1 `$9,506` ~55%, v2 `18 YEARS` ~65%, v3 `$110` ~42%; v3's mega was sized to 240px specifically to clear 40% with a 4-glyph string). `npm run check` = **21/21 WCAG AA, 0 runtime/layout/motion issues** (one cosmetic `timeline_track_too_dense` warning — the cost of co-hosting hi+en in one project file, per the "one HyperFrames project" contract). Backgrounds are the en video's OWN scene photos (en s7/s5/s1, re-graded under the design scrim) — distinct md5s from the hi thumbnails, no new/cross-video images, no AI-collage, no shocked-face. Red is the trap throughout (this video's colour thesis); green is deliberately absent — the thumbnail sells the trap, not the escape.

> **Numeral note (read before touching the thumbnail):** the interest figure is **$9,506**, not the $9,496 that appears in `script-en.md`/`storyboard-en.md`. Those were the pre-build hand-estimates; the **build calculator regenerated it to $9,506** (script build-handoff #5 explicitly delegates the on-screen integers to the calculator — "never hand-derived"). The render, the thumbnail and this description all say **$9,506** — consistent. Do not "correct" it back to $9,496.

## Thumbnail sameness (last 3 on @moneymavens101 — vault packs)

emergency-fund ("ONE REPAIR FROM BROKE", car-in-shop · red/left/photo) · needs-vs-wants
("YOU THINK $86. IT'S $219." over $100 bills · red/left + 12-tick strip) · pay-yourself-first
(v1 green **centred** photo-**free** "$4,800" **or** v2 red left "EMPTY BY THE 20TH?" — `chosen:`
still unrecorded). Dominant channel composition = **red-accent, left-aligned text over a money
photo**. None used $9,506, "18 YEARS", the $170/$110/$60 split, or a red centred-mega-over-photo
layout, so **no near-duplicate** here. v2 sits closest to the last-3 family (red/left/photo) — the
safe continuity pick; **v1 (red centred over a photo) and v3 (split) vary the composition** while
keeping the red-trap semantics. (pay-yourself-first introduced a centred block, but in **green and
photo-free**; v1 here is the first **red centred over a photo** on the channel — distinct.)

## Search evidence — FRESH autocomplete pull (2026-07-29, gl=us hl=en)

`tools/autocomplete.py` pull, 10 seeds, each fetched; empties/noise recorded, not papered over.

**Verified live US clusters (the demand this video can title into):**
- **The minimum-payment trap is a real US search string** — `credit card minimum payment trap`
  and `minimum payment trap` both autocomplete (our hook IS the query, same as the hi cut).
- `credit card minimum payments explained` / `credit card minimum payment or full payment` /
  `credit card minimum amount due` = the "how the minimum works / what is minimum due" lane.
- `what happens if you only pay the minimum` (+ `…the minimum payment on my credit card`) =
  the informational "what happens if I pay only the minimum" lane — strong curiosity string.
- **`good debt vs bad debt` is verified live in the US** — a real difference from the hi cut,
  where the pure-Hindi `acha karz aur bura karz` was dead. In English the concept name works
  as a search string, so it can lead a title (option 4). But `good debt vs bad debt robert
  kiyosaki` and `good debt vs bad debt dave ramsey` also autocomplete: **the generic concept is
  owned by Kiyosaki/Ramsey** — our differentiator is the specific minimum-payment math
  ($6,000 → $9,506 / 215 months), which no competitor autocomplete string claims.
- `credit card interest` / `credit card interest rates` / `credit card interest calculation` =
  interest lane. `how to pay off credit card debt` (+ fast/low-income variants) /
  `credit card debt payoff strategy` = the payoff lane.

**Noise recorded (NOT used as US tags):** the `credit card minimum payment` seed is heavily
contaminated with non-US strings (`…kya hota hai`, `…telugu / tamil / malayalam / sinhala`,
`…axis bank`) — YouTube's global volume for that phrase is India-heavy; only the clean US strings
above were kept. `is paying minimum on credit card bad` returned no exact match, reformulating to
`pay minimum on credit card` / `paying minimum amount due on credit card` (kept the US one).

**Competitor scoreboard:** `library.db` is **empty for this lane** (run.json `owed`:
"no comparable videos ≥100 views ≥240s" — scrape still owed, orchestrator's step, not run here).
Only competitor signal is from autocomplete: Kiyosaki/Ramsey own generic `good debt vs bad debt`;
no autocomplete competitor owns the specific minimum-payment math. Title into the math + the trap.

## Title (pick one — US English; $ figures, never ₹)

1. **The Credit Card Minimum-Payment Trap: $6,000 Costs You $9,506** (61 chars)
   ← **recommended.** Leads with the verified `credit card minimum payment trap` cluster
   (our hook = the query), carries the render's punch — $9,506 interest on $6,000. Pairs with
   thumbnail **v1** (same number). Highest search + highest shock.
2. Only Paying the Minimum? Here's What It Actually Costs (54) — the verified `what happens if
   you only pay the minimum` informational lane, curiosity-first, no number. Pairs v1 or v3.
   Highest search floor.
3. Pay Only the Minimum on $6,000? That's 215 Months of Debt (57) — the time-shock
   (`pay minimum on credit card` cluster + the 215-month / 18-year figure). Pairs **v2**.
4. Good Debt vs Bad Debt — and the Minimum-Payment Trap (52) — concept-lead on the verified
   `good debt vs bad debt` string, for the concept-search browser. Kiyosaki/Ramsey own the
   generic concept; our angle is the trap math — use only if the creator wants the concept name
   to lead. Pairs v1/v3.
5. Your $170 Minimum Is Mostly Interest — Here's the Math (54) — the month-1 split hook
   ($110 of your $170 is interest). Pairs **v3**.

*(The video's concept is "good debt vs bad debt", and unlike the hi cut that string IS a live US
search term — but the minimum-payment-trap cluster is broader and the trap-math is our
differentiator against Kiyosaki/Ramsey, so the recommended title leads with the trap and keeps the
good-vs-bad framing in option 4 + the description + tags. Same lesson as the sibling packs: title
the demand cluster, not just the internal name.)*

## Description

```
On a credit card, the most dangerous words are "minimum payment." It feels safe. It's a trap. On a $6,000 balance at around 22% APR, the minimum runs about $170 a month — and $110 of that is pure interest. Only $60 comes off what you actually owe. Keep paying just the minimum and that $6,000 takes about 215 months — roughly 18 years — to clear, and costs you $9,506 in interest. That's more than you borrowed.

In this video: what debt really is (renting money — the interest is the rent), good debt vs bad debt (good debt buys something that grows in value or income; bad debt just buys consumption), how the minimum actually works (it's about 1% of the balance plus that month's interest, and the interest is paid first — so your principal barely moves), and how compounding runs against you on a card. Then the one move that beats it: pay more than the minimum. Every extra dollar goes straight at the principal.

Debt isn't the enemy — thoughtless debt is. If you can't buy it in full, don't carry it on the card.

⏱ CHAPTERS
0:00 The minimum payment is a trap (the month-1 math)
0:18 What you'll know by the end
0:30 What debt really is — renting money
0:53 Good debt vs bad debt
1:18 How the minimum actually works
1:38 The only way out — pay more than the minimum
1:56 The math — $6,000 at ~22%, minimum only
2:24 Do this today
2:41 Recap

📊 SOURCES
• Minimum payment ≈ 1% of the balance + that month's interest, ~$35 floor, interest covered first (no negative amortization) — issuer cardmember agreements (Chase, Capital One) + CFPB Regulation Z, 2026
• ~22% APR = illustrative, typical US card range (about 20–24%); not any single bank's number — Federal Reserve G.19 assessed interest / WalletHub 2026
• $6,000 → 215 months / $9,506 interest = computed from the $35-floor amortization model (B₀=$6,000, ~22% APR, paying only the 1% + interest minimum, stop at balance ≤ 0) — for illustration only

⚠️ This video is general financial education, not financial advice. No bank, card, or product is recommended. $6,000 at ~22% is an example — put in your own card's APR and balance to get your own number.

#CreditCard #MinimumPayment #CreditCardDebt #GoodDebtVsBadDebt #PersonalFinance
```

Chapter times are the render's truth: `scene_start` per line in
`studio/videos/good-debt-vs-bad-debt-en/assets/voice/timing.json` (floored to the second;
total 178.582s = 2:58.6 ≈ 2:59). First chapter 0:00, 9 chapters, each ≥10s apart — YouTube-valid.
Every $ figure in the description ($6,000 · $170 · $110 · $60 · 215 months · 18 years · $9,506 ·
~22% · 1% · $35) is on-screen in the render (build-calculator locked). No ₹ anywhere.

## Tags (paste as a comma list)

```
credit card minimum payment, credit card minimum payment trap, minimum payment trap, credit card minimum payments explained, what happens if you only pay the minimum, credit card minimum payment or full payment, credit card minimum amount due, good debt vs bad debt, good debt bad debt, credit card interest, credit card interest rates, credit card interest calculation, how to pay off credit card debt, credit card debt payoff strategy, pay minimum on credit card, credit card debt, how credit card minimum payment works, personal finance
```

The first 15 are **autocomplete-verified 2026-07-29** (gl=us, hl=en — see the evidence section).
The last 3 (`credit card debt`, `how credit card minimum payment works`, `personal finance`) are
topical/descriptive — no direct US autocomplete this run. Non-US strings (the telugu/tamil/hindi/
axis-bank noise that surfaced on the broad seed) are deliberately absent — they belong to the ₹
cut. No `…hindi` / Hinglish tag here (standing rule — search clusters are per-market).

## Gate 2 compliance

- **Altered-content disclosure toggle: set "No".** Narration is synthetic (ElevenLabs "Brian")
  but there is **no realistic synthetic media presented as real** — motion graphics + licensed
  stock photos only, so YouTube's altered-content disclosure is not triggered and **no on-screen
  disclosure is required or present**. The narrator is a **voice, not a persona**: no name, no
  credentials, no "as your advisor" framing, and the video makes **no product/card/fund pick**
  (persona + no-recommendation rules enforced at script/audit — the 2026 AI-expert-persona
  carve-out hits US finance hardest, [[../../knowledge/niches/us-market-2026]]). The description
  carries the education-not-advice disclaimer.
- **Channel-level sameness — ⛔ FLAG, the enforcement line is now crossed.** Uploads on
  @moneymavens101: 50-30-20 (blockframe-9, 3:43) → emergency-fund (9, 2:46) → needs-vs-wants
  (9, 2:50) → pay-yourself-first (9, 2:58) → **THIS good-debt-vs-bad-debt (9, 2:59) = the 5th
  consecutive near-identical blockframe-9 structure** (hook → roadmap → concept → rule → audit →
  action → math-counter → do-today → recap). The pay-yourself-first-en pack explicitly warned
  "the next upload would be the 5th" — this is that upload. Per Gate 2, **mass-production sameness
  is the one enforcement category judged channel-level.** This video is still fine to publish
  (sameness is actionable going forward, not retroactively), **but the next cut MUST break the
  pattern** — medium-tier per-line-chapters, a different length band, or a reordered/merged beat
  structure. A 6th blockframe-9 would be an indefensible template run. **Escalate to the creator/
  orchestrator before the next en cut is scripted.** (Same flag, same count, now on BOTH channels —
  the hi cut crossed the identical line.)
- **Category:** Education. **Language:** English (US). **Audience:** not made for kids.
- **End screen / pinned comment:** cross-link the ₹/Hindi cut (@cashguruguides,
  [[youtube-metadata-hi]]), and vice versa.
- **Pinned comment suggestion:** "Open your card's app today — pay the minimum plus at least $20.
  Drop just your card's APR in a reply (a guess counts)." (asks for the one number everyone can
  answer — lowest-friction comment, same pattern as the sibling packs.)

## If this underperforms

The minimum-payment-trap lane has real US demand but Kiyosaki/Ramsey own the generic
good-vs-bad concept. Levers in order: swap to title #2 (curiosity/informational, highest floor),
then re-test the thumbnail (v1 ↔ v2 is a genuine composition A/B — the $9,506 punch vs the
18-YEARS time-trap — not a variant tweak).

Related: [[script-en]] · [[storyboard-en]] · [[audit-en]] · [[youtube-metadata-hi]] · [[../pay-yourself-first/youtube-metadata-en]] (house-style reference) · [[../../knowledge/design-finance-blockframe]]
