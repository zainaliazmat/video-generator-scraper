---
summary: Hindi/India script for «Good Debt vs Bad Debt — the minimum-payment trap». 9 VO segments (blockframe-9, ~2:46 target), INR, Standard Hindi (Harsh). On-screen text English/Hinglish. Every number traces to videos/good-debt-vs-bad-debt/facts-staging.md.
updated: 2026-07-28
source: creator brief (run.json 2026-07-28) + facts-staging.md attempt 1; structure mirrors videos/pay-yourself-first/script-hi.md
---

# «Good Debt vs Bad Debt» — Hindi / India edition

**Studio project (to build):** `vault/videos/good-debt-vs-bad-debt/src/hi`
**Language:** Standard Hindi, **Devanagari** — channel voice locked 2026-07-28.
**Voice:** ElevenLabs **Harsh** `HTUuC7OeeEt6OL5fViVe`, `eleven_multilingual_v2`, style 0.
**On-screen text:** English / Hinglish. **Titles + description:** English (Roman/Latin script).
**Style:** blockframe-9 motion graphics, 16:9, target 165s. Educational only — no host
persona, no first-person expertise, no product/card/fund pick; the credit card is the
generic instrument, APR/minimum appear only as price evidence (issuer MITC + RBI).

> **SCRIPT-ORTHOGRAPHY CONFLICT — resolved.** The launch task labelled this a
> "Nastaliq-script hi cut." That is wrong for this lane and was **not followed**:
> `format.json cuts.hi` = voice **Harsh** (standard `hi` accent), the pipeline
> contract says *Standard Hindi*, and both shipped hi scripts are Devanagari.
> Nastaliq belongs to the separate **Urdu** story channel (different voice). A
> Nastaliq/Urdu script read by Harsh is a hard TTS failure, so this cut is written
> in **Devanagari Standard Hindi**. No config was changed. If the creator truly
> wants an Urdu cut, that needs a new channel + voice in format.json — it does not
> exist today. Flagged for the orchestrator.

**Engine rule:** digits are **spelled out** in the VO text below (bare Latin digits
are a coin-flip English reading in ElevenLabs). On-screen numerals carry the exact
figures, `Intl.NumberFormat("en-IN")` grouping (`₹88,614`).

**Colour intent (thesis-derived — storyboard formalises the 4-line table):**
`--warn` red = the **interest trap / minimum-payment trap / bad debt**;
`--fund` green = **good debt / the escape (paying more) / money kept**;
`--target` amber = the **card under examination / the decision**;
`--pop` orange = the do-this-today CTA. (Per design-finance-blockframe §2 — on a
credit-card video red MUST be the interest trap, not reused blindly.)

**Hero-math handling (locked, see facts-staging + build-handoff):** VO speaks only
the **floor-independent robust anchors** — month-1 split, "a year barely moves it",
and the payoff as a **round range** (17+ years / nearly ₹90,000). The false-precise
on-screen integers (**208 months · ₹88,614**) are **locked by the build calculator**
(₹100-floor model) — displayed on screen, never spoken, never hand-derived here.

## Timing budget

Hindi narration ≈ **12.5 chars/s** (`format.json cuts.hi`). Char counts are the
budget estimate only; the build step regenerates + ffprobe-measures each clip and
adds the per-scene 0.4s lead-in / 1.0s tail before locking scene durations.

| # | Scene | chars | est. |
|---|---|---|---|
| s1 | Hook — the minimum is a trap (month-1 split) | ~220 | ~17.6s |
| s2 | Roadmap — four things | ~135 | ~10.8s |
| s3 | Concept — debt is renting money | ~240 | ~19.2s |
| s4 | Rule — good debt vs bad debt | ~275 | ~22.0s |
| s5 | Audit — how the minimum works + compounding against you | ~260 | ~20.8s |
| s6 | Action — pay more than the minimum | ~225 | ~18.0s |
| s7 | The math — ₹50,000 @ ~40%, 5% min | ~290 | ~23.2s |
| s8 | Do this today — minimum + ₹1,000 | ~240 | ~19.2s |
| s9 | Recap + CTA | ~185 | ~14.8s |
| | **Total** | **~2,070** | **~2:46** |

---

## s1 — HOOK

**VO**
> क्रेडिट कार्ड पर सबसे ख़तरनाक शब्द हैं — 'मिनिमम पेमेंट'। ये सहूलियत नहीं, एक जाल है। पचास हज़ार के बिल पर आप हर महीने पचीस सौ तिरासी रुपये भरते हैं — उसमें से सोलह सौ सरसठ सिर्फ़ ब्याज। कर्ज़ से घटते हैं बस नौ सौ रुपये। आज इसका पूरा हिसाब समझिए।

**On screen** — the month-1 split IS the focal shock.
- kicker: `The most dangerous words on a credit card`
- huge (warn): `"MINIMUM PAYMENT"`
- month-1 anatomy (₹50,000 bill · minimum due):
  ```
  YOU PAY          ₹2,583
  → INTEREST       ₹1,667
  → OFF THE DEBT   ₹  916
  ```
- stamp (warn): `IT'S A TRAP`

**Visuals** — bg keyword: `credit card and bills on wooden table`; cut-in
`hand holding phone with card statement` on «मिनिमम पेमेंट». 3 bg crossfades,
slow Ken Burns push-in.

---

## s2 — ROADMAP

**VO**
> चार बातें — कर्ज़ असल में क्या है, अच्छा और बुरा कर्ज़ का फ़र्क़, मिनिमम पेमेंट अंदर से कैसे चलता है, और ब्याज कैसे आपके ख़िलाफ़ बढ़ता है। और आख़िर में, आज करने वाला एक काम।

**On screen**
- kicker: `By the end you'll know`
- chips (2×2 — max 3 per row): `WHAT DEBT REALLY IS` · `GOOD vs BAD DEBT` /
  `HOW THE MINIMUM WORKS` · `COMPOUNDS AGAINST YOU`
- sub: `Then one thing to do today`

**Visuals** — bg keyword (calmest — roadmap rest beat, still carries a photo per
the every-frame-has-image rule): `₹500 notes flat-lay texture`, slow drift.

---

## s3 — CONCEPT — debt is renting money

**VO**
> पहली बात — कर्ज़ यानी पैसा किराए पर लेना। जो ब्याज देते हैं, वो उस पैसे का किराया है। किराया देना हमेशा ग़लत नहीं — पर देखिए किस चीज़ के लिए। किराए का औज़ार अगर कमाई करा दे, तो किराया वसूल। पर बाहर के खाने या सेल की ख़रीदारी का किराया? चीज़ कल ख़त्म, किराया महीनों चलेगा।

**On screen**
- kicker: `First — what debt really is`
- huge: `DEBT =` + accent span `RENTING MONEY`
- sub: `Interest is the rent`
- two-item contrast: `TOOL THAT EARNS → rent worth it` (fund) ·
  `DINNER, SALE BUY → rent on a ghost` (warn)

**Visuals** — bg keyword: `rolled rupee notes handed over`; cut-in
`restaurant dinner table` on «बाहर के खाने»,
`shopping sale bags` on «सेल की ख़रीदारी».

---

## s4 — RULE — good debt vs bad debt

**VO**
> तो नियम — अच्छा कर्ज़ वो जो ऐसी चीज़ ख़रीदे जिसकी क़ीमत या कमाई बढ़े — पढ़ाई, हुनर, अपना काम-धंधा। कर्ज़ चुकते-चुकते वो चीज़ ख़ुद आपके लिए कमाती है। बुरा कर्ज़ सिर्फ़ ख़र्च के लिए — कपड़े, गैजेट, छुट्टी — जो बिल आने से पहले ग़ायब। सबसे बुरा, कार्ड का बक़ाया। पर याद रखिए — कर्ज़ तभी अच्छा, जब फ़ायदा ब्याज से ज़्यादा हो।

**On screen** — two-column classifier (the focal).
- kicker: `The rule`
- col `GOOD DEBT — value grows` (fund): chips `EDUCATION` · `A SKILL` · `A BUSINESS`
- col `BAD DEBT — just spending` (warn): chips `CLOTHES` · `GADGETS` · `HOLIDAYS`
- stamp (warn): `CARD REVOLVE = WORST`
- foot (the honest caveat): `Even good debt is only "good" if the return beats the interest`

**Visuals** — bg keyword: `graduation cap on stack of books` (good side);
cut-in `shopping bags on arm` on «कपड़े, गैजेट, छुट्टी» (bad side). Densest scene →
calm bg, per design §5.

---

## s5 — AUDIT — how the minimum works + compounding against you

**VO**
> अब देखिए ये जाल अंदर से कैसे चलता है। बैंक बक़ाया का पाँच परसेंट माँगता है — और वो रक़म पहले पूरा ब्याज भरती है। यानी बैंक का ब्याज हमेशा वसूल, आपका मूल कर्ज़ मुश्किल से घटता है। ऊपर से लगता है ब्याज पर ब्याज। निवेश में यही चक्रवृद्धि दौलत बनाती है — कार्ड पर यही आपके ख़िलाफ़ दौड़ती है।

**On screen**
- kicker: `How the minimum actually works`
- rule block: `MINIMUM = 5% of balance` → `interest is paid FIRST` →
  `bank's interest: always covered · your principal: barely moves`
- huge (warn): `INTEREST ON INTEREST`
- snowball line: `COMPOUNDING — for you when you invest, against you on a card`
- foot: `RBI + issuer MITC 2026 · min must cover 100% of interest · ₹100 floor`

**Visuals** — bg keyword: `bank statement close-up`; cut-in `snowball rolling
downhill` on «चक्रवृद्धि» (the snowball-against-you motif). Densest scene → calm bg.

---

## s6 — ACTION — pay more than the minimum

**VO**
> निकलने का रास्ता एक ही — मिनिमम से ज़्यादा भरिए। मिनिमम बना ही इसलिए है कि आप सालों फँसे रहें। जिस दिन आप मिनिमम से हज़ार रुपये ऊपर भरना शुरू करते हैं, उसी दिन से सालों का ब्याज कटने लगता है। हर बढ़ा हुआ रुपया सीधे मूल कर्ज़ पर चोट करता है।

**On screen**
- kicker: `The only way out`
- huge: `PAY MORE THAN THE` + fund span `MINIMUM`
- flow: `MINIMUM` → `+ ₹1,000/mo` → `CUTS YEARS OFF THE TRAP`
- sub: `Every extra rupee hits the principal directly`

**Visuals** — bg keyword: `hand paying bill on phone banking app`; cut-in
`UPI payment confirmation screen` on «भरना शुरू करते हैं».

> **No fabricated figure:** the `+₹1,000` amount is the creator's action step;
> the *effect* stays qualitative ("cuts years off") because facts-staging supplies
> no build-locked payoff for the minimum-plus-₹1,000 case. See build-handoff #6.

---

## s7 — THE MATH (₹50,000 @ ~40%, 5% minimum)

**VO**
> अब पूरा हिसाब। पचास हज़ार का बक़ाया, क़रीब चालीस परसेंट सालाना ब्याज — भारत में आम बात — और आप सिर्फ़ पाँच परसेंट मिनिमम भरते हैं। एक साल बाद भी पचास में से क़रीब चालीस हज़ार बाक़ी। पूरा चुकाने में लगेंगे सत्रह साल से भी ज़्यादा — और सिर्फ़ ब्याज में क़रीब नब्बे हज़ार रुपये। यानी जितना उधार लिया, उससे भी ज़्यादा।

**On screen** — the figures are the visual; reveal in three anchors, punch on the last.
- setup: `₹50,000 · ~40% APR · 5% minimum only`
- APR label (never a single bank): `40% — illustrative, typical retail range`
- reveal rows:
  ```
  AFTER 1 YEAR     still ₹40,045 owed
  TIME TO CLEAR    208 MONTHS  (17+ years)
  INTEREST PAID    ₹88,614
  ```
- huge (warn, the punch): `₹88,614 INTEREST > ₹50,000 BORROWED`
- foot: `₹100-floor model · Federal Bank/ICICI MITC 2026 · figures build-calculator locked`

**Visuals** — bg keyword (calmest — densest scene): `dark desk with calculator and
ledger`, slow drift; the numbers carry the scene. Counter/reveal animates, no busy bg.

---

## s8 — DO THIS TODAY

**VO**
> तो आज का काम — इसी महीने कार्ड का बिल खोलिए, और मिनिमम से कम से कम हज़ार रुपये ज़्यादा भरिए। और एक पक्का नियम — जो चीज़ पूरी क़ीमत में नहीं ख़रीद सकते, उसे कार्ड पर घुमाइए मत। कर्ज़ बुरा नहीं — बिना सोचे लिया कर्ज़ बुरा है।

**On screen**
- stamp (pop): `DO THIS TODAY`
- chips + arrows: `OPEN YOUR CARD BILL` → `PAY MINIMUM + ₹1,000` → `THIS MONTH`
- rule: `Can't buy it in full? Don't revolve it on the card.`
- sub: `Debt isn't bad — thoughtless debt is.`

**Visuals** — bg keyword: `hand tapping phone banking app close-up`.

---

## s9 — RECAP + CTA

**VO**
> तो सीधी बात — कर्ज़ यानी पैसा किराए पर। अच्छा कर्ज़ कुछ बढ़ाता है, बुरा सिर्फ़ ख़र्च कराता है। मिनिमम पेमेंट एक जाल है — हमेशा उससे ज़्यादा भरिए। पैसे की ऐसी सीधी बात के लिए — सब्सक्राइब कीजिए।

**On screen**
- recap chips (2×2 — max 3 per row): `DEBT = RENTED MONEY` · `GOOD GROWS, BAD DRAINS` /
  `MINIMUM = A TRAP` · `ALWAYS PAY MORE`
- stamp (pop): `SUBSCRIBE`

**Visuals** — bg keyword: `young indian man confident with phone`.

---

## Fact trace (every number → facts-staging.md)

| Number in script | Where | facts-staging.md line |
|---|---|---|
| ₹50,000 balance | s1, s7 | Hero example (run.json + "Hero example" head) |
| ₹2,583 minimum due (month 1) | s1 | COMPUTED — "Month 1: minimum due = 5% of ₹51,667 = ₹2,583" |
| ₹1,667 interest (month 1) | s1 | COMPUTED — "of which ₹1,667 is interest" |
| ₹916 off principal (month 1) | s1 | COMPUTED — "only ₹916 reduces the ₹50,000" |
| ~40% APR ("illustrative, typical range") | s7 | Claim ₹-1 — 40–45% typical retail; "use around 40% / 40–45%, never a single bank" |
| 5% minimum · interest-first · ₹100 floor | s5, s7 | Claim ₹-2 — MAD = 5% of total due, ₹100 floor, RBI "covers 100% of interest / no negative amortization" |
| still ~₹40,000 after 1 year (on-screen ₹40,045) | s7 | COMPUTED — "Month 12 ≈ ₹40,000 (closed form ₹40,045)" |
| 208 months / 17+ years | s7 | COMPUTED range 200–210 mo (~17 yr); **build-calculator locked** 208 |
| ₹88,614 interest | s7 | COMPUTED range ₹85–90k; **build-calculator locked** ₹88,614 |
| interest > amount borrowed | s7 | COMPUTED — "≈ ₹85–90k pure interest on a ₹50,000 debt / more than you borrowed" |
| compounding for-you / against-you | s5 | THE TERMINATING MODEL + Claim ₹-2 (interest-on-interest); "snowball" analogy = long_form_scripting §10 bank |
| ₹1,000 more than minimum | s6, s8 | run.json `action_step` — "even Rs. 1,000 more" |

**Deliberately NOT used (so audit doesn't rediscover):**
- No single-bank APR on screen (staging: "Do NOT state a single-bank number; use ~40% / 40–45%").
- No computed "+₹1,000 → saves ₹X / clears in Y months" — no build-locked figure exists; kept qualitative (s6).
- The pure-5%-no-floor "never repaid" asymptote — true and available, but omitted from VO (too technical for a 12.5 c/s short); the "trap" framing carries it.
- No SOFT rows (HDFC/aggregator restatements) on screen alone.
- **No US-dollar symbol, no US institution, no cross-market figure** — ₹ set only (hi cut; dollar sign forbidden per format.json).

## Build handoff

1. `assets/voice/hindi-lines.json` = `{s1..s9}` with **only** the VO paragraphs above
   (no markdown, no on-screen text). Devanagari, verbatim.
2. TTS via `tools/tts/elevenlabs_tts.py`, voice `HTUuC7OeeEt6OL5fViVe` (Harsh),
   `eleven_multilingual_v2`, style 0. Budget: **9 calls** of the run's 30.
3. ffprobe-measure each clip → `data-start` / `data-duration`; re-check the ~165s
   total (add 0.4s lead-in + 1.0s tail per scene) before locking.
4. Images: keyword-matched bg for **all 9 scenes** (`photo_free_scene_ratio` = 0,
   creator rule 2026-07-28) + the cut-ins listed per scene. md5 the asset ledger —
   no image may repeat across videos/channels.
5. **s7 figures are calculator output, not script constants.** Regenerate
   `₹40,045 / 208 months / ₹88,614` from the ₹ model (B₀=₹50,000, APR 40% monthly
   i=0.033333, P = max(5%·statement, ₹100), stop at B≤0). On-screen numerals must
   equal that run; the VO stays a round range regardless. `en-IN` grouping.
6. If a data-backed `+₹1,000` contrast is wanted on screen in s6, the **build
   calculator must compute it** (same model, P = max(5%·statement,₹100)+₹1,000) —
   do not hand-type it; today's on-screen text is deliberately qualitative.
