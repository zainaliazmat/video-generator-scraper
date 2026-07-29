---
summary: Hindi/India script for «Your Credit History — the invisible record». 9 VO segments (blockframe-9, ~2:49 vs 165s target), INR, Standard Hindi (Harsh). On-screen text English/Hinglish. Every number traces to videos/credit-history/facts-staging.md — CIBIL ₹ set only, the US 7-year rule is explicitly excluded.
updated: 2026-07-29
source: creator brief (run.json 2026-07-29) + facts-staging.md attempt 2; structure mirrors videos/good-debt-vs-bad-debt/script-hi.md. NO study note exists (fin-research rescued — library.db has no finance lane), so retention shape is inherited from the two shipped hi cuts, not from a fresh study.
---

# «Your Credit History» — Hindi / India edition

**Studio project (to build):** `studio/videos/credit-history`
**Language:** Standard Hindi, **Devanagari** — channel voice locked 2026-07-28.
**Voice:** ElevenLabs **Harsh** `HTUuC7OeeEt6OL5fViVe`, `eleven_multilingual_v2`, style 0.
**On-screen text:** English / Hinglish. **Titles + description:** English (Roman/Latin script).
**Style:** blockframe-9 motion graphics, 16:9, target 165s. Educational only — no host
persona, no first-person expertise, no lender/card/product pick. CIBIL and "credit
report" appear as **terminology** (the words a viewer will see in their own bank app
and on cibil.com), never as a recommendation; no bank is ever named.

**Engine rule:** digits are **spelled out** in the VO text below (bare Latin digits are
a coin-flip English reading in ElevenLabs). On-screen numerals carry the exact figures,
`Intl.NumberFormat("en-IN")` grouping (`₹30,00,000`).

> ### ⚠ THE TWO THINGS THAT MUST NOT ENTER THIS CUT
> Both are named in facts-staging as the cross-market traps for this exact topic:
> 1. **NEVER "7 years."** That is the US FCRA rule (§1681c(a)). India has **no
>    statutory auto-delete**. This cut says **36 months / three years** — CIBIL's own
>    month-by-month window — and nothing more.
> 2. **NEVER a percentage weight** (35% / 30% / 15%). Those are **FICO's published
>    weights for FICO's score**. CIBIL publishes none. This cut names the factors
>    **ranked, without numbers**, and the on-screen foot says so out loud.
>
> A rupee-cut carrying either figure is a hard failure. The audit stage should grep
> this script for `7 year`, `सात साल`, `35`, `30%` and find nothing.

**Colour intent (thesis-derived — the storyboard formalises this four-line table):**
`--warn` red = **the missed payment and the price it charges** (the 36-month record,
the below-700 band); `--fund` green = **the on-time payment, the clean report, the top
band**; `--target` amber = **the score / the report under examination**; `--pop` orange
= the do-this-today CTA. (design-finance-blockframe §2 — semantics derive from *this*
video's thesis: red is the missed EMI, not "credit cards".)

**Per-scene tint ladder** (0.10–0.13, §2): `s1 red .12 · s2 amber .10 · s3 amber .12 ·
s4 green .10 · s5 red .13 · s6 green .10 · s7 red .12 · s8 orange .12 · s9 green .13`.
**`ken` alternation** (§5 rule 1): `in, out, in, out, in, out, in, out, in`.

## Timing budget

Hindi narration ≈ **12.5 chars/s** (`format.json cuts.hi`). Char counts are the budget
estimate only; the build step regenerates + ffprobe-measures each clip and adds the
per-scene **0.4s lead-in / 1.0s tail** before locking scene durations.

| # | Scene | chars | est. VO |
|---|---|---|---|
| s1 | Hook — the report you've never seen | ~212 | ~17.0s |
| s2 | Roadmap — four things | ~157 | ~12.6s |
| s3 | Concept — what the report and the score are | ~238 | ~19.0s |
| s4 | Rule — what builds it (factors, ranked, no weights) | ~247 | ~19.8s |
| s5 | Audit — what destroys it: 36 months (THE HERO) | ~253 | ~20.2s |
| s6 | Action — auto-pay every due date | ~238 | ~19.0s |
| s7 | The math — one percentage point on a ₹30 lakh loan | ~310 | ~24.8s |
| s8 | Do this today — free annual report + auto-pay | ~242 | ~19.4s |
| s9 | Recap + CTA | ~213 | ~17.0s |
| | **VO total** | **~2,110** | **~2:49** |

**Budget check:** 165s × 12.5 = **2,062 char budget**; this draft is **~2,110 (+2.3%)**
→ **~169s VO**, i.e. ~4s over target. Rendered runtime adds 9 × 1.4s of lead-in/tail
= **~181s total**, comfortably inside the short tier's 60–300s range. If the measured
TTS comes in long, cut from **s7** (the only scene over 25s) — the "एक ही घर, सिर्फ़ एक
अलग नंबर।" closer is the keeper, the rate-card mechanism sentence is the trim.

---

## s1 — HOOK

**VO**
> एक रिपोर्ट है जो आपने कभी देखी नहीं, पर वो तय करती है कि आपको लोन मिलेगा या नहीं — और किस ब्याज पर। बैंक आपसे मिलने से पहले उसे पढ़ चुका होता है। नाम है — क्रेडिट रिपोर्ट। और उसमें आपकी हर चूकी हुई किश्त लिखी है।

**On screen** — the "invisible record" is the focal shock; the loan-decision line lands last.
- kicker: `A file you've never seen`
- huge (target): `YOUR CREDIT REPORT`
- decision strip (reveal after the huge):
  ```
  LOAN?        →  it decides
  INTEREST?    →  it decides
  YOU'VE SEEN IT?  →  probably never
  ```
- stamp (warn): `EVERY MISSED EMI IS IN IT`

**Visuals** — bg keyword: `rows of paper files in an archive, dark`; cut-in
`sealed envelope on a desk` on «एक रिपोर्ट है»; cut-in `bank counter paperwork` on
«बैंक आपसे मिलने से पहले». 3 bg crossfades, slow Ken Burns push-**in**.

---

## s2 — ROADMAP

**VO**
> चार बातें — ये रिपोर्ट है क्या, इसे बनाता क्या है, बिगाड़ता क्या है, और ज़रूरत पड़ने से बहुत पहले ये क्यों मायने रखती है। और आख़िर में, आज करने वाले दो काम।

**On screen**
- kicker: `By the end you'll know`
- chips (2×2 — max 3 per row, ≤22 chars): `WHAT THE REPORT IS` · `WHAT BUILDS IT` /
  `WHAT DESTROYS IT` · `WHY IT MATTERS EARLY`
- sub: `Then two things to do today`

**Visuals** — bg keyword: `stack of tied document bundles` (calmest — roadmap rest
beat, but it still carries a photo per the every-frame-has-image rule, 2026-07-28).
Ken **out**, slow.

---

## s3 — CONCEPT — what the report and the score are

**VO**
> पहली बात — आपका हर लोन, हर क्रेडिट कार्ड, हर किश्त क्रेडिट ब्यूरो के पास दर्ज होती है। इसी रिकॉर्ड का नाम है क्रेडिट रिपोर्ट, और उसका निचोड़ है तीन अंकों का एक नंबर — सिबिल स्कोर, तीन सौ से नौ सौ के बीच। सात सौ के ऊपर अच्छा माना जाता है।

**On screen** — the 300→900 scale is the single focal element.
- kicker: `First — what it actually is`
- head2: `THE REPORT = the record` → `THE SCORE = the summary`
- scale bar (the focal, `.mega` numerals at each end):
  ```
  300 ├────────────────────────────┤ 900
                    700+ = generally good
                    750+ = best pricing
  ```
- foot: `TransUnion CIBIL — score range 300–900`

**Visuals** — bg keyword: `printed statement page with ruled columns, macro`; cut-in
`three-digit number printed on a form` on «तीन अंकों का एक नंबर». Ken **in**.

---

## s4 — RULE — what builds it

**VO**
> इसे बनाता क्या है? सिबिल की सूची में सबसे ऊपर — पेमेंट हिस्ट्री, यानी हर किश्त वक़्त पर। दूसरी है क्रेडिट यूटिलाइज़ेशन — लिमिट का कितना हिस्सा आप इस्तेमाल करते हैं। फिर आपका क्रेडिट कितना पुराना है, और आख़िर में, आप कितनी बार नया लोन माँगते हैं।

**On screen** — a ranked ladder, **no percentages anywhere**.
- kicker: `What builds it`
- ranked rows (cascade, 0.6s apart, fund-bordered — 4 items ≤5 cascade cap):
  ```
  1  PAYMENT HISTORY      every EMI, on time
  2  CREDIT UTILISATION   how much of the limit you use
  3  AGE OF CREDIT        how old your accounts are
  4  NEW ENQUIRIES        how often you apply
  ```
- foot (the guard-rail, `--muted`):
  `CIBIL names these factors — it publishes no percentage weights. Also counted: credit mix.`

**Visuals** — bg keyword: `desk diary open with a pen` (calm — 4 stacked rows,
densest-scene rule §5.3); cut-in `credit card resting on a paper bill` on
«क्रेडिट यूटिलाइज़ेशन». Ken **out**.

> **Deliberate omission:** no `35%` / `30%` / `15%` anywhere. Those are FICO's weights
> for FICO's score (facts-staging **Claim US-2** — the US-market claim two) and
> importing them is exactly the cross-market conversion this pipeline forbids
> (Claim ₹-2, "DO NOT").

---

## s5 — AUDIT — what destroys it (THE HERO SCENE)

**VO**
> अब बिगाड़ता क्या है। आपकी रिपोर्ट में पिछले छत्तीस महीनों का महीना-दर-महीना रिकॉर्ड होता है। यानी एक चूकी हुई किश्त वहाँ पूरे तीन साल दिखती है। और सिबिल के अपने शब्दों में — वो हमेशा आपकी क्रेडिट हिस्ट्री का हिस्सा रहेगी। एक चूक, और गिनकर छत्तीस महीने।

**On screen** — **the timeline animation is the hero visual** (creator brief).
- kicker: `What destroys it`
- the grid (the focal): 36 cells in 3 rows of 12 = the month-by-month payment history.
  Cells fill green left→right, **one cell slams red** at ~40% of the clip, then the
  red cell stays lit while the remaining cells keep filling green past it.
- counter under the grid, counting the red cell's age: `MONTH 1 → MONTH 36`
- huge (warn, lands on «छत्तीस महीने»): `ONE MISS = 36 MONTHS`
- foot: `CIBIL — 36-month month-by-month payment history; "will always be a part of your credit history"`

**Visuals** — bg keyword: `red ink stamp and pad on a document` (calm, thematic —
the grid carries the scene); cut-in `torn calendar page` on «एक चूकी हुई किश्त».
Ken **in**. The grid must keep animating — no static hold past ~2s (§5.2).

> **The rule this scene obeys:** say **36 months / three years**, never "7 years"
> (facts-staging Claim ₹-3 + the RED FLAG section). The VO's second half is the
> staging note's own blessed wording — CIBIL's "always a part of your credit history"
> — which carries the "it doesn't just vanish" beat **without** making a statutory
> claim, since CICRA 2005's primary text was never obtained.

---

## s6 — ACTION — auto-pay every due date

**VO**
> इसका इलाज आसान है — ऑटो-पे। हर कार्ड और हर लोन की ड्यू डेट पर ऑटो-डेबिट लगा दीजिए, या फ़ोन में महीने का रिमाइंडर। याद रखना आपका काम नहीं होना चाहिए। और यूटिलाइज़ेशन — लिमिट का कम हिस्सा इस्तेमाल कीजिए, और बिल पूरा भरिए, मिनिमम नहीं।

**On screen**
- kicker: `The fix`
- huge (fund): `AUTO-PAY` + sub `every due date`
- flow: `EVERY CARD` → `EVERY LOAN` → `AUTO-DEBIT or CALENDAR ALERT`
- stamp (fund): `REMEMBERING SHOULDN'T BE YOUR JOB`
- sub: `Use a small share of the limit · pay the full bill, not the minimum`

**Visuals** — bg keyword: `wristwatch and a diary on a dark table`; cut-in
`bank passbook open` on «ड्यू डेट». Ken **out**.
**No phone-screen photo as a background** (§7 — this has shipped wrong three times).

---

## s7 — THE MATH — one percentage point (the ~70% reward beat)

**VO**
> अब हिसाब — कम स्कोर की क़ीमत। बैंक अपने रेट सिबिल बैंड से जोड़ते हैं — वही लोन, वही बैंक, पर नीचे के बैंड में क़रीब एक परसेंट ऊपर का ब्याज। तीस लाख के बीस साल के लोन पर उसका मतलब — हर महीने क़रीब पंद्रह सौ रुपये ज़्यादा, और पूरे लोन में तीन से साढ़े चार लाख ज़्यादा ब्याज। एक ही घर, सिर्फ़ एक अलग नंबर।

**On screen** — figures reveal in three anchors, punch on the last. **No bank name,
no specific interest rate** (facts-staging Claim ₹-4 on-screen rule).
- setup: `₹30,00,000 · 20 years · same loan, same bank`
- the spread (never a rate, only the gap):
  ```
  TOP SCORE BAND      →  the bank's best price
  BELOW-700 BAND      →  ~1 percentage point higher
  ```
- reveal rows (build-calculator locked — see handoff #5):
  ```
  EXTRA EVERY MONTH    ₹1,390 – ₹1,860
  EXTRA INTEREST       ₹3.3 – 4.5 lakh
  ```
- huge (warn, the punch): `SAME HOUSE. DIFFERENT NUMBER.`
- foot: `Two lenders' own published rate cards, keyed to the CIBIL band — spread, not rates`

**Visuals** — bg keyword: `blueprint paper texture` (calmest — densest scene, §5.3);
cut-in `house keys on a property document` on «एक ही घर». Ken **in**. The numbers
carry the scene; keep the background nearly still.

> **Why a ₹30 lakh home loan for a ₹30,000/mo audience (staging's flagged mismatch):**
> that gap **is the argument**, and the VO makes it the argument — the score is priced
> on the loan you haven't taken yet, which is the brief's "why it matters before you
> ever need it" beat. facts-staging explicitly forbids improvising a nearer-term
> personal/two-wheeler example: none was sourced. Do not invent one at build time.

---

## s8 — DO THIS TODAY

**VO**
> तो आज दो काम। पहला — अपनी क्रेडिट रिपोर्ट एक बार देखिए; हर ब्यूरो से साल में एक फ़ुल रिपोर्ट मुफ़्त मिलती है। कोई ग़लत एंट्री दिखे तो विवाद दर्ज कीजिए। दूसरा — हर ड्यू डेट आज ही ऑटो-पे पर डालिए। स्कोर एक दिन में नहीं, महीनों में बनता है।

**On screen**
- stamp (pop): `DO THIS TODAY`
- two numbered blocks:
  ```
  1  PULL YOUR CREDIT REPORT   one free full report a year, from each bureau
  2  PUT EVERY DUE DATE ON AUTO-PAY
  ```
- sub: `Wrong entry? Raise a dispute.`
- foot: `A score is built in months, not in a day — do this long before you need the loan`

**Visuals** — bg keyword: `magnifying glass over a printed document`; cut-in
`pen ticking a checklist` on «विवाद दर्ज कीजिए». Ken **out**.

---

## s9 — RECAP + CTA

**VO**
> तो सीधी बात — बैंक आपसे पहले आपकी रिपोर्ट पढ़ता है। वक़्त पर भरी किश्तें उसे बनाती हैं, एक चूक छत्तीस महीने दिखती है, और कम स्कोर हर बड़े लोन पर लाखों वसूलता है। पैसे की ऐसी सीधी बात के लिए — सब्सक्राइब कीजिए।

**On screen**
- recap chips (2×2 — max 3 per row, ≤22 chars): `BANK READS IT FIRST` · `ON-TIME EMIs BUILD IT` /
  `ONE MISS = 36 MONTHS` · `LOW SCORE COSTS LAKHS`
- cta block (pop): `SUBSCRIBE`

**Visuals** — bg keyword: `sunlit doorway of a new home`. Ken **in**.
*(Not a person — both shipped hi cuts closed on `young indian man … phone`; the
no-image-repeat rule §7 bars reusing it, and a face fights the CTA type.)*

---

## Fact trace (every number → facts-staging.md)

| Number / claim in script | Where | facts-staging.md line |
|---|---|---|
| Score is a three-digit number, **300–900** | s3 VO + scale bar | Claim ₹-1 — "three-digit number from **300 to 900**", HARD (TransUnion CIBIL, primary) |
| **700+** generally good | s3 VO + scale | Claim ₹-1 — "Above ~700 is generally treated as good" |
| **750+** best pricing (screen only) | s3 scale | Claim ₹-1 — "lenders' best pricing starts around 750–800"; audit narrowed the screen form to `750+` because every re-checked lender card puts its *best* band at 800+ or "750 & above", so a closed 750–800 range reads as excluding 800+ |
| Factors **ranked, no weights** — payment history · utilisation · age · enquiries (+ mix) | s4 VO + ladder + foot | Claim ₹-2 — "Four named factors, **no published percentage weights**… plus credit mix", HARD (terminology) |
| **36 months / three years** month-by-month record | s5 VO + 36-cell grid + counter, s9 | Claim ₹-3 — "visible on the CIBIL report for **36 months (3 years)** of month-by-month payment history" |
| "will always be a part of your credit history" | s5 VO + foot | Claim ₹-3 — CIBIL's own wording, and the staging note's **blessed on-screen wording** |
| Same loan, same bank, **~1 percentage point** apart on score alone | s7 VO + spread block | Claim ₹-4 — HARD on the spread: "roughly **0.75 to 1.00 percentage point**"; on-screen rule "never a specific bank, never a specific rate" |
| **₹30,00,000 · 20 years** model | s7 setup | COMPUTED ₹-A — P = ₹30,00,000, n = 240 months |
| **~₹1,500/mo** spoken · **₹1,390–₹1,860** on screen | s7 | COMPUTED ₹-A — "₹1,390–1,860 more every month" |
| **₹3.3–4.5 lakh** extra interest | s7 VO + reveal | COMPUTED ₹-A — "₹3.3–4.5 lakh more interest over the loan" |
| **One free full report per year, per bureau** | s8 VO + block | Claim ₹-5 — "One free full credit report per calendar year from each CIC"; staging: "the free annual report is **the safest of the three for screen**" |
| Dispute a wrong entry | s8 | Claim ₹-3 source line — CIBIL: no correction/deletion without the lender's confirmation (i.e. the dispute route exists) |

### Deliberately NOT used (so the audit stage doesn't rediscover them)

- **"7 years" / CICRA auto-delete** — the blog-tier claim (zetapp, gocredit, freed.care,
  bajajhousingfinance, airtel, paytm…). No primary exists; it is the US FCRA rule in an
  Indian costume. **REJECTED per the RED FLAG section.**
- **35% / 30% / 15% / 10%** — FICO's weights (**Claim US-2**, the US-market claim two in
  facts-staging). CIBIL publishes none.
- **"No law deletes it" as a spoken claim** — true per the industry-press reading, but
  CICRA 2005's primary text was never obtained (one 2015 secondary). The VO makes the
  point through **CIBIL's own quote** instead, which needs no statute.
- **RBI ₹100/day compensation** — staging: "needs an RBI primary before it goes on
  screen." rbi.org.in 403s; no primary was read. **Omitted entirely.**
- **Fortnightly (15th / last-day) reporting** — same SOFT bucket, no RBI primary. Cut
  as a second unhedgeable number on a scene that already lands the 36-month hero. Add
  it only after an RBI read.
- **Average CIBIL score / "minimum 701 for a home loan"** — aggregator framing, listed
  as rejected in staging.
- **Any named lender, any specific interest rate, any rate-card date** — the two sourced
  cards are stale (07.07.2025) / undated; only the **spread** is durable.
- **No dollar sign, no US institution, no FICO figure, no cross-market conversion** —
  ₹ set only (`format.json` pins `cuts.hi.forbidden_currency` to the US dollar symbol,
  and the check is a whole-file scan — the glyph must not appear anywhere in this file,
  not even in a claim ID, which is why US-market claims are cited as `Claim US-n` here).

---

## Build handoff

1. `assets/voice/hindi-lines.json` = `{s1..s9}` with **only** the VO paragraphs above
   (no markdown, no on-screen text). Devanagari, verbatim — **slice the source, never
   retype**.
2. TTS via `tools/tts/elevenlabs_tts.py`, voice `HTUuC7OeeEt6OL5fViVe` (Harsh),
   `eleven_multilingual_v2`, style 0. Budget: **9 calls** of the run's 30.
3. ffprobe-measure each clip → `data-start` / `data-duration`; scene duration =
   `0.4 + clip + 1.0` (design §6). Re-check the total before locking; the four homes of
   the timing numbers must be **generated from one source**, never hand-edited.
4. Images: keyword-matched bg for **all 9 scenes** (`photo_free_scene_ratio` = 0,
   creator rule 2026-07-28) plus the cut-ins listed per scene. **md5 the asset ledger** —
   no image may repeat across videos or channels (§7); the two shipped hi cuts already
   burned `hand tapping phone banking app` and `young indian man … phone`.
5. **s7 figures are calculator output, not script constants.** Regenerate
   `₹1,390–₹1,860` and `₹3.3–4.5 lakh` from the ₹ model
   (`EMI = P·i·(1+i)^n / ((1+i)^n − 1)`, P = ₹30,00,000, n = 240, Δ = 0.75 and 1.00 pp
   on the sourced band spread) and lock the integers. On-screen numerals must equal that
   run; the VO stays a round anchor ("क़रीब पंद्रह सौ") regardless. `en-IN` grouping.
6. **s5's 36-cell grid is the hero animation** — 3 rows × 12, green fill left→right,
   one cell slams `--warn` at ~40% of the clip and stays lit, remaining cells keep
   filling past it. It must still be moving at every point in the scene (§5.2, no static
   hold > ~2s). The `MONTH 1 → MONTH 36` counter runs under it.
7. Anchor cues to **word-level timings** (faster-whisper), not character-offset
   interpolation — the drift is worst on Hindi (§6). Cut-ins listed above name the exact
   VO word they land on.
