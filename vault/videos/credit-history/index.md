---
summary: Milestone note for «Your Credit History» pair (Hindi/₹ 2:57.7 · US/$ 2:53.2) — both cuts rendered, MASTER QA PASS, facts promoted, committed 2026-07-29; publish packs written. NOT uploaded. Owed — proof-listen (hi, en) · thumbnail pick · upload · analytics after 28 days (+ finance-lane scrape, + the architecture decision below). ⛔ 6th consecutive blockframe-9 on BOTH channels: the flag itself is no longer the finding — the finding is that three written warnings changed nothing, because `tier` is chosen in run.json BEFORE fin-script while the pack that warns is read at upload AFTER the artifact exists.
updated: 2026-07-29
source: run.json + the fin-render / fin-build / fin-assets / fin-facts / fin-package logs in logs/ (the /finance-video pipeline) + the two publish packs; prior-run `chosen:` lines read back from vault/videos/{pay-yourself-first,good-debt-vs-bad-debt}/youtube-metadata-{hi,en}.md
---

# Your Credit History — milestone note

Run 2026-07-28→29, `/finance-video` pipeline. Topic: what a credit report is, what
builds it, what destroys it, and how long one miss stays visible — India cut on CIBIL /
36 months, US cut on FICO / the FCRA seven-year rule.

Stage attempts: **fin-research rescued** (no study note; `library.db` has no finance
lane — 2nd run rescued for this reason), **fin-facts attempt 2**, **fin-script-hi
attempt 2** (the `$-2` / `₹-5` naming bug below), **fin-build-hi attempt 2**
(wrong-subject car fob), **fin-render-hi attempt 2** (genuine re-run). Everything else
attempt 1. ⚠ **`fin-render-en-2.md` is NOT a failed attempt** — the en cut passed
gate ② first time; `-2` is invocation 2 (master QA) of the same attempt, and the log
says so at the top. Do not read it as a rework.

Budget: **18 of 30 ElevenLabs calls** (9 VO clips per cut). Pixabay: **hi 34 fetches
over 4 rounds** (14 accepted, 3 cut-ins dropped), **en 41 fetches over 6 rounds**
(11 accepted, 6 cut-ins dropped) — the retry ladder, not the budget, is what this cost.

## The two cuts

| | Hindi / India (@cashguruguides) | US / English (@moneymavens101) |
|---|---|---|
| Master | `studio/videos/credit-history-hi/renders/FINAL-1080p-hi.mp4` | `studio/videos/credit-history-en/renders/FINAL-1080p-en.mp4` |
| Runtime | **177.667 s (2:57.7)** video / 177.707 container · 12,412 kb/s video (12,594 overall) · 5330 frames · 279.8 MB | **173.233 s (2:53.2)** video / 173.248 container · 11,765 kb/s video (11,949 overall) · 5197 frames · 258.8 MB |
| Voice | ElevenLabs **Harsh** `HTUuC7OeeEt6OL5fViVe` — **Devanagari Standard Hindi** | ElevenLabs **Brian** `nPczCjzI2devNBz1zQrb` |
| Script | [[script-hi]] (9 lines h1–h9) | [[script-en]] (9 lines en1–en9, US rewrite not a translation) |
| Title (recommended) | "CIBIL Score Kya Hota Hai? Ek Missed EMI = 36 Mahine" | "How Long Do Late Payments Stay on Your Credit Report? 7 Years" |
| Publish pack | [[youtube-metadata-hi]] | [[youtube-metadata-en]] |

Structure of both cuts: **blockframe-9** (hook → roadmap → concept → what builds it →
what destroys it → action → math → do-today → recap).

## Hero numbers (with sources)

The two markets have **structurally different answers to the same question**, and this
is the run's most valuable fact: **the US 7-year rule does not exist in India.**

- **hi — one missed EMI is visible for 36 months (3 years)** of the month-by-month
  payment grid, and the account history behind it does not disappear (CIBIL's own
  words: "will always be a part of your credit history"). SOFT-tagged; CIBIL primary
  reached via domain-restricted search (cibil.com 403s a direct fetch).
  - Scale **300–900**, 700+ generally good, 750+ best pricing — TransUnion CIBIL
    (HARD), corroborated by two lenders' band-keyed rate cards.
  - Money beat: a **0.75–1.00 percentage-point** band spread on a **₹30,00,000 / 20-yr**
    home loan = **₹1,390–1,860 more a month, ₹3.3–4.5 lakh more interest**. HARD on the
    spread (Union Bank of India + Bank of Maharashtra published cards agree), SOFT on
    every specific rate — hence **no bank named and no rate quoted on screen**.
  - Factors are named and **ranked, never weighted** — CIBIL publishes no percentages.
- **en — most negative information stays 7 years, bankruptcy 10, and the clock starts
  at the original delinquency, not at payoff.** **HARD** — FCRA 15 U.S.C. §1681c(a)
  (Cornell LII) + CFPB, both read directly. Strongest claim in the file; it carries the
  hero, the title and thumbnail v1.
  - Scale **300–850**, 670+ "good" — FICO (owner) + CFPB (HARD).
  - **35% payment history + 30% amounts owed = 65% of the score** — myFICO + the Federal
    Reserve's 2007 Report to Congress agreeing independently (HARD on 35/30 only; the
    15/10/10 tail is single-sourced and stayed off screen).
  - Money beat: **$25,000 used car, 72 months, ~6% vs ~19%** → **$418 vs $590/mo,
    ~$172 more a month, ~$12,400 more in interest** (build-calculator output). SOFT on
    any decimal APR — Experian's own page, a restatement and Bankrate give three
    different super-prime figures, and the table's quarter label contradicts its article
    — so the screen says "about three times", never a decimal, never a quarter.
- Full sourcing + the HARD/SOFT tags: [[facts-staging]]. Promoted to
  [[../../knowledge/money-facts-2026]] by the orchestrator this run (archive does not
  promote facts).

### The fabrication this run refused

**Nine Indian blogs** (zetapp, gocredit, freed.care, bajajhousingfinance, loansparadise,
srfc, airtel, paytm, credithelpindia) assert that **CICRA 2005 mandates automatic
deletion of negative entries after 7 years.** No primary source exists; the one
industry account of the actual Act says the opposite (a seven-year *minimum*, **no
maximum** — which is why RBI opened a consultation on capping retention at all). **It is
the US FCRA rule wearing an Indian costume.** fin-facts tagged it REJECT; it is now in
money-facts-2026's "Do not claim". Scripting this topic from search results would have
shipped a fabricated statute in the Hindi cut. This is the clearest demonstration yet of
why fin-facts is a separate stage from fin-script.

## QA (from the fin-render logs — both MASTER QA PASS)

| | hi | en |
|---|---|---|
| Runtime vs timing.json | 177.667 s vs 177.642 → **+0.025 s** video / +0.065 container; 5330 frames exact | 173.233 s vs 173.227 → **+0.006 s** video / +0.021 container; 5197 frames exact |
| VO placement drift | max **+0.0216 s**, mean +0.0212, spread 0.0020 s over 9 clips | max **+0.0218 s**, mean +0.02129, spread 0.00092 s over 9 clips |
| Tail residual / accumulation | worst 0.5 ms over 176 s; **zero accumulation** | worst 0.5 ms over 172 s; **zero accumulation** |
| True peak | **−4.33 dBTP** (3.33 dB headroom) | **−3.00 dBTP** (2.00 dB headroom) — thinnest logged |
| Loudness | **−22.17 LUFS**, LRA 3.30 | **−21.19 LUFS**, LRA 3.60 |
| VO content | 9/9 lines, right slot, right order | 9/9; every sub-1.000 similarity is ASR numeral formatting only |
| Black segments | **0** at three sensitivities, 5330/5330 scanned | **0** at three sensitivities, 5197/5197 scanned |
| Master == gated composition | 4 frames PSNR + 3 visual confirmations | 6 frames PSNR (33.8–38.9 dB band) + 5 visual confirmations |

**Audio facts worth keeping (pipeline constants, not defects):**

1. **VO drift is +0.021 s and always will be.** 1024 samples @ 48 kHz = 21.333 ms =
   exactly one AAC-LC priming frame; the mux carries `start_pts=0` with no edit list, so
   the whole audio track sits one AAC frame late, uniformly. Measured at 21.29 ms mean on
   en. `pay-yourself-first` logged 0.021 s on both cuts by an independent
   cross-correlation method. Far inside ITU-R BT.1359. **Do not chase it.**
2. **Loudness runs 7–8 LU under YouTube's −14 LUFS on every cut ever rendered here**
   (this pair −22.17 / −21.19; good-debt −22.02 / −21.09; pay-yourself-first −22.24 /
   −21.13). Broadcast-correct (EBU R128 = −23), quieter than the feed, and YouTube
   applies no positive gain.
3. **en's −3.00 dBTP comes from the source, not the render** — `en1.mp3` peaks at
   −2.9907 dBFS and the master reads −3.0015 after the AAC round trip. There is no gain
   staging anywhere in the pipeline, so the ceiling is whatever ElevenLabs returns. **If a
   future TTS clip comes back near 0 dBFS the −1 dBTP gate will actually bite.**
   fin-render's recommendation, recorded here as owed: **promote a `loudnorm I=-14:TP=-1`
   pre-publish pass from optional to standard** — it fixes the headroom risk and the
   8 LU loudness deficit in one pass.

## Thumbnails (3 variants per cut, creator picks at upload)

`studio/videos/credit-history-thumbs/thumbnail-{hi,en}-v{1,2,3}.png` — one project per
slug (hi §v1–v3, en §env1–env3). Backgrounds are each cut's **own** scene photos under
the design grade; six distinct md5s, no cross-video reuse. `npm run check` clean,
29/29 (hi) and 36/36 (en) WCAG AA; legibility assert measured on the downscaled PNGs.

| | hi | en |
|---|---|---|
| **v1 — recommended** | THE ONE MISS — red mega **36 MAHINE** + the 36-cell payment grid (59%) | THE SEVEN-YEAR MARK — red mega **7 YEARS** + the 7-year track (50.9%) |
| v2 | THE PRICE — red mega **₹4.5 LAKH** over the blueprint (58%) | THE PRICE — red mega **$12,400** + two rate rows (42.8%) |
| v3 | THE SCALE — green **700+** over a 300→900 gauge split at the true 66.7% (47%) | THE SCALE — green **670+** over a 300→850 bar split at the true 67.3% (45.3%) |

**`chosen:` is unfilled in both packs as of close-out.**

**The design space is close to exhausted, and this is a channel-level finding.**
Thirteen of @moneymavens101's fifteen prior variants resolve to one big red number over
a graded photo. v1-en is the **second red-mega-"N YEARS" in two uploads** (good-debt
shipped "18 YEARS"); v2-en is the **fourth consecutive red-mega-$ lead**. Only v3
breaks the pattern on either channel — and **v3-hi and v3-en are near-twins**, so
picking both ships one composition in two languages on the same day (defensible for a
cross-linked pair, but it should be a decision, not an accident). The next real variance
has to come from the design system or the video's own visuals, not from re-arranging the
same three parts. *(the composition analysis is measurable; that any of it costs CTR is
**unvalidated — no analytics yet**)*

## The thumbnail feedback loop is dead — and that is now provable

Read back this run (procedure step 3), directly from the files:

| Pack | `chosen:` | Upload |
|---|---|---|
| pay-yourself-first hi / en | **blank** | **UPLOADED 2026-07-28** — youtu.be/PKU0_TeJ9_c · youtu.be/mlvp4xZTROg |
| good-debt-vs-bad-debt hi / en | **blank** | not uploaded |
| credit-history hi / en | **blank** | not uploaded |

**The field survived a real upload unfilled.** So it is not "the upload hasn't happened
yet", and a seventh request in a seventh pack will not work either. Two things follow:

1. **The pick is recoverable without anyone filling anything: the chosen thumbnail is
   the public thumbnail.** Compare the live video's thumbnail against the three (four,
   for pay-yourself-first-en) PNGs on disk and record the match. **Both
   pay-yourself-first URLs are live now, so two picks are recoverable today.** This
   stage could not run it — fin-archive has no network access — so it is **owed**, to
   whichever stage or human can open the URLs. Record the result in
   [[../pay-yourself-first/index]], not here.
2. **The creator does give feedback — just not in that field.** pay-yourself-first-en
   records a **creator title pick on 2026-07-28** (option 8, "The $5 Trick…", vidIQ 83)
   and a **`thumbnail-en-v4.png` built for it**, which exists on disk. So by upload day
   the `chosen:` field's own option set (v1/v2/v3) could not even express the answer.
   Feedback lands as prose in the section the creator was already editing. Design the
   loop around that, not around an empty field at the top of a long file.

## Run events + learnings worth keeping

### ⛔ Architecture sameness — the headline finding (channel-level, both channels)

This is the **6th consecutive blockframe-9 ~3-minute cut on EACH channel.**
@moneymavens101's own record: 50-30-20 (3:43) → emergency-fund (2:46) → needs-vs-wants
(2:49.6) → pay-yourself-first (2:57.8) → good-debt-vs-bad-debt (2:59) → **credit-history
(2:53.2)** — **five of six inside a 13-second band**. @cashguruguides matches it topic
for topic.

**The sameness is not the finding. The finding is that the control failed three times in
writing.** pay-yourself-first's pack flagged the 4th ("the next upload would be the
5th — vary the architecture"). good-debt's pack **and** its milestone note flagged the
5th, called a 6th "an indefensible template run", and instructed **"escalate before the
next en cut is scripted."** The next cut was then researched, scripted, storyboarded,
voiced, built, rendered and packaged on the same architecture. Three identical warnings,
zero behaviour change.

**Diagnosis (fin-package's, and it is correct): the control is in the wrong place, not
unheard.** Architecture is chosen by `tier` in `vault/videos/<slug>/run.json`, resolved
through `tools/format.json` → `tiers.<tier>.architecture`, **before fin-script runs.**
The pack that carries the warning is read **at upload, after the artifact exists.** A
gate that fires after the artifact is finished cannot change the artifact.

**Owed action (orchestrator's — archive may not write `tools/` or `.claude/`): make the
next run's `tier` a deliberate decision recorded in `run.json`, and treat "6 consecutive
shorts on blockframe-9" as the reason it must not be `short` again.** Break options,
pick one, don't stack: medium tier with per-line chapters (`tiers.medium`, reference
`studio/videos/firaun-ka-anjaam/build.py`); a 60–90 s single-argument short, well
outside the 2:46–2:59 band; or the same short tier with the roadmap and recap bookends
dropped, which changes the 9-beat order itself.

**Cross-channel, first time both records were in one place:** the two channels have
shipped the **same six topics, in the same order, in the same architecture, in the same
runtime band.** Per-channel review sees six each; together it is a twelve-cut template
run from one pipeline. One architecture change fixes both — and **the second channel is
buying no diversification against this risk.**

Publishing this pair remains defensible (sameness is actionable forward, not
retroactively). Scripting a 7th on the same architecture is not. *(that sameness costs
views on YouTube specifically is **unvalidated — no analytics yet**; the Gate 2 policy
position is enforceable regardless)*

**Recording gap that makes the count ambiguous and is cheap to close:** only
pay-yourself-first has a confirmed upload URL in the vault, so the sequences above are
the **production** order. Either reading crosses the line, but **record upload dates and
URLs in the milestone notes** and the ambiguity disappears.

### `library.db` has no finance lane (channel-wide, 2nd rescue for this reason)

1,124 rows, **zero** matching credit / score / loan / debt / bureau in the title — the
three substring hits are false positives (`fico` inside a Portuguese "Ficou", `apr`
inside two WW2 documentaries' "April"). The library holds AI-tools and
history-documentary sweeps only. fin-research will be rescued on **every** finance topic
until a finance scrape exists, and every competitor scoreboard in every pack is
autocomplete-only. **A finance-lane scrape is owed channel-wide, not per video.**

### Pixabay craft — cost 4 rounds on hi and 6 on en, so write it down

- **Short one-noun queries beat descriptive phrases.** The storyboard's 6-to-9-word
  queries ("torn paper calendar page on a dark surface") fall back to whatever matches a
  single weak token and return generic stock — round 1 landed 5 of 17. Shortening to the
  strong noun (`blueprint`, `accounting ledger`, `calendar`, `pocket watch`, `document`)
  landed 9 of 12 retries **and produced the best images in the set**. Storyboard stage
  should write manifest queries as **1–3 nouns**; the pretty phrasing belongs in the
  intent column, not the search string.
- **`#N` fixes ranking; a synonym fixes the noun.** `#N` on a bad long query only returns
  more of the same wrong thing, because the query is what's broken, not the ranking.
- **Generic office nouns are pre-burned library-wide** — `calendar`, `wallet`,
  `paperwork`, `contract`, `desk lamp` all collide.
- **Same-slug adjacency is NOT where duplicates live.** Seven hash collisions this run,
  none from the direction the storyboard predicted: pay-yourself-first ×2,
  emergency-fund ×2, 50-30-20-rule-en ×1. Dedupe must stay a **whole-grid md5 ledger
  across both channels**, never a per-slug check.
- **Any photo with an identifiable car carries a manufacturer badge.** Ask for the key,
  the road or the paperwork — never "a row of cars". The one clean `car key#2` is a
  single object on an empty field.
- Authority held: a **cut-in may be dropped rather than faked; a background may not**
  (creator rule 2026-07-28 — every frame has an image). hi dropped 3, en dropped 6, all
  9 backgrounds shipped in both.

### A wrong subject cannot be fixed by framing

fin-build tried to **crop a car fob out of frame** rather than delete the element under
s7's "SAME HOUSE." type. The render frame gate failed it, and it cost a full extra
build + render cycle. **If an image's subject is wrong for the line it sits under,
delete the element.** Reframing hides the object and keeps the contradiction. (Second
lesson from the same fix: removing the car photo *lowered* `#s7q`'s contrast ratio ~0.15,
because the crushed left two-thirds of that photo had been doing contrast work
accidentally — the replacement blueprint is the brighter plate. Verified by two
independent measurements; still passes at 2.37–2.88 with the `.huge` text-shadow, and a
darker s7 plate is a polish item for fin-assets, not a defect.)

### A green checker is not evidence the frames are good

The **max-density snapshot pass caught 11 real defects across the two cuts** (6 hi,
5 en) that `npm run check` scored **green**. `npm run check` validates the DOM and the
contrast sampler; it does not look at the rendered frame at its busiest moment. **Keep
the snapshot pass at maximum density, at full resolution, never at thumbnail size.**

### A log correction that must not be lost

`fin-build-en`'s log claims `#s5ctr` covers the s5 QUALITY seal. **It does not** — they
sit ~420 px apart and never overlap. What makes the seal illegible is **the grade and the
bottom-edge crop**. The mitigation on file should read *"illegible under the grade at the
bottom edge"*. Left uncorrected, a future cut would move the counter believing the seal
was handled, and the seal would still be illegible. (Confirmed independently in
[[logs/fin-render-en-2|fin-render-en-2]] §7.)

### Pipeline convention bug — one rename fixes it for every future run

facts-staging names its claims **`$-2` / `₹-5`**, using **currency glyphs as market
prefixes**. `pipeline_check`'s currency-purity scan is a **whole-file substring match**,
so the claim IDs themselves trip it — the hi script fails for containing a `$` that is
only a label. **Cost fin-script-hi a retry.** Renaming the convention to **`US-2` /
`IN-5`** in fin-facts fixes it permanently for both cuts. (Same family as the
already-recorded rule: *state the currency rule in words, never type the forbidden
glyph.*)

> Everything in this section except where explicitly marked is a **pipeline/engineering
> fact** — reproducible, measurable, not analytics-dependent. Nothing here has been
> promoted to [[../../knowledge/best-practices]]: that file takes evidence only after
> ≥28 days of real analytics, and zero-view "evidence" beside five dated confirmations
> saying the opposite would poison the one file that compounds.

## Current state + what is owed

**State: RENDERED + PACKAGED + FACTS PROMOTED + COMMITTED 2026-07-29. Not uploaded.**
Renders, audio, frames and assets are **KEPT** — post-delivery cleanup runs only after
upload, on the creator's word ([[../../CLAUDE]]). Nothing was deleted this stage.

Owed:

- **proof-listen (hi, en)**
- **thumbnail pick** — fill `chosen:` in [[youtube-metadata-hi]] + [[youtube-metadata-en]]
  at upload; and separately, **recover the two pay-yourself-first picks off the live
  videos** (youtu.be/PKU0_TeJ9_c · youtu.be/mlvp4xZTROg) by comparing against the PNGs
  on disk, since asking a seventh time demonstrably does not work
- **upload** (both cuts; cross-link each other in end screen / pinned comment) — and
  **record the URL + date here**, which is what makes the sameness count unambiguous
- **analytics after 28 days** — only then may anything here touch
  [[../../knowledge/best-practices]]
- **architecture decision before the next run is created** — `tier` in `run.json`, not a
  seventh warning in a seventh pack (orchestrator's; see the sameness section)
- **finance-lane scrape into `library.db`** — channel-wide, blocks fin-research and every
  competitor scoreboard
- **`loudnorm I=-14:TP=-1` pre-publish pass promoted to standard** — headroom safety
  (en is at −3.00 dBTP from source) plus the 7–8 LU loudness deficit
- **rename the facts-staging claim-ID convention** `$-N`/`₹-N` → `US-N`/`IN-N` in
  fin-facts (one-line fix, saves a retry every run)
- **storyboard queries as 1–3 nouns**, and fix the `#s5ctr` mitigation text in the en
  build notes

Related: [[script-hi]] · [[script-en]] · [[storyboard-hi]] · [[storyboard-en]] ·
[[audit-hi]] · [[audit-en]] · [[facts-staging]] · [[youtube-metadata-hi]] ·
[[youtube-metadata-en]] · [[../../knowledge/design-finance-blockframe]] ·
[[../../knowledge/money-facts-2026]] · [[../good-debt-vs-bad-debt/index]] ·
[[../pay-yourself-first/index]]
