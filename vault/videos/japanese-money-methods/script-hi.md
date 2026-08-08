---
summary: Hindi/India script for «Japan ke 3 paise wale tarike». LONG tier, per-line chapter architecture — 92 single-sentence VO lines across 8 chapters, 7,598 chars ≈ 10:57 vs the 660s target. INR only, no ¥→₹ conversion, no Japan-vs-India saving-rate head-to-head anywhere. Standard Hindi (Harsh). On-screen text English/Hinglish, ledger-rail. Every number traces to videos/japanese-money-methods/facts-staging.md.
updated: 2026-08-01
source: run.json creator brief + premise_correction (2026-08-01) + facts-staging.md attempt 1 + study note knowledge/video-studies/japanese-money-methods.md. Architecture ledger-rail per run.json; layout spec from knowledge/finance-audit-2026-07-29/03-design.md §4A.
stage: fin-script, cut hi, attempt 1
---

# «जापान के तीन तरीक़े» — Hindi / India edition (LONG, per-line chapters)

**Studio project (to build):** `studio/videos/japanese-money-methods-hi`
**Voice:** ElevenLabs **Harsh** `HTUuC7OeeEt6OL5fViVe`, `eleven_multilingual_v2`, style 0.
Standard Hindi, Devanagari — channel voice locked 2026-07-28.
**On-screen text:** English / Hinglish + romaji. **Title + description:** Roman script.
**Architecture:** `ledger-rail` (run.json). **LONG tier → per-line chapters** — none of the
9-segment blockframe constants apply, and `lines: 9` on the `ledger-rail` registry entry is
a SHORT-tier constant. **One line = one TTS clip = one scene = one exact timeline anchor.**

**Engine rule:** digits are **spelled out** in every VO line (bare Latin digits are a
coin-flip English reading in ElevenLabs). On-screen numerals carry the exact figures,
`Intl.NumberFormat("en-IN")` grouping.

**Persona rules (YouTube 2026 AI carve-out):** no host persona, no first-person expertise,
no fund/stock/scheme pick. **मैं** and **हम** appear nowhere in the VO. PPF and the monthly
investing minimum appear **only as price evidence** — never as "put your money here".

---

> ### ⚠ THE SIX THINGS THAT MUST NOT ENTER THIS CUT
> 1. **NEVER a Japan-vs-India or Japan-vs-US saving-rate comparison** — spoken, on screen,
>    or implied by adjacency. Three different definitions (`facts-staging.md` §1, §6).
>    **India's 7.0% and 34.2% are therefore not used at all** — see "Deliberately NOT used".
> 2. **NEVER "Japanese people save because of their culture."** Horioka (NBER WP 33181, J7):
>    culture, tradition and national character are **not a major determinant**. Chapter 3
>    says the opposite of the source video, out loud.
> 3. **NEVER a rupee or dollar equivalent of a yen figure.** J4/J5 stay in yen or become
>    percentages. the dollar glyph appears nowhere in this file, not even inside a claim ID.
> 4. **NEVER a number attached to mottainai, hara hachi bu or taru wo shiru.** They are
>    principles. No calories, no lifespans, no "kakeibo saves you 35%" (§5.2 — searched, no
>    study exists).
> 5. **NEVER attribute the four kakeibo pillars to Hani Motoko or to 1904.** She gets the
>    budget-first idea (HARD); Needs/Wants/Culture/Unexpected is the modern English
>    repackaging (SOFT). Line 6.7 says so on the record — that honesty is the moat.
> 6. **NEVER "121 years old."** Say "1904" or "over a hundred years ago". The publisher
>    counted the 120th in 2025 from the **1905** edition.

---

## Title options (Roman script — per the title-language rule)

1. **Japan Ke 3 Paise Wale Tarike — Jo Kisi Finance Course Mein Nahi Milte**
   *(recommended — countable promise front-loaded, no claim the facts can't carry)*
2. 37.8% ya 1%? Japan Ki Bachat Ka Asli Hisaab | Japanese Money Methods Hindi
3. Mottainai, Hara Hachi Bu, Kakeibo — Japan Ke 3 Tarike Jo Aaj Se Chalu Ho Sakte Hain

⚠ The source video's title question ("जापानी लोग गरीब क्यों नहीं होते?") is **retired** with
the premise. Do not restore it in packaging.

---

## Chapters (ship as YouTube chapters — study conclusion 10; nobody in the packet has them)

| # | Chapter | starts | lines | chars |
|---|---|---|---|---|
| 1 | Aapka salary month | 0:00 | 10 | 639 |
| 2 | Japan ke apne do aankde | 0:57 | 11 | 854 |
| 3 | Wo paisa jaata kahan hai | 2:11 | 12 | 1,083 |
| 4 | Mottainai | 3:44 | 13 | 1,127 |
| 5 | Hara Hachi Bu | 5:21 | 12 | 1,085 |
| 6 | Kakeibo | 6:54 | 14 | 1,166 |
| 7 | **Taru wo Shiru** (the unpromised fourth) | 8:34 | 12 | 964 |
| 8 | Aaj raat ka ek kaam + recap | 9:58 | 8 | 680 |

---

## Timing budget

Hindi narration = **13.03 chars/s** (`format.json cuts.hi.chars_per_second` — the measured
FLAT delivered rate, pause silence included). LONG charges **0.25s lead-in + 0.55s tail per
line** (`tiers.long`) = **0.8 × 92 = 73.6s** of inter-line padding.

**Budget formula** (the trap in `cuts.en._chars_per_second_trap` — padding is not audio, so
it comes out of the target *before* the rate is applied):
`(660 − 73.6) × 13.03 = 7,640 char budget`. This draft is **7,598 (−0.5%)** after the
fin-audit-hi-1 edits (was 7,544 / −1.3%).

| Ch | lines | chars | VO | + padding | runtime | starts |
|---|---|---|---|---|---|---|
| 1 | 10 | 639 | 49.0s | 8.0 | 57.0s | 0:00 |
| 2 | 11 | 854 | 65.5s | 8.8 | 74.3s | 0:57 |
| 3 | 12 | 1,083 | 83.1s | 9.6 | 92.7s | 2:11 |
| 4 | 13 | 1,127 | 86.5s | 10.4 | 96.9s | 3:44 |
| 5 | 12 | 1,085 | 83.3s | 9.6 | 92.9s | 5:21 |
| 6 | 14 | 1,166 | 89.5s | 11.2 | 100.7s | 6:54 |
| 7 | 12 | 964 | 74.0s | 9.6 | 83.6s | 8:34 |
| 8 | 8 | 680 | 52.2s | 6.4 | 58.6s | 9:58 |
| | **92** | **7,598** | **583.1s** | **73.6s** | **656.7s** | |

**Estimated runtime 656.7s (10:57) vs the 660s target — 0.5% under.** LONG's `min_seconds`
is 600, so the floor is clear by 57s. Char counts are a budget estimate (±5%); the build
step recounts them programmatically from the extracted lines file, then ffprobe-measures
every clip.

**Pace:** 656.7 / 92 = **7.14s average scene** (`target_scene_seconds` 6.5,
`max_scene_seconds` 9.0). Longest line 103 chars → 7.9s VO + 0.8 = **8.7s**, under the
photo-hold ceiling. Shortest 57 chars → 4.4s, well over `tts.min_clip_seconds` 1.0.
**No line may exceed 105 characters** — that is where a scene breaches the hold check.

### Where the retention beats land

- **Promise** at **1.2 ≈ 0:08** (clause opens ~7.9s, closes ~11.6s), restated and expanded
  at 2.1 = **0:57**; **first number** at 2.3 = **1:15**. ⚠ fin-audit-hi-1 moved this: the
  draft had NO promise until 0:54 and failed the 15-second promise gate outright. The
  pain-mirror still runs 0:00–0:57 with zero *stats* and entirely in second person (study
  conclusion 1), but the countable promise is now paid inside the first fifteen seconds —
  the study's "spend 40s before the promise" reading does not override the gate.
- **Mid-video drop zone (55–65% = 6:01–7:07)** opens on 5.11, the honesty beat, and 5.12,
  a tension bridge — not a flat transition.
- **~70% (7:37)** lands on **6.7**: the famous four categories are told, on the record, to
  be a later Western addition. The video's most distinctive moment is an admission.
- **The unpromised fourth method** opens at **8:31 = 78%** (TOP's ran 72–87%; this one
  78–91%, pushed later because this cut carries a longer evidence chapter).
- **One stacked CTA**, once, at 8.7–8.8 ≈ **97%**.

---

## Per-scene timing budget

`chars` → `est s` at 13.03 chars/s. Add 0.8s per line for lead-in + tail to get scene duration.

| # | chars | est s | | # | chars | est s | | # | chars | est s |
|---|---|---|---|---|---|---|---|---|---|---|
| 1.1 | 47 | 3.6 | | 4.1 | 91 | 7.0 | | 6.7 | 94 | 7.2 |
| 1.2 | 94 | 7.2 | | 4.2 | 97 | 7.4 | | 6.8 | 70 | 5.4 |
| 1.3 | 71 | 5.4 | | 4.3 | 96 | 7.4 | | 6.9 | 71 | 5.4 |
| 1.4 | 54 | 4.1 | | 4.4 | 84 | 6.4 | | 6.10 | 82 | 6.3 |
| 1.5 | 61 | 4.7 | | 4.5 | 79 | 6.1 | | 6.11 | 70 | 5.4 |
| 1.6 | 77 | 5.9 | | 4.6 | 79 | 6.1 | | 6.12 | 78 | 6.0 |
| 1.7 | 67 | 5.1 | | 4.7 | 78 | 6.0 | | 6.13 | 103 | 7.9 |
| 1.8 | 58 | 4.5 | | 4.8 | 95 | 7.3 | | 6.14 | 97 | 7.4 |
| 1.9 | 53 | 4.1 | | 4.9 | 79 | 6.1 | | 7.1 | 57 | 4.4 |
| 1.10 | 57 | 4.4 | | 4.10 | 83 | 6.4 | | 7.2 | 76 | 5.8 |
| 2.1 | 99 | 7.6 | | 4.11 | 98 | 7.5 | | 7.3 | 71 | 5.4 |
| 2.2 | 63 | 4.8 | | 4.12 | 98 | 7.5 | | 7.4 | 94 | 7.2 |
| 2.3 | 74 | 5.7 | | 4.13 | 70 | 5.4 | | 7.5 | 79 | 6.1 |
| 2.4 | 52 | 4.0 | | 5.1 | 97 | 7.4 | | 7.6 | 84 | 6.4 |
| 2.5 | 70 | 5.4 | | 5.2 | 62 | 4.8 | | 7.7 | 93 | 7.1 |
| 2.6 | 79 | 6.1 | | 5.3 | 88 | 6.8 | | 7.8 | 80 | 6.1 |
| 2.7 | 66 | 5.1 | | 5.4 | 86 | 6.6 | | 7.9 | 90 | 6.9 |
| 2.8 | 72 | 5.5 | | 5.5 | 96 | 7.4 | | 7.10 | 84 | 6.4 |
| 2.9 | 99 | 7.6 | | 5.6 | 103 | 7.9 | | 7.11 | 83 | 6.4 |
| 2.10 | 88 | 6.8 | | 5.7 | 95 | 7.3 | | 7.12 | 73 | 5.6 |
| 2.11 | 92 | 7.1 | | 5.8 | 99 | 7.6 | | 8.1 | 72 | 5.5 |
| 3.1 | 73 | 5.6 | | 5.9 | 94 | 7.2 | | 8.2 | 76 | 5.8 |
| 3.2 | 100 | 7.7 | | 5.10 | 73 | 5.6 | | 8.3 | 87 | 6.7 |
| 3.3 | 81 | 6.2 | | 5.11 | 100 | 7.7 | | 8.4 | 78 | 6.0 |
| 3.4 | 100 | 7.7 | | 5.12 | 92 | 7.1 | | 8.5 | 80 | 6.1 |
| 3.5 | 101 | 7.8 | | 6.1 | 97 | 7.4 | | 8.6 | 93 | 7.1 |
| 3.6 | 86 | 6.6 | | 6.2 | 79 | 6.1 | | 8.7 | 101 | 7.8 |
| 3.7 | 82 | 6.3 | | 6.3 | 71 | 5.4 | | 8.8 | 93 | 7.1 |
| 3.8 | 88 | 6.8 | | 6.4 | 71 | 5.4 | | | | |
| 3.9 | 98 | 7.5 | | 6.5 | 96 | 7.4 | | | | |
| 3.10 | 81 | 6.2 | | 6.6 | 87 | 6.7 | | | | |
| 3.11 | 102 | 7.8 | | | | | | | | |
| 3.12 | 91 | 7.0 | | | | | | | | |

---

## The ledger-rail spec, as this script uses it

`knowledge/finance-audit-2026-07-29/03-design.md` §4A:

- **`.scene` is `grid-template-columns: 300px 1fr`.** The left rail carries the scene id at
  96px **weight 200** (the thin end of the axis the system has never used), a `--muted`
  hairline, then the beat label at 26px tracked 4px. At LONG the label is the **chapter
  name**, persisting for the whole chapter so the rail reads as a spine.
- **The photograph is a hard-edged right panel** (x=1180→1920, full height) with one
  `linear-gradient(90deg, #0d1017, transparent 30%)` left edge. **The four-layer scrim and
  every `text-shadow` delete** — type sits on flat `--bg`. That is the whole point.
- **Content column flush left, ragged right, max-width 1200px. Two type sizes per scene:**
  `head:` (54px/800) + **one** of `stmt:` (44px/500) or `num:` (200px/900, `tabular-nums`).
  `foot:` (26px/200 `--muted`) is the permitted third and carries the source or the
  illustrative label.
- **One role colour per scene, ever.** `--warn` red = the leak, or a real number used
  wrongly · `--fund` green = the behaviour that works once it exists · `--target` amber = a
  figure or definition under examination · `--pop` orange = the CTA block, **once**, at 8.7.
- **Ken Burns inside the panel** (`1.0 ↔ 1.06`), alternating per scene. Boundary = 0.45s
  cross-dissolve (`scene.transition_seconds`).
- **`RAIL OFF` is the anti-sameness device:** on seven scenes the rail retracts and the
  photo goes full-bleed. Those seven are **1.1, 2.7, 3.12, 4.10, 6.7, 7.4, 8.6** — the
  hook, the thesis, the honest line, the one question, the admission, the stone, the close.
  Nothing else may use it.

---

# THE SCRIPT

> **VO block rule.** Every `>` quoted line below is a VO line, verbatim, and is the only
> thing that goes to TTS. Everything in backticks is a production cue and never spoken.
> **Slice these strings — never retype them.** Retyping Devanagari silently swaps characters
> (nukta, chandrabindu) and the swap is inaudible until the render.

---

## Chapter 1 — आपका सैलरी महीना (PAIN-MIRROR COLD OPEN · no stat, no greeting, no roadmap)

*Study conclusion 1. Fifty-seven seconds, entirely second person, entirely concrete, and not
one statistic — the cost of entry is paid in recognition. No title card anywhere. The one
thing that is NOT deferred is the promise: 1.2 names the three methods inside the first
fifteen seconds (fin-audit-hi-1), because the 15-second promise gate outranks the study.*

**1.1**
> महीने की पहली तारीख़। तनख़्वाह अकाउंट में आ गई।

`[RAIL OFF | img: a phone face-up on a kitchen counter at night, notification glow, no face | head: THE FIRST | stmt: Salary is in.]`

**1.2**
> फ़ोन पर वो नोटिफिकेशन दो सेकंड अच्छा लगता है — और बाक़ी महीने के लिए जापान के तीन तरीक़े हैं।

`[rail 1.2 · AAPKA SALARY MONTH | img: same counter, tighter crop — ONE continuous zoom across 1.1 and 1.2 | head: TWO SECONDS | stmt: Then the rest of the month. And Japan's three methods. | colour: --fund]`

`[AUDIT fin-audit-hi-1: rewritten. The cut previously carried NO payoff promise until 2.1 at 0:54, failing the 15-second promise gate. The promise clause now opens at ~7.9s and closes by ~11.6s. Still no statistic in Chapter 1 — "तीन" is a count, not a figure.]`

**1.3**
> फिर किराया जाता है। फिर बिजली का बिल, जो इस बार पिछली बार से ज़्यादा है।

`[rail 1.3 | img: a rent receipt and an electricity bill weighted under a steel glass | head: THEN RENT | stmt: Then the power bill. Higher than last time. | colour: --warn]`

**1.4**
> फिर वो सब्सक्रिप्शन कटता है जो पिछले साल चालू किया था।

`[rail 1.4 | img: a bank SMS printout, one debit line circled in pen | head: THEN THE AUTO-DEBIT | stmt: The subscription you started last year.]`

**1.5**
> एक शादी का लिफ़ाफ़ा, दो बार बाहर का खाना, और एक ऑनलाइन ऑर्डर।

`[rail 1.5 | img: a red-and-gold shagun envelope beside a food-delivery bag on a table | head: AND THEN | stmt: One wedding envelope. Two dinners out. One order.]`

**1.6**
> कुछ भी बड़ा नहीं था। हर चीज़ छोटी थी, हर चीज़ ज़रूरी थी, और हर चीज़ जायज़ थी।

`[rail 1.6 | img: a spread of small paper bills and receipts on a bedsheet | head: NOTHING WAS BIG | stmt: Every one was small. Every one was fair.]`

**1.7**
> और बीस तारीख़ आते-आते अकाउंट ऐसा दिखता है जैसे तनख़्वाह आई ही न हो।

`[rail 1.7 | img: a wall calendar with the 20th circled, evening light | head: BY THE 20th | stmt: The account looks like the salary never arrived. | colour: --warn]`

**1.8**
> फिर आप हिसाब लगाते हैं और कोई एक बड़ा ख़र्च मिलता ही नहीं।

`[rail 1.8 | img: a hand doing arithmetic in a diary margin, hand only, no face | head: YOU DO THE SUM | stmt: And there is no single big expense to blame.]`

**1.9**
> पैसा किसी एक जगह नहीं गया। वो हर जगह थोड़ा-थोड़ा गया।

`[rail 1.9 | img: water draining through many small holes in a steel plate | head: WHERE IT WENT | stmt: Not one place. A little everywhere. | colour: --warn]`

**1.10**
> क्या यह आपकी कहानी है? अगर हाँ, तो यह वीडियो आपके लिए है।

`[rail 1.10 | img: an empty steel chair at a kitchen table, one lamp on | head: IS THIS YOURS? | stmt: Then this one is for you.]`

---

## Chapter 2 — जापान के अपने दो आँकड़े (THE PROMISE + THE NUMBER)

*The premise correction lives here. The debunk runs on Japan's OWN two published numbers —
one government, one year, two surveys — so no cross-market comparison is needed or made.
`facts-staging.md` J1/J2/J3.*

**2.1**
> आज तीन जापानी तरीक़ों की बात, जो सैकड़ों साल पुराने हैं और किसी फ़ाइनेंस कोर्स में नहीं पढ़ाए जाते।

`[rail 2.1 · JAPAN KE DO AANKDE | img: a Japanese wooden shopfront noren curtain at dusk | head: THREE METHODS | stmt: Centuries old. In no finance course. | colour: --fund]`

**2.2**
> पर उससे पहले वो आँकड़ा, जिसकी वजह से जापान आपकी फ़ीड पर आता है।

`[rail 2.2 | img: a phone held up showing a blurred short-video feed, hand only | head: FIRST, THE NUMBER | stmt: The one that put Japan on your feed.]`

**2.3**
> इंटरनेट कहता है कि जापानी लोग अपनी तनख़्वाह का सैंतीस परसेंट बचा लेते हैं।

`[rail 2.3 | img: a printed statistics table, macro, one row in focus | head: THE CLAIM | num: 37.8% | foot: Statistics Bureau of Japan, Kakei Chosa 2024 annual summary, Table I-2-2 | colour: --target]`

**2.4**
> यह आँकड़ा असली है। जापान की सरकार ख़ुद इसे छापती है।

`[rail 2.4 | img: a government publication cover on a desk, official seal visible | head: IT IS REAL | stmt: Japan's own government publishes it.]`

**2.5**
> दो हज़ार चौबीस के परिवार-ख़र्च सर्वे में यह सैंतीस दशमलव आठ परसेंट है।

`[rail 2.5 | img: the same table, wider — columns of figures | head: THE SURVEY | num: 37.8% | foot: FIES 2024, salaried-worker households: surplus JPY 197,432 of disposable JPY 522,569 | colour: --target]`

**2.6**
> उसी साल, उसी सरकार के राष्ट्रीय लेखा आँकड़ों में यही बचत दर क़रीब एक परसेंट है।

`[rail 2.6 | img: a second, thicker bound volume beside the first | head: THE SAME YEAR | num: ABOUT 1% | foot: National Accounts (SNA) household saving rate, calendar 2024 — Horioka, NBER WP 33181, p.7 | colour: --target]`

**2.7**
> एक ही देश, एक ही साल, एक ही सरकार — और तीस गुना से भी बड़ा फ़र्क़।

`[RAIL OFF | img: two identical brass weights of visibly different size on a shop balance | head: ONE GOVERNMENT. ONE YEAR. | num: 30 TIMES | foot: "more than 30 times as high" — Horioka, NBER WP 33181, p.7 | colour: --warn]`

**2.8**
> फ़र्क़ इसमें है कि किसे गिना जा रहा है, और किस तरीक़े से गिना जा रहा है।

`[rail 2.8 | img: two clipboards side by side, different forms | head: THE DIFFERENCE | stmt: Who is counted. And how.]`

**2.9**
> सैंतीस वाला आँकड़ा सिर्फ़ नौकरीपेशा परिवारों का है, दूसरा सबका — बुज़ुर्ग, बेरोज़गार, दुकानदार, सब।

`[rail 2.9 | img: a crowded Osaka pedestrian crossing, wide, faces indistinct | head: WHO IS IN | stmt: 37.8% counts salaried households only. The other counts everyone. | foot: Horioka p.7 — the National Accounts include the self-employed, unemployed, retired and unincorporated enterprises]`

**2.10**
> दोनों आँकड़े सच हैं। पर इंटरनेट सिर्फ़ बड़ा वाला उठाता है, क्योंकि छोटा वाला बिकता नहीं।

`[rail 2.10 | img: a newspaper folded so only the headline shows | head: BOTH ARE TRUE | stmt: Only one of them travels. | colour: --warn]`

**2.11**
> तो सवाल यह है कि इन तरीक़ों में असल में बचता क्या है — और वो आपके तीस हज़ार पर कैसे लगता है।

`[rail 2.11 | img: a ₹500 note held flat against a plain grey card | head: THE REAL QUESTION | stmt: What survives in the methods — and what it does to ₹30,000 | foot: ₹30,000/mo in-hand is this channel's worked example, not a national average]`

---

## Chapter 3 — वो पैसा जाता कहाँ है (THE EVIDENCE CHAPTER)

*J5 (the surplus split), J8 (the one BOJ table that states two markets itself — the ONLY
sanctioned cross-market comparison in this video), J6 (the real high-saving era) and J7
(culture is rejected by the primary literature).*

**3.1**
> उसी सर्वे में यह भी लिखा है कि हर महीने जो रक़म बचती है, वो जाती कहाँ है।

`[rail 3.1 · PAISA JAATA KAHAN HAI | img: a passbook open on a counter, columns of entries | head: THE SAME SURVEY | stmt: It also records where the surplus goes.]`

**3.2**
> उस बचत का लगभग नब्बे परसेंट सीधे बैंक जमा में चला जाता है, और तीन परसेंट के आसपास शेयर और बॉन्ड में।

`[rail 3.2 | img: a bank counter with a queue of deposit slips, no faces | head: WHERE IT LANDS | stmt: About 90% into deposits. About 3% into securities. | foot: ILLUSTRATIVE — computed from the FIES 2024 monthly surplus split (deposits JPY 175,241 · securities JPY 6,705 of JPY 197,432) | colour: --target]`

**3.3**
> यानी जापान बचाता बहुत है, पर उस बचत को काम पर लगाने के मामले में वो बहुत पीछे है।

`[rail 3.3 | img: sealed steel lockers in a row, all shut | head: SAVING IS NOT INVESTING | stmt: Japan saves hard and puts very little of it to work.]`

**3.4**
> बैंक ऑफ़ जापान की एक तालिका बताती है कि जापानी घरों की इक्यावन परसेंट संपत्ति नक़दी और जमा में पड़ी है।

`[rail 3.4 | img: a printed central-bank chart page under a desk lamp | head: JAPAN | num: 51.0% | foot: Cash and deposits, share of household financial assets — Bank of Japan Flow of Funds, Chart 2, end-March 2025 | colour: --target]`

**3.5**
> उसी तालिका में अमेरिकी घरों का यह हिस्सा साढ़े ग्यारह परसेंट है, और इकतालीस परसेंट शेयरों में है।

`[rail 3.5 | img: the same chart page, the second column in focus | head: SAME TABLE, NEXT COLUMN | stmt: Cash 11.5% · Equity 41.5% | foot: The SAME BOJ table states both markets — no conversion, no second source. Asset mix only; this is NOT a saving-rate comparison. | colour: --target]`

**3.6**
> तो जापान की मिसाल बचत की है, निवेश की नहीं — और यही बात ज़्यादातर वीडियो छोड़ देते हैं।

`[rail 3.6 | img: a full clay pot with the lid still tied shut | head: THE HALF NOBODY SHOWS | stmt: Japan is an example of saving. Not of investing.]`

**3.7**
> अब वो हिस्सा जो और भी कम लोग बताते हैं — जापान हमेशा से बचत करने वाला देश नहीं था।

`[rail 3.7 | img: a black-and-white 1950s Tokyo street scene, archival grain | head: AND ONE MORE THING | stmt: Japan was not always a nation of savers. | colour: --warn]`

**3.8**
> युद्ध के बाद सिर्फ़ उन्नीस सौ इकसठ से छियासी तक वहाँ बचत की दर पंद्रह परसेंट से ऊपर रही।

`[rail 3.8 | img: an old wall calendar page, a range of years visible | head: THE HIGH-SAVING ERA | stmt: Postwar, only 1961 to 1986. Twenty-five years. | foot: The only POSTWAR period above 15% — Horioka, NBER WP 33181, p.3. Wartime rates were far higher and were forced saving under rationing (p.2). | colour: --target]`

`[AUDIT fin-audit-hi-1: "युद्ध के बाद" / "Postwar" inserted. Horioka p.3 conditions this claim on the postwar period — "if we confine ourselves to the postwar period, the only period during which Japan's household saving rate exceeded 15% was the 25-year period from 1961 until 1986". p.2 records the rate reaching 44% in the waning years of WWII, so the unqualified "only 1961-1986" was NOT backed by the cited source. facts-staging J6 dropped the qualifier and the script inherited it.]`

**3.9**
> सत्तर के दशक में वो तेईस परसेंट तक गई थी, और दो हज़ार दो के बाद शायद ही कभी पाँच परसेंट से ऊपर गई।

`[rail 3.9 | img: a hand-drawn line on graph paper, peak then decline | head: PEAK, THEN | num: 23.2% | foot: Mid-1970s peak; no higher than 5% since 2002 EXCEPT a temporary blip in 2020 (Covid), and negative in 2013-15, 2017 and 2023 — Horioka, NBER WP 33181, p.2 | colour: --warn]`

`[AUDIT fin-audit-hi-1: "कभी ... नहीं गई" ("never went above") softened to "शायद ही कभी" ("hardly ever"), and the Covid carve-out added to the foot. Horioka p.2 reads "has been no higher than 5% during the past two decades (since 2002) EXCEPT for a temporary blip in 2020 due to the Covid-19 pandemic" — the absolute "never" was not backed by the cited source.]`

**3.10**
> इस पर हुई सबसे बड़ी रिसर्च कहती है कि इसकी वजह जापानी संस्कृति या स्वभाव नहीं था।

`[rail 3.10 | img: a thick working paper on a desk, one paragraph in focus | head: NOT CULTURE | stmt: "Culture, tradition and national character are not a major determinant." | foot: Horioka, NBER WP 33181, sections 3 and 9-10 | colour: --warn]`

**3.11**
> वजह थी उधार का न मिलना, सामाजिक सुरक्षा का न होना, तेज़ी से बढ़ती आमदनी, टैक्स छूट और सरकार का अभियान।

`[rail 3.11 | img: a vintage government savings-campaign poster on a wall | head: THE ACTUAL REASONS | stmt: No consumer credit · No safety net · Fast income growth · A tax break · A state campaign | foot: Horioka, NBER WP 33181, sections 9-10]`

**3.12**
> यानी तरीक़े काम करते हैं — पर वो कभी वजह नहीं थे। और यही इस वीडियो की सबसे ईमानदार लाइन है।

`[RAIL OFF | img: a single lit paper lantern in a dark street, wide | head: THE HONEST LINE | stmt: The methods work. They were never the reason. | colour: --fund]`

---

## Chapter 4 — मोत्ताइनाई (METHOD ONE · the participation beat)

*TOP's move 3, the device none of our six shipped videos has: three physical checks the
viewer performs inside the video. `facts-staging.md` §4 — HARD on the meaning, SOFT on the
etymology detail (the government page 403'd), **zero numbers attached to the principle**.*

**4.1**
> पहला तरीक़ा — मोत्ताइनाई। जापानी में इसका मतलब है, किसी चीज़ की असली क़ीमत का ज़ाया हो जाना।

`[rail 4.1 · MOTTAINAI | img: a chipped but repaired ceramic bowl on a wooden board | head: MOTTAINAI | stmt: A thing's real value, going unused. | foot: Roughly, from mottai, "a thing's rightful worth", plus nai, "without" — attested since about the 13th century]`

**4.2**
> यह बर्बाद मत करो वाली डाँट नहीं है। यह अफ़सोस है — कि जो चीज़ थी, उसका पूरा इस्तेमाल हुआ ही नहीं।

`[rail 4.2 | img: a folded cloth with a worn edge, mended by hand | head: NOT A SCOLDING | stmt: It is regret. Not instruction.]`

**4.3**
> अलमारी में जो कमीज़ टँगी है, उसमें एक किसान की फ़सल है, एक बुनकर के हाथ हैं, एक ट्रक का सफ़र है।

`[rail 4.3 | img: a cotton field at dawn, wide | head: ONE SHIRT | stmt: A farmer's crop. A weaver's hands. A truck's journey.]`

**4.4**
> और उसमें आपकी तनख़्वाह के वो घंटे भी हैं, जो आपने उसे ख़रीदने के लिए काम करके बिताए।

`[rail 4.4 | img: a wall clock in an office corridor, evening | head: AND YOURS | stmt: The hours of your salary that paid for it. | colour: --warn]`

**4.5**
> अब वीडियो रोकिए। उठिए, अलमारी खोलिए, और वो कपड़े गिनिए जिन पर टैग अब तक लगा है।

`[rail 4.5 | img: an open Indian wardrobe, hangers dense, price tags still on two garments | head: PAUSE. CHECK ONE. | stmt: Count the clothes still wearing their tags. | colour: --fund]`

**4.6**
> फिर फ़ोन खोलिए और उन सब्सक्रिप्शन की सूची देखिए जो हर महीने अपने आप कट रही हैं।

`[rail 4.6 | img: a phone's settings list on a table, screen text illegible, hand only | head: CHECK TWO | stmt: The subscriptions list. All of it. | colour: --fund]`

**4.7**
> और आख़िर में फ़्रिज खोलिए, और उस खाने को देखिए जो अगले हफ़्ते फेंक दिया जाएगा।

`[rail 4.7 | img: an open Indian fridge shelf, steel dabbas and a wilting bunch of coriander | head: CHECK THREE | stmt: What will be thrown out next week. | colour: --fund]`

**4.8**
> तीनों जगह जो दिखा, वो पैसे की कमी नहीं है। वो ख़रीदी हुई चीज़ों की बिना इस्तेमाल पड़ी क़ीमत है।

`[rail 4.8 | img: a stack of unopened boxes in a corner of a room | head: WHAT YOU SAW | stmt: Not a shortage of money. Value already bought and never used. | colour: --warn]`

**4.9**
> मोत्ताइनाई एक ही सवाल में सिमट जाता है, और वो सवाल ख़रीदने से पहले पूछा जाता है।

`[rail 4.9 | img: a hand hovering over a shop shelf, not yet touching, hand only | head: IT IS ONE QUESTION | stmt: And it is asked before, not after.]`

**4.10**
> सवाल यह है — क्या इसकी पूरी क़ीमत निकल पाएगी? और अगर जवाब शायद है, तो जवाब नहीं है।

`[RAIL OFF | img: a single object on a bare wooden table, hard side light | head: THE QUESTION | stmt: Will its full value be used? If the answer is MAYBE, the answer is NO. | colour: --fund]`

**4.11**
> तीस हज़ार की तनख़्वाह में यह सवाल महीने में तीन-चार बार ही आता है, पर हर बार एक ख़रीद रोक देता है।

`[rail 4.11 | img: a shopping bag set back down on a counter | head: ON ₹30,000 | stmt: The question comes up three or four times a month. | foot: ₹30,000/mo is the channel's worked example — not a statistic]`

**4.12**
> और यही मोत्ताइनाई का पूरा काम है — ख़र्च कम करना नहीं, बल्कि ख़रीदी हुई चीज़ का पूरा इस्तेमाल करना।

`[rail 4.12 | img: a well-used leather chappal, repaired, beside a new one in its box | head: THE WHOLE POINT | stmt: Not spending less. Using fully what was bought.]`

**4.13**
> अगला तरीक़ा पेट से शुरू होता है, और सीधे आपकी सैलरी पर जा कर रुकता है।

`[rail 4.13 | img: a simple set meal in small bowls, top-down | head: NEXT | stmt: The next one starts at the stomach.]`

---

## Chapter 5 — हारा हाची बू (METHOD TWO · the day-one rule)

*The principle carries **zero** numbers — `facts-staging.md` §5.5 rejects every calorie,
intake and lifespan figure attached to it. The only figures here are Japan's own FIES
consumption share (J4) and the channel's ₹30,000 worked example. 5.11 is the honesty beat
and sits inside the 55–65% drop zone by design.*

**5.1**
> दूसरा तरीक़ा — हारा हाची बू। ओकिनावा में यह पुरानी आदत है, और इसकी जड़ें कन्फ़्यूशियस तक जाती हैं।

`[rail 5.1 · HARA HACHI BU | img: Okinawan elders walking a shoreline path at sunrise, distant, no faces | head: HARA HACHI BU | stmt: An old Okinawan habit, Confucian in origin. | foot: No calorie, intake or lifespan figure is claimed here — every one in circulation is unsourced]`

**5.2**
> इसका मतलब है, पेट के दस हिस्सों में से आठ भर जाएँ तो खाना बंद।

`[rail 5.2 | img: a small rice bowl, deliberately not full, top-down on wood | head: EIGHT PARTS IN TEN | stmt: Stop there.]`

**5.3**
> पेट भरने का एहसास देर से आता है, इसलिए आख़िरी दो हिस्से हमेशा ज़रूरत से ज़्यादा होते हैं।

`[rail 5.3 | img: a hand setting chopsticks down across a bowl, hand only | head: WHY IT WORKS | stmt: Fullness arrives late. The last two parts are always surplus.]`

**5.4**
> अब यही बात तनख़्वाह पर रखिए — दस में से आठ हिस्से पर जीना, और दो हिस्से पहले दिन बाहर।

`[rail 5.4 | img: an Indian kitchen counter, a steel dabba pushed aside from a stack of notes | head: NOW THE SALARY | stmt: Live on eight parts. Move two out on day one. | colour: --fund]`

**5.5**
> तीस हज़ार की तनख़्वाह पर यह बीस परसेंट यानी छह हज़ार रुपये बनते हैं, और जीना चौबीस हज़ार में है।

`[rail 5.5 | img: two unequal stacks of ₹500 notes squared on a table | head: ON ₹30,000 | stmt: ₹6,000 out · ₹24,000 to live on | foot: 20% of the channel's ₹30,000 worked example. An arithmetic split, not a statistic. | colour: --fund]`

**5.6**
> और यह पहली तारीख़ का काम है, तीस तारीख़ का नहीं — महीने के आख़िर में जो बचता है वो हमेशा शून्य होता है।

`[rail 5.6 | img: an empty wallet lying open at month end | head: DAY ONE, NOT DAY THIRTY | stmt: What is left at month end is always zero. | colour: --warn]`

**5.7**
> जापान के उसी सर्वे में नौकरीपेशा परिवार अपनी हाथ में आई आमदनी का बासठ परसेंट ही ख़र्च करते हैं।

`[rail 5.7 | img: the FIES table again, the consumption row in focus | head: JAPAN'S OWN FIGURE | num: 62.2% | foot: Average propensity to consume, salaried-worker households — Statistics Bureau FIES 2024, Table I-2-2. Japan's own number; not compared with any other country's. | colour: --target]`

**5.8**
> यह कोई तपस्या नहीं है। यह सिर्फ़ पहले दिन का एक फ़ैसला है, जो बाक़ी महीने को अपने आप संभाल लेता है।

`[rail 5.8 | img: a switch in the on position, dust on the plate | head: NOT DISCIPLINE | stmt: One decision on day one, carrying the other twenty-nine.]`

**5.9**
> अगर बीस परसेंट ज़्यादा लगे, तो पाँच परसेंट से शुरू कीजिए — तीस हज़ार पर वो पंद्रह सौ रुपये हैं।

`[rail 5.9 | img: a small coin beside a much larger one on a counter | head: IF 20% IS TOO MUCH | num: ₹1,500 | foot: 5% of the ₹30,000 worked example | colour: --fund]`

**5.10**
> महीने-दर-महीने निवेश की न्यूनतम रक़म पाँच सौ रुपये है, और कुछ जगह ढाई सौ।

`[rail 5.10 | img: a ₹500 note and loose coins on a bank counter | head: THE ENTRY TICKET | stmt: ₹500 a month. ₹250 in some. | foot: AMFI — SIP minimum ₹500/mo, ₹250 "Chhoti SIP". Price evidence, not a recommendation. | colour: --target]`

**5.11**
> और सच यह भी है कि अगर ज़रूरतें ही पूरी तनख़्वाह खा जाती हैं, तो यह तरीक़ा पहले महीने काम नहीं करेगा।

`[rail 5.11 | img: a long straight road disappearing at the horizon | head: HONESTLY | stmt: If needs already eat the whole salary, this fails in month one. | colour: --warn]`

**5.12**
> तब सवाल बचत का नहीं, हिसाब का है — और हिसाब वाला तरीक़ा एक औरत ने सौ बरस से भी पहले लिखा था।

`[rail 5.12 | img: an old bound ledger, spine cracked, on a shelf | head: THEN THE QUESTION CHANGES | stmt: Not saving. Accounting. | colour: --target]`

---

## Chapter 6 — काकेइबो (METHOD THREE · and the admission at the ~70% mark)

*Line 6.7 is this video's Von Restorff beat and lands at ~7:37 ≈ **70%**: the famous four
categories are told, on the record, to be a later Western addition (`facts-staging.md` §4 —
SOFT, no Japanese primary found). Every competitor teaches them as Hani Motoko's. Saying
otherwise is the whole differentiator.*

**6.1**
> तीसरा तरीक़ा — काकेइबो। सीधा-सादा मतलब है, घर के हिसाब की किताब, जो हर महीने हाथ से लिखी जाती है।

`[rail 6.1 · KAKEIBO | img: a hand-ruled household ledger open on a low table, pen resting | head: KAKEIBO | stmt: The household account book. Written by hand.]`

**6.2**
> इसे उन्नीस सौ चार में हानि मोतोको ने बनाया, जो जापान की पहली महिला पत्रकार थीं।

`[rail 6.2 | img: an early-1900s Japanese magazine cover, archival | head: 1904 | stmt: Hani Motoko. Japan's first woman journalist. | foot: Fujin no Tomo Sha (publisher primary) + National Diet Library. First edition printed end-1904, for use in the 1905 year. | colour: --target]`

**6.3**
> वो किताब आज भी हर साल छपती है, बीच में चार साल युद्ध की वजह से छूटे थे।

`[rail 6.3 | img: a shelf of identical annual editions, spines aligned | head: STILL PRINTED | stmt: Every year since. Four wartime years missing. | foot: Over a hundred years of continuous publication — the publisher marked the 120th in 2025]`

**6.4**
> उनका असली आविष्कार चार ख़ानों वाला चार्ट नहीं था। उनका आविष्कार बजट था।

`[rail 6.4 | img: a blank ruled page, no headings yet | head: HER ACTUAL INVENTION | stmt: Not the four-column chart. The budget.]`

**6.5**
> साल भर की आमदनी को बारह से बाँटो, बचत का हिस्सा सबसे पहले अलग रखो, और बचा हुआ ख़र्चों में बाँटो।

`[rail 6.5 | img: twelve small equal stacks of coins in a row | head: THE METHOD | stmt: Divide the year by twelve. Set the saving aside FIRST. Then split the rest. | colour: --fund]`

**6.6**
> उन्नीस सौ चार में यह विचार नया था — कि बचत ख़र्च के बाद नहीं, ख़र्च से पहले तय होती है।

`[rail 6.6 | img: an inkwell and nib on a wooden desk, low light | head: WHY IT WAS NEW | stmt: Saving is decided before spending, not after.]`

**6.7**
> जो चार ख़ाने आज सिखाए जाते हैं — ज़रूरतें, चाहतें, संस्कृति और अनपेक्षित — वो बाद का जोड़ हैं।

`[RAIL OFF | img: THE FLAT-LAY (study conclusion 3) — top-down on wood: real ₹ coins and notes in four groups, four handwritten bilingual labels IN THE PHOTOGRAPH, not overlaid: NEEDS ज़रूरतें · WANTS चाहतें · CULTURE संस्कृति · UNEXPECTED अनपेक्षित | head: THE FOUR CATEGORIES | stmt: These came later. They are the version that travelled west. | foot: Consistent across secondary sources; no Japanese primary attributes them to Hani Motoko or to 1904 | colour: --warn]`

**6.8**
> हानि मोतोको के अपने ख़र्च के ख़ाने अलग थे, यह बात साफ़ रखना ज़रूरी है।

`[rail 6.8 | img: the same flat-lay, tighter crop on one handwritten label — ONE continuous zoom from 6.7 | head: SAY IT PLAINLY | stmt: Her own expense heads were different ones.]`

**6.9**
> काकेइबो का असली काम चार सवाल हैं, जो महीने की शुरुआत में पूछे जाते हैं।

`[rail 6.9 | img: a fresh page, dated at the top, nothing written yet | head: WHAT SURVIVES | stmt: Four questions. Asked at the start of the month.]`

**6.10**
> कितना आया। कितना अलग रखना है। कितना ख़र्च होगा। और पिछले महीने से क्या सुधारना है।

`[rail 6.10 | img: four short handwritten lines on ruled paper, macro | head: THE FOUR | stmt: How much came in · How much is set aside · How much goes out · What changes from last month | colour: --fund]`

**6.11**
> ध्यान दीजिए — दूसरा सवाल तीसरे से पहले आता है, और यही पूरा काकेइबो है।

`[rail 6.11 | img: the same page, the second line underlined in ink | head: THE ORDER IS THE METHOD | stmt: Question two comes before question three. | colour: --fund]`

**6.12**
> और यह काग़ज़ पर होता है — क़लम, कॉपी, फ़ोन नीचे, महीने में एक बार पंद्रह मिनट।

`[rail 6.12 | img: a phone lying face-down beside an open notebook and a pen | head: ON PAPER | stmt: Pen. Notebook. Phone face-down. Fifteen minutes.]`

**6.13**
> ऐप महीना बीत जाने के बाद बताता है कि पैसा कहाँ गया; काकेइबो शुरू होने से पहले तय करता है कि कहाँ जाएगा।

`[rail 6.13 | img: a printed bank statement beside the handwritten page | head: APP vs LEDGER | stmt: An app reports where it went. A kakeibo decides where it goes.]`

**6.14**
> पैसा कहाँ रखा जाए यह इस वीडियो का विषय नहीं, पर आज पी-पी-एफ़ की दर सात दशमलव एक परसेंट सालाना है।

`[rail 6.14 | img: a post office counter window, brass grille, no faces | head: TODAY'S RATE, FOR SCALE | num: 7.1% | foot: PPF, Q2 FY2026-27 (Dept. of Economic Affairs notification, unchanged for a ninth straight quarter). Price evidence only — this video recommends no scheme, fund or platform. | colour: --target]`

`[AUDIT fin-audit-hi-1: rewritten. The original named PPF as the destination for the kakeibo set-aside ("on the portion set aside first, you get 7.1% in PPF"), which is a scheme recommendation however the foot is labelled — a monetisation-gate risk under the persona rule. The rate now stands as bare price evidence and the VO says on the record that where to park money is not this video's subject.]`

---

## Chapter 7 — तारु वो शिरु (THE UNPROMISED FOURTH · opens at 78%)

*Study conclusion 2 — promise N, deliver N+1, and make the extra one a re-frame rather than
a mechanic. Nothing here is new information; it is the reason under the first three. §4 is
HARD on the inscription, the temple and the shared-radical design. The donor attribution is
SOFT and is **not** used.*

**7.1**
> वादा तीन तरीक़ों का था। एक और है, और वही सबसे मुश्किल है।

`[rail 7.1 · TARU WO SHIRU | img: a moss-edged stone path in mist, Kyoto | head: THERE IS A FOURTH | stmt: And it is the hard one. | colour: --target]`

**7.2**
> क्योतो के रयोआन-जी मंदिर में एक पत्थर का हौज़ है, जिस पर चार अक्षर खुदे हैं।

`[rail 7.2 | img: the Ryoan-ji rock garden in mist, wide | head: RYOAN-JI, KYOTO | stmt: A stone basin. Four characters cut into it.]`

**7.3**
> उनका मतलब है — जो है, वही काफ़ी है; और इतना जान लेना ही असली अमीरी है।

`[rail 7.3 | img: the tsukubai basin itself, water surface still, top-down. The kanji live IN the photograph — never as composition text | head: WHAT IT SAYS | stmt: What there is, is enough. | foot: The tsukubai inscription at Ryoan-ji, Kyoto]`

**7.4**
> चारों अक्षरों में एक हिस्सा साझा है, और वो हिस्सा हौज़ के बीच का ख़ाली पानी वाला हिस्सा है।

`[RAIL OFF | img: the basin, macro on the square water hole at its centre | head: THE DESIGN | stmt: All four share one part — the emptiness at the centre. | colour: --target]`

**7.5**
> यानी चारों अक्षर अकेले अधूरे हैं। पूरा होने के लिए उन्हें बीच का ख़ालीपन चाहिए।

`[rail 7.5 | img: the same basin, water rings spreading — ONE continuous zoom from 7.4 | head: NONE OF THEM STANDS ALONE | stmt: Each needs the emptiness in the middle to be whole.]`

**7.6**
> अब अपनी पिछली दस साल की सूची देखिए — परीक्षा, नौकरी, पहली तनख़्वाह, फ़ोन, गाड़ी, घर।

`[rail 7.6 | img: an Indian two-wheeler parked outside a rented flat, evening | head: NOW YOUR LIST | stmt: Exam. Job. First salary. Phone. Bike. Flat.]`

**7.7**
> हर बार लगा कि यह मिल जाए तो बात बन जाएगी, और हर बार मिलने के कुछ हफ़्ते बाद लकीर आगे खिसक गई।

`[rail 7.7 | img: a chalk finish line on a road, half rubbed out and redrawn further along | head: EVERY TIME | stmt: The line moved a few weeks after you crossed it. | colour: --warn]`

**7.8**
> इसे आदत कहते हैं — आमदनी बढ़ती है, और उसके साथ ज़रूरत की परिभाषा भी बढ़ जाती है।

`[rail 7.8 | img: two shirts on hangers, near-identical, one newer | head: WHAT HAPPENED | stmt: Income rose. So did the definition of "need".]`

**7.9**
> पूरा बाज़ार इसी बात पर टिका है कि आपके पास जो है, वो आपको कम लगे, और अगली चीज़ ज़रूरी लगे।

`[rail 7.9 | img: a wall of backlit hoardings over a night street, text illegible | head: THE WHOLE MARKET | stmt: It runs on what you have feeling like less. | colour: --warn]`

**7.10**
> तारु वो शिरु का सवाल एक ही है — आपके लिए काफ़ी क्या है? और इसका जवाब जल्दी मत दीजिए।

`[rail 7.10 | img: an empty chair facing a window at first light | head: THE QUESTION | stmt: What is enough for you? Do not answer quickly. | colour: --fund]`

**7.11**
> क्योंकि जिस दिन यह जवाब काग़ज़ पर लिखा जाता है, उस दिन बचत अपने आप शुरू हो जाती है।

`[rail 7.11 | img: a single written line on an otherwise blank page | head: WHY IT MATTERS | stmt: The day it is written down, the saving starts by itself. | colour: --fund]`

**7.12**
> पहले तीन तरीक़े बताते हैं कि पैसा कैसे बचाना है। चौथा बताता है कि किसलिए।

`[rail 7.12 | img: the Ryoan-ji garden at last light, wide | head: THE DIFFERENCE | stmt: Three tell you how. The fourth tells you what for.]`

---

## Chapter 8 — आज रात का एक काम + recap (PEAK-END · one stacked CTA)

*Recap in four single lines, then the action while attention is still on the argument, then
the one CTA in eleven minutes. Study conclusion 8 — the share line is a person, not a verb.*

**8.1**
> मोत्ताइनाई — ख़रीदने से पहले पूछिए कि इसकी पूरी क़ीमत निकल पाएगी या नहीं।

`[rail 8.1 · AAJ RAAT KA EK KAAM | img: the shop shelf from 4.9, hand withdrawn | head: RECAP ONE | stmt: MOTTAINAI — ask before buying, not after.]`

**8.2**
> हारा हाची बू — पहली तारीख़ को दो हिस्से बाहर, और आठ हिस्सों में महीना चलाइए।

`[rail 8.2 | img: the two unequal note stacks from 5.5, new crop | head: RECAP TWO | stmt: HARA HACHI BU — two parts out on day one. Live on eight. | colour: --fund]`

**8.3**
> काकेइबो — महीने की शुरुआत में चार सवाल काग़ज़ पर लिखिए, और बचत का ख़ाना सबसे पहले भरिए।

`[rail 8.3 | img: the ledger page from 6.10, now filled in | head: RECAP THREE | stmt: KAKEIBO — four questions at the start. Savings line first. | colour: --fund]`

**8.4**
> तारु वो शिरु — तय कीजिए कि आपके लिए काफ़ी क्या है, वरना बाक़ी तीनों बेकार हैं।

`[rail 8.4 | img: the still basin from 7.3, later light | head: RECAP FOUR | stmt: TARU WO SHIRU — decide what is enough, or the other three do nothing. | colour: --target]`

**8.5**
> आज रात का काम एक ही है — एक काग़ज़, एक क़लम, और वो चार सवाल; पंद्रह मिनट, आज ही।

`[rail 8.5 | img: a notebook and pen set out under a lamp on an Indian kitchen table, nothing written yet | head: TONIGHT | stmt: One page. One pen. Four questions. Fifteen minutes. | colour: --fund]`

**8.6**
> आज जो सुना वो जानकारी है; जो आज से करना शुरू करेंगे, वो समझ है — और फ़र्क़ सिर्फ़ इतना ही है।

`[RAIL OFF | img: the same table, the page now carrying four handwritten lines | head: THE WHOLE VIDEO | stmt: What you heard is information. What you start is understanding.]`

**8.7**
> कमेंट में बताइए कौन सा तरीक़ा सबसे ज़्यादा चुभा, और पैसे की ऐसी सीधी बात के लिए चैनल सब्सक्राइब कीजिए।

`[rail 8.7 | img: a closed ledger and a capped pen, finished | head: — | num: SUBSCRIBE | foot: Comment which of the four hit hardest | colour: --pop (the single --pop block of the video)]`

**8.8**
> और यह वीडियो उस दोस्त को भेजिए जो हर महीने कहता है कि पता ही नहीं चलता पैसा कहाँ चला जाता है।

`[rail 8.8 | img: two steel cups of tea on a parapet at night, no people | head: SEND IT TO | stmt: The friend who says every month: I don't know where it goes.]`

---

## Fact trace (every number → facts-staging.md)

| Number / claim in script | Where | facts-staging.md row | Tag |
|---|---|---|---|
| **37.8%** — Japan's FIES salaried-worker surplus rate, 2024 | 2.3, 2.5 | **J2** — Statistics Bureau of Japan, *Kakei Chōsa* 2024 annual summary, Table I-2-2, + Horioka p.7 | **HARD** — two independent, one is the issuing agency. Exact on screen and spoken. |
| **about 1%** — Japan's National-Accounts household saving rate, 2024 | 2.6 | **J1** — Horioka, NBER WP 33181, p.2 and p.7 | **HARD on the rate.** The *decimal* 1.1 is single-sourced, so the VO says "क़रीब एक परसेंट" and the screen says `ABOUT 1%`. ⚠ staging asks for `~1%`; the tilde is **absent from the 97-codepoint font subset** (03-design.md §1.4), so it is spelled out. |
| **more than 30 times** the gap | 2.7 | **J3** — Horioka p.7, verbatim "more than 30 times as high" | **HARD**. Screen reads `30 TIMES` (`×` is also absent from the subset). |
| Who each survey counts | 2.9 | **J3** — FIES covers salaried-worker households only; the National Accounts include the self-employed, unemployed, retired and unincorporated enterprises | **HARD** |
| **JPY 197,432 surplus of JPY 522,569 disposable** (screen only, foot) | 2.5 | **J4** — Statistics Bureau, same PDF, Table I-2-2 | **HARD** — stays in yen, never converted, never spoken |
| **~90% to deposits · ~3% to securities** | 3.2 | **J5** — of the ¥197,432 monthly surplus: deposits ¥175,241, securities ¥6,705 | raw ¥ **HARD**; the *ratio* is **COMPUTED** → the frame carries an `ILLUSTRATIVE` foot and the VO says "लगभग" / "के आसपास" |
| **51.0%** Japan cash & deposits | 3.4 | **J8** — Bank of Japan, *Flow of Funds — Overview of Japan, the US and the Euro area*, 29 Aug 2025, Chart 2, end-March 2025 | **HARD** |
| **11.5%** US cash · **41.5%** US equity | 3.5 | **J8 / U3** — the SAME BOJ Chart 2 | **HARD** — one table stating both markets, so this is **not** a cross-market conversion. The foot says so on screen, and says explicitly that it is an asset-mix comparison and **not** a saving-rate one. |
| **1961–1986** above 15% (**postwar only**) · **23.2%** mid-1970s peak · no higher than 5% since 2002 **except the 2020 Covid blip** | 3.8, 3.9 | **J6** — Horioka pp.2–3 and Fig. 1, re-read direct at audit | **HARD as now qualified.** ⚠ fin-audit-hi-1 corrected BOTH halves: staging J6 dropped Horioka's "if we confine ourselves to the postwar period" (the rate hit 44% in the late war years, p.2) and dropped his "except for a temporary blip in 2020 due to the Covid-19 pandemic". The unqualified draft wording was not backed by the cited page. |
| **Culture is not a major determinant** + the actual drivers | 3.10, 3.11 | **J7** — Horioka §3 and §9–10: no consumer credit, no safety net until the 1970s, fast income growth, the Maruyū tax break, state saving campaigns | **HARD** — this is the premise correction, stated on screen |
| **Mottainai** — meaning and etymology | 4.1 | **§4** — 勿体 "rightful value" + ない negation, attested since ~13th century | **HARD on the meaning** (three independent) · **SOFT on the etymology** (gov-online.go.jp 403'd) → the VO gives the meaning; the etymology sits in a `foot:` hedged with "roughly" |
| **Hara hachi bu** — "eight parts in ten", Okinawa, Confucian | 5.1, 5.2 | **§4** — Blue Zones (Buettner) + health secondaries | **SOFT** — term and meaning solid. **No calorie, intake, weight or lifespan number appears anywhere near it**, and 5.1's foot says so on screen. |
| **62.2%** — Japan's average propensity to consume | 5.7 | **J4** — consumption ¥325,137 ÷ disposable ¥522,569, FIES 2024 | **HARD** — Japan's own figure, presented alone; the foot states it is not compared with any other country's |
| **₹30,000/mo** worked example · **₹6,000** (20%) · **₹24,000** · **₹1,500** (5%) | 2.11, 4.11, 5.5, 5.9 | **I5** — vault locked example, channel convention | **CONVENTION**, labelled on screen every time. ⚠ 20% of ₹30,000 is **₹6,000**; the shipped `first-lakh-first-thousand` cut used ₹5,000 for the same split and that was arithmetically wrong. This cut is correct — **do not "fix" it back down**. |
| **₹500/mo minimum · ₹250** | 5.10 | **I9** — AMFI, official | **HARD** — price evidence, and the foot says so |
| **7.1%** — PPF | 6.14 | **I8** — Dept. of Economic Affairs notification, Q2 FY2026-27, unchanged for a ninth consecutive quarter | **HARD** — rate re-verified live at audit (still 7.1% for Jul–Sep 2026). ⚠ fin-audit-hi-1 rewrote the SENTENCE, not the number: the draft routed the kakeibo set-aside INTO PPF, which is a scheme recommendation whatever the foot says. It now reads as bare price evidence and disclaims the placement out loud. |
| **1904** · Hani Motoko · Japan's first woman journalist · still printed · four wartime years missing | 6.2, 6.3 | **§4 Kakeibo** — Fujin no Tomo Sha (publisher primary) + National Diet Library | **HARD**. Screen says "over a hundred years"; **never "121 years"** — the publisher counted the 120th in 2025 from the 1905 edition. |
| The budget-first idea (divide by twelve, saving aside first) | 6.5, 6.6 | **§4 Kakeibo** — the publisher's own words: introducing 予算 to ordinary household finance | **HARD** |
| The four categories are a **later** addition | 6.7, 6.8 | **§4** — the four pillars are what the Western/English repackaging teaches (Fumiko Chiba, 2017 onward); Hani's own ledger used its own Japanese expense heads | **SOFT** — so the script states the *uncertainty* rather than the attribution, on screen, at the 70% mark |
| **Ryōan-ji tsukubai** · four characters · the shared 口 radical supplied by the square water hole | 7.2–7.5 | **§4 Taru wo shiru** — Traditional Kyoto + Wikipedia (Tsukubai) + Nara Yamato Spirit Tours | **HARD** on the inscription, the temple and the radical design. The Tokugawa Mitsukuni donor attribution is **SOFT and is not used**; nor is the replica question. |

### Deliberately NOT used (so the audit stage doesn't rediscover them)

- **India's saving rate — I1 (7.0% of GNDI) and I3 (34.2%) — is used nowhere in this
  script.** Not an oversight: §1 and §6 forbid a Japan-vs-India head-to-head, and stating
  India's rate anywhere in a video whose hook is Japan's rate creates the comparison by
  adjacency even if no sentence makes it. The chapter that would have carried it (Ch5) uses
  the channel's own ₹30,000 split instead — honest, actionable, comparable to nothing.
- **"Japan saves 37%, India saves 4–8%"** — the source video's headline (TOP `fQyN80dLDpQ`,
  0:54). §5.1: the 37 is real but misapplied and the "India 4–8%" half has **no identified
  source at all**. The two never appear together in this file.
- **"Kakeibo saves you 20–35% of your income."** §5.2 — asserted by at least seven sites and
  one YouTube short; searched for the underlying study and **there is none**. Same disease
  as the Munger "first 100,000 dollars" line killed on the previous run.
- **Every calorie, intake and longevity figure attached to hara hachi bu** (§5.5) — all
  wellness blogs with no primary, and the Okinawa centenarian data has been contested since
  the 2010s. This is a money video; the principle carries zero numbers.
- **Trading Economics quarterly prints** (0.4% Q3 2025, 3.9% Q4 2025) — §5.4. Real, but
  Japan's quarterly rate swings on the bonus cycle. Annual only, on screen.
- **J9 (¥2,386tn at end-March 2026, stocks +28.6%) and New NISA.** Both **SOFT** — the BOJ
  primary for that quarter was not read and the FSA page was not fetched. Nothing in the
  argument needs them, so no SOFT row is spent for texture.
- **I6 / I7 — "mutual funds ~13% of FY25 flows", "₹45.2 into MFs per ₹100 of deposits".**
  Both **SOFT**, RBI primary not read. The Chapter 3 beat they would have decorated lands
  behaviourally instead, with no Indian figure at all.
- **Any ¥→₹ conversion, any dollar glyph, any US institution, any US example.** §6. The dollar
  sign appears nowhere in this file. The US appears exactly once, as two percentages in the
  BOJ table that states them itself.
- **A named fund, index fund, AMC, bank, app or platform.** Persona rule. PPF and the
  monthly minimum appear as **price evidence only**, and the 5.10 and 6.14 feet say so.
- **The handwriting-beats-typing science** TOP asserts at ~11:00. No source was staged, so
  6.12 keeps the paper ritual as a practice and claims nothing about memory.
- **"Advertising spends billions."** TOP's line at ~13:30. No spend figure is staged, so 7.9
  makes the same point as an observation about the market, carrying no number.

---

## Build handoff

1. **`assets/voice/hindi-lines.json` = 92 entries keyed `1.1 … 8.8`**, containing **only**
   the `>` VO strings above — no markdown, no cue text, no on-screen text. Devanagari,
   verbatim. **Slice the source file; never retype.** Gate the extraction with a
   byte-for-byte reconstruction check against this file before generating audio
   (`long_form_scripting.md` §1.7, the firaun re-lining rule).
2. **TTS** via `tools/tts/elevenlabs_tts.py`, voice `HTUuC7OeeEt6OL5fViVe` (Harsh),
   `eleven_multilingual_v2`, style 0. **92 clips.** `run.json budget.max_elevenlabs_calls`
   is **30**, so this cut cannot be generated in one burst — batch it and record the count,
   or the `-en` cut has no headroom left.
3. **Timing is by construction.** One line = one clip = one scene. LONG charges
   `lead_in_seconds 0.25` + `tail_seconds 0.55` per line (`format.json tiers.long`) — **not**
   the `scene.*` 0.4/1.0 defaults, which are tuned for SHORT's nine lines and would spend
   128s of this video on padding. Never hand-edit a duration; regenerate all four homes of
   the timing numbers from one source.
4. **Recount the characters programmatically** and re-check the total against
   `(660 − 92 × 0.8) × 13.03 = 7,640` before locking. The tables above are a budget estimate
   at ±5%. **No line may exceed 105 characters** — that is the `max_scene_seconds` 9.0
   boundary at this rate, and two lines already sit at 103 (5.6, 6.13). The audit's longest
   rewrite, 1.2, lands at ~94.
5. **Images: one per line, 92 scenes, zero photo-free frames** (`photo_free_scene_ratio` = 0,
   creator rule 2026-07-28). Three pairs are holds — **1.1→1.2, 6.7→6.8, 7.4→7.5** — and each
   must run **ONE continuous zoom across both scenes**, never a self-dissolve (creator rule,
   firaun 2026-07-23); give the second scene a tighter crop of the same source so no single
   framing holds past 9.0s. **Localisation rule (study conclusion 4):** Japan owns the story
   frames (Okinawa, Ryōan-ji, the archival Tokyo street, the FIES tables); **every frame
   where the viewer is asked to act is Indian** — 4.5, 4.6, 4.7, 5.4, 5.5, 5.9, 5.10, 7.6,
   8.2, 8.5, 8.6, 8.8. md5 the asset ledger: no image may repeat across videos or channels.
6. **6.7 is a photograph, not an overlay.** The four categories ship as a real top-down
   flat-lay on wood — actual ₹ coins and notes in four groups with four handwritten bilingual
   labels **inside the frame**. This is TOP's single text moment in seventeen minutes and the
   most stealable thing in the packet. Do not rebuild it as a card.
7. **⚠ THE FONT SUBSET WILL EAT JAPANESE AND FOUR PUNCTUATION MARKS.**
   `tools/scaffold/assets/fonts/NotoSansFinance-var.woff2` carries **97 codepoints**
   (03-design.md §1.4): **no CJK at all**, and `>` `→` `▶` `×` `≈` `~` `¥` are absent.
   Already obeyed by every cue above:
   - **On-screen Japanese is romaji only** — `MOTTAINAI`, `HARA HACHI BU`, `KAKEIBO`,
     `TARU WO SHIRU`, `RYOAN-JI`. Any kanji must live **in the photograph** (the tsukubai at
     7.3/7.4), never as composition text.
   - Yen figures are written `JPY 197,432`, never with the ¥ glyph.
   - `ABOUT 1%` and `30 TIMES` replace `~1%` and `30×`. `·` (present) is the separator.
   - Verify every on-screen string against a dumped `subset.txt` before render — this is the
     defect that shipped live in `good-debt/hi`'s 76px hero line.
8. **ledger-rail specifics.** Rail 300px, scene id 96px **weight 200**, chapter label 26px
   tracked 4px, `--muted` hairline between. Photo panel x=1180→1920 with one
   `linear-gradient(90deg, #0d1017, transparent 30%)` left edge. **Delete the four-layer
   scrim and every `text-shadow`** — type is on flat `--bg`, which is the point of this
   architecture. Seven scenes are `RAIL OFF` (1.1, 2.7, 3.12, 4.10, 6.7, 7.4, 8.6); nothing
   else may use it.
9. **Anchor cues to word-level timings** (faster-whisper), not character-offset
   interpolation — the drift is worst on Hindi. `first_cue_by_seconds` 0.5,
   `cue_min_gap_seconds` 0.8, `max_simultaneous_elements` 6.
10. **Chapter-wise production.** Build, proof and re-render chapter by chapter; concat and
    final-render only after all eight chapters are locked. Encode with an explicit
    `-o renders/FINAL-1080p-hi.mp4`.
11. **Burn subtitles into every frame** (study conclusion 6 — the clearest binary in the
    packet: TOP does it on 209/209 sampled frames, the LOW on 0 and died at 2,131 views).
12. **Never name the tool** in the title, description or on screen (study conclusion 7 — two
    independent confirmations across two studies).
