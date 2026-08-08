---
summary: US/English script for «Japanese Money Methods». LONG tier, per-line chapter architecture — 92 single-sentence VO lines across 8 chapters, 9,619 chars ≈ 11:11 at the format.json en rate. Edited by fin-audit-en-1 (1.2, 1.5, 3.8, 3.9, 5.7, 6.14 cue, 6.15) — see audit-en.md. A US REWRITE, not a translation of script-hi.md — dollars, US shocks, US institutions, US b-roll. No Japan-vs-US saving-rate head-to-head anywhere; the only cross-market beat is the single BOJ table that states both markets itself. Every number traces to videos/japanese-money-methods/facts-staging.md.
updated: 2026-08-01
source: run.json creator brief + premise_correction (2026-08-01) + facts-staging.md attempt 1 + study note knowledge/video-studies/japanese-money-methods.md + knowledge/us-english-script-style.md. Architecture ledger-rail per run.json; layout spec from knowledge/finance-audit-2026-07-29/03-design.md §4A. script-hi.md was read for STRUCTURE ONLY.
stage: fin-script, cut en, attempt 1
---

# «Japanese Money Methods» — US / English edition (LONG, per-line chapters)

**Studio project (to build):** `studio/videos/japanese-money-methods-en`
**Voice:** ElevenLabs **Brian** `nPczCjzI2devNBz1zQrb`, `eleven_multilingual_v2`, style 0.
**On-screen text:** English + romaji. **Title + description:** English.
**Architecture:** `ledger-rail` (run.json). **LONG tier → per-line chapters** — none of the
9-segment blockframe constants apply, and `lines: 9` on the `ledger-rail` registry entry is
a SHORT-tier constant. **One line = one TTS clip = one scene = one exact timeline anchor.**

**Engine rule:** digits are **spelled out** in every VO line (bare Latin digits are a
coin-flip reading in ElevenLabs). On-screen numerals carry the exact figures,
`Intl.NumberFormat("en-US")` grouping.

**Persona rules (YouTube 2026 AI carve-out):** no host persona, no first-person expertise,
no fund/stock/account pick. **I** and **we** appear nowhere in the VO. The card APR and the
savings account appear **only as price evidence and as a generic institution** — never as
"put your money here".

---

> ### ⚠ THE SEVEN THINGS THAT MUST NOT ENTER THIS CUT
> 1. **This is a US rewrite, not a translation.** The Indian cut's currency glyph, lakh,
>    crore, UPI, PPF, SIP, a passbook, a wedding envelope, a two-wheeler — none of them may
>    appear in this file, in a cue, or in a photograph.
> 2. **NEVER a Japan-vs-US saving-rate comparison** — spoken, on screen, or implied by
>    adjacency. Three different definitions (`facts-staging.md` §1, §6). **The US personal
>    saving rate (U1 2.7%, U2 3.0%) is therefore not used at all** — see "Deliberately NOT
>    used". The ONE sanctioned cross-market beat is 3.5, the BOJ table that states Japan and
>    the US itself, and it is an **asset-mix** comparison, labelled as such on screen.
> 3. **NEVER "Japanese people save because of their culture."** Horioka (NBER WP 33181, J7):
>    culture, tradition and national character are **not a major determinant**. Chapter 3
>    says the opposite of the source video, out loud.
> 4. **NEVER a dollar equivalent of a yen figure.** J4/J5 stay in yen or become percentages.
> 5. **NEVER a number attached to mottainai, hara hachi bu or taru wo shiru.** They are
>    principles. No calories, no lifespans, no "kakeibo saves you 35%" (§5.2 — searched, no
>    study exists).
> 6. **NEVER attribute the four kakeibo pillars to Hani Motoko or to 1904.** She gets the
>    budget-first idea (HARD); Needs/Wants/Culture/Unexpected is the modern English
>    repackaging (SOFT). Line 6.7 says so on the record — that honesty is the moat.
> 7. **NEVER "121 years old."** Say "nineteen oh four" or "over a hundred years ago". The
>    publisher counted the 120th in 2025 from the **1905** edition.

---

## Title options (English)

1. **The Japanese Money Method: 37.8% And 1% Are The Same Country**
   *(recommended — the two-number hook is the premise correction, and it is checkable)*
2. 4 Japanese Money Methods That Are In No Finance Course
3. Japan Saves 37 Percent? Here Is What That Number Actually Counts

⚠ The source video's title question ("why Japanese people don't go broke") is **retired**
with the premise. Do not restore it in packaging.

---

## Chapters (ship as YouTube chapters — study conclusion 10; nobody in the packet has them)

| # | Chapter | starts | lines | chars |
|---|---|---|---|---|
| 1 | Your paycheck month | 0:00 | 10 | 872 |
| 2 | Japan's own two numbers | 1:02 | 11 | 1,164 |
| 3 | Where that money actually goes | 2:23 | 12 | 1,340 |
| 4 | Mottainai | 3:56 | 13 | 1,324 |
| 5 | Hara Hachi Bu | 5:28 | 12 | 1,387 |
| 6 | Kakeibo | 7:04 | 15 | 1,500 |
| 7 | **Taru wo Shiru** (the unpromised fourth) | 8:49 | 11 | 1,197 |
| 8 | Tonight's one job + recap | 10:12 | 8 | 835 |

---

## Timing budget

English narration = **16.1 chars/s** (`format.json cuts.en.chars_per_second`). LONG charges
**0.25s lead-in + 0.55s tail per line** (`tiers.long`) = **0.8 × 92 = 73.6s** of inter-line
padding.

**Budget formula** — the fix `cuts.en._chars_per_second_trap` demands: padding is not audio,
so it comes out of the target *before* the rate is applied.
`(660 − 73.6) × 16.1 = 9,441 char budget`. This draft is **9,619 (+1.9%)** after the
fin-audit-en-1 edits (1.2, 1.5, 3.8, 3.9, 5.7, 6.15 — net +38 chars).

| Ch | lines | chars | VO | + padding | runtime | starts |
|---|---|---|---|---|---|---|
| 1 | 10 | 872 | 54.2s | 8.0 | 62.2s | 0:00 |
| 2 | 11 | 1,164 | 72.3s | 8.8 | 81.1s | 1:02 |
| 3 | 12 | 1,340 | 83.2s | 9.6 | 92.8s | 2:23 |
| 4 | 13 | 1,324 | 82.2s | 10.4 | 92.6s | 3:56 |
| 5 | 12 | 1,387 | 86.1s | 9.6 | 95.7s | 5:28 |
| 6 | 15 | 1,500 | 93.2s | 12.0 | 105.2s | 7:04 |
| 7 | 11 | 1,197 | 74.3s | 8.8 | 83.1s | 8:49 |
| 8 | 8 | 835 | 51.9s | 6.4 | 58.3s | 10:12 |
| | **92** | **9,619** | **597.5s** | **73.6s** | **671.1s** | |

**Estimated runtime 671.1s (11:11) vs the 660s target — 1.7% over.**

### ⚠ The two-rate hedge (read before cutting or padding this script)

`format.json` carries **two** truths for this cut and they disagree by 10%:
`cuts.en.chars_per_second` is **16.1**, and `cuts.en._chars_per_second_trap` records that
`first-lakh-first-thousand-en` actually delivered **17.73 c/s flat**, with the explicit
instruction *"Fix the budget formula FIRST, then the rate"* — and *"DO NOT raise this key
on its own."* The formula fix is applied above; the key is not this stage's to change
(`tools/` is not writable here). So this draft is sized to survive **both** readings:

| If the real flat rate is | VO | + 73.6s padding | runtime | vs 660 target | vs LONG floor 600 |
|---|---|---|---|---|---|
| 16.1 c/s (the key) | 597.5s | 73.6s | **671.1s** | +1.7% | +71.1s |
| 17.73 c/s (measured) | 542.5s | 73.6s | **616.1s** | −6.6% | +16.1s |

Budgeting at 16.1 alone would have shipped 9,441 chars → 606s at the measured rate, six
seconds off breaching `tiers.long.min_seconds`. Budgeting at 17.73 alone would have shipped
10,396 chars → 719s at the key's rate, 9% long. **9,619 is inside the overlap.** After the real
clips exist, `pipeline_check` measures every one of them; if the flat rate lands at 17.73
again, the honest fix is to raise the key with the measurement, not to re-pad this script.

**Pace:** 671.1 / 92 = **7.29s average scene** (`target_scene_seconds` 6.5,
`max_scene_seconds` 9.0). Longest line 128 chars → 8.0s VO + 0.8 = **8.8s**, under the
photo-hold ceiling at 16.1 and 8.0s at 17.73. Shortest 61 chars → 3.8s, well over
`tts.min_clip_seconds` 1.0. **No line may exceed 130 characters** — that is where a scene
breaches the hold check at the slower of the two rates.

### Where the retention beats land

- **Promise** inside **1.2**: the clause opens ≈**8.7s** and closes ≈**13.2s**, inside the
  fifteen-second gate. 2.1 at **1:02** then expands it. The pain-mirror still runs the whole
  of chapter 1 with zero stats, entirely second person; only the roadmap moved forward.
  ⚠ Study conclusion 1 ("TOP spends 40s before its first promise") does **not** override the
  gate — that note has been corrected, and the hi cut took the same edit at its 1.2.
- **First number** at 2.3 = **1:17**.
- **Mid-video drop zone (55–65% = 6:09–7:16)** opens on **5.11 at 6:47 = 60.7%**, the honesty
  beat — "if the bills already eat the whole paycheck, this fails in month one, and that is
  not your fault" — then 5.12, a tension bridge. Not a flat transition.
- **~70%** lands on **6.7 at 7:46 = 69.4%**: the famous four categories are told, on
  the record, to be a later Western addition. The video's most distinctive moment is an
  admission.
- **The unpromised fourth method** opens at **8:49 = 78.9%** (TOP's ran 72–87%).
- **One stacked CTA**, once, at 8.7–8.8 ≈ **97.8%**.

---

## Per-scene timing budget

`chars` → `est s` at 16.1 chars/s. Add 0.8s per line for lead-in + tail to get scene duration.

| # | chars | est s | | # | chars | est s | | # | chars | est s |
|---|---|---|---|---|---|---|---|---|---|---|
| 1.1 | 68 | 4.2 | | 4.1 | 101 | 6.3 | | 6.7 | 101 | 6.3 |
| 1.2 | 119 | 7.4 | | 4.2 | 103 | 6.4 | | 6.8 | 103 | 6.4 |
| 1.3 | 90 | 5.6 | | 4.3 | 112 | 7.0 | | 6.9 | 100 | 6.2 |
| 1.4 | 97 | 6.0 | | 4.4 | 84 | 5.2 | | 6.10 | 95 | 5.9 |
| 1.5 | 97 | 6.0 | | 4.5 | 102 | 6.3 | | 6.11 | 94 | 5.8 |
| 1.6 | 90 | 5.6 | | 4.6 | 112 | 7.0 | | 6.12 | 91 | 5.7 |
| 1.7 | 72 | 4.5 | | 4.7 | 103 | 6.4 | | 6.13 | 91 | 5.7 |
| 1.8 | 91 | 5.7 | | 4.8 | 104 | 6.5 | | 6.14 | 118 | 7.3 |
| 1.9 | 87 | 5.4 | | 4.9 | 107 | 6.6 | | 6.15 | 115 | 7.1 |
| 1.10 | 61 | 3.8 | | 4.10 | 85 | 5.3 | | 7.1 | 95 | 5.9 |
| 2.1 | 110 | 6.8 | | 4.11 | 118 | 7.3 | | 7.2 | 112 | 7.0 |
| 2.2 | 113 | 7.0 | | 4.12 | 112 | 7.0 | | 7.3 | 96 | 6.0 |
| 2.3 | 104 | 6.5 | | 4.13 | 81 | 5.0 | | 7.4 | 116 | 7.2 |
| 2.4 | 80 | 5.0 | | 5.1 | 118 | 7.3 | | 7.5 | 113 | 7.0 |
| 2.5 | 111 | 6.9 | | 5.2 | 102 | 6.3 | | 7.6 | 118 | 7.3 |
| 2.6 | 106 | 6.6 | | 5.3 | 94 | 5.8 | | 7.7 | 104 | 6.5 |
| 2.7 | 99 | 6.1 | | 5.4 | 93 | 5.8 | | 7.8 | 109 | 6.8 |
| 2.8 | 99 | 6.1 | | 5.5 | 122 | 7.6 | | 7.9 | 99 | 6.1 |
| 2.9 | 123 | 7.6 | | 5.6 | 123 | 7.6 | | 7.10 | 117 | 7.3 |
| 2.10 | 100 | 6.2 | | 5.7 | 119 | 7.4 | | 7.11 | 118 | 7.3 |
| 2.11 | 119 | 7.4 | | 5.8 | 126 | 7.8 | | 8.1 | 95 | 5.9 |
| 3.1 | 103 | 6.4 | | 5.9 | 125 | 7.8 | | 8.2 | 99 | 6.1 |
| 3.2 | 108 | 6.7 | | 5.10 | 115 | 7.1 | | 8.3 | 119 | 7.4 |
| 3.3 | 102 | 6.3 | | 5.11 | 126 | 7.8 | | 8.4 | 91 | 5.7 |
| 3.4 | 111 | 6.9 | | 5.12 | 124 | 7.7 | | 8.5 | 110 | 6.8 |
| 3.5 | 128 | 8.0 | | 6.1 | 106 | 6.6 | | 8.6 | 107 | 6.6 |
| 3.6 | 111 | 6.9 | | 6.2 | 90 | 5.6 | | 8.7 | 117 | 7.3 |
| 3.7 | 109 | 6.8 | | 6.3 | 89 | 5.5 | | 8.8 | 97 | 6.0 |
| 3.8 | 119 | 7.4 | | 6.4 | 96 | 6.0 | | | | |
| 3.9 | 118 | 7.3 | | 6.5 | 116 | 7.2 | | | | |
| 3.10 | 108 | 6.7 | | 6.6 | 95 | 5.9 | | | | |
| 3.11 | 118 | 7.3 | | | | | | | | |
| 3.12 | 105 | 6.5 | | | | | | | | |

Char counts are a budget estimate (±5%); the build step recounts them programmatically from
the extracted lines file, then ffprobe-measures every clip.

---

## The ledger-rail spec, as this script uses it

`knowledge/finance-audit-2026-07-29/03-design.md` §4A:

- **`.scene` is `grid-template-columns: 300px 1fr`.** The left rail carries the scene id at
  96px **weight 200**, a `--muted` hairline, then the beat label at 26px tracked 4px. At
  LONG the label is the **chapter name**, persisting for the whole chapter so the rail
  reads as a spine.
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
> **Slice these strings — never retype them.**

---

## Chapter 1 — Your paycheck month (PAIN-MIRROR COLD OPEN · no stat, no greeting, no roadmap)

*Study conclusion 1. Sixty-two seconds, entirely second person, entirely concrete, and not
one number — the cost of entry is paid in recognition. No title card anywhere. Every frame
in this chapter is an American kitchen, not Japan. **The payoff promise sits inside 1.2
(≈8.7–13.2s)**, not at 2.1: check 3 of the audit gate is a hard fifteen-second rule and
outranks the study note's 40-second finding.*

**1.1**
> The first of the month, and the direct deposit lands in the account.

`[RAIL OFF | img: a phone face-up on a kitchen counter at night, banking notification glow, no face | head: IT LANDED | stmt: The deposit is in.]`

**1.2**
> For about two seconds that notification feels like relief, and three old Japanese methods are what make it last longer.

`[rail 1.2 · YOUR PAYCHECK MONTH | img: same counter, tighter crop — ONE continuous zoom across 1.1 and 1.2 | head: TWO SECONDS | stmt: Three Japanese methods make it last longer. | AUDIT fin-audit-en-1: rewritten — check 3. The draft deferred every payoff promise to 2.1 at 0:59; the promise clause now opens ≈8.7s and closes ≈13.2s.]`

**1.3**
> Then rent goes out. Then the electric bill, which is somehow higher than it was last year.

`[rail 1.3 | img: a utility bill and a lease payment stub on a counter under a fridge magnet | head: THEN RENT | stmt: Then the power bill. Higher again. | colour: --warn]`

**1.4**
> Then the car insurance renewal, the one you forgot bills every six months instead of every month.

`[rail 1.4 | img: an auto-insurance renewal letter half out of its envelope on a kitchen table | head: THEN THE RENEWAL | stmt: The six-month bill you budget like a monthly one.]`

**1.5**
> A birthday gift, two food delivery orders, and one streaming service that quietly renewed itself.

`[rail 1.5 | img: a delivery bag and a gift bag on the same counter, receipts under both — NO readable brand marks on the bag | head: AND THEN | stmt: One gift. Two delivery orders. One auto-renewal. | AUDIT fin-audit-en-1: "DoorDash" → "food delivery" — check 4. A named platform in VO, and not as price evidence. The screen cue was already generic, so the VO was the only place it appeared.]`

**1.6**
> Nothing on that list was big. Every one of them was small, and every one of them was fair.

`[rail 1.6 | img: a spread of small paper receipts fanned across a kitchen table | head: NOTHING WAS BIG | stmt: Every one was small. Every one was fair.]`

**1.7**
> And by the twentieth the balance looks like the paycheck never arrived.

`[rail 1.7 | img: a wall calendar with the 20th circled, evening light through a window | head: BY THE 20th | stmt: The balance looks like payday never happened. | colour: --warn]`

**1.8**
> So you scroll back through the statement, looking for the one big expense that explains it.

`[rail 1.8 | img: a hand scrolling a bank statement on a laptop, screen text illegible, hand only | head: YOU GO LOOKING | stmt: For the one big line that explains it.]`

**1.9**
> It is not in there. The money did not go to one place, it went a little bit everywhere.

`[rail 1.9 | img: water draining through many small holes in a metal colander | head: IT IS NOT THERE | stmt: Not one place. A little everywhere. | colour: --warn]`

**1.10**
> If that is your month, every month, then this one is for you.

`[rail 1.10 | img: an empty chair at a kitchen table, one lamp on | head: IS THAT YOURS? | stmt: Then this one is for you.]`

---

## Chapter 2 — Japan's own two numbers (THE PROMISE + THE NUMBER)

*The premise correction lives here. The debunk runs on Japan's OWN two published numbers —
one government, one year, two surveys — so no cross-market comparison is needed or made.
`facts-staging.md` J1/J2/J3.*

**2.1**
> Today, three Japanese money methods that are centuries old, and that are taught in no finance course anywhere.

`[rail 2.1 · JAPAN'S TWO NUMBERS | img: a wooden noren curtain over a Japanese shopfront at dusk | head: THREE METHODS | stmt: Centuries old. In no finance course. | colour: --fund]`

**2.2**
> But first, the number that put Japan on your feed in the first place, because that number is doing a lot of work.

`[rail 2.2 | img: a phone held up showing a blurred short-video feed, hand only | head: FIRST, THE NUMBER | stmt: The one that put Japan on your feed.]`

**2.3**
> The internet says a regular Japanese household saves thirty-seven percent of its pay every single month.

`[rail 2.3 | img: a printed statistics table, macro, one row in focus | head: THE CLAIM | num: 37.8% | foot: Statistics Bureau of Japan, Kakei Chosa 2024 annual summary, Table I-2-2 | colour: --target]`

**2.4**
> That number is real. It is not made up, and Japan's own government publishes it.

`[rail 2.4 | img: a government publication cover on a desk, official seal visible | head: IT IS REAL | stmt: Japan's own government publishes it.]`

**2.5**
> In the twenty twenty-four Family Income and Expenditure Survey, the number is thirty-seven point eight percent.

`[rail 2.5 | img: the same table, wider — columns of figures | head: THE SURVEY | num: 37.8% | foot: FIES 2024, salaried-worker households: surplus JPY 197,432 of disposable JPY 522,569 | colour: --target]`

**2.6**
> The same year, the same government's national accounts put the household saving rate at about one percent.

`[rail 2.6 | img: a second, thicker bound volume beside the first | head: THE SAME YEAR | num: ABOUT 1% | foot: National Accounts (SNA) household saving rate, calendar 2024 — Horioka, NBER WP 33181, p.7 | colour: --target]`

**2.7**
> One country. One year. One government. And a gap between the two figures of more than thirty times.

`[RAIL OFF | img: two brass weights of visibly different size on a balance scale | head: ONE GOVERNMENT. ONE YEAR. | num: 30 TIMES | foot: "more than 30 times as high" — Horioka, NBER WP 33181, p.7 | colour: --warn]`

**2.8**
> The difference is not Japanese discipline, and it is not a secret. It is who gets counted, and how.

`[rail 2.8 | img: two clipboards side by side carrying different forms | head: THE DIFFERENCE | stmt: Who is counted. And how.]`

**2.9**
> The thirty-seven counts salaried households only. The other one counts everybody, including retirees and the self-employed.

`[rail 2.9 | img: a crowded Osaka pedestrian crossing, wide, faces indistinct | head: WHO IS IN | stmt: 37.8% counts salaried households only. The other counts everyone. | foot: Horioka p.7 — the National Accounts include the self-employed, unemployed, retired and unincorporated enterprises]`

**2.10**
> Both numbers are true. Only the big one travels, because the small one does not sell on a thumbnail.

`[rail 2.10 | img: a newspaper folded so only the headline shows | head: BOTH ARE TRUE | stmt: Only one of them travels. | colour: --warn]`

**2.11**
> So the real question is what actually survives inside these methods, and what it does to four thousand dollars a month.

`[rail 2.11 | img: four twenty-dollar bills laid flat on a plain grey card | head: THE REAL QUESTION | stmt: What survives in the methods — and what it does to $4,000 | foot: $4,000/mo take-home is this channel's worked example, not a national average. US real median household income was $83,730 in 2024 (Census P60-286).]`

---

## Chapter 3 — Where that money actually goes (THE EVIDENCE CHAPTER)

*J5 (the surplus split), J8/U3 (the one BOJ table that states two markets itself — the ONLY
sanctioned cross-market comparison in this video, and an asset-mix one), J6 (the real
high-saving era) and J7 (culture is rejected by the primary literature).*

**3.1**
> That same survey also records where the monthly surplus actually goes, which is the part nobody quotes.

`[rail 3.1 · WHERE IT GOES | img: a bank ledger page open on a counter, columns of entries | head: THE SAME SURVEY | stmt: It also records where the surplus goes.]`

**3.2**
> About ninety percent of it goes straight into bank deposits. About three percent goes into stocks and bonds.

`[rail 3.2 | img: a teller counter with a stack of deposit slips, no faces | head: WHERE IT LANDS | stmt: About 90% into deposits. About 3% into securities. | foot: ILLUSTRATIVE — computed from the FIES 2024 monthly surplus split (deposits JPY 175,241 · securities JPY 6,705 of JPY 197,432) | colour: --target]`

**3.3**
> So Japan saves hard, and then puts almost none of that saving to work, which is a very different thing.

`[rail 3.3 | img: a row of closed safe-deposit boxes, all shut | head: SAVING IS NOT INVESTING | stmt: Japan saves hard and puts very little of it to work.]`

**3.4**
> One Bank of Japan table says fifty-one percent of Japanese household financial assets sit in cash and deposits.

`[rail 3.4 | img: a printed central-bank chart page under a desk lamp | head: JAPAN | num: 51.0% | foot: Cash and deposits, share of household financial assets — Bank of Japan Flow of Funds, Chart 2, end-March 2025 | colour: --target]`

**3.5**
> The next column of the same table puts American households at eleven point five percent in cash and forty-one percent in stocks.

`[rail 3.5 | img: the same chart page, the second column in focus | head: SAME TABLE, NEXT COLUMN | stmt: US cash 11.5% · US equity 41.5% | foot: The SAME BOJ table states both markets — no conversion, no second source. ASSET MIX ONLY. This is NOT a saving-rate comparison. | colour: --target]`

**3.6**
> That is the half of the story most videos skip. Japan is an example of saving, and not an example of investing.

`[rail 3.6 | img: a sealed jar, full, lid still on | head: THE HALF NOBODY SHOWS | stmt: An example of saving. Not of investing.]`

**3.7**
> And here is the part almost nobody mentions. Japan was not always a nation of savers, and the timing matters.

`[rail 3.7 | img: a black-and-white 1950s Tokyo street scene, archival grain | head: AND ONE MORE THING | stmt: Japan was not always a nation of savers. | colour: --warn]`

**3.8**
> After the war, the rate was above fifteen percent for exactly twenty-five years, from nineteen sixty-one to eighty-six.

`[rail 3.8 | img: an old wall calendar page, a range of years visible | head: THE POSTWAR HIGH-SAVING ERA | stmt: 1961 to 1986. Twenty-five years. | foot: POSTWAR ONLY — Horioka, NBER WP 33181, p.3. The wartime rate reached 44%, so this is the postwar record, not the all-time one. | colour: --target | AUDIT fin-audit-en-1: rewritten — check 1. Horioka p.3 restricts the claim to "if we confine ourselves to the postwar period"; the unqualified sentence was false against its own citation.]`

**3.9**
> Its postwar peak was near twenty-three percent, and since two thousand two it has hardly ever been above five percent.

`[rail 3.9 | img: a hand-drawn line on graph paper, peak then decline | head: THE POSTWAR PEAK | num: 23.2% | foot: Postwar peak, mid-1970s. No higher than 5% since 2002 apart from a temporary 2020 Covid blip, and negative in 2013-15, 2017 and 2023 — Horioka p.2 | colour: --warn | AUDIT fin-audit-en-1: rewritten — check 1. Horioka p.2 carves out "a temporary blip in 2020 due to the Covid-19 pandemic", which the absolute "has not been" denied; and the 23.2% is the POSTWAR peak (44% in the war years).]`

**3.10**
> The largest study of that history says the cause was not culture, not tradition, and not national character.

`[rail 3.10 | img: a thick working paper on a desk, one paragraph in focus | head: NOT CULTURE | stmt: "Culture, tradition and national character are not a major determinant." | foot: Horioka, NBER WP 33181, sections 3 and 9-10 | colour: --warn]`

**3.11**
> The causes were no consumer credit, no safety net, fast income growth, a tax break, and a government savings campaign.

`[rail 3.11 | img: a vintage government savings-campaign poster on a wall | head: THE ACTUAL REASONS | stmt: No consumer credit · No safety net · Fast income growth · A tax break · A state campaign | foot: Horioka, NBER WP 33181, sections 9-10]`

**3.12**
> So the methods work. They were simply never the reason. That is the most honest line in this whole video.

`[RAIL OFF | img: a single lit paper lantern in a dark street, wide | head: THE HONEST LINE | stmt: The methods work. They were never the reason. | colour: --fund]`

---

## Chapter 4 — Mottainai (METHOD ONE · the participation beat)

*TOP's move 3, the device none of our shipped videos has: three physical checks the viewer
performs inside the video. `facts-staging.md` §4 — HARD on the meaning, SOFT on the
etymology detail (the government page 403'd), **zero numbers attached to the principle**.
The three check frames are American: a closet, a phone's subscriptions screen, a fridge.*

**4.1**
> Method one is mottainai. Roughly translated, it means the real value of a thing quietly going unused.

`[rail 4.1 · MOTTAINAI | img: a chipped ceramic bowl repaired with visible seams on a wooden board | head: MOTTAINAI | stmt: A thing's real value, going unused. | foot: Roughly, from mottai, "a thing's rightful worth", plus nai, "without" — attested since about the 13th century]`

**4.2**
> It is not a lecture about waste. It is regret that something you already paid for was never fully used.

`[rail 4.2 | img: a folded cloth with a worn edge, mended by hand | head: NOT A SCOLDING | stmt: It is regret. Not instruction.]`

**4.3**
> The shirt hanging in your closet holds a farmer's crop, a mill's hours, a truck's diesel, and a store's shelf.

`[rail 4.3 | img: a cotton field at dawn, wide | head: ONE SHIRT | stmt: A farmer's crop. A mill's hours. A truck's diesel.]`

**4.4**
> It also holds the hours of your own working life, the ones you traded to pay for it.

`[rail 4.4 | img: a wall clock in an office corridor, evening | head: AND YOURS | stmt: The hours of your own pay that bought it. | colour: --warn]`

**4.5**
> Pause this video. Stand up, open your closet, and count the clothes that are still wearing their tags.

`[rail 4.5 | img: an open American closet, hangers dense, price tags still on two garments | head: PAUSE. CHECK ONE. | stmt: Count the clothes still wearing their tags. | colour: --fund]`

**4.6**
> Then open your phone, go to the subscriptions screen, and read the whole list of things billing you every month.

`[rail 4.6 | img: a phone's subscriptions settings list on a table, screen text illegible, hand only | head: CHECK TWO | stmt: The subscriptions screen. All of it. | colour: --fund]`

**4.7**
> Then open the refrigerator and look at the food that is going to be thrown out by the end of next week.

`[rail 4.7 | img: an open refrigerator shelf, takeout containers and wilting greens | head: CHECK THREE | stmt: What gets thrown out next week. | colour: --fund]`

**4.8**
> None of that is a shortage of money. All three of them are value you already bought and then never used.

`[rail 4.8 | img: a stack of unopened delivery boxes in the corner of a room | head: WHAT YOU SAW | stmt: Not a shortage of money. Value already bought and never used. | colour: --warn]`

**4.9**
> Mottainai collapses into a single question, and the question gets asked before the purchase, never after it.

`[rail 4.9 | img: a hand hovering over a store shelf, not yet touching, hand only | head: IT IS ONE QUESTION | stmt: And it is asked before, not after.]`

**4.10**
> Will its full value actually get used? If the answer is maybe, then the answer is no.

`[RAIL OFF | img: a single object on a bare wooden table, hard side light | head: THE QUESTION | stmt: Will its full value be used? If the answer is MAYBE, the answer is NO. | colour: --fund]`

**4.11**
> On four thousand dollars a month that question comes up maybe three or four times, and every time it stops a purchase.

`[rail 4.11 | img: a shopping cart abandoned mid-aisle in a US grocery store | head: ON $4,000 | stmt: The question comes up three or four times a month. | foot: $4,000/mo take-home is the channel's worked example — not a statistic]`

**4.12**
> That is the whole job of mottainai. It is not about spending less, it is about using up what was already bought.

`[rail 4.12 | img: a worn, resoled leather boot beside a new one still in its box | head: THE WHOLE POINT | stmt: Not spending less. Using fully what was bought.]`

**4.13**
> The next method starts at the dinner table, and it ends inside your bank account.

`[rail 4.13 | img: a simple set meal in small bowls, top-down | head: NEXT | stmt: The next one starts at the dinner table.]`

---

## Chapter 5 — Hara Hachi Bu (METHOD TWO · the day-one rule)

*The principle carries **zero** numbers — `facts-staging.md` §5.5 rejects every calorie,
intake and lifespan figure attached to it. The only figures here are Japan's own FIES
consumption share (J4) and the channel's $4,000 worked example. 5.11 is the honesty beat and
sits inside the 55–65% drop zone by design.*

**5.1**
> Method two is hara hachi bu, an old Okinawan habit with Confucian roots, and it has nothing to do with money at first.

`[rail 5.1 · HARA HACHI BU | img: Okinawan elders walking a shoreline path at sunrise, distant, no faces | head: HARA HACHI BU | stmt: An old Okinawan habit, Confucian in origin. | foot: No calorie, intake or lifespan figure is claimed here — every one in circulation is unsourced]`

**5.2**
> It means you stop eating when your stomach is eight parts full out of ten, not when the plate is empty.

`[rail 5.2 | img: a small rice bowl, deliberately not full, top-down on wood | head: EIGHT PARTS IN TEN | stmt: Stop there.]`

**5.3**
> Fullness arrives late, so the last two parts are always more than the body actually asked for.

`[rail 5.3 | img: a hand setting chopsticks down across a bowl, hand only | head: WHY IT WORKS | stmt: Fullness arrives late. The last two parts are surplus.]`

**5.4**
> Now put that same rule on a paycheck. Live on eight parts, and move two parts out on day one.

`[rail 5.4 | img: an American kitchen counter, a small stack of bills pushed to one side | head: NOW THE PAYCHECK | stmt: Live on eight parts. Move two out on day one. | colour: --fund]`

**5.5**
> On four thousand dollars a month, two parts is eight hundred dollars moved out, and thirty-two hundred dollars to live on.

`[rail 5.5 | img: two unequal stacks of twenty-dollar bills squared on a table | head: ON $4,000 | stmt: $800 out · $3,200 to live on | foot: 20% of the channel's $4,000 worked example. An arithmetic split, not a statistic. | colour: --fund]`

**5.6**
> And it happens the day after payday, not on the thirtieth, because whatever is left at the end of the month is always zero.

`[rail 5.6 | img: an empty wallet lying open on a counter at month end | head: DAY ONE, NOT DAY THIRTY | stmt: What is left at month end is always zero. | colour: --warn]`

**5.7**
> Automate it so it moves without a decision, into an account that is separate from the one the card and the bills touch.

`[rail 5.7 | img: a laptop showing a scheduled recurring transfer screen, amounts illegible | head: AUTOMATICALLY, NOT HEROICALLY | stmt: A separate account. Not the one the card touches. | foot: No account type, bank, app or fund is named or recommended anywhere in this video. | colour: --fund | AUDIT fin-audit-en-1: rewritten — checks 4 and 7. "A federally insured savings account" plus an on-screen HIGH-YIELD SAVINGS · FDIC INSURED row is a product-category placement recommendation; a disclaimer under a recommendation is still a recommendation (same standard applied to hi 6.14). The mechanic — automation and separation — is what the method needs, and it survives intact.]`

**5.8**
> This is not discipline, and it is not about willpower. It is one decision on day one that carries the other twenty-nine days.

`[rail 5.8 | img: a light switch in the on position, dust on the plate | head: NOT DISCIPLINE | stmt: One decision on day one, carrying the other twenty-nine.]`

**5.9**
> In Japan's own survey, salaried households spend only sixty-two percent of their take-home pay, and the rest is that surplus.

`[rail 5.9 | img: the FIES table again, the consumption row in focus | head: JAPAN'S OWN FIGURE | num: 62.2% | foot: Average propensity to consume, salaried-worker households — Statistics Bureau FIES 2024, Table I-2-2. Japan's own number; not compared with any other country's. | colour: --target]`

**5.10**
> If twenty percent is too much right now, start at five percent, which on that same paycheck is two hundred dollars.

`[rail 5.10 | img: a single twenty-dollar bill beside a much thicker folded stack | head: IF 20% IS TOO MUCH | num: $200 | foot: 5% of the $4,000 worked example | colour: --fund]`

**5.11**
> And here is the honest part. If the bills already eat the whole paycheck, this fails in month one, and that is not your fault.

`[rail 5.11 | img: a long straight highway disappearing at the horizon | head: HONESTLY | stmt: If the bills already eat the paycheck, this fails in month one. | colour: --warn]`

**5.12**
> Then the problem is not saving, it is accounting, and the accounting method was written by a woman over a hundred years ago.

`[rail 5.12 | img: an old bound ledger, spine cracked, on a shelf | head: THEN THE QUESTION CHANGES | stmt: Not saving. Accounting. | colour: --target]`

---

## Chapter 6 — Kakeibo (METHOD THREE · and the admission at the ~70% mark)

*Line 6.7 is this video's Von Restorff beat and lands at 7:46 ≈ **69.4%**: the famous four
categories are told, on the record, to be a later Western addition (`facts-staging.md` §4 —
SOFT, no Japanese primary found). Every competitor teaches them as Hani Motoko's. Saying
otherwise is the whole differentiator.*

**6.1**
> Method three is kakeibo. It translates as household account book, and it is written by hand, once a month.

`[rail 6.1 · KAKEIBO | img: a hand-ruled household ledger open on a low table, pen resting | head: KAKEIBO | stmt: The household account book. Written by hand.]`

**6.2**
> It was created in nineteen oh four by Hani Motoko, who was Japan's first woman journalist.

`[rail 6.2 | img: an early-1900s Japanese magazine cover, archival | head: 1904 | stmt: Hani Motoko. Japan's first woman journalist. | foot: Fujin no Tomo Sha (publisher primary) + National Diet Library. First edition printed end-1904, for use in the 1905 year. | colour: --target]`

**6.3**
> It has been printed every single year since then, with four years missing during the war.

`[rail 6.3 | img: a shelf of identical annual editions, spines aligned | head: STILL PRINTED | stmt: Every year since. Four wartime years missing. | foot: Over a hundred years of continuous publication — the publisher marked the 120th in 2025]`

**6.4**
> Her actual invention was not a four column chart. Her actual invention was the idea of a budget.

`[rail 6.4 | img: a blank ruled page, no headings yet | head: HER ACTUAL INVENTION | stmt: Not the four-column chart. The budget.]`

**6.5**
> Divide the year's income by twelve, set the saving aside first, and then split whatever is left across the expenses.

`[rail 6.5 | img: twelve small equal stacks of coins in a row on wood | head: THE METHOD | stmt: Divide the year by twelve. Set the saving aside FIRST. Then split the rest. | colour: --fund]`

**6.6**
> In nineteen oh four that was a new idea. Saving gets decided before the spending, not after it.

`[rail 6.6 | img: an inkwell and nib on a wooden desk, low light | head: WHY IT WAS NEW | stmt: Saving is decided before spending, not after.]`

**6.7**
> The four categories everybody teaches today, needs, wants, culture, and unexpected, came a lot later.

`[RAIL OFF | img: THE FLAT-LAY (study conclusion 3) — top-down on wood: real US coins and bills in four groups, four handwritten labels IN THE PHOTOGRAPH, not overlaid: NEEDS · WANTS · CULTURE · UNEXPECTED | head: THE FOUR CATEGORIES | stmt: These came later. They are the version that travelled west. | foot: Consistent across secondary sources; no Japanese primary attributes them to Hani Motoko or to 1904 | colour: --warn]`

**6.8**
> No Japanese source attributes them to Hani Motoko, and her own ledger used a different set of headings.

`[rail 6.8 | img: the same flat-lay, tighter crop on one handwritten label — ONE continuous zoom from 6.7 | head: SAY IT PLAINLY | stmt: Her own expense headings were different ones.]`

**6.9**
> What actually survives is four questions, and they get asked at the start of the month, not the end.

`[rail 6.9 | img: a fresh page, dated at the top, nothing written yet | head: WHAT SURVIVES | stmt: Four questions. Asked at the start of the month.]`

**6.10**
> How much came in. How much gets set aside. How much goes out. And what changes from last month.

`[rail 6.10 | img: four short handwritten lines on ruled paper, macro | head: THE FOUR | stmt: How much came in · How much is set aside · How much goes out · What changes | colour: --fund]`

**6.11**
> Notice that question two comes before question three, because that order is the entire method.

`[rail 6.11 | img: the same page, the second line underlined in ink | head: THE ORDER IS THE METHOD | stmt: Question two comes before question three. | colour: --fund]`

**6.12**
> It happens on paper. A pen, a notebook, the phone face down, fifteen minutes, once a month.

`[rail 6.12 | img: a phone lying face-down beside an open notebook and a pen | head: ON PAPER | stmt: Pen. Notebook. Phone face-down. Fifteen minutes.]`

**6.13**
> An app reports where the money went. A paper ledger decides where the money is going to go.

`[rail 6.13 | img: a printed bank statement beside the handwritten page | head: APP vs LEDGER | stmt: An app reports where it went. A ledger decides where it goes.]`

**6.14**
> It decides whether a four hundred dollar surprise is an inconvenience or a card balance at over twenty percent a year.

`[rail 6.14 | img: a car on a shop lift with a repair estimate clipped to the fender | head: WHAT THE SET-ASIDE LINE BUYS | num: OVER 20% | foot: Card APR on accounts assessed interest, 22.15% — May 2026, Federal Reserve G.19 released 8 July 2026. Price evidence, not a recommendation. | colour: --warn | AUDIT fin-audit-en-1 + ORCHESTRATOR RE-CHECK 2026-08-01: the audit was half right and its replacement figure was wrong. Direct fetch of the current G.19 (rel. 8 Jul 2026): there is indeed no "Q2 2026" print, so U7's period label was wrong — but 22.15% IS real and current, as the MAY 2026 monthly figure; 21.52% is Q1 2026 (not 2025 Q4, which was 22.30%) and is not the latest print. Screen now carries 22.15% / May 2026. VO unchanged — "over twenty percent" is true of every recent quarter.]`

**6.15**
> In the latest Federal Reserve survey, about four in ten adults could not cover that four hundred dollars with cash.

`[rail 6.15 | img: a checkout terminal mid-transaction, hands only | head: THE RECEIPT | num: 4 IN 10 | foot: 63% of adults could cover a $400 emergency with cash or its equivalent — Federal Reserve SHED 2025, fielded Oct 2025, released 13 May 2026 | colour: --target | AUDIT fin-audit-en-1: "households" → "adults" — check 1. SHED reports the share of ADULTS; the report's title is about households but the statistic is not a household one.]`

---

## Chapter 7 — Taru wo Shiru (THE UNPROMISED FOURTH · opens at 78.9%)

*Study conclusion 2 — promise N, deliver N+1, and make the extra one a re-frame rather than
a mechanic. Nothing here is new information; it is the reason under the first three. §4 is
HARD on the inscription, the temple and the shared-radical design. The Tokugawa Mitsukuni
donor attribution is SOFT and is **not** used.*

**7.1**
> The promise at the top was three methods. There is a fourth one, and it is the hardest of them.

`[rail 7.1 · TARU WO SHIRU | img: a moss-edged stone path in mist, Kyoto | head: THERE IS A FOURTH | stmt: And it is the hard one. | colour: --target]`

**7.2**
> At Ryoan-ji temple in Kyoto there is a stone water basin with four characters cut around the hole in its center.

`[rail 7.2 | img: the Ryoan-ji rock garden in mist, wide | head: RYOAN-JI, KYOTO | stmt: A stone basin. Four characters cut into it.]`

**7.3**
> Together they say, what there is, is enough, and knowing only that is the whole of the teaching.

`[rail 7.3 | img: the tsukubai basin itself, water surface still, top-down. The kanji live IN the photograph — never as composition text | head: WHAT IT SAYS | stmt: What there is, is enough. | foot: The tsukubai inscription at Ryoan-ji, Kyoto]`

**7.4**
> All four characters share one single part, and that shared part is the emptiness at the centre of the basin.

`[RAIL OFF | img: the basin, macro on the still water at its centre | head: THE DESIGN | stmt: All four share one part — the emptiness at the centre. | colour: --target]`

**7.5**
> On its own, not one of them is a complete character. Each of them needs that emptiness in the middle to be whole.

`[rail 7.5 | img: the same basin, water rings spreading — ONE continuous zoom from 7.4 | head: NONE OF THEM STANDS ALONE | stmt: Each needs the emptiness in the middle to be whole.]`

**7.6**
> Now look at your own last ten years. The degree, the first job, the first paycheck, the phone, the car, the apartment.

`[rail 7.6 | img: a used sedan parked outside a US apartment building, evening | head: NOW YOUR LIST | stmt: Degree. Job. First paycheck. Phone. Car. Apartment.]`

**7.7**
> Every time it felt like the finish line, and every time the line moved a few weeks after you crossed it.

`[rail 7.7 | img: a chalk finish line on asphalt, half rubbed out and redrawn further along | head: EVERY TIME | stmt: The line moved a few weeks after you crossed it. | colour: --warn]`

**7.8**
> Income went up, and the definition of a need went up right behind it, which is why the raise never showed up.

`[rail 7.8 | img: two near-identical jackets on hangers, one newer | head: WHAT HAPPENED | stmt: Income rose. So did the definition of "need".]`

**7.9**
> An entire industry runs on making whatever you already own feel like less than whatever comes next.

`[rail 7.9 | img: a wall of backlit billboards over a night street, text illegible | head: THE WHOLE MARKET | stmt: It runs on what you have feeling like less. | colour: --warn]`

**7.10**
> Taru wo shiru asks one question, and it is the only one here you have to answer for yourself. What is enough for you?

`[rail 7.10 | img: an empty chair facing a window at first light | head: THE QUESTION | stmt: What is enough for you? | colour: --fund]`

**7.11**
> Do not answer that quickly, because three methods tell you how to keep money, and the fourth tells you what it is for.

`[rail 7.11 | img: the Ryoan-ji garden at last light, wide | head: THE DIFFERENCE | stmt: Three tell you how. The fourth tells you what for.]`

---

## Chapter 8 — Tonight's one job + recap (PEAK-END · one stacked CTA)

*Recap in four single lines, then the action while attention is still on the argument, then
the one CTA in eleven minutes. Study conclusion 8 — the share line is a person, not a verb.*

**8.1**
> Mottainai. Before the purchase, ask whether the full value of the thing will actually get used.

`[rail 8.1 · TONIGHT | img: the store shelf from 4.9, hand withdrawn | head: RECAP ONE | stmt: MOTTAINAI — ask before buying, not after.]`

**8.2**
> Hara hachi bu. Move two parts out the day after payday, automatically, and live on the other eight.

`[rail 8.2 | img: the two unequal bill stacks from 5.5, new crop | head: RECAP TWO | stmt: HARA HACHI BU — two parts out the day after payday. Live on eight. | colour: --fund]`

**8.3**
> Kakeibo. Write the four questions on paper at the start of the month, and fill in the saving line before anything else.

`[rail 8.3 | img: the ledger page from 6.10, now filled in | head: RECAP THREE | stmt: KAKEIBO — four questions at the start. Savings line first. | colour: --fund]`

**8.4**
> Taru wo shiru. Decide what is enough for you, or the other three methods do nothing at all.

`[rail 8.4 | img: the still basin from 7.3, later light | head: RECAP FOUR | stmt: TARU WO SHIRU — decide what is enough, or the other three do nothing. | colour: --target]`

**8.5**
> Tonight, one sheet of paper, one pen, and those four questions. Fifteen minutes, and it is done for the month.

`[rail 8.5 | img: a notebook and pen set out under a lamp on an American kitchen table, nothing written yet | head: TONIGHT | stmt: One page. One pen. Four questions. Fifteen minutes. | colour: --fund]`

**8.6**
> What you heard today is information. What you start tonight is the only part of it that changes anything.

`[RAIL OFF | img: the same table, the page now carrying four handwritten lines | head: THE WHOLE VIDEO | stmt: What you heard is information. What you start is understanding.]`

**8.7**
> Comment which of the four hit hardest, and subscribe if you want money explained this plainly, without a sales pitch.

`[rail 8.7 | img: a closed notebook and a capped pen, finished | head: — | num: SUBSCRIBE | foot: Comment which of the four hit hardest | colour: --pop (the single --pop block of the video)]`

**8.8**
> And send this to the friend who says every single month that they have no idea where it all went.

`[rail 8.8 | img: two coffee mugs on a porch rail at night, no people | head: SEND IT TO | stmt: The friend who says every month: I have no idea where it goes.]`

---

## Fact trace (every number → facts-staging.md)

| Number / claim in script | Where | facts-staging.md row | Tag |
|---|---|---|---|
| **37.8%** — Japan's FIES salaried-worker surplus rate, 2024 | 2.3, 2.5 | **J2** — Statistics Bureau of Japan, *Kakei Chōsa* 2024 annual summary, Table I-2-2, + Horioka p.7 | **HARD** — two independent, one is the issuing agency |
| **about 1%** — Japan's National-Accounts household saving rate, 2024 | 2.6 | **J1** — Horioka, NBER WP 33181, p.2 and p.7 | **HARD on the rate.** The *decimal* 1.1 is single-sourced, so the VO says "about one percent" and the screen says `ABOUT 1%`. ⚠ staging asks for `~1%`; the tilde is **absent from the 97-codepoint font subset**, so it is spelled out. |
| **more than thirty times** the gap | 2.7 | **J3** — Horioka p.7, verbatim "more than 30 times as high" | **HARD**. Screen reads `30 TIMES` (`×` is also absent from the subset). |
| Who each survey counts | 2.9 | **J3** | **HARD** |
| **JPY 197,432 surplus of JPY 522,569 disposable** (screen only, foot) | 2.5 | **J4** | **HARD** — stays in yen, never converted, never spoken |
| **~90% to deposits · ~3% to securities** | 3.2 | **J5** — deposits ¥175,241, securities ¥6,705 of the ¥197,432 surplus | raw yen **HARD**; the *ratio* is **COMPUTED** → the frame carries an `ILLUSTRATIVE` foot and the VO says "about" both times |
| **51.0%** Japan cash & deposits | 3.4 | **J8** — BOJ *Flow of Funds*, Chart 2, end-March 2025 | **HARD** |
| **11.5%** US cash · **41.5%** US equity | 3.5 | **J8 / U3** — the SAME BOJ Chart 2 | **HARD** — one table stating both markets, so this is **not** a cross-market conversion. The foot says so on screen and labels it ASSET MIX ONLY, explicitly **not** a saving-rate comparison. |
| **1961–1986** above 15% **(postwar only)** · **23.2%** **postwar** peak, mid-1970s · hardly ever above 5% since 2002 | 3.8, 3.9 | **J6** — Horioka p.2 and p.3 (re-read direct by fin-audit-en-1) | **HARD, but only with both qualifiers.** p.3: "**if we confine ourselves to the postwar period**, the only period during which Japan's household saving rate exceeded 15% was the 25-year period from 1961 until 1986"; p.2: the rate "reached **44%** in the waning years of the Second World War", and has been no higher than 5% since 2002 "**except for a temporary blip in 2020 due to the Covid-19 pandemic**". Both lines were rewritten — see `audit-en.md`. |
| **Culture is not a major determinant** + the actual drivers | 3.10, 3.11 | **J7** — Horioka §3 and §9–10 | **HARD** — this is the premise correction, stated on screen |
| **Mottainai** — meaning and etymology | 4.1 | **§4** | **HARD on the meaning** · **SOFT on the etymology** (gov-online.go.jp 403'd) → the VO gives the meaning hedged with "roughly"; the etymology sits in a `foot:` |
| **Hara hachi bu** — "eight parts in ten", Okinawa, Confucian | 5.1, 5.2 | **§4** | **SOFT** — term and meaning solid. **No calorie, intake, weight or lifespan number appears anywhere near it**, and 5.1's foot says so on screen. |
| **62.2%** — Japan's average propensity to consume | 5.9 | **J4** — consumption ¥325,137 ÷ disposable ¥522,569 | **HARD** — Japan's own figure, presented alone; the foot states it is not compared with any other country's |
| **$4,000/mo** worked example · **$800** (20%) · **$3,200** · **$200** (5%) | 2.11, 4.11, 5.5, 5.10 | **U6** — vault locked example, channel convention | **CONVENTION**, labelled on screen every time. 20% of $4,000 is $800 and 5% is $200 — arithmetic, not statistics. |
| **$83,730** real median household income, 2024 (screen only, foot at 2.11) | 2.11 | **U4** — US Census P60-286 | **HARD** — carried as context so the worked example is not mistaken for a national figure |
| **over 20%** card APR on accounts assessed interest | 6.14 | **U7** — Federal Reserve G.19 | ⚠️ **staging row corrected by fin-audit-en-1.** U7 records "22.15%, Q2 2026"; the current release (8 Jul 2026, reference month May 2026) marks **2026 Q1 and Q2 "n.a."** and publishes **21.52% for 2025 Q4** as the latest quarter. No Q2 2026 print exists. VO "over twenty percent" is unaffected and true; the screen `num` and `foot` were corrected. Price evidence, and the foot says so. |
| **about 4 in 10 adults** cannot cover a $400 emergency with cash | 6.15 | **U5** — Federal Reserve SHED 2025 (63% of **adults** can), fielded Oct 2025, released 13 May 2026 | **HARD** — the complement of the published 63%. The unit is **adults**, not households; the VO said "households" and was corrected. |
| **1904** · Hani Motoko · Japan's first woman journalist · still printed · four wartime years missing | 6.2, 6.3 | **§4 Kakeibo** — Fujin no Tomo Sha (publisher primary) + National Diet Library | **HARD**. Screen says "over a hundred years"; **never "121 years"**. |
| The budget-first idea (divide by twelve, saving aside first) | 6.5, 6.6 | **§4 Kakeibo** — the publisher's own words: introducing 予算 to ordinary household finance | **HARD** |
| The four categories are a **later** addition | 6.7, 6.8 | **§4** — the four pillars are the Western/English repackaging (Fumiko Chiba, 2017 onward) | **SOFT** — so the script states the *uncertainty* rather than the attribution, on screen, at the 70% mark |
| **Ryōan-ji tsukubai** · four characters · the shared radical supplied by the square water hole | 7.2–7.5 | **§4 Taru wo shiru** — Traditional Kyoto + Wikipedia (Tsukubai) + Nara Yamato Spirit Tours | **HARD** on the inscription, the temple and the radical design. The Tokugawa Mitsukuni donor attribution is **SOFT and is not used**; nor is the replica question. |

### Deliberately NOT used (so the audit stage doesn't rediscover them)

- **The US personal saving rate — U1 (2.7%, June 2026) and U2 (3.0%, May 2026) — is used
  nowhere in this script.** Not an oversight, and this is the single most important omission
  in the file. §3's own note says "Americans save less than the Japanese national-accounts
  rate" is **not claimable**: 2.7% (BEA, gross concept) and 1.1% (Japan SNA, net of
  depreciation) are not like-for-like. Stating the US rate anywhere in a video whose hook is
  Japan's rate creates the comparison by adjacency even if no sentence makes it. The
  chapters that would have carried it use the channel's own $4,000 split instead — honest,
  actionable, comparable to nothing.
- **"Japan saves 37%, America/India saves single digits."** The source video's headline
  (TOP `fQyN80dLDpQ`, 0:54). §5.1 — the 37 is real but misapplied, and the second half has
  no identified source at all. The two never appear together in this file.
- **"Kakeibo saves you 20–35% of your income."** §5.2 — asserted by at least seven sites and
  one YouTube short; searched for the underlying study and **there is none**.
- **Every calorie, intake and longevity figure attached to hara hachi bu** (§5.5) — all
  wellness blogs with no primary, and the Okinawa centenarian data has been contested since
  the 2010s. This is a money video; the principle carries zero numbers.
- **Trading Economics quarterly prints** (0.4% Q3 2025, 3.9% Q4 2025) — §5.4. Real, but
  Japan's quarterly rate swings on the bonus cycle. Annual only, on screen.
- **J9 (¥2,386tn at end-March 2026, stocks +28.6%) and New NISA.** Both **SOFT** — the BOJ
  primary for that quarter was not read and the FSA page was not fetched. Nothing in the
  argument needs them, so no SOFT row is spent for texture.
- **Every India row (§2) and every figure in the Indian cut's currency.** This is the US
  cut; §6 forbids any conversion, and the Indian instruments, institutions and examples
  appear nowhere — not in a VO line, not in a cue, not in a photograph.
- **Any yen-to-dollar conversion.** §6. J4/J5 stay in yen inside `foot:` lines or become
  percentages. The US appears as figures exactly twice: the BOJ table's own second column
  (3.5), and the two Federal Reserve rows (6.14, 6.15) that are about US households only and
  are compared to nothing.
- **A named bank, brokerage, card, fund, index fund or app** — and, after fin-audit-en-1,
  **any account type at all.** Persona rule. 5.7 originally routed the set-aside into "a
  federally insured savings account" with a `HIGH-YIELD SAVINGS · FDIC INSURED` row on
  screen; that is a product-category placement recommendation and a disclaimer under a
  recommendation is still a recommendation. 5.7 now names only the mechanic — automate it,
  keep it separate. The card APR remains price evidence.
- **The handwriting-beats-typing science** TOP asserts at ~11:00. No source was staged, so
  6.12 keeps the paper ritual as a practice and claims nothing about memory.
- **"Advertising spends billions."** TOP's line at ~13:30. No spend figure is staged, so 7.9
  makes the same point as an observation about the market, carrying no number.

---

## Build handoff

1. **`assets/voice/english-lines.json` = 92 entries keyed `1.1 … 8.8`**, containing **only**
   the `>` VO strings above — no markdown, no cue text, no on-screen text. **Slice the
   source file; never retype.** Gate the extraction with a byte-for-byte reconstruction
   check against this file before generating audio (`long_form_scripting.md` §1.7).
2. **TTS** via `tools/tts/elevenlabs_tts.py`, voice `nPczCjzI2devNBz1zQrb` (Brian),
   `eleven_multilingual_v2`, style 0. **92 clips.** ⚠ `run.json budget.max_elevenlabs_calls`
   is **30** for the whole run and the hi cut also needs 92 — the two cuts cannot both be
   generated under that cap. Raise the cap deliberately or batch and record the count; do
   not discover this at generation time.
3. **Timing is by construction.** One line = one clip = one scene. LONG charges
   `lead_in_seconds 0.25` + `tail_seconds 0.55` per line (`format.json tiers.long`) — **not**
   the `scene.*` 0.4/1.0 defaults, which are tuned for SHORT's nine lines and would spend
   128s of this video on padding. Never hand-edit a duration; regenerate all four homes of
   the timing numbers from one source.
4. **Recount the characters programmatically** and re-check the total against
   `(660 − 92 × 0.8) × 16.1 = 9,441` before locking, then read the two-rate hedge above
   before reacting to the result. **No line may exceed 130 characters.** Post-audit total is
   **9,619**; the fin-audit-en-1 edits are the only VO lines whose bytes moved, so a stale
   `english-lines.json` will fail the reconstruction gate at 1.2, 1.5, 3.8, 3.9, 5.7 and 6.15.
5. **Measure the delivered flat rate after TTS** (total chars ÷ total audio seconds) and put
   it in the build log. If it lands near 17.73 again, the fix belongs in
   `format.json cuts.en.chars_per_second` — with the measurement beside it — not in a
   re-padded script.
6. **Images: one per line, 92 scenes, zero photo-free frames** (`photo_free_scene_ratio` = 0,
   creator rule 2026-07-28). Three pairs are holds — **1.1→1.2, 6.7→6.8, 7.4→7.5** — and each
   must run **ONE continuous zoom across both scenes**, never a self-dissolve (creator rule,
   firaun 2026-07-23); give the second scene a tighter crop of the same source so no single
   framing holds past 9.0s.
7. **Localisation rule (study conclusion 4, and the trap fin-research named): do not make a
   beautiful video about Japan.** Japan owns the story frames only — Okinawa, Ryōan-ji, the
   archival Tokyo street, the FIES and BOJ pages, the noren curtain. **Every frame where the
   viewer is asked to act is American:** 1.1–1.10, 4.5, 4.6, 4.7, 4.11, 5.4, 5.5, 5.7, 5.10,
   6.10, 6.12, 6.14, 6.15, 7.6, 7.7, 8.2, 8.3, 8.5, 8.6, 8.8. **Sweep every photo for
   non-US currency, signage, plugs, licence plates and vehicles** — a euro coin and a Swiss
   franc shipped in the first `-en` cut. md5 the asset ledger: no image may repeat across
   videos or channels.
8. **6.7 is a photograph, not an overlay.** The four categories ship as a real top-down
   flat-lay on wood — actual US coins and bills in four groups with four handwritten labels
   **inside the frame**. This is TOP's single text moment in seventeen minutes and the most
   stealable thing in the packet. Do not rebuild it as a card.
9. **⚠ THE FONT SUBSET WILL EAT JAPANESE AND FOUR PUNCTUATION MARKS.**
   `tools/scaffold/assets/fonts/NotoSansFinance-var.woff2` carries **97 codepoints**
   (03-design.md §1.4): **no CJK at all**, and `>` `→` `▶` `×` `≈` `~` `¥` are absent.
   Already obeyed by every cue above:
   - **On-screen Japanese is romaji only** — `MOTTAINAI`, `HARA HACHI BU`, `KAKEIBO`,
     `TARU WO SHIRU`, `RYOAN-JI`. Any kanji must live **in the photograph** (the tsukubai at
     7.3/7.4), never as composition text.
   - Yen figures are written `JPY 197,432`, never with the yen glyph.
   - `ABOUT 1%`, `ABOUT 22%` and `30 TIMES` replace `~1%`, `~22%` and `30×`. `·` is the
     separator (present in the subset).
   - Verify every on-screen string against a dumped `subset.txt` before render.
10. **ledger-rail specifics.** Rail 300px, scene id 96px **weight 200**, chapter label 26px
    tracked 4px, `--muted` hairline between. Photo panel x=1180→1920 with one
    `linear-gradient(90deg, #0d1017, transparent 30%)` left edge. **Delete the four-layer
    scrim and every `text-shadow`.** Seven scenes are `RAIL OFF` (1.1, 2.7, 3.12, 4.10, 6.7,
    7.4, 8.6); nothing else may use it.
11. **Anchor cues to word-level timings** (faster-whisper), not character-offset
    interpolation. `first_cue_by_seconds` 0.5, `cue_min_gap_seconds` 0.8,
    `max_simultaneous_elements` 6.
12. **Chapter-wise production.** Build, proof and re-render chapter by chapter; concat and
    final-render only after all eight chapters are locked. Encode with an explicit
    `-o renders/FINAL-1080p-en.mp4`.
13. **Burn subtitles into every frame** (study conclusion 6 — the clearest binary in the
    packet: TOP does it on 209/209 sampled frames, the LOW on 0 and died at 2,131 views).
14. **Never name the tool** in the title, description or on screen (study conclusion 7).
