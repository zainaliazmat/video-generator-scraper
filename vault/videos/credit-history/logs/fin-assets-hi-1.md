---
summary: Gate ③ stock-asset pass for credit-history hi — 14 images accepted (9 bg + 5 cut-ins), 3 cut-ins dropped (s3-cut, s4-cut, s6-cut) after the retry ladder failed; 20 fetches rejected on look or hash across 4 rounds. Every scene keeps its bg photo.
updated: 2026-07-29
source: pixabay_fetch.py runs against studio/videos/credit-history-hi/assets/img/manifest.json; every image opened with Read; md5 ledger over studio/videos/*/assets/img/*.jpg (both channels)
---

# fin-assets — credit-history · hi · attempt 1

**Result: 14 accepted / 20 rejected across 4 fetch rounds. 3 cut-ins dropped.**
All 9 backgrounds ship (creator rule 2026-07-28 held — no photo-free scene).

## The finding that drove this run

**Over-specified queries lose to Pixabay's loose token match.** Every one of the
storyboard's 6-to-9-word queries ("torn paper calendar page on a dark surface",
"architectural blueprint paper texture close up") fell back to whatever matched a
single weak token — `paper`, `book`, `page` — and returned generic book/flower
stock. Round 1 landed **5 of 17**.

Shortening to the one strong noun (`blueprint`, `accounting ledger`, `calendar`,
`pocket watch`, `document`, `old documents`) landed **9 of 12 retries** and produced
the best images in the set. This is the opposite of the retry knob the tool
documents: `#N` on a bad long query only returns more of the same wrong thing,
because the query — not the ranking — is what's broken.

**Recommendation for the storyboard stage: write manifest queries as 1–3 nouns.**
The long descriptive phrasing reads well in the storyboard table but is actively
harmful as a search string.

## Accepted (14)

| slot | final query | what it is | hash |
|---|---|---|---|
| `s1.jpg` | rows of archive files on shelves dark | archive box-file shelves receding | `14bc6463` |
| `s1-cutA.jpg` | manila folder | 3 lever-arch box files, shelf | `3032e620` |
| `s1-cutB.jpg` | bank loan application form with a pen | printed form + ballpoint | `20b66b86` |
| `s2.jpg` | old documents | handwritten letters tied with twine | `0c6881c7` |
| `s3.jpg` | accounting ledger | handwritten ruled ledger, blue/red columns | `5ad798b7` |
| `s4.jpg` | open desk diary with a pen on dark wood | ruled notebook + fountain pen + cup | `29c20073` |
| `s5.jpg` | red rubber stamp and ink pad on a wooden desk | wooden stamp on a stamped sheet | `da06090b` |
| `s5-cut.jpg` | calendar | month date-grid close-up | `bb2ac44c` |
| `s6.jpg` | pocket watch | exposed pocket-watch movement on wood | `5153cf85` |
| `s7.jpg` | blueprint | architectural floor plan + pen + ruler | `c049a9d0` |
| `s7-cut.jpg` | house key | keyring of door keys (+ fob — see note) | `a43e2d5b` |
| `s8.jpg` | document | white document + fountain pen on black | `7b4bfa43` |
| `s8-cut.jpg` | pen ticking boxes on a paper checklist | ticked + empty checkbox, pen | `5b0a0e72` |
| `s9.jpg` | open door sunlight | open doorway into a sunlit garden room | `8af12274` |

Three upgrades on the storyboard's intent, not just recoveries:
- **`s3`** is a genuine handwritten accounting ledger with ruled columns and figures —
  exactly "the record at the bureau", far better than round 1's printed book.
- **`s6`** is the bare pocket-watch *movement*, not a dial. Zero brand surface (the
  rejected round-1 watch had `U-BOAT` legible dead centre) and the visible clockwork
  reads as "a system that runs without you" — which is the auto-pay thesis.
- **`s7`** is monochrome line-work on white: the quietest image in the set, under the
  densest scene, exactly as the storyboard asked.

## Dropped cut-ins (3) — scene keeps its bg

Authority: a cut-in may be dropped rather than faked; a background may not.

- **`s3-cut`** («तीन अंकों का एक नंबर»). Four queries, four misses: German legal book +
  glasses → `ADMIT ONE` raffle tickets with **`Office DEPOT®` legible** → a yellow road
  marking. **Dropped on merit, not just failure:** the scene's focal `#s3scale`
  ("300 ├──┤ 900") *is* the three-digit number rendered as type. A second number-object
  would compete with the focal the storyboard is careful to keep singular.
- **`s4-cut`** («लिमिट का कितना हिस्सा»). `credit cards` and `credit card mockup` both
  return the same shot: five cards in a jeans pocket with **`MasterCard` legible ×4**
  plus `Payoneer`. Pixabay's credit-card library is the brand minefield §7 describes;
  there is no unbranded top hit to walk to. Dropping also helps — s4 is the 4-row
  ladder, the densest scene, and the storyboard wants it calm.
- **`s6-cut`** («ड्यू डेट … लगा दीजिए»). `bank passbook` and `bank book` both returned
  lilacs on a novel — and that image is **byte-identical to `needs-vs-wants/s1-bill.jpg`**
  (`afa1c940`), already shipped. Passbooks effectively don't exist on Pixabay. The
  reminder beat is already carried by `#s6flow`'s text and the pocket-watch bg.

### What the build must change

The storyboard's cue tables still reference these IDs. Remove:

- **s3** — cue 10 (`#s3cut` fade at +12.7); drop `#s3cut` from cue 12's exit list.
- **s4** — cue 4 (`#s4cut` at +10.0); drop `#s4cut` from cue 5's exit. The storyboard
  notes this cut-in filled the 6.0s r2→r3 window; `ken OUT` is continuous so §5.2 still
  holds, but if the build wants a beat there, use a `pulse` on `#s4r2` at ~+10.0 —
  **do not** substitute an unrelated photo.
- **s6** — cue 6 (`#s6cut` at +6.3) and cue 8 (its exit at +9.3).

All simultaneous-element counts only decrease; no cap is at risk.

## Rejected (20) — by trap

**Readable brand marks (3).** `U-BOAT` on the round-1 s6 watch dial; `Office DEPOT®`
on the s3-cut ticket roll; `MasterCard` ×4 + `Payoneer` on both s4-cut attempts.

**Hash collision with a shipped image (3).**
- round-1 `s3-cut` ≡ round-1 `s8` — *within this video*, the same glasses-on-book hit
  for two different queries.
- round-2 `s8` ≡ `50-30-20-rule-en/s7.jpg` (`0d48ed1f`).
- `s6-cut` ≡ `needs-vs-wants/s1-bill.jpg` (`afa1c940`) — hit twice, two queries.

**Keyword miss / generic-pretty (12).** Roses on a novel for "torn calendar page";
lilacs on a novel for "bank passbook"; coin-stacks-with-plants for "bank book";
a blank teal wood panel for "two credit cards"; a colour magazine stack for
"blueprint"; a brass key with daisies for "key in door"; a road marking for "digits".

**Person as subject (1).** Round-1 `s1-cutA` returned a woman with red thread bound
round her fist, face partly in frame — nothing to do with "manila folder", and a
person under a negative-money claim is the Pixabay unflattering-use line.

**Content adjacency (1).** Round-1 `s2` was a stack of **Indian newspapers** with
`BJP hit back` and a rape headline legible, plus a `KBK Infographics` mark and a
Pixabay watermark — as the *calmest* bg slot in the video. Worst single result of the run.

## Ledger check

`md5sum studio/videos/*/assets/img/*.jpg` across **both** channels: all 14 kept hashes
unique. The three storyboard-flagged collision risks were checked by name and are clear:

- **`s5-cut` vs `pay-yourself-first`'s two calendars** (`wall calendar dates close up#2`
  hi / `paper monthly calendar planner desk` en) — no collision.
- **`s4` diary vs `pay-yourself-first`'s `old book pages warm lamp light`** — no collision.
- **`s8` is not a magnifying glass** — the storyboard's substitution held; no collision
  with `good-debt-vs-bad-debt-hi/s5.jpg`.

Stale files for the 3 dropped slots remain on disk (`s3-cut.jpg`, `s4-cut.jpg`,
`s6-cut.jpg` + `.src` sidecars) — unreferenced by the pruned manifest, so inert. Only
`s6-cut.jpg` still shows a collision in a ledger sweep; it is a dead file, not an asset.

`CREDITS.txt` is append-only by design, so it carries one line per *fetch attempt*.
**Every kept image has its line; the last entry per filename is the live one.** Lines
for rejected fetches and the 3 dropped slots are superseded — do not read the file
top-down as the shipping credit list.

## The one filter override (s8)

`s8.jpg` is the only near-black image in the set — roughly 55–60% of the frame is a
pure-black field with the white document on the upper-right diagonal.

It is **not** the failure mode the vault describes (a near-black *texture* going flat
under `brightness(.62)`): the subject here is bright paper, which survives the grade
fine. The risk is the inverse — with the s8 orange tint `.12` plus the four-layer
scrim over a >50% black field, the lower-left goes to a dead wash with no tonality,
and `ken OUT` across a dead field reads as no motion at all (§5.2).

**Set on `#s8 .bg` only:** `filter: grayscale(.32) brightness(.95) contrast(1.05)`.

A gentle lift, deliberately nowhere near `50-30-20-en`'s `brightness(1.45)` — that one
was rescuing charred wood with no bright subject. **Ceiling:** this is a judgement from
looking at the image, not a measured mean-luminance figure (no image tooling on this
stage's allowlist). If the build has ffmpeg to hand, measure it and adjust; if the
paper blows out, come back down toward `.75`. **This is the video's only override —
do not add a second.**

## Residual notes for the build

- **`s7-cut` crop.** The keyring is genuinely flat door keys, but a black car fob sits
  in the right third (the Pixabay page slug is literally `key-car-key-keychain`). Under
  «एक ही घर» / "SAME HOUSE. DIFFERENT NUMBER." that's a soft drift to the wrong asset
  class. **Frame the cut-in on the left two-thirds and crop the fob out.** No brand is
  visible on it either way.
- **`s1-cutB`** carries legible **German** form labels (`Familienname`, `Angaben zum
  Betrieb`). Not a brand and on-keyword (form + pen), so kept — but it is the one kept
  image with foreign-language text a viewer could read. If the build wants it gone,
  crop to the pen and the ruled boxes.
- **High-key set.** `s2`, `s5-cut`, `s7`, `s8-cut` are all bright white images. Under
  `brightness(.62)` they land at a light mid-grey, not the near-black the system usually
  gets. Expect to lean on the scrim rather than the grade for type contrast on those
  scenes — this is a legibility watch item, not a defect.
- **`s9`** is an Irish/European cottage doorway. The storyboard accepted that no slot
  needs to say "India" (the ₹ figures do that), and it matches "sunlit open doorway"
  precisely, including the "door the report opens" reading.

## Sign-off

- [x] Every scene has a full-bleed bg photo (9/9) — photo-free retired
- [x] Every image opened with Read and judged on the measured trap list
- [x] md5 checked across both channels; 14/14 unique
- [x] No brand mark, no face, no phone screen, no `$`, no demonetised note in the kept set
- [x] Every kept image has a CREDITS.txt line
- [x] One filter override, on s8, with its ceiling recorded
- [ ] Build stage removes the 3 dropped cut-in cues (s3 cue 10, s4 cue 4, s6 cues 6+8)
