# fin-assets — pay-yourself-first / en / attempt 1

2026-07-28. 9 slots (s2+s7 photo-free by design, cap 0.23×9≈2 fully used — no drop authority left; all rejects handled by #N retry, none dropped).

## Result: 9/9 accepted, 4 fetches rejected along the way, 0 slots dropped

| Slot | Query (final) | Verdict |
|---|---|---|
| s1-a | empty leather wallet no money#2 | keep — empty-pockets, headless torso, hands+object, no readable brand at grade |
| s1-b | paper monthly calendar planner desk | keep — open ring planner, no brands/faces |
| s1-c | scattered one dollar bills on table#2 | keep — $1 bills, correct currency for en cut |
| s3 | paycheck stub pen calculator desk#4 | keep after 2 retries (see rejects) |
| s4 | antique book open warm candle light#2 | keep — see filter override below |
| s5 | stacked brown cardboard boxes pile | keep — paper-stack texture, calm bg |
| s6 | morning sunlight bedroom alarm clock#2 | keep — clock + coffee beans, "QUARTZ" is generic |
| s8 | piggy bank us dollar bills savings | keep — $1 pile; no piggy bank in frame but reads "savings" as texture; currency correct |
| s9 | new york city skyline sunrise#3 | keep — NYC skyline through bedroom window, no brands |

## Rejected

1. **s3 #2, s4 #1, s6 #1 — md5 duplicates of pay-yourself-first-hi** (74e6113d…, c84d9ea0…, b81682b7…). The hi cut's images entered the ledger this run; byte-identical reuse across both channels is the R-5 mass-production failure. All three re-fetched at next index.
2. **s3 #3 — legible handwritten letter** (pixabay "merry-christmas-pen-handwriting"): readable off-topic handwriting under a paycheck VO line. Rejected, took #4 (calculator + pen + blank paperwork — clean).

## md5 dedupe

Full ledger run over `studio/videos/*/assets/img/*.jpg`; after swaps, all 9 en hashes are unique across every project on both channels. grain.png copied from needs-vs-wants (hash 9f7c8e6b… verified identical) — grain is a shared texture asset, not a stock photo, exempt from the photo dedupe.

## Filter override (the ONE allowed)

**s4** is the near-black frame (candle + book, mean luminance visually ~15–20%; everything outside the candle pool is pure black). The system grade `brightness(.62)` will crush it flat. Build stage must inline on s4's `.bg` only:
`filter: grayscale(.32) brightness(1.4)` (precedent: 50-30-20-en S8 ran 1.45). No other scene needs an override — s6 is dark-warm but its subject is mid-tone, survives .62.

## CREDITS.txt

Append-only history; latest line per slot = kept image. All 9 kept slots verified present (s3→business-calculator-861325, s4→candle-book-1646765, s6→clock-alarm-8592484).
