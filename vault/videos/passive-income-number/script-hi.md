---
summary: Hindi/India script for «The passive-income number». MEDIUM tier, per-line chapter architecture — 78 single-sentence VO lines across 7 chapters, ~5,876 chars ≈ 8:33 vs the 510s target. INR only. Standard Hindi (Harsh). On-screen text English/Hinglish, blockframe-9 + the chapter archetype layer. Hero: ₹1 crore at a 3.0% withdrawal rate = ₹25,000/month, set beside the PLFS regular-salaried average ₹24,217. Every corpus figure speaks its withdrawal rate in the same VO breath. Every number traces to videos/passive-income-number/facts-staging.md.
updated: 2026-08-07
source: run.json creator brief + constraints block (2026-08-07) + facts-staging.md attempt 1 (fin-facts) + study note knowledge/video-studies/passive-income-number.md. Architecture blockframe-9 per run.json architecture_lock; MEDIUM tier → per-line chapters (tools/format.json tiers.medium) on the chapter archetype layer (knowledge/design-chapter-archetypes.md).
stage: fin-script, cut hi, attempt 1
---

# «वो नंबर, जो हर महीने पैसे देता है» — Hindi / India edition (MEDIUM, per-line chapters)

**Studio project (to build):** `studio/videos/passive-income-number-hi`
**Language:** Standard Hindi, **Devanagari** — channel voice locked 2026-07-28
([[../../knowledge/niches/india-finance-market]]). ⚠ The launch message for this stage
named the Haryanvi style guide; that guide was retired for finance by the same
2026-07-28 creator decision and was **not** read. See the log for the conflict record.
**Voice:** ElevenLabs **Harsh** `HTUuC7OeeEt6OL5fViVe`, `eleven_multilingual_v2`, style 0.
**On-screen text:** English / Hinglish. **Title + description:** Roman script.
**Architecture:** `blockframe-9` (`format.json architecture_lock`) as the visual system,
**MEDIUM tier → per-line chapters**, laid out on the four chapter archetypes
(A plate · B figure · C ledger · D band). None of the 9-segment blockframe constants
apply; `lines: 9` on the registry entry is a SHORT-tier constant.
**One line = one TTS clip = one scene = one exact timeline anchor.**

**Engine rule:** digits are **spelled out** in every VO line below (bare Latin digits are
a coin-flip English reading in ElevenLabs). On-screen numerals carry the exact figures,
`Intl.NumberFormat("en-IN")` grouping (`₹1,00,00,000`).

**Persona rules (YouTube 2026 AI carve-out):** no host persona, no first-person
expertise, no fund / AMC / bank / app / scheme pick. **मैं** and **हम** appear nowhere in
the VO. The post-office monthly-income scheme and the small-savings rate appear **only as
published price evidence** — "this is what the published rate is" — never as "put your
money here". Second person throughout.

---

> ### ⚠ THE SIX THINGS THAT MUST NOT ENTER THIS CUT
> Every one is named in `run.json.constraints` or in `facts-staging.md` PART F, and the
> study note records both format twins failing on the first two.
> 1. **NEVER a corpus figure without its withdrawal rate in the SAME VO breath.** Not
>    "stated once at the start" — *every rung, every time*. Dark Ledger states four
>    percent once and then ships six bare numbers; that is the observed failure this cut
>    exists to not repeat. Every frame carrying a corpus also carries the rate.
> 2. **NEVER convert a corpus into an age.** No "free at fifty", no "quit in N years", no
>    age anywhere in this cut at all. Line 6.11 says out loud that this is a sum about
>    money and a rate, not about an age.
> 3. **NEVER a return spoken as an expectation.** Three percent is a *chosen* number
>    (2.6, 2.7); the growth rates in 6.15–6.16 are "मानी हुई बढ़त" and land with the words
>    "हिसाब हैं, वादे नहीं".
> 4. **NEVER the banned word.** The English payout word, its Devanagari transliteration
>    and any inline English use are all forbidden in script, on-screen text, title and
>    tags (`run.json.constraints.hi_currency_framing`). **The live trap:** the index's
>    total-return figure is *defined* using that word, so this cut **never explains the
>    index measure at all** — 6.16 quotes only the shape, "क़रीब बारह परसेंट".
> 5. **NEVER the rupee's counterpart glyph, a foreign institution, or a cross-market
>    conversion.** PART C of `facts-staging.md` is the other cut's block and contributes
>    nothing here. ₹1 crore is not any foreign figure and no line, frame or chart may
>    imply it.
> 6. **NEVER four percent as advice.** It appears only as *the imported rule this video
>    corrects*, always beside India's three percent, always with its provenance (5.12–5.15).

---

## Title options (Roman script — per the title-language rule)

1. **Har Mahine ₹25,000 Ke Liye Kitna Paisa Chahiye — Poora Hisaab**
   *(recommended — the monthly figure is the searchable promise, and it is the one number
   the video actually pays off)*
2. ₹1 Crore Se Har Mahine Kitna Milega? 3% Ka Seedha Hisaab
3. Passive Income Ka Asli Number — Aur Wo 4% Wala Rule Jo India Ke Liye Nahi Hai

⚠ Packaging carries the abstraction, the script carries the bills (study conclusion 6 —
both twins do exactly this). `passive income` and `financial freedom` belong in the
title/description/tags; the VO says "बिजली का बिल" and "राशन".

---

## Chapters (ship these as YouTube chapters — study conclusion 10)

| # | Chapter | starts | lines | chars |
|---|---|---|---|---|
| 1 | Wo subah | 0:00 | 7 | 416 |
| 2 | Pehli seedhi — ₹10 lakh | 0:37 | 12 | 919 |
| 3 | Doosri seedhi — ₹20 lakh | 1:58 | 9 | 647 |
| 4 | Teesri seedhi — ₹40 lakh | 2:55 | 9 | 679 |
| 5 | **12% ka jaal, aur 3% vs 4%** (the ~50% correction beat) | 3:54 | 17 | 1,300 |
| 6 | **Chauthi aur paanchvi seedhi — ₹1 crore** (the hero) | 5:47 | 16 | 1,278 |
| 7 | Wapas usi subah par | 7:38 | 8 | 637 |

---

## Timing budget

Hindi narration = **13.03 chars/s** (`format.json cuts.hi.chars_per_second` — the measured
**FLAT delivered rate, pause silence included**). MEDIUM charges **0.25 s lead-in + 0.55 s
tail per line** (`tiers.medium`) = **0.8 × 78 = 62.4 s** of inter-line padding.

**Budget formula** — padding is not audio, so it comes out of the target *before* the rate
is applied (`format.json cuts.en._chars_per_second_trap` documents what happens when it
does not; the same correction was applied to the hi cut of `japanese-money-methods`):

`(510 − 62.4) × 13.03 = 5,832 char budget`. This draft is **5,876 (+0.8%)** after the
three `fin-audit` VO rewrites (5.9 +24, 5.14 +7, 7.6 −6).

⚠ **This is deliberately not the 6,645 in the launch brief.** 510 × 13.03 = 6,645 is the
*uncorrected* formula; at 78 lines it would produce 6,645 ÷ 13.03 + 62.4 = **572 s**, i.e.
**12% long** against a 510 s target. The corrected formula is used here and is flagged in
the log.

| Ch | lines | chars | VO | + padding | runtime | starts |
|---|---|---|---|---|---|---|
| 1 | 7 | 416 | 31.9s | 5.6 | 37.5s | 0:00 |
| 2 | 12 | 919 | 70.5s | 9.6 | 80.1s | 0:37 |
| 3 | 9 | 647 | 49.7s | 7.2 | 56.9s | 1:58 |
| 4 | 9 | 679 | 52.1s | 7.2 | 59.3s | 2:55 |
| 5 | 17 | 1,300 | 99.8s | 13.6 | 113.4s | 3:54 |
| 6 | 16 | 1,278 | 98.1s | 12.8 | 110.9s | 5:47 |
| 7 | 8 | 637 | 48.9s | 6.4 | 55.3s | 7:38 |
| | **78** | **5,876** | **451.0s** | **62.4s** | **513.4s** | |

**Estimated runtime 513.4 s (8:33) vs the 510 s target — +0.7%.** Char counts are a budget
estimate (±5%); the build step recounts them programmatically from the extracted lines
file, then ffprobe-measures every clip.

**Pace:** 513.4 / 78 = **6.58 s average scene** (`target_scene_seconds` 6.5,
`max_scene_seconds` 9.0). The longest line is now **5.14 at 103 chars** → 7.90 s VO + 0.8 =
**8.70 s**, still under the photo-hold ceiling but with only 0.30 s of margin — do not
lengthen 5.14 at build time. Shortest is 1.3 at 27 chars → 2.07 s, well over
`tts.min_clip_seconds` 1.0. **No line may exceed 105 characters** — that is where a scene
breaches the hold check.

**Line count:** 78 exactly, per `format.json tiers.medium.lines` and the launch brief.
78 hi + 78 en = **156 ElevenLabs calls of the run's 188** (`run.json.budget`), leaving 32
for retries.

### Where the retention beats land

- **The withheld number is named at 1.4 ≈ 0:14.5** — inside the standing 15-second promise
  gate. Both twins are outside it (A announces at ≈0:22, B names at ≈0:45); study
  conclusion 2 is explicit that **the gate still wins**. B's *form* is copied, not its
  timing: 1.4–1.5 name a number and refuse to say it, which commits to nothing.
- **Rung 1 lands at 2.9 ≈ 1:30 (17.5%)** — inside the brief's 8–25% band.
- **The mid-video drop zone (55–65% = 4:41–5:32)** opens on the post-office ceiling
  evidence (5.7–5.11) and runs straight into the provenance correction — new sourced
  material, not a transition.
- **The too-good-to-be-true rate trap punches at 5.6 ≈ 4:24 (51.6%)**, and the four-percent
  provenance opens at 5.12 ≈ **5:04**. Both twins put their yield-trap warning within about
  half a minute of the 5:00 mark on two different runtimes; ours sits in the same window.
- **The hero lands at 6.7 ≈ 6:20 (74.3%)** and is validated by the one sourced external
  statistic at 6.9 ≈ 6:33 — B's move exactly (one citation, near the climax, to give the
  viewer permission to believe the payoff).
- **The callback opens at 7.1 ≈ 7:36 (89.1%)**, and the **single terminal CTA** is 7.8 at
  ≈8:26 (98.9%). **Zero mid-roll CTAs** — third independent confirmation of that line.

---

## Per-scene timing budget

`arch` = chapter archetype (`format.json chapter_design.archetypes`):
**A** plate (chapter opens, hand-offs) · **B** figure (the point is a number) ·
**C** ledger (the point is evidence — a bill, a rate card, a paper) ·
**D** band (the point is the motion — money moving, a corpus draining).

| # | chars | est s | arch | | # | chars | est s | arch |
|---|---|---|---|---|---|---|---|---|
| 1.1 | 42 | 3.2 | A | | 5.1 | 55 | 4.2 | A |
| 1.2 | 63 | 4.8 | A | | 5.2 | 84 | 6.4 | B |
| 1.3 | 27 | 2.1 | D | | 5.3 | 76 | 5.8 | A |
| 1.4 | 55 | 4.2 | A | | 5.4 | 64 | 4.9 | D |
| 1.5 | 71 | 5.4 | D | | 5.5 | 66 | 5.1 | D |
| 1.6 | 76 | 5.8 | A | | 5.6 | 55 | 4.2 | B |
| 1.7 | 82 | 6.3 | B | | 5.7 | 84 | 6.4 | C |
| 2.1 | 62 | 4.8 | A | | 5.8 | 80 | 6.1 | B |
| 2.2 | 70 | 5.4 | C | | 5.9 | 82 | 6.3 | C |
| 2.3 | 82 | 6.3 | D | | 5.10 | 88 | 6.8 | B |
| 2.4 | 95 | 7.3 | D | | 5.11 | 85 | 6.5 | A |
| 2.5 | 51 | 3.9 | A | | 5.12 | 65 | 5.0 | B |
| 2.6 | 74 | 5.7 | B | | 5.13 | 73 | 5.6 | C |
| 2.7 | 88 | 6.8 | B | | 5.14 | 103 | 7.9 | C |
| 2.8 | 72 | 5.5 | B | | 5.15 | 80 | 6.1 | C |
| 2.9 | 78 | 6.0 | B | | 5.16 | 84 | 6.4 | B |
| 2.10 | 66 | 5.1 | C | | 5.17 | 76 | 5.8 | B |
| 2.11 | 89 | 6.8 | C | | 6.1 | 60 | 4.6 | A |
| 2.12 | 92 | 7.1 | A | | 6.2 | 88 | 6.8 | B |
| 3.1 | 71 | 5.4 | A | | 6.3 | 72 | 5.5 | C |
| 3.2 | 80 | 6.1 | B | | 6.4 | 62 | 4.8 | D |
| 3.3 | 68 | 5.2 | C | | 6.5 | 52 | 4.0 | A |
| 3.4 | 68 | 5.2 | A | | 6.6 | 58 | 4.5 | B |
| 3.5 | 42 | 3.2 | B | | 6.7 | 82 | 6.3 | B |
| 3.6 | 96 | 7.4 | B | | 6.8 | 60 | 4.6 | A |
| 3.7 | 76 | 5.8 | D | | 6.9 | 92 | 7.1 | C |
| 3.8 | 80 | 6.1 | C | | 6.10 | 78 | 6.0 | B |
| 3.9 | 66 | 5.1 | A | | 6.11 | 96 | 7.4 | B |
| 4.1 | 62 | 4.8 | A | | 6.12 | 96 | 7.4 | B |
| 4.2 | 89 | 6.8 | B | | 6.13 | 100 | 7.7 | B |
| 4.3 | 45 | 3.5 | C | | 6.14 | 96 | 7.4 | A |
| 4.4 | 77 | 5.9 | C | | 6.15 | 88 | 6.8 | B |
| 4.5 | 86 | 6.6 | A | | 6.16 | 98 | 7.5 | B |
| 4.6 | 90 | 6.9 | D | | 7.1 | 68 | 5.2 | A |
| 4.7 | 88 | 6.8 | D | | 7.2 | 55 | 4.2 | D |
| 4.8 | 68 | 5.2 | C | | 7.3 | 78 | 6.0 | B |
| 4.9 | 74 | 5.7 | B | | 7.4 | 92 | 7.1 | A |
| | | | | | 7.5 | 96 | 7.4 | D |
| | | | | | 7.6 | 94 | 7.2 | B |
| | | | | | 7.7 | 88 | 6.8 | A |
| | | | | | 7.8 | 66 | 5.1 | A |

**Archetype sequence check** (rhythm, not variety for its own sake):
ch1 `A A D A D A B` · ch2 `A C D D A B B B B C C A` · ch3 `A B C A B B D C A` ·
ch4 `A B C C A D D C B` · ch5 `A B A D D B C B C B A B C C C B B` ·
ch6 `A B C D A B B A C B B B B A B B` · ch7 `A D B A D B A A`.
Ch5 holds **C** across 5.13–5.15 deliberately: three documents are one argument (the
American paper, what it excluded, the Indian paper), and varying the layout there would
break the only through-line the chapter has.

### Role colour semantics (one role colour per scene, ever)

⚠ Corrected by `fin-audit` (hi, attempt 1): the lists below now match the per-scene
`colour:` cues exactly. The previous version filed 4.7 under `--warn` and 5.16 under
`--target` when both cues say the opposite, and omitted six scenes entirely. **The cue is
authoritative; this table is the index.** A storyboard that colours from the old table
would have painted the "why the rate is small" beat as a danger and the "above 3.75% it
breaks" beat as merely under examination — i.e. inverted on the two scenes that carry the
thesis.

- `--fund` green (`#22c55e`) = **the corpus doing its stated job at the stated rate** — the
  rungs that land: **2.9, 2.11, 3.2, 4.2, 6.2, 6.4, 6.7, 6.10, 7.6**.
- `--warn` red (`#ef4444`) = **the thing that eats the corpus** — the too-high withdrawal
  rate (5.2, 5.4, 5.5, 5.6), the imported rule and what it excluded (5.12, 5.14, 6.12,
  6.13), the failure edge (5.16), the honesty beat (4.6), the internet's inflation of it
  (3.8).
- `--target` amber (`#f59e0b`) = **a rate under examination** — **2.6, 2.7, 3.5, 4.7, 4.9,
  5.8, 5.10, 5.15, 5.17, 6.6, 6.15, 6.16**.
- `--pop` orange (`#ff5c39`) = the CTA block, **once**, at 7.8.

**Thesis check:** green never lands on a figure that lacks its rate, red never lands on
India's 3.0%, and amber never lands on the imported 4%. The table argues *with* the
script's thesis at every scene.

---

# THE SCRIPT

> **VO block rule.** Every `>` quoted line below is a VO line, verbatim, and is the only
> thing that goes to TTS. Everything in backticks is a production cue and is never spoken.
> **Slice these strings — never retype them.** Retyping Devanagari silently swaps
> characters (nukta, chandrabindu) and the swap is inaudible until the render.
>
> **The rate rule, mechanically:** every frame whose `num:` or `stmt:` carries a corpus
> also carries its withdrawal rate in that same frame, and the VO line speaks the rate in
> the same sentence. If a build ever produces a corpus frame without a visible rate, that
> frame is wrong, not the script.

---

## Chapter 1 — वो सुबह (COLD OPEN · the won morning, second person)

*Study conclusion 1: two unrelated operators, near-verbatim, both breakouts — wake → no
alarm → coffee → window → phone → money that arrived while you slept. Six beats, same
order. No greeting, no title card, no roadmap before the number is named. The number is
NAMED and WITHHELD (B's form), not announced (A's) — an open loop commits to nothing,
which is the only kind of promise `no_return_promise` allows.*

**1.1**
> एक मंगलवार की सुबह। अलार्म नहीं बजा।

`[arch A | img: an unlit bedside alarm clock on a wooden table, first light through a curtain | bar: A TUESDAY | stmt: The alarm did not go off]`

**1.2**
> चाय बनती है, आप खिड़की के पास बैठते हैं, और फ़ोन एक बार बजता है।

`[arch A | img: a steel glass of chai steaming on a windowsill, morning street out of focus behind | bar: THE MORNING | stmt: Tea. The window. One buzz.]`

**1.3**
> पैसा आ गया, सोते हुए।

`[arch D | img: a phone face-down on a table, screen glow on the wood — money notification NOT legible | bar: — | stmt: Money arrived. While you slept.]`

**1.4**
> आप अमीर नहीं हुए — आप बस एक ख़ास नंबर तक पहुँच गए।

`[arch A | img: a single closed brown envelope squared on a bare table | bar: NOT RICH | stmt: You just reached a number | foot: The number is withheld until Chapter 6 — this is the open loop]`

**1.5**
> वो नंबर आपका बिजली का बिल, आपका राशन और आपका किराया चुपचाप भरता रहता है।

`[arch D | img: three household bills fanned on a table — electricity, a grocery slip, a rent receipt | bar: WHAT IT PAYS | stmt: Electricity. Ration. Rent.]`

**1.6**
> इस वीडियो में वो नंबर सीढ़ी दर सीढ़ी निकलेगा — सबसे छोटी सीढ़ी से शुरू करके।

`[arch A | img: a narrow flight of stone steps rising out of frame, empty | bar: RUNG BY RUNG | stmt: Smallest rung first]`

**1.7**
> और हर सीढ़ी पर वो शर्त भी साथ रहेगी, जिसके बिना कोई भी नंबर सिर्फ़ एक वादा है।

`[arch B | img: a brass balance scale, one pan holding a folded paper slip | bar: THE CONDITION | stmt: Every figure ships with its rate | foot: A corpus without its withdrawal rate is a promise, not arithmetic]`

---

## Chapter 2 — पहली सीढ़ी: दस लाख

*The mechanism in the smallest unit, then rung 1. The assumption sentence (2.6–2.7) is A's
best sentence, restated without a host persona: the rate is a declared CHOICE, not a rate
the market owes you. Study conclusion 7.*

**2.1**
> सबसे पहले यह समझिए कि जमा पैसा हर महीने कुछ देता कैसे है।

`[arch A | img: a locked steel almirah with a small key in the lock | bar: FIRST, THE MECHANISM | stmt: How saved money pays a monthly amount]`

**2.2**
> इसका एक सीधा नाम है — एस डब्ल्यू पी, यानी सिस्टेमैटिक विदड्रॉअल प्लान।

`[arch C | img: a printed mutual-fund transaction form on a desk, macro, no logo legible | bar: THE NAME | stmt: SWP — Systematic Withdrawal Plan | foot: Terminology as four Indian fund houses define it — not a product recommendation]`

**2.3**
> एक तय रक़म, हर महीने एक तय तारीख़ पर, आपके अपने जमा पैसे में से निकल आती है।

`[arch D | img: a date circled in ballpoint on a wall calendar | bar: WHAT IT DOES | stmt: A fixed amount, a fixed date, out of your own corpus]`

**2.4**
> एस आई पी में पैसा हर महीने अंदर जाता है; एस डब्ल्यू पी में वही पैसा हर महीने बाहर आता है।

`[arch D | img: a hand posting a note into a slotted steel box, and the same box with a note being drawn out (hands only, no face) | bar: IN vs OUT | stmt: SIP puts in. SWP takes out.]`

**2.5**
> अब असली सवाल — हर साल कितना निकालना सुरक्षित है?

`[arch A | img: an empty water tap over a half-full steel bucket | bar: THE REAL QUESTION | stmt: How much a year is safe to take out?]`

**2.6**
> इस पूरे वीडियो में एक ही मान लिया गया नंबर चलेगा — तीन परसेंट सालाना।

`[arch B | img: a single figure written in pencil on ruled paper, underlined twice | bar: THE WORKING NUMBER | num: 3.0% | foot: Withdrawal rate — the assumption every figure in this video is divided by | colour: --target]`

**2.7**
> तीन परसेंट कोई वादा नहीं है; यह एक चुना हुआ, सावधान नंबर है, और आगे इसकी वजह भी आएगी।

`[arch B | hold 2.6's image, ONE continuous zoom across both scenes | bar: A CHOICE, NOT A FORECAST | stmt: 3.0% is chosen. The reason is in Chapter 5. | colour: --target]`

**2.8**
> तो पहली सीढ़ी — दस लाख रुपये, तीन परसेंट सालाना निकालने के हिसाब से।

`[arch B | img: a small steel cash box, lid open, notes squared inside | bar: RUNG ONE | num: ₹10,00,000 | stmt: at a 3.0% withdrawal rate | foot: ILLUSTRATIVE · corpus × 3.0% ÷ 12 — arithmetic, not a forecast]`

**2.9**
> दस लाख का तीन परसेंट यानी साल का तीस हज़ार, यानी महीने के ढाई हज़ार रुपये।

`[arch B | img: a hand-written division worked out on a ledger page (hand not in frame) | bar: THE SUM | stmt: ₹10,00,000 × 3.0% = ₹30,000/yr = ₹2,500/month | foot: ILLUSTRATIVE · withdrawal rate 3.0% · not a return promise | colour: --fund]`

**2.10**
> ढाई हज़ार में क्या आता है? आपका मोबाइल रिचार्ज और घर का इंटरनेट।

`[arch C | img: a broadband bill and a recharge receipt overlapping on a table | bar: WHAT ₹2,500 BUYS | stmt: The phone recharge and the home internet]`

**2.11**
> पूरे साल का रिचार्ज, पूरे साल का इंटरनेट — और आपकी तनख़्वाह में से एक रुपया नहीं गया।

`[arch C | img: twelve identical bill stubs pinned in a row on a board | bar: ALL TWELVE MONTHS | stmt: Not one rupee out of the salary | colour: --fund]`

**2.12**
> यह छोटा लगता है, और है भी छोटा — पर यह बिल अब आपकी कमाई नहीं, आपका जमा पैसा भर रहा है।

`[arch A | img: a single brick set down at the foot of a stone staircase | bar: THE FIRST BRICK | stmt: The bill is now paid by the corpus, not the income]`

---

## Chapter 3 — दूसरी सीढ़ी: बीस लाख

*Rung 2. The rate is re-spoken with the corpus at 3.1, 3.2, 3.5 and 3.6 — four times in
nine lines. This is the beat where Dark Ledger stops re-stating it and starts shipping
bare numbers; repetition FEELS redundant here and is not.*

**3.1**
> अब दूसरी सीढ़ी — बीस लाख रुपये, उसी तीन परसेंट सालाना के हिसाब से।

`[arch A | img: two steel cash boxes side by side, the second visibly deeper | bar: RUNG TWO | num: ₹20,00,000 | stmt: at a 3.0% withdrawal rate]`

**3.2**
> बीस लाख का तीन परसेंट यानी साल का साठ हज़ार, यानी महीने के पाँच हज़ार रुपये।

`[arch B | img: the same ledger page, a second division worked below the first | bar: THE SUM | stmt: ₹20,00,000 × 3.0% = ₹60,000/yr = ₹5,000/month | foot: ILLUSTRATIVE · withdrawal rate 3.0% | colour: --fund]`

**3.3**
> पाँच हज़ार महीना — गर्मियों वाला बिजली का बिल, वो भी पूरे साल का।

`[arch C | img: an Indian electricity bill on a table under a ceiling fan's shadow | bar: WHAT ₹5,000 BUYS | stmt: The summer electricity bill — all year]`

**3.4**
> मई में जो बिल देखकर घर में बहस होती है, वो बहस बंद हो जाती है।

`[arch A | img: an old wall-mounted electricity meter, dial mid-spin | bar: THE MAY ARGUMENT | stmt: The one that ends]`

**3.5**
> ध्यान दीजिए — दर वही रही, तीन परसेंट।

`[arch B | img: a rubber stamp resting on an ink pad | bar: THE RATE HELD | num: 3.0% | colour: --target]`

**3.6**
> उसी तीन परसेंट पर जमा रक़म दस लाख से बीस लाख हुई, और महीने का पैसा ढाई हज़ार से पाँच हज़ार।

`[arch B | img: two brass weights of clearly different mass on a shop balance | bar: ONLY THE CORPUS MOVED | stmt: ₹10,00,000 → ₹20,00,000 · ₹2,500 → ₹5,000/month, both at 3.0% | foot: ILLUSTRATIVE · the rate is identical on both sides]`

**3.7**
> यह कोई जादू नहीं है, यह एक भाग है — साल का हिस्सा, बारह से बाँटा हुआ।

`[arch D | img: a round steel plate of grain being divided into twelve small heaps | bar: NOT MAGIC | stmt: One division, split twelve ways]`

**3.8**
> और इसी सीधी बात को इंटरनेट पर अक्सर बहुत बड़ा और बहुत जल्दी बना दिया जाता है।

`[arch C | img: a stack of glossy printed flyers with large numerals, edges curling | bar: WHAT THE INTERNET DOES | stmt: Makes it bigger and faster than it is | colour: --warn]`

**3.9**
> असल में यह धीमा है, और धीमा होना ही इसकी सबसे भरोसेमंद बात है।

`[arch A | img: a bullock cart wheel at rest on a dirt road, long shadow | bar: IT IS SLOW | stmt: Slow is the trustworthy part]`

---

## Chapter 4 — तीसरी सीढ़ी: चालीस लाख

*Rung 3, then the honesty beat the format twins both skip: the money comes out of your own
capital, which is exactly WHY the rate is kept small. Dark Ledger says the opposite
("you do not touch the principal") and that is an implied capital-preservation promise the
arithmetic does not make.*

**4.1**
> तीसरी सीढ़ी — चालीस लाख रुपये, फिर वही तीन परसेंट सालाना।

`[arch A | img: a large steel trunk with the lid propped open, cloth-wrapped bundles inside | bar: RUNG THREE | num: ₹40,00,000 | stmt: at a 3.0% withdrawal rate]`

**4.2**
> चालीस लाख का तीन परसेंट यानी साल का एक लाख बीस हज़ार, यानी महीने के दस हज़ार रुपये।

`[arch B | img: the ledger page again, a third division worked below the other two | bar: THE SUM | stmt: ₹40,00,000 × 3.0% = ₹1,20,000/yr = ₹10,000/month | foot: ILLUSTRATIVE · withdrawal rate 3.0% | colour: --fund]`

**4.3**
> दस हज़ार महीना — यानी घर का पूरा राशन।

`[arch C | img: a kirana shop counter with a handwritten monthly ration list on the glass | bar: WHAT ₹10,000 BUYS | stmt: The month's ration]`

**4.4**
> आटा, दाल, चावल, तेल, दूध, सब्ज़ी — हर महीने, बिना आपकी तनख़्वाह को छुए।

`[arch C | img: open sacks of atta, dal and rice in a row, a tin of oil beside them | bar: THE WHOLE LIST | stmt: Without touching the salary]`

**4.5**
> यहाँ एक बात साफ़ कहनी ज़रूरी है, क्योंकि यही वो जगह है जहाँ ज़्यादातर लोग बहक जाते हैं।

`[arch A | img: a road sign post with one arm snapped off, plain sky behind | bar: SAY IT PLAINLY | stmt: This is where most people get it wrong]`

**4.6**
> एस डब्ल्यू पी का पैसा आसमान से नहीं आता — वो आपकी अपनी जमा रक़म में से ही निकलता है।

`[arch D | img: a water tank with the outlet pipe running, level visibly below the fill line | bar: WHERE IT COMES FROM | stmt: Out of your own corpus — capital and growth both | colour: --warn]`

**4.7**
> इसीलिए निकालने की दर छोटी रखी जाती है, ताकि बची हुई रक़म फिर से बढ़ने का वक़्त पा सके।

`[arch D | img: a narrow tap opened only a quarter turn, a thin steady stream | bar: WHY THE RATE IS SMALL | stmt: So what is left has time to grow back | colour: --target]`

**4.8**
> और यह भी याद रखिए कि इस तरह निकाले गए पैसे पर टैक्स भी लगता है।

`[arch C | img: a tax challan form face-up on a desk, pen across it | bar: AND TAX | stmt: Withdrawals are taxable | foot: Rate deliberately not stated — no statute page was read this run]`

**4.9**
> अब तक तीन सीढ़ियाँ हो चुकीं, और तीनों पर एक ही दर चली — तीन परसेंट।

`[arch B | img: three stone steps rising, each edge worn | bar: THREE RUNGS, ONE RATE | stmt: ₹10,00,000 · ₹20,00,000 · ₹40,00,000 — all at 3.0% | colour: --target]`

---

## Chapter 5 — बारह परसेंट का जाल, और तीन बनाम चार (THE ~50% CORRECTION BEAT)

*Both twins put a "too good to be true" warning within about half a minute of the 5:00
mark, on two different runtimes. In a rupee SWP frame the identical trap is a too-HIGH
withdrawal rate, which is structurally better: it forces the rate onto the screen and
converts a compliance constraint into the video's most dramatic moment. Then the beat this
whole run exists for — four percent is an imported American number and India's own
published research says three.*

**5.1**
> अब वो सवाल, जो इस पूरे हिसाब को तोड़ भी सकता है।

`[arch A | img: a hairline crack running across a dry clay pot | bar: THE QUESTION THAT BREAKS IT | stmt: — ]`

**5.2**
> अगर तीन परसेंट की जगह दस या बारह परसेंट निकाल लें, तो सीढ़ी छोटी नहीं हो जाएगी?

`[arch B | img: a tap opened wide, water hitting the bucket hard enough to splash out | bar: WHY NOT TAKE MORE? | stmt: 10% or 12% withdrawal instead of 3.0% | foot: A withdrawal rate — the amount you PULL OUT, not a return | colour: --warn]`

**5.3**
> सुनने में यह बहुत अच्छा लगता है, और यही वो जगह है जहाँ रुक जाना चाहिए।

`[arch A | img: a hand-painted "STOP" on a weathered wooden gate | bar: STOP HERE | stmt: It sounds good. That is the tell.]`

**5.4**
> इतनी बड़ी दर से निकाला गया पैसा मूल रक़म को ही खाने लगता है।

`[arch D | img: a sack of grain with a tear at the base, grain running out onto the floor | bar: WHAT IT EATS | stmt: A high withdrawal rate consumes the capital | colour: --warn]`

**5.5**
> और मूल रक़म ख़त्म होते ही महीने वाला पैसा भी ख़त्म हो जाता है।

`[arch D | img: an empty water tank, outlet pipe dry, nothing running | bar: THEN IT STOPS | stmt: Capital gone, monthly income gone | colour: --warn]`

**5.6**
> बारह परसेंट मौक़ा नहीं है — बारह परसेंट चेतावनी है।

`[arch B | img: a red-painted warning triangle bolted to a concrete pole | bar: — | num: 12% | stmt: Not an opportunity. A warning. | colour: --warn]`

**5.7**
> इसका सबसे साफ़ सबूत सरकार की अपनी स्कीम में है — पोस्ट ऑफ़िस की मंथली इनकम स्कीम।

`[arch C | img: a post office counter window with a brass grille, no faces | bar: THE GOVERNMENT'S OWN | stmt: Post Office Monthly Income Scheme]`

**5.8**
> वो सात दशमलव चार परसेंट सालाना देती है, हर महीने, और सरकार की गारंटी के साथ।

`[arch B | img: a printed post-office rate board on a wall, macro | bar: THE PUBLISHED RATE | num: 7.4% p.a. | stmt: paid monthly, sovereign-backed | foot: Q1–Q2 FY27 — published rate as price evidence, not a recommendation | colour: --target]`

**5.9**
> पर उसी सात दशमलव चार परसेंट पर ज़्यादा से ज़्यादा नौ लाख रुपये ही रखे जा सकते हैं।

`[arch C | img: a deposit form with a ceiling figure printed in a boxed field | bar: THE CEILING | stmt: ₹9,00,000 maximum at 7.4%, single account]`

**5.10**
> नौ लाख पर सात दशमलव चार परसेंट यानी महीने के क़रीब पचपन सौ रुपये — यही उसकी छत है।

`[arch B | img: a low concrete ceiling photographed from directly below, one bare bulb | bar: THE ROOF | stmt: ₹9,00,000 at 7.4% ≈ ₹5,550/month | foot: ILLUSTRATIVE · ₹9,00,000 × 7.4% ÷ 12 · single-account ceiling | colour: --target]`

**5.11**
> गारंटी वाली मंथली इनकम की छत यही है, और इसीलिए एस डब्ल्यू पी वाला रास्ता मौजूद है।

`[arch A | img: a doorway cut into a thick wall, a lit passage beyond | bar: WHY THE OTHER ROUTE EXISTS | stmt: That is the ceiling on guaranteed monthly income]`

**5.12**
> अब वो नंबर, जो इंटरनेट पर सबसे ज़्यादा दिखता है — चार परसेंट।

`[arch B | img: a phone-free desk with a printed search-results page, one figure ringed in pen | bar: THE INTERNET'S NUMBER | num: 4% | colour: --warn]`

**5.13**
> चार परसेंट अमेरिका का नंबर है, उन्नीस सौ चौरानवे के एक रिसर्च पेपर से।

`[arch C | img: a bound academic journal open flat on a library table, columns of text, no legible title | bar: WHERE IT CAME FROM | stmt: Bengen, Journal of Financial Planning, October 1994 | foot: Confirmed on three surfaces; the 1994 paper itself was not retrieved]`

**5.14**
> उस नियम की रिसर्च वहाँ के आँकड़ों पर बनी थी, तीस साल के लिए, और उसमें टैक्स और ख़र्चे जोड़े ही नहीं गए।

`[arch C | img: a printed methodology page with two lines struck through in ink | bar: WHAT IT EXCLUDED | stmt: Built on that market's history · 30-year horizon · no tax, no costs | foot: Cooley, Hubbard & Walz, AAII Journal, Feb 1998 — the authors state this themselves | colour: --warn]`

**5.15**
> भारत के अपने आँकड़ों पर हुई रिसर्च कुछ और कहती है — तीन से साढ़े तीन परसेंट।

`[arch C | img: a stapled research paper on an Indian desk beside a cup, top sheet blank of legible text | bar: INDIA'S OWN RESEARCH | stmt: 3.0% – 3.5% | foot: Raju & Saraogi, "Balancing Acts: Safe Withdrawal Rates in the Indian Context", Jan 2024 · independently corroborated by ONE Indian practitioner surface (freefincal, Feb 2026) | colour: --target]`

**5.16**
> और पौने चार परसेंट के ऊपर जाते ही रक़म ख़त्म हो जाने का ख़तरा तेज़ी से बढ़ता है।

`[arch B | img: a stair tread with the nosing broken away, seen edge-on | bar: THE EDGE | num: 3.75% | stmt: Above this, failure risk rises sharply | colour: --warn]`

**5.17**
> वजह भी सीधी है — रिज़र्व बैंक इस साल महँगाई क़रीब पाँच परसेंट मान रहा है।

`[arch B | img: a vegetable-market price slate with figures chalked and re-chalked | bar: WHY INDIA'S IS LOWER | num: ~5% | stmt: RBI's projected inflation for the year | foot: RBI Monetary Policy Committee, 5 Aug 2026 — FY27 CPI projection 5.0% | colour: --target]`

---

## Chapter 6 — चौथी और पाँचवीं सीढ़ी: एक करोड़ (THE HERO)

*The number the video is named for, at 74% of runtime, priced in rent/EMI and then set
beside the one sourced external statistic — B's move exactly (one citation, near the
climax). 6.11 is the guard rail: the sum is about a corpus and a rate, never about an age.*

**6.1**
> अब चौथी सीढ़ी — पचास लाख रुपये, वही तीन परसेंट सालाना।

`[arch A | img: a bank locker door standing open, empty shelf inside | bar: RUNG FOUR | num: ₹50,00,000 | stmt: at a 3.0% withdrawal rate]`

**6.2**
> पचास लाख का तीन परसेंट यानी साल का डेढ़ लाख, यानी महीने के साढ़े बारह हज़ार रुपये।

`[arch B | img: the ledger page, a fourth division worked below the others | bar: THE SUM | stmt: ₹50,00,000 × 3.0% = ₹1,50,000/yr = ₹12,500/month | foot: ILLUSTRATIVE · withdrawal rate 3.0% | colour: --fund]`

**6.3**
> साढ़े बारह हज़ार महीना — कई शहरों में एक कमरे का किराया, या बाइक की क़िस्त।

`[arch C | img: a rent receipt book open on a table, carbon sheet visible | bar: WHAT ₹12,500 BUYS | stmt: A one-room rent, or the two-wheeler EMI]`

**6.4**
> हर महीने जो रक़म सबसे पहले जाती है, वो अब जेब से नहीं जा रही।

`[arch D | img: an empty trouser pocket turned out against a plain wall | bar: THE FIRST OUTGOING | stmt: No longer out of the pocket | colour: --fund]`

**6.5**
> और अब पाँचवीं सीढ़ी, जिसके लिए यह वीडियो बना है।

`[arch A | img: the top landing of the stone staircase, light falling across it | bar: RUNG FIVE | stmt: The one this video is about]`

**6.6**
> एक करोड़ रुपये, तीन परसेंट सालाना निकालने के हिसाब से।

`[arch B | img: a heavy steel safe door, handle centred, closed | bar: THE CORPUS | num: ₹1,00,00,000 | stmt: at a 3.0% withdrawal rate | colour: --target]`

**6.7**
> एक करोड़ का तीन परसेंट यानी साल के तीन लाख, यानी महीने के पच्चीस हज़ार रुपये।

`[arch B | img: the ledger page, the final division worked and underlined | bar: THE NUMBER | num: ₹25,000 / month | stmt: ₹1,00,00,000 × 3.0% = ₹3,00,000/yr | foot: ILLUSTRATIVE · withdrawal rate 3.0% · corpus = annual withdrawal ÷ rate | colour: --fund]`

**6.8**
> अब इस पच्चीस हज़ार को एक सरकारी आँकड़े के बगल में रखिए।

`[arch A | img: two sheets of paper laid edge to edge on a desk | bar: SET IT BESIDE THIS | stmt: — ]`

**6.9**
> नियमित तनख़्वाह पाने वाले भारतीय की औसत महीने की कमाई चौबीस हज़ार दो सौ सत्रह रुपये है।

`[arch C | img: a printed pay slip on thin paper, folded once, figures not legible | bar: THE SOURCED FIGURE | num: ₹24,217 | stmt: Average monthly earnings, regular wage/salaried | foot: PLFS Annual Report 2025 (Jan–Dec 2025), PIB — men ₹24,217, women ₹18,353]`

**6.10**
> यानी एक करोड़, तीन परसेंट पर, औसत तनख़्वाह के बराबर पैसा हर महीने देता है।

`[arch B | img: a two-pan balance sitting level, a coin in each pan | bar: THEY MEET | stmt: ₹25,000 at 3.0% vs ₹24,217 earned | foot: ₹1,00,00,000 at a 3.0% withdrawal rate · PLFS 2025 | colour: --fund]`

**6.11**
> यही वो नंबर है — औसत तनख़्वाह जितना पैसा, और यह उम्र का नहीं, सिर्फ़ रक़म और दर का हिसाब है।

`[arch B | img: a stone milestone marker beside an empty road, no distance legible | bar: WHAT IT IS | stmt: A sum about a corpus and a rate — never about an age | foot: No age, no date and no "years to freedom" is claimed anywhere in this video]`

**6.12**
> और अगर आपने वही उधार लिया हुआ चार परसेंट मान लिया होता, तो निशाना पचहत्तर लाख पर रुक जाता।

`[arch B | img: a target board with the outer ring cut away, hung on a wall | bar: THE IMPORTED RULE | num: ₹75,00,000 | stmt: what 4% would set as the target for the same ₹25,000/month | colour: --warn]`

**6.13**
> पचहत्तर लाख वाला निशाना चार परसेंट पर टिका है — यानी उधार लिया नंबर लक्ष्य एक-चौथाई छोटा कर देता है।

`[arch B | img: a short measuring tape held against a long timber plank | bar: THE COST OF IMPORTING IT | stmt: ₹75,00,000 at 4% vs ₹1,00,00,000 at 3.0% — a quarter smaller | foot: Same ₹25,000/month, two different rates. India's own research says 3.0–3.5%. | colour: --warn]`

**6.14**
> एक करोड़ तक पहुँचने का महीने का ख़र्च क्या बैठता है — और यहाँ दर निकालने की नहीं, बढ़ने की है।

`[arch A | img: a monthly standing-instruction slip on a bank counter | bar: WHAT IT COSTS PER MONTH | stmt: The rates below are ASSUMED GROWTH — not the 3.0% withdrawal rate | foot: Two different objects. Withdrawal rate = what you take out. Growth rate = what the corpus is assumed to earn.]`

**6.15**
> बीस साल में, सात दशमलव एक परसेंट की मानी हुई बढ़त पर, महीने के क़रीब उन्नीस हज़ार।

`[arch B | img: a passbook open at a page of small regular entries | bar: 20 YEARS · ASSUMED 7.1% GROWTH | num: ≈ ₹19,000 / month | foot: ILLUSTRATIVE · monthly compounding · 7.1% is the published PPF / 3-yr post-office rate, Q2 FY27 — used as an assumption, not a forecast | colour: --target]`

**6.16**
> और क़रीब बारह परसेंट की मानी हुई बढ़त पर, महीने के क़रीब दस हज़ार — दोनों हिसाब हैं, वादे नहीं।

`[arch B | img: a printed newspaper market page folded on a table, no headline legible | bar: 20 YEARS · ASSUMED ~12% GROWTH | num: ≈ ₹10,000 / month | foot: ILLUSTRATIVE · monthly compounding · ~12% is a long-run index SHAPE, never a decimal and never a promise. Both columns shown on purpose. | colour: --target]`

---

## Chapter 7 — वापस उसी सुबह पर

*Both twins close on the morning and on time, not on money. A recaps and CTAs once; B does
neither and holds the higher reach. This takes B's callback, A's single terminal CTA, and
nothing else — zero mid-roll CTA, third independent confirmation of that line.*

**7.1**
> अब वापस उसी मंगलवार की सुबह पर चलिए, जहाँ अलार्म नहीं बजा था।

`[arch A | img: the bedside clock from 1.1, later light on the same table (same object, new crop) | bar: BACK TO TUESDAY | stmt: The alarm that did not go off]`

**7.2**
> फ़ोन पर जो पैसा आया था, वो किसी नौकरी का नहीं था।

`[arch D | img: the phone from 1.3, face-down, the glow gone (same object, new crop) | bar: THAT MONEY | stmt: It was not from a job]`

**7.3**
> वो एक करोड़ का तीन परसेंट था, बारह महीनों में बँटा हुआ — और बस इतना ही।

`[arch B | img: a single ledger line with a figure and a percentage written beside it | bar: WHAT IT WAS | stmt: ₹1,00,00,000 × 3.0% ÷ 12 | foot: The whole video, in one division]`

**7.4**
> इस पूरे वीडियो में कोई भी रक़म अपनी दर के बिना नहीं बोली गई, और यही सबसे ज़रूरी आदत है।

`[arch A | img: five stamped receipts laid in a row, each with a figure and a percent mark | bar: THE HABIT | stmt: Every figure carried its rate]`

**7.5**
> दर के बिना कोई रक़म सिर्फ़ एक वादा है; दर के साथ वो एक भाग है, जिसे आप ख़ुद जाँच सकते हैं।

`[arch D | img: a hand working a division on paper with a pencil (hand only, no face) | bar: THE TEST | stmt: Without a rate it is a promise. With one it is a division you can check.]`

**7.6**
> और यह सीढ़ी एक करोड़ से नहीं, तीन परसेंट वाले उस ढाई हज़ार के पहले रिचार्ज बिल से शुरू हुई थी।

`[arch B | img: the single brick from 2.12, now with two more set beside it | bar: WHERE IT STARTED | stmt: Not at ₹1,00,00,000 — at the ₹2,500 recharge bill, both at 3.0% | colour: --fund]`

**7.7**
> सुबह किसकी है, यह उसी दिन तय होना शुरू होता है जिस दिन पहली सीढ़ी की ईंट रखी जाती है।

`[arch A | img: the window from 1.2 at full daylight, chai glass empty (same object, new crop) | bar: WHOSE MORNING | stmt: It starts on the day the first brick is laid]`

**7.8**
> पैसे की ऐसी सीधी, बिना वादे वाली बात के लिए — सब्सक्राइब कीजिए।

`[arch A | img: a closed ledger and a capped pen laid down, finished | bar: — | num: SUBSCRIBE | colour: --pop (the single --pop block of the video)]`

---

## Fact trace (every number → facts-staging.md)

| Number / claim in script | Where | facts-staging.md row | Tag |
|---|---|---|---|
| **3.0% withdrawal rate** — the assumption everything divides by | 2.6, 2.7, 2.8, 2.9, 3.1, 3.2, 3.5, 3.6, 4.1, 4.2, 4.9, 5.2, 5.15, 6.1, 6.2, 6.6, 6.7, 6.10, 6.13, 7.3 | A.3 "India SWR, peer-reviewed — 3.0–3.5%; best SWR **3.0% at a 40% equity allocation**" (Raju & Saraogi, 2024-01-17) | **HARD on the band** · spoken as a *chosen* number, never as a fact about the future |
| **3.0 – 3.5%** stated as India's published range | 5.15 | A.3 same row | HARD on the band |
| **3.75%** — above this, failure risk rises sharply | 5.16 | A.3 "failure risk rises sharply **above 3.75%**" | HARD (same paper) |
| **4%** = a 1994 US paper, 30-year horizon, no tax/costs | 5.12, 5.13, 5.14, 6.12, 6.13 | A.1 (Bengen, JFP Oct 1994) + A.2 #1 (Trinity, verbatim: *"The study did not adjust for taxes or transaction costs"*) + A.2 #2 (built for 30 years) | **HARD (primary — the Trinity paper was read direct)** |
| **~5%** inflation, the mechanism for the lower rate | 5.17 | A.3 "RBI projects CPI inflation at **5.0% for FY27**", MPC 2026-08-05 | HARD |
| **POMIS 7.4% p.a., paid monthly** | 5.7, 5.8 | B.2 "POMIS rate — **7.4% p.a., paid monthly**" | HARD (two independent + the unchanged notification) |
| **₹9,00,000** POMIS single-account ceiling | 5.9 | B.2 "deposit ceiling — **₹9 lakh single** · ₹15 lakh joint" | HARD (unanimous) |
| **≈ ₹5,550/month** POMIS ceiling output | 5.10 | B.2 lead-out: "Maximum monthly income from one account: **₹5,550**" · PART E records that the secondaries' "₹5,500" is a bad rounding | COMPUTED — spoken as "क़रीब पचपन सौ", exact on screen |
| **₹10,00,000 → ₹2,500/month at 3.0%** | 2.8, 2.9, 3.6 | B.3 formula row: `corpus = annual withdrawal ÷ withdrawal rate`, applied at the staged 3.0% | COMPUTED · `ILLUSTRATIVE` foot on every frame |
| **₹20,00,000 → ₹5,000/month at 3.0%** | 3.1, 3.2, 3.6 | B.3, same formula | COMPUTED |
| **₹40,00,000 → ₹10,000/month at 3.0%** | 4.1, 4.2 | B.3, same formula | COMPUTED |
| **₹50,00,000 → ₹12,500/month at 3.0%** | 6.1, 6.2 | B.3, same formula | COMPUTED |
| **★ ₹1,00,00,000 → ₹25,000/month at 3.0%** — the hero | 6.6, 6.7, 6.10, 6.13, 7.3 | B.3 "**★ THE ₹ HERO NUMBER: ₹1 crore, at a 3% withdrawal rate, is ₹25,000 a month**" — table row ₹25,000/mo (₹3,00,000/yr) at 3.0% = ₹1,00,00,000 | COMPUTED (the staged hero row) |
| **₹75,00,000** = the same ₹25,000/month at 4% | 6.12, 6.13 | B.3 table, 4.0% column: ₹25,000/mo → ₹75,00,000 | COMPUTED (staged row) |
| **A quarter smaller** — the rule-import cost | 6.13 | B.3 "The imported rule under-states an Indian target by **25%**" | COMPUTED (staged framing) |
| **₹24,217** — average monthly earnings, regular wage/salaried | 6.9, 6.10 | B.1 "Regular wage/salaried avg monthly earnings — **₹24,217** men / ₹18,353 women", PLFS Annual Report 2025, PIB | **HARD** |
| **7.1%** assumed growth, and **≈ ₹19,000/month for 20 years** | 6.15 | B.1 "PPF — **7.1% p.a.**, Q2 FY2026-27" + B.3 "Getting there" table, 20-year row at 7.1% ≈ ₹19,000/mo | rate **HARD** · the monthly figure **COMPUTED**, labelled illustrative |
| **~12%** assumed growth, and **≈ ₹10,000/month for 20 years** | 6.16 | B.1 Nifty 50 long-run figure (**SOFT — shape only, never a decimal**, all three NSE hosts 403'd) + B.3 20-year row at ~12% ≈ ₹10,000/mo | **SOFT** — shape only, spoken as "क़रीब बारह परसेंट", no decimal anywhere, and the index measure is **never explained** (B.1 vocabulary trap) |
| **SWP** definition — a fixed amount, a fixed date, out of your own corpus | 2.2, 2.3, 2.4, 4.6, 4.7 | B.2 "SWP = what it is … withdrawals come out of **capital + appreciation**" — four fund houses, identical definition | **HARD (terminology)** |
| Withdrawals are taxable | 4.8 | B.2 LTCG row — tagged **SOFT** (no statute or ITD page read) | **SOFT — so no figure is spoken or shown**, only the fact that tax applies |
| **12%** as a withdrawal rate = a warning | 5.2, 5.4, 5.5, 5.6 | Study conclusion 6 (both twins warn at 10–12%, at ≈5:00) + A.3 (failure risk rises sharply above 3.75%) | the trap beat — **12% is spoken only as a rate someone might PULL OUT, never as a return** |

### Deliberately NOT used (so fin-audit does not rediscover them)

- **The whole of PART C.** That is the other cut's block: a foreign market's income figure,
  a foreign safe-rate literature, foreign funds and a foreign household-spending average.
  The currency firewall in `facts-staging.md` is explicit that the two sets differ on three
  axes at once and are not convertible. The rupee's counterpart glyph appears nowhere in
  this file, not even inside a claim ID.
- **The banned payout word, in every form** — English, inline English, and every Devanagari
  transliteration — and, with it, **any explanation of the index's total-return measure**,
  because that measure is *defined* using the word. 6.16 quotes the shape and nothing else.
- **Bengen's own 2025 revision to 4.7%, and the 3.9% forward-looking figure.** Both are
  HARD and both are rates for the *other* market. Importing either would commit exactly the
  error Chapter 5 spends seventeen lines correcting.
- **Pfau's country count and every country SAFEMAX decimal.** `facts-staging.md` records a
  live conflict (17 vs 19 countries) and instructs "most developed markets", never a count.
  Not needed here — the India research carries the point directly.
- **SCSS 8.2% / ₹30 lakh.** SOFT, no primary read, and **age-gated at sixty-plus** — using
  it would put an age into a video whose binding constraint is that no corpus becomes an age.
- **Any precise India tax figure** (12.5%, ₹1.25 lakh). SOFT — no statute or Income Tax
  Department page was read. 4.8 says tax applies and stops.
- **Industry AUM ₹82.22 lakh crore and the ₹32,087 crore monthly SIP inflow.** SOFT, and
  the staging note itself calls them "context colour only, not a claim the video needs".
- **The 15-year and 25-year SIP rows** (₹32,000 / ₹20,000 and ₹12,150 / ₹5,300). Only the
  20-year row is spoken, and both of its columns are shown. Adding horizons invites the
  viewer to read a *date*, which PART D forbids.
- **The ₹500 / ₹250 monthly minimum.** True and HARD, but it belongs to a "start today"
  beat, and neither twin has one — both close on the morning image. Recorded as an
  available beat if a later cut wants it.
- **Every age, every date-of-freedom, and every "quit your job" formulation.** PART D: the
  only sourced early-retirement statement in the whole file is a warning to withdraw
  *less*. 6.11 states the refusal on the record.
- **A named fund, AMC, bank, app or platform.** Persona rule. The post-office monthly-income
  scheme and the 7.1% small-savings rate appear as published price evidence only, and the
  5.8 and 6.15 foots say so on screen.

---

## Build handoff

1. **`assets/voice/hindi-lines.json` = 78 entries keyed `1.1 … 7.8`**, containing **only**
   the `>` VO strings above — no markdown, no cue text, no on-screen text. Devanagari,
   verbatim. **Slice the source file; never retype.** Gate the extraction with a
   byte-for-byte reconstruction check against this file before generating audio
   (`long_form_scripting.md` §1.7).
2. **TTS** via `tools/tts/elevenlabs_tts.py`, voice `HTUuC7OeeEt6OL5fViVe` (Harsh),
   `eleven_multilingual_v2`, style 0. **78 calls** of the run's 188; the `-en` cut needs a
   comparable number, so do not burn retries casually.
3. **Timing is by construction.** One line = one clip = one scene. Scene span =
   `probe(clip) + lead_in + tail`, with MEDIUM's `lead_in_seconds` 0.25 and `tail_seconds`
   0.55 (`format.json tiers.medium`). Never hand-edit a duration; regenerate all homes of
   the timing numbers from one source.
4. **Recount the characters programmatically** and re-check the total against
   `(510 − 0.8 × lines) × 13.03` — **not** `510 × 13.03`. The table above is a budget
   estimate at ±5%.
5. **The rate is a build-time invariant, not a design preference.** Assert it: every scene
   whose on-screen text contains a corpus token (`₹10,00,000`, `₹20,00,000`, `₹40,00,000`,
   `₹50,00,000`, `₹75,00,000`, `₹1,00,00,000`, `₹9,00,000`) must also render a rate token
   (`3.0%`, `4%`, `7.4%`) in the same frame. That is
   `run.json.constraints.withdrawal_rate_on_screen`, and it is the one thing `fin-audit`
   hard-fails.
6. **Pin the arithmetic convention before computing anything on screen.** Every rung is
   `corpus × 0.03 ÷ 12`, exact, no rounding: ₹10,00,000→₹2,500 · ₹20,00,000→₹5,000 ·
   ₹40,00,000→₹10,000 · ₹50,00,000→₹12,500 · ₹1,00,00,000→₹25,000. The POMIS figure is
   `₹9,00,000 × 0.074 ÷ 12 = ₹5,550` exactly — **not** the ₹5,500 every secondary prints
   (PART E). The VO says "क़रीब पचपन सौ"; the frame says `₹5,550`.
7. **Images: one per line, 78 scenes, zero photo-free frames** (`photo_free_scene_ratio` =
   0). Six lines are marked as returning to an earlier object with a **new crop** — 7.1
   (1.1's clock), 7.2 (1.3's phone), 7.6 (2.12's brick), 7.7 (1.2's window) — those are new
   photographs of the same subject, not the same file re-used; the sound-off rule is per
   line. **2.7 is the only true hold** (it holds 2.6's image): run it as ONE continuous
   zoom across both scenes, never a self-dissolve. That pair totals 5.7 + 6.8 + padding ≈
   14.1 s on one photograph and **breaches `scene.max_scene_seconds` 9.0** — fix it at build
   time by giving 2.7 a second, tighter crop of the same source.
8. **Nothing on screen may be a legible foreign document, price or figure**, and no frame
   may put a rupee figure and a foreign figure in one composition. The 5.13/5.14 journal
   and methodology pages are photographed with **no legible title or numerals** for exactly
   this reason — the citation lives in the `foot:`, not in the photograph.
9. **Never fabricate a source document.** 5.15's Indian research paper is photographed as a
   stapled document with a blank top sheet; no invented seal, agency name or legible figure
   may appear on a frame cited to a real paper (`format.json vector_art.lottie.truth_bar`).
10. **Chapter-wise production.** Build, proof and re-render chapter by chapter
    (`fin-editor` then `fin-ceo`); concat and final-render only after all seven chapters
    are locked.
11. **Captions.** Narration MD + `.srt` per cut via `tools/transcript.py` — join the
    generated lines, never retype them.
