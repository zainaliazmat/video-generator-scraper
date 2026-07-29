---
summary: fin-package credit-history · en · attempt 1 · STATUS ok. Three en thumbnail variants added to the existing studio/videos/credit-history-thumbs project (check clean, 36/36 AA, legibility 50.9/42.8/45.3%), publish pack written with real chapter times from timing.json and 15 autocomplete-verified US tags from a fresh 2026-07-29 gl=us/hl=en pull (32 seeds, 4 empties recorded). ⛔ Hard finding — 6th consecutive blockframe-9 on @moneymavens101 on its OWN record; the channel's own control failed twice in writing, so the escalation is to move the control to run.json, not to write the warning a fourth time.
updated: 2026-07-29
source: own tools/autocomplete.py pulls (2026-07-29, gl=us hl=en, 32 seeds incl. 4 empties) · own read-only sqlite count on library.db (0 real lane rows / 1,124 total; 3 substring false positives) · studio/videos/credit-history-en/assets/voice/timing.json · studio/videos/credit-history-en/index.html (foots #s3f/#s4f/#s5f/#s7f/#s8f, countUp targets) · vault/videos/{good-debt-vs-bad-debt,pay-yourself-first,needs-vs-wants,emergency-fund,50-30-20-rule}/ en packs + milestone notes
---

# fin-package — credit-history · en · attempt 1

**Result: `STATUS: ok`.**

## Artifacts

- `vault/videos/credit-history/youtube-metadata-en.md`
- `studio/videos/credit-history-thumbs/thumbnail-en-v1.png` · `-v2.png` · `-v3.png` (1280×720)
- `studio/videos/credit-history-thumbs/index.html` (§env1/§env2/§env3 added; hi §v1–v3 untouched)
- `studio/videos/credit-history-thumbs/assets/img/en3.jpg` · `en5.jpg` · `en7.jpg` (staged from the en render)

## Thumbnails

Extended the existing per-slug project rather than making a second one (contract: one
HyperFrames project per slug). Root duration 6 → 12s, three new sections at
`data-start` 6/8/10, exported with `npx hyperframes@0.7.66 snapshot --at 7,9,11 --no-end`.
Backgrounds are the **en** video's own scene photos — all six image md5s in the project
are distinct, so the en thumbs share nothing with the hi thumbs.

| | Idea | Focal / accent | Numerals |
|---|---|---|---|
| **v1 (rec.)** | `ONE MISSED PAYMENT` → red mega **7 YEARS** + the 7-year track frozen with the mark landed on year 1 | red / amber | 7 · 1–7 (en5) |
| v2 | `SAME CAR, LOWER SCORE` → `EXTRA COST` → red mega **$12,400**, over two rate rows (~6% → $418/mo · ~19% → $590/mo) | red / green | 12,400 · 6 · 418 · 19 · 590 · 25,000 · 72 (en7) |
| v3 | `WHAT'S A GOOD SCORE?` → `CREDIT SCORE` → green mega **670+** over a 300→850 bar split at 67.3% | green / red | 670 · 300 · 850 (en3) |

- `npm run check`: **0 lint errors · 0 runtime · 0 layout issues (9 samples) · 0 motion ·
  36/36 WCAG AA.** One cosmetic `timeline_track_too_dense` warning — the known cost of
  co-hosting both cuts in one file, same as the good-debt thumbs project.
- Legibility assert run on the **actual PNGs downscaled to 320×180** (not estimated):
  `7 YEARS` **50.9%** · `$12,400` **42.8%** · `670+` **45.3%** — all clear 40%.
- **Numeral discipline holds.** Every numeral was checked against the built render, not the
  script: `12400` and `1→7` are `countUp` targets in `index.html`, `$418`/`$590`/`~6%`/`~19%`/
  `$25,000`/`72 months`/`300`/`850`/`670` are literal on-screen strings. Nothing from
  [[audit-en]]'s kill-list (no 740, no 714, no decimal APR, no quarter label).
- **Currency separation verified programmatically**, not by eye: splitting `index.html` at the
  EN marker gives en block **0 rupee / 8 `$`**, hi block **0 `$` / 9 rupee**.
- ≤12 chars per line, ≤2 big lines per variant, one focal + one accent each.

Two in-flight fixes, both real: v1's sub wrapped and orphaned "miss" (block 76% → 88%, sub
34px → 30px), and v2 initially reused the hi cut's hard `.bright` grade, which erased the
car-key plate entirely — the en7 layout only carries type on the left third, so the standard
grade was correct. The v3 gauge split is geometrically honest: (670−300)/(850−300) = **67.3%**.

**Sameness call made honestly rather than flattered:** thirteen of the channel's fifteen prior
variants resolve to "one big red number over a graded photo," and **v2 is a fourth consecutive
red-mega-$ lead** while **v1 is the second red-mega-"N YEARS" in two uploads** (good-debt v2
shipped "18 YEARS"). Only **v3** — first gauge, first green-focal-over-photo on this channel —
is a real break. v1 is still recommended, on the merits, not on novelty. Cross-channel flag
raised: v3-en and v3-hi are the same composition, so picking both ships one asset in two
languages on the same day.

## Search evidence

`tools/autocomplete.py`, 32 seeds, gl=us hl=en, 2026-07-29. No transient failures.

**The headline result is a genuine difference from the hi cut:** the seven-year hero has a
**live query in question form** — `how long do late payments stay on credit report`
autocompletes as its own seed *and* as a completion of the longer phrasing, with `30 day late
payment on credit report` alongside. The hi cut's equivalent hero string returned nothing.
So the en title can lead with the demand string and answer it with the video's
strongest-sourced claim.

Other verified clusters: `credit score explained usa` (own seed, #2 on the parent) ·
`how credit score works in usa` (#1 on its seed) · `credit score for car loan` +
`average car loan interest rate by credit score` (en7's beat almost verbatim) ·
`what is a good credit score` · `fico score explained` / `…vs credit score` ·
`credit utilization ratio credit score` · `dispute credit report` · `how to build credit`
(deepest clean-US cluster in the pull) · `what is a fair credit reporting act`.

**Four empties/negatives, all recorded and all load-bearing:**
`7 years credit report` → **NO SUGGESTIONS** (the hero number is the answer, not the query) ·
`what hurts your credit score` → **NO SUGGESTIONS** (en5's own framing has no string, which
kills the obvious title for that scene) · `credit score mistakes` → **NO SUGGESTIONS** ·
`autopay` under gl=us → Hindi strings plus **cancel** strings. That last one now **confirms in
both markets** what the hi pack found in one: en6's action step is not a search string
anywhere, in either cut.

**Lane contamination is the finding that shaped the title.** Under `gl=us hl=en` the bare
seeds are South-Asia-heavy (`credit score …easypaisa/pakistan/kaise badhaye`,
`cibil score range in tamil`, telugu/kannada/malayalam variants), and **`credit history` —
the video's internal name — returns 8 of 10 non-US strings**. Also `how to improve credit
score in mobile legends` — the phrase collides with a video-game credit score. Hence: the
title must not lead with the internal name, and where a US disambiguator exists as a verified
string (`…usa`), it earns its place.

**Competitor scoreboard: `library.db` is empty for this lane — verified, not assumed.**
1,124 rows; 0 match credit/loan/score/debt/bureau. The three substring hits are false
positives (`fico` inside a Portuguese "Ficou", `apr` inside two WW2 docs' "April"). Scrape
still owed to the orchestrator, same as the last four runs. Autocomplete-only competitor
signal: the build-credit lane is owned by product-led creators (chime / capital one / secured
card), `free credit report` is owned outright by a 2007 ad jingle — but **nothing named
attaches to the retention / seven-year lane**, unlike the hi cut (kuldeep singhania) and
good-debt (Kiyosaki/Ramsey).

## Title

Recommended: **How Long Do Late Payments Stay on Your Credit Report? 7 Years** (61 chars) —
leads verbatim with the verified live string and answers it with the FCRA claim, which is the
only HARD-on-the-nose fact in the file. Query, hero fact and thumbnail number are the same
thing; that is the best structural position any title in this series has had. Four alternates
in the pack, each named against its cluster, including one (#5, the flat thesis statement)
offered **and argued against** because both of its phrasings returned NO SUGGESTIONS.

Also recorded in the pack: **do not lift `READ BEFORE YOU ARE` from the en9 recap chip into
any title, description or tag.** It is approved upstream copy that only works as a compressed
echo of the VO line; standing alone it is a dangling fragment. The description uses the full
sentence instead.

## Gate 2

- **Altered-content disclosure: "No".** Synthetic narration (ElevenLabs Brian) but no
  realistic synthetic media presented as real — motion graphics over licensed stock. No
  on-screen disclosure required or present. Narrator is a voice, not a persona; no lender,
  card, bureau or monitoring-product pick; FICO/"credit report" as terminology only; Experian,
  CFPB, the Fed and the FCRA only as muted source foots. The pack also records **where** a
  disclosure would go if the creator elected to add one anyway (the empty `foot` slot in en1,
  never over the en5 timeline or en7 rate rows) while noting it is neither required nor
  recommended.
- **⛔ Channel sameness — 6th consecutive blockframe-9 on @moneymavens101, on its own record.**
  50-30-20 (3:43) → emergency-fund (2:46) → needs-vs-wants (2:49.6) → pay-yourself-first
  (2:57.8) → good-debt-vs-bad-debt (2:59) → this (2:53.2); five of six inside a 13-second
  runtime band. **The pattern holds independently of the hi channel — nothing was inherited.**
- **What makes this different from a first flag:** this channel's own packs flagged the 4th
  ("the next upload would be the 5th — vary the architecture") and the 5th ("a 6th would be an
  indefensible template run… escalate before the next en cut is scripted"). The next en cut
  was then researched, scripted, voiced, built, rendered and packaged on the same architecture.
  Three identical warnings, zero behaviour change. **So the escalation is not a fourth warning
  — it is that the control is in the wrong place.** A pack is read at upload; the architecture
  is chosen by `tier` in `run.json` before fin-script runs. A gate that fires after the
  artifact exists cannot change the artifact. Owed action (orchestrator's — I may not write
  `tools/` or `.claude/`): make the next run's `tier` a deliberate, recorded decision and treat
  "6 consecutive shorts on blockframe-9" as the reason it must not be `short` again.
- **Cross-channel observation this pack could make and neither prior one could:** the two
  channels have now shipped the same six topics, in the same order, on the same architecture,
  in the same runtime band. Per-channel review sees six each; together it is a twelve-cut
  template run from one pipeline. It does not change either channel's Gate 2 position, but it
  does mean one architecture change fixes both — and that the second channel provides no
  diversification against this risk.
- Publishing this cut remains defensible; scripting a 7th on the same architecture is not.
- Recording caveat: only pay-yourself-first has a confirmed upload URL, so the count is the
  **production** sequence (confirmed-live count is 1). Recording upload dates in the milestone
  notes is still owed.

## Findings owed / not fixed here

1. **`chosen:` is unfilled in five packs and this makes six — and the finding is now sharper
   than the hi pack could put it.** pay-yourself-first was **actually uploaded 2026-07-28**
   (`youtu.be/mlvp4xZTROg`, `youtu.be/PKU0_TeJ9_c`) and its `chosen:` line is *still* blank.
   The field survived a real upload, so a sixth request will not work either. **Cheap fix that
   depends on nobody: the chosen thumbnail is the public thumbnail — fin-archive can read the
   pick back off the live video by comparing it against the three PNGs. Both pay-yourself-first
   URLs are live now, so two of the missing picks are recoverable today.**
2. **Finance-lane scrape still owed** — `library.db` has never seen this lane (5th run running).
3. Thumbnail composition space on @moneymavens101 is close to exhausted at 3 variants ×
   6 uploads on a fixed design system; the next real variance has to come from the design
   system or the video's visuals, not from re-arranging the same three parts.
4. Housekeeping: the `snapshots/` scratch dir now holds only the three en frames — the hi
   frames were overwritten by this run's `--at`. The hi deliverables (`thumbnail-hi-v*.png`)
   are untouched, and the frames regenerate from `--at 1,3,5`.

## Commands run

Only the allowlist: `npm run check` and `npx hyperframes@0.7.66 snapshot --at 7,9,11 --no-end`
(and one earlier `--at 7,9` re-snapshot after the two fixes) inside
`studio/videos/credit-history-thumbs/`, plus `python3 tools/autocomplete.py --q "…" --gl us
--hl en` (32 seeds). One read-only sqlite count on `library.db` for the competitor scoreboard;
no scraper needed. File staging used `cp` (three scene photos); edits to `index.html` and the
pack were file writes. The legibility assert and the currency/tag scans ran through
`venv/bin/python` (Pillow) on the produced PNGs and files. No git.
