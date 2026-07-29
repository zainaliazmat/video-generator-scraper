# fin-package — good-debt-vs-bad-debt · en · attempt 1

**When:** 2026-07-29 · **Stage:** thumbnails + publish pack + Gate 2 compliance
**Status:** ok

## Inputs read
- `vault/CLAUDE.md`, `tools/format.json` (cuts.en: @moneymavens101, $, ₹ forbidden, Brian, 15 c/s).
- Master `studio/videos/good-debt-vs-bad-debt-en/renders/FINAL-1080p-en.mp4` (2:59 / 178.6s, per task) — matches `assets/voice/timing.json` total 178.582s.
- `[[script-en]]` ($ SET fact-trace), `[[storyboard-en]]` (scene DOM + measured timing.json), and the **built render** `studio/videos/good-debt-vs-bad-debt-en/index.html` for the actual on-screen (build-calculator-locked) integers.
- House style: `[[../pay-yourself-first/youtube-metadata-en]]` (en pack reference), `[[youtube-metadata-hi]]` (sibling hi pack, parallel structure), `studio/videos/good-debt-vs-bad-debt-thumbs/index.html` (existing hi thumb project).

## Deliverables written
- `vault/videos/good-debt-vs-bad-debt/youtube-metadata-en.md` — 5 US-English title options, description w/ real chapters + on-screen sources + education-not-advice disclaimer, 18 tags (15 autocomplete-verified), Gate 2 record.
- `studio/videos/good-debt-vs-bad-debt-thumbs/` — added 3 en sections (§env1/env2/env3) to the existing project's `index.html` (hi §v1/v2/v3 preserved verbatim; root data-duration 6→12). Staged the en video's own s7/s5/s1 photos as `en-s7.jpg`/`en-s5.jpg`/`en-s1.jpg` (distinct md5s from the hi thumbs images).
- 3 thumbnails: `thumbnail-en-v1.png` · `-v2.png` · `-v3.png` (1280×720). Snapshot via `npx hyperframes@0.7.66 snapshot --at 7,9,11 --no-end`, renamed from the frame-*.png outputs.

## Checks
- `npm run check` (allowlisted, inside thumbs dir): Runtime 0 / Layout 0 / Motion 0 / **Contrast 21/21 WCAG AA** / **check passed**. One cosmetic `timeline_track_too_dense` warning (6 timed elements — hi+en co-hosted in one project per the "one HyperFrames project" contract; a warning, not an error). Version-pin nudge (0.7.66 → 0.7.81) ignored — pin is intentional (`format.json hyperframes_pin`).
- Legibility assert (largest line ≥40% width @ 320×180), visually confirmed on the rendered PNGs: v1 `$9,506` ~55% · v2 `18 YEARS` ~65% · v3 `$110` ~42% — all pass (v3 mega sized to 240px specifically to clear 40% with a 4-glyph string).
- **Numeral discipline — every thumbnail numeral is on-screen in the en render:** v1 9,506·6,000 (s7) · v2 215·18·6,000 (s7 "215 MONTHS · 18 YRS") · v3 170·110·60 (s1 month-1 split). **No ₹ anywhere**; $ only.
- Visual QA of all 3 PNGs (Read): $-only confirmed, red-trap focal + amber accent, dark blockframe design, cinematic not cluttered, no AI-collage/shocked-face. v3 bg is an unmistakable US $1 bill (pyramid/eye) — reinforces US market.

## Numeral correction caught (load-bearing)
The render shows **$9,506** interest, NOT the **$9,496** written in `script-en.md`/`storyboard-en.md`.
Those were pre-build hand-estimates; the build calculator regenerated $9,506 (script build-handoff
#5 delegates the on-screen integers to the calculator — "never hand-derived"). Render + thumbnail +
description all say $9,506, consistent. Flagged in the pack so nobody reverts the thumbnail to $9,496.
(Also confirmed on-screen: $5,318 after 1 yr · 215 months · 18 yrs — the storyboard's "215 MONTHS
(~18 years)" shipped as "215 MONTHS · 18 YRS".)

## Search evidence (fresh — gl=us hl=en, 2026-07-29)
`tools/autocomplete.py`, 10 seeds, each fetched; empties/noise recorded:
- Verified live US: `credit card minimum payment trap`, `minimum payment trap`, `credit card
  minimum payments explained`, `credit card minimum payment or full payment`, `credit card minimum
  amount due`, `what happens if you only pay the minimum`, `good debt vs bad debt` (+`good debt bad
  debt`), `credit card interest` (+`rates`/`calculation`), `how to pay off credit card debt`,
  `credit card debt payoff strategy`, `pay minimum on credit card`.
- **Key difference from the hi cut:** `good debt vs bad debt` IS a live US string (the pure-Hindi
  `acha karz aur bura karz` was dead in the hi run) — so it can lead an en title. But Kiyosaki/
  Ramsey own the generic concept (`…robert kiyosaki`, `…dave ramsey` autocomplete); our
  differentiator is the specific minimum-payment math.
- Noise recorded (NOT used as US tags): telugu/tamil/malayalam/sinhala/hindi + `axis bank` strings
  on the broad `credit card minimum payment` seed — India-heavy global volume; kept only clean US.
- Competitor scoreboard: `library.db` empty for this lane (scrape owed = orchestrator's step, not
  run here — same as hi). Autocomplete is the only competitor signal.

## Findings / flags
- **Recommended title:** #1 — *The Credit Card Minimum-Payment Trap: $6,000 Costs You $9,506* (pairs with thumbnail v1).
- **Recommended thumbnail:** v1 (centred red $9,506 over the calculator/notepad).
- **Thumbnail sameness:** no near-duplicate of any last-3 en thumb; v2 is the channel-continuity option (red/left/photo), v1 (red centred over a photo — a new composition, vs pay-yourself-first's green photo-free centred) and v3 vary it. Recorded in pack.
- **⛔ Channel-level sameness (Gate 2, hard flag):** this is the **5th consecutive blockframe-9** on @moneymavens101 — the enforcement line the pay-yourself-first-en pack warned about. Publishable, but the **next en cut must change architecture.** Both channels now at the 5th (hi crossed the same line). Escalate before next script.
- **Gate 2 altered-content:** toggle "No" — synthetic voice only, no realistic synthetic media, no persona, no product pick; disclaimer in description.
- `chosen:` line left unfilled for the creator (fin-archive reads it back — the thumbnail loop learns from it).

## Notes for next stage
- Thumbs project now co-hosts hi (§v1/v2/v3, data-start 0/2/4) + en (§env1/env2/env3, 6/8/10) in one `index.html`; images `s{1,5,7}.jpg` (hi) + `en-s{1,5,7}.jpg` (en). The dense-track lint warning is expected and benign.
- Early slip self-corrected: the initial `cp` of en images into thumbs briefly overwrote the shipped hi `s1/s5/s7.jpg` (check flagged 404s); restored byte-identical from `studio/videos/good-debt-vs-bad-debt-hi/assets/img/` (md5-verified) before re-check.
- End-screen cross-link now resolvable both ways (hi pack owed the en link; en pack links hi).
