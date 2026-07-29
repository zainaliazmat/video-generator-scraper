---
summary: fin-storyboard for credit-history en, attempt 1. 9 scenes / 17 image slots (9 bg + 8 cut-ins), every keyframe derived from the measured timing.json (173.227s), all three audit advisories closed in-file, all 9 scenes carry a declared divergence from the hi master skeleton.
updated: 2026-07-29
source: script-en.md (post-audit-edit) + studio/videos/credit-history-en/assets/voice/timing.json (measured) + knowledge/design-finance-blockframe.md + templates/storyboard-template-finance.md + storyboard-hi.md (master skeleton) + audit-en.md + logs/fin-voice-en-1.md + logs/fin-assets-hi-1.md
---

# fin-storyboard — credit-history / en / attempt 1

STATUS: ok

## Artifacts

- `vault/videos/credit-history/storyboard-en.md`
- `studio/videos/credit-history-en/assets/img/manifest.json` — 17 keys

## Colour table (derived from THIS video's thesis, not ported)

| Token | This video | Not |
|---|---|---|
| `--fund` green | on-time payment · low balance · clean report · **top credit tier** · auto-pay | — |
| `--warn` red | the missed payment and the price it charges — the year-zero mark, the subprime row, `$172`/`$12,400`, the bankruptcy chip | never "a credit card", never the score itself |
| `--target` amber | the report/score **under examination** — `YOUR CREDIT REPORT`, the 300–850 scale | not a verdict |
| `--pop` orange | CTA (fixed) | — |

Two inversions explicitly refused in the file: `needs-vs-wants` (amber = wants) and
`good-debt-vs-bad-debt` (red = the minimum payment). Consequence recorded on s6:
`#s6u2`'s "not the minimum" renders **`--muted`**, not `--warn`.

## Timing — measured only

Every offset is `0.4 + chars_before/total × measured clip`, computed against
`timing.json`, with the char position of the anchor word printed in each cue row.
The script's paced estimates were not used anywhere.

The scene fin-voice flagged: **en5 = 18.798s scene / 17.398s clip**, not the ~21.7s the
script paced. Its 16-cue table was written from scratch — mark slam at +4.2, fill
+4.6→+15.5, correction block +11.2/+13.9, mark clears at +15.5 — rather than scaled from
the hi cut's 20.940s equivalent.

## The three audit advisories — closed in-file

1. **`≤6` at risk in en5 and en7.** Both are now sequenced with declared exits. Measured
   peaks: en5 **6** (three exits: kicker +6.0, cut-in +8.2, chip +12.6 — without them the
   scene sits at 8), en7 **5** (three exit waves at +11.0, +17.6, +24.9 — without them it
   sits at 10). Whole-video peaks: s1 5 · s2 6 · s3 5 · s4 5 · s5 6 · s6 3 · s7 5 · s8 5 · s9 5.
2. **Undeclared reveal gaps in en1, en7, en8.** Resolved by anchoring rather than by
   declaring cascades. en1's decision strip: 2.4 / 1.6s. en7's reveal rows: 2.8s. en8's
   two numbered blocks: 4.7s. **No cascade is declared anywhere in the cut** — the
   script's en4 0.6s cascade and the hi skeleton's s3/s6 0.7s cascades are all retired,
   because Brian spaces every one of those groups ≥0.8s in the measured read. Every
   reveal gap in the file is printed in its scene block.
3. **The FICO-band-next-to-Experian-APR ban.** Written into s7 as a boxed STANDING BAN
   and into the sign-off. `#s7band1`/`#s7band2` name the tiers in words only
   (`TOP CREDIT TIER`, `SUBPRIME`) — no `781+`, no `670`, no scale numeral in copy, foot
   or image. `#s3g1`'s `670+` is 78s earlier and never co-present. Related: `#s3g2` is
   **deleted** (the audit killed `upper 700s = best offers`, whose only tier evidence was
   the same VantageScore grid).

## Manifest queries — 1 to 3 nouns

Direct application of `fin-assets-hi-1.md`: the hi cut's 6-to-9-word queries landed 5 of
17 in round 1; one strong noun recovered 9 of 12 on retry. All 17 queries here are 1–2
words. The storyboard keeps a "must show / must not" column as the acceptance test so the
descriptive intent is not lost with the long string.

Two substitutions made from the hi run's measured traps:
- `s4-cut` is **`leather wallet`**, not "credit cards" — both hi attempts returned
  `MasterCard`×4 + `Payoneer` legible.
- `s7-cut` is **`car dealership`** with an explicit non-US plate/signage/RHD sweep.

Five collision risks named with hashes against `credit-history-hi` (`s4` vs `bb2ac44c`,
`s7` vs `a43e2d5b`, `s6-cut` vs `5153cf85`, `s8-cut` vs `5b0a0e72`, `s1` vs `14bc6463`),
two with fallback queries.

## Divergence list — all 9 scenes

IDs ported verbatim where the element is the same in kind. New IDs only where it is not:
`#s5track`, `#s5mark`, `#s5fix1/2`, `#s4q`. Deleted: `#s3g2`, `#s4r3`, `#s4r4`, `#s5grid`,
`#s5q`, `#s8free`. Largest divergences: **s4** (FICO publishes weights, CIBIL does not —
4 weightless ranked rows become 2 proportional bars + a `65%` punch, and the hi foot's
guard is inverted), **s5** (36-cell grid → 7-tick track, new correction block, hero
retimed into 2.9s less than planned), **s7** (full US auto-loan model, third exit wave,
cut-in re-anchored out of the dense window), **s8** (`#s8free` deleted — no US
free-report source exists in the USD SET).

## Notes for the next stage (assets, then build)

- A cut-in may be dropped rather than faked; a **background may not** —
  `photo_free_scene_ratio` is 0, no exception. If a cut-in drops, remove its cue row; all
  simultaneous counts only decrease.
- `×` (U+00D7) in `#s9d` is unverified against the font subset. Check with fontTools; if
  absent render `3x RATE` (chip stays 20 chars). Do not swap the font.
- s7's four dollar integers are calculator output. Round each payment before subtracting
  ($590 − $418 = $172) — rounding the difference prints $173 and disagrees with the screen.
- s1's ≤15s hook gate clears by ≈3.4s (naming at ≈+11.6 on a 14.707s clip); the on-screen
  payoff at +3.0 is independent of delivery rate. Whisper re-check is a formality.
