---
summary: Milestone note for «Pehla 1 Lakh / The First $10,000» (hi 8:34.8 · en 8:25.6) — the channel's FIRST MEDIUM-tier run, FIRST swiss-band build and first *offense* topic. Both cuts rendered, MASTER QA PASS, packaged, facts promoted; **LIVE on YouTube 2026-08-01, source archived to `src/`, studio dirs deleted** (hi youtu.be/TxAANc0_7lQ · en youtu.be/UF350uxHlqU). **Thumbnails AI-enhanced retroactively 2026-08-06** — the gullak/coin-jar pair, with the prompts kept in-note. The durable lesson is one class of bug seen five times: **every constant in this pipeline was tuned at SHORT's 9 lines and misbehaves at 86.** Second lesson: **every image defect on both cuts was invisible at contact-sheet size and legible at 1:1** — root cause was country-blind queries. Owed — the enhanced PNGs are not in the repo · re-measure legibility on them · swap the live thumbnails · analytics after 28 days.
updated: 2026-07-31
source: run.json + the 39 stage logs in logs/ (fin-research → fin-render), both publish packs, facts-staging.md, and the prior-run `chosen:` lines read back from vault/videos/{pay-yourself-first,good-debt-vs-bad-debt,credit-history}/youtube-metadata-{hi,en}.md
---

# The First ₹1 Lakh / The First $10,000 — milestone note

Run 2026-07-30 → 07-31, `/finance-video`. Topic: why the first savings milestone is the
hardest one — **zero of it comes from returns** — and what the same monthly amount buys
you at the tenth milestone. Selected as topic #1 of
[[../../knowledge/niches/finance-topics-2026-07-31]] (226,845 views at **48× subs** on a
4,660-sub faceless Hindi channel).

**Three firsts, all deliberate:** first **MEDIUM** tier (510 s target vs the six previous
~3-minute cuts), first **swiss-band** architecture (creator pick over the locked
blockframe-9 default), and the channel's first **offense** video after six defense ones.
That combination is why this run found five tooling defects: nothing in the pipeline had
ever run at 86 scenes.

Stage attempts: fin-research 2 · **fin-build-hi 2 · fin-build-en 3 · fin-render-hi 4 ·
fin-render-en 3** (fin-render-en-3 and fin-render-hi-4 are QA-only invocations on
re-encoded files, not reworks — each log says so at the top). Everything else attempt 1.
Budget: **178 of 200** ElevenLabs calls (86 hi + 92 en). Pixabay: 0 paid calls;
stock came from Pexels + Pixabay free tiers over 4 asset rounds (hi 2, en 3).

## The two cuts

| | Hindi / India (@cashguruguides) | US / English (@moneymavens101) |
|---|---|---|
| Upload file | `studio/videos/first-lakh-first-thousand-hi/renders/PUBLISH-1080p-hi.mp4` | `studio/videos/first-lakh-first-thousand-en/renders/PUBLISH-1080p-en.mp4` |
| ⚠️ Not the deliverable | `FINAL-` / `MIXED-` are pre-loudnorm (−3.2 dBTP) | same |
| Runtime | **514.789 s timeline / 514.900 container — 8:34.8** · 15,444 f @ 30/1 · 783.8 MB | **505.561 / 505.600 — 8:25.6** · 15,167 f @ 30/1 · 757.8 MB |
| Scenes / lines | **86** | **92** |
| Chapters | 9, per-line model (0:00 · 1:00 · 1:54 · 2:41 · 3:42 · 4:38 · 5:40 · 6:27 · 7:36) | 9, per-line model, smallest gap 43 s |
| Voice | ElevenLabs **Harsh** `HTUuC7OeeEt6OL5fViVe`, `eleven_multilingual_v2`, style 0 — Devanagari Standard Hindi | ElevenLabs **Brian** `nPczCjzI2devNBz1zQrb` — US rewrite, not a translation |
| Title (recommended) | **"Pehla 1 Lakh Kaise Banaye — 20 Mahine vs 7 Mahine"** | **"Why The First $10K Is The Hardest — 12.5 Months vs 6"** |
| Thumbnail | `…-thumbs/thumbnail-hi.png` (§v2) | `…-thumbs/thumbnail-en.png` (§env2) |
| Publish pack | [[youtube-metadata-hi]] | [[youtube-metadata-en]] |
| Script / storyboard | [[script-hi]] · [[storyboard-hi]] | [[script-en]] · [[storyboard-en]] |

Architecture: **swiss-band** on both, `tier: medium`. The pack's Gate-2 sameness check is
**not flagged on either channel for the first time in six uploads** — architecture, tier,
runtime, scene count, chapter model and register all changed at once.

## Hero numbers (with sources)

Full sourcing and HARD/SOFT tags: [[facts-staging]] — promoted to
[[../../knowledge/money-facts-2026]] by the orchestrator this run (this stage does not
promote facts).

**hi — ₹5,000/mo (₹30,000 in-hand × the locked 20% convention), monthly compounding:**

- **20 months to the first ₹1 lakh at 0%.** The hook. Zero help from returns.
- **A 12.4% return buys two months on the first lakh (20 → 18); on the tenth it buys
  thirteen (20 → 7).** That single contrast is the video. Every months-figure is
  **COMPUTED and labelled illustrative on screen**, never spoken as a statistic.
- Rate to build on: **7.1% PPF / 3-yr post-office TD** — HARD, DEA notification
  2026-06-30, two independent outlets quoting it; **9th/10th consecutive unchanged
  quarter**. Nifty 50 TRI ~12.4% is **SOFT** (both NSE PDFs 403'd) → "roughly twelve
  percent", never a decimal.
- Inputs: PLFS Annual Report 2025 ₹18,353–₹24,217 (HARD) · RBI Annual Report May 2026,
  net household financial savings 7.0% of GNDI (HARD) · AMFI ₹500/₹250 SIP minimum, on
  screen as **price evidence** only.
- ⚠️ **₹1 lakh is NOT the crossover.** Crossover ≈ ₹8.5 lakh at 7.1%, ≈ ₹4.8 lakh at
  12.4%. Conflating the psychological milestone with the crossover is the one factual
  error this script was most likely to make; the frames say "the *habit* takes over".

**en — $800/mo ($4,000 take-home × 20%), monthly compounding:**

- **12.5 months to the first $10,000 at 0%; the tenth $10,000 takes 6.**
- **The stronger US beat is the saving rate, not the return** — at the BEA's actual
  national personal saving rate of **2.7%** (June 2026, released 2026-07-30, read direct,
  HARD) the same $4,000 take-home saves $108/mo → **7.7 years** to the first $10,000.
  Both inputs HARD; same person, same market, same returns, only the rate moved.
- **Munger's $100,000 IS the crossover**, and it is arithmetic: at $9,600/yr and a ~10%
  market the money out-earns the contribution at ≈$96,000. The quote itself is **SOFT** —
  no primary reachable — so it is paraphrased with **no year and no venue on screen**, and
  it is colour, not evidence.
- Inputs: FDIC national savings rate **0.38%** as of 2026-07-20 (read direct, HARD) ·
  Fed funds 3.50–3.75% (read direct, HARD) · S&P 500 "about ten percent" **shape only** —
  four sources give four different decimals, so no decimal is ever spoken.
- Standing rules held: **no APY and no fund return on screen in either market.**

## QA (from the fin-render logs — both MASTER QA PASS)

| | hi (attempt 4) | en (attempt 3) |
|---|---|---|
| Runtime vs `timing.json` | 514.816 vs 514.789 → **+0.027 s** | 505.579 vs 505.561 → **+0.018 s** |
| VO lines verified present | **86 / 86** FINAL and PUBLISH (cross-correlation) | **92 / 92** FINAL, PUBLISH **and** by transcription |
| VO placement drift | **+0.0213 … +0.0214 s**, sd **0.0000**, 0 outliers / 172 | **+0.0213 … +0.0214 s**, sd **0.0000**, 0 outliers / 184 |
| PUBLISH loudness | **−14.07 LUFS**, LRA 3.00 | **−14.14 LUFS**, LRA 3.00 |
| PUBLISH true peak | **−1.26 dBTP** (0.26 dB margin), flat factor 0.000000, 2 peak samples of 24,711,168 | **−1.05 dBTP** (**0.05 dB margin**), flat factor 0.000000, 2 of 24,268,800 |
| Black segments | **0** in 15,444 f, two thresholds | **0** in 15,167 f, two thresholds |
| Silences | 136, all 0.42–1.28 s designed gaps | 136, 0.417–1.324 s, all designed |

Two audio facts worth keeping:

1. **The loudnorm pass that credit-history recorded as owed is now standard, and it
   worked.** Every previous cut shipped at −21 to −22 LUFS (7–8 LU under the feed); both
   of these land within 0.14 LU of −14 with zero added limiter activity. The
   `PUBLISH-` file is the deliverable — `FINAL-`/`MIXED-` are pre-loudnorm.
2. **en's −1.05 dBTP leaves 0.05 dB of margin** — a tenth of hi's. It passes and it
   bought no clipping (flat factor, peak count and abs peak count are identical to hi's
   to the digit), but **use a slightly lower loudnorm target on the next en cut.**
3. **+0.0213 s VO drift is one AAC-LC priming frame and always will be.** Fourth video to
   measure it, third independent method. Do not chase it.

## The durable lesson: a constant tuned at 9 lines misbehaves at 86

Five defects, one family. None of them was reachable at SHORT tier — all five had been
latent through six uploads. **All fixed and committed this run.**

| # | Defect | Why it hid until now | Fix |
|---|---|---|---|
| 1 | `scene.lead_in_seconds` + `tail_seconds` are charged **per line**, not per cut: 0.4 + 1.0 cost the hi cut **120.4 s of dead air in a 566 s timeline** | at 9 lines it is 12.6 s of a 180 s cut — invisible | tier-scaled to **0.25 + 0.55**; hi retimed 566.39 s → **514.79 s against a 510 s target with zero extra API calls** |
| 2 | `check_voice`'s flat chars/rate estimate **cannot see punctuation**, so the cold-open hook self-flagged as truncated | a 9-line script never had a heavily punctuated hook line carrying the whole estimate | estimate is now **pause-aware** (`tts.pause_seconds`); **trailing punctuation is charged nothing** because the engine trims end silence |
| 3 | `mix.py` looped the 248 s music bed with a **hard splice** | every SHORT cut was shorter than the bed and looped **zero times** | crossfaded. (Beds are creator-supplied and **not regenerable — never run `sfx.py --kit --music --force`.**) |
| 4 | fin-build reported "86 scenes eyeballed" when **8 had survived**: `hyperframes snapshot` **wipes its `-o` dir every run** | at 9 scenes one batch covers the cut, so nothing was ever overwritten | **per-batch snapshot dirs**. On its first outing this fix caught the en cut's CANADA / 5 CENTS defect at build time |
| 5 | `cuts.hi.chars_per_second` 12.5 vs **13.03 measured** (the voice runs 4% fast) | a 4% error on 180 s is 7 s | raised to 13.03 · **`max_scene_seconds: 9.0` added** · `tiers.medium/long` lines 78/92 |

⚠️ **Recorded trap — do NOT raise `cuts.en.chars_per_second` on its own.** Measured at
**17.73** against a configured lower value, but **fin-script's char budget ignores scene
padding**, so today two errors cancel. Fix both together or neither; changing one alone
will overrun the next en cut.

**The generalisation for the next run:** before the first MEDIUM/LONG run of anything,
ask of each constant *"is this charged per cut or per line?"* Per-line constants are the
ones that break, and they break silently in the direction of a longer video.

## The image lesson — the most expensive thing this run learned

**Every image defect on both cuts was invisible at contact-sheet size and legible at
1:1.** The full list, all caught by reading promoted picks at full resolution:

euro and zloty coins on the **rupee** hook · `1 ZLOTY` under a ₹1,500 card ·
`UNITED STATES OF AMERICA — ONE CENT` on a recap · `CANADA` / `DOLLAR` / `5 CENTS` under
the BEA statistic · `SUMA PLN` at **7.9 px/char** · prop money (two notes sharing serial
`E 34112707 E`; a second sheet repeating `LB45440078L`) · **Kaweco** branding held through
the whole CTA · a **FICO** mark · a **demonetised ₹500**.

**Root cause: country-blind queries.** Measured, not assumed —
`few dollar bills and coins on a table@pexels` returned **2 of 6 cells carrying bitcoin
props** from a query that never mentioned crypto; **naming the denomination** returned
**6 clean cells across three sheets**. So:

- **Name the denomination, not the category.** `twenty dollar bills on table`,
  not `dollar bills and coins`. The category query is what lets a zloty, a Canadian
  nickel or a bitcoin prop into a currency-specific frame.
- **Read every promoted pick at 1:1 before accepting it.** A contact sheet decides
  composition; it cannot decide text.
- **Serial numbers are a currency-authenticity test.** Repeated serials across notes in
  one frame = prop/reproduction money. New rejection rule, earned this run.
- **Brand marks are held longest on the CTA frame** — reject and re-query rather than
  settle there.
- **Resolution: Pexels `--pick` gives ~1880 px, Pixabay 1280 px.** Any slot carrying a ken
  zoom needs the Pexels source to clear the ≥1600 px rule.
- **Audit per FILE, not per scene** — `s11.jpg` served both s11's full-bleed background
  and s59's 630 px minor. A per-scene audit cannot see that.

*(that any of this affects retention is **unvalidated — no analytics yet**; it is a
correctness standard, not a performance claim.)*

### Gate two's standard is a measurement, not a taste

Gate two ships **legibility at 1080p, not at 3×**. On that standard it **let s59's GBP
chart through at 2.09 px/char** and **blocked `SUMA PLN` at 7.9 px/char** — the same class
of object, opposite verdicts, decided by a number. s59 was re-checked at 4× and 12×
nearest-neighbour: no glyph structure resolves, no currency symbol and no digit group is
readable, so `£10,000,000` cannot be read by a viewer. That is the whole test. Keep the
standard measured; the moment it becomes taste it becomes unarguable.

### The s57 sampling trap

**After a cross-dissolve the first safe sample is `scene_start + transition_seconds`.**
Sample at `scene_start` and you are reviewing the *outgoing* scene's photograph — which is
how s57's prop money was reported clean once before it was caught. Cheap rule, expensive
to relearn.

### Two build notes carried, not fixed

- **`blankBar`** — a scene table row carrying `bar: "—"` (the storyboard's "no title here"
  marker) rendered a full-width black bar holding one dash next to the CTA. The predicate
  now suppresses the element *and* its GSAP cue, with an inline self-check that runs on
  every `node build.mjs`. **A cue on a missing selector is a silent no-op — that is how
  this class of defect hides.** It currently lives in two cut-local `build.mjs` copies;
  folding it into `tools/scaffold` is a between-runs job (below).
- **s90 holds the video's only per-scene grade override.** Measured on delivered pixels,
  **s48 is darker** (YAVG 5.3–5.7, p90 24, YMAX 133 vs s90's 13.79 / 33 / 255) and passed
  gate two on a 1:1 read anyway — deliberate chiaroscuro, not a black frame. **If the
  per-scene grade allowance is ever widened, s48 is the better candidate than s90.**

## Thumbnails — AI-ENHANCED 2026-08-06 (retroactive; these tiles predate the step)

Both cuts were re-enhanced through **Nano Banana / Google Flow** after publication,
under [[../../knowledge/design-thumbnail-ai-enhance]]. The originals were built before
that step existed and were flat, near-monochrome grades — the "sterile" class the
creator later named. **Every string survived** both passes, including the `₹` glyph and
the two-colour sub-lines; zero garbling, zero invented text, one pass each.

**What the enhance added:** a worn brass **gullak** with four ascending ₹ coin stacks
on a scratched wooden table (hi), and a mason jar of US coins with three ascending
stacks and folded $1 notes (en), both in warm window light. The gullak is the finding —
a named cultural object in a prompt delivers what [[../../knowledge/stock-photo-sourcing]]
measures as a ~20 % hit rate for India-with-people stock.

⚠️ **The tone constraint was load-bearing and is a CONTENT decision, not a style one.**
This video's thesis is that the **first** lakh is slow and only the tenth is fast. A
triumphant cash-pile would argue with that, so both prompts specified *"patient,
ordinary saving, not wealth — small denominations, modest quantities, a domestic table.
No overflowing cash, no gold bars, no luxury, no glitter, no rays of light, no upward
arrows."* → **run the sound-off test on the PROMPT, where it is cheap, not only on the
returned image.**

<details><summary>The two enhance prompts (paste with the matching PNG attached)</summary>

Both share one skeleton; only the bracketed parts differ. Preserve-text block lists the
exact strings — hi: `Rs 5,000 / MAHINA` · `PEHLA LAKH` · `20 MAHINE` · the red rule ·
`dasva lakh - wahi Rs 5,000, sirf 7 mahine` (white, `7 mahine` green). en:
`THE FIRST $10,000` · `$800 / MONTH` · `12.5 MONTHS` · the red rule ·
`the tenth $10,000 - same $800, just 6 months` (white, `6 months` green).

```
Enhance this YouTube thumbnail. Keep the composition and the left-hand text
column EXACTLY as they are.

ABSOLUTE RULE — TEXT: preserve every existing letter pixel-for-pixel. Do not
re-render, re-letter, restyle, translate, move or re-space ANY text. [list the
exact strings, their colours and positions] must come back byte-identical.
Add NO new text, NO labels, NO signs, NO handwriting, NO numbers, NO captions
anywhere in the image.

WHAT TO REBUILD — only the right 55% of the frame, behind and around the type:
Replace the flat grey plate with a warm, cinematic, photoreal still life on a
worn wooden table in soft late-afternoon window light. Deep shadow on the left
so the text column stays clean and high-contrast; warm amber falloff right.

ADD, on the right third only, as ONE clear hero group:
  hi — a traditional Indian steel or clay gullak (coin bank), slightly worn;
       three or four modest stacks of Indian rupee coins gently ascending left
       to right; a few folded Indian rupee banknotes under the nearest stack
  en — a plain glass jar holding US coins about a third full; three or four
       modest ascending stacks of US coins; a few folded US banknotes under the
       nearest stack
Shallow depth of field, warm rim-light on the metal, visible table grain.

TONE — this matters: it must read as PATIENT, ORDINARY SAVING, not wealth.
Small denominations, modest quantities, a domestic table. No overflowing cash,
no gold bars, no luxury, no glitter, no rays of light, no upward arrows.

HARD CONSTRAINTS:
- [INDIAN | US] currency only. No other currency. No currency symbols drawn
  anywhere in the art.
- ONE hero group. No charts, pie graphs, receipts, bill lists, checklists,
  progress bars or infographics. Small props turn to mud at 320x180.
- No people, no faces, no hands, no bodies anywhere.
- Not a collage, not a comic, not 3D-render or CGI. One continuous photoreal
  scene with real optics.
- Do not add any promise, badge, tick, seal or arrow implying wealth, riches,
  guaranteed returns, "financial freedom" or "get rich".
- Output 16:9, 1280x720.
```
</details>

🔴 **Owed on the enhanced pair:** the returned PNGs are **not in this repo** — same gap
as japanese-money-methods. Save them as `src/thumbs/thumbnail-{hi,en}-ai.png`. They also
return at ~2752×1536 (1.79:1) and need resizing to 1280×720 before they replace the live
thumbnails. And `12.5 MONTHS` now overlaps the jar in the -en tile — **the ≥40 % assert
has not been re-measured on the returned image**, only eyeballed.

## The original (pre-enhance) builds — ONE per cut, creator rule 2026-07-29

`studio/videos/first-lakh-first-thousand-thumbs/thumbnail-{hi,en}.png`, one HyperFrames
project per slug (hi §v2 at 0–2 s, en §env2 at 2–4 s). Both: `npm run check` 0 lint /
0 runtime / 0 layout / 0 motion, **25/25 WCAG AA**; legibility measured off the exported
PNG downscaled to 320×180 — hi `20 MAHINE` **65.0%** of frame width, en `12.5 MONTHS`
**77.5%** (threshold 40%). Currency firewall verified by splitting the project at the
`#env2` marker: hi section 0 `$`, en section 0 `₹`.

**`chosen:` is filled by construction on both cuts** — with one build there is nothing to
choose. Two things are new and traceable to this video's own render: the label is a
**squared module** (every prior thumbnail on both channels used `border-radius: 999px`)
and the statement **hangs from a rule** — `.swiss-band` grammar, so the thumbnail and the
video finally agree. Honest structural repeat named in both packs: a **duration in the red
mega slot** is now the third consecutive @moneymavens101 upload (18 YEARS → 7 YEARS →
12.5 MONTHS); what has never shipped before is a thumbnail whose whole idea is **two**
durations, with the accent colour carrying a second contrasting figure rather than
restating the focal one. Cross-channel: the en thumbnail deliberately avoids the en cut's
quarter macro so the pair reads as siblings, not as one asset in two languages.

### Prior-run `chosen:` readback (procedure step 3)

| Pack | `chosen:` as of this close-out | Upload |
|---|---|---|
| pay-yourself-first hi / en | **blank** | LIVE 2026-07-28 — youtu.be/PKU0_TeJ9_c · youtu.be/mlvp4xZTROg |
| good-debt-vs-bad-debt hi / en | **v2** ✅ (creator pick, 2026-07-29) — already recorded in [[../good-debt-vs-bad-debt/index]] | LIVE 2026-07-29 |
| credit-history hi / en | **blank** | LIVE 2026-07-31 — youtu.be/j_YM-im4qz4 · youtu.be/yoN-gAATN6Y |
| **this pair hi / en** | **v2 / v2** (filled by construction) | not uploaded |

**No prior milestone note changed this run** — nothing was newly filled. The four blanks
are all on live videos, so the picks remain recoverable by comparing each live thumbnail
against the PNGs in that video's `src/thumbs/`; fin-archive has no network access, so that
readback stays owed to whoever can open the URLs.

## Search + positioning findings worth keeping

- **The demand verb in this lane is EARN, not SAVE — in both markets.** hi: six of seven
  completions on `pehla 1 lakh` say `kamaye`, not `bachaye`. en: the `10000 dollars` lane
  is `make/earn your first 10000`. **This video teaches accumulating from a fixed salary.**
  Titling into the earn verb buys CTR and loses retention on exactly that mismatch, so
  every recommended title leads with the build/save spelling and the earn strings are kept
  as tags only.
- **The thesis is a query in the US and is not in India.** `why the first 10k is the
  hardest` is live (and `how long does it take to save 10k` is live in its own right);
  `sabse mushkil 1 lakh` returns **NO SUGGESTIONS**, which retired the hi script's own
  recommended title. Where the thesis has no query, **the thumbnail carries the thesis and
  the title carries the query.**
- **Spelling decides the lane.** `the first 10000 is the hardest` redirects to the
  *hundred*-thousand string; `10K` owns it. And in Hindi the numeral `1` is load-bearing —
  `pehla lakh` without it lands in a devotional corpus.
- **`library.db` has a finance lane now** — 2,970 rows, **423** matching
  `lakh|crore|saving|compound|sip|invest|bachat` (it was 0 of 1,124 at credit-history), so
  the channel-wide scrape owed since then is done. **Limit:** the `subscribers` column is
  empty across the lane, so **views÷subs cannot be recomputed from library.db** — the 48×
  ranking still lives only in the niche note.
- **Runtime question, now half-answered and testable.** Every non-podcast lane leader runs
  **11–26 min** and the 48× proof ran **21:50**; this cut is 8:35 — the channel's longest
  by 2.7× and still shorter than every competitor. **This is the first datapoint the
  channel will ever have on length, and it is the main thing to read at 28 days.**
  *(unvalidated — no analytics yet)*
- Lane winners title a first-person conditional ("If I Started Investing in 2026") or a
  step-by-step — **neither available to us** (persona rules; not a fund-picking video).
  Our differentiator: **no competitor title in the pull carries a months-to-milestone
  figure.**

## Current state + what is owed

**State: BOTH CUTS RENDERED, QA'D, PACKAGED — NOT UPLOADED.**
No YouTube URL exists, so per the finished-video rule in [[../../CLAUDE]] this video is
**not finished**: `tools/archive_cut.py` has **not** been run, **nothing has been deleted**,
and `studio/videos/first-lakh-first-thousand-{hi,en,thumbs}` must survive until the URLs
land. Post-delivery cleanup runs only after upload, on the creator's word.

**Owed:**

- **proof-listen (hi, en)** — nobody has listened to either cut end to end; QA measured
  placement and levels, not delivery
- **thumbnail pick** — `chosen:` is filled by construction on both cuts here; still
  **blank on pay-yourself-first (hi + en) and credit-history (hi + en)**, all four live,
  all four recoverable off the public thumbnail
- **upload** (hi → @cashguruguides · en → @moneymavens101, `PUBLISH-` files only), then
  `tools/archive_cut.py <slug> --hi <url> --en <url>`
- **analytics after 28 days** — and specifically the **length** read (8:35 vs a lane whose
  breakouts run 15–22 min) and CTR against the two-duration thumbnail
- **re-scrape `fQyN80dLDpQ`** — `study.py "Story of Success" --skip-video`; it 429'd, so
  **the topic's own 48×-subs proof has no transcript in the study packet**
  (`run.json owed_rescrape`)
- **creator decision: `architecture_lock` vs ask-the-style-every-run.**
  `tools/format.json` carries `architecture_lock: blockframe-9` while the command asks the
  style each run and takes the answer — this run resolved the disagreement by hand and
  shipped swiss-band. Two coherent options: (a) reword the lock as a pre-selected
  **default**, or (b) delete it and let rotation supply the default. Per "fix defaults,
  not gates", this belongs in config, not in a per-run judgement call
  (`run.json owed_creator_decision`)
- **between-runs scaffold jobs:** re-path `blockframe.css`, and **fold `blankBar` into
  `tools/scaffold`** so it stops living in two cut-local `build.mjs` copies
- **next en cut: a slightly lower loudnorm target** (0.05 dB of true-peak margin is thin)
- **next time the per-scene grade allowance is discussed: s48, not s90**
- **do not raise `cuts.en.chars_per_second` alone** — see the trap above

> Everything in this note is a **pipeline/engineering measurement** except where marked
> `unvalidated — no analytics yet`. **Nothing here has been promoted to
> [[../../knowledge/best-practices]]**: that file takes evidence only after ≥28 days of
> real analytics, and zero-view "evidence" beside dated confirmations saying the opposite
> would poison the one file that compounds.

Related: [[script-hi]] · [[script-en]] · [[storyboard-hi]] · [[storyboard-en]] ·
[[audit-hi]] · [[audit-en]] · [[facts-staging]] · [[youtube-metadata-hi]] ·
[[youtube-metadata-en]] · [[../../knowledge/money-facts-2026]] ·
[[../../knowledge/design-finance-blockframe]] ·
[[../../knowledge/finance-audit-2026-07-29/index]] ·
[[../../knowledge/niches/finance-topics-2026-07-31]] ·
[[../../knowledge/stock-photo-sourcing]] · [[../credit-history/index]] ·
[[../../workflows/finance-video]]

## Published + archived (2026-08-01)

**State: LIVE on YouTube · source archived · studio dir deleted.**

| Cut | Channel | URL | Thumbnail |
|---|---|---|---|
| en | @moneymavens101 | https://youtu.be/UF350uxHlqU | `src/thumbs/thumbnail-en.png` |
| hi | @cashguruguides | https://youtu.be/TxAANc0_7lQ | `src/thumbs/thumbnail-hi.png` |

**Source: `src/`** — composition, meta/package JSON, `gen_vo_*.sh`, the VO lines
(`assets/voice/*.txt`), the image prompts (`assets/img/*.src`), stock CREDITS and the
thumbnail PNGs. `studio/videos/first-lakh-first-thousand*` is **deleted** per the finished-video rule
(`vault/CLAUDE.md`). **Re-render is reproducible, not free** — the scene photos and VO
mp3s are gone, so a rebuild re-pays image gens + ElevenLabs off the archived prompts
and lines. `gen_vo_*.sh` still `cd`s into the deleted studio path — repoint it first.

Still owed: analytics after 28 days.
