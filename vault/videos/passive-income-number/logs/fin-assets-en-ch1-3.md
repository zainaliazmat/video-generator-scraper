---
summary: en ch1 narrow re-fetch of s3 + s4 only, against the parent's four-part checkable spec. 13 sheets, 78 candidates, 1 accepted — a top-down terrazzo table (cottonbro studio, Pexels 1880) whose black-screen phone is dominant, at 59.8% of frame width, and croppable to 1600x900 with the phone at 53%. All four criteria verified BEFORE promotion by measurement, and afterwards by simulating the cover + inset:-8% + plateKen geometry at all four ken extremes. 0 md5 collisions, `check assets --chapter 1` PASS.
updated: 2026-08-08
source: fin-assets attempt 3, chapter 1, en cut — narrow fix against the parent's resolution override of fin-assets-en-ch1-2.
---

# fin-assets — passive-income-number / en / chapter 1 / attempt 3 (NARROW: s3 + s4)

**PASS `check assets --slug passive-income-number --cut en --chapter 1`.**

**Accepted 1 fetch + 1 derived crop · rejected 77 candidates · dropped 0.**
s1, s2, s5, s6, s7, s8 untouched — mtimes confirm it (02:37–05:13, before this run's
05:30). Only `s3.jpg`, `s4.jpg`, their `.src` sidecars, `CREDITS.txt` and
`manifest.json` were written.

| slot | source | W×H | YHIGH | YAVG | R−B | md5 |
|---|---|---|---|---|---|---|
| **s3** | Pexels · cottonbro studio · `black-iphone-5-beside-white-ceramic-mug-on-white-table-5052863` | **1880×1253** | **209** | 129.7 | +1.8 | `8fa18b3c…` |
| **s4** | derived `crop=1600:900:280:320` of s3 — no fetch, no flip | **1600×900** | **206** | 126.9 | +1.4 | `9657c440…` |

The photograph: a round terrazzo table shot from directly above, dark floor and a green
chair back around it. A black iPhone, whole, screen completely black, low and near-centre.
A hand-thrown stoneware cup of black coffee upper right, a small grey bud vase with a
dried eucalyptus sprig upper left. Off wood. No text, no brand mark, no people, no
currency, no screen glow.

---

## The four criteria, verified before promoting

The parent asked for these to be checked ahead of the fetch rather than argued afterwards.
Each was measured, not eyeballed.

**1 · Pexels `large2x`, not Pixabay.** 1880×1253. ✓

**2 · The phone is dominant, not the mug.** Flood-filled the dark blob at threshold 70 on
a 1/5-scale luma dump: the phone occupies **x 1000–1255, y 580–1075** — 255×495 = **126,225
px² of solid object**. The cup's disc is ≈73,600 px², the vase body ≈41,800 px². The phone
therefore wins on area outright, and wins on contrast by a wider margin still: it is the
only near-black object on a pale ground, so it is the darkest and the largest thing in
frame at once. This is the inverse of the attempt-1 and attempt-2 failures, where the mug
was the mass and the phone was the accessory.

**3 · Roughly centred, not against either edge.** Phone centre **x = 1125 of 1880 = 59.8%**;
its right edge sits **625 px** from the source's right edge. Attempt 2's phone was 26 px
from the edge, which is what made every crop unpayable. There is no such constraint here.

**4 · The s4 crop is ≥1600 px, contains the phone under `.p-d`, and is a true crop.**
`crop=1600:900:280:320` — a straight ffmpeg crop of the promoted s3, no second fetch and no
flip, so §6b's matched-frame hold is intact. In the crop the phone sits at **53.0% of the
width and 56.1% of the height**. Both numbers were solved for, not discovered: x0 = 280 is
the maximum offset a 1600-wide crop allows and it lands the phone nearest centre; y0 = 320
was chosen as the value that keeps the phone's bottom inside the frame at the *tightest*
ken (1.16) while keeping its centre inside the Lottie band's mapped footprint at the
*widest* (1.08).

---

## Verified against what actually ships, not against the raw file

The raw file is not what the viewer sees. `.bg` is `background-size:cover` at `inset:-8%`,
then `plateKen` scales it about its centre — so the on-screen frame is the source scaled by
`k · max(2227.2/W, 1252.8/H)` and centre-cropped to 1920×1080. I reproduced that geometry
exactly and looked at all four extremes:

| frame | scale | verdict |
|---|---|---|
| s3 @ ken 1.00 | 1.185× | table, vase, cup and a whole phone; phone dominant |
| s3 @ ken 1.08 (the cut) | 1.280× | phone whole and dominant — see the one declared deviation |
| s4 @ ken 1.08 (banner lands) | 1.503× | **phone centred at 54% of frame width, unmistakably the subject**; cup and vase base held as partials at the top |
| s4 @ ken 1.16 | 1.615× | phone still whole, still centred, still clear of every edge |

The Lottie stage is `left 550, top 602, 820×300`. Mapped back through that geometry it
covers **crop x 33–67%, y 55–77%** at ken 1.08 — the phone (crop x 45–61%, y 29–84%) sits
inside the banner's x-range entirely, with the banner crossing its middle. That is the beat:
the banner is on the phone, not floating next to a coffee cup.

**The grade was checked too, because this is a pale-surface pick.** Applied
`grayscale(.32) brightness(.62) contrast(1.05)` to the s4 ken-1.08 frame: YHIGH falls
209 → 122, still above the source floor, and the terrazzo reads as a **mid-dark speckled
stone with dense high-frequency aggregate**, not the flat charcoal slab the never-buy-high-key
rule warns about. That rule targets *featureless* white — white marble, paper on paper. A
pale ground carrying thousands of dark specks with a black object on it is the opposite
configuration, and it is the same tonal recipe the incumbent (pale concrete, dark ground,
YHIGH 226) already shipped past the editor.

**Read at full resolution, then zoomed.** Phone at 2.6× and cup at 3.2×: the screen is dead
black with only dust and a smudge on it — **no wordmark, no logo, no icon, no reflection
carrying anything legible**. The cup is unmarked stoneware. Nothing in either frame prints
a character.

---

## Three rounds, 78 candidates, and the genre that owns this query

The pool fought this slot hard. Rounds 1 and 2 were **0 for 48**, and the rejections fell
into three families rather than being scattered misses:

| round | queries | what came back |
|---|---|---|
| 1 | dark stone counter · concrete top view · marble countertop · flat lay on dark | **13 of 24 were white-screen device mockups.** "Smartphone + coffee" is owned by the mockup-template genre, and a blank white screen is the standing rejection wearing a different hat — it is a screen, and it is the brightest thing in frame. Also 3 lit screens, 4 faces, an Apple keyboard |
| 2 | foreground close-up · shallow DoF · stone table morning light · kitchen island | **people in kitchens** (7), lit camera-app screens (4), the same wooden-board red-mug frame three times, a mug reading `GROUNDS CAFE`, a newspaper reading `BURGLARY SHOCK`, a **green-screen** phone, and a wall clock reading `13 10` — a legible figure that also contradicts the kicker `BEFORE NOON` |
| 3 | the incumbent's own shoot title · phone as head noun · `#6` offset · **`still life of…`** · low angle | 29 more rejections and **the one hit** |

**The query that worked, and why.** `still life of a mobile phone and a cup of coffee on a
dark table@pexels`. Two words did the work:

- **`still life`** pulls out of the mockup and lifestyle genres into art photography, where
  the objects are arranged for composition rather than to demo a device. It is the same
  lever as naming a denomination on a currency slot: it names the *genre*, and filtering
  after the fetch is the expensive way to do what the query does free.
- **making the phone the head noun** ("a mobile phone and a cup of coffee", not "coffee with
  a smartphone") is what moved it from accessory to subject. Every round-1 and round-2
  phrasing that led with coffee returned a mug-dominant frame — including three separate
  re-appearances of the incumbent's own family.

The `#6` offset probe was worth running and did **not** help: offsetting past the top hits
returns *more of the same genre*, not a different one. Offset escapes a bad top result;
it does not escape a bad genre. Only re-nouning the query did that.

---

## Declared deviations — three, all stated rather than hidden

**1. At s3's ken 1.08 the phone's bottom rounded corner reaches the frame's bottom edge.**
The last ~10 px of a 590 px on-screen phone, on the final frame of 1.3 — the instant it is
already dissolving into s4, where the phone is fully inside with margin at both ends. It
reads as a complete phone throughout (the home button and chin are visible). It is not
fixable at this stage without either cropping s3 — which would put it under the 1880 px the
parent's criterion 1 requires — or a `background-position: center 40%` override on `#s3-bg`,
which is fin-build's file and fin-build's call. **Flagged for fin-build as optional; not a
blocker.** The alternative was a different photograph, and no other photograph in 78
candidates satisfied criteria 2 and 3 at all.

**2. The cup's top rim is outside s4's crop.** s4 is a *tighter* crop; partial objects at
its edges are what a tighter crop produces. §10's requirement is "the phone lying face-down
beside the mug" — the mug is in frame, plainly a cup of black coffee, and holds the
top-right corner. The ken window would have clipped its top at 1.08 regardless of where the
crop rect sat, so no crop choice was traded away here.

**3. Warmth is +1.8 / +1.4 R−B, below the ~+40 guideline.** Identical in kind and cause to
attempt 2's off-wood picks (−6.0 / −4.3): stone and terrazzo are neutral by construction,
and warm brown wood was the thing supplying warmth in the frames that had it. `R−B` is a
guideline; `pipeline_check` gates `YHIGH` only, and both files clear it with ~96 points of
margin. §11's `--f1:#241d15` ground on both scenes is the mechanism for exactly this, and it
is unchanged. **No new trade was made here** — this is the same accepted trade as attempt 2,
carried forward.

---

## The gates, swept

- **md5 across every image on disk** — 54 jpgs under `studio/videos` + `vault/videos`,
  both cuts and all chapters. The new s3 and s4 hashes are unique. The only three duplicate
  hashes on disk are `renders/SHEET.jpg` ↔ `renders/SHEET-chN.jpg` copies in three projects
  — render contact sheets, not source imagery, and not this stage's files.
- **CREDITS re-keyed in the same move as the pixels.** `s4.jpg`'s row still carried
  attempt 2's photographer (Sheldon Li); it now carries cottonbro studio and the same page
  URL as s3, marked `(derived crop of s3.jpg)`. This is the licence breach the stage brief
  names, and it is the second consecutive attempt in which s4's row had to be re-keyed —
  **any re-derivation of s4 must re-key it again.**
- **`manifest.json` updated in the same move**, both keys: s3's query and s4's crop rect.
  `.src` sidecars likewise. The check's licence assertion reaches both files.
- **No faces, no people, no hands** in either frame.
- **No readable brand mark, no legible figure, no legible text** — verified at 2.6× and 3.2×,
  not just at full frame.
- **No lit screen.** The phone is black, per §10's amended s3/s4 row (approved deviation).
- **No non-US marks, no currency of any kind** in frame.
- **Gate 4, one picture per point.** s1 is a *white* phone on warm bamboo in a hard diagonal
  sunbeam, off-centre left, alone. s3 is a *black* phone on pale terrazzo, overhead, soft
  even light, with a cup and a vase. Different device, surface, light, angle and cast. They
  rhyme as §10's "the morning" family intends; they do not read as one image reused.
- **Wood count unchanged at 3 of 8** (s1, s2, s7 — the three the editor's brief protected).
  The new s3/s4 are terrazzo, so the editor's finding 6 stays answered.

---

## Handoff

- **fin-build:** nothing changes mechanically. s4 is still the §6b hold partner of s3, still
  a derived crop, the Lottie still stages on `.p-d` at `+1.13`, the `buzz` still at `+1.85`.
  What changes is that the banner now lands **on the phone** rather than beside it. One
  optional nudge is offered above (deviation 1) and is fin-build's call, not mine.
- **The cut-level manifest** (`passive-income-number-en/assets/img/manifest.json`) still
  holds attempt 1's queries for s3/s5/s6/s8 and must be re-synced at cut assembly, together
  with s4's CREDITS row. Unchanged standing item from attempts 1 and 2, now one row larger.
- **`_cand/` holds this round's s3 sheet only.** The 12 survey sheets that found it were built
  in a scratch manifest outside the project and are not in `_cand/`; their queries and
  verdicts are tabulated above, which is the durable half.
- **No storyboard edit was needed.** The crop rect lives in `.src` and `manifest.json`, one
  home; the storyboard carries no resolution or crop fact that this run made stale.

## Reusable findings

1. **"Phone + coffee" is a mockup query, not a scene query.** 13 of the first 24 cells were
   blank-white-screen device mockups, and a white mockup screen is the never-a-lit-screen
   rejection in disguise — it is a screen, and it is the brightest thing in frame. The escape
   is `still life of …`: it names the genre, and the genre is what was wrong.
2. **Make the object you need dominant the HEAD NOUN of the query.** Every phrasing that led
   with coffee returned a mug-dominant frame; the phrasing that led with the phone returned
   the phone. Composition follows grammar in a stock index more reliably than it follows
   adjectives — this is the same lesson as naming the denomination on a currency slot, and
   it is cheaper than any amount of post-fetch filtering.
3. **`#N` escapes a bad top hit, never a bad genre.** The offset probe returned six more
   cells of the same three failure families. When a slot fails on genre, re-noun the query;
   do not paginate through it.
4. **Simulate the frame, don't judge the file.** `cover` + `inset:-8%` + `plateKen` is a
   1.18×–1.61× centre-crop that no amount of looking at the raw jpg reveals. Reproducing it
   in four ffmpeg calls turned "is the phone under the band?" from an argument into a
   measurement, and caught the one real edge condition (deviation 1) that a full-resolution
   read alone would have shipped. **The full-resolution read finds what is IN the picture;
   only the simulated frame finds what will still be in the FRAME.**
5. **Give the next attempt numbers, not adjectives.** Attempts 1 and 2 both failed on
   "dominant", which is unfalsifiable at fetch time. The parent's rewrite — 1880 px, phone
   dominant, not against an edge, ≥1600 px crop — is checkable *before* the download, and
   this run's whole method was to check it there. Where a rejected candidate can be measured
   instead of debated, one sheet does the work of three rounds.
