---
summary: Targeted two-cut repair of s65/s66 after the creator killed the four-group flat-lay. s65 becomes money-on-an-open-ruled-ledger (top down, dark wood, per market); s66 keeps the hold and crops to the ledger's own ruled column headings — a crop target that exists in the frame. Two image slots respecced, no new files, no timing/VO/cue changes.
updated: 2026-08-01
source: creator decision 2026-08-01 · script-hi.md / script-en.md lines 6.7–6.8 (recorded, unchanged) · timing.json (both cuts) · logs/fin-assets-hi-1.md + logs/fin-assets-en-3.md · knowledge/design-finance-blockframe.md · knowledge/stock-photo-sourcing.md · tools/format.json
stage: fin-storyboard, cuts hi + en, recut attempt 2 (partial — s65/s66 only)
---

# fin-storyboard — s65/s66 recut, both cuts

## The decision I was handed

The four-group / four-label rupee (and dollar) flat-lay **does not exist and will not be
made**. fin-assets read ~24 candidate cells across both cuts: no cell has four distinct
groups; none has a handwritten label. There is no image-generation route in this project, so
*"draw this yourself if you can't do so Recut"* resolves to **recut**. The hi fallback on
disk is honest but weak (₹500 fan); the en fallback is unshippable (mean lum 212, near-white,
full-bleed RAIL OFF, 14.217s on screen, and 6.8's crop has nothing to land on).

## What I changed

**s65 (both cuts) — the photograph is now money lying on an open ruled ledger, top down, on
dark wood.** One file, unchanged mechanics: RAIL OFF full-bleed, `--warn`, the `stamp`
(456.92 hi / 436.08 en), the outgoing half of the s65→s66 hold.

**s66 (both cuts) — the crop target changed from "one handwritten label" to "the ledger's own
ruled column headings."** That is the only edit s66 needed, and it is the whole point: 6.8
says *her own expense headings were different ones*, so a push-in on a set of headings that
is visibly not NEEDS/WANTS/CULTURE/UNEXPECTED **is** the line. The old spec asked the crop to
find a label that was never going to be in any photograph.

## The three calls, with reasons

1. **Not four objects, not a four-part sequence.** 6.7 *disowns* the four categories.
   Revealing them one at a time as the VO names them is the picture arguing for the thing the
   sentence takes away (design-finance-blockframe §7, "check what the picture is saying").
   And any query demanding *exactly four* of something repeats the sourcing failure this
   recut exists to end. The type carries the four; the photograph carries the ledger.
2. **The hold survives — and this is why I did not give s66 its own file.** The brief allowed
   a real second photograph for s66. Taking it would break the hold, and a broken hold forces
   `ken` to alternate again from s66 onward, **flipping the direction column of every
   remaining scene** in §7 of both storyboards (a hold repeats a direction; removing one
   shifts parity to the end of the cut). That is a 26-row cascade edit in a targeted repair.
   A hold is a mechanical device — one file, two framings — and nothing in it ever depended
   on what the photograph depicted. What was broken was the *crop target*, and that is fixed
   directly.
3. **Sourceability over composition.** "Ledger + cash, top down" is a stock-photography
   staple in both markets (bookkeeping frames); "four labelled groups" is not. Per
   `stock-photo-sourcing.md` this is the object-led rung, not the India-with-people rung.

## Acceptance criteria I wrote into both storyboards (§12.1)

Top-down with the book open · correct current-series currency, distinct serials, no prop
money · **mean luminance ≤140** (this is the failure that killed the en file: 212 under light
type on a full-bleed frame) · a band of ruled column headings present and legible *as
writing* · no Devanagari, no Japanese script (romaji-only sign-off; the 97-codepoint subset
has no Devanagari), and for en no non-US market signal.

Each cut carries a **three-rung retry ladder** so fin-assets never has to escalate again:
ledger+money → ledger alone (s65 then leaves the currency-slot list in §9) → money alone on a
dark surface (s66's crop degrades to one note's printed panel; the log must say so). The
ladders differ at rung 3 by design: **hi rung 3 is the file already on disk** (zero fetch, it
is honest); **en rung 3 is still a fetch**, because its on-disk file cannot ship.

## Image slots to send fin-assets after

| cut | slot | rung-1 query | notes |
|---|---|---|---|
| **hi** | `s65.jpg` | `indian rupee notes lying on an open ruled account book top down on a dark wooden table@pexels` | ≥1880px (RAIL OFF), current stone-grey ₹500 only, lum ≤140, headings band required |
| **en** | `s65.jpg` | `us dollar bills lying on an open ruled accounting ledger top down on a dark wooden table@pexels` | ≥1880px (RAIL OFF), current Federal Reserve notes, lum ≤140, headings band required. **Must re-fetch — the file on disk does not ship** |

**`s66` needs no file in either cut.** It is the incoming half of a hold and uses a tighter
crop of `s65.jpg`; a second file there would be a second photograph, which is the one thing a
hold forbids. Counts are unchanged: hi 97 slots / 94 files, en 96 slots / 93 files, manifests
same size — only the `s65.jpg` query string moved in each.

## Vector art: none added, deliberately

A four-square icon on s65 would carry "the four categories" without asking stock for four of
anything. Rejected: s65 already spends cue slot 7 on its `foot` (the sourcing caveat, which
is the fact-honesty of the beat), so an icon would need a new offset in the §4 cue ladder,
and §8 would gain a seventh icon for the one scene that *disowns* what the icon draws.
Recorded in `storyboard-hi.md` §8 and cross-referenced from `storyboard-en.md` §8. No emoji.

## What I did NOT touch

VO (recorded, unchanged), `timing.json`, every `start`/`dur`, the cue ladder, SFX cue list
and count, the colour semantics, the transitions table, the RAIL OFF set, the file counts,
and all 90 other scenes. Beyond the two rows and §12.1 the only edits were: the `stage:`
frontmatter line in each file (traceability), one clause added to each §9 currency-slot list
naming the rung-2 case, one paragraph in hi §8 (the icon decision) with a one-line pointer in
en §8, and **en §11 divergence D24**, which asserted the now-dead flat-lay spec and would
otherwise have documented a photograph nobody is going to fetch.

**Not flagged:** the `bed-resolve` 248s loop hazard in §2 of both files. Per the stage brief
that is not a decision (mix.py laps the bed with a 3s acrossfade); I left the existing notes
alone because rewriting them is outside this repair's scope, but they should not be
re-escalated.

## Handoff

`fin-assets`, two slots, both `s65.jpg`. Read every promoted cell at **full resolution**
before accepting, and record which ladder rung landed — s66's framing note in §7 is only
correct at rungs 1 and 2, and rung 3 obliges a line in the assets log.
