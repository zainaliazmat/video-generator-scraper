# fin-package — good-debt-vs-bad-debt · hi · attempt 1

**When:** 2026-07-28 · **Stage:** thumbnails + publish pack + Gate 2 compliance
**Status:** ok

## Inputs read
- `vault/CLAUDE.md`, `tools/format.json` (cuts.hi: @cashguruguides, ₹, $ forbidden, Harsh)
- Render `studio/videos/good-debt-vs-bad-debt-hi/renders/FINAL-1080p-hi.mp4` — ffprobe 195.20s, 1920×1080, h264, ~11.93 Mbps, AAC. Matches timing.json 195.17s (+0.03 AAC priming).
- `[[script-hi]]` (fact-trace), `[[storyboard-hi]]` (scene DOM + measured timing.json), `assets/voice/timing.json` (chapter scene_start values).
- House style: `[[../pay-yourself-first/youtube-metadata-hi]]`, `studio/videos/pay-yourself-first-thumbs/index.html`, `[[../../knowledge/design-finance-blockframe]]`.
- Sibling packs for the two sameness checks: 50-30-20, emergency-fund, needs-vs-wants, pay-yourself-first.

## Deliverables written
- `vault/videos/good-debt-vs-bad-debt/youtube-metadata-hi.md` — 4 Roman-Hindi title options, Hinglish description w/ real chapters + on-screen sources + disclaimer, 17 tags, Gate 2 record.
- `studio/videos/good-debt-vs-bad-debt-thumbs/` — new HyperFrames project (mirrors pay-yourself-first-thumbs): `index.html` (§v1/v2/v3), `package.json`, `meta.json`, assets (font + gsap + grain copied from pyf-thumbs; bg s7/s5/s1 copied from the video's own `assets/img`).
- 3 thumbnails: `thumbnail-hi-v1.png` · `-v2.png` · `-v3.png` (1280×720). Snapshot via `npx hyperframes@0.7.66 snapshot --at 1,3,5 --no-end`.

## Checks
- `npm run check` (allowlisted, inside thumbs dir): Lint 0 / Runtime 0 / Layout 0 / Motion 0 / **Contrast 22/22 WCAG AA** / check passed.
- Legibility assert (largest line ≥40% width @ 320×180): v1 ₹88,614 ~60% · v2 "17 SAAL" ~55% · v3 ₹1,667 ~49% — all pass. Visually verified all 3 (₹ glyph renders, grade darkens the photos so light text reads).
- **Numeral discipline — every thumbnail numeral is in script-hi.md:** v1 88,614·50,000 (s7) · v2 208·17·50,000 (s7) · v3 2,583·1,667·916 (s1). No $ anywhere; ₹ only where a figure appears.

## Search evidence (fresh — a change from the pay-yourself-first run)
`tools/autocomplete.py` now exists (added 2026-07-28). Fresh pull gl=in hl=hi, ~18 seeds, each fetched; empties recorded:
- Verified live: `credit card minimum payment trap`, `minimum payment trap`, `credit card minimum payment kya hota hai`, `credit card ka/mein minimum payment karne se kya hota hai`, `credit card ka byaj kitna lagta hai`, `credit card ke jaal se kaise bache / …se bahar kaise nikale`, `good debt vs bad debt in hindi`, `50000 credit card debt`.
- Empty (recorded): `acha karz aur bura karz` (→ title stays English "Good Debt vs Bad Debt"), `how minimum payment works`, `debt kaise khatam kare` (thin).
- Competitor: `library.db` empty for this lane (scrape owed, not run — orchestrator's step). Autocomplete signal: Ankur Warikoo owns `credit card trap`; our differentiator = the specific minimum-payment math.

## Findings / flags
- **Recommended title:** #1 — *Credit Card Minimum Payment: Ek Jaal — ₹50,000 par ₹88,614 Byaj* (pairs with thumbnail v1).
- **Recommended thumbnail:** v1 (centred red ₹88,614 over the calculator).
- **Thumbnail sameness:** no near-duplicate of any last-3 thumb; v2 is the channel-continuity option (red/left/photo), v1+v3 vary composition. Recorded in pack.
- **⛔ Channel-level sameness (Gate 2, hard flag):** this is the **5th consecutive blockframe-9** on @cashguruguides — the enforcement line the pay-yourself-first pack warned about. Publishable, but the **next cut must change architecture**. Escalate before next script.
- `chosen:` line left unfilled for the creator (fin-archive reads it back — the thumbnail loop learns from it).

## Notes for next stage
- s1.jpg shipped as a notebook/coffee desk flat-lay (not the storyboard's "credit card + bills" keyword) — fine as a scrimmed dark texture under v3, noted for asset provenance.
- en pack not written yet (`studio/videos/good-debt-vs-bad-debt-en` exists) — Gate 2 end-screen cross-link owed when it ships.
