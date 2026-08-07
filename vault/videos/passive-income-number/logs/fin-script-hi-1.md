# fin-script — passive-income-number · cut hi · attempt 1

**Date:** 2026-08-07 · **Status:** ok
**Wrote:** `vault/videos/passive-income-number/script-hi.md`

## Inputs read

- `vault/CLAUDE.md` (first, per contract)
- `vault/videos/passive-income-number/run.json` — the `constraints` block, treated as binding
- `vault/videos/passive-income-number/facts-staging.md` (fin-facts attempt 1) — every number
- `vault/knowledge/video-studies/passive-income-number.md` — the two format twins
- `tools/format.json` — `cuts.hi` (13.03 chars/s, Harsh `HTUuC7OeeEt6OL5fViVe`),
  `tiers.medium` (510 s, per-line-chapters, 78 lines, 0.25 + 0.55 padding),
  `scene` bounds, `chapter_design.archetypes`, `colors`
- `vault/skills/long_form_scripting.md`
- `vault/knowledge/design-chapter-archetypes.md` — the A/B/C/D layer for MEDIUM/LONG cuts
- `vault/knowledge/niches/india-finance-market.md` (hi cut)
- `vault/videos/first-lakh-first-thousand/script-hi.md` + its log, and
  `vault/videos/japanese-money-methods/script-hi.md` — house style for a per-line chapter
  cut, and the corrected char-budget formula

## ⚠ Two conflicts in the launch brief, both resolved against the vault

Recording both because each has cost this pipeline a retry before.

1. **"Haryanvi-Hindi cut, follow `haryanvi-hindi-script-style.md`."** Not followed, and that
   file was **not read**. `vault/knowledge/niches/india-finance-market.md` records the
   creator decision of **2026-07-28**: Standard Hindi on the Harsh voice is the **locked
   channel identity** for `@cashguruguides`, Haryanvi is **retired for finance**, and
   "a Haryanvi-marked script read by a standard-Hindi voice is the failure to avoid".
   The `fin-script` contract says the same thing and names the same date. Three prior hi
   cuts (`first-lakh-first-thousand`, `japanese-money-methods`, `good-debt-vs-bad-debt`)
   logged this identical conflict and resolved it the same way. Written in **Devanagari
   Standard Hindi**. No config was changed. If the creator has genuinely reversed the
   2026-07-28 decision, the fix is to change it in `india-finance-market.md` — its one
   home — and re-run; it must not be carried in a launch message.

2. **"hi char budget ≈6,645 at 13.03 c/s."** That is `510 × 13.03`, the *uncorrected*
   formula. `format.json cuts.en._chars_per_second_trap` is explicit that per-line padding
   is not audio and must come out of the target **before** the rate is applied, and that
   the fix is owed in fin-script's formula. At MEDIUM's 78 lines the padding is
   `0.8 × 78 = 62.4 s`, so a 6,645-char script runs `6,645 ÷ 13.03 + 62.4 = 572 s` —
   **12% long**. Used the corrected budget instead:
   `(510 − 62.4) × 13.03 = 5,832`. This is the same correction the `japanese-money-methods`
   hi cut already shipped with (it landed 0.5% under target). Flagged, not silently applied.

## Output

**78 VO lines · 7 chapters · ~5,851 chars · ~449.0 s VO + 62.4 s padding ≈ 511.4 s (8:31)**
vs the 510 s target = **+0.3%**. Corrected char budget 5,832; draft is +0.3%.
Average scene **6.56 s** (`target_scene_seconds` 6.5, `max_scene_seconds` 9.0). Longest
lines 100 chars → 8.47 s incl. padding; shortest 27 chars → 2.87 s (over
`tts.min_clip_seconds` 1.0). Cap declared in the script: **no line above 105 chars**.

ElevenLabs: 78 hi + ~78 en = 156 of the run's 188 ceiling, leaving 32 for retries.

## Structure (the brief's six bands, verified against the estimate)

| Brief band | Chapter | measured |
|---|---|---|
| 0–8% won morning, number withheld | 1 (7 lines) | 0:00–0:37 = **0–7.3%**; the withheld number is *named* at 1.4 ≈ **0:14.5**, inside the 15 s promise gate |
| 8–25% rung 1, one named bill, rate spoken | 2 (12 lines) | 0:37–1:58 = **7.3–23.0%**; ₹10,00,000 → ₹2,500/mo lands at 2.9 ≈ **1:30 (17.5%)**, priced as the recharge + internet bill |
| 25–50% rungs 2–3, each re-stamped | 3 + 4 (18 lines) | 1:58–3:54 = **23.0–45.7%**; ₹20,00,000 → ₹5,000 (electricity), ₹40,00,000 → ₹10,000 (ration) |
| ~50% the rate trap + the 3.0 vs 4% correction | 5 (17 lines) | 3:54–5:45; the trap punches at 5.6 ≈ **4:24 (51.6%)** and the provenance opens at 5.12 ≈ **5:04** — both twins warn within ~30 s of the 5:00 mark |
| 50–85% rungs 4–5 to rent/EMI + one sourced stat | 6 (16 lines) | 5:45–7:36; ₹50,00,000 → ₹12,500 (rent/EMI) then the hero at 6.7 ≈ **6:20 (74.3%)**, validated by the PLFS ₹24,217 at 6.9 ≈ **6:33** |
| 85–100% callback, ≤1 terminal CTA | 7 (8 lines) | 7:36–8:31 = **89.1–100%**; the single CTA is the last line at ≈8:26 (98.9%). **Zero mid-roll CTA** |

## Decisions worth recording

1. **The hero is the spine, and it lands once.** ₹1,00,00,000 at a 3.0% withdrawal rate =
   ₹25,000/month, set immediately beside the PLFS regular-salaried average ₹24,217
   (6.7 → 6.9 → 6.10). Nothing before Chapter 6 reveals it — including the 4% correction
   in Chapter 5, which is deliberately stated as "a quarter smaller" *in the abstract* so
   the ₹75,00,000 / ₹1,00,00,000 pair can land concretely at 6.12–6.13, after the hero.
2. **The rate is re-spoken with every corpus, in the same sentence, at every rung.** This
   is the study's headline failure — Dark Ledger states 4% once and ships six bare numbers.
   Counted: the 3.0% rate appears in **20 VO lines**, including both halves of every rung
   (the corpus line and the division line) and the "only the corpus moved" line 3.6, which
   was rewritten specifically because its first draft named two corpora with no rate.
   Handoff item 5 turns this into a build-time assertion rather than a prose warning.
3. **No age exists in this cut at all** — not narrative, not implied. B carries ages as
   narrative and A converts a corpus into one ("financially free at 50"), which is the
   sentence `no_unsourced_retire_early` bans. 6.11 states the refusal on the record:
   "यह उम्र का नहीं, सिर्फ़ रक़म और दर का हिसाब है".
4. **The trap beat is a withdrawal rate, not a yield** — which is what makes it work in a
   rupee SWP frame and is strictly more accurate than either twin. 12% is spoken only as a
   rate someone might *pull out* (5.2, 5.4, 5.5, 5.6), never as a return.
5. **The two rate objects are disambiguated out loud.** 12% appears as a *withdrawal* rate
   in Chapter 5 and ~12% as an *assumed growth* rate in 6.16. That is exactly the
   conflation Dark Ledger commits, so 6.14 exists solely to name the difference before
   either growth figure is spoken, and both on-screen foots say "ASSUMED GROWTH".
6. **Both SIP columns are shown, never just the fast one.** 6.15 = ≈₹19,000/month at an
   assumed 7.1%; 6.16 = ≈₹10,000/month at an assumed ~12%; the line ends "दोनों हिसाब हैं,
   वादे नहीं". Showing only the ~12% column is the promise the staging note says this run
   must not make.
7. **The post-office monthly-income scheme is the reality-check, and it needs no forbidden
   vocabulary** (5.7–5.11): a published 7.4% paid monthly, capped at ₹9,00,000, ceiling
   ≈₹5,550/month. It is the honest roof on guaranteed monthly income in India and it is
   why the SWP route exists at all.
8. **Seven chapters, not nine.** MEDIUM → per-line chapters; the `lines: 9` on the
   `blockframe-9` registry entry is a SHORT-tier constant and none of the 9-segment
   constants were applied. Chapter sizes follow the brief's percentage bands, not a
   fixed count.
9. **Archetypes assigned by what the scene does**, per `design-chapter-archetypes.md` —
   and 5.13–5.15 deliberately hold **C** across three consecutive scenes because three
   documents are one argument.

## Fact discipline

- Every number traces to a `facts-staging.md` row; the trace table in the script names the
  row and the tag for each, including which ones are COMPUTED and which are HARD.
- **The banned payout word appears nowhere** — not in VO, not on screen, not in the prose,
  not transliterated. **And the live trap is closed at the root:** the index's total-return
  measure is never explained, never named and never abbreviated anywhere in the file, so
  no line can force the word. 6.16 quotes only "क़रीब बारह परसेंट" and the frame says
  "long-run index SHAPE, never a decimal".
- **Currency firewall holds.** Grep for the other cut's glyph across the whole file returns
  **zero** — prose, cue text, foots and claim IDs included. The commentary says "the
  rupee's counterpart glyph" and "a foreign figure" rather than typing it, per the rule
  that cost `japanese-money-methods-hi` a retry on 2026-08-01. PART C of the staging file
  contributed nothing to this cut.
- **No decimal on the equity shape.** ~12% is SOFT (all three NSE hosts 403'd); spoken as
  "क़रीब बारह परसेंट" and shown as `~12%`. The exact rates spoken are the HARD ones:
  3.0/3.5/3.75 (India research), 7.4 (POMIS), 7.1 (PPF / 3-yr TD), ~5 (RBI projection).
- **No precise tax figure.** The LTCG row is SOFT, so 4.8 says tax applies and stops; the
  frame foot says the rate is deliberately not stated and why.
- **≈₹5,550, not ₹5,500.** PART E flags the secondaries' rounding as wrong; the VO says
  "क़रीब पचपन सौ" and the frame carries the exact figure. Pinned in handoff item 6.
- **Digits spelled out in every VO line** — grep for Latin or Devanagari digits inside the
  78 `>` VO lines returns zero. On-screen numerals carry the exact figures with `en-IN`
  grouping.
- Sourced attributions name only what was actually read: the Trinity paper is quoted as
  primary (read direct), Bengen 1994 is flagged in the 5.13 foot as confirmed on three
  surfaces but not retrieved, and the Indian research paper is cited by author and title
  with a photograph carrying no legible text.

## Persona / policy

No host persona, no first-person expertise; **मैं** and **हम** appear in no VO line. No
fund, AMC, bank, app or platform is named. The post-office monthly-income scheme, the
7.4% and the 7.1% appear as **published price evidence** — 5.8 and 6.15 say so in their
on-screen foots. SWP and SIP appear as terminology, defined from four fund houses'
identical wording, never as "do this". Second person throughout.

## Handed to the next stage

- 78-entry `hindi-lines.json`, sliced not retyped, byte-reconstruction gated.
- **One open build defect flagged in the handoff:** the 2.6 + 2.7 hold pair totals ≈14.1 s
  on a single photograph and breaches `scene.max_scene_seconds` 9.0. Fix = give 2.7 a
  tighter second crop of the same source. The four callback scenes (7.1, 7.2, 7.6, 7.7)
  are **new photographs of the same subject**, not re-used files — the sound-off rule is
  per line.
- Per-scene archetype assignment and the role-colour semantics are in the script; the
  sequence is written out so the storyboard stage can check it reads as a rhythm.
- Handoff item 5 is the one to implement as code, not prose: a corpus token on screen
  without a rate token in the same frame should fail the build, not a review.

## Owed / not done here

- The `-en` cut is a **US rewrite, not a translation** of this file. It has its own hero
  (the format-twin phrase and its ~3.7× gap), its own rates and its own institutions;
  the only thing the two cuts share is the rung ladder.
- `run.json.owed` still stands: the real study packet (`study.py --ids JiuVKaO2a6c
  Jn3N9OzSY1c` once cookies exist) and a scrape of this lane. **Everything visual in the
  study is still MISSING** — no keyframes, no hook frames, no on-screen-text read — so the
  frame-level question this cut's binding constraint is *about* (how a corpus number is
  shown with its rate) rests on our own rule, not on observed evidence.
- vidIQ packaging pass for the title lock: 13 credits remain against a ~35-credit budget.
  The three title options above are unverified and must be treated as candidates.
