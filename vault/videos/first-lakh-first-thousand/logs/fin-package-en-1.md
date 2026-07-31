# fin-package — first-lakh-first-thousand · cut `en` · attempt 1

**Status:** ok · 2026-07-31

## Inputs read
- `vault/CLAUDE.md`, `tools/format.json` (`cuts.en`, `architectures.swiss-band`, `colors`)
- `vault/videos/first-lakh-first-thousand/{run.json, script-en.md, youtube-metadata-hi.md}`
- `studio/videos/first-lakh-first-thousand-en/{index.html, assets/voice/timing.json, renders/PUBLISH-1080p-en.mp4}`
- Prior-upload records: `vault/videos/{50-30-20-rule,emergency-fund,needs-vs-wants,pay-yourself-first,good-debt-vs-bad-debt,credit-history}/index.md` + credit-history's `youtube-metadata-en.md` (thumbnail sameness baseline)

## Thumbnail — ONE, v2 style
Added section `#env2` to the existing `studio/videos/first-lakh-first-thousand-thumbs/index.html`
(one project per slug; the hi section `#v2` is untouched). Root `data-duration` 2 → 4 so the
two cuts sit on separate timeline windows: hi at 0–2s (track 1), en at 2–4s (track 2).
Exported `npx hyperframes snapshot --at 2.5` → `thumbnail-en.png`.

- Photo: `assets/img/en-s1.jpg`, a copy of the en render's own `s1.jpg` (worn $1 bills on a
  plank) — scene 1, the frame that carries `THE FIRST $10,000 / 12.5 MONTHS`. Copied with
  its `.src` sidecar. Given its own `.bg.en` grade (`grayscale .46 / brightness 1.10 /
  contrast 1.12`); the hi plate's grade is tuned for a low-key coin macro and blows this one out.
- Deliberately NOT the en cut's quarter macro (`s5.jpg`), which would have made the hi and en
  thumbnails one asset in two languages. Recorded as a decision in the pack.
- `npm run check`: 0 lint · 0 runtime · 0 layout (9 samples) · 0 motion · 25/25 WCAG AA.
- Legibility assert: at 320×180 the red mega `12.5 MONTHS` spans x18→265 = **248px = 77.5%**
  of frame width (threshold 40%). Measured by isolating `--warn` pixels above the rule.
- `≤12 chars × ≤2 lines`: `$800 / MONTH` (12) · `12.5 MONTHS` (11). Pass.
- Currency firewall: en section = 0 rupee glyphs, 4 `$`.
- Numeral discipline: 10,000 / 800 / 12.5 / 6 — all four spoken in script-en and on screen
  in the render (s1, s2, s3, 6.5, 9.5).

## Research
`tools/autocomplete.py --gl us --hl en`, 30 seeds, all fetched this session. Empties recorded.
Two findings that changed the recommendation:
1. `why the first 10k is the hardest` is a **live query** (own seed + #1 completion of
   `first 10k is the hardest`) — the opposite of the hi cut, where the thesis returned nothing.
   But `the first 10000 is the hardest` redirects to the **100k** string, so the script's own
   recommended `$10,000` phrasing loses its own lane. Retired in favour of the `10K` spelling.
2. Same earn-vs-save verb trap as the hi cut, in English: the `10000 dollars` / `first 10k`
   lane is dominated by make/earn (plus heavy road-race contamination on bare `10K`).
   Every recommended title leads with **save** and keeps `$` on the numeral.
Empties recorded: `savings rate vs return` (chapter 4's whole thesis has no query),
`10000 in 12 months` (loan noise), `first 100000`, `munger first 100000`, `saving rate`.

Competitor scoreboard from `library.db` (read-only): 7 US rows survived manual filtering.
Two limits stated in the pack rather than papered over — `subscribers` is empty across the
lane (no views÷subs recompute), and the US slice is contaminated with Hindi SIP videos,
AI-money videos and celebrity-net-worth biographies.

## Chapter times
Read from `timing.json` `scene_start` of each chapter's first line (92 lines, total 505.561s
vs the 505.600s container). 9 chapters, first at 0:00, smallest gap 43s. YouTube-valid.

## Gate 2
- Altered-content toggle **No**; no on-screen disclosure required and none appears. No host
  persona — grep-verified that no VO line in script-en contains "I", "my" or "we" (the only
  "I" in the file is in the Chapter 6 heading, quoting the viewer). No product pick; the
  FDIC rate / HYSA ratio / Fed range are price evidence and the render's foots say so.
- Channel sameness **not flagged**, verified on @moneymavens101's own record rather than
  inherited from the hi cut: six prior en uploads were all blockframe-9 at 2:46–3:43.3;
  this is the **first swiss-band on this channel**, 92 scenes, 8:25.6 (2.3× the previous
  longest), per-line chapters, and the channel's first offense video.

## Carried forward (not fixed here)
- `chosen:` still blank for pay-yourself-first (hi+en) and credit-history (hi+en) — four live
  videos, no CTR readback yet. Filled by construction on both cuts of this video.
- `run.json owed_creator_decision` (the `architecture_lock` vs ask-the-style disagreement) is
  unchanged and still worth closing in code, not per-run.

## Writes
- `vault/videos/first-lakh-first-thousand/youtube-metadata-en.md`
- `studio/videos/first-lakh-first-thousand-thumbs/thumbnail-en.png`
- `studio/videos/first-lakh-first-thousand-thumbs/index.html` (+`#env2` section, `.bg.en` grade, root duration 4)
- `studio/videos/first-lakh-first-thousand-thumbs/assets/img/en-s1.jpg{,.src}`
