---
summary: US/English script for «Pay Yourself First — the payday auto-transfer». 9 VO segments (~2:50 target 165s), blockframe style, USD, Brian voice. US rewrite (not a translation) — hero math $400/mo → $4,800/yr echoing the Fed SHED $400 stat. Every number sourced from videos/pay-yourself-first/facts-staging.md.
updated: 2026-07-28
source: creator brief (run.json 2026-07-28) + facts-staging.md attempt 1; structure mirrors script-hi.md, register per knowledge/us-english-script-style.md
---

# «Pay Yourself First» — English / USA edition

**Studio project (to build):** `studio/videos/pay-yourself-first-en`
**Voice:** ElevenLabs **Brian** `nPczCjzI2devNBz1zQrb`, `eleven_multilingual_v2`, style 0.
**Style:** blockframe motion graphics, 16:9, target 165s. Educational only — no host
persona, no product recommendation; HYSA/FDIC named generically, never a specific
bank or app.
**Engine rule:** digits are spelled out in the VO text below; on-screen numerals
carry the exact figures.
**US rewrite notes:** $ everywhere, US comma grouping, US shocks (credit card,
DoorDash), US institutions (HYSA, FDIC, ACH), US authority stats (BLS, Fed SHED,
BEA, BofA Institute). The credit-card shock carries **no APR number** — no APR
row exists in facts-staging, and every number must trace (contract rule).

## Timing budget

English narration ≈ **15.0 chars/s** (tools/format.json, `cuts.en`). Char counts
are the budget estimate; regenerate and ffprobe-measure before locking scenes.

| # | Scene | chars | est. |
|---|---|---|---|
| en1 | Hook — empty by the 20th | ~296 | ~19.7s |
| en2 | Roadmap — four things | ~143 | ~9.5s |
| en3 | Concept — flip the formula | ~260 | ~17.3s |
| en4 | Rule — pay yourself first (100-year-old) | ~194 | ~12.9s |
| en5 | Audit — why willpower loses (3¢ of every $1) | ~345 | ~23.0s |
| en6 | Action — the day-after-payday auto-transfer | ~311 | ~20.7s |
| en7 | The math — counter to $4,800 + the 5% ladder | ~453 | ~30.2s |
| en8 | Do this today — schedule it, even 5% | ~285 | ~19.0s |
| en9 | Recap + CTA | ~246 | ~16.4s |
| | **Total** | ~2,533 | **~2:49** |

---

## en1 — HOOK

**VO**
> Quick question — why is your account always empty by the twentieth? You're not reckless. You save whatever's left — and there's never anything left. Nearly one in four American households ends the month with nothing. Today: the hundred-year-old rule that saves your money the morning you get paid.

**On screen**
- kicker: `Be honest`
- huge: `EMPTY BY THE` + warn span `20TH?`
- calendar strip: `1 → 20` with a draining balance bar
- stat strip: `1 in 4 US households — nothing left at month-end`
- foot: `Bank of America Institute · Nov 2025`
- stamp (warn): `EVERY MONTH`

**Visuals** — 3 bg crossfades, Ken Burns slow push. Pexels:
`man checking phone bank app late night`, `empty wallet open hands`,
`calendar page close up`.

---

## en2 — ROADMAP

**VO**
> Four things: saving what's left versus saving first, why willpower keeps losing, the payday auto-transfer, and what that money is actually for.

**On screen**
- kicker: `By the end you'll know`
- chips (2×2 rows — max 3 per row, format.json): `SAVE FIRST, NOT LAST` · `WHY WILLPOWER LOSES` / `PAYDAY AUTO-TRANSFER` · `WHAT IT'S FOR`
- sub: `Works even at 5%`

**Visuals** — no bg photo (clean block scene).

---

## en3 — CONCEPT — flip the formula

**VO**
> Most people run this formula: income minus expenses equals savings. Whatever survives the month, that's your savings. And nothing survives the month. Flip it: income minus savings equals expenses. Take the savings out first — then run the month on what's left.

**On screen** — the equation flip is the focal moment (one focal per scene).
- head (struck through, warn): `INCOME − EXPENSES = SAVINGS`
- huge (positive): `INCOME − SAVINGS = EXPENSES`
- stamp: `FLIP THE FORMULA`

**Visuals** — Pexels: `paycheck stub desk calculator`, then hold the clean
equation block (max static hold 2s → keep the flip animating).

---

## en4 — RULE — pay yourself first

**VO**
> The rule is called pay yourself first, and it's a hundred years old — from a nineteen twenty-six book, The Richest Man in Babylon: a part of all you earn is yours to keep. Start with ten percent.

**On screen**
- kicker: `A 100-year-old rule`
- huge: `PAY YOURSELF` + accent span `FIRST`
- book card: `THE RICHEST MAN IN BABYLON · 1926`
- quote chip: `"A part of all you earn is yours to keep"`

**Visuals** — Pexels: `old book pages warm lamp light`.

---

## en5 — AUDIT — why willpower loses

**VO**
> So why doesn't willpower work? Because money sitting in checking finds a thousand ways out — DoorDash, the sale, the card balance. And it isn't a paycheck problem: the median full-time worker earns about twelve hundred fifty dollars a week — yet as a country, we save three cents of every dollar. That's not weak character. That's a missing system.

**On screen**
- kicker: `Why willpower loses`
- chips (warn, staggered): `DOORDASH` · `THE SALE` · `CARD BALANCE`
- context chip: `Median pay $1,251/wk`
- big stat: `$1.00 EARNED →` + warn span `3¢ SAVED`
- foot: `BLS Q2 2026 median weekly earnings · BEA personal saving rate 3.0%, May 2026`

**Visuals** — Pexels: `online shopping checkout phone`,
`food delivery bag doorstep`.

---

## en6 — ACTION — the day-after-payday auto-transfer

**VO**
> The fix is automation. Set an automatic transfer for the morning after payday — a fixed amount that moves itself into a high-yield savings account at a different bank. FDIC insured, roughly ten times the interest of a regular savings account, and a day away from temptation. Money you never see, you never spend.

**On screen**
- kicker: `The fix — automation`
- flow blocks: `PAYDAY` → `AUTO-TRANSFER` → `SAVED BY 9 AM`
- chips: `HIGH-YIELD SAVINGS` · `DIFFERENT BANK` · `FDIC INSURED`
- sub: `~10× a typical savings account` *(no APY on screen — standing rule)*
- stamp: `MONEY YOU DON'T SEE, YOU DON'T SPEND`

**Visuals** — Pexels: `sunrise alarm clock bedside morning`,
`mobile banking transfer phone screen`.

---

## en7 — THE MATH (counter, month by month)

**VO**
> Now the math. Say take-home is four thousand dollars a month, and every payday, four hundred — ten percent — moves on its own. Twelve months later: four thousand eight hundred dollars. And notice — four hundred dollars is the exact emergency about four in ten American adults can't cover in cash. Same number, two different lives. Can't do ten percent? Start at five — two hundred a month is two thousand four hundred a year. Right now, you're saving zero.

**On screen** — the counter IS the visual; counts up in 12 steps (= 12 months),
locale `en-US` grouping.
- head: `$400 · every payday · automatic`
- counter: `$0 → $4,800`
- echo card (warn→positive flip): `$400 — the emergency ~4 in 10 adults can't cover` → `$400 — your monthly auto-save`
- ladder card: `Start at 5% → $200/mo = $2,400/yr`
- foot: `Fed SHED 2025 · $4,000/mo take-home example`

**Visuals** — clean block scene, no photo bg (the counter carries it), bar fills
month by month like the hi cut s7 / needs-vs-wants en7.

---

## en8 — DO THIS TODAY

**VO**
> So here's today's move. Open your banking app and schedule the transfer for the day after your payday — even five percent starts the machine. And what's it for? First an emergency fund, then your big goals — so the next surprise lands on savings, not on a credit card at brutal interest.

**On screen**
- stamp (pop): `DO THIS TODAY`
- chips + arrows: `OPEN BANKING APP` → `SCHEDULE THE TRANSFER` → `DAY AFTER PAYDAY`
- sub: `Even 5% works — first stop: emergency fund, then your goals`

**Visuals** — Pexels: `hand tapping phone banking app close up`.

---

## en9 — RECAP + CTA

**VO**
> So — save first, spend second. Trust the system, not your willpower. Set the auto-transfer today, even at five percent. Next month, the twentieth won't scare you. Then don't say nobody warned you. And for money talk this straight — hit subscribe.

**On screen**
- recap chips (2×2 rows — max 3 per row, format.json): `SAVE FIRST` · `TRUST THE SYSTEM` / `AUTOMATE ON PAYDAY` · `START AT 5%`
- stamp: `SUBSCRIBE`

**Visuals** — Pexels: `young man smiling relieved phone`.

---

## Fact trace (every number → facts-staging.md)

| Number in script | Where | facts-staging.md line |
|---|---|---|
| $4,000/mo take-home → 10% = $400/mo → $4,800/yr | en7 VO + counter | Hero math — US worked example (locked in money-facts-2026) |
| $400 emergency ~4 in 10 adults can't cover | en7 echo card | Fed SHED row, HARD (verify-only → money-facts-2026); echo is deliberate per staging |
| 5% ladder: $200/mo = $2,400/yr | en7, en8 | Arithmetic on the staged $4,000 hero example (brief's "even 5%" action) |
| Median full-time pay $1,251/wk | en5 | BLS Q2 2026 row, HARD |
| 3¢ of every $1 (personal saving rate 3.0%) | en5 | BEA row, HARD (verify-only → money-facts-2026) |
| 1 in 4 households nothing left | en1 | BofA Institute row — "conservative floor" framing blessed in staging conflict note |
| HYSA ≈ 10× typical savings (no APY shown) | en6 | HYSA row + on-screen rule — order-of-magnitude claim only, APY banned on screen |
| "100-year-old rule", Babylon 1926, "a part of all you earn…", start with 10% | en4 | Rule provenance section, HARD |

Deliberately NOT used: PYMNTS 66% paycheck-to-paycheck (SOFT, conflict row — BofA
1-in-4 used alone as the conservative floor per staging guidance); any APY number
(standing on-screen ban); **the 22% APR figure** — named in the brief as the shock,
but no APR row exists in facts-staging, so en8 says "brutal interest" with no
number (contract: no sourced line, no number). No rupee, lakh, or India
institution appears anywhere in this cut.

## Build handoff

1. `assets/voice/english-lines.json` = `{en1..en9}` with **only** the VO paragraphs
   above (no markdown, no on-screen text).
2. TTS via `tools/tts/elevenlabs_tts.py`, voice `nPczCjzI2devNBz1zQrb`,
   `eleven_multilingual_v2`, style 0. Budget: 9 calls.
3. ffprobe-measure each clip → `data-start` / `data-duration`; re-check the
   ~165s total before locking scenes.
4. Images: Pexels per scene above → `assets/img/s1..s9.jpg` (+ `s1-a/b/c`
   crossfades); en2 + en7 stay photo-free (2/9 ≈ the 0.23 photo-free ratio).
   Sweep every photo for non-US currency, signage and vehicles (style-note rule).
5. Counter in en7 animates 12 steps with `en-US` grouping (`$4,800`).
