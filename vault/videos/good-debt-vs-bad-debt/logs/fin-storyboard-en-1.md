# fin-storyboard · good-debt-vs-bad-debt · en · attempt 1

**Date:** 2026-07-28 · **Tier:** short (blockframe-9) · **Result:** ok

## Inputs read
- `vault/CLAUDE.md`, `tools/format.json` (layout ladder, colours, `photo_free_scene_ratio` 0)
- `vault/knowledge/design-finance-blockframe.md` (the dark system — the ONLY finance design doc)
- `vault/templates/storyboard-template-finance.md`
- `vault/videos/good-debt-vs-bad-debt/script-en.md` ($ SET, audit-approved)
- `studio/videos/good-debt-vs-bad-debt-en/assets/voice/timing.json` (measured, total **178.582s / 2:59**)
- `vault/videos/good-debt-vs-bad-debt/storyboard-hi.md` (master skeleton — element IDs ported verbatim)
- `studio/videos/good-debt-vs-bad-debt-hi/assets/img/manifest.json` (shipped hi queries, for cross-cut hash-distinctness)

## Written
- `vault/videos/good-debt-vs-bad-debt/storyboard-en.md` — 9 scenes, 4-line colour table, per-scene DOM + GSAP cue table (anchored/fixed classes) on measured en timings, keyword bg + cut-ins, full `-en` divergence list.
- `studio/videos/good-debt-vs-bad-debt-en/assets/img/manifest.json` — **16 slots** (9 bg + 7 cut-ins).

## Key decisions / catches
1. **Colour semantics** = thesis roles: red = interest/minimum-payment trap & bad debt; green = good debt / the escape (paying MORE) / money kept; amber = the card/decision under examination; orange = do-it-today CTA. Matches the hi cut (same thesis).
2. **Cross-stage colour correction (s6).** `script-en.md` §en6 puts the `--fund` (green) span on **MINIMUM** — the trap in the escape colour. Corrected to sit on **MORE**, carrying the hi audit fix. Flagged for the audit.
3. **s1 timing (fin-voice en1 flag).** Interest reveal `#s1r2` ($110) anchored to «pure interest» at +13.1; full month-1 split ($170 +9.5 / $110 +13.1 / $60 +14.3) lands **≤15s**. Build advisory: whisper-verify; if the interest clause measures past 15s, tighten r1/r2 forward, never push r3 earlier than spoken.
4. **US market.** $ only, no ₹. s5 uses the US **"1% of balance + interest"** minimum (not India's 5%) — the load-bearing rewrite divergence. s7 hero math $6,000 @ ~22% → $5,318 / 215 mo / $9,496 (build-calculator-locked slots, displayed not spoken). US source foots (Chase/Capital One/CFPB Reg Z; Fed G.19/WalletHub).
5. **Every scene has a bg photo** (photo-free retired). Densest scenes (s4/s5/s7) get the calmest bg. Phone-screen bg/cut-ins (script s6/s8) and s9 face+phone replaced object-led per design §7.
6. **Image pool distinct from hi.** All 16 queries reworded + $-market so top hits differ from the shipped hi manifest (checked against it: hi shipped s1=overdue-bills, s7=calculator-keypad, s9=seedling — none reused). Build must md5-check the non-currency concepts (cap+books, snowball, calculator, card+calc, card statement).
7. **Divergence list** — one reason per scene, s5 (mechanism) + s7 (hero math) load-bearing; not a translation in a layout costume.

## Layout checks (format.json)
- One focal per scene ✓ · first cue +0.40 (≤0.5) ✓ · ≤6 simultaneous (peaks: s2 6, s6 6, s7 6, s8 6) ✓ · cue gaps ≥0.8 except declared cascade s6 (4 items @ 0.6s) ✓ · chips ≤3/row, ≤22 chars (verified per scene) ✓ · ken alternates in/out ✓.

## Open items for build
- Anchored offsets are char-interpolated — refine with faster-whisper word timings (s1 ≤15s is the hard one).
- s7 integers = regenerate from the $35-floor $ model, `en-US` grouping; do not use the transcribed values.
- md5 every image against the full ledger; drop a cut-in (never the bg) rather than ship a colliding/faked hash.
