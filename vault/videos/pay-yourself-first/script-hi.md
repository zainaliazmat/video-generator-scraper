---
summary: Hindi/India script for «Pay Yourself First — the payday auto-transfer». 9 VO segments (~2:45 target), blockframe style, INR, standard Hindi (Harsh). On-screen text English/Hinglish. Every number sourced from videos/pay-yourself-first/facts-staging.md.
updated: 2026-07-28
source: creator brief (run.json 2026-07-28) + facts-staging.md attempt 1; structure mirrors videos/needs-vs-wants/script-hi.md
---

# «Pay Yourself First» — Hindi / India edition

**Studio project (to build):** `vault/videos/pay-yourself-first/src/hi`
**Language:** Standard Hindi, Devanagari. **Not Haryanvi** — channel voice locked 2026-07-28.
**Voice:** ElevenLabs **Harsh** `HTUuC7OeeEt6OL5fViVe`, `eleven_multilingual_v2`, style 0.
**On-screen text:** English / Hinglish. **Titles + description:** English.
**Style:** blockframe motion graphics, 16:9, target 165s. Educational only — no host
persona, no product recommendation; Standing Instruction / UPI Autopay appear as
terminology only (the names viewers will find in their bank app).
**Engine rule:** digits are spelled out in the VO text below (Latin digits are a
coin-flip English reading in ElevenLabs). On-screen numerals carry the exact figures.
**Plausibility rule honored (facts-staging flag):** ₹12,000/mo is explicitly framed
as the higher-earner example (₹60–70k in-hand); the 5% ladder (₹1,200/mo on the
₹24,000 average salary) is the step every viewer is asked to take today.

## Timing budget

Hindi narration ≈ **12.5 chars/s** (tools/format.json, `cuts.hi`). Char counts are
the budget estimate; regenerate and ffprobe-measure before locking scene durations.

| # | Scene | chars | est. |
|---|---|---|---|
| s1 | Hook — empty by the 20th | ~200 | ~16.0s |
| s2 | Roadmap — four things | ~145 | ~11.6s |
| s3 | Concept — flip the formula | ~260 | ~20.8s |
| s4 | Rule — pay yourself first (100-year-old) | ~185 | ~14.8s |
| s5 | Audit — why willpower loses (₹7 of ₹100) | ~255 | ~20.4s |
| s6 | Action — the payday-morning auto-transfer | ~235 | ~18.8s |
| s7 | The math — counter to ₹1,44,000 + the 5% ladder | ~320 | ~25.6s |
| s8 | Do this today — set the SI, even 5% | ~225 | ~18.0s |
| s9 | Recap + CTA | ~235 | ~18.8s |
| | **Total** | ~2,060 | **~2:45** |

---

## s1 — HOOK

**VO**
> एक सवाल — हर महीने बीस तारीख़ तक आपका अकाउंट खाली क्यों हो जाता है? क्योंकि आप बचत सबसे आख़िर में करते हैं। आज सीखिए सौ साल पुराना वो नियम, जिससे बचत महीने की पहली सुबह अपने आप हो जाती है।

**On screen**
- kicker: `Be honest`
- huge: `EMPTY BY THE` + warn span `20TH?`
- calendar strip: `1 → 20` with a draining balance bar
- stamp (warn): `EVERY MONTH`

**Visuals** — 3 bg crossfades, Ken Burns slow push. Pexels:
`indian man checking phone bank balance night`, `empty wallet open hands`,
`calendar page close up`.

---

## s2 — ROADMAP

**VO**
> चार बातें — आख़िर में बचाने और पहले बचाने का फ़र्क़, विलपावर क्यों हार जाती है, सैलरी वाले दिन का ऑटो-ट्रांसफ़र, और वो पैसा आख़िर किस काम के लिए है।

**On screen**
- kicker: `By the end you'll know`
- chips (2×2 rows — max 3 per row, format.json): `SAVE FIRST, NOT LAST` · `WHY WILLPOWER LOSES` / `PAYDAY AUTO-TRANSFER` · `WHAT IT'S FOR`
- sub: `Works even at 5%`

**Visuals** — no bg photo (clean block scene).

---

## s3 — CONCEPT — flip the formula

**VO**
> ज़्यादातर लोगों का फ़ॉर्मूला है — कमाई, माइनस ख़र्चा, बराबर बचत। यानी जो महीने के आख़िर में बच जाए, वही बचत। और सच ये है कि आख़िर में कुछ बचता ही नहीं। समझदार लोग फ़ॉर्मूला उल्टा कर देते हैं — कमाई, माइनस बचत, बराबर ख़र्चा। पहले बचत निकालिए, और बचे हुए पैसों में महीना चलाइए।

**On screen** — the equation flip is the focal moment (one focal per scene).
- head (struck through, warn): `INCOME − EXPENSES = SAVINGS`
- huge (positive): `INCOME − SAVINGS = EXPENSES`
- stamp: `FLIP THE FORMULA`

**Visuals** — Pexels: `salary payslip desk calculator india`, then hold the clean
equation block (max static hold 2s → keep the flip animating).

---

## s4 — RULE — pay yourself first

**VO**
> इस नियम का नाम है — पे योरसेल्फ़ फ़र्स्ट। सबसे पहले अपने आप को पैसे दीजिए। ये आइडिया सौ साल पुरानी किताब द रिचेस्ट मैन इन बेबीलोन से आया है — जो कमाते हो, उसका एक हिस्सा सिर्फ़ तुम्हारा है।

**On screen**
- kicker: `A 100-year-old rule`
- huge: `PAY YOURSELF` + accent span `FIRST`
- book card: `THE RICHEST MAN IN BABYLON · 1926`
- quote chip: `"A part of all you earn is yours to keep"`

**Visuals** — Pexels: `old book pages warm lamp light`.

---

## s5 — AUDIT — why willpower loses

**VO**
> पर विलपावर से क्यों नहीं होता? क्योंकि अकाउंट में पड़ा पैसा ख़र्च होने के हज़ार बहाने ढूँढ लेता है — सेल, बाहर का खाना, ईएमआई। पूरे देश का यही हाल है — आरबीआई के हिसाब से हम हर सौ रुपये में से सिर्फ़ सात रुपये बचा पाते हैं। ये इरादे की कमी नहीं, सिस्टम की कमी है।

**On screen**
- kicker: `Why willpower loses`
- chips (warn, staggered): `SALE` · `FOOD APPS` · `EMI`
- big stat: `₹100 EARNED →` + warn span `₹7 SAVED`
- foot: `RBI FY25 · net household financial savings, 7% of GNDI`

**Visuals** — Pexels: `crowded indian market shopping bags`,
`food delivery app phone hand`.

---

## s6 — ACTION — the payday-morning auto-transfer

**VO**
> इसका इलाज है ऑटोमेशन। बैंक में एक स्टैंडिंग इंस्ट्रक्शन या यूपीआई ऑटोपे सेट कीजिए — सैलरी आने के अगले ही मिनट, एक तय रक़म अपने आप दूसरे अकाउंट में चली जाए। आपकी नींद खुलने से पहले बचत हो चुकी होगी। जो पैसा दिखता नहीं, वो ख़र्च भी नहीं होता।

**On screen**
- kicker: `The fix — automation`
- flow blocks: `SALARY IN` → `AUTO-TRANSFER` → `SAVED BY 9 AM`
- chips: `STANDING INSTRUCTION` · `UPI AUTOPAY`
- stamp: `MONEY YOU DON'T SEE, YOU DON'T SPEND`

**Visuals** — Pexels: `sunrise alarm clock bedside morning`,
`upi payment phone screen`.

---

## s7 — THE MATH (counter, month by month)

**VO**
> अब हिसाब। मान लीजिए इन-हैंड सैलरी साठ-सत्तर हज़ार है, और हर महीने की पहली तारीख़ को बारह हज़ार अपने आप हट जाते हैं। बारह महीने बाद — एक लाख चौवालीस हज़ार। और अगर सैलरी औसत है — क़रीब चौबीस हज़ार — तो पाँच परसेंट से शुरू कीजिए: बारह सौ रुपये महीना, साल के चौदह हज़ार चार सौ। रक़म छोटी लगे? अभी आप शून्य बचा रहे हैं।

**On screen** — the counter IS the visual; counts up in 12 steps (= 12 months),
locale `en-IN` grouping.
- head: `₹12,000 · on the 1st · every month`
- counter: `₹0 → ₹1,44,000`
- sub: `Higher-income example — ₹60–70k in-hand`
- ladder card: `Avg salary ₹24,000 → 5% = ₹1,200/mo = ₹14,400/yr`
- foot: `PLFS 2025 · avg salaried earnings (men) ₹24,217/mo · (women) ₹18,353`

**Visuals** — clean block scene, no photo bg (the counter carries it), bar fills
month by month like needs-vs-wants h7.

---

## s8 — DO THIS TODAY

**VO**
> तो आज का काम — अभी बैंक ऐप खोलिए और सैलरी वाली तारीख़ के लिए स्टैंडिंग इंस्ट्रक्शन सेट कर दीजिए। पाँच परसेंट से ही सही — शुरुआत आज हो। और ये पैसा किसलिए है? पहले इमरजेंसी फंड, फिर आपके बड़े गोल — ख़र्च होने के लिए नहीं, आज़ादी के लिए।

**On screen**
- stamp (pop): `DO THIS TODAY`
- chips + arrows: `OPEN BANK APP` → `SET THE AUTO-TRANSFER` → `SALARY DATE, EVEN 5%`
- sub: `First stop: emergency fund → then your goals`

**Visuals** — Pexels: `hand tapping phone banking app close up`.

---

## s9 — RECAP + CTA

**VO**
> तो बात सीधी है — बचत पहले, ख़र्चा बाद में। विलपावर पर नहीं, सिस्टम पर भरोसा कीजिए। आज स्टैंडिंग इंस्ट्रक्शन सेट कीजिए, चाहे पाँच परसेंट से ही। अगले महीने की बीस तारीख़ को अकाउंट खाली नहीं मिलेगा। और पैसे की ऐसी सीधी बात के लिए — सब्सक्राइब कीजिए।

**On screen**
- recap chips (2×2 rows — max 3 per row, format.json): `SAVE FIRST` · `TRUST THE SYSTEM` / `AUTOMATE ON PAYDAY` · `START AT 5%`
- stamp: `SUBSCRIBE`

**Visuals** — Pexels: `young indian man smiling confident phone`.

---

## Fact trace (every number → facts-staging.md)

| Number in script | Where | facts-staging.md line |
|---|---|---|
| ₹12,000/mo → ₹1,44,000/yr | s7 VO + counter | Hero math — pure arithmetic |
| ₹60–70k in-hand framing | s7 | Plausibility flag — "higher-earner example (₹60–80k in-hand at 15–20%)" |
| Avg salary ≈ ₹24,000 (on-screen exact ₹24,217) | s7 | PLFS 2025 row, HARD (verify-only → money-facts-2026) |
| 5% = ₹1,200/mo = ₹14,400/yr | s7, s8 | Plausibility flag ladder — arithmetic on PLFS row |
| ₹100 → ₹7 saved (RBI 7.0% of GNDI FY25) | s5 | RBI row, HARD; "7 paise of every rupee" framing blessed in staging note |
| "100-year-old rule", Babylon 1926, "a part of all you earn…" | s4 | Rule provenance section, HARD |
| Standing Instruction / UPI Autopay naming | s6, s8 | Banking terminology section (HDFC/SBI/NPCI product pages) |

Deliberately NOT used: SOFT survey rows (YouGov 53%, emergency-fund percentages) —
no SOFT number goes on screen alone; the RBI macro row is the honest anchor per
the staging note. No fabricated "X% save first" stat exists — none invented.

## Build handoff

1. `assets/voice/hindi-lines.json` = `{s1..s9}` with **only** the VO paragraphs
   above (no markdown, no on-screen text).
2. TTS via `tools/tts/elevenlabs_tts.py`, voice `HTUuC7OeeEt6OL5fViVe`,
   `eleven_multilingual_v2`, style 0. Budget: 9 calls of the run's 30.
3. ffprobe-measure each clip → `data-start` / `data-duration`; re-check the
   ~165s total before locking scenes.
4. Images: Pexels per scene above → `assets/img/s1..s9.jpg` (+ `s1-a/b/c`
   crossfades); s2 + s7 stay photo-free (2/9 ≈ the 0.23 photo-free ratio).
5. Counter in s7 animates 12 steps with `en-IN` grouping (`₹1,44,000`).
