---
summary: Milestone note for «Good Debt vs Bad Debt — the minimum-payment trap» pair (Hindi/₹ 3:15 · US/$ 2:59) — both cuts rendered, MASTER QA PASS, committed 2026-07-28/29; publish packs written. NOT uploaded. Owed — proof-listen (hi, en) · thumbnail pick · upload · lane scrape · analytics after 28 days. ⛔ HARD flag: 5th consecutive blockframe-9 on BOTH channels — the sameness enforcement line is crossed; the NEXT finance cut MUST change architecture.
updated: 2026-07-29
source: run.json + the fin-render / fin-build / fin-assets / fin-package logs in logs/ (the /finance-video pipeline)
---

# Good Debt vs Bad Debt — milestone note

Run 2026-07-28→29, `/finance-video` pipeline. Topic: the credit-card
minimum-payment trap, framed as good debt vs bad debt. fin-research was **rescued**
(missing study note, library empty for this lane); fin-script-hi took **attempt 2**
(currency-check trap, below); both fin-render cuts landed on **attempt 3** (frame-gate
re-source + orchestrator-owned encode). Budget: **18 of 30 ElevenLabs calls** (9 VO
clips per cut); **144 Pixabay calls** (hi 48 + 30 frame-gate re-source, en 66).

## The two cuts

| | Hindi / India (@cashguruguides) | US / English (@moneymavens101) |
|---|---|---|
| Master | `studio/videos/good-debt-vs-bad-debt-hi/renders/FINAL-1080p-hi.mp4` | `studio/videos/good-debt-vs-bad-debt-en/renders/FINAL-1080p-en.mp4` |
| Runtime | **195.20 s (3:15)** · 11.75 Mb/s video (~11.93 overall) | **178.60 s (2:59)** · 12.2 Mb/s video |
| Voice | ElevenLabs **Harsh** — **Devanagari Standard Hindi** (NOT Nastaliq) | ElevenLabs **Brian** |
| Script | [[script-hi]] (9 lines h1–h9) | [[script-en]] (9 lines en1–en9, US rewrite not a translation) |
| Title (recommended) | "Credit Card Minimum Payment: Ek Jaal — ₹50,000 par ₹88,614 Byaj" | "The Credit Card Minimum-Payment Trap: $6,000 Costs You $9,506" |
| Publish pack | [[youtube-metadata-hi]] | [[youtube-metadata-en]] |

Structure of both cuts: **blockframe-9** (hook → roadmap → concept → good-vs-bad →
how-the-minimum-works → action → math-counter → do-today → recap).

## Hero numbers (with sources)

- **hi: ₹50,000 card @ ~40% APR, 5% minimum only → 208 months (17+ yrs) + ₹88,614
  interest** — more than the principal. Sources: Minimum Amount Due ≈ 5% of balance,
  ₹100 floor, interest covered first / no negative amortization = RBI norms + issuer
  MITC 2026; ~40% APR = illustrative India retail range (40–45%), not any single bank =
  Federal Bank / ICICI MITC 2026; the 208 / ₹88,614 pair = ₹100-floor amortization
  model computed (B₀ = ₹50,000). On screen, month-1 split: ₹2,583 min / ₹1,667 interest
  / ₹916 off principal.
- **en: $6,000 card @ ~22% APR, minimum (1% + interest) only → 215 months (~18 yrs) +
  $9,506 interest** — more than borrowed. Sources: min ≈ 1% of balance + that month's
  interest, ~$35 floor, interest first = issuer cardmember agreements (Chase, Capital
  One) + CFPB Regulation Z 2026; ~22% APR = illustrative US range (20–24%) = Fed G.19 /
  WalletHub 2026; 215 / $9,506 = $35-floor model (B₀ = $6,000). On screen, month-1
  split: $170 / $110 / $60; 12-mo balance $5,318.
  - **⚠ Numeral note:** the en interest is **$9,506**, NOT the $9,496 that still appears
    in [[script-en]] / [[storyboard-en]] (pre-build hand estimate). The **build
    calculator regenerated it** — render, thumbnail and description all say $9,506. Do
    not "correct" it back.
- Both markets' facts staged in [[facts-staging]] — promotion to
  `knowledge/money-facts-2026` is the **orchestrator's** step, not archive's.

## QA (from the fin-render logs — both MASTER QA PASS)

| | hi (attempt 3) | en (attempt 3) |
|---|---|---|
| Runtime vs timing.json | 195.20 s, **+0.03 s** (0.9 frame) | 178.60 s, **+0.018 s** (0.54 frame) |
| VO placement drift | max **0.045 s** (s8); 7/9 flat +0.022 s; zero accumulation | max **+0.093 s** raw (en7 — its own 0.071 s head-lead); encode-isolated +0.022 s; zero accumulation |
| True peak | **−3.23 dBTP** (< −1) | **−4.74 dBTP** |
| Loudness | −22.0 LUFS (broadcast-safe; ~8 LU under YT −14) | −21.0 LUFS |
| VO content | 9/9; hero round-anchors spoken; **208 / ₹88,614 on-screen ONLY (absent from VO)** | 9/9; **215 mo / $9,506 on-screen ONLY (absent from VO)** |
| Black segments | 0 | 0 |

Optional pre-publish loudness lift toward −14 LUFS is available on both (peak headroom
allows it) — orchestrator's call, not a gate fail.

## Thumbnails (3 variants per cut, creator picks at upload)

`studio/videos/good-debt-vs-bad-debt-thumbs/thumbnail-{hi,en}-v{1,2,3}.png` (source:
`…-thumbs/index.html` — hi §v1/v2/v3, en §env1/env2/env3, one shared project).
- **v1 — recommended** THE PUNCH: centred red mega **₹88,614 / $9,506** over the
  calculator texture. Centred → breaks the channel's left-aligned streak.
- v2 THE TIME TRAP: 208 MAHINE / 17 SAAL · 215 MONTHS / 18 YEARS — closest to the
  last-3 red/left/photo family (the safe continuity pick).
- v3 THE SPLIT: the month-1 anatomy (₹1,667 / $110).

Red is the trap throughout; green is deliberately absent (the thumbnail sells the
trap, not the escape). Backgrounds are the video's OWN re-graded scene photos — no
new/cross-video images, no AI-collage, no shocked-face. `chosen:` line sits in each
publish pack — **unfilled as of close-out**.

## Run events + learnings worth keeping

**⛔ CHANNEL SAMENESS — HARD flag, enforcement line crossed (both channels).** This is
the **5th consecutive blockframe-9 ~3-min cut on EACH channel**: 50-30-20 →
emergency-fund → needs-vs-wants → pay-yourself-first → **this**. pay-yourself-first
explicitly warned "the next upload would be the 5th" — this is that upload. Per Gate 2,
mass-production sameness is the one category judged channel-level. This pair still
publishes fine (actionable forward, not retroactively), **but the next finance cut MUST
change architecture** — medium-tier per-line-chapters, a different layout, or a
different length band. A 6th blockframe-9 is an indefensible template run. **Escalate to
creator/orchestrator BEFORE the next cut is scripted.** *(the sameness policy is
enforceable now; whether it actually costs views = unvalidated — no analytics yet)*

> **WHAT ACTUALLY HAPPENED (added 2026-07-29 by fin-archive):** it wasn't. `credit-history`
> was then researched, scripted, voiced, built, rendered and packaged on the same
> architecture — **the 6th consecutive blockframe-9 on both channels.** This warning is the
> third of three that changed nothing, which is itself the finding: the control is in the
> wrong place. `tier` is chosen in `run.json` *before* fin-script; a milestone note and a
> publish pack are read *after* the artifact exists. See [[../credit-history/index]].

**HERO-MATH DOCTRINE (worked — reuse for any model-dependent number).** The
minimum-payment payoff is floor/model-dependent, so the VO speaks ONLY floor-independent
anchors + round ranges ("17+ years / nearly the whole principal in interest"; "the
better part of two decades / more than you borrowed") while the exact integer (208 /
₹88,614; 215 / $9,506) is computed in build code and shown **on screen only, never
spoken**. Verified 3 ways: orchestrator Python, fin-facts closed-form, build node. QA
explicitly confirms the false-precise integers are ABSENT from narration.

**FONT GLYPHS (recurring build risk — fix at source).** The self-hosted `FinanceSans`
subset has **no `~` (U+007E)** and **no `>` (U+003E)** — visible use falls back to a
non-deterministic system font. Build must render them as CSS (the `.gt` chevron, same
em-border technique as `.arr`/`.tri`) or avoid the glyph (write "around 22%" not "~22%";
"18 YRS" not "~18 YRS"). Cost the en build a fix pass. Fix the subset — or lint for these
two glyphs — at source so every future build stops re-hitting it.

**CURRENCY-PURITY FOOTNOTE TRAP (cost the hi script a retry).** The script currency check
is a blunt whole-file substring match, so an agent's OWN "no $" / "no ₹" compliance note —
if written with the forbidden glyph — fails its own check. Standing rule for every finance
agent: **state the currency rule in words, never type the forbidden glyph.** Cost
fin-script-hi attempt 2.

**ORTHOGRAPHY — hi finance = Devanagari, NOT Nastaliq.** The hi finance cut is
**Devanagari Standard Hindi** (voice Harsh). A launch-arg said "Nastaliq" and was
correctly rejected — Nastaliq belongs to a different (Urdu) channel that does not exist
in `tools/format.json`. Do not route finance-hi through the Nastaliq lane. (The
vault's Nastaliq rule governs the *history/Urdu* work, not finance-hi.)

**ASSET FRAME-GATE (worked — front-load next time).** Full-frame render QA (gate two)
caught backgrounds that thumbnail-eyeballing missed: an antique coin depicting a **Hindu
deity** (revered-figure violation), plus foreign-language / cross-market b-roll (German
legal text, Polish metallurgy book, a US road in the ₹ cut). The **hi cut needed a full
5-slot re-source** (fin-assets attempt 2, [[logs/fin-assets-hi-2|fin-assets-hi-2]]);
front-loading those lessons let the en cut pass the frame gate first time. **Always
frame-gate at full res, never thumbnail size.** The **India-finance Pixabay pool is
small + heavily consumed** — poison map in that log: one demonetised ₹500 pile is the
immovable #1 for every rupee query (escape only via `#N`); ~3 clean rupee images exist
channel-wide; homonym traps recur ("bill"→a bird, "coins"→a €1 coin). Reach first for
`#N`-past-₹500, magnifier-over-ledger, calculator-keypad macro, a seedling closer, and
denomination-free coin stacks.

> The frame-gate, glyph, currency-check, orthography and hero-math items are
> pipeline/engineering facts — reproducible, not analytics-dependent — so they are stated
> as facts. Anything about **audience response** below is marked unvalidated.

**Thumbnail composition observation:** v1 (a centred red mega-number over the video's own
re-graded scene photo) is a fresh composition vs the channel's red/left-text-over-money-photo
streak — a genuine v1↔v2 A/B if the creator wants one. *(unvalidated — no analytics yet)*

## Current state + what is owed

**State: RENDERED + PACKAGED + COMMITTED, not uploaded.** Renders and assets are KEPT —
post-delivery cleanup (deleting renders / audio / frames) runs ONLY after upload, on the
creator's word ([[../../CLAUDE]]). Nothing was deleted this stage.

Owed:
- **proof-listen (hi, en)**
- **thumbnail pick** — fill `chosen:` in [[youtube-metadata-hi]] + [[youtube-metadata-en]]
  at upload (fin-archive reads it back next run — this is how the thumbnail loop learns;
  it is still unfilled for pay-yourself-first, so the loop has no recorded pick yet)
- **upload** (both cuts; cross-link each other in end screen / pinned comment)
- **lane scrape** — `library.db` has **NO comparable videos** for the debt /
  credit-card-explainer lane (≥100 views, ≥240 s); from run.json `owed`. Orchestrator's step.
- **analytics after 28 days** — only then may any learning here touch
  [[../../knowledge/best-practices]].

Flagged for the pipeline (engineering, not a deliverable): the `FinanceSans`
missing-glyph subset and the substring-match currency check both **recur** — fix at
source (font subset / lint; word-not-glyph agent rule) so future runs stop paying for them.

Related: [[script-hi]] · [[script-en]] · [[storyboard-hi]] · [[storyboard-en]] ·
[[youtube-metadata-hi]] · [[youtube-metadata-en]] · [[audit-hi]] · [[audit-en]] ·
[[../../knowledge/design-finance-blockframe]] · [[../pay-yourself-first/index]]
