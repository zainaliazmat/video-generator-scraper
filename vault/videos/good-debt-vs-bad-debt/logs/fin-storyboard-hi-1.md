---
summary: fin-storyboard hi attempt 1 — 9-scene blockframe storyboard + 16-slot image manifest for good-debt-vs-bad-debt. Every scene carries a bg photo (photo-free retired); cues built on measured timing.json; s1 interest-reveal engineered ≤15s per audit check 3.
updated: 2026-07-28
source: script-hi.md (audit-PASS) + timing.json (measured 195.17s) + design-finance-blockframe §2/§5/§7 + audit-hi.md check 3 + fin-voice-hi-1.md s1 flag
---

# fin-storyboard — good-debt-vs-bad-debt / hi / attempt 1

STATUS: ok

## What ran
- Read (contract order): `vault/CLAUDE.md`, `tools/format.json`, `design-finance-blockframe.md`
  (the ONLY finance design doc — techtooltester deliberately NOT read), `script-hi.md`,
  `storyboard-template-finance.md`, `timing.json`. Cross-read `audit-hi.md` (checks I must
  satisfy), `fin-voice-hi-1.md` (s1 flag), and `pay-yourself-first/storyboard-hi.md` (the
  freshest proven master format).
- Wrote `vault/videos/good-debt-vs-bad-debt/storyboard-hi.md` and
  `studio/videos/good-debt-vs-bad-debt-hi/assets/img/manifest.json`.

## Key decisions
- **Colour table (thesis-derived):** warn/red = interest & minimum-payment trap + bad debt +
  card revolve + interest>borrowed; fund/green = good debt + the escape (paying MORE) + money
  kept off principal; target/amber = the card / "debt = renting money" concept / the decision;
  pop/orange = CTA. Checked every coloured element — none argues against the script.
- **Every scene has a bg photo** (creator rule 2026-07-28; `photo_free_scene_ratio` 0). 9 bg +
  7 cut-ins = 16 slots. Cut-ins only where the VO names a concrete thing (s1 statement, s3
  dinner+sale, s4 shopping bags, s5 snowball, s6 paying, s8 card bill); s2/s7/s9 correctly bg-only.
  Densest scenes (s4/s5/s7) get the calmest bg (books / bank statement / calculator+ledger).
- **ken alternates across all 9** (in/out…), since no scene is photo-free any more.
- **Timing verbatim from timing.json** (total 195.17s / 3:15) — the 4-place rule flagged for build.

## Handoffs honoured
- **s1 interest-reveal ≤15s (audit check 3 + fin-voice flag, TIGHTEST):** h1 is 20.74s; the month-1
  split is revealed synced to speech, not gated to clip end. `#s1r2` INTEREST ₹1,667 (the
  trap-proof) anchored +13.1 on «सोलह सौ सरसठ सिर्फ़ ब्याज», fully readable ≤15s. `#s1r3` principal
  ₹916 synced to its own word «नौ सौ रुपये» (~+15.9) per fin-voice. Explicit build advisory written
  (ffprobe/whisper-verify; if the interest clause measures past 15s, tighten r1/r2 forward, don't
  push r3 early). Full split (₹2,583 / ₹1,667 / ₹916) lands within s1.
- **Colour on a credit-card video:** red is the interest trap, not reused blindly.
- **Audit non-blocking note applied:** s6 green accent moved from "MINIMUM" (the trap) to "MORE"
  (the escape). s2 chip already the 21-char "COMPOUNDS AGAINST YOU".
- **s7 false-precise integers** (₹40,045 / 208 / ₹88,614) marked as build-calculator output,
  displayed-not-spoken; VO stays round-range. Placeholder recorded.
- **+₹1,000 effect kept qualitative** ("CUTS YEARS OFF THE TRAP") — no fabricated payoff.

## Deviations from the script's Visuals (deliberate, per design doc)
- **Phone-screen bg banned (§7, shipped wrong 3×):** s6 `phone banking app` and s8 `phone
  banking app` backgrounds → object-led (fanned notes / card+calculator); s9 `young indian man
  with phone` (face+screen) → calm road-to-horizon closer. Cut-ins re-framed as paper/hand-object.
- **s4 classifier:** a literal 3+3 chip grid = 8 visible > ≤6 cap, so each column is one `.col`
  card (items = internal `popEach` tags). Role colours preserved. Noted in storyboard.

## Layout self-check (format.json)
- ≤6 simultaneous: every scene peaks ≤6 (s2 & s7 hit exactly 6; exits declared where needed). ✓
- One focal/scene, huge→bill handoffs via explicit exits (no huge+mega together). ✓
- First cue +0.40 every scene (≤0.5s). ✓ · reveal gaps ≥0.8 except the one declared cascade (s6, 4 items @0.6s). ✓
- Chips ≤3/row, ≤22 chars (recap chips 15–20). ✓ · No static frame >2s (ken under every scene). ✓

## Returns
- **Scene count:** 9.
- **Image-slot count:** 16 (9 bg + 7 cut-ins). Per scene: s1 2 · s2 1 · s3 3 · s4 2 · s5 2 · s6 2 · s7 1 · s8 2 · s9 1.

## Artifacts
- `vault/videos/good-debt-vs-bad-debt/storyboard-hi.md`
- `studio/videos/good-debt-vs-bad-debt-hi/assets/img/manifest.json`
