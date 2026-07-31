---
summary: Targeted fix pass on the six frames fin-render gate two rejected on the hi cut — five wrong-currency picks and one flat-black grade failure. All six replaced with Indian-currency or currency-neutral sources, every candidate inspected at full resolution, md5 clean across all projects.
updated: 2026-07-31
source: pixabay contact sheets + full-resolution inspection of every promoted pick; md5sum over studio/videos/*/assets/img/*.jpg
stage: fin-assets, cut hi, attempt 2 — targeted fix pass (6 of 86 slots)
---

# fin-assets — «पहला एक लाख» hi, attempt 2 — 6/6 replaced, PASS

Scope was six slots. The other 80 were not touched: not re-queried, not re-fetched,
their bytes and their ledger hashes are unchanged.

## What shipped

| slot | on-screen line | new image | source | why it clears |
|---|---|---|---|---|
| **s1** (hook, 11.7s) | THE FIRST LAKH · 20 MONTHS / THE TENTH LAKH · 7 MONTHS | four rolled banknotes — **₹10 / ₹20 / ₹50 / ₹100**, red serials, RBI seals, black ground | pixabay 4508838, rupixen | ₹ symbols large and legible on all four; none of these denominations was ever demonetised; black ground suits the hook's stacked type; ascending denominations read as "growing" |
| **s12** | ₹60,000 | tall stack of mixed coins on white, no legible mark anywhere | pixabay 7702613, F1Digitals | currency-**neutral** — zero text, zero denomination, zero country in frame, so nothing to contradict ₹ |
| **s17** | WHAT THE MARKET BOUGHT YOU / 2 MONTHS | hourglass, pink sand, standing on open **newsprint** | pixabay 620397, Nile | see grade note below |
| **s34** | how much of each month's income leaves and stays out | a hand offering a folded wad of **₹10** notes, dark ground | pixabay 2459328, pprasantasahooo | ₹10 legible, "OF INDIA" legible, nothing else; a hand *paying out* is the VO's "leaves" |
| **s79** | **₹1,500 works. ₹500 works.** | a single coin held in fingers, **RESERVE BANK OF INDIA · PLATINUM JUBILEE 1935–2010** struck around the rim | pixabay 5206872, ElenzaPhotograhy | the scene is about the *amount*, so the coin is the subject — and the only text on it is RBI's own |
| **s81** (RECAP ONE) | The first lakh: 100% you | close pile of **₹5** coins — "5 RUPEES 2010", "₹5", "INDIA", Ashoka capital | pixabay 4395478, rupixen | unambiguously Indian at any zoom; warm brass texture, no faces, no brands |

## The grade failure (s17)

Gate two measured `YAVG = 16.03` (the video black floor) over the un-toned right region
`767×900+1153+180`, held 8.4s. Cause was the source, not the CSS: the old Pexels hourglass
was low-key on the right and `grayscale(.32) brightness(.62)` crushed it.

The replacement inverts the problem — the right half is open newsprint at roughly 225–235
luminance with one out-of-focus grey photo block around 110–130. After the system grade that
lands near 140 and 70 respectively, i.e. **no pixel anywhere near the 16 floor**, and in the
same band as the frames that already passed (`s33` 90.0, `s84` 89.3).

**No per-scene `filter:` override is written, and none is needed.** fin-build's one permitted
override is still spent on `s46 brightness(1.40)` and stays there — the cap is not exceeded.

Keyword fit is better than the old asset's too: an hourglass standing on financial newsprint
under "what the market bought you / 2 months" is time-against-market, not a generic hourglass.
The newsprint body text is genuinely out of focus and carries no masthead or brand.

## Rejected, and why — this is where the pass earned its keep

Contact sheets ran first (`--candidates 6`, one API search per slot), then **every promoted
pick was read at full resolution before it was accepted**. Three rejections were invisible at
contact-sheet size and would have shipped:

- **`indian rupee coins stack` cell 4** (pixabay 4395523) — was my first choice for the hook.
  At grid size it reads as a clean fan of ₹ notes over Indian coins. At full resolution the
  note is olive-green with **`पाँच`** ("five") visible at the cropped bottom-left corner and no
  denomination otherwise legible → almost certainly the **pre-2016 ₹500**, the demonetised
  series. Rejected. This is the exact trap the sourcing note warns about, and it is exactly the
  kind of thing a thumbnail hides.
- **`indian rupee notes hand` cell 2** (pixabay 3887566) — a ledger/diary + pen + spread cash,
  a near-perfect keyword match for s34, and I wanted it. Full resolution shows a ₹2000 and a
  new ₹50 *alongside* several **green ₹500s** (old series), plus a phone body in frame.
  Mixed-series cash under a ₹ claim is a defect an Indian viewer clocks instantly. Rejected in
  favour of the plain ₹10 wad — less pretty, not wrong.
- **`hourglass white background` cell 2** — a **Minion** figurine behind the glass. A licensed
  character is a brand mark. Rejected.

Also rejected across the six sheets: old-₹500 piles (4395462, several sheets), a ₹500 note
lying on an **Apple laptop keyboard** with `command` legible (4508945), euro / ruble / gold-
hoard coins answering `indian coin macro` (cells 3–6), the pennies jar that caused the original
s81 failure (15727), and a pink hourglass shot with **euro banknotes** stacked on its right
(`hourglass white background` cell 6).

Two contact sheets (`s1`, `s17` first run) rendered only 3 of 6 and 1 of 6 cells — some preview
downloads silently fail and `build_sheet` tiles only what arrived, keeping the true cell numbers
on the labels. Not fatal (the `.json` still lists all six), but it means a sheet can quietly show
you fewer options than you asked for. Worth a look if it recurs.

## md5 — clean

```
md5sum studio/videos/*/assets/img/*.jpg | sort | uniq -w32 -D   → no output
```

179 images across every project on both channels, **zero duplicate hashes**. That covers the
cross-video ledger, this cut's other 80 files, and the 93 files in
`first-lakh-first-thousand-en` (which finished after attempt 1 and shares 30+ subjects). No
re-pick was needed for a collision.

## CREDITS + manifest

`CREDITS.txt` is append-only, so the fix pass left stale lines behind for every slot it
re-fetched. Pruned by hand to **exactly one line per image**: 86 credit lines, 86 `.jpg` files
on disk, one-to-one. Each of the six `.src` sidecars carries the query that actually produced
the file on disk, and `manifest.json` was updated to match those six queries so a later plain
`--manifest` run skips rather than clobbers.

Nothing was dropped: 86 slots in, 86 out, every scene keeps its background.

`assets/img/manifest.fix.json` is the throwaway 6-slot manifest this pass drove the fetcher
with. Like `_cand/` it is not referenced by `index.html`, not read by `pipeline_check` (which
resolves `manifest.json` by exact name), and not archived. Post-delivery cleanup reclaims both.
