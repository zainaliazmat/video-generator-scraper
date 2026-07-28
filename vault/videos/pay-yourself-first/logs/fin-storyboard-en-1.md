# fin-storyboard · pay-yourself-first · cut=en · tier=short · attempt=1

**Date:** 2026-07-28 · **Status:** ok

## Inputs read
- `vault/CLAUDE.md`, `tools/format.json` (layout constants, en cut: $, en-US, Brian)
- `vault/knowledge/design-finance-blockframe.md` (only design doc — techtooltester NOT read)
- `vault/templates/storyboard-template-finance.md`
- `vault/videos/pay-yourself-first/script-en.md` (US rewrite, hero math $400/mo → $4,800/yr)
- `vault/videos/pay-yourself-first/storyboard-hi.md` (master skeleton — IDs ported)
- `studio/videos/pay-yourself-first-en/assets/voice/timing.json` (measured, en1..en9, total 177.772s) ✓ present

## Output
- `vault/videos/pay-yourself-first/storyboard-en.md`
- `studio/videos/pay-yourself-first-en/assets/img/manifest.json` (9 slots)

## Decisions
- Skeleton + element IDs ported verbatim from the hi master; new IDs only where the
  en script adds beats: `s1stat/s1f` (BofA stat), `s4t` (10% chip), `s5m` (BLS
  median-pay chip), `s6t3` (FDIC), `s6x` (~10× sub), `s7echo` (Fed SHED $400 flip).
- Divergence list: 7 of 9 scenes diverge with reasons (s2, s9 structurally identical — noted).
- Colour semantics same as hi (same thesis, same video); the one deliberate
  warn→fund flip is `#s7echo` ($400 emergency → $400 auto-save).
- Counter: $0 → $4,800 in 12 stepped increments of $400, `Intl.NumberFormat("en-US")`.
- Photo-free: s2 + s7 (matches hi master, 2/9 ≤ 0.23 cap), both `drift()`; s7 is
  densest scene → calmest background.
- Exits declared to hold ≤6 simultaneous: s5 (kicker), s6 (flow row), s7 (sub, then
  kicker), s8 (stamp), s9 (kicker). s6 phase order inverted (flow → chips) to
  follow en VO order.
- All anchored offsets char-interpolated from en VO text against measured clip
  durations (0.4 + chars_before/total × clip); marked A/F; surplus → holds.
- Image queries: US object-led (dollar bills, US paycheck), phone-screen and face
  queries from script-en replaced per design ban; queries re-worded vs hi cut to
  avoid deterministic top-hit hash collisions.

## Checks
- Cue spacing ≥0.8s outside declared cascades (s5 chips ×3 @0.65, s6 flow ×5 @0.6) ✓
- First cue +0.40 every scene ✓ · ≤3 chips/row, ≤22 chars ✓ · ken alternates in/out/in/out/in/out/in ✓
- Timing table = timing.json verbatim; total 177.772s ✓
- No ₹ / India institution anywhere; foots cite BofA, BLS, BEA, Fed SHED ✓
