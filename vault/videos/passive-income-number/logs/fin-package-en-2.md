---
summary: fin-package, passive-income-number, cut en, attempt 2 — the R3/R3b packaging update. Title LOCKED at «Living Off Dividends: How Much Do You Actually Need Invested?» with a real vidiq_score_title of 87 (gate 75, cleared by 12); tag block rebuilt on R3b vidIQ volumes to 14 tags / 448 chars / 52 headroom with per-tag autocomplete-vs-volume provenance; thumbnail re-verified against the new title and KEPT, not re-cut, with npm run check and the 320x180 legibility measurement re-executed this session.
updated: 2026-08-15
stage: fin-package, cut en, attempt 2
---

# Ran

| # | Command / action | Result |
|---|---|---|
| 1 | `cat vault/CLAUDE.md` · `cat tools/format/fin-package.json` | Read first, per contract. `hyperframes_pin` = **0.7.66**, `packaging.title_score_min` = **75**. No missing constant this pass. |
| 2 | Read `vault/videos/passive-income-number/youtube-metadata-en.md` in full (483 lines, attempt 1) | The pack to be updated in place. |
| 3 | `python3 tools/autocomplete.py --q "living off dividends" --gl us` | 10 suggestions, seed at **#1** |
| 4 | `python3 tools/autocomplete.py --q "how much do you need invested" --gl us` | 10 suggestions, `how much do you need invested to live off dividends` at **#1** |
| 5 | `python3 tools/autocomplete.py --q "dividend investing" --gl us` | 10 suggestions, seed at **#1** — the "typed" half of the R3b anchor tag |
| 6 | Read `studio/videos/passive-income-number-thumbs/index.html` `<div id="type-en">` + `:root` colour tokens | Three text nodes confirmed; `--fund #22c55e`, `--warn #ef4444`, `--ink #f5f3ec` |
| 7 | `cd studio/videos/passive-income-number-thumbs && npm run check` (runs `npx --yes hyperframes@0.7.66 check`, pinned) | **Check passed** — 0 lint · 0 runtime · 0 layout across 9 samples · 0 motion · **15/15 WCAG AA** |
| 8 | PIL: downscale `thumbnail-en.png` 1280×720 → 320×180 (LANCZOS), isolate `--fund` / `--warn` / ink pixels, measure x-extent + right margin | Numbers in §Evidence |
| 9 | PIL: mean luma of left third vs right third of the shipped PNG | Plate-visibility check — the failure mode where the scrim crushes the photograph to black |
| 10 | Python char-count of the candidate tag block against the 500 limit, per-tag and total | 448 / 14 tags / 52 headroom |
| 11 | Edited `youtube-metadata-en.md` in place — 7 scripted replacements, each with an `assert` on the target string so a silent no-op is impossible | All 7 asserted and applied |
| 12 | Post-edit verification: heading inventory, regex re-extraction of the shipped tag block, grep for stale attempt-1 references | 4 stale references found and fixed (§Changed) |

**Not run, and why:** `npx hyperframes snapshot` — the thumbnail was judged a KEEP (§Evidence), so there was nothing to re-export; re-exporting an unchanged source would have produced a new PNG mtime and destroyed the byte-identity evidence. `tools/transcript.py` — the caption pack was verified in attempt 1 and the brief explicitly excludes it from this pass. No `backend/` scraper — a competitor scoreboard cannot change a locked title (§Owed).

# Failed

**Nothing failed this pass. Two things were REJECTED on judgement rather than failing a check, and one attempt-1 self-inflicted error was caught in review:**

1. **The highest-scoring generated title was not shipped.** `Dividend Investing: Don't Make This Calculation Mistake` scored **91**, four points above the shipped 87 and the top of the whole cluster. Rejected: the video does not correct a mistake the viewer is making, it prices an income. A "you're doing it wrong" hook on an arithmetic walk-through is a promise chapter 6 spends four lines refusing to make. Score is necessary, not sufficient — the SS-taxation precedent, where all eight well-scoring options were rejected.

2. **`personal finance` was rejected despite the highest opportunity score in the R3b set (76.3, 257,592 US/mo).** R3b left the call open with the condition "include only as a broad anchor if you have room, and say it was chosen despite its share." It would have fit — 448 + 2 + 16 = 466, leaving 34 headroom. Rejected on three grounds recorded in the pack: PK 21.9% vs US 12.9% share on a US-only cut; it is the single broadest string available attached to a title that just became sharply specific; and it spends 18 of a 52-character cushion that exists as a control, not as slack.

3. **⚠️ Caught in my own review: I initially transcribed row 10 of the `how much do you need invested` pull as a duplicate of row 8 and wrote a sentence explaining the "duplicate".** The tool actually returned `how much do you want to invest every month phonepe`. Both the row and the invented explanation were corrected before the file was finalised (an `assert`-guarded replacement, so the fix is verifiable). Recording it because the failure mode is exactly the one this stage exists to prevent — **a fabricated observation dressed as recorded evidence**, and it survived one self-read. Raw tool output goes in by copy, never by recall, and a sentence *interpreting* raw data is where the fabrication attaches.

# Evidence

## 1. Title — the score gate is now MET, with a real number

| Title | `vidiq_score_title` | Verdict |
|---|---|---|
| **Living Off Dividends: How Much Do You Actually Need Invested?** (61 chars) | **87** | **SHIPPED** |
| How Much You Need Invested To Live Off Dividends ($5,000/Month at 4%) (69) | 76 | attempt-1 baseline, superseded (+11) |
| Living Off Dividends In Retirement: How Much Do You Actually Need? (66) | 81 | runner-up |
| How Much You Need Invested To Live Off Dividends (The Honest Number) (68) | 74 | **under the 75 gate** |
| Dividend Investing: Don't Make This Calculation Mistake | 91 | rejected on claim (§Failed 1) |

`packaging.title_score_min` = 75. **87 clears it by 12.** Written to frontmatter as `title-score: 87` / `title-scored-on: 2026-08-15`, verified by re-reading the file after the edit.

**Three of ten generated titles failed a `run.json` constraint, independent of score:**

| Generated | Score | Constraint |
|---|---|---|
| The $5,000/Month Dividend Goal: Is Your Portfolio Big Enough? | 85 | `derived_income_carries_assumption` — bare derived income, no rate |
| How Much Capital Do You Need for $5,000/Month? The Harsh Reality | 78 | `derived_income_carries_assumption` — same figure, same failure |
| Planning for $5,000/Month: The Arithmetic of Financial Independence | 71 | `no_unsourced_retire_early` **and** `derived_income_carries_assumption` |

**30% constraint-failure rate on the generated cluster, and all three failures are the same figure.** The generator reaches for the derived income number by default because it is the most clickable string in the description it was handed. Reusable: on any corpus-arithmetic video, filter `vidiq_generate_titles` output on the constraints *before* reading the scores, or the 85 will anchor the decision.

**The locked title passes `derived_income_carries_assumption` by ABSENCE** — no derived income figure, no corpus figure, no rate anywhere in the 61 characters. That is strictly stronger than the attempt-1 title, whose entire `at 4%` suffix existed only to qualify a figure it did not need to carry.

## 2. Demand — both halves of the title verified typed, `gl=us`, 2026-08-15

`--q "living off dividends"` — **seed is its own #1**, ten deep:

```
1	living off dividends
2	living off dividends in retirement
3	living off dividends canada
4	living off dividends australia
5	living off dividends passive income
6	living off dividends uk
7	living off dividends south africa
8	living off dividends philippines
9	living off dividends robinhood
10	living off dividends for early retirement
```

`--q "how much do you need invested"` — **title's second half at #1**:

```
1	how much do you need invested to live off dividends
2	how much do you have invested
3	how much do you need to invest to receive $1000 a month in dividends
4	how much do you need to invest each month to retire a millionaire
5	how much do you need to invest in real estate
6	how much do you need to invest in forex
7	how much do i need to invest to make 1000 a month in dividends
8	how much money you need to invest in stock market
9	how much do you want to invest every month
10	how much do you want to invest every month phonepe
```

`--q "dividend investing"` — **seed is its own #1**:

```
1	dividend investing
2	dividend investing in pakistan
3	dividend investing psx
4	dividend investing for beginners
5	dividend investing strategy
6	dividend investing portfolio
7	dividend investing india
8	dividend investing vs growth
9	dividend investing course
10	dividend investing book
```

A seed returning **itself at #1** is the autocomplete signature of a head term rather than a tail completion. Attempt 1 only reached `how much do you need invested to live off dividends` at **#3**, off the differently-worded seed `how much do i need invested`; the exact phrasing moves it to **#1**. No empty return this pass — the one empty result in this pack remains attempt 1's `passive income number` (**NO SUGGESTIONS**), which is still recorded.

⚠️ Rows 2/3/7 of the `dividend investing` pull (`in pakistan`, `psx` = Pakistan Stock Exchange, `india`) and row 10 of the second pull (`phonepe`, an India payments app) are non-US completions inside a `gl=us` request. Third recurrence of this caveat in this pack.

## 3. The keyword doing measurable work: «Invested» = 6 points

```
87  Living Off Dividends: How Much Do You Actually Need Invested?
81  Living Off Dividends In Retirement: How Much Do You Actually Need?
```

The 81 differs by dropping `Invested` and adding `In Retirement`. **Six score points for one word**, and autocomplete explains it: with `Invested`, the title's second half is a live #1 suggestion string; without it, it is a paraphrase. Carried into the pack as a reusable finding — on a "how much do you need" question, the *verb of the asset* (invested / saved / in your 401k) is the keyword, not the audience qualifier.

## 4. Thumbnail — re-run against the locked title, KEPT

**Judgement: BETTER, not neutral and not a miss.** Attempt 1's stated worry was that a title leading with a figure would duplicate the tile's numbers and waste it. The locked title carries **no figure at all** and ends in a question mark, so the relationship changed from *complementary* to **question → answer**: the title asks how much, the tile is the two numbers with their rates. The one figure that could have collided (`$5,000/Month`) is gone from the title entirely, so the collision is not avoided but structurally impossible. `<div id="type-en">` was **not** edited; the PNG is byte-identical to attempt 1 (mtime unchanged, 06:17).

Re-measured this session on the shipped `thumbnail-en.png`, downscaled 1280×720 → 320×180:

| Line | colour | x-extent | span | % of width | right margin |
|---|---|---|---|---|---|
| `$5.6M at 1.08%` | `--warn` #ef4444 | 17 → 168 | **152 px** | **47.5 %** | **151 px (47.2 %)** |
| `$1.5M at 4.0%` | `--fund` #22c55e | 17 → 161 | 145 px | 45.3 % | 158 px (49.4 %) |
| `Same paycheck.` | `--ink` #f5f3ec | 17 → 124 | 108 px | 33.8 % | 195 px (60.9 %) |

Threshold ≥40 % for the largest line: **47.5 %, passes**. Real right margin: **151 px**, nothing touches the frame edge. Identical to attempt 1 to the pixel — which is itself the evidence that nothing was silently re-exported between passes.

**The photograph is genuinely on the tile** (the documented failure is a scrim that crushes the plate to flat black). Mean luma, sampled every 4th pixel: **right third 147.2** (the plate side) vs **left third 36.6** (the type side), full frame 84.3. A **4.0×** ratio — the plate reads as a photograph, not as a black field.

**`npm run check`** re-executed this session, not quoted: `npx --yes hyperframes@0.7.66 check` → **Check passed** · 0 lint · 0 runtime · 0 layout across 9 samples · 0 motion · **15/15 WCAG AA contrast**. Pin honoured on the only `npx` call made.

**No-repeat re-checked against the NEW title.** Title tokens `Living Off Dividends How Much Do You Actually Need Invested` vs tile tokens `Same paycheck at at $1.5M 4.0% $5.6M 1.08%` — **zero shared words, zero shared figures.** A cleaner pass than under the attempt-1 title, which at least shared the money register.

**Subject test improves too:** the old title buried `Dividends` at character 41; the locked title opens on it (`Living Off Dividends:` = the first 21 chars, and browse rows truncate from the right). The vehicle keyword is now the first thing read on the title line, and the price pair is the whole of the tile — subject named once, prominently, never twice.

**One trap flagged in the pack for the next editor:** do NOT add the word `Dividends` to the tile now that the title leads with it. That would be the first title/tile repeat this pack has ever had, for nothing.

## 5. Tags — rebuilt on R3b volumes

| | attempt 1 | attempt 2 |
|---|---|---|
| strings | 14 | 14 |
| characters | 458 | **448** |
| headroom under 500 | 42 | **52** |

Verified by re-extracting the block from the written file with a regex and counting: **448 chars, 14 tags.** Headroom went UP while the block got stronger.

**Added — `dividend investing`** (18 chars). **48,704 US/mo at competition 39.2** — lowest competition of any term with real US volume, second-highest opportunity (69.2), and **44.4 % US share**, against 8.1 % for `passive income`. Autocomplete-verified this pass at #1.

**Added — `living off dividends`** (20 chars). The locked title's head term, missing from attempt 1's block, which carried only the `…in retirement` long form. Seed's own #1, 8,636/mo global · comp 52.8 · overall 54.1.

**Dropped to make room:** `4 percent rule` (14, the most generic of three 4%-rule strings, fully subsumed by the two longer ones that stay) and `how much money do i need to retire` (33, the broadest string in the block and the only one outside the dividend family where every measured volume actually lives). Net −47 / +38 / −2 separators = 458 → 448.

**⛔ `passive income` excluded despite 346,954/mo.** Top markets **PK 21.3 · IN 11.0 · BD 10.3 · VN 8.8 · US 8.1** — the worst US share in the set, on a cut that has been US-only since 2026-08-15. Independently, `passive income forever` sits inside the `no_unsourced_retire_early` family the constraints table already polices. Two independent reasons.

**Zero-volume terms recorded so nothing looks like a sacrifice:** `live off passive income` = **0** and `how to retire off dividends` = **0**. The latter was dropped in attempt 1 on constraint grounds — **the constraint cost this pack zero measurable demand.** Combined with attempt 1's `passive income number` → NO SUGGESTIONS, the phrase family the slug is named after is dead twice over.

**Provenance is labelled per tag** in the pack as **A** (autocomplete — proves TYPED, with the seed named) and **V** (vidIQ `countryVolume` — proves HOW OFTEN, in which country). Ten of fourteen are A-only; four carry both. There is no tag with volume but no typed evidence.

## 6. The slug/demand mismatch — noted, nothing renamed

The video is `passive-income-number`; the locked title, the whole tag block and every volume in R3b live in the **dividend** family. Per the brief: **noted, not renamed.** The slug is an internal run identifier that no viewer sees, and renaming it mid-run would break `run.json`, six studio directories, ~70 log files and the archive path for a cosmetic gain.

## 7. The volume-authority caveat is now measured, not suspected

Attempt 1 wrote *"the R3 vidIQ pass should be treated as the volume authority, not this [autocomplete]."* R3b ran and proved it in a way autocomplete could not: autocomplete could see that *something* was off in `gl=us` pulls (rupee, lakh, `psx`, `phonepe` completions) but could not say **how** off, and had no way to reveal that the cleanest-looking generic term in the niche (`personal finance`, 76.3 overall) is **12.9 % US** and therefore among the worst picks for this cut. **Third demonstration that autocomplete-only is insufficient** on this channel, after `japanese money habits` (31,899/mo, invisible to it) and attempt 1's own contamination. The pairing, not either alone, is the standard.

# Changed

**One file rewritten in place** — `vault/videos/passive-income-number/youtube-metadata-en.md` (483 → 657 lines, 49,370 → 69,7xx bytes). Eleven scripted edits, each guarded by an `assert` on the target string so a silent no-op was impossible.

| Section | Change |
|---|---|
| frontmatter | `title-score: UNSCORED…` → **`title-score: 87`**; `title-scored-on:` → **`2026-08-15`**; new `title:` line carrying the locked string; `stage:` → attempt 2; `summary:` finding (2) rewritten from "gate UNMET" to RESOLVED with the number; `source:` seed count 20 → 23; tag description 458/42 → 448/52 with provenance |
| §The four things this pack must not get wrong | `derived_income_carries_assumption` row rewritten — the constraint now passes by **absence** (no figure in the title) rather than by disclosure; `no_unsourced_retire_early` row extended with the 71-scoring rejected title and the zero-volume postscript |
| **§Title** | Replaced end to end (5,010 → 8,047 chars): the lock + score table, the 91-scorer rejection, the three constraint rejections, both re-pulled autocomplete returns raw, the «Invested» = 6-points finding, the slug/demand note, and why the title now passes by absence. Script summary for the scorer retained verbatim (it is what produced the scores) |
| §Thumbnail | **New lead block** `✅ RE-RUN AGAINST THE LOCKED TITLE — KEPT, NOT RE-CUT` with the before/after relationship table and the six re-run measurements; `never repeat the title` row re-checked token-by-token against the new title; subject-test section extended with the truncation argument; `If the title moves` rewritten as an explicitly-not-exercised runbook plus the "don't add `Dividends` to the tile" trap |
| **§Tags** | Rebuilt: new 448-char block, 14-row A/V provenance table, the two additions with their numbers, `passive income` exclusion, `personal finance` considered-and-rejected, zero-volume table, dropped-this-pass table, attempt-1 drops retained (with R3b competition numbers added to the stock-pick row) |
| §Search evidence | Header 20 → 23 seeds; three new seed rows appended to the table; caveat paragraph rewritten as RESOLVED with the country-share numbers; competitor-scoreboard note updated — still owed, but its value has changed now that the title is locked |
| §Gate 2 | One sentence only, in the positioning note: "no slate slot **or** a scored title" → still no slate slot, but now a scored title above the same gate the slate is held to. Everything else in Gate 2 untouched, per the brief |
| §Owed | Items 1 and 2 struck as CLOSED with their evidence; 3–6 restated; item 5 notes the enhance prompt needs no edit (it is plate-only, therefore title-independent); item 7 added for the sameness trend |
| new §Attempt 2 — what changed | An explicit changed/untouched ledger at the foot of the pack |

**Deliberately NOT changed**, per the brief and because the measurements still hold: the **description** including its chapter block (times read from the render's `data-start`; the script table is stale by up to 7 s) · the **caption pack** (149 cues) · **§Gate 2** substantively · the **AI-enhance prompt** (plate-only, so a title change cannot reach it) · **`thumbnail-en.png` itself** (byte-identical, mtime 06:17) · `narration-en.md` · `captions-en.srt`. No file under `studio/` was written this pass.

# Owed

1. **On-screen disclaimer — still UNMET.** `fact_gate.disclaimer_placements` requires all four; `onscreen` is absent from the render (0 hits for `advice` / `licensed` / `professional` / `Confirm` in `index.html`). Not fixable from this stage — a scene edit and a re-render. Should be decided **once at channel level** and written into `fact-integrity.md`, not re-argued per video.
2. **Competitor scoreboard — still not pulled.** R3b delivered *keyword* demand, not a competitor scoreboard; no `vidiq_similar_videos` / `vidiq_similar_thumbnails` call has been made on the `living off dividends` cluster, and that family is unreachable from this stage. Its value has narrowed: the title is locked, so a pull can no longer change it — what remains is thumbnail-composition evidence and a view-ceiling estimate for the cluster.
3. **`thumbnail-en-ai.png` does not exist.** The plate-only Nano Banana prompt ships and needs **no edit** for the new title. When it is run: re-measure the 320×180 legibility span and the contrast reading on the **RETURNED** image, not the pre-enhance render, then update the `chosen:` line.
4. **`vidiq_score_thumbnail`** needs a live `videoId`; score it the day the video goes up.
5. **Channel-level sameness trend.** Not a blocker — this is the **3rd** consecutive long-form per-line-chapter cut, not the 5th, so the enforcement bar is not met. A 4th would leave the channel one upload from it with no unspent lever (`architecture_lock` removed layout). Decide at the next `run.json`, before fin-script, the only point where tier is still free.
6. **Retired brand asset.** `assets/brand/moneymavens101.jpg` is still the retired pink coin-face, so this render carries the old avatar watermark on every frame — now on a third video. Not worth a re-render alone; worth fixing before the fourth.
7. **A checked-in filter for `vidiq_generate_titles` output.** 3 of 10 generated candidates broke a `run.json` constraint and one of them scored 85. Reading scores before applying the constraint filter anchors the decision on a string that cannot ship. This is a *default*, not a gate, per the fix-defaults-not-gates rule: the constraint filter belongs in the R3 procedure ahead of the score sort.
