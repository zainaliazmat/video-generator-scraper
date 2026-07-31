---
summary: fin-script log for first-lakh-first-thousand, cut en, attempt 1. Wrote script-en.md — 92 VO lines, ~7,648 chars, ~498s (8:18) vs the 510s MEDIUM target. US rewrite of the Hindi spine, not a translation.
updated: 2026-07-31
source: tools/format.json (rates, tiers, scene bounds) · facts-staging.md §2 · knowledge/video-studies/first-lakh-first-thousand.md · skills/long_form_scripting.md · knowledge/us-english-script-style.md · knowledge/finance-audit-2026-07-29/11-swiss-vignelli.md · script-hi.md + audit-hi.md (structure only)
stage: fin-script, cut en, attempt 1
---

# fin-script — en, attempt 1

**STATUS: ok** · wrote `vault/videos/first-lakh-first-thousand/script-en.md`.

## Constants, read not remembered

| Constant | Value | Home |
|---|---|---|
| chars/second, `en` | **16.1** | `format.json cuts.en.chars_per_second` (measured; the retired 15.0 estimate budgeted every en cut ~7% long) |
| tier | MEDIUM → `per-line-chapters`, target **510s** | `format.json tiers.medium` |
| scene bounds | target 6.5s, **max 9.0s**, min clip 1.0s | `format.json scene`, `tts.min_clip_seconds` |
| architecture | `swiss-band` (creator pick, run.json — overrides the blockframe-9 lock for this run) | `run.json.architecture` |
| voice | Brian `nPczCjzI2devNBz1zQrb`, `eleven_multilingual_v2`, style 0 | `format.json cuts.en` |
| photo-free scenes | **0** | `format.json layout.photo_free_scene_ratio` |

`format.json tiers.medium.lines: 78` was **not** used as a constant —
`scene._scene_seconds_note` states scene count is emergent from the script. Likewise the
`lines: 9` on the `swiss-band` registry entry is a SHORT-tier value and does not apply.

## What shipped

- **92 single-sentence VO lines** across **9 chapters** (10 / 10 / 10 / 11 / 11 / 10 / 8 / 12 / 10).
- **~7,648 chars** against a budget of 510 × 16.1 = **8,211** → **−6.9%**.
- **~475.0s VO + ~23.2s gaps = ~498.2s (8:18)** vs the 510s target → **−2.4%**, matching
  the Hindi cut's −2.3% so the pair ships at the same length.
- Average scene **5.4s**; longest line 127 chars ≈ 7.9s (under `max_scene_seconds` 9.0);
  shortest 22 chars ≈ 1.4s (over `tts.min_clip_seconds` 1.0).
- Per-scene timing budget table included (chars → est. seconds → aperture).

## The `-en` cut as a rewrite, not a translation

The Hindi script was read for **structure only**. Everything below is different content
reaching the same spine:

| Beat | hi | en |
|---|---|---|
| Milestone | ₹1,00,000 | **$10,000** (emotional equivalent per the brief — explicitly *not* a conversion; staging's Currency Firewall) |
| Monthly amount | ₹5,000 (20% of ₹30,000) | **$800** (20% of $4,000) |
| Hook figures | 20 months → 7 | **12.5 months → 6** |
| The thesis gap | 2 months vs 13 | **½ month vs 6½** |
| The rate on screen | PPF / post-office TD 7.1% | **FDIC national savings rate 0.38%** + the "roughly ten times" HYSA ratio |
| "Waiting for rates" | small-savings unchanged 9 quarters | **Fed target range unchanged since 11 Dec 2025** |
| Market shape | ~12%/yr Nifty TRI | **~10%/yr S&P shape** |
| The honesty stat | PLFS ₹18,353–₹24,217 · RBI 7.0% of GNDI | **BLS $1,251/wk · Fed SHED $400 · BEA 2.7% saving rate** |
| Crossover | ~₹5 lakh — five times past the milestone | **~$96,000 ≈ $100,000 — ten times past it**, and Munger's number *is* that point |
| ~70% re-frame | rooftop water tank + bucket | **a fire pit and a coal bed** — deliberately a different physical base |
| Action | auto-transfer on salary day | **automatic transfer dated the day after payday** |

**The strongest US beat is not the return, it is the saving rate** (staging §2.3): at the
BEA's real 2.7%, the same $4,000 take-home saves $108/mo and the first $10,000 takes almost
eight years — versus 12.5 months at the worked example. Both inputs are HARD/CONVENTION.
That comparison anchors chapter 4, the mid-video drop zone.

**Munger is colour, not evidence.** Chapter 5 reaches ~$96,000 by arithmetic *first*, then
lands the quote at 5.8 in staging's sanctioned paraphrase — no year, no venue, no profanity,
nothing on screen but "as widely reported". If the SOFT quote were struck tomorrow the
chapter still stands.

## Rules actively enforced

- **Zero rupee glyphs, zero "lakh"/"rupee", zero cross-market arithmetic.** No line
  implies $10,000 and ₹1,00,000 are the same thing.
- **Digits spelled out in every VO line.** No bare Latin digit, no `$` glyph inside a VO
  string; on-screen numerals carry the exact figures in US comma grouping.
- **No APY for any product, anywhere.** ~4.15% (SOFT, "never on screen") is absent, and its
  derived crossover (≈$231,000) was dropped with it because it cannot be footed without
  printing the rate. Only the FDIC's regulator-published national rate appears.
- **No decimal on the market return** — "about ten percent a year" spoken, `~10%/yr` shown.
- **No months figure spoken as a statistic.** Every one carries its condition in the same
  sentence, every math frame carries an `ILLUSTRATIVE` foot, and **2.8 says it out loud**
  in the VO ("model numbers, not promises").
- **Persona.** No "I", no host, no credentials, no fund/stock/product pick. 2.4 uses
  "now suppose", not the imperative fin-audit killed on the Hindi cut at the same beat.
  8.8 and 8.11 carry "price evidence, not a recommendation" / "a category, not a product"
  on screen.
- **Green ≠ returns.** The `--fund` definition is written as "the mechanism that works
  without you once it exists", the correction fin-audit made to the Hindi cut — 5.10 is
  green and its entire job is to deny that returns take over at the first milestone.

## Study conclusions applied

1. First sentence carries the number (1.1), second figure on screen by ~11s. No greeting,
   no title card — the LOW pick's 15-second static title card is the named cause of death.
2. Three loops planted at 1.7–1.9, answered on schedule at 5.1 (Q1), 1.8→8.8/8.9 (Q2) and
   6.1 (Q3).
3. The visible sum is chapter 3 — the arithmetic the LOW pick refused to perform.
4. ~70% beat is a **re-frame with a physical image**, not a new fact (ch.7, punch at ~73%).
5. Chapters shipped as YouTube chapters with start times.
6. MID's three-rung ladder (emergency fund → stability → growth) is 8.10–8.11, product-free.

## Flagged for the next stages

1. ⚠ **ElevenLabs budget is the tightest constraint in the run.** 86 (hi) + 92 (en) =
   **178 of 200**. Twenty-two calls of retry headroom across both cuts. `fin-voice` must
   regenerate individual failed clips, never a whole chapter.
2. ⚠ **Rounding convention.** Same trap fin-audit pinned on the Hindi cut: staging §2.3
   rounds to the **nearest** month. The VO is locked to 12.5 / 12 · 12.5 / 11 · 12.5 / 6.
   A `ceil` build prints integers the voice contradicts and the fix costs a TTS re-cut.
   Extra en-specific hazard: **12.5 is exact** ($10,000 ÷ $800) and must render `12.5`,
   never `13`.
3. **Extraction hazard, same as the Hindi cut.** The ⚠ admonition near the top of
   `script-en.md` is a `>` blockquote. Key extraction off the `**N.N**` headers, not
   `grep '^>'`, or the warning text goes to ElevenLabs and burns calls.
4. **Aperture cycles must not sync between cuts.** hi opens on `R`; en opens on `B` with
   its first `R` at scene five. Written into Build handoff §9.
5. **US photo sweep is a build gate, not a nicety.** The first `-en` cut shipped a
   motorcycle in a workshop, a Swiss 5-franc coin and euro coins. 92 images is 92 chances.
6. **Not raised as a defect, but the audit should look at it:** average scene 5.4s is below
   `scene.target_scene_seconds` 6.5. Deliberate — English carries more per second, and the
   study's failure case is dead frames, not brisk ones. Every scene is inside the hard 9.0s
   bound, which is the constraint `check_build` actually enforces.

## Not done here

- `vault/knowledge/best-practices.md` still owes the two failure-mode lines the study note
  flagged as un-appended. Out of scope for this stage; still owed.
- The `Story of Success` transcript (`fQyN80dLDpQ`, the 48×-subs breakout on this exact
  topic) is still owed — every hook/beat finding used here rests on two podcasts, one of
  which underperforms its own subscriber base.
