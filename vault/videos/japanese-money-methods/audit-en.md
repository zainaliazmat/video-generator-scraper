---
summary: Gate-one adversarial audit of script-en.md for japanese-money-methods (LONG, en). Every load-bearing number re-fetched from its recorded source; six direct edits. One staged US figure did not survive re-fetch — G.19 publishes no Q2 2026 card APR — and the two Horioka qualifier errors the hi audit found WERE inherited by this cut after all. Verdict PASS after edits.
updated: 2026-08-01
source: Re-fetched primaries read as PDFs, not via search index — Horioka NBER WP 33181 (pp.1-8), Statistics Bureau FIES 2024 summary (pp.8-11), BOJ Flow of Funds overview (Chart 2). Plus Federal Reserve G.19 current release (8 Jul 2026), Fed SHED 2025 press release, Census P60-286, Fujin no Tomo Sha 120th page, Wikipedia Tsukubai + Mottainai.
stage: fin-audit, cut en, attempt 1
---

# audit-en — japanese-money-methods

PASS

Passing **after six direct edits**. As submitted the script would have failed checks **3**,
**1** (twice) and **4**. Downstream voice work must re-run against the edited file — the VO
strings for **1.2, 1.5, 3.8, 3.9, 5.7 and 6.15** have changed and the pipeline hash-checks
this. 6.14's VO is unchanged; only its screen figure and citation moved.

⚠️ **The handoff note into this stage said "script-en.md did not inherit either error." That
is false.** It inherited both, in softer wording that hid them — see §2.2 and §2.3. The
independence re-fetch is what caught it; grading against the corrected `facts-staging.md`
J6 text alone would not have.

---

## 1. Independence re-fetch — every load-bearing number

`facts-staging.md` was written by this same run and was not used as grading evidence. The
three primaries returned raw PDF binary through the fetch tool and were then read **as PDFs,
page by page**, so the figures below are from the documents themselves.

| Figure | Script line | Re-fetched source | Verdict |
|---|---|---|---|
| **37.8%** FIES surplus rate | 2.3, 2.5 | FIES 2024 summary **p.11**, 表I-2-2: 黒字率 **37.8**; independently Horioka **p.7** "37.8 percent according to the Family Income and Expenditure Survey" | ✅ two independent, one is the issuing agency |
| **about 1%** SNA rate | 2.6 | Horioka **p.2**: "The most recently available figure is for 2024, when it was a mere **1.1%**"; **p.7** "1.1 percent according to the National Accounts" | ✅ VO says "about one percent", screen `ABOUT 1%` |
| **more than thirty times** | 2.7 | Horioka **p.7** verbatim: "the figure from the 'Family Income and Expenditure Survey' is more than 30 times as high as the figure from the National Accounts!" | ✅ |
| Who each survey counts | 2.9 | Horioka **p.7** verbatim: "only for salaried worker households whereas the National Accounts include everyone including the self-employed, the unemployed, the retired, and private unincorporated enterprises" | ✅ |
| **JPY 636,155 · 522,569 · 325,137 · 197,432** | 2.5 foot | FIES **p.11**, 表I-2-2 — all four exact | ✅ stays in yen, never spoken, never converted |
| **~90% deposits · ~3% securities** | 3.2 | FIES **p.11** §(4): 預貯金純増 **175,241**, 有価証券純購入 **6,705** of 黒字 **197,432** → 88.8% / 3.4% | ✅ ratio is COMPUTED; frame carries `ILLUSTRATIVE` and the VO says "about" both times |
| **51.0%** Japan cash · **11.5%** US cash · **41.5%** US equity | 3.4, 3.5 | BOJ *Flow of Funds* overview, **Chart 2 (p.3)**, data as of **end-March 2025**: Japan ¥2,195tn, US $128.8tn | ✅ one table states both markets — not a cross-market conversion |
| **1961–1986** above 15% | 3.8 | Horioka **p.3** — restricted to the postwar period | ⚠️ **REWRITTEN — §2.2** |
| **23.2%** peak · never above 5% since 2002 | 3.9 | Horioka **p.2** — postwar-scoped, and carves out 2020 | ⚠️ **REWRITTEN — §2.3** |
| Culture not a major determinant + the actual drivers | 3.10, 3.11 | Horioka **p.3 §3** verbatim: "culture, tradition, and national character are not a major determinant of Japan's household saving rate"; abstract lists unavailability of consumer credit, unavailability of social safety nets, high income growth, tax breaks for saving, saving promotion policies, land/housing prices | ✅ premise correction holds, and 3.11's five drivers match the abstract one for one |
| **62.2%** avg propensity to consume | 5.9 | FIES **p.11**: 平均消費性向 **62.2%** | ✅ Japan's own figure, presented uncompared |
| **$4,000 · $800 · $3,200 · $200** | 2.11, 4.11, 5.5, 5.10 | Channel convention; arithmetic re-checked (20% and 5%) | ✅ all correct, labelled on screen every time |
| **$83,730** real median household income 2024 | 2.11 foot | Census **P60-286**, *Income in the United States: 2024*, issued Sept 2025 | ✅ |
| **about 22%** card APR | 6.14 | Federal Reserve **G.19** | ❌ **KILLED AS DATED — §2.4** |
| **63% / about 4 in 10** on a $400 emergency | 6.15 | Fed **SHED 2025**, fielded Oct 2025, released **13 May 2026**: "The share who would cover a $400 emergency expense using cash or its equivalent also remained unchanged from 2024 at 63 percent" | ✅ number holds — **unit corrected, §2.6** |
| **1904** · Hani Motoko · 4 wartime years · budget-first | 6.2, 6.3, 6.5, 6.6 | Fujin no Tomo Sha (publisher primary): 「羽仁もと子案家計簿」が初めて発行されたのは明治37（1904）年末 · 戦中戦後の4年間は紙の統制により発行できませんでした · 1年分の収入を12等分したものから貯蓄分をまずとって | ✅ and the script correctly never says "121 years" |
| **Ryōan-ji tsukubai** · four characters · shared 口 | 7.2–7.5 | Wikipedia *Tsukubai*: 吾唯足知, each character "read in combination with 口 (kuchi), the shape of the central bowl" | ✅ the Tokugawa Mitsukuni donor attribution is SOFT and is correctly **not** used |
| **Mottainai** — meaning, 13th century | 4.1 | Wikipedia *Mottainai*: "regret at the full value of something not being put to good use"; "An archaic Japanese dictionary dates the use of the term … back to the 13th century" | ✅ meaning and date hold — see the SOFT note below |

**One staged number did not survive the re-fetch** (U7, §2.4). Two *sentences* asserted more
than their cited page supports (§2.2, §2.3). Nothing was untraceable and nothing was
fabricated out of thin air.

**SOFT row left standing, deliberately:** 4.1's `foot:` glosses *mottai* as "a thing's
rightful worth" and *nai* as "without". The one source readable directly (Wikipedia) instead
gives *mottai* as "shape/form, something impressive" and notes *nai* "may have originally
been used as an emphatic", and treats the Buddhist origin as contested. `facts-staging.md`
tagged this SOFT precisely because gov-online.go.jp 403'd. The VO already hedges with
"Roughly", the claim carries no number, and the meaning — the only load-bearing part — is
confirmed by three sources. Disclosed disagreement between secondaries is not a kill. Left
as written; recorded here so nobody promotes it to HARD.

---

## 2. What was killed or rewritten, and why

### 2.1 — 1.2 rewritten · **check 3, the fifteen-second promise gate**

The submitted cut carried **no payoff promise until 2.1 at 0:59**. This is the same defect
the hi cut had, argued from the same study conclusion ("TOP spends 40s before its first
promise"), and it is the single largest defect in the file — deliberate, which is worse than
an oversight. A competitor's retention curve does not override a gate, and the study note has
since been corrected.

- was: `For about two seconds, that notification on your phone feels like relief.` (73 ch)
- now: `For about two seconds that notification feels like relief, and three old Japanese methods are what make it last longer.` (119 ch)

Promise clause opens ≈**8.7s**, closes ≈**13.2s**. Chapter 1 still carries **zero
statistics** and stays entirely in second person, so the pain-mirror is intact; only the
roadmap moved. 2.1 now reads as the expansion of a promise already made.

### 2.2 — 3.8 rewritten · **check 1, the source does not back the claim** · INHERITED AFTER ALL

- was: "The saving rate stayed above fifteen percent **for exactly twenty-five years**, from nineteen sixty-one to nineteen eighty-six."
- Horioka **p.3**: "**if we confine ourselves to the postwar period**, the only period during which Japan's household saving rate exceeded 15% was the 25-year period from 1961 until 1986."
- Horioka **p.2**: the rate "reached **44%** in the waning years of the Second World War."

"For exactly twenty-five years" is an exclusivity claim — it asserts that 25 years is the
whole of the time the rate was above 15%. That is true only postwar. The hi cut said "only";
this cut said "exactly". **Same false claim, different word.** The handoff note's assertion
that this cut did not inherit the error is wrong.

- now: `After the war, the rate was above fifteen percent for exactly twenty-five years, from nineteen sixty-one to eighty-six.` (119 ch)
- `foot:` now leads `POSTWAR ONLY` and records the 44% wartime rate; the `head:` is now `THE POSTWAR HIGH-SAVING ERA`; the citation is corrected from p.2 to **p.3**.

### 2.3 — 3.9 rewritten · **check 1, the source does not back the claim** · INHERITED AFTER ALL

- was: "It **peaked** near twenty-three percent in the mid nineteen seventies, and **has not been** above five percent since two thousand two."
- Horioka **p.2**: "has been no higher than 5% during the past two decades (since 2002) **except for a temporary blip in 2020 due to the Covid-19 pandemic**."
- Horioka **p.2**, same paragraph, scoped to "trends over time … **during the postwar period**": "it peaked at 23.2%".

Two defects in one sentence: an absolute the source explicitly carves an exception out of,
and an unqualified "peaked" when the wartime rate was 44%. `facts-staging.md` J6 was
corrected on 2026-08-01 to carry both qualifiers; this line carries neither.

- now: `Its postwar peak was near twenty-three percent, and since two thousand two it has hardly ever been above five percent.` (118 ch)
- `head:` `PEAK, THEN` → `THE POSTWAR PEAK`; `foot:` now names the mid-1970s date, the 2020 Covid blip and the negative years, and drops the phantom "p.11" citation.

### 2.4 — 6.14's screen figure and date killed · **check 1, the injected-plausible-date case**

This is the row the independence rule exists for. `facts-staging.md` U7 records **"~22%
(22.15% Q2 2026), Q2 2026, Fed G.19, HARD (carried)"**, and the script put `ABOUT 22%` on
screen under `foot: … Q2 2026 — Federal Reserve G.19`.

Re-fetched: the **current G.19 release is dated 8 July 2026, reference month May 2026**. Its
Terms of Credit table marks **2026 Q1 and 2026 Q2 as "n.a."** and publishes **21.52% for
2025 Q4** as the most recent quarterly figure for accounts assessed interest. **There is no
Q2 2026 print, and no 22.15% anywhere in it.** A dated, precise, plausible, HARD-tagged
figure that the source does not contain — shipped, it would have been an on-screen citation
to a document that says something else.

- VO **unchanged**: "a card balance at **over twenty percent** a year" is true of every
  published quarter in the last two years (21.52–22.83%).
- `num:` `ABOUT 22%` → `OVER 20%`; `foot:` now reads 21.52%, names 2025 Q4 as the latest
  quarter G.19 publishes, and dates the release.

**`facts-staging.md` U7 must not be promoted to `money-facts-2026.md` in its current form.**

### 2.5 — 5.7 rewritten · **checks 4 and 7, the monetisation gate**

- was: "Automate it so it moves without a decision, into a separate **federally insured savings account at a different bank**", with `stmt: HIGH-YIELD SAVINGS · FDIC INSURED · A DIFFERENT BANK`.

No brand is named, but the sentence routes the set-aside into a product *category* and the
screen names its yield profile and its insurance status. That is a placement recommendation;
the `foot:` reading "Institutions named generically. No bank, app or fund is named or
recommended" is the same disclaimer-under-a-recommendation that was rejected at hi 6.14.
The script's own persona box promises the savings account appears "never as 'put your money
here'" — 5.7 was exactly that.

- now: `Automate it so it moves without a decision, into an account that is separate from the one the card and the bills touch.` (119 ch)
- `stmt:` → `A separate account. Not the one the card touches.`; `foot:` now disclaims **any**
  account type. The mechanic the method actually needs — automation plus separation —
  survives untouched.

### 2.6 — 6.15 unit corrected · **check 1**

SHED reports the share of **adults**, not households; the report's *title* is about
households, which is how the slip happened. "about four in ten households" → "about four in
ten adults", and the `foot:` now says "63% of adults" and carries the exact release date.

### 2.7 — 1.5 de-branded · **check 4**

"two **DoorDash** orders" named a platform in VO, and not as price evidence — the one thing
check 4 permits. The screen cue for the same scene was already generic ("Two delivery
orders"), so the VO was the only place it appeared. → "two **food delivery** orders", and the
image cue now forbids readable brand marks on the bag.

---

## 3. Checks that passed without edit

2. **Char budget.** `(660 − 92 × 0.8) × 16.1 = 9,441`. Draft 9,581 (+1.5%); post-edit
   **9,619 (+1.9%)**. Inside ±10% on the padding-corrected formula and also inside ±10% of
   the raw `660 × 16.1 = 10,626` reading. Spot-recounted 1.1 (68) and 3.5 (128) by hand
   against the per-scene table and both were exact, so the table is trustworthy; the build
   step still recounts programmatically.
5. **Currency purity.** **Zero `₹` in the file** (grep, whole file). `$` present as required.
   No `¥` glyph anywhere — yen written `JPY 197,432`, which also dodges the 97-codepoint font
   subset. The words "lakh/crore/UPI/PPF/SIP" appear only inside the prohibition list and one
   filename, never in a VO line or a cue.
6. **TTS silent-killers.** No `(28:4)`-style cite refs in any VO line or cue (the two `d+:d+`
   hits are runtime timecodes in the analysis prose). **No bare Latin digit in any of the 92
   VO lines** — verified by grep across all `> ` lines post-edit. Every figure is spelled out
   ("thirty-seven point eight", "twenty-three", "nineteen oh four", "four in ten").
7. **Persona.** No `I`, `we`, `my`, `our` in any VO line. No host persona, no first-person
   expertise. After §2.5 and §2.7, no product, platform, account type, fund or brand is
   recommended or named anywhere. The card APR is price evidence and says so.
8. **Layout lints.** **One focal element per scene** — no cue carries both `stmt:` and `num:`
   (all 92 checked by grep). Three cues per scene (head / stmt-or-num / foot) inside 3.8–8.0s
   scenes clears `cue_min_gap_seconds` 0.8 and `first_cue_by_seconds` 0.5 with room; no
   cascade is declared and none is needed. Longest line post-edit is 3.5 at 128 ch → 8.0s VO
   + 0.8 = **8.8s**, under `max_scene_seconds` 9.0. Colour table is thesis-consistent:
   `--warn` on leaks and on numbers used wrongly, `--fund` on behaviour that works, `--target`
   on figures under examination, `--pop` once at 8.7. 3.12 — "the methods work, they were
   never the reason" — is `--fund`, which agrees with the premise correction rather than
   arguing against it.

Also verified: **no Japan-vs-US saving-rate comparison** anywhere, spoken or by adjacency —
U1/U2 (the US personal saving rate) are used nowhere at all, which is the correct and
deliberate omission; the only cross-market beat is 3.5, one BOJ table stating both markets,
labelled ASSET MIX ONLY on screen. No ¥→$ conversion. No number attached to mottainai, hara
hachi bu or taru wo shiru. The four kakeibo pillars are explicitly **not** attributed to Hani
Motoko (6.7, 6.8).

---

## 4. Three things the build stage must not get wrong (not script defects)

1. **Extraction hazard.** The warning box above `# THE SCRIPT` is a `>` blockquote containing
   English text and Latin digits. A naive `^> ` slicer sweeps it into the VO set. Extraction
   must key off the `**N.N**` markers and land exactly **92** entries `1.1…8.8`; the
   byte-for-byte reconstruction gate in build handoff §1 catches it if not.
2. **`·`-separated statements are not chip rows.** 3.11 (five items) and 6.10 (four items)
   would breach `max_chips_per_row` 3, and 6.10 also `max_chip_chars` 22, **if built as
   chips**. They are `stmt:` strings at 44px and must render as wrapped statement lines, per
   the ledger-rail two-type-sizes rule.
3. **`AUDIT fin-audit-en-1:` fields inside six cues are annotations, not composition text.**
   They record why a line changed. Strip them when the cue is turned into scene content.

## 5. Budget note carried forward

`run.json budget.max_elevenlabs_calls` is now **221** (LONG tier, corrected 2026-08-01), so
the 92 + 92 clips of the two cuts fit. Build handoff §2 still says the cap is 30 — stale
prose in the script, not a defect in the pipeline; it can be corrected at build time.
