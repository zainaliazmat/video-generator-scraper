---
summary: Hindi/India script for «The first ₹1 lakh is the hardest». MEDIUM tier, per-line chapter architecture — 86 single-sentence VO lines across 9 chapters, ~5,958 chars ≈ 8:18 vs the 510s target. INR only. Standard Hindi (Harsh). On-screen text English/Hinglish, swiss-band. Every number traces to videos/first-lakh-first-thousand/facts-staging.md.
updated: 2026-07-31
source: run.json creator brief (2026-07-31) + facts-staging.md attempt 1 + study note knowledge/video-studies/first-lakh-first-thousand.md. Architecture swiss-band per run.json creator pick; layout spec from knowledge/finance-audit-2026-07-29/11-swiss-vignelli.md Direction 1.
stage: fin-script, cut hi, attempt 1
---

# «पहला एक लाख» — Hindi / India edition (MEDIUM, per-line chapters)

**Studio project (to build):** `studio/videos/first-lakh-first-thousand`
**Language:** Standard Hindi, **Devanagari** — channel voice locked 2026-07-28.
**Voice:** ElevenLabs **Harsh** `HTUuC7OeeEt6OL5fViVe`, `eleven_multilingual_v2`, style 0.
**On-screen text:** English / Hinglish. **Title + description:** Roman script.
**Architecture:** `swiss-band` (run.json creator pick), **MEDIUM tier → per-line chapters**.
**Tier note:** none of the 9-segment blockframe constants apply here. `lines: 9` on the
`swiss-band` registry entry is a SHORT-tier constant. Scene count is emergent from the
script: **one line = one TTS clip = one scene = one exact timeline anchor.**

**Engine rule:** digits are **spelled out** in every VO line below (bare Latin digits are
a coin-flip English reading in ElevenLabs). On-screen numerals carry the exact figures,
`Intl.NumberFormat("en-IN")` grouping (`₹1,00,000`).

**Persona rules (YouTube 2026 AI carve-out):** no host persona, no first-person
expertise, no fund/stock/scheme pick. PPF, post-office small savings and the monthly
minimum appear **only as price evidence** — "this is what the rate is" — never as
"put your money here". Second person throughout; the word "मैं" appears nowhere.

---

> ### ⚠ THE FIVE THINGS THAT MUST NOT ENTER THIS CUT
> All five are named in `facts-staging.md` §4 as the traps for this exact topic.
> 1. **NEVER a dollar sign, a US institution, or a cross-market conversion.** ₹1 lakh
>    is not the other market's milestone and no line may imply it. Munger's line is a
>    US beat — it does not appear in this cut at all.
> 2. **NEVER "₹1 lakh is where compounding takes over."** The crossover is ~₹5 lakh
>    (₹8.5 lakh at seven percent). Chapter 5 exists to say the opposite, out loud.
> 3. **NEVER a months-to-milestone figure spoken as a statistic.** Every one of them is
>    model output. Each spoken figure carries its condition in the same sentence
>    ("पाँच हज़ार महीना", "इस हिसाब से"), and every math frame carries the
>    `ILLUSTRATIVE · ₹5,000/mo · monthly compounding` foot.
> 4. **NEVER a decimal on the equity return.** Say "क़रीब बारह परसेंट", show `~12%/yr`.
>    The Nifty figure is SOFT — both NSE PDFs 403'd. Seven-point-one is HARD and may be
>    exact on screen.
> 5. **NEVER "Indians save five thousand a month."** ₹5,000 is 20% of the locked
>    ₹30,000 worked example — a split, not a statistic. The VO always says
>    "अगर आप ... रख दें".

---

## Title options (Roman script — per the title-language rule)

1. **Pehla 1 Lakh Sabse Mushkil Kyun Hai — 20 Mahine ka Sach** *(recommended — number
   front-loaded, the hook figure is in the title)*
2. Pehla ₹1,00,000: 20 Mahine. Dasva Lakh: 7 Mahine. Farq Kya Hai?
3. ₹5,000 Mahina se Pehla Lakh — Poora Hisaab

---

## Chapters (ship these as YouTube chapters — study conclusion 7)

| # | Chapter | starts | lines |
|---|---|---|---|
| 1 | The first lakh — 20 months vs 7 months | 0:00 | 10 |
| 2 | Why 100% of it is you | 0:55 | 9 |
| 3 | The tenth lakh — the same ₹5,000 | 1:48 | 8 |
| 4 | Savings rate beats return rate | 2:31 | 10 |
| 5 | The crossover — and where it actually is | 3:32 | 10 |
| 6 | "But I can't save ₹5,000" | 4:28 | 10 |
| 7 | **The tank and the bucket** (the ~70% re-frame) | 5:30 | 8 |
| 8 | How you actually cross it | 6:19 | 11 |
| 9 | Do this today + recap | 7:24 | 10 |

---

## Timing budget

Hindi narration ≈ **12.5 chars/s** (`format.json cuts.hi.chars_per_second`). Char counts
below are the **budget estimate (±10%)** — the build step recounts them programmatically
from the extracted lines file and then ffprobe-measures every clip. Gap model (firaun
`build.py`): **0.2s intra-chapter**, **0.8s at a chapter boundary**.

| Ch | lines | chars | VO | + gaps | chapter runtime |
|---|---|---|---|---|---|
| 1 | 10 | ~660 | 52.8s | 2.6 | 55.4s |
| 2 | 9 | ~630 | 50.4s | 2.4 | 52.8s |
| 3 | 8 | ~505 | 40.4s | 2.2 | 42.6s |
| 4 | 10 | ~732 | 58.6s | 2.6 | 61.2s |
| 5 | 10 | ~668 | 53.4s | 2.6 | 56.0s |
| 6 | 10 | ~742 | 59.4s | 2.6 | 62.0s |
| 7 | 8 | ~579 | 46.3s | 2.2 | 48.5s |
| 8 | 11 | ~788 | 63.0s | 2.8 | 65.8s |
| 9 | 10 | ~654 | 52.3s | 1.8 | 54.1s |
| | **86** | **~5,958** | **~476.6s** | **~21.8s** | **~498.4s** |

**Budget check:** 510s × 12.5 = **6,375 char budget**; this draft is **~5,958 (−6.5%)**.
Estimated runtime **~498s (8:18) vs the 510s target — 2.3% under.** That headroom is
deliberate: Hindi TTS at 12.5 chars/s has run slightly slow on the shipped cuts, and the
per-line gap model is a floor, not a ceiling.

**Pace:** ~498s / 86 scenes = **5.8s average scene**, against `scene.target_scene_seconds`
6.5 and `scene.max_scene_seconds` 9.0. No single line exceeds ~103 chars (8.2s), so no
scene can breach the 9s photo-hold check. The shortest line (5.3) is ~23 chars ≈ 1.8s —
above `tts.min_clip_seconds` 1.0.

**Why 86 lines and not the 78 in `format.json tiers.medium.lines`:** that 78 is
510 ÷ 6.5, and `format.json scene._scene_seconds_note` is explicit that scene count is
**emergent from the script, never a constant**. A finance argument built on punch lines
runs shorter per line than firaun's narrative lines. 86 also keeps the pair inside the
run's ElevenLabs ceiling: 86 hi + ~86 en = 172 of 200, leaving 28 calls of retry headroom.

---

## Per-scene timing budget

`ap` = aperture (see the sequence layer below). B = band · C-R/C-L = picture column,
photo right/left · R = reversed field · M = mosaic (major + minor).

| # | chars | est s | ap | | # | chars | est s | ap |
|---|---|---|---|---|---|---|---|---|
| 1.1 | 47 | 3.8 | R | | 5.1 | 59 | 4.7 | B |
| 1.2 | 52 | 4.2 | R | | 5.2 | 93 | 7.4 | B |
| 1.3 | 61 | 4.9 | B | | 5.3 | 23 | 1.8 | R |
| 1.4 | 101 | 8.1 | C-R | | 5.4 | 90 | 7.2 | B |
| 1.5 | 64 | 5.1 | B | | 5.5 | 101 | 8.1 | M |
| 1.6 | 44 | 3.5 | B | | 5.6 | 64 | 5.1 | C-L |
| 1.7 | 83 | 6.6 | B | | 5.7 | 70 | 5.6 | B |
| 1.8 | 59 | 4.7 | C-L | | 5.8 | 59 | 4.7 | B |
| 1.9 | 65 | 5.2 | B | | 5.9 | 52 | 4.2 | R |
| 1.10 | 68 | 5.4 | B | | 5.10 | 57 | 4.6 | B |
| 2.1 | 75 | 6.0 | B | | 6.1 | 56 | 4.5 | B |
| 2.2 | 46 | 3.7 | B | | 6.2 | 86 | 6.9 | B |
| 2.3 | 52 | 4.2 | M | | 6.3 | 95 | 7.6 | C-R |
| 2.4 | 82 | 6.6 | C-R | | 6.4 | 57 | 4.6 | B |
| 2.5 | 35 | 2.8 | B | | 6.5 | 76 | 6.1 | M |
| 2.6 | 100 | 8.0 | B | | 6.6 | 59 | 4.7 | B |
| 2.7 | 95 | 7.6 | R | | 6.7 | 67 | 5.4 | B |
| 2.8 | 80 | 6.4 | B | | 6.8 | 66 | 5.3 | C-L |
| 2.9 | 65 | 5.2 | B | | 6.9 | 91 | 7.3 | B |
| 3.1 | 64 | 5.1 | B | | 6.10 | 65 | 5.2 | B |
| 3.2 | 80 | 6.4 | M | | 7.1 | 87 | 7.0 | B |
| 3.3 | 41 | 3.3 | B | | 7.2 | 65 | 5.2 | B |
| 3.4 | 48 | 3.8 | B | | 7.3 | 67 | 5.4 | C-R |
| 3.5 | 72 | 5.8 | C-L | | 7.4 | 68 | 5.4 | B |
| 3.6 | 57 | 4.6 | B | | 7.5 | 78 | 6.2 | B |
| 3.7 | 63 | 5.0 | R | | 7.6 | 75 | 6.0 | R |
| 3.8 | 80 | 6.4 | B | | 7.7 | 76 | 6.1 | B |
| 4.1 | 66 | 5.3 | B | | 7.8 | 63 | 5.0 | B |
| 4.2 | 48 | 3.8 | B | | 8.1 | 62 | 5.0 | B |
| 4.3 | 67 | 5.4 | C-R | | 8.2 | 103 | 8.2 | C-R |
| 4.4 | 65 | 5.2 | B | | 8.3 | 85 | 6.8 | B |
| 4.5 | 85 | 6.8 | B | | 8.4 | 45 | 3.6 | B |
| 4.6 | 82 | 6.6 | R | | 8.5 | 72 | 5.8 | B |
| 4.7 | 68 | 5.4 | B | | 8.6 | 73 | 5.8 | C-L |
| 4.8 | 54 | 4.3 | B | | 8.7 | 87 | 7.0 | B |
| 4.9 | 82 | 6.6 | C-L | | 8.8 | 66 | 5.3 | M |
| 4.10 | 87 | 7.0 | M | | 8.9 | 57 | 4.6 | B |
| | | | | | 8.10 | 61 | 4.9 | B |
| | | | | | 8.11 | 77 | 6.2 | R |
| 9.1 | 43 | 3.4 | B | | 9.6 | 45 | 3.6 | M |
| 9.2 | 65 | 5.2 | C-R | | 9.7 | 86 | 6.9 | B |
| 9.3 | 61 | 4.9 | B | | 9.8 | 81 | 6.5 | R |
| 9.4 | 63 | 5.0 | B | | 9.9 | 48 | 3.8 | B |
| 9.5 | 98 | 7.8 | B | | 9.10 | 64 | 5.1 | B |

---

## The swiss-band spec, as this script uses it

Direction 1 of `knowledge/finance-audit-2026-07-29/11-swiss-vignelli.md`. Load-bearing
constraints the on-screen blocks below already obey:

- **Two type sizes per scene.** Every scene is `bar:` (84px/800, reversed in the black
  title bar) + **one** of `stmt:` (54px/500, hung from the 3px rule at y=780) or `num:`
  (200px/900, tabular, hung from the same rule). A `foot:` (26px/200 `--muted`) is the
  permitted third size and carries the source / the illustrative label.
- **Never a bar + a heading + a subhead in one frame.** No chip rows, no bulleted rows,
  no enumerated lists — the per-line architecture makes them unnecessary anyway.
- **Flush left, squared corners, no scrim, no `text-shadow`, no per-scene `--tint`,
  no rotation.**
- **One role colour per scene, ever.** This video's semantics, derived from its thesis:
  `--warn` red = **the stretch nobody helps you with** (the first lakh, the twenty
  months, the market's two-month gift) · `--fund` green = **the mechanism that works
  without you once it exists** — the standing instruction now, returns later (the
  auto-transfer, the habit, the savings rate; the tenth lakh, seven months, the rain).
  ⚠ Audit note: green is NOT "returns doing the work" — it is used on 4.6, 4.8, 5.9,
  8.2, 8.5, 8.7, 9.2 and 9.4, every one of which is the viewer's own behaviour, and
  5.9 exists specifically to deny that returns take over at the first lakh. Reading it
  as "returns" would make the palette argue against the video's thesis ·
  `--target` amber = **a rate or a threshold
  under examination** (7.1%, ~12%, the ₹5 lakh crossover) · `--pop` orange = the CTA
  block, **once**, at 9.9.
- **Ken Burns at half amplitude** inside the band (`1.0 ↔ 1.06`, `xPercent ∓1.2`),
  alternating direction per scene. Boundary = **hard directional wipe, 0.45s** (same
  duration as the dissolve it replaces — `scdet` must be re-measured, §9 open question).

### The sequence layer (the anti-sameness engine — mandatory, not optional)

Canon p.84: a fixed system with a **declared cycle of apertures**, never one frame
repeated. The programme, not the artefact:

- **BAND (D1) is the default** and carries ~62% of scenes.
- **COLUMN (D2)** on one scene in roughly every four, alternating photo side L/R across
  the whole video, so the swap reads as a rhythm.
- **REVERSED FIELD (D4)** on exactly **9 scenes**, all marked `R` in the table above —
  the hook (1.1, 1.2), the thesis (2.7), the sentence the video is named for (3.7), the
  savings-rate line (4.6), the crossover term (5.3) and its correction (5.9), the rain
  line (7.6), the way it actually breaks (8.11) and the closing statement (9.8).
  Reversed type only where the image's left third measures below 25% luminance —
  **measure it, do not assume it**.
- **MOSAIC (D3)** on the 8 scenes that carry a two-figure comparison (2.3, 3.2, 4.10,
  5.5, 6.5, 8.8, 9.6). Major rectangle = photo, minor rectangle = the second figure.
- **Cycle offset varies by video** — this cut starts on R. The `-en` cut must not.

---

# THE SCRIPT

> **VO block rule.** Every `>` quoted line below is a VO line, verbatim, and is the only
> thing that goes to TTS. Everything in backticks is a production cue and never spoken.
> **Slice these strings — never retype them.** Retyping Devanagari silently swaps
> characters (nukta, chandrabindu) and the swap is inaudible until the render.

---

## Chapter 1 — पहला एक लाख (HOOK · cold open on the number)

*Study conclusion 1: the first sentence carries the number. TOP's frame-one is a figure;
LOW opened on a static title card and died at 0.048× subs. No greeting, no roadmap
before the number, no title card anywhere.*

**1.1**
> पाँच हज़ार रुपये महीना। पहला एक लाख — बीस महीने।

`[ap R | img: steel coin jar half-full on a kitchen shelf, low light | bar: THE FIRST LAKH | num: 20 MONTHS | foot: ILLUSTRATIVE · ₹5,000/mo · 0% return · monthly compounding | colour: --warn]`

**1.2**
> वही पाँच हज़ार महीना, नौ लाख से दस लाख — सात महीने।

`[ap R | hold 1.1's image, ONE continuous zoom across both scenes | bar: THE TENTH LAKH | num: 7 MONTHS | foot: ILLUSTRATIVE · ₹5,000/mo · ~12%/yr · monthly compounding | colour: --fund]`

**1.3**
> एक ही रक़म, एक ही आदमी, एक ही बाज़ार — पर बीस महीने और सात महीने।

`[ap B | img: two identical brass weights on a shop balance scale | bar: SAME ₹5,000 | stmt: 20 months → 7 months | colour: --warn]`

**1.4**
> दोनों में पैसा उसी जगह लगा है; फ़र्क़ सिर्फ़ इतना है कि दूसरी बार आपके साथ पहले से नौ लाख खड़े हैं।

`[ap C-R | img: stacked ledger volumes on a shelf, one thin one thick | bar: WHAT CHANGED | stmt: The second time, ₹9,00,000 was already standing behind it | foot: Illustrative model — same monthly amount, same rate]`

**1.5**
> इसीलिए पहला एक लाख आपकी ज़िंदगी का सबसे मुश्किल एक लाख होता है।

`[ap B | img: single rupee coin standing on edge on a wooden table, hard side light | bar: THE HARDEST ONE | stmt: The first ₹1,00,000 is the hardest money you will ever save | colour: --warn]`

**1.6**
> उसके बाद पैसा आपकी मदद करना शुरू करता है।

`[ap B | hold 1.5's image, ONE continuous zoom across both scenes | bar: AFTER THAT | stmt: The money starts helping]`

**1.7**
> तीन सवाल, जिनके जवाब इस वीडियो में हैं — पहला, वो मदद असल में शुरू कब होती है?

`[ap B | img: three closed envelopes fanned on a desk | bar: QUESTION ONE | stmt: When does the money actually start helping? | colour: --target]`

**1.8**
> दूसरा — शुरुआत में सही स्कीम चुनने से कितना फ़र्क़ पड़ता है?

`[ap C-L | img: printed interest-rate chart page, macro, one column in focus | bar: QUESTION TWO | stmt: How much does picking the right scheme change? | colour: --target]`

**1.9**
> और तीसरा — अगर पाँच हज़ार महीना बचता ही नहीं, तो पहला कदम क्या है?

`[ap B | img: an empty steel tiffin box open on a table | bar: QUESTION THREE | stmt: And if ₹5,000 a month isn't there? | colour: --target]`

**1.10**
> जवाब तीनों मिलेंगे। पर पहले वो हिसाब, जो शुरुआत में कोई नहीं दिखाता।

`[ap B | img: hand-written arithmetic on lined paper, pencil resting | bar: FIRST, THE ARITHMETIC | stmt: The sum nobody does at the start]`

---

## Chapter 2 — पहले लाख का सौ परसेंट आप हैं

*Core beat 1 of the creator brief. This chapter is the whole thesis, stated as arithmetic
rather than as an opinion.*

**2.1**
> मान लीजिए तनख़्वाह तीस हज़ार है, और आप हर महीने पाँच हज़ार अलग रख देते हैं।

`[ap B | img: pay slip printed on thin paper, folded once | bar: THE EXAMPLE | stmt: ₹30,000 take-home · ₹5,000 set aside | foot: Channel worked-example convention — not a national average]`

**2.2**
> साठ हज़ार साल के। कोई रिटर्न नहीं, सिर्फ़ जमा।

`[ap B | img: twelve small stacks of coins in a row | bar: PER YEAR | num: ₹60,000 | foot: ₹5,000 × 12 — deposits only, no return]`

**2.3**
> इस हिसाब से पहला एक लाख बीस महीने में पूरा होता है।

`[ap M | major: wall calendar with months crossed off; minor: coin jar | bar: AT 0% | num: 20 MONTHS | foot: ILLUSTRATIVE · ₹5,000/mo · 0% · monthly compounding | colour: --warn]`

**2.4**
> अब मान लीजिए वही पैसा सरकारी छोटी बचत के रेट पर पड़ा है — अभी क़रीब सात दशमलव एक परसेंट।

`[ap C-R | img: post office counter window, brass grille, no faces | bar: THE RATE | num: 7.1% | foot: PPF and the 3-year post-office time deposit, Q2 FY2026-27 (DEA notification, 30 Jun 2026) | colour: --target]`

**2.5**
> बीस महीने घटकर उन्नीस हो जाते हैं।

`[ap B | img: single calendar page torn and falling | bar: AT 7.1% | num: 19 MONTHS | foot: ILLUSTRATIVE · ₹5,000/mo · 7.1% · monthly compounding]`

**2.6**
> और अगर इतिहास वाला बाज़ार का रिटर्न मान लें, क़रीब बारह परसेंट सालाना — तो बीस से घटकर अठारह महीने।

`[ap B | img: newspaper market page, macro, folded | bar: AT ~12% | num: 18 MONTHS | foot: ILLUSTRATIVE · ₹5,000/mo · ~12%/yr · long-run Nifty 50 TRI shape — never a precise figure | colour: --target]`

**2.7**
> देश का सबसे अच्छा माना जाने वाला रिटर्न, पूरे पहले लाख पर, आपको सिर्फ़ दो महीने बचाकर देता है।

`[ap R | img: sand running through the neck of an hourglass, macro | bar: WHAT THE MARKET BOUGHT YOU | num: 2 MONTHS | foot: 20 months → 18 months, on the first ₹1,00,000 | colour: --warn]`

**2.8**
> क्योंकि जिस पैसे पर रिटर्न मिलना है, वो पैसा अभी है ही नहीं।

`[ap B | img: empty steel plate on a bare table, raking light | bar: WHY | stmt: There is no balance for a return to act on yet]`

**2.9**
> पहले लाख का सौ परसेंट आपकी बचत से आता है, रिटर्न से कुछ भी नहीं।

`[ap B | img: single hand placing a note into a locked steel box (hand only, no face) | bar: THE FIRST LAKH | stmt: 100% savings · 0% returns | colour: --warn]`

---

## Chapter 3 — दसवाँ लाख (the visible sum)

*Study conclusion 6: do at least one visible sum on screen — the arithmetic the LOW
video refused to perform. This chapter is that sum.*

**3.1**
> अब यही हिसाब आगे बढ़ाइए — वही पाँच हज़ार महीना, कुछ भी बदले बिना।

`[ap B | img: a long strip of ruled ledger paper running off the table edge | bar: SAME INPUT | stmt: ₹5,000 a month · nothing else changes]`

**3.2**
> दूसरा लाख — बिना रिटर्न के बीस महीने, सात परसेंट पर सत्रह, बारह परसेंट पर पंद्रह।

`[ap M | major: two coin jars side by side, second fuller; minor: rate card macro | bar: THE SECOND LAKH | stmt: 0% → 20 · 7.1% → 17 · ~12% → 15 months | foot: ILLUSTRATIVE · ₹5,000/mo · monthly compounding]`

**3.3**
> अंतर बढ़ने लगा — दो महीने से पाँच महीने।

`[ap B | img: two nails of different height in a plank, side light | bar: THE GAP GROWS | stmt: 2 months → 5 months]`

**3.4**
> अब सीधे दसवें लाख पर जाइए — नौ लाख से दस लाख तक।

`[ap B | img: a full steel trunk with the lid propped open | bar: THE TENTH LAKH | stmt: ₹9,00,000 → ₹10,00,000]`

**3.5**
> बिना रिटर्न के वही बीस महीने। पैसा कभी तेज़ नहीं होता अगर वो काम न करे।

`[ap C-L | img: stationary bullock cart wheel, dust, still | bar: STILL AT 0% | num: 20 MONTHS | foot: ILLUSTRATIVE · ₹5,000/mo · 0% — the interval never shortens | colour: --warn]`

**3.6**
> सात परसेंट पर — नौ महीने। और बारह परसेंट पर — सात महीने।

`[ap B | img: railway platform clock, hands mid-sweep | bar: WITH RETURNS | stmt: 7.1% → 9 months · ~12% → 7 months | foot: ILLUSTRATIVE · ₹5,000/mo · monthly compounding | colour: --fund]`

**3.7**
> पहले लाख पर रिटर्न ने दो महीने बचाए थे। दसवें पर तेरह बचा दिए।

`[ap R | img: two ropes of very different length coiled on a deck | bar: 2 vs 13 | num: 13 MONTHS | foot: The same return, on the tenth lakh instead of the first | colour: --fund]`

**3.8**
> यही इस पूरे वीडियो की बात है — और यही वो हिस्सा है जो शुरुआत में कोई नहीं बताता।

`[ap B | img: a page torn out of a bound book, the gap visible | bar: THIS IS THE VIDEO | stmt: Two months at the start. Thirteen at the tenth.]`

---

## Chapter 4 — रेट नहीं, सेविंग रेट

*Core beat 3. This is the mid-video drop zone (~2:31–3:32, i.e. 30–43% — the flat stretch
gets tension, not a transition): the chapter opens by accusing the viewer's actual
behaviour, not by summarising.*

**4.1**
> अब सोचिए — शुरुआत में लोग सबसे ज़्यादा वक़्त किस चीज़ पर लगाते हैं?

`[ap B | img: a dozen printed comparison sheets spread across a bed | bar: WHERE THE TIME GOES | stmt: What do people spend the first months on?]`

**4.2**
> सही फ़ंड ढूँढने पर। सही स्कीम, सही रेट, सही ऐप।

`[ap B | img: rows of identical blank forms in a wooden rack | bar: THE SEARCH | stmt: The right scheme. The right rate. The right app.]`

**4.3**
> हफ़्तों की रिसर्च, दर्जनों वीडियो, और आख़िर में खाता खुलता ही नहीं।

`[ap C-R | img: a form left half-filled, pen capped beside it | bar: THE RESULT | stmt: Weeks of research — and the account never opens | colour: --warn]`

**4.4**
> पर हिसाब साफ़ कह रहा है — पहले लाख पर रेट का असर दो महीने का था।

`[ap B | img: a short ruler laid against a long plank | bar: WHAT IT WAS WORTH | num: 2 MONTHS | foot: ILLUSTRATIVE · the whole gap between 0% and ~12% on the first ₹1,00,000]`

**4.5**
> और अगर आप उन दो महीनों की तलाश में छह महीने शुरू ही नहीं करते, तो घाटा उल्टा हो गया।

`[ap B | img: an unopened envelope gathering dust on a window sill | bar: THE REAL COST | stmt: Six months not starting, to win two | colour: --warn]`

**4.6**
> शुरुआत में जो चीज़ सबसे ज़्यादा मायने रखती है, वो रिटर्न रेट नहीं — सेविंग रेट है।

`[ap R | img: a tap running into a bucket, water column caught mid-fall | bar: THE ONE THAT MATTERS | stmt: Not the return rate. The savings rate. | colour: --fund]`

**4.7**
> यानी हर महीने आपकी आमदनी का कितना हिस्सा बाहर निकलकर अलग हो जाता है।

`[ap B | img: an envelope with a portion of notes pulled clear of it | bar: DEFINITION | stmt: How much of each month's income leaves and stays out]`

**4.8**
> और यह वो अकेला नंबर है जो पूरी तरह आपके क़ाबू में है।

`[ap B | img: a hand on a brass tap handle (hand only, no face) | bar: YOURS | stmt: The only number fully in your control | colour: --fund]`

**4.9**
> बाज़ार आपकी नहीं सुनता, रेट सरकार तय करती है, पर कितना अलग हटेगा — यह आप तय करते हैं।

`[ap C-L | img: a government notification page, official seal visible, macro | bar: WHO DECIDES WHAT | stmt: Market: not you · Rate: not you · Amount: you]`

**4.10**
> छोटी बचत के रेट पिछली नौ तिमाही से एक इंच नहीं हिले — यह इंतज़ार करने लायक़ चीज़ नहीं है।

`[ap M | major: a wall of identical post office rate boards; minor: a calendar of quarters | bar: NOT WORTH WAITING FOR | stmt: Small-savings rates: unchanged for nine straight quarters | foot: Dept. of Economic Affairs notification, 30 Jun 2026 — Q2 FY2026-27 | colour: --target]`

---

## Chapter 5 — क्रॉसओवर

*Core beat 2, and the answer to loop one. This chapter carries the single factual error
the video was most likely to make (facts-staging §1.3) — so it states the correction
explicitly, three times.*

**5.1**
> तो पैसा आपकी मदद करना शुरू कब करता है? पहला सवाल, अब जवाब।

`[ap B | img: the first of the three envelopes now open | bar: QUESTION ONE, ANSWERED | stmt: When does the money start helping?]`

**5.2**
> एक बिंदु आता है जहाँ आपका पैसा साल भर में उतना कमा लेता है, जितना आप साल भर में बचा पाते हैं।

`[ap B | img: a two-pan balance almost level, one coin short | bar: THE POINT | stmt: The year your money earns what you save]`

**5.3**
> इसे क्रॉसओवर कहते हैं।

`[ap R | hold 5.2's image, ONE continuous zoom into the pivot | bar: THE WORD | num: CROSSOVER | colour: --target]`

**5.4**
> आप साल में साठ हज़ार डाल रहे हैं — तो सवाल यह है कि जमा पैसा साठ हज़ार कब कमाने लगेगा।

`[ap B | img: a bundle of notes bound with a paper band | bar: THE TEST | stmt: When does the balance earn ₹60,000 in a year? | foot: ₹5,000/mo × 12 = ₹60,000 a year in]`

**5.5**
> सात परसेंट के हिसाब से यह क़रीब साढ़े आठ लाख पर आता है, और बारह परसेंट के हिसाब से क़रीब पाँच लाख पर।

`[ap M | major: a large full water tank on a roof; minor: a rate card | bar: WHERE IT LANDS | stmt: ~₹8,50,000 at 7.1% · ~₹4,80,000 at ~12% | foot: ILLUSTRATIVE · ₹60,000/yr contribution · monthly compounding | colour: --target]`

**5.6**
> यानी असली मोड़ पहले लाख पर नहीं, कहीं पाँच लाख के आसपास आता है।

`[ap C-L | img: a road bend marker stone, weathered | bar: THE REAL TURN | num: ~₹5,00,000 | foot: Not ₹1,00,000 — the crossover sits roughly five times further out | colour: --target]`

**5.7**
> यह बात साफ़ कह देना ज़रूरी है, क्योंकि इंटरनेट पर अक्सर उल्टा लिखा मिलता है।

`[ap B | img: a printed page with a line struck through in ink | bar: SAY IT PLAINLY | stmt: The internet usually says otherwise | colour: --warn]`

**5.8**
> पहला लाख वो जगह नहीं है जहाँ ब्याज आपका काम सँभाल लेता है।

`[ap B | img: an idle hand-pump handle, dry ground beneath | bar: NOT THAT | stmt: The first lakh is not where interest takes over | colour: --warn]`

**5.9**
> पहला लाख वो जगह है जहाँ आदत आपका काम सँभाल लेती है।

`[ap R | img: a worn doorstep, footpath polished smooth by use | bar: THIS | stmt: The first lakh is where the HABIT takes over | colour: --fund]`

**5.10**
> और आदत के बिना पाँच लाख तक पहुँचने का कोई रास्ता नहीं है।

`[ap B | img: a long flight of stone steps going up, empty | bar: THE ONLY ROUTE | stmt: There is no path to ₹5,00,000 that skips it]`

---

## Chapter 6 — "पर पाँच हज़ार कहाँ से आएँ?"

*Answer to loop three, and the honesty beat. facts-staging forbids dressing ₹5,000 as a
national average; this chapter says out loud that it is a split, and that a smaller
amount genuinely takes longer.*

**6.1**
> अब तीसरा सवाल — अगर हर महीने पाँच हज़ार बचते ही नहीं तो?

`[ap B | img: the third envelope, being opened with a thumb | bar: QUESTION THREE | stmt: And if ₹5,000 a month simply isn't there?]`

**6.2**
> नियमित तनख़्वाह पाने वाले भारतीयों की औसत महीने की कमाई अठारह से चौबीस हज़ार के बीच है।

`[ap B | img: a bus-stop queue of feet and bags, morning, no faces | bar: THE REAL SPREAD | stmt: ₹18,353 – ₹24,217 a month | foot: PLFS Annual Report 2025 — regular wage/salaried average: ₹24,217 men, ₹18,353 women]`

**6.3**
> और रिज़र्व बैंक के आँकड़े में हर सौ रुपये की राष्ट्रीय आमदनी पर सिर्फ़ सात रुपये बचत में जाते हैं।

`[ap C-R | img: a hundred-rupee note held flat against grey card | bar: WHAT THE COUNTRY SAVES | stmt: ₹7 out of every ₹100 | foot: RBI Annual Report, May 2026 — net household financial savings, 7.0% of GNDI, FY25 | colour: --warn]`

**6.4**
> तो पाँच हज़ार कोई औसत नहीं है — वो एक बँटवारे का नतीजा है।

`[ap B | img: a chapati divided into unequal pieces on a steel plate | bar: NOT AN AVERAGE | stmt: ₹5,000 is the output of a split]`

**6.5**
> तीस हज़ार में से पैंसठ परसेंट ज़रूरतें, पंद्रह परसेंट शौक़, और बीस परसेंट बचत।

`[ap M | major: three unequal grain piles on a cloth; minor: the ₹30,000 pay slip | bar: THE SPLIT | stmt: 65 needs · 15 wants · 20 savings | foot: Channel convention — a workable Indian split, not a published statistic]`

**6.6**
> बीस परसेंट यानी पाँच हज़ार। यही इस वीडियो का पूरा हिसाब है।

`[ap B | img: a single stack of five notes squared on a table | bar: 20% OF ₹30,000 | num: ₹5,000 | foot: Every figure in this video runs on this one input]`

**6.7**
> अगर आपका बीस परसेंट पंद्रह सौ बनता है, तो शुरुआत पंद्रह सौ से होगी।

`[ap B | img: a small pile of coins beside a much larger one | bar: YOUR 20% | stmt: If yours is ₹1,500, you start at ₹1,500]`

**6.8**
> और सच यह है कि तब पहला लाख दूर रहेगा — यह छिपाने वाली बात नहीं है।

`[ap C-L | img: a long straight road disappearing at the horizon | bar: HONESTLY | stmt: Then the first lakh is further away. That's the truth. | colour: --warn]`

**6.9**
> पर महीने-दर-महीने निवेश की न्यूनतम रक़म पाँच सौ रुपये है, और कुछ योजनाओं में ढाई सौ।

`[ap B | img: a five-hundred rupee note and loose coins on a counter | bar: THE ENTRY TICKET | stmt: ₹500 a month · ₹250 in some | foot: AMFI — SIP minimum ₹500/mo; ₹250 "Chhoti SIP". Price evidence, not a recommendation. | colour: --target]`

**6.10**
> यानी रुकावट रक़म नहीं है। रुकावट वो तारीख़ है जो कभी आती ही नहीं।

`[ap B | img: a calendar with no marks on any date | bar: THE REAL BLOCKER | stmt: Not the amount. The date that never arrives. | colour: --warn]`

---

## Chapter 7 — टंकी और बाल्टी (THE ~70% RE-FRAME)

*Study conclusion 4 and TOP's move 3: at ~70% the video re-frames what it already
proved with a physical image, rather than introducing a new fact. Runs 5:30–6:19 of
8:18 — the punch line (7.7) lands at ~6:12 ≈ **70%**. Nothing here is new information.*

**7.1**
> एक तस्वीर से समझिए — छत पर एक पानी की टंकी है, और वो खाली है।

`[ap B | img: a black plastic water tank on a rooftop, morning light | bar: PICTURE THIS | stmt: An empty tank on the roof]`

**7.2**
> आपके पास एक बाल्टी है, और सीढ़ी है।

`[ap B | img: a steel bucket at the foot of a ladder | bar: WHAT YOU HAVE | stmt: A bucket. And a ladder.]`

**7.3**
> पहली बार टंकी भरने का सिर्फ़ एक तरीक़ा है — आप, सीढ़ी, और बाल्टी।

`[ap C-R | img: a bucket carried up a ladder rung (hands and bucket only, no face) | bar: THE ONLY WAY | stmt: The first fill is you, the ladder and the bucket | colour: --warn]`

**7.4**
> बारिश उस वक़्त आपकी कोई मदद नहीं करती, क्योंकि टंकी की सतह छोटी है।

`[ap B | img: a few raindrops on a small tin lid | bar: WHY THE RAIN CAN'T HELP | stmt: The surface catching it is tiny]`

**7.5**
> पर जैसे-जैसे टंकी भरती है, पानी की चौड़ी सतह बारिश को पकड़ने लगती है।

`[ap B | img: rain rings spreading across a wide open water surface | bar: AS IT FILLS | stmt: A wider surface starts catching the rain | colour: --fund]`

**7.6**
> एक दिन ऐसा आता है जब बारिश उतना पानी डाल देती है जितना आप बाल्टी से डालते थे।

`[ap R | img: heavy rain falling on a full open tank, wide | bar: ONE DAY | stmt: The rain puts in what your bucket used to | colour: --fund]`

**7.7**
> वो दिन क्रॉसओवर है — और वो पहली बाल्टी के बाद आता है, पहली बाल्टी में नहीं।

`[ap B | img: the bucket set down, empty, beside a full tank | bar: THAT DAY IS THE CROSSOVER | stmt: It comes AFTER the first bucket — not in it | colour: --target]`

**7.8**
> जहाँ यह मिसाल टूटती है वो भी बता देते हैं — बारिश हर साल एक जैसी नहीं होती, और न बाज़ार।

`[ap B | img: a dry cracked field beside a water channel | bar: WHERE THE ANALOGY BREAKS | stmt: Rain isn't the same every year. Neither is the market. | foot: Long-run market returns are a historical shape, not a promise | colour: --warn]`

---

## Chapter 8 — पहली बाल्टी कैसे भरती है

*Core beat 4 + the three-rung ladder from the MID study pick at 49:42 (emergency fund →
stability → growth), restated product-free. No scheme, no fund, no bank and no app is
named anywhere in this chapter — the whole thing is behaviour.*

**8.1**
> तो पहली बाल्टी भरने का तरीक़ा क्या है? तीन चीज़ें, और तीनों उबाऊ।

`[ap B | img: three plain steel vessels in a row | bar: THREE THINGS | stmt: All three are boring]`

**8.2**
> पहली — तारीख़ तय कीजिए, इरादा नहीं; तनख़्वाह जिस दिन आती है, उसी दिन ऑटो-ट्रांसफ़र लग जाए।

`[ap C-R | img: a date circled on a wall calendar in pen | bar: ONE — PICK A DATE | stmt: A date, not an intention. Salary day. | colour: --fund]`

**8.3**
> महीने के आख़िर में जो बचेगा उससे बचत कभी नहीं होती — बची हुई रक़म हमेशा शून्य होती है।

`[ap B | img: an empty wallet lying open, month-end | bar: WHY NOT LATER | stmt: What's left at month end is always zero | colour: --warn]`

**8.4**
> दूसरी — हर बढ़ोतरी पर बचत बढ़ाइए, ख़र्च नहीं।

`[ap B | img: a growth-ring cross-section of cut timber | bar: TWO — THE ESCALATOR | stmt: Raise the saving, not the spending]`

**8.5**
> अगली बार तनख़्वाह बढ़े, तो पूरी बढ़ोतरी उसी ऑटो-ट्रांसफ़र में जोड़ दीजिए।

`[ap B | img: a measuring jug being topped up to the next mark | bar: THE WHOLE RAISE | stmt: Add all of the next raise to the same transfer | colour: --fund]`

**8.6**
> आपकी ज़िंदगी वैसी ही रहेगी जैसी कल थी, और बचत की दर चुपचाप ऊपर चली जाएगी।

`[ap C-L | img: an unchanged kitchen shelf, same items, softer light | bar: NOTHING CHANGES | stmt: Your life stays yesterday's. The rate quietly climbs.]`

**8.7**
> तीसरी — उसे छूने में मुश्किल बना दीजिए: अलग खाता, कोई कार्ड नहीं, कोई शॉर्टकट नहीं।

`[ap B | img: a padlock on a small steel cupboard | bar: THREE — MAKE IT HARD | stmt: A separate account. No card. No shortcut. | colour: --fund]`

**8.8**
> और क्रम भी उतना ही सीधा है — पहले सुरक्षा, फिर स्थिरता, फिर बढ़त।

`[ap M | major: three stone steps rising; minor: a closed steel box | bar: THE ORDER | stmt: Safety → stability → growth | foot: The sequence practitioners describe — ordering, not a product pick]`

**8.9**
> पहले कुछ महीनों का ख़र्च ऐसी जगह जहाँ से तुरंत निकल सके।

`[ap B | img: an open wide-mouthed jar on a low shelf | bar: RUNG ONE | stmt: A few months of expenses you can reach the same day]`

**8.10**
> उसके बाद ही वो हिस्सा जिसे लंबे वक़्त के लिए बंद किया जा सके।

`[ap B | img: a sealed clay pot with a cloth tie | bar: RUNGS TWO AND THREE | stmt: Only then the part you can shut away for years]`

**8.11**
> क्योंकि पहला लाख अक्सर बचत की कमी से नहीं टूटता — वो एक इमरजेंसी से टूटता है।

`[ap R | img: a cracked earthen pot, contents spilled | bar: HOW IT ACTUALLY BREAKS | stmt: Not by under-saving. By one emergency. | colour: --warn]`

---

## Chapter 9 — आज का एक काम + recap

*Peak-end: the action first (while attention is still on the argument), the recap second,
the CTA after a payoff, then a loop into the next video (session time).*

**9.1**
> तो आज का काम एक ही है, और पाँच मिनट का है।

`[ap B | img: a wall clock reading five past the hour | bar: TODAY | stmt: One job. Five minutes.]`

**9.2**
> बैंक ऐप खोलिए, एक ऑटो-ट्रांसफ़र बनाइए, और तारीख़ तनख़्वाह वाली रखिए।

`[ap C-R | img: a bank passbook open beside a pen — NOT a phone screen (§7, has shipped wrong three times) | bar: DO THIS | stmt: One auto-transfer, dated to salary day | colour: --fund]`

**9.3**
> रक़म वो जो आपको डराए नहीं — पंद्रह सौ चलेगा, पाँच सौ भी चलेगा।

`[ap B | img: a small coin and a large coin side by side | bar: THE AMOUNT | stmt: ₹1,500 works. ₹500 works. | foot: The size is not the point; the standing instruction is]`

**9.4**
> और एक बार बना देने के बाद, उस फ़ैसले को दोबारा नहीं लेना पड़ता।

`[ap B | img: a switch in the on position, dust on the plate | bar: WHY IT WORKS | stmt: You never have to make the decision again | colour: --fund]`

**9.5**
> छोटी बात दोहरा देते हैं — पहले लाख का सौ परसेंट आपकी बचत है, रिटर्न वहाँ सिर्फ़ दो महीने बचाता है।

`[ap B | img: the coin jar from 1.1, now noticeably fuller (same object, new crop) | bar: RECAP ONE | stmt: The first lakh: 100% you · returns buy 2 months | colour: --warn]`

**9.6**
> दसवें लाख पर वही रिटर्न तेरह महीने बचाता है।

`[ap M | major: the full steel trunk; minor: the two ropes | bar: RECAP TWO | stmt: The tenth lakh: the same return buys 13 | colour: --fund]`

**9.7**
> और जहाँ पैसा सच में आपका हाथ बँटाने लगता है, वो जगह पाँच लाख के आसपास है — एक लाख नहीं।

`[ap B | img: the roadside bend marker again, later light | bar: RECAP THREE | stmt: The crossover is near ₹5,00,000 — not ₹1,00,000 | colour: --target]`

**9.8**
> पहला लाख मुश्किल है क्योंकि वो पूरा आपका है। उसके बाद पैसा साथ देना शुरू करता है।

`[ap R | img: a full water tank at dusk, roofline silhouette | bar: THE WHOLE VIDEO | stmt: Hard because it's all you. After that, the money helps. | colour: --fund]`

**9.9**
> पैसे की ऐसी सीधी बात के लिए — सब्सक्राइब कीजिए।

`[ap B | img: an open ledger and a pen laid down, finished | bar: — | num: SUBSCRIBE | colour: --pop (the single --pop block of the video)]`

**9.10**
> और अगली बार — वो पाँच लाख, और उसके बाद पैसा किस रफ़्तार से चलता है।

`[ap B | img: a stone milestone marker on an open road, distance ahead | bar: NEXT | stmt: The ₹5,00,000 mark — and the speed after it]`

---

## Fact trace (every number → facts-staging.md)

| Number / claim in script | Where | facts-staging.md line | Tag |
|---|---|---|---|
| **₹30,000/mo** worked example | 2.1, 6.5, 6.6 | §1.1 "Worked-example in-hand salary — ₹30,000/mo, channel convention" | CONVENTION (labelled on screen) |
| **65 / 15 / 20** split | 6.5 | §1.1 "Honest Indian budget split — 65 needs / 15 wants / **20 savings**" | CONVENTION (labelled on screen) |
| **₹5,000/mo**, **₹60,000/yr** | 1.1, 2.1, 2.2, 5.4, 6.6 | §1.1 "₹30,000 × 20% = ₹5,000/mo … say 'if you put away five thousand a month'" | derived from two conventions — VO obeys the wording rule |
| **₹18,353 – ₹24,217** monthly earnings | 6.2 | §1.1 "Regular wage/salaried avg monthly earnings — ₹24,217 men / ₹18,353 women, PLFS Annual Report 2025, PIB" | HARD |
| **₹7 of every ₹100** of national income saved | 6.3 | §1.1 "Net household financial savings — 7.0% of GNDI, FY25, RBI Annual Report May 2026" | HARD |
| **7.1%** — PPF / 3-yr post-office TD | 2.4, 2.5, 3.2, 3.6, 5.5 | §1.2 "**PPF — 7.1% p.a.**, Q2 FY27" + "Post Office Time Deposits … 3yr **7.1%**" | HARD (the staging note's named "honest rate to build on") |
| Small-savings rates **unchanged, 9 straight quarters** | 4.10 | §1.2 "Small-savings rates unchanged for Q2 FY2026-27 … 9th/10th consecutive quarter, notified 2026-06-30" | HARD **at nine** — audit re-fetch 2026-07-31 (Upstox, quoting the Finance Ministry) reads "extending the status quo for the **ninth** consecutive quarter". Staging hedged 9-or-10; the draft had hardened it to ten, which no re-fetched source states. Corrected down. |
| **~12%/yr** equity, spoken "क़रीब बारह परसेंट" | 2.6, 2.7, 3.2, 3.6, 5.5 | §1.2 "Nifty 50 TRI since inception — 12.41% p.a." + "must say 'historically, roughly twelve percent' and never a decimal" | **SOFT** — shape only, no decimal spoken or shown |
| **₹500/mo minimum · ₹250** | 6.9 | §1.1 "SIP minimum — ₹500/mo; ₹250 'Chhoti SIP', AMFI" | HARD |
| First lakh: **20 / 19 / 18 months** | 1.1, 2.3, 2.5, 2.6 | §1.3 table, row "Months to the **first** ₹1 lakh — 20 / 19 / 18" | COMPUTED — `ILLUSTRATIVE` foot on every frame that shows one |
| Second lakh: **20 / 17 / 15 months** | 3.2 | §1.3 "Months for the **second** lakh — 20 / 17 / 15" | COMPUTED |
| Tenth lakh: **20 / 9 / 7 months** | 1.2, 3.5, 3.6 | §1.3 "Months for the **tenth** lakh (₹9L→₹10L) — 20 / 9 / 7" | COMPUTED |
| **2 months** vs **13 months** — the thesis | 2.7, 3.7, 4.4, 9.5, 9.6 | §1.3 "a 12.4% return buys you **two months** on the first lakh (20 → 18). On the tenth it buys you **thirteen** (20 → 7)" | COMPUTED — the staging note's own framing |
| Crossover **≈ ₹8.5 lakh at 7.1% · ≈ ₹4.8 lakh at ~12%** | 5.5 | §1.3 "Crossover … ≈ ₹8.5 lakh at 7.1%, ≈ ₹4.8 lakh at 12.4%" | COMPUTED |
| Crossover is **~₹5 lakh, NOT ₹1 lakh** | 5.6, 5.8, 5.9, 7.7, 9.7 | §1.3 "⚠️ **Do not call ₹1 lakh the crossover** … the crossover is roughly **₹5 lakh**" + §4 "Say 'the first lakh is where the *habit* takes over'" | the flagged error — corrected explicitly, three times |

### Deliberately NOT used (so the audit stage doesn't rediscover them)

- **Every dollar figure, every US institution, and the Munger quote.** §2 of
  facts-staging is the other cut's block. The quote is SOFT (no primary reachable) *and*
  denominated in a foreign currency; a ₹-cut carrying it fails twice. The dollar glyph
  appears nowhere in this file, not even inside a claim ID.
- **"₹1 lakh is where compounding takes over."** §4 "Do not claim". Chapters 5, 7 and 9
  say the opposite on purpose.
- **Any months figure spoken as a statistic.** §4. Every one carries its condition in the
  same sentence and an `ILLUSTRATIVE` foot in the same frame.
- **12.41% / 12.44% / any equity decimal.** §1.2 — both NSE PDFs 403'd, figures read via
  a search index only. Shape only, spoken and on screen.
- **Bank RD/FD rate tables (SBI 6.25–6.4%, ICICI 6.5%, HDFC, Axis, Kotak) and the SBI
  2.50% savings rate.** §1.2 tags both SOFT — a single aggregator, every issuer page
  403'd. Naming a bank's rate would also make a named product the evidence, which the
  persona rule forbids. The one rate this cut speaks is the HARD 7.1%.
- **NSC 7.7 / SCSS 8.2 / SSY 8.2 / KVP 7.5 / POMIS 7.4, and the 1/2/5-yr TDs.** SOFT,
  single-source, not needed — a rate ladder would also break the two-type-sizes rule.
- **"The median Indian has ₹X saved" style balance statistics.** §3 rejects the
  equivalents; no Indian source of that shape was found at all.
- **A named fund, index fund, AMC, bank, app or platform.** Persona rule. PPF, the
  post-office time deposit and the ₹500 monthly minimum appear as **price evidence only**,
  and the 6.9 foot says so on screen.

---

## Build handoff

1. **`assets/voice/hindi-lines.json` = 86 entries keyed `1.1 … 9.10`**, containing
   **only** the `>` VO strings above — no markdown, no cue text, no on-screen text.
   Devanagari, verbatim. **Slice the source file; never retype.** Gate the extraction
   with a byte-for-byte reconstruction check against this file before generating audio
   (the firaun re-lining rule, `long_form_scripting.md` §1.7).
2. **TTS** via `tools/tts/elevenlabs_tts.py`, voice `HTUuC7OeeEt6OL5fViVe` (Harsh),
   `eleven_multilingual_v2`, style 0. **86 calls** of the run's 200; the `-en` cut needs a
   comparable number, so do not burn retries casually.
3. **Timing is by construction.** One line = one clip = one scene. Scene span =
   `probe(clip) + gap_after(line)`, with `GAP_INTRA = 0.20` and `GAP_CHAPTER = 0.80`
   (firaun `build.py` gap model). Never hand-edit a duration; regenerate all four homes of
   the timing numbers from one source.
4. **Recount the characters programmatically** and re-check the total against
   510 × 12.5 = 6,375 before locking. The table above is a budget estimate at ±10%.
   ⚠ **Pin the rounding convention before you compute anything** (fin-audit hi/1).
   Every months-to-milestone integer in `facts-staging.md` §1.3 is **round to the
   nearest month**, not the first month at or above the target. Re-derived here at
   ₹5,000/mo, ordinary monthly annuity: first lakh at ~12% reaches ₹98,358 at month 18
   and ₹1,04,374 at month 19 → nearest is 18, ceiling is 19. Same one-month split on
   the second lakh (17 vs 18 at 7.1%, 15 vs 16 at ~12%) and the tenth (9 vs 10 at
   7.1%). The VO is locked to the NEAREST-month set (20/19/18 · 20/17/15 · 20/9/7).
   A build that uses `ceil` will silently put a different integer on screen from the
   one the voice says, and the voice cannot be re-cut without re-paying TTS.
5. **Images: one per line, 86 scenes, zero photo-free frames** (`photo_free_scene_ratio`
   = 0, creator rule 2026-07-28). Three lines are marked `hold` — 1.2 (holds 1.1), 1.6
   (holds 1.5) and 5.3 (holds 5.2) — and each pair must run **ONE continuous zoom** across
   both scenes, never a self-dissolve (creator rule, firaun 2026-07-23). ⚠ **The 5.2+5.3
   pair totals ~9.2s of a single photograph and breaches `max_scene_seconds` 9.0.** Fix it
   at build time by giving 5.3 a second, tighter crop of the same source rather than the
   identical frame. The other two pairs are 8.0s and 8.6s and pass.
   md5 the asset ledger: no image may repeat across videos or channels, and the shipped
   cuts have already burned `hand tapping phone banking app` and `young indian man … phone`.
6. **The `.swiss` divergences from `design-finance-blockframe.md` are load-bearing** — see
   §8 of `11-swiss-vignelli.md`: radii → 0, rotation → 0, `text-shadow` off, four-layer
   scrim deleted (hard-edged tone block on a column line instead), per-scene `--tint`
   retired, grade to ~`grayscale(0.85)`, Ken Burns halved inside the band, `back.out` /
   `breathe` / `drift` unused, every scene flush left.
7. **Reversed type is measured, not assumed.** The 9 `ap R` scenes put type on the
   photograph. Measure the left third's mean luminance at fetch time and reject any image
   above 25%; there is no scrim to rescue it.
8. **Anchor cues to word-level timings** (faster-whisper), not character-offset
   interpolation — the drift is worst on Hindi.
9. **Chapter-wise production.** Build, proof and re-render chapter by chapter; concat and
   final-render only after all nine chapters are locked.
