---
summary: US/English script for «Good Debt vs Bad Debt — the minimum-payment trap». 9 VO segments (blockframe-9, ~2:47 target 165s), USD, Brian voice, @moneymavens101. US rewrite (not a translation) — hero math $6,000 @ ~22% APR, US "1% + interest" minimum, $35 floor. Every number traces to videos/good-debt-vs-bad-debt/facts-staging.md ($ SET).
updated: 2026-07-28
source: creator brief (run.json 2026-07-28) + facts-staging.md attempt 1 ($ SET); structure mirrors script-hi.md, register per knowledge/us-english-script-style.md; hero-math per orchestrator's en constraints
---

# «Good Debt vs Bad Debt» — English / USA edition

**Studio project (to build):** `studio/videos/good-debt-vs-bad-debt-en`
**Language:** US English, en-US. **Voice:** ElevenLabs **Brian** `nPczCjzI2devNBz1zQrb`, `eleven_multilingual_v2`, style 0.
**On-screen text:** English. **Titles + description:** English.
**Style:** blockframe-9 motion graphics, 16:9, target 165s. Educational only — no host
persona, no first-person expertise, no product/card/fund pick; the credit card is the
generic instrument, APR/minimum appear only as price evidence (Fed G.19 + issuer
agreements + CFPB).

> **US REWRITE, NOT A TRANSLATION** (us-english-script-style.md rule zero). The Hindi
> script was read for structure only. Everything here is US-market: dollars only, US card
> APR (~22%, not India's ~40%), the US **"1% of balance + interest"** minimum
> mechanism (NOT India's "5% of total due" — different math, facts-staging Claim $-2),
> $6,000 illustrative balance (typical US revolving debt, not a conversion of the India
> cut's fifty-thousand-rupee balance), US institutions in the source foots. **A rupee
> anywhere in this cut is a hard fail** — zero rupee signs, no lakh, no India institution,
> no cross-market figure.

**Engine rule:** digits are **spelled out** in the VO text below (bare Latin digits
are a coin-flip TTS reading in ElevenLabs). On-screen numerals carry the exact
figures, `Intl.NumberFormat("en-US")` grouping (`$9,496`).

**Colour intent (thesis-derived — storyboard formalises the 4-line table):**
`--warn` red = the **interest trap / minimum-payment trap / bad debt** (the loss);
`--fund` green = **good debt / the escape (paying more) / balance falling**;
`--target` amber = the **card under examination / the decision**;
`--pop` orange = the do-this-today CTA. (Per design-finance-blockframe §2 — on a
credit-card video red MUST be the interest trap, not reused blindly.)

## Hero-math (LOCKED — chosen by fin-script, handed to the build calculator)

| Input | Value | Source |
|---|---|---|
| Illustrative balance B₀ | **$6,000** | fin-script pick — US-sensible revolving balance, typical $5,000–$6,000 band (facts-staging $ SET). NOT a rupee conversion. |
| APR (label "illustrative — typical range") | **~22%** → monthly i = 0.22/12 = **0.0183333** | Claim $-1 (Fed G.19 22.15% assessed-interest; WalletHub/Forbes 20–24%) |
| Minimum rule | **max( 1%·B + interest , $35 floor )** | Claim $-2 (Chase/Capital One agreements; $35 = the "commonly ~$35" midpoint) |

**Model (facts-staging THE TERMINATING MODEL, $ spec):** in the percentage regime
principal falls exactly 1%/month, so **B(t) = 6000 · 0.99ᵗ**. Floor $35 binds at
B ≈ $1,235; a flat-$35 tail then clears it. **VO speaks only the floor-independent
robust anchors** — the month-1 split ($170 / $110 / $60), "a year barely moves it"
(still over $5,000 owed), and the payoff as a **round range** ("the better part of two
decades" / "more in interest than you borrowed"). The false-precise on-screen integers
(**$5,318 · ~215 months · $9,496 interest**) are **locked by the build calculator**
(the $35-floor model) — displayed on screen, never spoken, never hand-derived here.

## Timing budget

English narration ≈ **15.0 chars/s** (`format.json cuts.en`). Char counts are the
budget estimate only; the build step regenerates + ffprobe-measures each clip and adds
the per-scene 0.4s lead-in / 1.0s tail before locking scene durations.

| # | Scene | chars | est. |
|---|---|---|---|
| en1 | Hook — the minimum is a trap (month-1 split) | ~289 | ~19.3s |
| en2 | Roadmap — four things | ~151 | ~10.1s |
| en3 | Concept — debt is renting money | ~283 | ~18.9s |
| en4 | Rule — good debt vs bad debt | ~324 | ~21.6s |
| en5 | Audit — how the minimum works + compounding against you | ~327 | ~21.8s |
| en6 | Action — pay more than the minimum | ~257 | ~17.1s |
| en7 | The math — $6,000 @ ~22%, minimum only | ~404 | ~26.9s |
| en8 | Do this today — minimum + $20 | ~240 | ~16.0s |
| en9 | Recap + CTA | ~227 | ~15.1s |
| | **Total** | **~2,502** | **~2:47** |

Band check: 165s × 15 c/s = 2,475 ±10% → 2,228–2,723. Script ~2,502 (101.1%). Inside.

---

## en1 — HOOK

**VO**
> On a credit card, the most dangerous words are 'minimum payment.' It feels safe. It's a trap. On a six-thousand-dollar balance, the minimum runs about a hundred seventy dollars — and a hundred ten of that is pure interest. Only sixty dollars comes off what you owe. Today, the actual math.

**On screen** — the month-1 split IS the focal shock.
- kicker: `The most dangerous words on a credit card`
- huge (warn): `"MINIMUM PAYMENT"`
- month-1 anatomy ($6,000 balance · minimum due):
  ```
  YOU PAY          $170
  → INTEREST       $110
  → OFF THE DEBT    $60
  ```
- stamp (warn): `IT'S A TRAP`

**Visuals** — bg keyword: `credit card and paper bills on desk`; cut-in
`hand holding phone with card statement` on «minimum payment». 3 bg crossfades,
slow Ken Burns push-in. (US card art — no foreign currency/signage in frame.)

---

## en2 — ROADMAP

**VO**
> Four things: what debt really is, good debt versus bad debt, how the minimum works, and how interest compounds against you. Then one move to make today.

**On screen**
- kicker: `By the end you'll know`
- chips (2×2 — max 3 per row): `WHAT DEBT REALLY IS` · `GOOD vs BAD DEBT` /
  `HOW THE MINIMUM WORKS` · `COMPOUNDS AGAINST YOU`
- sub: `Then one move for today`

**Visuals** — bg keyword (calmest — roadmap rest beat, still carries a photo per
the every-frame-has-image rule): `stack of US dollar bills flat-lay texture`, slow drift.

---

## en3 — CONCEPT — debt is renting money

**VO**
> First — what debt really is. Debt is renting money, and the interest is the rent. Renting money isn't always wrong — it depends what you rent it for. Rent a tool that earns, and the rent pays for itself. Rent it for a dinner or a sale, and it's gone by morning — the rent runs for years.

**On screen**
- kicker: `First — what debt really is`
- huge: `DEBT =` + accent span `RENTING MONEY`
- sub: `Interest is the rent`
- two-item contrast: `A TOOL THAT EARNS → rent worth it` (fund) ·
  `A DINNER, A SALE → rent on a ghost` (warn)

**Visuals** — bg keyword: `rolled dollar bills handed over`; cut-in
`restaurant dinner table` on «a dinner», `retail sale shopping bags` on «a sale».

---

## en4 — RULE — good debt vs bad debt

**VO**
> So — the rule. Good debt buys what grows in value or income: a degree, a skill, a business. While you pay it down, it's earning for you. Bad debt just buys consumption — clothes, gadgets, a vacation, gone before the bill even lands. Worst of all: a credit-card balance. But debt is only good when the return beats the interest.

**On screen** — two-column classifier (the focal).
- kicker: `The rule`
- col `GOOD DEBT — value grows` (fund): chips `A DEGREE` · `A SKILL` · `A BUSINESS`
- col `BAD DEBT — just spending` (warn): chips `CLOTHES` · `GADGETS` · `VACATIONS`
- stamp (warn): `CARD BALANCE = WORST`
- foot (the honest caveat): `Even good debt is only "good" if the return beats the interest`

**Visuals** — bg keyword: `graduation cap on stack of books` (good side);
cut-in `shopping bags on arm` on «clothes, gadgets, a vacation» (bad side). Densest scene →
calm bg, per design §5.

---

## en5 — AUDIT — how the minimum works + compounding against you

**VO**
> Now, how the trap works inside. Your minimum is about one percent of the balance, plus that month's interest — and interest is paid first. So the bank always collects, and barely one percent of the balance comes off. Then it's interest on the interest. Compounding grows your money when you invest — on a card, it runs against you.

**On screen**
- kicker: `How the minimum actually works`
- rule block: `MINIMUM = 1% of balance + interest` → `interest is paid FIRST` →
  `bank's interest: always covered · your principal: barely moves`
- huge (warn): `INTEREST ON INTEREST`
- snowball line: `COMPOUNDING — for you when you invest, against you on a card`
- foot: `US min = 1% + interest (Chase / Capital One agreements · CFPB Reg Z) · $35 floor`

**Visuals** — bg keyword: `credit card statement close-up` (paper, not a phone
screen — design §7); cut-in `snowball rolling downhill` on «compounding» (the
snowball-against-you motif). Densest scene → calm bg.

---

## en6 — ACTION — pay more than the minimum

**VO**
> So how do you beat it? Pay more than the minimum — that's the whole game. The minimum is built to keep you paying for years. The day you add even a little on top, years of interest start falling away — because every extra dollar goes straight at the principal.

**On screen**
- kicker: `The only way out`
- huge: `PAY MORE THAN THE` + fund span `MINIMUM`
- flow: `MINIMUM` → `+ $20/mo` → `CUTS YEARS OFF`
- sub: `Every extra dollar hits the principal directly`

**Visuals** — bg keyword: `hand paying with phone banking app` (screen dim/angled,
not the bright focal — design §7); cut-in `mobile payment confirmation` on
«add even a little on top».

> **No fabricated figure:** the `+$20` amount is the creator's action step (run.json);
> the *effect* stays qualitative ("cuts years off") because facts-staging supplies no
> build-locked payoff for the minimum-plus-$20 case. See build-handoff #6.

---

## en7 — THE MATH ($6,000 @ ~22%, minimum only)

**VO**
> Now the full math. A six-thousand-dollar balance at around twenty-two percent — typical if you carry a balance — paying only the minimum. A year in, twelve payments made, you still owe over five thousand dollars. It's barely moved. Keep paying the minimum, and you stay in debt the better part of two decades — and pay more in interest than you borrowed. On six thousand, that's over nine thousand in interest.

**On screen** — the figures are the visual; reveal in three anchors, punch on the last.
- setup: `$6,000 · ~22% APR · minimum only`
- APR label (never a single issuer / never a decimal): `~22% — illustrative, typical range`
- min formula: `minimum = 1% of balance + interest (or $35)`
- reveal rows (build-calculator locked):
  ```
  AFTER 1 YEAR     still $5,318 owed
  TIME TO CLEAR    215 MONTHS  (~18 years)
  INTEREST PAID    $9,496
  ```
- huge (warn, the punch): `$9,496 INTEREST > $6,000 BORROWED`
- foot: `$35-floor model · Fed G.19 / WalletHub 2026 · figures build-calculator locked`

**Visuals** — bg keyword (calmest — densest scene): `dark desk with calculator and
notepad`, slow drift; the numbers carry the scene. Counter/reveal animates, no busy bg.

---

## en8 — DO THIS TODAY

**VO**
> So here's today's move. Open your card's app and pay the minimum plus at least twenty dollars — more if you can. And one hard rule: if you can't buy it in full, don't carry it on the card. Debt isn't the enemy. Debt you never thought about is.

**On screen**
- stamp (pop): `DO THIS TODAY`
- chips + arrows: `OPEN YOUR CARD APP` → `PAY MINIMUM + $20` → `THIS MONTH`
- rule: `Can't buy it in full? Don't carry it on the card.`
- sub: `Debt isn't the enemy — thoughtless debt is.`

**Visuals** — bg keyword: `hand tapping phone banking app close-up` (screen not the
bright focal — design §7).

---

## en9 — RECAP + CTA

**VO**
> So — straight talk. Debt is renting money. Good debt grows something; bad debt just drains you. The minimum is a trap — always pay more than it asks. Then don't say nobody warned you. For money talk this straight — hit subscribe.

**On screen**
- recap chips (2×2 — max 3 per row): `DEBT = RENTED MONEY` · `GOOD GROWS, BAD DRAINS` /
  `THE MINIMUM = A TRAP` · `ALWAYS PAY MORE`
- stamp (pop): `SUBSCRIBE`

**Visuals** — bg keyword: `young man confident with phone` (US setting, no foreign
signage/currency in frame).

---

## Fact trace (every number → facts-staging.md, $ SET)

| Number in script | Where | facts-staging.md line |
|---|---|---|
| $6,000 balance | en1, en7 | fin-script pick — US-sensible illustrative revolving balance ("$ SET" intro: "typical US card debt is ~$5,000–$6,000"). NOT a rupee conversion. |
| $170 minimum (month 1) | en1 | COMPUTED — $6,000 @ 22%: min = 1%·6000 + i·6000 = $60 + $110 = $170 (floor-independent) |
| $110 interest (month 1) | en1 | COMPUTED — i·B = 0.0183333 × 6000 = $110 |
| $60 off principal (month 1) | en1 | COMPUTED — 1%·B = $60 (the "principal falls exactly 1%/month" model feature) |
| ~22% APR ("illustrative, typical range") | en5, en7 | Claim $-1 — ~22% carriers / 20–24% band; "say ~22% / north of 20%, never a decimal" |
| minimum = 1% of balance + interest (or $35 floor) | en1, en5, en7 | Claim $-2 — greater of (1%·balance + interest + fees) or $25–$40 floor (~$35); US "1% + interest" ≠ India's 5% |
| still $5,318 after 1 year (on-screen) | en7 | COMPUTED — B₁₂ = 6000·0.99¹² = $5,318 (closed-form, build-locked); VO speaks round "over five thousand" |
| 215 months / ~18 years | en7 | COMPUTED $35-floor model — **build-calculator locked**; VO speaks round "the better part of two decades" |
| $9,496 interest ( > $6,000 borrowed) | en7 | COMPUTED $35-floor model — **build-calculator locked**; VO speaks round "over nine thousand / more than you borrowed" |
| compounding for-you / against-you | en5 | THE TERMINATING MODEL + Claim $-2 (interest-on-interest); "snowball" analogy = long_form_scripting §10 bank |
| +$20 more than minimum | en6, en8 | run.json `action_step` — "en: even $20 more" |

**Deliberately NOT used (so audit doesn't rediscover):**
- **No rupee sign, no lakh, no India institution, no cross-market conversion** — $ SET only;
  the US "1% + interest" mechanism, not the India cut's "5% of total due" (facts-staging:
  "do not reuse the rupee math"). A rupee here is a hard fail.
- No single-issuer APR on screen and no decimal (staging: "never a decimal; say ~22% / north of 20%").
- No false-precise spoken payoff integer — VO stays a round range ("better part of two
  decades" / "over nine thousand"); the exact $5,318 / 215 mo / $9,496 are on-screen only,
  build-calculator locked.
- No computed "+$20 → saves $X / clears in Y months" — no build-locked figure exists; kept
  qualitative (en6). The build calculator can compute it on request (handoff #6).
- The pure-percentage-no-floor "never repaid" asymptote — true and available (facts-staging),
  but omitted from VO (too technical for a 15 c/s short); the "trap" framing carries it.
- No blog-tier "average American pays $X in card interest" (facts-staging rejected list).

## Build handoff

1. `assets/voice/english-lines.json` = `{en1..en9}` with **only** the VO paragraphs above
   (no markdown, no on-screen text). English, verbatim.
2. TTS via `tools/tts/elevenlabs_tts.py`, voice `nPczCjzI2devNBz1zQrb` (Brian),
   `eleven_multilingual_v2`, style 0. Budget: **9 calls** of the run's 30.
3. ffprobe-measure each clip → `data-start` / `data-duration`; re-check the ~165s
   total (add 0.4s lead-in + 1.0s tail per scene) before locking.
4. Images: keyword-matched bg for **all 9 scenes** (`photo_free_scene_ratio` = 0,
   creator rule 2026-07-28) + the cut-ins listed per scene. **Sweep every photo for
   non-US currency, signage and vehicles** (us-english-style rule — a foreign coin
   shipped in the first en cut). No phone-screen photo as a background (design §7).
   md5 the asset ledger — no image may repeat across videos/channels.
5. **en7 figures are calculator output, not script constants.** Regenerate
   `$5,318 / 215 months / $9,496` from the $ model: B₀=$6,000, APR 22% monthly
   i=0.0183333, P = max(0.01·B + i·B, $35), stop at B≤0. On-screen numerals must
   equal that run; the VO stays a round range regardless. `en-US` grouping.
   (fin-script's reference run: percentage phase B(t)=6000·0.99ᵗ to ~$1,235 ≈ 157 mo,
   then a flat-$35 tail ≈ 58 mo → ~215 mo total; interest ≈ $9,496; total paid ≈ $15,496.)
6. If a data-backed `+$20` contrast is wanted on screen in en6, the **build calculator
   must compute it** (same model, P = max(0.01·B + i·B, $35) + $20) — do not hand-type
   it; today's on-screen text is deliberately qualitative.
