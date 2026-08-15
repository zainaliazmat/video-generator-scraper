# fin-package — passive-income-number, cut `en`, attempt 1

## Ran

1. Read `vault/CLAUDE.md`, `tools/format/fin-package.json`, `tools/packs/fin-package.md`,
   `run.json`, `script-en.md` (title options + chapter table + numeral trace),
   `storyboard-en.md` §1 (colour semantics), `facts-staging.md` header,
   `knowledge/channels.md` §E, `knowledge/niches/moneymavens-launch-slate.md`
   (title-score gate + thumbnail direction), `knowledge/vidiq-mcp.md`,
   and the three most recent `youtube-metadata-en.md` packs on this channel for the
   sameness comparison.
2. Resolved the six chapter start times out of the SHIPPED composition
   `studio/videos/passive-income-number-en-full/index.html` — `vo-<chapter>-1` → the
   owning scene (`s1`/`s9`/`s24`/`s40`/`s53`/`s69`) → that scene's `data-start`.
   Cross-checked against `run.json.chapters.en` locked frame counts and against
   `ffprobe` on the upload.
3. `python3 tools/autocomplete.py --q "<seed>" --gl us` × **20 seeds**. Every result
   recorded in the pack, including the one empty and the two India-contaminated pulls.
4. Built the thumbnail project `studio/videos/passive-income-number-thumbs/`
   (index.html + package.json + meta.json + CREDITS.txt + assets), exported with
   `npx --yes hyperframes@0.7.66 snapshot . --at 0 --no-end`, ran `npm run check`,
   measured the export at 320×180 by isolating `--fund`/`--warn`/`--ink` pixels.
5. Verified the caption pack (`captions-en.srt` + `narration-en.md`) rather than
   regenerating it — cue count, 84-char cap, ordering, first/last cue against runtime.
6. Verified stock attribution across all six chapter `CREDITS.txt` files against what
   `index.html` actually renders.
7. Wrote `vault/videos/passive-income-number/youtube-metadata-en.md`.

## Failed

**1. The vidIQ title-score gate is UNMET — `packaging.title_score_min` 75 has no number
behind it.**
`vidiq_generate_titles` / `vidiq_score_title` are **not reachable from this stage in this
environment**. The MCP servers registered for this session are `atlassian`, `context7` and
`figma`; there is no vidIQ tool. I did not estimate a score, did not round one up, and did
not write a number into `title-score:`. The frontmatter carries
`title-score: UNSCORED` and `title-scored-on: (not yet scored)`.
Handed to the R3 title-lock pass the orchestrator says runs after this stage with 5,453
credits, with the exact calls and three rejection rules written into the pack §Title.
**This is a fail, not a caveat** — the gate says "never proceed below it", and "no number"
is below it. The rest of the pack is complete and uploadable the moment R3 returns ≥75.

**2. `hyperframes check` failed on the first thumbnail build — `sweep_static`.**

```
Layout ✗ t=0s sweep_static [data-composition-id] — Timeline did not advance under seek;
every green verdict on this run is unreliable.
Fix: Confirm the composition seeks a paused GSAP/CSS timeline under `data-*` timing
attributes rather than only autoplaying.
```

Bisected before trusting the fixHint, per the recorded `japanese-money-methods` lesson
(same message there, different cause — an overflowing `nowrap` line — and two changes were
made on the strength of the hint before anything was tested, both wrong).

- Copy overflow ruled out by measurement: `.type` max-width **660 px**, widest line
  **608 px**. No overflow.
- The proxy tween ruled out: it is the identical construction that passes in
  `japanese-money-methods`.
- **Actual cause, and it is structural rather than a per-video quirk.** That project holds
  TWO 2-second clips inside a 4-second composition, so seeking swaps which section is
  visible and the sweep sees different pixels — the proxy tween never had to do any work.
  This project ships **ONE** thumbnail (creator rule 2026-07-29), so a single clip spans
  the whole composition and every seek returned an identical frame. **The checker was
  correct.**
- Fixed by giving the PHOTOGRAPH a real 4-second drift
  (`fromTo("#plate-en", {scale:1}, {scale:1.04}, duration 4)`), scoped so the type never
  moves, and exporting at **`--at 0`** where the plate scale is exactly 1.000 and the
  documented crop arithmetic holds byte-for-byte. The 8 cosmetic `container_overflow`
  infos this produced are declared with `data-layout-allow-overflow`, not silenced.
- **Every future one-thumbnail project in this repo will hit this.** Written up in the
  pack §"A `check` failure worth writing down" so the next stage does not re-debug it.

**3. The render carries no disclaimer at all — `fact_gate.disclaimer_placements.onscreen`
is UNMET and cannot be fixed from this stage.**
`studio/videos/passive-income-number-en-full/index.html` returns **0 hits** for each of
`advice`, `education`, `educational`, `licensed`, `professional`, `Confirm`,
`tax, or legal`. There is no disclaimer card and no lower third. `script-en.md` contains no
spoken disclaimer line either.
- `spoken` (required ≤0:45 *if any figure lands before then*) — **not triggered**: chapter 1
  runs 0:00–0:46 and has no figure at all (eight lines, no dollar amount, no percentage);
  the first figure is 4.0% at 2.3 ≈1:00. Recorded as reasoning, not claimed as a pass,
  because the constants file also says "All four required."
- `onscreen` — **unconditional, and absent.** Needs a scene edit and a re-render.
- `description` and `pinned` — satisfied by this pack.

## Evidence

### Chapter times — the script table is STALE and was NOT shipped

The orchestrator's brief said the `script-en.md` chapter table is "the AUTHORITY … must be
used verbatim." It is a pre-render estimate at the budgeted 17.57 chars/s and it disagrees
with the shipped composition. `script-en.md` line 123 says so itself: *"Chapter starts after
ch4 shift ≈ +0.7s — regenerate them from measured audio, per build handoff 3."*

| Ch | first scene | `data-start` (index.html) | shipped | script table | delta |
|---|---|---|---|---|---|
| 1 | `s1` | 0.000 | 0:00 | 0:00 | 0 |
| 2 | `s9` | 46.420 | 0:46 | 0:44 | **+2s** |
| 3 | `s24` | 151.938 | 2:31 | 2:30 | **+1s** |
| 4 | `s40` | 248.539 | 4:08 | 4:08 | 0 |
| 5 | `s53` | 335.817 | 5:35 | 5:31 | **+4s** |
| 6 | `s69` | 441.900 | 7:21 | 7:14 | **+7s** |

Corroborating VO onsets from the same file: `vo-1-1` 0.250 · `vo-2-1` 46.670 ·
`vo-3-1` 152.188 · `vo-4-1` 248.789 · `vo-5-1` 336.067 · `vo-6-1` 442.150 — each exactly
0.250 s after its scene, which is the MEDIUM lead-in, so the two records are consistent.

Third independent record, `run.json.chapters.en` locked seconds:
46.433 + 105.533 + 96.601 + 87.300 + 106.084 + 85.973 = **527.924 s**. Cumulative sums
reproduce the measured `data-start` values to within 0.02 s. `ffprobe` on the upload:
528.000 s container, 15,837 frames @ 30/1, 595,718,638 B, 9,026 kb/s, 1920×1080.
**Two records agree with each other; the script table agrees with neither.** Drift is
monotonic and grows with runtime — a 7 s error at 7:21 drops the viewer inside chapter 5's
closing beat, in a video whose payoff is the 5.7 reveal.

### Thumbnail — measured, not asserted

`studio/videos/passive-income-number-thumbs/thumbnail-en.png` · 1280×720 · 1,071,332 B.

`npm run check` (`hyperframes@0.7.66`): **0 lint · 0 runtime · 0 layout across 9 samples ·
0 motion · 15/15 WCAG AA contrast.**

Legibility at **320×180** (LANCZOS downscale of the export, coloured pixels isolated):

| Line | x-extent | span | % of width | right margin |
|---|---|---|---|---|
| `$1.5M at 4.0%` (green `--fund`) | 17 → 161 | 145 px | 45.3 % | 158 px (49.4 %) |
| `$5.6M at 1.08%` (red `--warn`) | 17 → 168 | 152 px | **47.5 %** | 151 px (47.2 %) |
| `Same paycheck.` (ink) | 17 → 124 | 108 px | 33.8 % | 195 px (60.9 %) |

Threshold ≥40 % on the largest line → **47.5 %, pass**, with a real 151 px right margin
(no frame-edge contact). ≤12 chars/line: `$1.5M at 4.0%` = 13, `$5.6M at 1.08%` = 14 —
**1–2 over, flagged and kept**, because the overage is entirely the inline rate and moving
it to its own row creates the body-copy sub-line the 2026-08-06 rule bans.

Plate provenance: `assets/img/plate-vault.jpg` md5 `9e99f67b08eb537eff2cf7f54dc6af91` ==
`studio/videos/passive-income-number-en-ch4/assets-ch4/final/s41.jpg` md5
`9e99f67b08eb537eff2cf7f54dc6af91`. The cut's OWN scene photo, the frame carrying
"RUNG FOUR · $1,500,000 · AT A 4.0% WITHDRAWAL RATE" at 4:15. **No deviation to record** —
no sibling-cut borrow, no retired asset, no AI art, no new fetch.

Numeral trace (every numeral on the tile is in the script AND on screen in the render):
`1.5` → 4.2/4.3 frame `$1,500,000` · `4.0` → 2.3 onward, 14 corpus frames ·
`5.6` → 5.7 VO "five point six million" · `1.08` → 5.7 frame `$5,555,556 AT 1.08%`.
⚠️ **`5.6` is a rounding of the frame's `$5,555,556`** — it is the script's own spoken form
and its own title option 2 form, so it is traceable, but it is a rounding and the pack says
so rather than implying an exact match.

Packaging pattern (`fin-package.json packaging`): objects **1** (the two-door source photo
is cropped so the hero door sits at x 754–1220 and the second door at x 191–583 under a
~0.88 scrim, reading as brick) · red elements **1** (one line, no rule/circle/arrow) ·
ALL-CAPS words **0** · title repetition **none** (title sells the income, tile sells the
price) · emoji/brackets **none** · no person, no chart.

⚠️ **Word-count deviation, recorded not hidden.** Word tokens excluding figures = 4
(`Same` · `paycheck` · `at` · `at`), inside the 2–4 band. Counting figures = 8. The extra
load is `at 4.0%` and `at 1.08%`, which are `run.json.constraints.withdrawal_rate_on_screen`
and not copy. Constraint beats packaging preference.

⚠️ **Cool-background/warm-subject is a PARTIAL pass.** The plate is warm brick. Handled with
one lever — `saturate(0.52)` — chosen because brick is strongly chromatic and the vault door
is near-neutral cream, so desaturation separates them in chroma without a second layer. A
cooling overlay would have been a second grade stacked on a photograph, which is what
`grade_note` exists to prevent. Result reads "less warm background, neutral-bright subject",
not the plan's ideal. Flagged.

### Search evidence — `tools/autocomplete.py --gl us`, 2026-08-15, 20 seeds

Headline: **`how much do you need invested to live off dividends` is a live suggestion**
(#3 on the seed `how much do i need invested`). The recommended title's first 47 characters
are a typed string.

Empties and contamination, recorded rather than papered over:
- **`passive income number` → NO SUGGESTIONS.** The slug's own phrase has zero US demand.
  Nothing in the pack uses it.
- `how much to invest for 5000 a month` and `how much invested for 5000 a month` → **all
  ten results are India-market** (`rupees`, `1 lakh`). The `$5,000/month` framing has no US
  autocomplete corpus in that phrasing.
- `dividend income` → returns `dividend income kya hota hai`, `dividend income per kitna tax
  lagta hai` **despite `gl=us`**.
- `trinity study` → contaminated by `trinity bible study`, `trinity college dublin study
  abroad`; only the full `trinity study 4 percent rule` is ours, which is what is tagged.
- `1.5 million retirement` → 2 results only. Thin — `$1.5M` is thumbnail material, not a
  title lead.

⚠️ **Tool caveat with teeth:** several `gl=us` pulls returned unmistakably India-market
suggestions, so either the endpoint is not honouring `gl` or it is blending a session/IP
signal. The tag families actually shipped came back clean and US-shaped, but this is the
second recorded demonstration that autocomplete alone is weak evidence (the first:
`japanese money habits`, 31,899 searches/month, invisible to it). **R3's vidIQ pass should
be treated as the volume authority, not this stage's pulls.**

**No competitor scoreboard pull ran.** `vidiq_similar_*` is unreachable (see Failed 1) and a
fresh `backend/` scrape would have produced a point-in-time snapshot with no baseline inside
this stage. Recorded as owed.

### Tags

14 strings, **458 characters, 42 of headroom** under the 500 limit. Every string is a
verbatim autocomplete suggestion. Six demand-verified strings were **dropped on the
constraints, not on volume**: `how to retire on dividends`, `how to retire on dividend
income`, `dividend portfolio to live off` (`no_unsourced_retire_early` — the video *prices*
retiring on dividends, chapter 4 frames the number as a warning, and a tag is a claim about
what the video delivers); `best dividend stocks for retirement` and `dividend stocks for
retirement` (`fact-integrity` §6 — no naming or implying a good security);
`5000 a month passive income` (the video prices $5,000/month, never promises it).
Four generic/redundant strings were dropped to buy the headroom.

### Captions — verified, not regenerated

`studio/videos/passive-income-number-en/renders/captions-en.srt`:
**149 cues** · **0** over 84 characters (longest is exactly 84, cue #56) · **0** out of
order · last cue `00:08:43,431 → 00:08:47,323` = 527.323 s, inside the 527.924 s timeline
and the 528.000 s container · first cue `00:00:00,250`, matching `vo-1-1 data-start="0.25"`
exactly. Upload route recorded in the pack: Subtitles → Add language → Upload file →
**With timing**. `narration-en.md` present (19,255 B), generated by `tools/transcript.py`
in the same run. Neither file was touched.

### Attribution (licence condition, not bookkeeping)

83 distinct JPEGs rendered by `index.html`; 84 credit rows across the six chapter
`CREDITS.txt` files; **0 rendered images without a credit row.** This is the check that
failed on `japanese-money-methods` (34 of 96 uncredited). Clean here.

### Sameness

Last three shipped `en` thumbnails: `pay-yourself-first` v2 (empty pocket · `EMPTY BY THE
20TH?` · red) · `credit-history` v2 (car key · `EXTRA COST` / `$12,400` + rate rows · red +
green) · `japanese-money-methods` v2 (Japan street · methods row / `3 JAPANESE MONEY RULES`
/ `EVEN ON $4,000 A MONTH` · red + amber + green). This build: bank vault door, a new object
class for the channel; `Same paycheck.` / `$1.5M at 4.0%` / `$5.6M at 1.08%`; green primary
with a single red counterweight; **zero ALL-CAPS words**, a first on this channel. Keeping
the v2 family is intended; this is not a near-identical repeat of any specific predecessor.

⚠️ **Channel-level structure sameness — FLAGGED, below the enforcement bar.** The run of
long-form per-line-chapter cuts is now **3** (first-lakh 8:25.6 → japanese 10:26.8 → this
8:47.9), not 5, and the six ~3-minute blockframe-9 cuts before them are a different format.
So Gate 2's "5th consecutive near-identical structure" is not met. **The finding is that the
`japanese-money-methods` pack explicitly predicted this third cut and asked for a deliberate
choice at the next `run.json` — and the choice was not made.** Runtime has now settled into
an 8–10 minute band, and `architecture_lock` (2026-07-30) removed layout as an anti-sameness
lever. A fourth would put the channel one upload from the bar with no unspent lever.

### Positioning

This run started 2026-08-07 and **pre-dates the 2026-08-15 repositioning** to 50+ US
retirement money. It is not on the committed ten in
`knowledge/niches/moneymavens-launch-slate.md` and was never scored against that slate —
which is a second, independent reason the score gate cannot be waved through here. It is
nonetheless the closest of the pre-repositioning runs to the new lane (safe withdrawal
rates, Trinity, retirement income).

Also carried forward: `assets/brand/moneymavens101.jpg` is still the retired pink coin-face,
so this render watermarks the old avatar on every frame. Third video affected.

## Changed

| Path | What |
|---|---|
| `vault/videos/passive-income-number/youtube-metadata-en.md` | **NEW** — the publish pack. Title + the two alternates with verdicts, the score-gate hand-off, description with measured chapters and on-screen citations, 14 tags, the thumbnail record + `chosen:` line, the plate-only Nano Banana prompt, the caption pack, Gate 2, Owed. |
| `studio/videos/passive-income-number-thumbs/index.html` | **NEW** — one section `#v2-en`, three named layers (`#plate-en` / `.scrim` / `#type-en`), three named text nodes (`#t-subject` / `#t-figure-a` / `#t-figure-b`). Crop arithmetic, scrim ramp targets, colour derivation and the `sweep_static` post-mortem are in the file's own comments. |
| `studio/videos/passive-income-number-thumbs/thumbnail-en.png` | **NEW** — the shipped tile, 1280×720. |
| `studio/videos/passive-income-number-thumbs/{package.json,meta.json,CREDITS.txt}` | **NEW** — `hyperframes@0.7.66` pinned in every script; CREDITS carries the Pexels attribution and the md5 provenance of the plate. |
| `studio/videos/passive-income-number-thumbs/assets/` | **NEW** — `plate-vault.jpg` (byte copy of `s41.jpg`), `grain.png`, `NotoSansFinance-var.woff2`, `gsap.min.js`, all copied from the ch1 project. `node_modules` symlinked to ch1. |

Not touched: `captions-en.srt`, `narration-en.md` (both verified only), `run.json`, any
chapter project, `.claude/`, `tools/`. No git.

**Where to re-cut if R3 moves the title:** `studio/videos/passive-income-number-thumbs/index.html`
→ `<div id="type-en">`, three text nodes only. `#plate-en` never needs touching — a closed
vault asserts "a large store of money", true under any title this video can honestly carry.
Then `npx --yes hyperframes@0.7.66 snapshot . --at 0 --no-end` → copy to `thumbnail-en.png`
→ `npm run check` → re-run the 320×180 measurement on the NEW png → confirm no word or
figure now appears on both the title and the tile → say in the revised pack that §Thumbnail
was re-run.

## Owed

1. **The vidIQ title score — the blocking item.** R3, with the calls and the three rejection
   rules in the pack §Title. Write the REAL number into `title-score:` +
   `title-scored-on:`. Below 75, regenerate; do not proceed.
2. **Re-run §Thumbnail if the title changes.** Instructions above and in the pack.
3. **The on-screen disclaimer.** Absent from the render (Failed 3). Needs a channel-level
   decision written into `knowledge/fact-integrity.md`, not a per-video argument: either a
   re-render with a lower third at the first dollar figure (2.11), or a written finding that
   description + pinned suffice for a non-tax / non-Medicare / non-SS video.
4. **Competitor scoreboard** on the `live off dividends` cluster — one `vidiq_similar_videos`
   call inside R3's budget, before the title locks.
5. **`thumbnail-en-ai.png`** — the enhance prompt ships, the enhanced image does not exist.
   Re-measure legibility and contrast on the RETURNED image, then update `chosen:`.
6. **`vidiq_score_thumbnail` after publish** — needs a live `videoId`.
7. **The tier decision for the next run**, before fin-script, per the sameness finding.
8. **The brand avatar** (`assets/brand/moneymavens101.jpg` → `tools/make_watermark.py en`) —
   channel-level, now on its third video.

**MISSING-CONSTANT:** none. Every constant used came from `tools/format/fin-package.json`.
**OPENED-BODY:** `vault/knowledge/niches/moneymavens-launch-slate.md` — needed the
title-score gate's exact wording and the `vidiq_similar_thumbnails` provenance behind the
packaging block; and `vault/knowledge/channels.md` §E — needed the upload sequence for the
Gate 2 sameness comparison and the About/brand state. Neither is in the pack's BOX.
