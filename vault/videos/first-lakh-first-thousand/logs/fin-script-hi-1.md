# fin-script — first-lakh-first-thousand · cut hi · attempt 1

**Date:** 2026-07-31 · **Status:** ok
**Wrote:** `vault/videos/first-lakh-first-thousand/script-hi.md`

## Inputs read

- `vault/CLAUDE.md` (first, per contract)
- `tools/format.json` — cuts.hi (12.5 chars/s, Harsh `HTUuC7OeeEt6OL5fViVe`), tiers.medium
  (510s, per-line-chapters, reference `studio/videos/firaun-ka-anjaam/build.py`), scene
  bounds (6.5 target / 9.0 max, `_scene_seconds_note`), layout caps, colors
- `vault/videos/first-lakh-first-thousand/facts-staging.md` (attempt 1) — every number
- `vault/videos/first-lakh-first-thousand/run.json` — creator brief, tier, architecture
- `vault/knowledge/video-studies/first-lakh-first-thousand.md` — retention shape
- `vault/skills/long_form_scripting.md`
- `vault/knowledge/niches/india-finance-market.md` (hi cut). **Did NOT read**
  `haryanvi-hindi-script-style.md` — Standard Hindi per creator decision 2026-07-28.
- `vault/knowledge/finance-audit-2026-07-29/11-swiss-vignelli.md` — run.json picked
  `swiss-band`, so Direction 1's spec governs the on-screen blocks
- `studio/videos/firaun-ka-anjaam/build.py` + `vault/videos/video-hist-02-firaun/
  script-v2-nastaliq-lines.md` — the per-line line/cue format and the gap model
- `vault/videos/credit-history/script-hi.md` — house style for the trace + handoff blocks

## Output

**86 VO lines · 9 chapters · ~5,958 chars · ~476.6s VO + ~21.8s gaps ≈ 498s (8:18)**
vs the 510s target = **−2.3%**. Char budget 510 × 12.5 = 6,375; draft is −6.5%.
Average scene 5.8s (target 6.5, max 9.0). Longest line 103 chars / 8.2s; shortest 23
chars / 1.8s (above `tts.min_clip_seconds` 1.0).

## Decisions worth recording

1. **86 lines, not the 78 in `format.json tiers.medium.lines`.** That 78 is 510 ÷ 6.5 and
   `scene._scene_seconds_note` says scene count is emergent, never a constant. A finance
   argument built on punch lines runs shorter per line than firaun's narrative lines.
   86 hi + ~86 en = 172 ElevenLabs calls of the run's 200 — 28 left for retries. Going
   much above 90 lines per cut would put the pair against the ceiling.
2. **None of the 9-segment constants applied.** The `swiss-band` registry entry declares
   `tier: short, lines: 9`; run.json already flags that as a SHORT-tier constant. Written
   as per-line chapters throughout.
3. **The hook opens on the number, in the first sentence** (study conclusion 1) — "पाँच
   हज़ार रुपये महीना। पहला एक लाख — बीस महीने।" No title card, no greeting, no roadmap
   before a figure. Three loops planted at 1.7–1.9 and closed on schedule (5.1, 4.4, 6.1).
4. **The ~70% beat is a re-frame, not a fact** (study conclusion 4 + TOP's move 3):
   chapter 7's rooftop tank and bucket, at 5:30–6:19 of 8:18. The punch line 7.7 lands at
   ≈70%. Nothing in that chapter is new information, and 7.8 states where the analogy
   breaks (§10 of the scripting skill).
5. **The one visible sum** (study conclusion 6, the LOW video's fatal omission) is chapter
   3: the second lakh and the tenth lakh at the same ₹5,000. 20 → 7.
6. **Chapters ship as YouTube chapters** (study conclusion 7 — MID's best packaging).

## Fact discipline

- Every number traces to a `facts-staging.md` line; the trace table in the script names
  the row and the tag for each.
- **The flagged error is corrected, not avoided.** facts-staging §1.3 warns that calling
  ₹1 lakh the crossover is "the one factual error this script is most likely to make".
  Chapter 5 states the crossover is ≈₹8.5 lakh at 7.1% / ≈₹4.8 lakh at ~12% — roughly
  ₹5 lakh — and 5.9 uses the staging note's own blessed wording ("the first lakh is where
  the *habit* takes over"). Restated at 7.7 and 9.7.
- **No months figure is spoken as a statistic** (§4). Each carries its condition in the
  same sentence; every math frame carries an `ILLUSTRATIVE · ₹5,000/mo · <rate> · monthly
  compounding` foot.
- **No equity decimal** anywhere, spoken or on screen — both NSE PDFs 403'd, so the row is
  SOFT and only the shape ("क़रीब बारह परसेंट" / `~12%/yr`) is used. The only exact rate
  spoken is the HARD 7.1% (PPF / 3-yr post-office TD).
- **₹5,000 is never presented as a national average** — 6.4/6.5 say out loud that it is
  the 20% leg of the locked 65/15/20 split, and the frame labels it a channel convention.
  6.7/6.8 concede honestly that a smaller amount takes longer.
- **Currency firewall holds:** grep for the dollar glyph across the whole file returns
  zero. The Munger quote is absent from this cut entirely — it is SOFT *and* denominated
  in the other currency.
- **Digits spelled out in every VO line;** grep for Latin digits inside the `>` VO lines
  returns only the prose callout block, no VO line.

## Persona / policy

No host persona, no "मैं", no first-person expertise, no fund/AMC/bank/app named. PPF,
the post-office time deposit, the small-savings quarterly notification and the ₹500/₹250
monthly minimum appear as **price evidence only**; 6.9's on-screen foot says so in words.
The three-rung ordering in chapter 8 (safety → stability → growth) is sequencing, framed
as "the order practitioners describe", with no instrument named.

## Handed to the next stage

- 86-entry `hindi-lines.json`, sliced not retyped, byte-reconstruction gated.
- **One open build defect flagged in the handoff:** the 5.2 + 5.3 hold pair totals ~9.2s
  on a single photograph and breaches `scene.max_scene_seconds` 9.0. Fix = give 5.3 a
  tighter second crop of the same source. The 1.1+1.2 (8.0s) and 1.5+1.6 (8.6s) pairs pass.
- Per-scene aperture assignment (band / column L-R / reversed / mosaic) is in the timing
  table; the reversed-field scenes need measured luminance, not assumed.

## Owed / not done here

- The `-en` cut is a separate US rewrite, not a translation of this file. It must not
  reuse this cut's aperture cycle offset (this one starts on R).
- The study note's owed scrape (`fQyN80dLDpQ`, the 48×-subs faceless winner on this exact
  topic) is still 429'd, so the retention shape here rests on two podcasts plus the LOW
  autopsy, not on a faceless small-channel winner.
