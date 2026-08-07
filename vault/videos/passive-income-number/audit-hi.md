---
summary: fin-audit gate for passive-income-number script-hi.md, attempt 1. PASS after five direct edits — two corpus frames shipped without their withdrawal rate (5.9, 7.6), one VO line attributed a methodology claim to a paper nobody read (5.14), one on-screen foot over-claimed a source as a backtest (5.15), and the role-colour legend contradicted its own cues on the two scenes carrying the thesis. Every load-bearing figure re-fetched from its recorded source independently of facts-staging.md.
updated: 2026-08-07
source: script-hi.md (fin-script hi attempt 1) audited against facts-staging.md, knowledge/video-studies/passive-income-number.md, run.json.constraints, tools/format.json. Sources re-fetched live 2026-08-07 by this stage, not trusted from the staging file.
stage: fin-audit, cut hi, attempt 1
---

# audit-hi — passive-income-number

PASS

Passing **with edits**. The script's argument, structure and sourcing survived; five
defects were rewritten in place rather than bounced, because each was mechanical and none
required re-opening the thesis. **The script file changed — voice work must re-run against
the edited file.**

---

## 1. The independence rule — every load-bearing figure re-fetched

`facts-staging.md` was written by this same run, so no figure below is graded against the
claim text. Each was re-retrieved from the URL the staging file records, by this stage.

| Figure | Script lines | Re-fetch result | Verdict |
|---|---|---|---|
| **RBI CPI 5.0% for FY27** | 5.17 | Business Today (read direct): *"CPI inflation outlook for FY2026–27 at 5.0 per cent"*, Q1 5.3 / Q2 4.7 / Q3 5.9 / Q4 5.5, repo held **5.25%**, neutral, MPC **2026-08-05** | **CONFIRMED — exact, including the quarterly split and the date.** This was the highest-risk row in the file (a plausible dated RBI line is the classic injection shape); it is real |
| **POMIS 7.4% p.a., paid monthly** | 5.7, 5.8 | Upstox (read direct): 7.4%, unchanged since 2023-04-01, monthly income | **CONFIRMED** |
| **₹9 lakh single / ₹15 lakh joint ceiling** | 5.9 | Upstox (read direct), same page | **CONFIRMED** |
| **₹5,550/month on ₹9 lakh** | 5.10 | Source prints **₹5,500**; ₹9,00,000 × 7.4% ÷ 12 = **₹5,550** exactly | **CONFIRMED as COMPUTED.** PART E already caught the secondaries' bad rounding. Script speaks "क़रीब पचपन सौ" and prints ₹5,550 — correct on both surfaces |
| **India SWR 3.0–3.5%, best 3.0%, failure risk above 3.75%** | 2.6→7.3 (20 lines), 5.15, 5.16 | SSRN **403'd to me as well**. Recovered independently via search index: Raju & Saraogi, *Balancing Acts*, **2024-01-17**; 3.0–3.5% recommended over 4%; 3% average investor, 2.6% risk-averse; failure risk rises "especially beyond 3.75%" | **CONFIRMED on the band and on 3.75%.** Primary still unreached — the tag stays HARD-on-band / SOFT-on-decimal, and the script already speaks only the band |
| **freefincal corroboration** | 5.15 foot | Read direct: bands are **<3.5% adequate · 3.5–4.5% grey · >4.5% inadequate** | **CONFIRMED as an independent surface** — but it discloses **no backtest**. See defect D4 |
| **Trinity: no tax, no costs; 30-year horizon** | 5.14 | AAII Journal PDF **read direct, full paper**. Verbatim bullet: *"The study did not adjust for taxes or transaction costs."* Payout periods 15/20/25/30 yrs; Cooley, Hubbard & Walz, Trinity University; **AAII Journal, February 1998, p. 16**. Also verbatim: *"young retirees who anticipate long payout periods should plan on lower withdrawal rates"* | **CONFIRMED PRIMARY.** The strongest-sourced claim in the cut |
| **4% originates in a 1994 US paper** | 5.12, 5.13 | Bengen 1994 PDF retrieved but not text-extractable this run; author/journal/date corroborated across the staged surfaces | **CONFIRMED on origin, author, year.** The 1994 paper's *contents* remain unread — which is why D3 below is a defect |
| **₹24,217 regular wage/salaried avg monthly earnings** | 6.9, 6.10 | PIB PLFS Annual Report 2025 (Jan–Dec 2025): male ₹22,891 (2024) → **₹24,217** (2025); female ₹17,126 → **₹18,353** | **CONFIRMED.** Script's foot correctly labels it men ₹24,217 / women ₹18,353 rather than passing the male figure off as the all-India average |
| **PPF 7.1% p.a., Q2 FY27** | 6.15 | Banked HARD in `knowledge/money-facts-2026.md` (DEA notification, two independents) | **CONFIRMED via the vault's own HARD row** |
| **~12% index shape** | 6.16 | SOFT by construction — all three NSE hosts 403'd for the second run running | **CORRECTLY HANDLED**: no decimal spoken, no decimal shown, labelled "ASSUMED", and the index measure is never explained |

**Arithmetic re-derived independently, every rung:** 10L→₹2,500 · 20L→₹5,000 · 40L→₹10,000
· 50L→₹12,500 · 1cr→₹25,000, all at 3.0% ÷ 12 — exact. ₹75L at 4.0% → ₹25,000 — exact.
₹75L vs ₹1cr = **25% smaller** — exact. SIP to ₹1 crore over 240 months: at 7.1% monthly
compounding **₹18,964** (script says "क़रीब उन्नीस हज़ार"), at 12% **₹10,109** (script says
"क़रीब दस हज़ार"). Both round honestly and both are labelled illustrative.

**No untraceable number found.** Every figure spoken or shown maps to a staging row.

---

## 2. The five run-specific checks

### Check 1 — rate with every corpus, at EVERY rung. **fin-script's claim verified true; two frames outside the ladder failed.**

fin-script claims 20 VO lines carry the rate across five rungs. Checked line by line: **all
20 verified** — 2.6, 2.7, 2.8, 2.9, 3.1, 3.2, 3.5, 3.6, 4.1, 4.2, 4.9, 5.2, 5.15, 6.1,
6.2, 6.6, 6.7, 6.10, 6.13, 7.3 each speak a rate in the same sentence (6.13 speaks "चार
परसेंट" beside an on-screen 3.0%, which the fact-trace mis-files under the 3.0% row —
harmless, the line does carry a rate with its corpus). Add 6.12 and 5.10, which also
qualify but are not in fin-script's list.

**Every one of the five rungs holds at every occurrence.** ₹10L, ₹20L, ₹40L, ₹50L and
₹1 crore never appear bare. The Dark Ledger failure — state it once, then ship six bare
numbers — is **not** reproduced. Rung four (6.1/6.2), the exact rung where the twin drops
it, re-speaks the rate twice.

**Two corpus frames outside the rung ladder did fail** (D1, D2 below). Both are on the
script's own build-time invariant token list, so the build assert in Build handoff §5 would
have hard-failed on them — or, worse, someone would have weakened the assert.

### Check 2 — no corpus-to-age conversion. **CLEAN.**
Grepped `उम्र` / `साल की` / `बरस` / `रिटायर` / `नौकरी छोड़`. The only hit is **6.11**, which
is the refusal itself: *"यह उम्र का नहीं, सिर्फ़ रक़म और दर का हिसाब है"*. No age appears
anywhere in the cut. The 20-year horizon at 6.15/6.16 is a **cost-per-month** input, framed
by 6.14 as "what it costs per month" — PART D permits exactly this and forbids the
achievement-date form, which is absent. The study's named counter-example ("financially
free at 50") has no analogue here.

### Check 3 — no return promise. **CLEAN.**
2.6 declares 3% as "मान लिया गया" (assumed); 2.7 says outright *"तीन परसेंट कोई वादा नहीं
है; यह एक चुना हुआ, सावधान नंबर है"*; 6.15/6.16 say "मानी हुई बढ़त" and close on *"दोनों
हिसाब हैं, वादे नहीं"*; 7.5 makes the rule itself the moral. 6.14 separates withdrawal rate
from growth rate on screen before either growth figure is spoken — a guard neither twin has.
4.7 ("so what is left has time to grow back") is purposive, carries no figure, and sits
directly under 4.6's admission that the money comes out of capital. Not a forecast.

### Check 4 — the banned payout word. **CLEAN, including the TRI trap.**
Grepped `dividend` / `डिविडेंड` / `डिवीडेंड` / `लाभांश` / `डिव` across the whole file: **zero
hits in any form** — VO, on-screen text, cues, titles, prose. The script never writes the
word even when discussing its own ban (it says "the banned word" / "the English payout
word"). The TRI trap is closed correctly: **6.16 quotes only the shape** ("क़रीब बारह
परसेंट", `ASSUMED ~12% GROWTH`) and the index measure is never named or explained anywhere,
which is the only way to quote a total-return figure in Hindi without forcing the word.

### Check 5 — provenance of 3.0% vs the internet's 4%. **HONEST after D4.**
5.12–5.15 attribute in the correct order: 4% is named as *America's* number from a **1994**
paper (5.13), what that research excluded is stated with the **1998** primary in the foot
(5.14), and India's own research is credited to **Raju & Saraogi, Jan 2024** by name and
date (5.15). The band is **never** presented as a multi-source consensus — the foot names
**one** paper and **one** practitioner surface, which is exactly what fin-facts established
(PART E: five India blogs repackage the same two papers, and treating them as independent
"would fake a consensus that is one author group"). None of those five blogs appears
anywhere in the script. D4 tightened the one remaining over-claim.

### Hero pairing — ₹25,000 vs PLFS ₹24,217. **CORRECT.**
6.7 derives ₹25,000 from ₹1 crore × 3.0% ÷ 12. 6.8 sets up the comparison. 6.9 states the
PLFS figure with its survey, period and both sexes' figures in the foot. 6.10 draws the
equivalence as *"औसत तनख़्वाह के बराबर"* (equal to the average salary) — not "replaces your
salary forever", not "you never work again". The two numbers are 3.2% apart and the script
says "बराबर", which is the honest read at that distance. The corpus is on a round crore by
arithmetic, not by rounding — verified.

---

## 3. Standard gate checks

| # | Check | Result |
|---|---|---|
| 1 | Numbers trace to staging **and** survive re-fetch | **PASS** — see §1; nothing untraceable, nothing unsupported |
| 2 | Char total within ±10% of budget | **PASS at +0.8%** — see the budget note below |
| 3 | Hook payoff promise inside 15 s | **PASS, tight** — see below |
| 4 | No product/platform recommended | **PASS** — POMIS and PPF appear only as published rates with "price evidence, not a recommendation" foots; SWP/SIP are generic vehicles, which `money-facts-2026` explicitly permits; no fund, AMC, bank, app or scheme is named anywhere |
| 5 | Currency purity | **PASS** — grepped `$`: **zero occurrences** in the file, including inside claim IDs. PART C of the staging file contributes nothing |
| 6 | No cite refs, no bare Latin digits in VO | **PASS** — grepped `^> .*[0-9]`: the only matches are the guard-rail blockquote at the head of the file, which is prose, not VO. **No VO line contains a Latin digit.** Every figure is spelled in Devanagari ("उन्नीस सौ चौरानवे", "चौबीस हज़ार दो सौ सत्रह", "सात दशमलव चार परसेंट"). No `(28:4)`-style refs |
| 7 | Persona rules | **PASS** — grepped `मैं` / `हमने` / `हमारा` / `हमें`: zero in VO. Second person throughout, no host persona, no first-person expertise, no investment pick. Monetisation-safe |
| 8 | Text-level layout lints | **PASS after D5** — see below |

**Budget (check 2) — read this before "fixing" the length.** The naive reading
`13.03 × 510 = 6,645` would put this script at **−11.9%** and tempt a later stage to pad it
by ~800 characters. That reading is **wrong** and `format.json` says so itself: 13.03 c/s is
the *flat delivered rate per second of audio*, and MEDIUM charges 0.8 s of non-audio padding
per line (`tiers.medium`), so the budget is `(510 − 0.8 × 78) × 13.03 = 5,832`. This is the
same correction `cuts.en._chars_per_second_trap` demands ("Fix the budget formula FIRST").
Post-edit total **5,876 = +0.8%**. Spot-recounting confirmed the long lines are exact
(6.13 counts 100 against a printed 100) while several short lines are printed ~3–6 high, so
the true total sits at or below 5,876 — the safe direction. **Do not pad this script.**

**Hook gate (check 3).** Recounted from actual character counts rather than the printed
table: 1.1 ends 3.6 s, 1.2 ends 9.2 s, 1.3 ends 11.6 s, so 1.4 opens at **11.6 s** and the
withheld-number phrase *"एक ख़ास नंबर"* lands at **≈13.9 s**. Inside the 15 s gate, with
~1 s of margin. This is B's form (name it, refuse to say it), which the study records as the
`no_return_promise`-safe shape. **Margin note for the build: if 1.1–1.3 come in slow, this
gate breaks.** Both twins sit outside it (A ≈0:22, B ≈0:45); the gate still wins.

**Layout lints (check 8).** One focal element per scene holds — where a frame carries both
`num:` and `stmt:`, the `stmt` is the mandated rate qualifier or the working, not a second
focal. **No `chips:` cue exists anywhere in the script**, so the ≤3-per-row and ≤22-char
lints have nothing to bite on. No per-scene cue offsets are declared at script stage, so
`cue_min_gap_seconds` and the cascade rule are storyboard-stage and carry forward. The
colour table is the one that failed — D5.

---

## 4. What was rewritten, and why

Five edits. Nothing was killed; the argument is intact.

### D1 — 5.9 shipped a corpus with no rate. *(the documented failure mode, hit once)*
`₹9,00,000` appeared in the VO and in the frame with **no rate token anywhere in either**.
This breaches `run.json.constraints.withdrawal_rate_on_screen` ("A number without its
assumption visible is a fabricated promise") **and the script's own build-time invariant**,
which names `₹9,00,000` on its corpus-token list (Build handoff §5). The build assert would
have failed here.

- VO: `पर उसमें ज़्यादा से ज़्यादा नौ लाख रुपये रखे जा सकते हैं।`
- → `पर उसी सात दशमलव चार परसेंट पर ज़्यादा से ज़्यादा नौ लाख रुपये ही रखे जा सकते हैं।`
- Frame: `stmt: ₹9,00,000 maximum, single account` → `stmt: ₹9,00,000 maximum at 7.4%, single account`
- 57 → 82 chars (6.3 s + 0.8 = 7.1 s scene, under the 9.0 s hold ceiling).

### D2 — 7.6 shipped the hero corpus with no rate.
`एक करोड़` / `₹1,00,00,000` spoken and shown bare in the callback. Same breach, same token
list. Rhetorically it is a negation ("it did *not* start at a crore"), but the constraint is
mechanical and the token still renders.

- VO: `और यह सीढ़ी एक करोड़ से शुरू नहीं हुई थी — यह ढाई हज़ार वाले उस पहले रिचार्ज के बिल से शुरू हुई थी।`
- → `और यह सीढ़ी एक करोड़ से नहीं, तीन परसेंट वाले उस ढाई हज़ार के पहले रिचार्ज बिल से शुरू हुई थी।`
- Frame: `stmt:` gains `, both at 3.0%`
- 99 → 94 chars. The callback and the 2.10 recharge reference both survive.

### D3 — 5.14's VO attributed a methodology claim to a paper nobody read.
The line said **"वो पेपर"** ("that paper"), whose only antecedent is the **1994** paper named
in 5.13. But the "no tax, no transaction costs" statement is **Trinity 1998's**, verbatim
and self-stated — and `facts-staging.md` records that the 1994 paper "was NOT read (FPA PDF
403'd)". The frame's foot already credited Cooley/Hubbard/Walz 1998 correctly, so the VO and
the frame were pointing at **different documents**. On the one beat whose entire job is
provenance honesty, that is not survivable.

- `वो पेपर वहाँ के आँकड़ों पर बना था…` → `उस नियम की रिसर्च वहाँ के आँकड़ों पर बनी थी…`
- "That rule's research" scopes the claim to the 4%-rule literature, which the frame then
  pins to the paper actually read. 93 → 103 chars — **now the longest line in the cut**, at
  8.70 s against the 9.0 s ceiling. Flagged in the timing section: do not lengthen 5.14.

### D4 — 5.15's foot called freefincal "a backtest".
The foot claimed the band was *"corroborated independently by an Indian practitioner
backtest"*. Re-fetched: the article states three threshold bands as conclusions and
discloses **no backtest data** — `facts-staging.md` says so itself ("no backtest data
disclosed in the article", tagged SOFT). Asserting a methodology a source does not show is
the same class of error as D3, on a frame cited to a named real person.

- → `· independently corroborated by ONE Indian practitioner surface (freefincal, Feb 2026)`
- The capitalised **ONE** is deliberate: it is the on-screen guard against the five-blog
  fake consensus PART E identified.

### D5 — the role-colour legend contradicted its own cues, on the thesis scenes.
The legend filed **4.7** under `--warn` (cue says `--target`) and **5.16** under `--target`
(cue says `--warn`), and omitted 2.11, 3.8, 5.14, 6.4, 6.6 and 7.6 entirely. A storyboard
colouring from the legend rather than the cues would have painted *"why the rate is kept
small"* as a danger and *"above 3.75% it breaks"* as merely under examination — the two
scenes that carry the argument, both inverted. Rebuilt all three lists from the cues and
added a thesis check.

**Post-edit colour verdict:** green never lands on a figure lacking its rate, red never
lands on India's 3.0%, amber never lands on the imported 4%. **The colour table argues with
the thesis, not against it.**

---

## 5. Carried forward — not defects, but they will cost money if ignored

1. **The `>` extraction hazard (TTS spend).** VO lines are `>`-quoted, but so are the
   24-line guard block at the head of the file and the 9-line VO-block-rule block. A naive
   `^> ` extractor yields **~111 lines, not 78** — 33 of them English markdown prose that
   would be read aloud in Hindi, at ~33 wasted ElevenLabs calls against a 188 ceiling.
   Build handoff §1 already specifies keyed extraction (`1.1 … 7.8`) gated by a
   byte-for-byte reconstruction check. **Use it. Do not grep for `>`.**
2. **The 2.6/2.7 image hold still breaches `max_scene_seconds`.** Build handoff §7 flags it
   (5.7 + 6.8 + padding ≈ 14.1 s on one photograph) and prescribes a second tighter crop.
   Unresolved at script stage by design; it is a build fix, and `check_build` will catch it
   if it is skipped.
3. **The hook gate has ~1 s of margin.** See check 3.
4. **5.14 has 0.30 s of hold-ceiling margin.** See D3.
5. **SSRN remains unreachable** for the second stage running. The 3.0–3.5% band and the
   3.75% edge are confirmed on a secondary index, not on the paper. The script speaks only
   the band and attributes it by author and date, which is the correct posture for that tag
   — but a primary read is owed before this rate is promoted to `money-facts-2026.md`.

---

## 6. Verdict

**PASS** — five defects rewritten, none killed, no claim unsupported after re-fetch.

The two rate-token breaches are the exact failure this gate exists to catch, and they were
in the two places least likely to be noticed: a ceiling frame that is not a rung, and an
emotional callback where the number is being *denied* rather than asserted. The ladder
itself — the part everyone checks — was already clean at all five rungs.

**Cleared for TTS.** The script file changed; downstream voice work must re-run against the
edited file (the pipeline hash-checks this).
