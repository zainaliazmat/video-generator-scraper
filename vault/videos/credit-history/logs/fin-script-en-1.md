# fin-script log — credit-history, cut `en`, attempt 1 (2026-07-29)

## What I read

1. `vault/CLAUDE.md` — two-home rule, session protocol.
2. `tools/format.json` — `cuts.en`: 15.0 chars/s, Brian `nPczCjzI2devNBz1zQrb`,
   forbidden currency = the India glyph; `tiers.short` = blockframe-9, 9 lines,
   default 165s; `layout` caps (3 chips/row, 22 chars/chip, ≤6 elements,
   `photo_free_scene_ratio` 0, `keyword_images` true); `scene` 0.4/1.0 lead-tail.
3. `vault/videos/credit-history/facts-staging.md` — the **USD SET only**, plus the
   RED FLAG section (read first, it governs this topic).
4. `vault/skills/long_form_scripting.md` — hook jobs, ~70% reward beat, densest-scene
   handling, deliverable shape.
5. `vault/knowledge/us-english-script-style.md` — rule zero (rewrite, never translate),
   register, photo-sweep rule.
6. `vault/knowledge/design-finance-blockframe.md` — colour roles, tint ladder, motion
   rules, imagery §7 (no phone-screen bg, no repeated image, no faces).
7. `vault/videos/credit-history/script-hi.md` — **structure only** (blockframe-9 beat
   order, scene-note shape). No content, no figure, no image keyword reused.
8. `vault/videos/credit-history/audit-hi.md` — to learn what gate-one actually checks
   (hook-payoff clock, chip length, currency scan, VO digit hygiene, persona grep).
9. `vault/videos/good-debt-vs-bad-debt/script-en.md` + `pay-yourself-first/script-en.md`
   — the two shipped en cuts, for register and burned image keywords.
10. `tools/pipeline_check.py :113 check_script` — confirmed the currency check is a
    **whole-file substring scan**, so the India glyph may not appear anywhere in the
    file, not even in a claim ID. India claims are cited as `Claim IN-…`-free prose and
    the USD claims as `Claim USD-n`.

**Study note absent.** `vault/knowledge/video-studies/credit-history.md` does not exist
(fin-research was rescued for exactly this — `run.json` records it). Retention shape is
therefore inherited from the two shipped en cuts, same as the hi cut did. Recorded, not
worked around.

## The decision that shaped this cut

facts-staging opens with a RED FLAG saying the hero question — *how long does a miss stay
visible* — **has structurally different answers in the two markets**, and that the internet
claims they're the same. So this is not a market-swap of the Hindi script; it is a different
argument built on a different, stronger statute:

| | hi cut | en cut |
|---|---|---|
| Hero | 36-month rolling DPD grid (SOFT-ish, CIBIL only) | **7 years, FCRA §1681c(a)** (HARD — statute + CFPB, both read directly) |
| Factors | ranked, **no weights** (CIBIL publishes none) | **35% + 30% = 65%** (myFICO + Federal Reserve) |
| Money beat | ~1 point on a home loan | **~3× the rate on a used-car loan** |
| Hero visual | 36-cell month grid | **7-year timeline with a mark that clears at year seven** |

Nothing crossed the line in either direction. The mirror guard is written into the file:
the hi script may never say "seven years"; this one may never say "thirty-six months".

## The second decision — what got left out

The hero rule is HARD and the money beat is deliberately fuzzy, because staging says so:

- **No decimal APR, no quarter label.** Staging records a **three-way conflict** on the
  super-prime rate (three values, all attributed to Experian) *and* a table whose own label
  contradicts its article's quarter. Only the shape is HARD, so VO and screen carry rounded
  bands (`~6%` / `~19%`) and the "about three times" framing, which is Experian's own.
  19.42 ÷ 6.30 = 3.08, so the multiple and the modelled pair agree.
- **No free-report claim.** The USD SET has no line for it. The Hindi cut's annual-free-report
  right is an *India* regulator claim and does not transfer, so en8 says "pull up your credit
  report" with no cost and no frequency. This is the one place a translator would have
  silently imported a foreign right; contract rule held instead.
- **No average-FICO 714** (SOFT, fetch timed out, staging says writer context only).
- **No 15/10/10 weight tail** (SOFT-adjacent, single-sourced). The en4 foot says other
  factors count without asserting a weight.

## Numbers

- Segments: **9** (blockframe-9, short tier — hook · roadmap · concept · rule · audit ·
  action · the math · do-this-today · recap+CTA).
- VO chars: **2,595** vs the 165 × 15.0 = **2,475** budget → **+4.8%**, inside the ±10%
  band (2,228–2,723).
- Est. VO **~173s** (target 165s, +8s); rendered **~186s** with 9 × 1.4s lead-in/tail —
  inside the short tier's 60–300s range.
- Trim lever if the measured TTS runs long: **en7** (the only scene over 25s) — drop
  "Same car, same price, two different scores."; keep "Same car. Different number."
- Hook payoff: the report is named at **189 chars ≈ 13.0s** including lead-in. ~2s margin
  to the 15s gate; build advisory written into the scene.

## Self-checks run before returning

| Check | Result |
|---|---|
| Currency purity (whole-file scan for the India glyph) | **clean** — the glyph appears nowhere; the words "rupee", "lakh", "CIBIL", "thirty-six" appear only inside the guard blockquote and the deliberately-NOT-used table, the same pattern the hi audit blessed |
| Bare Latin digits inside VO paragraphs | **none** — every figure spelled out (seven, ten, three hundred, eight hundred fifty, six hundred seventy, thirty-five, thirty, sixty-five, twenty-five-thousand-dollar, six-year, six, nineteen, three, a hundred seventy, twelve thousand four hundred) |
| Every number traces to a staging line | **yes** — 17-row fact-trace table; the only non-staging items are the two behavioural actions from `run.json` and they carry no figure |
| Persona | no first person anywhere, no credential claim, no card/loan/bureau/monitoring pick; FICO is terminology, Experian/CFPB/FCRA are foot-level source evidence, no lender named |
| Chip lengths ≤22 | en2 `WHY IT MATTERS EARLY` (20) is the longest; en9 longest is `WEAK SCORE = 3× RATE` (20) — the hi audit failed two 23-char chips, so these were counted, not eyeballed |
| Chips per row ≤3 | en2 and en9 are 2×2 |
| One focal per scene | en5's timeline is the focal; the correction block reveals *after* the mark lands (handoff #6) |
| Every scene has an image | 9/9 bg keywords + 8 cut-ins; no keyword collides with the hi cut's list or the two shipped en cuts' burned set |
| No rupee/India imagery, no phone-screen bg, no face | en9 closes on an empty highway, not the young-man-with-phone shot both shipped en cuts used |

## Handed to the next stage

fin-audit should independently re-fetch: §1681c(a) via Cornell LII and the CFPB
"how long does negative information stay" page (both were readable for fin-facts), myFICO's
weights page, and the Experian tier table. The one number worth a hard look is **$12,400** —
it is a difference of two model outputs, so a small change in either APR moves it; handoff
#5 tells the build stage to regenerate all four dollar figures rather than trust the script.
