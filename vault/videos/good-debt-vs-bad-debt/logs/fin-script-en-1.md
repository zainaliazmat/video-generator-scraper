---
slug: good-debt-vs-bad-debt
stage: fin-script
cut: en
attempt: 1
status: ok
updated: 2026-07-28
---

# fin-script — good-debt-vs-bad-debt / en / attempt 1

STATUS: ok. Wrote `vault/videos/good-debt-vs-bad-debt/script-en.md` — the US/English
cut, blockframe-9 (SHORT tier), Brian voice, @moneymavens101. US **rewrite** of the
minimum-payment-trap spine, not a translation of the hi cut (read hi only for structure).

## Hero-math (chosen by fin-script, per orchestrator's en constraints)

- **Balance $6,000** · **APR ~22%** ("illustrative — typical range") · **floor $35**.
- Why $6,000: sits in the typical US revolving band $5,000–$6,000 (facts-staging $ SET),
  and it gives clean, floor-independent month-1 anchors — min **$170** = 1%·6000 ($60) +
  interest ($110). $5,000 gives $141.67/$91.67/$50 (messy). NOT a conversion of the hi
  cut's fifty-thousand-rupee balance; the US "1% + interest" mechanism, not India's "5% of
  total due" (facts-staging Claim $-2, explicitly "do not reuse the rupee math").
- **VO speaks only floor-independent anchors/ranges:** month-1 split ($170/$110/$60),
  "a year barely moves it" (still over $5,000 owed), payoff as a round range ("the better
  part of two decades" / "more in interest than you borrowed" / "over nine thousand").
  **No false-precise floor-dependent integer is spoken.**
- **On-screen build-locked integers** (my reference run, en7 — the build calculator
  regenerates + locks): B₁₂ = 6000·0.99¹² = **$5,318** after 1 year; percentage phase to
  ~$1,235 ≈ 157 mo + flat-$35 tail ≈ 58 mo → **~215 months (~18 yr)**; interest ≈
  **$9,496** (> $6,000 borrowed); total paid ≈ $15,496. Model: P = max(0.01·B + i·B, $35),
  i = 0.0183333, stop at B≤0. Handed to build in the script's Build-handoff #5.

## Budget

- 9 VO segments, **~2,502 chars** → **~2:47 est** VO vs **165s** target (101.1%).
- Band 165 × 15 c/s = 2,475 ±10% (2,228–2,723) → inside. Build ffprobe-measures + adds
  0.4s lead-in / 1.0s tail per scene before locking (script mandates it).

## Hard-rule / compliance checks (self)

- **Currency purity:** grep `₹` = **0** (fixed 7 self-referential glyphs in my own
  "no-rupee" notes → spelled "rupee", the way the hi cut spelled "dollar sign"). `$`
  present (required). No lakh, no India institution, no cross-market figure.
- **Digits spelled in VO:** grep `^> .*[0-9]` hits only the two meta-note blockquotes
  (lines 19-21, 184-186) — **zero digits in the nine VO paragraphs**. On-screen numerals
  carry all figures.
- **Persona:** no host, no first-person expertise (no "I"/"we the experts"), no
  product/card/fund pick. APR/minimum = price evidence only; Fed G.19 / WalletHub /
  Chase / Capital One / CFPB appear only in source foots. "Compounding when you invest"
  is a concept, not an investment pick.
- **Layout (advisory — storyboard owns final):** one focal per scene; chips ≤3/row.
  Chip `GOOD GROWS, BAD DRAINS` (en9) = **22 chars = the limit** (≤22 OK; the hi audit
  flagged only a 23). All other chips well under.

## Flags for downstream

1. **Build (en7):** regenerate the on-screen integers from the $ model above — do not
   treat $5,318 / 215 mo / $9,496 as script constants. en-US grouping.
2. **Assets:** sweep every photo for non-US currency, signage, vehicles (us-english-style
   rule — a foreign coin shipped in the first en cut); no phone-screen photo as a bg
   (design §7 — en6/en8 use phone-banking, keep the screen dim/angled, not the focal).
3. **en6 `+$20`:** effect kept qualitative ("cuts years off"); no fabricated payoff. Build
   can compute a data-backed contrast if wanted (handoff #6).
4. **Studio project** to build: `studio/videos/good-debt-vs-bad-debt-en`.

NEXT: fin-audit-en — independence re-fetch of the ~22% APR (Fed G.19 / WalletHub) and the
US "1% + interest" minimum (Chase / Capital One / CFPB), and re-verify the en7 model math.
