---
summary: Hindi/India script for «The passive-income number». MEDIUM tier, per-line chapters — 81 single-sentence VO lines across 7 chapters, 6,422 chars ≈ 8:34.5 against the 510s target. Style E (teacher + curiosity), adopted 2026-08-07. ATTEMPT 3 (2026-08-08) is a TARGETED EXPANSION AND NOTHING ELSE — the rate key moved from 13.03 (measured on the retired Harsh voice) to a measured 14.281 on Amrut, which re-opened budget the cut was always owed; TEN lines in chapters 3–7 were lengthened by 503 characters and the other 71 are byte-identical. No new lines, no new scenes, no new facts, no changed register, no changed chapter boundaries, no changed rung ladder, no changed number. INR only. Standard Hindi, voice Amrut Deshmukh. Hero: ₹1 crore at a 3.0% withdrawal rate = ₹25,000/month, beside the PLFS regular-salaried average ₹24,217. Every number traces to videos/passive-income-number/facts-staging.md.
updated: 2026-08-08
source: run.json creator brief + constraints + style_decision (2026-08-07) · studio/voice-tests/passive-income-number/style-E-teacher-curiosity.txt (ch1+ch2, creator-approved, verbatim) · script-hi.md attempts 1–2 (facts, structure, chapter boundaries, rung ladder, cues — carried unchanged) · studio/videos/passive-income-number-hi/assets/voice/timing.json (the 81 MEASURED clip durations + programmatic char counts this attempt is budgeted on) · tools/format.json cuts.hi.chars_per_second 14.281 (measured 2026-08-08 on Amrut) · facts-staging.md attempt 1 (PARTS A, B, D, E, F) · knowledge/video-studies/passive-income-number.md · knowledge/niches/india-finance-market.md · skills/long_form_scripting.md · script-en.md (REGISTER MODEL ONLY, never a source). Architecture per tools/format.json tiers.medium + chapter_design.
stage: fin-script, cut hi, attempt 3 — TARGETED EXPANSION (10 lines, chapters 3–7, +503 chars)
---

# «वो नंबर, जो हर महीने पैसे देता है» — Hindi / India edition (MEDIUM, per-line chapters)

**Studio project (to build):** `studio/videos/passive-income-number-hi`
**Language:** Standard Hindi, **Devanagari** — channel register locked 2026-07-28
([[../../knowledge/niches/india-finance-market]]). `haryanvi-hindi-script-style.md` is not
the guide for this lane and was not read.
**Voice:** ElevenLabs **Amrut Deshmukh** `LHJy3mhZWsvhUjy0zUM1`, `eleven_multilingual_v2`,
style 0. ⚠ **Voice changed 2026-08-07** (was Harsh) — creator pick after an A/B listening
test, chosen to match this teacher register (`format.json cuts.hi._voice_note`).
**On-screen text:** English / Hinglish. **Title + description:** Roman script.
**Architecture:** `blockframe-9` (`format.json architecture_lock`) + the **chapter archetype
layer** (A plate · B figure · C ledger · D band). **MEDIUM tier → per-line chapters** — none
of the 9-segment blockframe constants apply; `lines: 9` on the registry entry is a SHORT-tier
constant. **One line = one TTS clip = one scene = one exact timeline anchor.**

**Engine rule:** digits are **spelled out** in every VO line (bare Latin digits are a
coin-flip English reading in ElevenLabs). On-screen numerals carry the exact figures,
`Intl.NumberFormat("en-IN")` grouping (`₹1,00,00,000`).

**Persona rules (YouTube 2026 AI carve-out):** no host persona, no first-person expertise,
no fund / AMC / bank / app / scheme pick. **मैं** and **हम** appear nowhere in the VO —
style E's teaching signposts are **imperatives** (`ध्यान दीजिए`, `समझिए`, `हिसाब सामने कीजिए`,
`देखिए`), never a narrator claiming to teach. The post-office monthly-income scheme and the
small-savings rates appear **only as published price evidence**. Second person throughout.

---

## ⚠ ATTEMPT 3 — what changed, and the one reason it changed

**This is an EXPANSION, not a restyle and not a rewrite.** Register, structure, chapter
boundaries, beat order, the rung ladder, every fact and every number are attempt 2's, which
passed `fin-audit`. Chapters 1 and 2 were **not touched at all**.

**The reason is arithmetic.** Attempt 2 was budgeted at **13.03 chars/s** — a key measured on
**Harsh**, the retired voice. The voice is **Amrut**, measured on 2026-08-08 at **14.281 c/s**
across all 81 rendered clips (5,919 chars ÷ 414.454 s of audio), and `format.json` was
corrected. At the true key the tier's own budget is

```
(510 − 81 × 0.8) × 14.281 = 445.2 × 14.281 = 6,357 chars
```

so attempt 2's 5,919 characters were **438 short of the length the cut was always meant to
be**, and the voiced result measured **479.259 s = 7:59.259**. YouTube places mid-roll ads
only at **8:00 or longer**, and MEDIUM tier exists in this pipeline precisely to earn
mid-roll — the cut was forfeiting it by **0.741 s**.

**Creator decision (2026-08-08):** expand to the 510 s target. This draft adds **503
characters across exactly ten lines**, landing at **6,422 chars → 514.5 s (8:34.5)**.

### The five rules the expansion obeyed

1. **No new lines, no new scenes.** 81 lines in, 81 lines out. A new line would mean a new
   photograph and a new storyboard row, and the hi storyboard has not been built yet.
2. **Concentrated, not spread.** Every touched line must be re-voiced at one ElevenLabs call
   each. `run.json budget.elevenlabs_calls` is **290 of 350**; ten lines is 300. Touching all
   81 would breach the ceiling.
3. **Chapters 1–2 untouched.** They are the creator-approved style-E reference verbatim, and
   the hook gate measured on 1.3 at **8.682 s** is a result this attempt must not disturb.
4. **`max_scene_seconds` 9.0 respected on every touched line** — see the headroom table below.
   **6.13 already breaches at 9.812 s and was deliberately not touched.**
5. **Content, not padding.** Every addition is a worked step, a concrete comparison or a
   signposted clarification. Where a line could only be padded, it was left alone.

### The ten lines, and what each one now teaches

| line | before | after | Δ | modelled scene s | what the added text does |
|---|---|---|---|---|---|
| **3.5** | 65 | 110 | +45 | 8.08 | Says out loud that the **bill did not shrink** — only the pocket changed. Kills the one misreading the rung ladder invites, and rhymes with 2.13. |
| **3.6** | 65 | 117 | +52 | 8.20 | Names the mechanism the whole ladder rests on: the rate is **one stamp pressed on every rung**, and the only thing that moves is the corpus. On-metaphor with the frame's stamp. |
| **4.4** | 61 | 119 | +58 | 8.15 | **Speaks the 3.0% rate inside a derived-income line** (it was frame-only before — see the rate check), then marks rung three as the first rung that pays a **need**, not a convenience. |
| **4.9** | 63 | 117 | +54 | 8.06 | The tax line was one clause and stopped. It now states the practical consequence with **no figure**: what reaches the hand is a little less than the ledger. B.2's LTCG row is SOFT, so still no number. |
| **5.3** | 57 | 113 | +56 | 7.54 | The strongest addition in the draft: **the division at a bigger rate is not wrong** — it is the tank that fails. Converts "stop here" from an assertion into a reason, and hands off directly into 5.4's tank callback. |
| **5.12** | 61 | 105 | +44 | 7.96 | Explains **why** four percent dominates the internet — repetition, until a paper starts sounding like a rule. Primes 5.13's provenance beat. |
| **5.17** | 73 | 121 | +48 | 8.42 | The inflation line stated a rate and stopped. It now states the **mechanism**: next year the same ration costs more, so the withdrawal has to rise — which is why the surviving rate is smaller. |
| **6.4** | 53 | 105 | +52 | 7.81 | **Closes the chapter-1 open loop out loud** — "the specific number held back at the start is this one" — at the exact moment it pays off. |
| **6.8** | 55 | 104 | +49 | 7.95 | Says why the comparison beat exists at all: a number alone means nothing, meaning comes from what sits next to it. Also fills the one frame in the cut with an empty `stmt:`. |
| **6.11** | 66 | 111 | +45 | 7.95 | Hardens the guard rail: **no date, no promise** — only a sum and a rate. Strengthens `no_unsourced_retire_early` rather than merely restating it. |
| | **619** | **1,122** | **+503** | | |

### Why those ten and not ten others

`timing.json` gives a **measured** duration for all 81 clips, so headroom is a fact here, not
an estimate. The ten chosen are all lines whose measured scene duration sat **below 4.9 s**
(i.e. 4+ seconds of headroom against `max_scene_seconds` 9.0) **and** whose beat had a real
missing step. Lines with the biggest headroom that were still left alone, and why:

- **5.6** («बारह परसेंट चेतावनी है», 3.99 s) — the punch of that line **is** its brevity.
- **7.8** (the single CTA, 4.74 s) — a longer CTA is a worse CTA.
- **6.5** (the hero corpus, 4.51 s) and **6.1 / 4.1 / 3.1** (rung openers) — a rung opener can
  only be padded; the teaching in a rung lives in the lines after it.
- **All of chapters 1 and 2** — locked by rule 3 above.

### The headroom arithmetic, stated so it can be checked

Each touched line was modelled as **measured base duration + (added chars ÷ 14.281) + 0.8 s
padding**, i.e. the known measurement for the text that already exists plus the *cut mean*
for the text that does not yet exist. That is deliberately the conservative half of the
evidence: all ten of these lines measured **16–19 c/s** individually (they are short, clean,
low-pause lines, which is exactly why they had headroom), so pricing their new text at the
14.281 mean over-states every one of them.

> ⚠ **The 117-character flat ceiling is a screen, not a verdict.** At 14.281 c/s,
> `max_scene_seconds` 9.0 minus 0.8 s of padding is 8.2 s of VO = **117 characters**, and
> **4.4 (119) and 5.17 (121) sit just above it**. The measurement is what governs, and it
> cuts both ways on this cut: **2.4 is 107 chars and measured 7.053 s** (15.17 c/s — the flat
> model over-charged it by a full second), while **6.13 is 103 chars and measured 9.012 s**
> (11.43 c/s — the flat model under-charged it into a real breach). Character count predicts
> duration to about ±20% per line on this voice. **Re-measure every touched clip after TTS;
> that number, not this one, decides whether a scene needs a second `data-framings`.**

---

## What style E is, and what it did NOT change

Creator decision `run.json.style_decision` (2026-08-07): style E for both cuts, and this
cut's voice to Amrut. **That was a restyle, not a rewrite.** Every fact, chapter boundary,
beat order, rung and number is attempt 1's, which passed `fin-audit`. Four moves changed the
writing:

1. **The open is a what-if, not a statement.** The phone's *silence* is the promise; its
   *single buzz* is the payoff. (Was: «एक मंगलवार की सुबह। अलार्म नहीं बजा।»)
2. **Signposted teaching** — *यहाँ ध्यान दीजिए · इसे ऐसे समझिए · हिसाब सामने कीजिए · अब देखिए कि …
   क्या आता है · यह मानिए · वापस उसी टंकी पर चलिए*. **12 signposts across 81 lines**, all
   imperatives so no first person can enter. They mark structure, never fill space.
3. **The tank is load-bearing and pays off twice.** 2.3–2.4 plant it — a tank filled slowly
   over years, one tap in (SIP), one tap out (SWP), and the only question that matters is how
   much can be drawn each year without emptying it. **4.7–4.8 is the first callback** (the
   money comes out of *your own tank*, which is why the outgoing tap is kept narrow);
   **5.4–5.5 is the second** (at ten or twelve percent it is not the growth coming out, it is
   the capital). So the rate-trap beat at the halfway mark is a **return to a picture the
   viewer already holds**, not a new idea at the drop zone. **Attempt 3's edit to 5.3 hands
   into that callback one clip earlier**, which is the only structural effect the expansion
   has anywhere in the cut.
4. **Stepped arithmetic.** Every rung is corpus-and-rate → yearly → monthly, each on its own
   line. No calculation is compressed into one mouthful.

**Chapters 1 and 2 are `studio/voice-tests/passive-income-number/style-E-teacher-curiosity.txt`
verbatim** — 21 lines, creator-approved, not one character altered, in attempt 2 or attempt 3.

> ⚠ **`script-en.md` was read for REGISTER ONLY, never as a source.**
> `market_rewrite_not_translation` holds in both directions: the en cut is a US video built on
> US literature at US rates, and nothing in it — not a figure, not an institution, not a bill,
> not a photograph — crosses into this file. This cut is SIP / SWP / ₹ / India, sourced from
> PARTS A.3, B and D of `facts-staging.md`. **PART C contributed nothing.**

---

> ### ⚠ THE SIX THINGS THAT MUST NOT ENTER THIS CUT
> 1. **NEVER a corpus figure without its withdrawal rate in the SAME VO breath.** Not "stated
>    once at the start" — *every rung, every time*. Dark Ledger states four percent once and
>    then ships six bare numbers; that is the observed failure this cut exists not to repeat.
>    Every frame carrying a corpus carries the rate — and, per the 2026-08-07
>    `derived_income_carries_assumption` extension, **so does every "what X buys" frame**,
>    because the monthly figure is the corpus's output and therefore the promise the video
>    actually makes.
> 2. **NEVER convert a corpus into an age.** No "retire early", no "quit your job", no age
>    anywhere in this cut at all. 6.11 says out loud that this is a sum about money and a
>    rate, not about an age — and after attempt 3 it also refuses a *date* and a *promise*.
> 3. **NEVER a return spoken as an expectation.** Three percent is a *chosen* number (2.6,
>    2.7); the growth rates in 6.15–6.16 are «मानी हुई बढ़त» and land with «दोनों हिसाब हैं,
>    वादे नहीं».
> 4. **NEVER the banned word.** The English payout word, its Devanagari transliteration and
>    any inline English use are forbidden in script, on-screen text, title and tags
>    (`hi_currency_framing`). **The live trap:** the index's total-return measure is *defined*
>    using that word, so this cut **never explains that measure at all** — 6.16 quotes only
>    the shape, «क़रीब बारह परसेंट».
> 5. **NEVER the rupee's counterpart glyph, a foreign institution, or a cross-market
>    conversion.** ₹1 crore is not any foreign figure and no line, frame or chart may imply it.
> 6. **NEVER four percent as advice.** It appears only as *the imported rule this video
>    corrects*, always beside India's three percent, always with its provenance (5.12–5.15).

---

## Title options (Roman script — per the title-language rule)

1. **Har Mahine ₹25,000 Ke Liye Kitna Paisa Chahiye — Poora Hisaab**
   *(recommended — the monthly figure is the searchable promise, and it is the one number the
   video actually pays off)*
2. ₹1 Crore Se Har Mahine Kitna Milega? 3% Ka Seedha Hisaab
3. Passive Income Ka Asli Number — Aur Wo 4% Wala Rule Jo India Ke Liye Nahi Hai

⚠ Packaging carries the abstraction, the script carries the bills (study conclusion 6 — both
twins do exactly this). `passive income` and `financial freedom` belong in the
title/description/tags; the VO says «बिजली का बिल» and «राशन». **Unverified** — the vidIQ
packaging pass is still owed and only 13 credits remain (`run.json.owed`).

---

## Chapters (ship these as YouTube chapters — study conclusion 10)

Starts are **measured** for chapters 1 and 2 and for every untouched line, and modelled only
across the ten expanded lines.

| # | Chapter | starts | % | lines | chars | runtime |
|---|---|---|---|---|---|---|
| 1 | Wo din | 0:00 | 0.0% | 8 | 553 | 42.5s |
| 2 | Pehli seedhi — ₹10 lakh | 0:42 | 8.3% | 13 | 996 | 81.5s |
| 3 | Doosri seedhi — ₹20 lakh | 2:04 | 24.1% | 9 | 753 | 60.2s |
| 4 | Teesri seedhi — ₹40 lakh | 3:04 | 35.8% | 10 | 814 | 64.1s |
| 5 | **12% ka jaal, aur 3% vs 4%** (the ~50% correction beat) | 4:08 | 48.3% | 17 | 1,386 | 110.3s |
| 6 | **Chauthi aur paanchvi seedhi — ₹1 crore** (the hero) | 5:59 | 69.7% | 16 | 1,339 | 111.6s |
| 7 | Wapas usi din par | 7:50 | 91.4% | 8 | 581 | 44.2s |
| | | | | **81** | **6,422** | **514.5s** |

---

## Timing budget

Hindi narration = **14.281 chars/s** (`format.json cuts.hi.chars_per_second` — the **FLAT
delivered rate on Amrut, pause silence included**, measured 2026-08-08 across all 81 clips of
this cut: 5,919 chars ÷ 414.454 s). MEDIUM charges **0.25 s lead-in + 0.55 s tail per line**
(`tiers.medium`) = **0.8 × 81 = 64.8 s** of inter-line padding.

**Budget formula.** Padding is not audio, so it comes out of the target *before* the rate is
applied:

```
(510 − lines × (lead_in + tail)) × chars_per_second
(510 − 81 × 0.8) × 14.281 = 445.2 × 14.281 = 6,357 chars
```

This draft is **6,422 chars — +1.0% over budget, landing at 514.5 s (8:34.5) against the
510 s target, +0.9%.** Comfortably inside the ±5% band, and **34.5 s past the 8:00 mid-roll
threshold**, which is the entire point of the expansion.

> ⚠ **Do NOT use `target_seconds × rate`.** 510 × 14.281 = 7,283 ignores per-line padding and
> would run `7,283 ÷ 14.281 + 64.8 = 575 s` — **12.7% long**. `cuts.en._chars_per_second_trap`
> records why the wrong formula survived (a wrong rate and a wrong formula cancelled) and
> states the ordering rule: **fix the formula first, raise the key second.** Both halves are
> now RESOLVED for `hi` as well: the formula was corrected 2026-08-07 and the key was raised
> 13.03 → 14.281 on 2026-08-08 from an 81-clip measurement. **Attempt 3 is the second half of
> that correction landing in the script.**

| Ch | lines | chars | VO | + padding | runtime | starts |
|---|---|---|---|---|---|---|
| 1 | 8 | 553 | 36.1s | 6.4 | 42.5s | 0:00 |
| 2 | 13 | 996 | 71.1s | 10.4 | 81.5s | 0:42 |
| 3 | 9 | 753 | 53.0s | 7.2 | 60.2s | 2:04 |
| 4 | 10 | 814 | 56.1s | 8.0 | 64.1s | 3:04 |
| 5 | 17 | 1,386 | 96.7s | 13.6 | 110.3s | 4:08 |
| 6 | 16 | 1,339 | 98.8s | 12.8 | 111.6s | 5:59 |
| 7 | 8 | 581 | 37.8s | 6.4 | 44.2s | 7:50 |
| | **81** | **6,422** | **449.7s** | **64.8s** | **514.5s** | |

**Pace:** 514.5 / 81 = **6.35 s average scene** (`target_scene_seconds` 6.5,
`max_scene_seconds` 9.0).

### ⚠ The scenes that run long — measured, not estimated

`check_build` fails any scene holding one photograph past **9.0 s**. Every figure below is
`probe(clip) + 0.8`, measured off the rendered clips, except the four marked *mod.* which are
`measured base + added chars ÷ 14.281 + 0.8`.

| scene | scene s | source | action |
|---|---|---|---|
| **6.13** | **9.812** | measured | ⚠ **THE ONLY REAL BREACH IN THE CUT.** Deliberately NOT expanded. **Needs TWO `data-framings`** — wide on the tape against the plank, then a push to the short end. Build handoff item 7. |
| 6.9 | 8.741 | measured | inside 9.0 with 0.26 s. Untouched. Watch it if the clip is ever re-voiced. |
| 2.13 | 8.506 | measured | inside. Untouched. |
| 3.7 | 8.506 | measured | inside. Untouched. |
| 5.17 | 8.419 | *mod.* | expanded +48. Re-measure. |
| 3.6 | 8.203 | *mod.* | expanded +52. Re-measure. |
| 6.8 | 8.175 | *mod.* | expanded +49. Re-measure. |
| 1.6 | 8.167 | measured | inside. Untouched (chapter 1 is locked). |
| 4.4 | 8.152 | *mod.* | expanded +58. Re-measure. |
| 5.10 / 6.3 | 8.088 | measured | inside. Untouched. |
| 3.5 | 8.078 | *mod.* | expanded +45. Re-measure. |
| 4.9 | 8.055 | *mod.* | expanded +54. Re-measure. |

> ⚠ **The attempt-2 exception on 2.4 is VOID and must not be carried forward.** That draft
> predicted 107 chars → 9.01 s from the flat model and ordered two `data-framings` for it.
> **It measured 7.853 s.** One framing is correct there. The two-framings treatment belongs to
> **6.13**, which the same flat model had predicted at 7.9 s and which actually measured 9.812.
> This is the single most useful thing the voiced pass taught, and it inverts the instruction
> the storyboard would otherwise have been handed.

### ⚠ Register note for fin-voice — the key is now MEASURED, and what is still owed

The attempt-2 register note is superseded. It reasoned from a **118.0 s continuous reference
read** that Amrut ran ≈13.09 c/s and that 13.03 therefore stood. That was wrong by **9.6%**,
and the reason is recorded in `format.json cuts.hi._voice_note`: **a continuous read carries
inter-sentence pause INSIDE the audio; per-line clips push that same pause out into
`lead_in + tail`, where it stops counting as speech.** The same 21 lines ran **118.0 s
continuous vs 107.20 s as per-line clips.**

- **14.281 c/s is measured**, 5,919 chars ÷ 414.454 s, all 81 clips, this cut, this voice.
- The drift against 13.03 was **ONE-SIDED — 71 of 81 lines short against expected** — which is
  this repo's documented signature of a wrong key rather than noise (`cuts.en._chars_per_second_trap`;
  en showed 78/78). Two-sided drift is a roughly correct key.
- **Still owed after this re-voice:** the ten re-cut clips are the first Amrut evidence on
  *newly written* style-E text rather than on text that had already been read once. Re-measure
  the flat rate across the new 81 and record it beside 14.281. `rate_key_en_followup` found
  style E ran ~1.5% pause-heavier than its key predicted, so a small negative drift on these
  ten is expected and is not a defect.
- **Measure the SHAPE, not just the size.** If the ten new clips all drift the same way,
  14.281 is already stale for freshly written text. If they scatter, it is fine.

### The hook gate — MEASURED, and untouched by attempt 3

Chapter 1 was not edited, so every number here is unchanged from the voiced pass.

| | modelled (attempt 2) | **MEASURED (fin-voice, silencedetect)** |
|---|---|---|
| **The payoff promise** — money arrives, before noon, in your account (**1.3**) | onset ≈10.4 s, close ≈14.7 s | **onset 8.682 s · close 11.294 s** |
| **The number, named and withheld** (**1.5**) | ≈22.9 s | **18.299 s** |

**The gate is measured on the promise, and the promise is 1.3** — the same object the en cut's
gate was measured on (`hook_gate_en.measured_onset_seconds` 9.571 for *"money is deposited into
your account"*). The gate clears with **6.32 s of headroom**, better than the model and better
than the en cut's own 9.571 s.

⚠ **The tracked risk stands and attempt 3 does not touch it.** The number-naming clause moved
from style A's 15.0 s to 18.299 s. That is 3.3 s later, not the 7.9 s the model feared, and the
format twins land their number at 0:40–0:54 of an 8–11 minute cut. **If hi retention falls off
before 0:30, this is still the first thing to re-test** — and re-testing it means editing
creator-approved chapter-1 copy, which is a creator decision, not a stage decision.

### Where the other retention beats land (recomputed on the expanded timeline)

- **Rung one's corpus at 2.8 = 1:27.2 (16.9%)**, its monthly figure at 2.10 = **1:37.9 (19.0%)**
  — inside the 8–25% band with room. Both absolute times are unchanged; only the percentages
  moved, because the denominator grew.
- **The rate trap punches at 5.2 = 4:12.5 (49.1%)** and the tank callback opens at 5.4 =
  **4:25.8 (51.7%)**.
- **The mid-video drop zone (55–65% = 4:43–5:34) now opens on 5.8**, the published post-office
  rate, and runs straight through the ceiling (5.9), the roof (5.10) and into the imported-rule
  takedown (5.12 at **5:13.5, 60.9%**). ⚠ **Flagged honestly, not swallowed:** attempt 2 had
  «बारह परसेंट चेतावनी है» opening the zone at 54.5%; the expansion pushes 5.6 to **4:36.3
  (53.7%)**, about 1.5 s *before* the zone opens. The zone therefore opens on a **reveal**
  (the government's own scheme is capped) rather than on the **warning**. That is still
  tension, not a flat transition — which is what the rule actually asks for — but it is a
  deliberate 0.8-percentage-point trade taken to buy mid-roll, and it is recorded here so no
  later stage reads it as drift.
- **The four-percent provenance opens at 5.13 = 5:21.5 (62.5%)**, still straddling the 5:00
  mark both twins converge on.
- **The hero lands at 6.5 = 6:25.4 (74.9%)** — the ~70% reward beat, unmoved — pays out as
  ₹25,000/month at 6.7 = **6:35.9**, and is validated by the one sourced external statistic at
  6.9 = **6:49.9 (79.7%)**.
- **The callback opens at 7.1 = 7:50.3 (91.4%)**; the **single terminal CTA** is 7.8 at
  **8:29.7 (99.1%)**. **Zero mid-roll CTAs** — third independent confirmation of that line.
- **Mid-roll eligibility: 514.5 s ≥ 480 s, with 34.5 s of margin.** This is the deliverable.

---

## Per-scene timing budget

`chars` → `est s` at **14.281 chars/s**. Add **0.8 s per line** (0.25 lead-in + 0.55 tail,
`tiers.medium`) for scene duration. Character counts are the **programmatic** ones from
`assets/voice/timing.json` for the 71 unchanged lines; the ten expanded lines are marked ★
and hand-counted (±2%), to be recounted by the build. `arch` = chapter archetype
(`format.json chapter_design.archetypes`): **A** plate (opens, hand-offs) · **B** figure (the
point is a number) · **C** ledger (evidence — a bill, a rate card, a paper) · **D** band (the
point is the motion).

| # | chars | est s | arch | | # | chars | est s | arch | | # | chars | est s | arch |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.1 | 55 | 3.9 | A | | 3.7 | 95 | 6.7 | B | | 5.15 | 76 | 5.3 | C |
| 1.2 | 56 | 3.9 | D | | 3.8 | 71 | 5.0 | C | | 5.16 | 77 | 5.4 | B |
| 1.3 | 57 | 4.0 | A | | 3.9 | 65 | 4.6 | A | | 5.17 ★ | **121** | 8.5 | B |
| 1.4 | 85 | 6.0 | D | | 4.1 | 60 | 4.2 | A | | 6.1 | 54 | 3.8 | A |
| 1.5 | 48 | 3.4 | A | | 4.2 | 72 | 5.0 | B | | 6.2 | 82 | 5.7 | B |
| 1.6 | 87 | 6.1 | D | | 4.3 | 78 | 5.5 | B | | 6.3 | 97 | 6.8 | C |
| 1.7 | 77 | 5.4 | B | | 4.4 ★ | **119** | 8.3 | C | | 6.4 ★ | **105** | 7.4 | A |
| 1.8 | 88 | 6.2 | A | | 4.5 | 84 | 5.9 | C | | 6.5 | 54 | 3.8 | B |
| 2.1 | 66 | 4.6 | A | | 4.6 | 64 | 4.5 | A | | 6.6 | 62 | 4.3 | B |
| 2.2 | 67 | 4.7 | C | | 4.7 | 79 | 5.5 | D | | 6.7 | 76 | 5.3 | B |
| 2.3 | 73 | 5.1 | D | | 4.8 | 78 | 5.5 | D | | 6.8 ★ | **104** | 7.3 | A |
| 2.4 | 107 | 7.5 | D | | 4.9 ★ | **117** | 8.2 | C | | 6.9 | 93 | 6.5 | C |
| 2.5 | 77 | 5.4 | A | | 4.10 | 63 | 4.4 | B | | 6.10 | 74 | 5.2 | B |
| 2.6 | 68 | 4.8 | B | | 5.1 | 48 | 3.4 | A | | 6.11 ★ | **111** | 7.8 | B |
| 2.7 | 79 | 5.5 | B | | 5.2 | 72 | 5.0 | B | | 6.12 | 91 | 6.4 | B |
| 2.8 | 68 | 4.8 | B | | 5.3 ★ | **113** | 7.9 | A | | 6.13 | 103 | 7.2 | B |
| 2.9 | 62 | 4.3 | B | | 5.4 | 72 | 5.0 | D | | 6.14 | 65 | 4.6 | A |
| 2.10 | 60 | 4.2 | B | | 5.5 | 58 | 4.1 | D | | 6.15 | 82 | 5.7 | B |
| 2.11 | 83 | 5.8 | C | | 5.6 | 51 | 3.6 | B | | 6.16 | 86 | 6.0 | B |
| 2.12 | 84 | 5.9 | C | | 5.7 | 81 | 5.7 | C | | 7.1 | 65 | 4.6 | A |
| 2.13 | 102 | 7.1 | A | | 5.8 | 76 | 5.3 | B | | 7.2 | 62 | 4.3 | D |
| 3.1 | 66 | 4.6 | A | | 5.9 | 78 | 5.5 | C | | 7.3 | 71 | 5.0 | B |
| 3.2 | 63 | 4.4 | B | | 5.10 | 84 | 5.9 | B | | 7.4 | 77 | 5.4 | A |
| 3.3 | 79 | 5.5 | B | | 5.11 | 82 | 5.7 | A | | 7.5 | 80 | 5.6 | D |
| 3.4 | 87 | 6.1 | C | | 5.12 ★ | **105** | 7.4 | B | | 7.6 | 79 | 5.5 | B |
| 3.5 ★ | **110** | 7.7 | A | | 5.13 | 89 | 6.2 | C | | 7.7 | 84 | 5.9 | A |
| 3.6 ★ | **117** | 8.2 | B | | 5.14 | 103 | 7.2 | C | | 7.8 | 63 | 4.4 | A |

**81 lines · 6,422 chars · 449.7 s VO · +64.8 s padding · 514.5 s (8:34.5).**
★ = expanded this attempt (10 lines, +503 chars). The other 71 are byte-identical to the
voiced cut and **must not be re-voiced**.

**Archetype sequence** (rhythm, not variety for its own sake) — **unchanged, the expansion
touched no archetype**:
ch1 `A D A D A D B A` · ch2 `A C D D A B B B B B C C A` · ch3 `A B B C A B B C A` ·
ch4 `A B B C C A D D C B` · ch5 `A B A D D B C B C B A B C C C B B` ·
ch6 `A B C A B B B A C B B B B A B B` · ch7 `A D B A D B A A`.
Ch5 holds **C** across 5.13–5.15 deliberately: three documents are one argument (the American
paper, what it excluded, the Indian paper), and varying the layout there would break the only
through-line the chapter has.

### Role colour semantics (one role colour per scene, ever) — unchanged

- `--fund` green (`#22c55e`) = **the corpus doing its stated job at the stated rate** —
  **2.10, 2.12, 3.3, 4.3, 6.2, 6.7, 6.10, 7.6**.
- `--warn` red (`#ef4444`) = **the thing that eats the corpus** — the too-high withdrawal rate
  (5.2, 5.4, 5.5, 5.6), the imported rule and what it excluded (5.12, 5.14, 6.12, 6.13), the
  failure edge (5.16), the honesty beat (4.7), the internet's inflation of it (3.8).
- `--target` amber (`#f59e0b`) = **a rate under examination** — **2.3, 2.4, 2.6, 2.7, 3.6,
  4.8, 4.10, 5.8, 5.10, 5.15, 5.17, 6.5, 6.15, 6.16**.
- `--pop` orange (`#ff5c39`) = the CTA block, **once**, at 7.8.

**Thesis check:** green never lands on a figure that lacks its rate, red never lands on
India's 3.0%, and amber never lands on the imported 4%.

---

# THE SCRIPT

> **VO block rule.** Every `>` quoted line below is a VO line, verbatim, and is the only thing
> that goes to TTS. Everything in backticks is a production cue and is never spoken.
> **Slice these strings — never retype them.** Retyping Devanagari silently swaps characters
> (nukta, chandrabindu) and the swap is inaudible until the render.
>
> ⚠ This file carries guard blockquotes as well as VO lines, so a bare `^> ` grep sweeps in
> junk — **extract by the `**N.M**` line key**, exactly as fin-voice did on the en cut.
>
> ⚠ **ATTEMPT 3 INTEGRITY GATE — run this BEFORE any TTS call.** Ten lines changed. Diff the
> 81 extracted strings against the existing `studio/videos/passive-income-number-hi/assets/voice/<id>.txt`
> sidecars, which are byte-exact records of what was voiced. **Exactly ten ids may differ:
> 3.5 · 3.6 · 4.4 · 4.9 · 5.3 · 5.12 · 5.17 · 6.4 · 6.8 · 6.11.** Any *other* id that differs
> is a transcription defect introduced by this rewrite (this attempt could only be delivered
> as a whole-file write) — **restore that line from its sidecar and do not spend a call on
> it.** `tools/tts/batch.py` already performs this comparison on resume and prints REGEN per
> changed line, so the check is free: a resume that prints eleven or more REGENs must be
> stopped, not continued.
>
> **The rate rule, mechanically:** every frame whose `num:` or `stmt:` carries a corpus **or a
> derived monthly income** also carries its rate in that same frame, and the VO line speaks
> the rate in the same sentence wherever the line is not creator-approved verbatim.

---

## Chapter 1 — वो दिन (WHAT-IF COLD OPEN · second person · no greeting, no number)

*Study conclusion 1: two unrelated operators, near-verbatim, both breakouts — wake → no alarm
→ coffee → window → phone → money that arrived while you slept. Style E keeps the payload and
changes the grammar: it is a **what-if**, the phone's **silence** is the promise, its **single
buzz** is the payoff. The number is NAMED and WITHHELD (twin B's form), never announced (twin
A's).* **⚠ Creator-approved verbatim — do not edit any VO line in this chapter. Attempt 3
touched nothing here.**

**1.1**
> सोचिए, एक ऐसा दिन जिसमें आपका फ़ोन एक बार भी नहीं बजता।

`[arch A | img: a phone lying face-down on a bedside table in a quiet Indian bedroom, screen dark, first light through a curtain, no people | bar: IMAGINE ONE DAY | stmt: The phone does not ring once.]`

**1.2**
> न अलार्म, न ऑफ़िस का कॉल, न काम की याद दिलाता कोई मैसेज।

`[arch D | img: an unlit bedside alarm clock face-down beside the bed, hard morning shadow, nothing switched on | bar: NOTHING ASKS FOR YOU | stmt: No alarm · No office call · No work reminder | cascade 3 items, 0.6s gap]`

**1.3**
> और उसी दिन, दोपहर से पहले, आपके खाते में पैसे आ जाते हैं।

`[arch A | img: a kitchen counter in late-morning light, a steel glass and a folded newspaper, nobody in frame — ONE continuous zoom across 1.3 and 1.4 | bar: BEFORE NOON | stmt: Money lands in the account. | ⚠ THE PROMISE — the hook gate is MEASURED on THIS clip: onset 8.682s, close 11.294s against a 15s gate]`

**1.4**
> यहाँ ध्यान दीजिए — फ़ोन उस दिन सिर्फ़ एक बार बजता है, और वो पैसे आने की ख़बर होती है।

`[arch D | img: the same counter, tighter — the phone now face-up beside the glass, notification glow, screen text illegible, no face | bar: ONE BUZZ | stmt: That one buzz is the money arriving. | lottie candidate: phone-notify-credit (already in the library) — re-tint; the card carries NO figure, the beat is the buzz. ⚠ the card MUST carry the ₹ glyph or sound-off it reads "a notification arrived", not "money arrived" (recorded ch1 blocker)]`

**1.5**
> आप अमीर नहीं हुए। आप एक ख़ास नंबर तक पहुँचे हैं।

`[arch A | img: a single blank index card squared on a bare wooden table, hard side light | bar: NOT RICH | stmt: One specific number. | foot: The number is withheld until Chapter 6 — this is the open loop, and 6.4 now closes it out loud]`

**1.6**
> उस नंबर का काम एक ही है — आपका बिजली का बिल, आपका राशन और आपका किराया चुपचाप भरते रहना।

`[arch D | img: three household bills fanned on a table — an electricity bill, a kirana slip, a rent receipt, three legibly different documents | bar: ITS ONE JOB | stmt: Electricity · Ration · Rent | cascade 3 items, 0.6s gap | ⚠ all three named bills must be IN FRAME — the superseded build's desk shot showed none of them]`

**1.7**
> इस वीडियो में वो नंबर पाँच सीढ़ियों में खुलेगा, सबसे छोटी सीढ़ी से शुरू करके।

`[arch B | img: the lowest steps of a narrow stone staircase, the top out of frame | bar: FIVE RUNGS | stmt: Smallest rung first]`

**1.8**
> और एक शर्त हर सीढ़ी पर दोहराई जाएगी — वो शर्त, जिसके बिना कोई भी नंबर सिर्फ़ एक वादा है।

`[arch A | img: a rubber stamp resting on an ink pad beside one stamped receipt carrying a percent mark | bar: THE CONDITION | stmt: Every figure ships with its rate | foot: A corpus without its withdrawal rate is a promise, not arithmetic]`

---

## Chapter 2 — पहली सीढ़ी: दस लाख (THE TANK, THE RATE, THEN THE FIRST CORPUS)

*The mechanism in the smallest unit, then rung 1. **2.3–2.4 plant the tank**, which turns
"safe withdrawal rate" from jargon into a picture and is load-bearing again at 4.7–4.8 and
5.4–5.5. The assumption sentence (2.6–2.7) is twin A's best sentence restated without a host
persona: the rate is a declared CHOICE, not a rate the market owes you. The arithmetic is
stepped: yearly (2.9) → monthly (2.10).* **⚠ Creator-approved verbatim — do not edit any VO
line in this chapter. Attempt 3 touched nothing here.**

**2.1**
> तो सबसे पहले एक बुनियादी बात — जमा पैसा हर महीने कुछ देता कैसे है?

`[arch A | img: a locked steel almirah with a small key in the lock | bar: FIRST, THE MECHANISM | stmt: How saved money pays a monthly amount]`

**2.2**
> इसका एक तय नाम है: एस डब्ल्यू पी, यानी सिस्टेमैटिक विदड्रॉअल प्लान।

`[arch C | img: a printed mutual-fund transaction form on a desk, macro, no logo legible | bar: THE NAME | stmt: SWP — Systematic Withdrawal Plan | foot: Terminology as four Indian fund houses define it — not a product recommendation]`

**2.3**
> इसे ऐसे समझिए — एक टंकी है, जिसमें आपने सालों से थोड़ा-थोड़ा पानी भरा है।

`[arch D | img: a plain steel water tank in workshop light, no branding, no legible gauge | bar: THE TANK | stmt: You filled it slowly, over years | colour: --target | lottie candidate: a tank with a level line and two taps — search the library first; the level is decorative and carries NO figure]`

**2.4**
> एस आई पी वो नल है जिससे पानी अंदर जाता है, और एस डब्ल्यू पी वो नल है जिससे हर महीने थोड़ा पानी बाहर आता है।

`[arch D | img: the same tank, one inlet pipe and one outlet tap visible in the same frame | bar: TWO TAPS | stmt: SIP fills it. SWP draws from it. | colour: --target | ⚠ CORRECTED 2026-08-08: this scene MEASURED 7.853s, not the 9.01s the flat model predicted. ONE data-framing is correct here. The two-framings instruction moves to 6.13, which actually breaches.]`

**2.5**
> अब मुख्य सवाल, और यही पूरा वीडियो है — हर साल कितना बाहर निकालना सुरक्षित है?

`[arch A | img: an empty tap over a half-full steel bucket | bar: THE REAL QUESTION | stmt: How much a year is safe to draw out]`

**2.6**
> इस पूरे वीडियो में एक ही मान लिया गया नंबर चलेगा: तीन परसेंट सालाना।

`[arch B | img: a single figure written in pencil on ruled paper, underlined twice | bar: THE WORKING NUMBER | num: 3.0% | foot: Withdrawal rate — the assumption every figure in this video is divided by | colour: --target]`

**2.7**
> यह नंबर कोई वादा नहीं है। यह एक चुना हुआ, सावधान नंबर है, और इसकी वजह आगे आएगी।

`[arch B | hold 2.6's image, ONE continuous zoom across both scenes | bar: A CHOICE, NOT A FORECAST | stmt: 3.0% is chosen. The reason is in Chapter 5. | colour: --target]`

**2.8**
> अब पहली सीढ़ी — दस लाख रुपये, तीन परसेंट सालाना निकालने के हिसाब से।

`[arch B | img: a small steel cash box, lid open, CURRENT-SERIES notes squared inside | bar: RUNG ONE | num: ₹10,00,000 | stmt: AT A 3.0% WITHDRAWAL RATE | foot: ILLUSTRATIVE · corpus times 3.0% divided by 12 — arithmetic, not a forecast | ⚠ CURRENT-SERIES NOTES ONLY — the video's first corpus figure previously sat on demonetised pre-2016 notes; match the cleared stone-grey note reference]`

**2.9**
> हिसाब सामने कीजिए: दस लाख का तीन परसेंट यानी साल का तीस हज़ार।

`[arch B | img: a hand-written division worked out on a ledger page (hand not in frame) | bar: THE SUM | stmt: ₹10,00,000 AT 3.0% IS ₹30,000 A YEAR | foot: ILLUSTRATIVE · withdrawal rate 3.0% · not a return promise]`

**2.10**
> और तीस हज़ार बटा बारह महीने — यानी महीने के ढाई हज़ार रुपये।

`[arch B | img: the same ledger page, the division carried down to a monthly line | bar: PER MONTH | num: ₹2,500 | foot: AT A 3.0% WITHDRAWAL RATE · ₹30,000 divided by 12 · ILLUSTRATIVE ARITHMETIC | colour: --fund | ⚠ this VO line does not speak the rate (creator-approved verbatim); 2.9 speaks it immediately before and the FRAME carries it — required by derived_income_carries_assumption]`

**2.11**
> अब देखिए कि ढाई हज़ार महीने में क्या आता है — आपका मोबाइल रिचार्ज और घर का इंटरनेट।

`[arch C | img: a broadband bill and a recharge receipt overlapping on a table — both identifiable as those documents, no bare cable | bar: WHAT ₹2,500 BUYS | stmt: The phone recharge and the home internet | foot: AT A 3.0% WITHDRAWAL RATE · ILLUSTRATIVE]`

**2.12**
> पूरे साल का रिचार्ज, पूरे साल का इंटरनेट, और आपकी तनख़्वाह में से एक रुपया नहीं गया।

`[arch C | img: twelve identical bill stubs pinned in a row on a board — twelve must be countable | bar: ALL TWELVE MONTHS | stmt: Not one rupee out of the salary | foot: AT A 3.0% WITHDRAWAL RATE · ILLUSTRATIVE | colour: --fund]`

**2.13**
> यह छोटा है, यह मानिए। पर ध्यान दीजिए कि बदला क्या — अब यह बिल आपकी कमाई नहीं, आपका जमा पैसा भर रहा है।

`[arch A | img: ONE brick set down at the foot of a stone staircase — a single brick, never a brickyard | bar: THE FIRST BRICK | stmt: The bill is now paid by the corpus, not the income]`

---

## Chapter 3 — दूसरी सीढ़ी: बीस लाख

*Rung 2, stepped the way chapter 2 established. The rate is re-spoken with the corpus at 3.1,
3.2, 3.3, 3.6 and 3.7 — five times in nine lines. This is where Dark Ledger stops re-stating
it and starts shipping bare numbers; repetition FEELS redundant here and is not.*
**Attempt 3 expanded 3.5 and 3.6.**

**3.1**
> अब दूसरी सीढ़ी — बीस लाख रुपये, उसी तीन परसेंट सालाना के हिसाब से।

`[arch A | img: two steel cash boxes side by side, the second visibly deeper | bar: RUNG TWO | num: ₹20,00,000 | stmt: AT A 3.0% WITHDRAWAL RATE]`

**3.2**
> हिसाब सामने कीजिए: बीस लाख का तीन परसेंट यानी साल का साठ हज़ार।

`[arch B | img: the same ledger page, a second division worked below the first | bar: THE SUM | stmt: ₹20,00,000 AT 3.0% IS ₹60,000 A YEAR | foot: ILLUSTRATIVE · withdrawal rate 3.0%]`

**3.3**
> और साठ हज़ार बटा बारह महीने — यानी उसी तीन परसेंट पर महीने के पाँच हज़ार रुपये।

`[arch B | img: the ledger page carried down to a second monthly line | bar: PER MONTH | num: ₹5,000 | foot: AT A 3.0% WITHDRAWAL RATE · ₹60,000 divided by 12 · ILLUSTRATIVE ARITHMETIC | colour: --fund]`

**3.4**
> अब देखिए कि पाँच हज़ार महीने में क्या आता है — गर्मियों वाला बिजली का बिल, पूरे साल का।

`[arch C | img: an Indian electricity bill on a table under a ceiling fan's shadow | bar: WHAT ₹5,000 BUYS | stmt: The summer electricity bill — all year | foot: AT A 3.0% WITHDRAWAL RATE · ILLUSTRATIVE]`

**3.5** ★ *expanded +45*
> मई में जो बिल देखकर घर में बहस होती है, वो बहस अब बंद हो जाती है — बिल उतना ही रहा, अब वो जमा रक़म से जाता है।

`[arch A | img: an old wall-mounted electricity meter, dial mid-spin | bar: THE MAY ARGUMENT | stmt: The bill did not shrink. The pocket changed. | foot: Paid by the corpus at a 3.0% withdrawal rate, not by the salary · ILLUSTRATIVE | ⚠ EXPANDED — modelled 8.08s scene, re-measure after TTS]`

**3.6** ★ *expanded +52*
> यहाँ ध्यान दीजिए कि बदला सिर्फ़ एक चीज़ — दर वही रही, तीन परसेंट। दर हर सीढ़ी पर एक ही मुहर है, बदलती सिर्फ़ रक़म है।

`[arch B | img: a rubber stamp pressed onto a fresh sheet, the percent mark just inked | bar: THE RATE HELD | num: 3.0% | foot: One stamp, every rung. Only the corpus moves. | colour: --target | ⚠ EXPANDED — modelled 8.20s scene, re-measure after TTS]`

**3.7**
> जमा रक़म दस लाख से बीस लाख हुई, और महीने का पैसा ढाई हज़ार से पाँच हज़ार — दोनों तीन परसेंट पर।

`[arch B | img: two brass weights of clearly different mass ON a shop balance, BOTH weights unmistakably in frame | bar: ONLY THE CORPUS MOVED | stmt: ₹10,00,000 TO ₹20,00,000 · ₹2,500 TO ₹5,000 A MONTH | foot: BOTH AT A 3.0% WITHDRAWAL RATE — the rate is identical on both sides · ILLUSTRATIVE]`

**3.8**
> और इसी सीधी बात को इंटरनेट पर बहुत बड़ा और बहुत जल्दी बना दिया जाता है।

`[arch C | img: a stack of glossy printed flyers with large numerals, edges curling | bar: WHAT THE INTERNET DOES | stmt: Makes it bigger and faster than it is | colour: --warn]`

**3.9**
> पर असल में यह धीमा है, और धीमा होना ही इसकी सबसे भरोसेमंद बात है।

`[arch A | img: a bullock cart wheel at rest on a dirt road, long shadow | bar: IT IS SLOW | stmt: Slow is the trustworthy part]`

---

## Chapter 4 — तीसरी सीढ़ी: चालीस लाख (AND THE FIRST TANK CALLBACK)

*Rung 3, then the honesty beat both twins skip: the money comes out of your own capital, which
is exactly WHY the rate is kept small. Dark Ledger says the opposite ("you do not touch the
principal") — an implied capital-preservation promise the arithmetic does not make. **4.7–4.8
is the tank callback**, so the honesty beat is a return to 2.3–2.4's picture, not a new idea.*
**Attempt 3 expanded 4.4 and 4.9.**

**4.1**
> अब तीसरी सीढ़ी — चालीस लाख रुपये, फिर वही तीन परसेंट सालाना।

`[arch A | img: a large steel trunk with the lid propped open, cloth-wrapped bundles inside | bar: RUNG THREE | num: ₹40,00,000 | stmt: AT A 3.0% WITHDRAWAL RATE]`

**4.2**
> हिसाब सामने कीजिए: चालीस लाख का तीन परसेंट यानी साल का एक लाख बीस हज़ार।

`[arch B | img: the ledger page, a third division worked below the other two | bar: THE SUM | stmt: ₹40,00,000 AT 3.0% IS ₹1,20,000 A YEAR | foot: ILLUSTRATIVE · withdrawal rate 3.0%]`

**4.3**
> और एक लाख बीस हज़ार बटा बारह — यानी उसी तीन परसेंट पर महीने के दस हज़ार रुपये।

`[arch B | img: the ledger page carried down to a third monthly line | bar: PER MONTH | num: ₹10,000 | foot: AT A 3.0% WITHDRAWAL RATE · ₹1,20,000 divided by 12 · ILLUSTRATIVE ARITHMETIC | colour: --fund]`

**4.4** ★ *expanded +58*
> अब देखिए कि उसी तीन परसेंट पर दस हज़ार महीने में क्या आता है — घर का पूरा राशन। यहाँ पैसा शौक़ नहीं, ज़रूरत उठा रहा है।

`[arch C | img: a kirana shop counter with a handwritten monthly ration list on the glass | bar: WHAT ₹10,000 BUYS | stmt: The month's ration — a need, not a nicety | foot: AT A 3.0% WITHDRAWAL RATE · ILLUSTRATIVE | ⚠ EXPANDED — the VO now SPEAKS the rate on this derived-income line; it was frame-only before. Modelled 8.15s scene, re-measure after TTS]`

**4.5**
> आटा, दाल, चावल, तेल, दूध और सब्ज़ी — हर महीने, और तनख़्वाह में से एक रुपया नहीं गया।

`[arch C | img: open sacks of atta, dal and rice in a row, a tin of oil beside them | bar: THE WHOLE LIST | stmt: Without touching the salary | foot: AT A 3.0% WITHDRAWAL RATE · ILLUSTRATIVE]`

**4.6**
> अब एक बात साफ़ कहनी ज़रूरी है — यहीं ज़्यादातर लोग बहक जाते हैं।

`[arch A | img: a road sign post with one arm snapped off, plain sky behind | bar: SAY IT PLAINLY | stmt: This is where most people get it wrong]`

**4.7**
> वापस उसी टंकी पर चलिए — यह पैसा आसमान से नहीं, आपकी अपनी टंकी में से निकलता है।

`[arch D | img: the 2.3 tank re-photographed from a different angle, the outlet running, level visibly below the fill line | bar: WHERE IT COMES FROM | stmt: Out of your own tank — capital and growth both | colour: --warn | TANK CALLBACK ONE — a different frame of the same object, never the same file]`

**4.8**
> इसीलिए बाहर वाला नल छोटा रखा जाता है, ताकि बची रक़म को फिर भरने का वक़्त मिले।

`[arch D | img: the same tank's outlet tap opened only a quarter turn, a thin steady stream | bar: WHY THE RATE IS SMALL | stmt: So what is left has time to fill back | colour: --target]`

**4.9** ★ *expanded +54*
> और यह भी याद रखिए कि इस तरह निकाले गए पैसे पर टैक्स भी लगता है। काग़ज़ पर जो हिसाब बना, हाथ में उससे थोड़ा कम आ सकता है।

`[arch C | img: a tax challan form face-up on a desk, pen across it | bar: AND TAX | stmt: Withdrawals are taxable — the hand may get less than the ledger | foot: NO RATE STATED ON PURPOSE — facts-staging B.2's LTCG row is SOFT, no statute or ITD page was read | ⚠ EXPANDED — modelled 8.06s scene, re-measure after TTS. Still ZERO tax figures, spoken or shown.]`

**4.10**
> अब तक तीन सीढ़ियाँ हुईं, और तीनों पर एक ही दर चली — तीन परसेंट।

`[arch B | img: three stone steps rising, each edge worn | bar: THREE RUNGS, ONE RATE | stmt: ₹10,00,000 · ₹20,00,000 · ₹40,00,000 — ALL AT 3.0% | colour: --target]`

---

## Chapter 5 — बारह परसेंट का जाल, और तीन बनाम चार (THE ~50% CORRECTION BEAT)

*Both twins put a "too good to be true" warning within about half a minute of the 5:00 mark,
on two different runtimes. In a rupee SWP frame the identical trap is a too-HIGH withdrawal
rate, which is structurally better: it forces the rate onto the screen and turns a compliance
constraint into the video's most dramatic moment. **5.4–5.5 is the second tank callback**, so
the drop zone opens on a familiar picture. Then the beat this whole run exists for — four
percent is an imported American number and India's own published research says three.*
**Attempt 3 expanded 5.3, 5.12 and 5.17.**

> ⚠ **The trap is a WITHDRAWAL rate, never a payout rate.** Twin B conflates the two (*"This
> is the famous 4% rule"* said over a payout figure). Every line below is about money someone
> **pulls out** of a corpus. Nothing here says a big advertised payout *is* a withdrawal rate,
> and the banned word appears nowhere.

**5.1**
> अब वो सवाल, जो इस पूरे हिसाब को तोड़ भी सकता है।

`[arch A | img: a hairline crack running across a dry clay pot | bar: THE QUESTION THAT BREAKS IT | stmt: — ]`

**5.2**
> अगर तीन की जगह दस या बारह परसेंट निकाल लें, तो सीढ़ी छोटी नहीं हो जाएगी?

`[arch B | img: a tap opened wide, water hitting a bucket hard enough to splash out | bar: WHY NOT TAKE MORE | stmt: 10% OR 12% WITHDRAWAL INSTEAD OF 3.0% | foot: A withdrawal rate — the amount you PULL OUT, not a return | colour: --warn | no question mark on screen, font subset | ⚠ the --warn tint lands on the 10/12% token, NEVER on the 3.0% comparator]`

**5.3** ★ *expanded +56*
> सुनने में यह बहुत अच्छा लगता है — और यहीं रुक जाना चाहिए। भाग तो सही निकलेगा, सवाल यह है कि टंकी कितने साल चलेगी।

`[arch A | img: a hand-painted STOP on a weathered wooden gate | bar: STOP HERE | stmt: The division still comes out right. The tank is the question. | ⚠ EXPANDED — this is now the hand-off INTO 5.4's tank callback, so 5.4 must land on the tank image immediately. Modelled 7.54s scene, re-measure after TTS]`

**5.4**
> इसे ऐसे समझिए — इतनी बड़ी दर पर बढ़त नहीं, मूल रक़म ही बाहर आने लगती है।

`[arch D | img: the 2.3 tank again, outlet wide open, the level dropping past the low mark | bar: WHAT IT EATS | stmt: A high withdrawal rate consumes the capital | colour: --warn | TANK CALLBACK TWO]`

**5.5**
> और टंकी ख़ाली होते ही महीने वाला पैसा भी ख़त्म हो जाता है।

`[arch D | img: the same tank, empty, outlet pipe dry, nothing running | bar: THEN IT STOPS | stmt: Capital gone, monthly income gone | colour: --warn]`

**5.6**
> बारह परसेंट मौक़ा नहीं है — बारह परसेंट चेतावनी है।

`[arch B | img: a red-painted warning triangle bolted to a concrete pole | bar: — | num: 12% | stmt: Not an opportunity. A warning. | colour: --warn | lands 4:36.3 (53.7%) — deliberately NOT expanded, the punch is the brevity]`

**5.7**
> इसका सबसे साफ़ सबूत सरकार की अपनी स्कीम में है — पोस्ट ऑफ़िस की मंथली इनकम स्कीम।

`[arch C | img: a post office counter window with a brass grille, no faces | bar: THE GOVERNMENT'S OWN | stmt: Post Office Monthly Income Scheme]`

**5.8**
> वो सात दशमलव चार परसेंट सालाना देती है, हर महीने, और सरकार की गारंटी के साथ।

`[arch B | img: a printed post-office rate board on a wall, macro | bar: THE PUBLISHED RATE | num: 7.4% p.a. | stmt: paid monthly, sovereign-backed | foot: Q1-Q2 FY27 — published rate as price evidence, not a recommendation | colour: --target | THE MID-VIDEO DROP ZONE OPENS HERE, 4:47 (55.8%)]`

**5.9**
> पर सात दशमलव चार परसेंट पर ज़्यादा से ज़्यादा नौ लाख रुपये ही रखे जा सकते हैं।

`[arch C | img: a deposit form with a ceiling figure printed in a boxed field | bar: THE CEILING | stmt: ₹9,00,000 MAXIMUM AT 7.4%, single account]`

**5.10**
> हिसाब सामने कीजिए: नौ लाख पर सात दशमलव चार परसेंट यानी महीने के क़रीब पचपन सौ रुपये।

`[arch B | img: a low concrete ceiling photographed from directly below, one bare bulb | bar: THE ROOF | num: ₹5,550 / MONTH | stmt: ₹9,00,000 AT 7.4% | foot: ILLUSTRATIVE · ₹9,00,000 times 7.4% divided by 12 · single-account ceiling | colour: --target]`

**5.11**
> गारंटी वाली मंथली इनकम की छत यही है, और इसीलिए एस डब्ल्यू पी वाला रास्ता मौजूद है।

`[arch A | img: a doorway cut into a thick wall, a lit passage beyond | bar: WHY THE OTHER ROUTE EXISTS | stmt: That is the ceiling on guaranteed monthly income]`

**5.12** ★ *expanded +44*
> अब वो नंबर, जो इंटरनेट पर सबसे ज़्यादा दिखता है — चार परसेंट। इतनी बार दोहराया गया कि नियम जैसा लगने लगा।

`[arch B | img: a printed search-results page on a desk, one figure ringed in pen | bar: THE INTERNET'S NUMBER | num: 4% | foot: Repeated until it sounds like a law. It is a paper — see the next frame. | colour: --warn | ⚠ EXPANDED — modelled 7.96s scene, re-measure after TTS]`

**5.13**
> यहाँ ध्यान दीजिए — चार परसेंट अमेरिका का नंबर है, उन्नीस सौ चौरानवे के एक रिसर्च पेपर से।

`[arch C | img: a bound academic journal open flat on a library table, columns of text, NO legible title or numerals | bar: WHERE IT CAME FROM | stmt: Bengen, Journal of Financial Planning, October 1994 | foot: Confirmed on three surfaces; the 1994 paper itself was not retrieved]`

**5.14**
> उस नियम की रिसर्च वहाँ के आँकड़ों पर बनी थी, तीस साल के लिए, और उसमें टैक्स और ख़र्चे जोड़े ही नहीं गए।

`[arch C | img: a printed methodology page with two lines struck through in ink | bar: WHAT IT EXCLUDED | stmt: Built on that market's history · 30-year horizon · no tax, no costs | foot: Cooley, Hubbard and Walz, AAII Journal, February 1998 — the authors state this themselves | colour: --warn]`

**5.15**
> भारत के अपने आँकड़ों पर हुई रिसर्च कुछ और कहती है — तीन से साढ़े तीन परसेंट।

`[arch C | img: a stapled research paper on an Indian desk beside a cup, top sheet blank of legible text | bar: INDIA'S OWN RESEARCH | stmt: 3.0% TO 3.5% | foot: Raju and Saraogi, "Balancing Acts: Safe Withdrawal Rates in the Indian Context", Jan 2024 · independently corroborated by ONE Indian practitioner surface (freefincal, Feb 2026) | colour: --target]`

**5.16**
> और पौने चार परसेंट के ऊपर जाते ही रक़म ख़त्म होने का ख़तरा तेज़ी से बढ़ता है।

`[arch B | img: a stair tread with the nosing broken away, seen edge-on | bar: THE EDGE | num: 3.75% | stmt: Above this, failure risk rises sharply | colour: --warn]`

**5.17** ★ *expanded +48*
> वजह भी सीधी है — रिज़र्व बैंक इस साल महँगाई क़रीब पाँच परसेंट मान रहा है। अगले साल वही राशन महँगा होगा, निकासी भी बढ़ेगी।

`[arch B | img: a vegetable-market price slate with figures chalked and re-chalked | bar: WHY INDIA'S IS LOWER | num: 5% | stmt: RBI's projected inflation — next year the same ration costs more | foot: RBI Monetary Policy Committee, 5 Aug 2026 — FY27 CPI projection 5.0% · a withdrawal that must rise each year is why the surviving rate is smaller | colour: --target | ⚠ EXPANDED — modelled 8.42s scene, the longest touched line. Re-measure after TTS FIRST.]`

---

## Chapter 6 — चौथी और पाँचवीं सीढ़ी: एक करोड़ (THE HERO)

*The number the video is named for, at 75% of runtime, priced in rent/EMI and then set beside
the one sourced external statistic — twin B's move exactly. 6.11 is the guard rail: the sum is
about a corpus and a rate, never about an age. 6.14 exists solely to name the difference
between a withdrawal rate and an assumed growth rate BEFORE either growth figure is spoken —
that separation is the conflation twin B commits.*
**Attempt 3 expanded 6.4, 6.8 and 6.11. 6.13 was deliberately left alone — it is the cut's one
measured breach of `max_scene_seconds`.**

**6.1**
> अब चौथी सीढ़ी — पचास लाख रुपये, वही तीन परसेंट सालाना।

`[arch A | img: a bank locker door standing open, empty shelf inside | bar: RUNG FOUR | num: ₹50,00,000 | stmt: AT A 3.0% WITHDRAWAL RATE]`

**6.2**
> पचास लाख का तीन परसेंट यानी साल का डेढ़ लाख, यानी महीने के साढ़े बारह हज़ार रुपये।

`[arch B | img: the ledger page, a fourth division worked below the others | bar: THE SUM | num: ₹12,500 / MONTH | stmt: ₹50,00,000 AT 3.0% IS ₹1,50,000 A YEAR | foot: ILLUSTRATIVE · withdrawal rate 3.0% | colour: --fund]`

**6.3**
> अब देखिए कि साढ़े बारह हज़ार में क्या आता है — कई शहरों में एक कमरे का किराया, या बाइक की क़िस्त।

`[arch C | img: a rent receipt book open on a table, carbon sheet visible | bar: WHAT ₹12,500 BUYS | stmt: A one-room rent in many cities, or the two-wheeler EMI | foot: AT A 3.0% WITHDRAWAL RATE · ILLUSTRATIVE]`

**6.4** ★ *expanded +52*
> और अब पाँचवीं सीढ़ी, जिसके लिए यह पूरा वीडियो बना है। शुरू में जो ख़ास नंबर रोक कर रखा गया था, वो यही है।

`[arch A | img: the top landing of the stone staircase, light falling across it | bar: RUNG FIVE | stmt: The number held back at the start | foot: The open loop from Chapter 1 closes here — NO figure on this frame, 6.5 carries it | ⚠ EXPANDED — modelled 7.81s scene, re-measure after TTS. Do NOT let the figure leak onto this frame; the payoff is the next scene.]`

**6.5**
> एक करोड़ रुपये, तीन परसेंट सालाना निकालने के हिसाब से।

`[arch B | img: a heavy steel safe door, handle centred, closed | bar: THE CORPUS | num: ₹1,00,00,000 | stmt: AT A 3.0% WITHDRAWAL RATE | colour: --target | THE ~70% REWARD BEAT — 6:25.4 = 74.9%]`

**6.6**
> हिसाब सामने कीजिए: एक करोड़ का तीन परसेंट यानी साल के तीन लाख।

`[arch B | img: the ledger page, the final division worked and underlined | bar: THE SUM | stmt: ₹1,00,00,000 AT 3.0% IS ₹3,00,000 A YEAR | foot: ILLUSTRATIVE · withdrawal rate 3.0% · corpus equals annual withdrawal divided by the rate]`

**6.7**
> और तीन लाख बटा बारह महीने — यानी तीन परसेंट पर, महीने के पच्चीस हज़ार रुपये।

`[arch B | img: the same ledger page, the monthly line ruled twice — ONE continuous zoom from 6.6 | bar: THE NUMBER | num: ₹25,000 / MONTH | stmt: AT A 3.0% WITHDRAWAL RATE | foot: ILLUSTRATIVE · ₹3,00,000 divided by 12 | colour: --fund]`

**6.8** ★ *expanded +49*
> अब इस पच्चीस हज़ार को एक सरकारी आँकड़े के बगल में रखिए। अकेला नंबर कुछ नहीं कहता, मतलब तुलना से बनता है।

`[arch A | img: two sheets of paper laid edge to edge on a desk | bar: SET IT BESIDE THIS | stmt: A number alone says nothing. Meaning comes from what sits next to it. | ⚠ EXPANDED — this frame's stmt was empty before and now carries the line's point. Modelled 7.95s scene, re-measure after TTS]`

**6.9**
> नियमित तनख़्वाह पाने वाले भारतीय पुरुष की औसत महीने की कमाई चौबीस हज़ार दो सौ सत्रह रुपये है।

`[arch C | img: a printed pay slip on thin paper, folded once, figures not legible | bar: THE SOURCED FIGURE | num: ₹24,217 | stmt: Average monthly earnings, regular wage or salaried · men | foot: PLFS Annual Report 2025 (Jan-Dec 2025), PIB — men ₹24,217, women ₹18,353 | ⚠ MEASURED 8.741s — 0.26s inside max_scene_seconds. Not expanded, and must not be.]`

**6.10**
> यानी एक करोड़, तीन परसेंट पर, औसत तनख़्वाह के बराबर पैसा हर महीने देता है।

`[arch B | img: a two-pan balance sitting level, a coin in each pan | bar: THEY MEET | stmt: ₹25,000 AT 3.0% vs ₹24,217 EARNED | foot: ₹1,00,00,000 at a 3.0% withdrawal rate · PLFS 2025 | colour: --fund]`

**6.11** ★ *expanded +45*
> यहाँ ध्यान दीजिए — यह उम्र का नहीं, सिर्फ़ रक़म और दर का हिसाब है। न कोई तारीख़ है, न कोई वादा — सिर्फ़ एक भाग।

`[arch B | img: a stone milestone marker beside an empty road, no distance legible | bar: WHAT IT IS | stmt: A corpus and a rate. No age, no date, no promise. | foot: No age, no date and no years-to-freedom is claimed anywhere in this video | ⚠ EXPANDED — this is the no_unsourced_retire_early guard rail and the expansion HARDENS it. Modelled 7.95s scene, re-measure after TTS]`

**6.12**
> अब देखिए कि उधार लिया चार परसेंट क्या करता है — वही पच्चीस हज़ार महीना, निशाना पचहत्तर लाख।

`[arch B | img: a target board with the outer ring cut away, hung on a wall | bar: THE IMPORTED RULE | num: ₹75,00,000 | stmt: WHAT 4% SETS AS THE TARGET FOR THE SAME ₹25,000 A MONTH | colour: --warn]`

**6.13**
> उधार लिया नंबर वही लक्ष्य एक-चौथाई छोटा कर देता है — चार परसेंट पर पचहत्तर लाख, तीन परसेंट पर एक करोड़।

`[arch B | img: a short measuring tape held against a long timber plank | bar: THE COST OF IMPORTING IT | stmt: ₹75,00,000 AT 4% vs ₹1,00,00,000 AT 3.0% — a quarter smaller | foot: Same ₹25,000 a month, two different rates. India's own research says 3.0 to 3.5%. | colour: --warn | ⚠⚠ MEASURED 9.012s of audio = 9.812s scene — THE ONLY BREACH OF max_scene_seconds 9.0 IN THE CUT. NOT EXPANDED. THIS SCENE NEEDS TWO data-framings: wide on the tape against the plank, then a push to the short end. | ⚠ the --warn tint lands on the 4% token, NEVER on the 3.0% comparator]`

**6.14**
> अब आख़िरी हिसाब, और यहाँ दर निकालने की नहीं, बढ़ने की मानी गई है।

`[arch A | img: a monthly standing-instruction slip on a bank counter | bar: WHAT IT COSTS PER MONTH | stmt: The rates below are ASSUMED GROWTH — not the 3.0% withdrawal rate | foot: Two different objects. Withdrawal rate is what you take out. Growth rate is what the corpus is assumed to earn.]`

**6.15**
> बीस साल में, सात दशमलव एक परसेंट की मानी हुई बढ़त पर, महीने के क़रीब उन्नीस हज़ार।

`[arch B | img: a passbook open at a page of small regular entries | bar: 20 YEARS · ASSUMED 7.1% GROWTH | num: ₹19,000 / MONTH | foot: ILLUSTRATIVE · monthly compounding · 7.1% is the published PPF and 3-yr post-office rate, Q2 FY27 — used as an assumption, not a forecast | colour: --target]`

**6.16**
> और क़रीब बारह परसेंट की मानी हुई बढ़त पर, क़रीब दस हज़ार — दोनों हिसाब हैं, वादे नहीं।

`[arch B | img: a printed newspaper market page folded on a table, no headline legible | bar: 20 YEARS · ASSUMED 12% GROWTH | num: ₹10,000 / MONTH | foot: ILLUSTRATIVE · monthly compounding · 12% is a long-run index SHAPE, never a decimal and never a promise. Both columns shown on purpose. | colour: --target]`

---

## Chapter 7 — वापस उसी दिन पर (PEAK-END · ONE terminal CTA)

*Both twins close on the day and on time, not on money. Twin A recaps and CTAs once; twin B
does neither and holds the higher reach. This takes B's callback, A's single terminal CTA, and
nothing else — zero mid-roll CTA, third independent confirmation of that line. ⚠ The callback
points at style E's chapter 1 (the silent phone, the one buzz), NOT at the superseded style-A
open (a Tuesday alarm, chai, a window) — none of those objects exist in this cut.*
**Attempt 3 touched nothing in this chapter: every line is a callback or the CTA, and both are
worse when longer.**

**7.1**
> अब वापस उसी दिन पर चलिए, जिस दिन आपका फ़ोन एक बार भी नहीं बजा था।

`[arch A | img: the 1.1 bedside table and phone re-photographed in late-afternoon light, phone face-down again, the day over — a DISTINCT frame, never a reuse | bar: BACK TO THE DAY | stmt: The phone that did not ring | CALLBACK — 91.4%]`

**7.2**
> उस दिन जो एक बार वो बजा, उसमें आया पैसा किसी नौकरी का नहीं था।

`[arch D | img: the same phone, screen glow gone, notification cleared (same object, new crop) | bar: THAT MONEY | stmt: It was not from a job]`

**7.3**
> वो एक करोड़ का तीन परसेंट था, बारह महीनों में बँटा हुआ — और बस इतना ही।

`[arch B | img: a single ledger line with a figure and a percentage written beside it | bar: WHAT IT WAS | stmt: ₹1,00,00,000 AT 3.0% DIVIDED BY 12 | foot: The whole video, in one division]`

**7.4**
> यहाँ ध्यान दीजिए कि इस पूरे वीडियो में कोई रक़म अपनी दर के बिना नहीं बोली गई।

`[arch A | img: five stamped receipts laid in a row, each with a figure and a percent mark | bar: THE HABIT | stmt: Every figure carried its rate]`

**7.5**
> दर के बिना रक़म एक वादा है — दर के साथ वो एक भाग है, जिसे आप ख़ुद जाँच सकते हैं।

`[arch D | img: a hand working a division on paper with a pencil (hand only, no face) | bar: THE TEST | stmt: Without a rate it is a promise. With one it is a division you can check.]`

**7.6**
> और यह सीढ़ी एक करोड़ से नहीं, तीन परसेंट वाले उस पहले ढाई हज़ार से शुरू हुई थी।

`[arch B | img: the single brick from 2.13, now with two more set beside it | bar: WHERE IT STARTED | stmt: Not at ₹1,00,00,000 — at the ₹2,500 recharge bill, BOTH AT 3.0% | colour: --fund]`

**7.7**
> दिन किसका है, यह उसी दिन तय होना शुरू होता है जिस दिन पहली सीढ़ी की ईंट रखी जाती है।

`[arch A | img: the 1.3 kitchen counter at full daylight, the steel glass empty (same object, new crop) | bar: WHOSE DAY | stmt: It starts on the day the first brick is laid]`

**7.8**
> पैसे की ऐसी सीधी, बिना वादे वाली बात के लिए — सब्सक्राइब कीजिए।

`[arch A | img: a closed ledger and a capped pen laid down, finished | bar: — | num: SUBSCRIBE | foot: The only CTA in the video, at 99.1% | colour: --pop]`

---

## Fact trace (every number → facts-staging.md)

**Attempt 3 added ZERO numbers.** Every row below is unchanged; the ten expanded lines added
explanation, comparison and guard-rail language only, and not one of them introduced a figure,
a decimal, a date or a rate that was not already spoken elsewhere in the cut.

| Number / claim in script | Where | facts-staging.md row | Tag |
|---|---|---|---|
| **3.0% withdrawal rate** — the assumption everything divides by | 2.6, 2.7, 2.8, 2.9, 3.1, 3.2, 3.3, 3.6, 3.7, 4.1, 4.2, 4.3, **4.4 (new — now spoken)**, 4.10, 5.2, 5.15, 6.1, 6.2, 6.5, 6.6, 6.7, 6.10, 6.13, 7.3, 7.6 | A.3 "India SWR, peer-reviewed — 3.0–3.5%; best SWR **3.0% at a 40% equity allocation**" (Raju & Saraogi, 2024-01-17) | **HARD on the band** · spoken as a *chosen* number, never as a fact about the future |
| **3.0 – 3.5%** stated as India's published range | 5.15 | A.3 same row | HARD on the band |
| **3.75%** — above this, failure risk rises sharply | 5.16 | A.3 "failure risk rises sharply **above 3.75%**" | **SOFT** — A.3's own tag is "HARD on the 3.0–3.5% band · **SOFT on any single decimal**", and 3.75% is a single decimal. SSRN 403'd again at audit; recovered only from secondary summaries of the paper. Kept because it errs toward caution, but a primary read is owed before promotion |
| **4%** = a 1994 US paper, 30-year horizon, no tax/costs | 5.12, 5.13, 5.14, 6.12, 6.13 | A.1 (Bengen, JFP Oct 1994) + A.2 #1 (Trinity, verbatim: *"The study did not adjust for taxes or transaction costs"*) + A.2 #2 (built for 30 years) | **HARD (primary — the Trinity paper was read direct)** |
| **~5%** inflation, the mechanism for the lower rate | 5.17 | A.3 "RBI projects CPI inflation at **5.0% for FY27**", MPC 2026-08-05 | HARD. **5.17's expansion states the MECHANISM** — next year's ration costs more, so the withdrawal must rise — which is the firewall's own wording ("this is *why* the rates differ — it is the mechanism, not a coincidence"), and is corroborated by A.1's record that Bengen's withdrawals were inflation-linked after year one. **No new figure.** |
| **POMIS 7.4% p.a., paid monthly** | 5.7, 5.8, 5.9, 5.10 | B.2 "POMIS rate — **7.4% p.a., paid monthly**" | HARD (two independent + the unchanged notification) |
| **₹9,00,000** POMIS single-account ceiling | 5.9, 5.10 | B.2 "deposit ceiling — **₹9 lakh single** · ₹15 lakh joint" | HARD (unanimous) |
| **≈ ₹5,550/month** POMIS ceiling output | 5.10 | B.2 lead-out: "Maximum monthly income from one account: **₹5,550**" · PART E records the secondaries' "₹5,500" as a bad rounding | COMPUTED — spoken as «क़रीब पचपन सौ», exact on screen |
| **₹10,00,000 → ₹2,500/month at 3.0%** | 2.8, 2.9, 2.10, 3.7, 7.6 | B.3 formula row: `corpus = annual withdrawal ÷ withdrawal rate`, at the staged 3.0% | COMPUTED · `ILLUSTRATIVE` foot on every frame |
| **₹20,00,000 → ₹5,000/month at 3.0%** | 3.1, 3.2, 3.3, 3.7 | B.3, same formula | COMPUTED |
| **₹40,00,000 → ₹10,000/month at 3.0%** | 4.1, 4.2, 4.3, 4.4 | B.3, same formula | COMPUTED |
| **₹50,00,000 → ₹12,500/month at 3.0%** | 6.1, 6.2 | B.3, same formula | COMPUTED |
| **★ ₹1,00,00,000 → ₹25,000/month at 3.0%** — the hero | 6.5, 6.6, 6.7, 6.10, 6.13, 7.3 | B.3 "**★ THE ₹ HERO NUMBER: ₹1 crore, at a 3% withdrawal rate, is ₹25,000 a month**" | COMPUTED (the staged hero row) |
| **₹75,00,000** = the same ₹25,000/month at 4% | 6.12, 6.13 | B.3 table, 4.0% column: ₹25,000/mo → ₹75,00,000 | COMPUTED (staged row) |
| **A quarter smaller** — the rule-import cost | 6.13 | B.3 "The imported rule under-states an Indian target by **25%**" | COMPUTED (staged framing) |
| **₹24,217** — average monthly earnings, regular wage/salaried | 6.9, 6.10 | B.1 "Regular wage/salaried avg monthly earnings — **₹24,217** men / ₹18,353 women", PLFS Annual Report 2025, PIB | **HARD** |
| **7.1%** assumed growth, and **≈ ₹19,000/month for 20 years** | 6.15 | B.1 "PPF — **7.1% p.a.**, Q2 FY2026-27" + B.3 "Getting there" table, 20-year row at 7.1% | rate **HARD** · the monthly figure **COMPUTED**, labelled illustrative |
| **~12%** assumed growth, and **≈ ₹10,000/month for 20 years** | 6.16 | B.1 Nifty 50 long-run figure (**SOFT — shape only, never a decimal**, all three NSE hosts 403'd) + B.3 20-year row | **SOFT** — shape only, spoken as «क़रीब बारह परसेंट», no decimal anywhere, and the index measure is **never explained** (B.1 vocabulary trap) |
| **SWP** definition — a fixed amount drawn monthly out of your own corpus | 2.2, 2.4, 4.7, 4.8, 5.11 | B.2 "SWP = what it is … withdrawals come out of **capital + appreciation**" — four fund houses, identical definition | **HARD (terminology)** |
| Withdrawals are taxable | 4.9 | B.2 LTCG row — tagged **SOFT** (no statute or ITD page read) | **SOFT — so no figure is spoken or shown**, only that tax applies. **4.9's expansion stays inside that**: it says what reaches the hand is *a little less* than the ledger figure — a direction, never a rate, never a threshold. |
| **12%** as a withdrawal rate = a warning | 5.2, 5.4, 5.5, 5.6 | Study conclusion 6 (both twins warn at 10–12%, at ≈5:00) + A.3 (failure risk rises sharply above 3.75%) | the trap beat — **12% is spoken only as a rate someone might PULL OUT, never as a return** |
| **The tank** (2.3, 2.4, 4.7, 4.8, **5.3 — spoken only**, 5.4, 5.5) | — | **not a fact — an analogy** | Carries no figure and asserts no measurement. Its one claim is definitional: the safe-withdrawal question *is* "how much can be drawn per year without emptying the corpus". Any drawn level line is decorative. **5.3 now names the tank in VO one clip before 5.4 shows it — a hand-off, not a seventh tank photograph.** |

### The rate-in-the-line check, one line at a time

`withdrawal_rate_on_screen` plus its 2026-08-07 `derived_income_carries_assumption` extension.
Every corpus line **and** every derived-income line, re-read individually:

| line | the figure | the rate, spoken in the same line |
|---|---|---|
| 2.8 | ₹10,00,000 | «तीन परसेंट सालाना निकालने के हिसाब से» |
| 2.9 | ₹30,000/yr | «दस लाख का तीन परसेंट» |
| 2.10 | ₹2,500/mo | **not spoken — creator-approved verbatim.** 2.9 speaks it in the immediately preceding clip; the FRAME carries `AT A 3.0% WITHDRAWAL RATE` |
| 2.11, 2.12 | ₹2,500/mo (what it buys) | **not spoken — creator-approved verbatim.** Frames carry the rate + `ILLUSTRATIVE` |
| 3.1 | ₹20,00,000 | «उसी तीन परसेंट सालाना के हिसाब से» |
| 3.2 | ₹60,000/yr | «बीस लाख का तीन परसेंट» |
| 3.3 | ₹5,000/mo | «उसी तीन परसेंट पर» |
| 3.4 | ₹5,000/mo (what it buys) | frame carries the rate + `ILLUSTRATIVE`; 3.3 speaks it immediately before |
| **3.5** | ₹5,000/mo (implied, no figure spoken) | **no figure in the line at all.** The frame's new `foot:` carries `3.0% · ILLUSTRATIVE` because the line asserts *who pays the bill*, which is the corpus's output |
| 3.7 | both corpora + both monthly figures | «दोनों तीन परसेंट पर» |
| 4.1 | ₹40,00,000 | «फिर वही तीन परसेंट सालाना» |
| 4.2 | ₹1,20,000/yr | «चालीस लाख का तीन परसेंट» |
| 4.3 | ₹10,000/mo | «उसी तीन परसेंट पर» |
| **4.4** | ₹10,000/mo (what it buys) | **«उसी तीन परसेंट पर» — NEW in attempt 3.** This line previously relied on the frame plus the preceding clip; it now speaks the rate in the same breath as the figure. **One of the four soft spots attempt 2 flagged for fin-audit is closed.** |
| 4.5 | ₹10,000/mo (what it buys) | frame carries the rate + `ILLUSTRATIVE`; 4.3 and now 4.4 both speak it before |
| 4.10 | all three corpora | «तीनों पर एक ही दर चली — तीन परसेंट» |
| 5.9 | ₹9,00,000 | «सात दशमलव चार परसेंट पर» |
| 5.10 | ≈₹5,550/mo | «नौ लाख पर सात दशमलव चार परसेंट» |
| 6.1 | ₹50,00,000 | «वही तीन परसेंट सालाना» |
| 6.2 | ₹1,50,000/yr and ₹12,500/mo | «पचास लाख का तीन परसेंट» |
| 6.3 | ₹12,500/mo (what it buys) | frame carries the rate + `ILLUSTRATIVE`; 6.2 speaks it immediately before |
| 6.5 | ₹1,00,00,000 | «तीन परसेंट सालाना निकालने के हिसाब से» |
| 6.6 | ₹3,00,000/yr | «एक करोड़ का तीन परसेंट» |
| 6.7 | ₹25,000/mo | «तीन परसेंट पर» ← *the hero's derived income carries its own rate* |
| 6.10 | ₹25,000/mo vs ₹24,217 | «एक करोड़, तीन परसेंट पर» |
| 6.12 | ₹75,00,000 + ₹25,000/mo | «उधार लिया चार परसेंट» |
| 6.13 | ₹75,00,000 and ₹1,00,00,000 | «चार परसेंट पर … तीन परसेंट पर» — both rates, both figures |
| 6.15 | ≈₹19,000/mo | «सात दशमलव एक परसेंट की मानी हुई बढ़त पर» |
| 6.16 | ≈₹10,000/mo | «क़रीब बारह परसेंट की मानी हुई बढ़त पर» |
| 7.3 | ₹1,00,00,000 → the monthly figure | «एक करोड़ का तीन परसेंट» |
| 7.6 | ₹1,00,00,000 and ₹2,500 | «तीन परसेंट वाले उस पहले ढाई हज़ार» |

**After attempt 3, THREE lines carry a figure whose rate is not in the spoken sentence — 2.10,
2.11 and 2.12 — down from four.** All three are creator-approved chapter-2 copy and cannot be
edited here. 3.4 / 4.5 / 6.3 inherit the rate from the immediately preceding clip and carry it
in frame, by design: those are the bill, not the arithmetic. `fin-audit` should re-rule only on
the three verbatim ones; if the preceding-clip rate does not satisfy "the same VO breath", the
fix is a change to the approved chapter-2 copy, not a silent edit.

### Deliberately NOT used (so fin-audit does not rediscover them)

- **The whole of PART C.** That is the other cut's block: a foreign market's income figure, a
  foreign safe-rate literature, foreign funds and a foreign household-spending average. The
  currency firewall is explicit that the two sets differ on three axes at once and are not
  convertible. **The rupee's counterpart glyph appears nowhere in this file, not even inside a
  claim ID.**
- **The banned payout word, in every form** — English, inline English, and every Devanagari
  transliteration — and, with it, **any explanation of the index's total-return measure**,
  because that measure is *defined* using the word. 6.16 quotes the shape and nothing else.
- **Bengen's own 2025 revision to 4.7%, and the 3.9% forward-looking figure.** Both HARD, both
  rates for the *other* market. Importing either would commit exactly the error Chapter 5
  spends seventeen lines correcting.
- **Pfau's country count and every country SAFEMAX decimal.** A live conflict is on record
  (17 vs 19 countries); the India research carries the point directly, so neither is needed.
- **SCSS 8.2% / ₹30 lakh.** SOFT, no primary read, and **age-gated at sixty-plus** — using it
  would put an age into a video whose binding constraint is that no corpus becomes an age.
- **Any precise India tax figure** (12.5%, ₹1.25 lakh). SOFT — no statute or Income Tax
  Department page was read. 4.9 says tax applies, says the hand gets a little less than the
  ledger, and stops. **Attempt 3's expansion of that line was written specifically to add
  meaning without adding a number**, because a number there would be the one unsourced claim
  in the cut.
- **Industry AUM ₹82.22 lakh crore and the ₹32,087 crore monthly SIP inflow.** SOFT, and the
  staging note itself calls them "context colour only".
- **The 15-year and 25-year SIP rows.** Only the 20-year row is spoken, and both of its columns
  are shown. Adding horizons invites the viewer to read a *date*, which PART D forbids.
- **The ₹500 / ₹250 monthly minimum.** True and HARD. It was **re-considered and re-rejected**
  as expansion material for attempt 3: it belongs to a "start today" beat, neither twin has
  one, and both close on the day image. Recorded as available for a later cut.
- **Every age, every date-of-freedom, and every "quit your job" formulation.** PART D: the only
  sourced early-retirement statement in the whole file is a warning to withdraw *less*. 6.11
  states the refusal on the record and, after attempt 3, refuses a date and a promise too.
- **A named fund, AMC, bank, app or platform.** Persona rule. The post-office monthly-income
  scheme and the 7.1% small-savings rate appear as published price evidence only, and the 5.8
  and 6.15 foots say so on screen.

---

## Build handoff

1. **`assets/voice/hindi-lines.json` = 81 entries keyed `1.1 … 7.8`**, containing **only** the
   `>` VO strings above — no markdown, no cue text, no on-screen text. Devanagari, verbatim.
   **Slice the source file; never retype.** Extract by the `**N.M**` line key, not by a bare
   `^> ` grep (this file carries guard blockquotes). Gate the extraction with a byte-for-byte
   reconstruction check before generating audio (`long_form_scripting.md` §1.7).
2. **⚠ RE-VOICE EXACTLY TEN CLIPS — 3.5 · 3.6 · 4.4 · 4.9 · 5.3 · 5.12 · 5.17 · 6.4 · 6.8 ·
   6.11.** The other 71 clips on disk are current: right voice (Amrut, and `assets/voice/.voice`
   now stamps it), right text, measured durations already in `timing.json`. **Run the resume,
   do NOT run `--force`** — `tools/tts/batch.py` compares each line against its `<id>.txt`
   sidecar and prints REGEN per changed line. **Expect exactly ten REGENs.** Eleven or more
   means this attempt's whole-file rewrite drifted a Devanagari character on a line it did not
   intend to touch (nukta or chandrabindu — inaudible until the render): stop, restore that
   line from its sidecar, and do not spend the call. Cost: **290 → 300 of 350**.
3. **Timing is by construction.** One line = one clip = one scene. Scene span =
   `probe(clip) + lead_in + tail`, with MEDIUM's `lead_in_seconds` 0.25 and `tail_seconds` 0.55
   (**not** the `scene.*` 0.4/1.0 defaults, which are tuned for SHORT's nine lines). Never
   hand-edit a duration; regenerate all homes of the timing numbers from one source. **Rebuild
   `timing.json` after the ten new clips land — 71 rows are unchanged and must not be
   re-probed into new values.**
4. **Recount the characters programmatically** before reacting to any drift, and re-check
   against `(510 − lines × 0.8) × 14.281 = 6,357` — **not** `510 × 14.281`. Target **6,422**,
   +1.0%. **The 117-character flat ceiling is a screen, not a verdict** (see the timing budget):
   4.4 at 119 and 5.17 at 121 sit above it on purpose, on lines whose measured base rate is
   17–19 c/s, and the arbiter is `probe()`.
5. **Re-measure the flat rate on the ten new clips** and record it beside 14.281 in the build
   log. These are the first Amrut clips of *newly written* style-E text; `rate_key_en_followup`
   found style E runs ~1.5% pause-heavier than its key predicts, so a small negative drift is
   expected and is not a defect. Record the **shape** (one-sided = the key needs moving again;
   two-sided = fine). Do not re-key `format.json` off ten lines — 81 was the sample that earned
   14.281.
6. **The hook gate is MEASURED and chapter 1 is untouched**: 1.3 onset **8.682 s**, close
   **11.294 s**, number-naming 1.5 at **18.299 s**, against a 15 s gate. Nothing in attempt 3
   moves any of these. Do not re-measure unless a chapter-1 clip is regenerated.
7. **⚠ THE TWO-FRAMINGS SCENE IS 6.13, NOT 2.4.** Attempt 2 predicted 2.4 at 9.01 s from the
   flat model and ordered two framings there; **2.4 measured 7.853 s and needs one.**
   **6.13 measured 9.012 s of audio = 9.812 s of scene and is the cut's only breach of
   `max_scene_seconds` 9.0** — it needs **two `data-framings`**: wide on the measuring tape
   against the timber plank, then a push to the short end. It was deliberately not expanded.
   **2.7** is still the only true image hold (it holds 2.6's): one continuous zoom across both
   scenes, never a self-dissolve, tighter crop on 2.7. **6.6 → 6.7** is the second
   continuous-zoom pair. **After the ten clips are voiced, re-check the eight modelled scenes
   in the long-scene table**; any that lands over 9.0 gets the same two-framings treatment.
8. **The rate is a build-time invariant, not a design preference.** Assert it: every scene whose
   on-screen text contains a corpus token (`₹10,00,000`, `₹20,00,000`, `₹40,00,000`,
   `₹50,00,000`, `₹75,00,000`, `₹1,00,00,000`, `₹9,00,000`) **or a derived monthly token**
   (`₹2,500`, `₹5,000`, `₹10,000`, `₹12,500`, `₹25,000`, `₹5,550`, `₹19,000`) must also render
   a rate token (`3.0%`, `4%`, `7.4%`, `7.1%`, `12%`) or an explicit `ILLUSTRATIVE` marker in
   the same frame. That is `withdrawal_rate_on_screen` + `derived_income_carries_assumption`,
   and it is the one thing `fin-audit` hard-fails. **3.5's new frame carries the rate in its
   `foot:` for exactly this reason** — the line asserts which pocket pays the bill, and that is
   the corpus's output.
9. **Pin the arithmetic convention before computing anything on screen.** Every rung is
   `corpus × 0.03 ÷ 12`, exact, no rounding: ₹10,00,000→₹2,500 · ₹20,00,000→₹5,000 ·
   ₹40,00,000→₹10,000 · ₹50,00,000→₹12,500 · ₹1,00,00,000→₹25,000. The POMIS figure is
   `₹9,00,000 × 0.074 ÷ 12 = ₹5,550` exactly — **not** the ₹5,500 every secondary prints
   (PART E). The VO says «क़रीब पचपन सौ»; the frame says `₹5,550`.
10. **⚠ THE COMMA DEFECT IS SYSTEM-SIDE, NOT PER SCENE.** The recorded ch2 blocker — a foot
    struck through by the comma descenders of `₹10,00,000` — recurs on **every lakh and crore
    rung in this cut**. It was fixed system-side; verify the fix holds at 2.8, 3.1, 3.7, 4.1,
    4.10, 6.1, 6.5, 6.12, 6.13, 7.3, 7.6 before any of those chapters is judged.
11. **⚠ THE RECORDED ch1/ch2 BLOCKERS ARE KEYED TO STYLE-A SCENE NUMBERS AND MUST BE RE-MAPPED.**
    Under style E, ch1 is s1–s8 and ch2 is s9–s21, so every `sNN` in `run.json.chapters.hi` is
    now wrong. Carry them **by subject**: the notification card needs the ₹ glyph (now 1.4) ·
    the three named bills must be in frame (now 1.6) · current-series notes under the first
    corpus (now 2.8) · one brick, not a brickyard (now 2.13) · the recharge and broadband
    documents must both be present, not a bare cable (now 2.11) · twelve stubs must be
    countable (now 2.12). **The `_carry_forward_from_ch1_assets` note is partly void:** style E
    has no chai glass and no window in chapter 1, so 7.7's callback now rhymes with the **1.3
    kitchen counter and its steel glass**; and since style E's 1.8 uses a stamp rather than a
    balance scale, 3.7's brass weights no longer risk reading as a reuse — but they must still
    be visibly ON the balance.
12. **Images: one per line, 81 scenes, zero photo-free frames** (`photo_free_scene_ratio` = 0),
    each passing the **sound-off test per line**. **Attempt 3 added no scene and changed no
    image brief** — the ten expanded lines keep their existing subjects, and every expansion
    was written to stay inside the picture that was already specified. The **tank is a recurring
    subject needing six distinct frames** (2.3 filled / 2.4 two taps / 4.7 outlet running, level
    down / 4.8 tap a quarter turn / 5.4 wide open, level dropping / 5.5 empty and dry) —
    *different frames of the same object*, never the same file, and tap position and level alone
    must say the beat. **5.3 mentions the tank in VO but must NOT get a seventh tank frame**: it
    keeps the STOP gate and hands into 5.4. 7.1, 7.2 and 7.7 are callbacks to 1.1, 1.4 and 1.3:
    **new photographs of the same subject**, not re-used files. **Every photograph in the
    superseded ch1/ch2 build passed the YHIGH gate** — re-use what still matches a brief, but
    note the style-E open needs new frames (no alarm-clock-first shot, no chai, no window).
13. **⚠ Grade + source rule.** The chapter grade is LOCKED (`grayscale(.32) brightness(.62)`)
    and per-scene overrides are forbidden, so **a white-dominant, high-key stock subject can
    only become a flat charcoal slab**. HIGHLIGHT CEILING predicts survival, not average
    brightness. This is what killed three ch1 scenes and one ch2 scene on the superseded build.
14. **Nothing on screen may be a legible foreign document, price or figure**, and no frame may
    put a rupee figure and a foreign figure in one composition. The 5.13/5.14 journal and
    methodology pages are photographed with **no legible title or numerals** — the citation
    lives in the `foot:`, not in the photograph. **Never fabricate a source document**: 5.15's
    Indian research paper is a stapled document with a blank top sheet; no invented seal,
    agency name or legible figure may appear on a frame cited to a real paper
    (`vector_art.lottie.truth_bar`). **5.12's new `foot:` names no source** — the provenance is
    5.13's job and stays there.
15. **⚠ THE FONT SUBSET.** `NotoSansFinance-var.woff2` carries 97 codepoints: `>` `→` `▶` `×`
    `≈` `~` are absent. Already obeyed in every cue above — `TO` not an arrow, `AT` / `IS` not
    an equals, `DIVIDED BY` not a solidus, `·` as the separator, `12%` not a tilde, and **no
    question mark in any on-screen string** (5.2's line is set as a statement for exactly this
    reason). The six on-screen strings attempt 3 changed (3.5, 3.6, 4.4, 4.9, 5.3, 5.12, 5.17,
    6.4, 6.8, 6.11) were written inside the same subset. Verify every on-screen string against
    a dumped `subset.txt` before render.
16. **Anchor cues to word-level timings** (faster-whisper), not character-offset interpolation.
    `first_cue_by_seconds` 0.5, `cue_min_gap_seconds` 0.8, `max_simultaneous_elements` 6,
    `max_chips_per_row` 3, `max_chip_chars` 22. **The ten expanded scenes each gained a second
    sentence, so each gained roughly one cue** — check them against `max_simultaneous_elements`
    and `cue_min_gap_seconds` rather than assuming the attempt-2 cue counts still hold.
17. **Lottie candidates** (`vector_art.reach_for_it_when`, cap 4 per chapter): **1.4** one
    notification arriving, carrying the ₹ glyph and no figure (`phone-notify-credit` is already
    in the library) · **2.3 / 2.4 / 4.7 / 4.8 / 5.4 / 5.5** the tank at six states, which is the
    cut's spine and worth drawing once and re-cutting · **4.10** three rungs at one rate ·
    **6.13** two targets at two rates. Search the library first (`tools/lottie/search.py`) —
    `two-rates-30x`, `stats-table-row` and `calendar-20th-circled` may re-cut. **Tint is
    required. Nothing drawn may read as a measurement**: the tank's level line is decorative.
18. **Chapter-wise production.** Build, proof and re-render chapter by chapter (`fin-editor`
    then `fin-ceo`); concat and final-render only after all seven chapters are locked. Encode
    with an explicit `-o renders/FINAL-1080p-hi.mp4`.
19. **Captions.** Narration MD + `.srt` per cut via `tools/transcript.py` — join the generated
    lines, never retype them (creator rule 2026-08-06). Burn subtitles into every frame.
20. **⚠ THE DELIVERABLE OF ATTEMPT 3 IS A RUNTIME, SO VERIFY IT AT THE END.** The cut exists at
    MEDIUM tier to earn mid-roll, and mid-roll needs **8:00**. Attempt 2 shipped 479.259 s and
    missed by 0.741 s. Target is **514.5 s (8:34.5)**, i.e. **34.5 s of margin**. After the
    final encode, `ffprobe` the runtime and record it in the build log. **If the encoded cut
    lands under 480 s, the expansion failed and nothing downstream of it matters.**
