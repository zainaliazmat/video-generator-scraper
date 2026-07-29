---
summary: fin-storyboard hi attempt 1 — 9-scene blockframe storyboard + 17-slot image manifest for credit-history. Every scene carries a bg photo; cues built on the measured timing.json (177.642s); s5's 36-cell grid spec'd as the hero animation; two script on-screen notes deliberately diverged (s4 cascade → anchored, s6 flow collapsed to one element) and one image query replaced to avoid a verified hash collision.
updated: 2026-07-29
source: script-hi.md (audit-PASS incl. its 3 edits) + timing.json (measured 177.642s) + design-finance-blockframe §2/§5/§6/§7 + audit-hi.md checks 1/3/8 + fin-voice-hi-1.md s1 advisory + storyboard-template-finance.md
---

# fin-storyboard — credit-history / hi / attempt 1

STATUS: ok

## What ran

- Read (contract order): `vault/CLAUDE.md`, `tools/format.json`,
  `vault/knowledge/design-finance-blockframe.md` (the ONLY finance design doc —
  `design-techtooltester` deliberately NOT read), `storyboard-template-finance.md`,
  `script-hi.md`, `timing.json`. Cross-read `audit-hi.md` (the checks I inherit),
  `run.json`, `fin-voice-hi-1.md` (the ≤15s advisory), `stock-photo-sourcing.md`,
  `good-debt-vs-bad-debt/storyboard-hi.md` (freshest proven master format) and every
  existing `manifest.json` on both channels (collision check).
- Wrote `vault/videos/credit-history/storyboard-hi.md` and
  `studio/videos/credit-history-hi/assets/img/manifest.json`.

## Key decisions

- **Colour table (thesis-derived, NOT inherited).** fund/green = the on-time payment,
  the clean report, the 700+/750+ bands, auto-pay and every action that builds the
  record; warn/red = the missed EMI and the price it charges (the one red grid cell,
  the below-700 band, the extra ₹/month, the extra interest); target/amber = the score
  and the report *under examination* (the 300–900 scale, the three-digit number);
  pop/orange = CTA. Checked every coloured element against it — none argues against
  the script.
- **The anti-drift call.** `good-debt-vs-bad-debt` makes red = "the minimum payment".
  In this video a minimum-only payment is a utilisation caveat, not the trap being
  exposed, so **s6's "not the minimum" renders `--muted`, not `--warn`.** Recorded in
  the storyboard as its own callout — this is exactly the per-video-semantics failure
  §2 warns about, and it was one edit away from happening.
- **Every scene has a bg photo** (creator rule 2026-07-28; `photo_free_scene_ratio` 0).
  9 bg + 8 cut-ins = 17 slots. Cut-ins only where the VO names a concrete thing (s1
  file + bank form, s3 printed number, s4 cards, s5 torn calendar, s6 passbook, s7
  house keys, s8 checklist). **s2 is bg-only and says why** — every noun in h2 is
  abstract and the bg already *is* the report as texture; §7's "drop a cut-in rather
  than fake it" over inventing one.
- **Densest scenes get the calmest bg:** s4 (4-row ladder) → open diary, s5 (grid +
  counter + huge) → stamp & ink pad, s7 (the math) → blueprint texture.
- **ken alternates across all 9** (in/out/in/…), no scene photo-free.
- **Timing verbatim from `timing.json`** (total 177.642s / 2:57.6). Offsets are
  char-interpolated against the *measured* clip lengths, with every anchor's Hindi
  word and its character index recorded so the build's whisper pass can verify rather
  than re-guess. The four-homes rule flagged for build.

## Handoffs honoured

- **Hook payoff ≤15s (audit check 3 + fin-voice flag).** Decoupled deliberately: the
  on-screen focal `#s1q` "YOUR CREDIT REPORT" reveals at **+3.2**, so the payoff no
  longer depends on the VO. The naming «नाम है — क्रेडिट रिपोर्ट» completes at char
  170/212 = 80.2% → ≈**+14.2** (margin ≈0.8s), re-synced by a `pulse` that may slide
  without breaking the gate. Build advisory written: whisper-verify h1; if it slips,
  trim «पर वो तय करती है कि», never the naming.
- **The two forbidden figures.** No "7 years" / CICRA auto-delete and no FICO
  percentage weight anywhere. s4 additionally forbids the *visual* form: rows are equal
  width, no ring chart, no proportional bar — a bar whose lengths differ would smuggle
  FICO's weights back in without a number on screen. `#s4f`'s guard-rail foot states
  it out loud.
- **Audit edits carried through:** s3 reads `750+ = best pricing` (not `750–800`);
  s9 chips are `BANK READS IT FIRST` (19) and `LOW SCORE COSTS LAKHS` (21). Storyboard
  says "do not restore" on both.
- **s5 hero grid** spec'd as behaviour + invariants (3 × 12, green fill left→right
  across the whole scene, one cell slams warn on «एक चूकी हुई किश्त» at +8.0 — which is
  also the script's "~40% of the clip" = 7.8s — and never clears while the fill runs
  past it). No static hold >2s anywhere in the scene.
- **s5 quote-marks residual** (audit's one open item) carried into Placeholders with
  the zero-risk fallback (reported speech).
- **s7 integers** marked build-calculator output, displayed-not-spoken, `en-IN`
  grouping; no lender named, no rate shown, only the spread.
- **s8's per-bureau wording** flagged as load-bearing (it is the one clause whose
  regulator primary was actually fetched).

## Deviations from the script's on-screen notes (deliberate, reasoned in-file)

1. **s4 ranked rows: cascade → anchored.** The script says "cascade, 0.6s apart". The
   VO spaces the four factors across 13.1s; a 0.6s cascade would dump all four in 1.8s
   and leave ~15s with no new motion (fails §5.2) while discarding four clean word
   anchors. Gaps are 3.3 / 6.0 / 3.8s — all ≥0.8, so no cascade is declared. The 6.0s
   hole is filled by the cut-in at +10.0.
2. **s6 flow collapsed to one element.** 3 nodes + 2 arrows = 5 elements would blow the
   ≤6 cap alongside the kicker, huge, cut-in, stamp and two subs. `#s6flow` is one
   `.row` with an internal `popEach` (counts as 1); arrows are CSS `::after` per §4
   (`→` is absent from the font subset). Same collapse `good-debt`'s s4 used.
3. **s4 cut-in re-anchored** from «क्रेडिट यूटिलाइज़ेशन» (collides with `#s4r2`'s own cue)
   to the explanation «लिमिट का कितना हिस्सा» 2.5s later — same beat, legal spacing.
4. **s8 bg is not a magnifying glass.** The script's query duplicates
   `good-debt-vs-bad-debt-hi/s5.jpg` (`magnifying glass financial document numbers`);
   Pixabay's deterministic top hit makes that a near-certain md5 collision — §7's
   verified failure mode. Replaced with clipped document pages, reason recorded.

## Layout self-check (format.json)

- **≤6 simultaneous:** peaks are s1 6 · s2 6 · s3 5 · s4 5 · s5 5 · s6 4 · s7 6 · s8 5 ·
  s9 5. Exits declared wherever a scene would exceed it (s1, s3, s4, s5, s6, s7, s8, s9). ✓
- **One focal per scene**, no `.huge` + `.mega` together: s3's `.mega`@240 scale is the
  only mega and has no huge; s5's `.huge` lands *after* the grid's fill completes;
  s7's punch fires after four exits. ✓
- **First cue +0.40 in all 9 scenes** (≤0.5s). ✓
- **Reveal gaps ≥0.8s** everywhere except three declared cascades: s3 enumeration
  (3 @ 0.7s), s3 band markers (2 @ 0.6s), s6 flow popEach (3 @ 0.7s) — all ≤5 items and
  inside `cascade.gap_seconds` [0.6, 0.7]. ✓
- **Chips ≤3/row, ≤22 chars:** s2 2×2 (18/14/16/20), s9 2×2 (19/21/20/21). ✓
- **Type on the ladder** — `.mega` overridden only to 240, a value already on it. ✓
- **No static frame >2s** — ken under every scene, plus s5's grid fill running
  continuously from +2.6 to +17.0. ✓
- **Currency purity:** zero `$` in the storyboard file (the `-en` divergence list names
  the US market in words only). ✓

## Returns

- **Scene count:** 9.
- **Image-slot count:** 17 (9 bg + 8 cut-ins). Per scene — s1 3 (bg + 2 cut-ins) ·
  s2 1 (bg) · s3 2 · s4 2 · s5 2 · s6 2 · s7 2 · s8 2 · s9 1 (bg).

## Artifacts

- `vault/videos/credit-history/storyboard-hi.md`
- `studio/videos/credit-history-hi/assets/img/manifest.json`

## Notes for the next stage

- Three image slots carry a known collision risk and are named in the storyboard's
  Image-sourcing note: `s5-cut.jpg` (vs `pay-yourself-first`'s two calendar assets),
  `s4.jpg` (vs `pay-yourself-first`'s book-pages asset), and the already-replaced
  `s8.jpg`. md5 each against the ledger; on collision use the `#2`/`#3` result knob
  rather than re-wording into another colliding query.
- The `-en` divergence list is pre-seeded in the storyboard with six mandatory
  divergences (FICO 300–850, FICO's *published* weights inverting s4's guard-rail,
  FCRA 7 years replacing 36 months, $ math from scratch, AnnualCreditReport.com
  replacing the RBI FFCR clause, and the passbook/EMI nouns). s4 is the largest:
  the `-en` cut may legitimately show percentages this cut is forbidden to carry.
