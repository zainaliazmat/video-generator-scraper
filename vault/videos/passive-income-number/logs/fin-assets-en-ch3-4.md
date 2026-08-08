---
summary: en ch3 attempt 4 — the two slots the editor named. s30 (the BLOCKER, the chapter's one drawn layer) is replaced with a shingle roof + three brick chimneys against sky: it names HOUSING with the type covered and gives the 33.4% bar a low-frequency ground, predicted composed median 97.7 / p10 36.1 against the birds-on-a-parapet frame's 62.1 / 12.6. s26 (the scale error) is replaced with a full-frame tyre-tread macro, predicted 85.3 / 8.4 against the aerial car park's 92.6 / 19.5 — one vehicle, not eighty, and the tonal shape of the chapter is unchanged. THE FLOOR DID NOT MOVE: it is still s37 at 20.5, and s26, the longest-held frame at 8.355s, ranks #9 of 16 on median. Payoff s34 still passes all four clauses (median #2, p10 #1, step-in +70.5). 13 contact sheets, 131 cells, 2 accepted; FOUR promoted candidates were killed only at full resolution, including prop money whose Pexels title reads "photo of money". s26 is a declared judgement call — it names a part, not the whole car.
updated: 2026-08-09
source: fin-assets attempt 4, chapter 3, en cut — editor-en-ch3-1 findings 1 and 3; measured on this stage's own reproduction of fin-build's §5 chain.
stage: fin-assets, cut en, chapter 3, attempt 4
---

# fin-assets — passive-income-number / en / chapter 3 / attempt 4

**Accepted 2 · rejected 129 cells over 13 contact sheets · dropped 0 · files replaced 2.**
Only s26 and s30 were touched. The other fourteen photographs are byte-identical to
the ones the editor reviewed — verified by hashing all sixteen.

`python3 tools/pipeline_check.py check assets --slug passive-income-number --cut en
--chapter 3` → **PASS assets-en** (with the flag, so the licence assertion reaches
`assets-ch3/final/`).

---

## 0. The instrument was re-validated before it was trusted

Same discipline as attempt 3, because the brief says predictions have missed the
composed frame on this chapter twice more. Chain: cover-crop to 16:9 at the scene's
`background-position` → the central 86.2% that `inset:-8%` shows → the locked grade
(`grayscale(.32)` is chroma-only; `brightness(.62)` then `contrast(1.05)`) → Rec.601
percentiles. Reproduced against fin-build's §5 table on scenes nobody has touched:

| scene | fin-build | mine | Δ |
|---|---|---|---|
| s24 | 37.7 | 36.6 | −1.1 |
| s25 | 92.0 | 93.9 | +1.9 |
| s28 | 95.7 | 95.8 | +0.1 |
| s34 | 128.1 | 128.3 | +0.2 |
| s35 | 139.2 | 137.9 | −1.3 |
| s37 | 21.6 | 20.5 | −1.1 |
| **outgoing s30** | **59.8** | **62.1** | **+2.3** |

⚠ **These are PREDICTIONS.** On this chapter the encode has come in at roughly
**half** the source-side figure twice (s31 predicted 70.6 → encoded 35.0; s27
predicted 97.0 → encoded 42.0). Ranks survived both times; absolute values did not.
Every number below is source-side. Margins under ~3 points are flagged unsafe.

---

## 1. s30 — THE BLOCKER, REPLACED

`roof of a house with asphalt shingles and a brick chimney against a blue sky@pexels`
· **1880×1253** · Pexels, Gene Samit · `rooftop-with-chimneys-20181619`
· md5 `349b12be…`

A weathered wood-shingle roof running across the lower half, **three brick chimneys**
against a blue sky, a **white clapboard gable end** at frame right, bare winter trees
behind.

| | outgoing (birds on a parapet) | **incoming** |
|---|---|---|
| composed median | 62.1 — 11th of 16 | **97.7 — 5th of 16** |
| p10 | 12.6 — 11th | **36.1 — 5th** |
| p90 − p50 | 16.3 | 18.9 |
| step-in (from s29 58.5) | +3.5 | **+39.2** |

**Sound-off gate: PASS, and it is the whole reason for the swap.** Type covered, the
frame is *the roof of a house* — a pitch, a ridge, chimneys, siding. The editor's
finding was that the outgoing photograph contained **no roof, no pitch, no chimney and
no building form**, so "housing" was absent from the frame that exists to quantify
housing. It is now the literal subject. It is also the editor's own prescription
("a dusk roof pitch with a chimney against sky") executed in daylight, which is what
moved it off a near-black lower band.

**It does not duplicate s29 or s32.** s29 is a wide angled suburban street at dusk with
a lawn, a sidewalk and a brick garage; s32 is a close white clapboard porch with a dark
door. s30 is a single elevation element against sky at a third scale, in flat winter
daylight. Three different scales, three different grounds.

**The drawn layer sits well on it — checked by looking, not only by measuring.** The
`p-b` plate rect (screen x1150–1920, y150–760) and the bar (x1220–1940, y395–515) were
rendered over the composed, graded frame with `.art-lift` approximated: the yellow
0.334 fill lands on darkened sky, and the ghost track's remaining two-thirds crosses
the large chimney, which is a **chunky, low-frequency form**, not competing texture.
Measured inside the bar's own rect: mean 86.4, sd 31.9, p10 35.1, p90 113.3 — a real
two-region ground, and `.art-lift` (which the build already applies for this scene)
darkens all of it before the bar draws.

**Full-resolution read: clean.** No signage, no house number, no maker's plate, no
brand, no people, no text of any kind anywhere in the frame. American colonial
vernacular (wood shakes + brick stacks + clapboard), so place and era match the
currency.

⚠ **One thing for fin-build to watch:** the type band (left 55%, y15–75%) measures
median 104.4 / p90 117.9 — the brightest type ground in the chapter, just above s27's
already-AA-passing 96.0 and s28's 110.5. Precedent says it passes 14/14; precedent is
not a check. **`bgpos` is not worth moving:** center 97.7 / 36.1 / 18.9 · center top
99.1 / 41.0 / 16.8 · center bottom 90.7 / 34.8 / 25.5. `center top` buys +1.4 median,
inside the method's own noise, and costs 2.1 of spread. **Recommend no code change** —
a plain regenerate is enough.

---

## 2. s26 — THE SCALE ERROR, REPLACED · ⚠ DECLARED JUDGEMENT CALL

`close up of a car tyre tread and alloy wheel on a driveway in daylight@pexels`
· **1880×1058** · Pexels, Mike Bird · `car-tire-closeup-photo-116676`
· md5 `09196f6b…`

A full-frame macro of one **worn tyre standing on speckled asphalt**, tread face filling
the frame, shadow at right.

| | outgoing (aerial car park, ~80 cars) | **incoming** |
|---|---|---|
| composed median | 92.6 — 7th of 16 | **85.3 — 9th of 16** |
| p10 | 19.5 — 9th | **8.4 — 12th** |
| p90 − p50 | 32.6 | 25.3 |
| step-in (from s25 93.9) | −1.3 | −8.6 |

**The scale error is fixed at the root.** The editor's objection was that a drone shot
of eighty cars silently re-scales a claim about *one* car's running cost. One tyre is
one vehicle and cannot be read as a fleet.

**Sound-off gate: PASS on the letter, weakly.** Type covered, a viewer names a concrete
object — *a worn tyre* — and the object is automotive, one of a set of four, and the
one part of a car that visibly wears out and gets bought again. **What it does not do
is name the whole car**: read alone it says "a tyre", not "the monthly cost of the car
outside". That is the declared call, and the editor should rule on it rather than have
it argued past them. Three things carry it in context: it is the third beat of a
four-scene car run (street → nozzle → tyre → door handle), the kicker reads **PER
MONTH**, and the build's own note already records that **the four chips are load-bearing
copy for this exact reason** — the storyboard's "four slips on a dashboard" frame was
unbuyable at attempt 1 and the cascade was promoted to carry the enumeration.

**It is the right ground for archetype D.** s26 is the chapter's second-heaviest type
frame: a 112px `$1,110` focal, a `brule` at 400 and a four-chip 2×2 cascade at measured
word onsets. §10 routes heavy-type frames to the quietest photograph. The chip band
(y55–85%) measures median 86.7 / p10 9.1 — even, mid-bright and with no countable
subject to fight four chips arriving one at a time. That is the same property the build
credited the outgoing aerial with, kept, minus the scale error.

**Full-resolution read: clean.** No sidewall text in frame, no tread-wear code, no
brand, no plate, no signage, no location cue, no currency. The source is already 16:9
(1880×1058), so **`bgpos` is a no-op on this slot** — there is zero crop slack in either
axis. fin-build should not spend a knob on it.

**Tonally it changes nothing that matters.** #9 on median against the outgoing's #7,
p10 8.4 against 19.5. It is **not** the floor (s37 20.5, s24 36.6, s36 50.3 and s33 57.8
all sit below it on median), which matters because s26 **is** the chapter's longest-held
frame at 8.355s and the stopping rule makes a relocated floor a defect exactly there.

---

## 3. What was rejected, and why — the ledger

**13 sheets, 131 cells, 2 accepted.** The s26 slot took 12 distinct queries; that is
recorded here so the next chapter does not re-pay for it.

### Rejected at full resolution, after being promoted (4 of 6 promotions)

| slot | candidate | killed by |
|---|---|---|
| s26 | key fob + calculator + dollar bills | **PROP MONEY.** Three notes in one frame carry the serial **`E 74116815 B`**, and the Pexels title itself reads *"car keys and calculator on the **photo of money**"*. Invisible at contact-sheet size by construction — spotting it needs two serials legible in one frame |
| s26 | white SUV on a two-post lift | **`SUBARU`** on the tailgate, **`Forester`** script beneath it, **`BRIDGESTONE`** on the sidewall — three readable brand marks |
| s26 | one car in a bright body shop | **`SKODA`** (a marque not sold in the US — a place error as well as a brand mark), plus **`WÜRTH`** on the hose reel and **`MIRKA`** on the extractor |
| s30 | brick tenements with fire escapes | not a text kill — a **measured** one: composed median **31.9 / p10 3.5**, which would have made the frame carrying the chapter's ONE drawn layer the second-darkest in the chapter, arriving on a −26.7 step. The per-cell tone pass caught it before the sheet's US read could sell it |

### Rejected on the sheet

- **s26 · auto repair shops (2 sheets, 18 cells).** Both pools answer this query with the
  same two shoots: a Russian shop (`Внимание к деталям`, `Опыт сервис`, Subaru signage)
  and a Spanish-language one (`DIAGNÓSTICO`, `AC Delco`). `#10` on the same query
  returned the same two shoots plus a Ferrari.
- **s26 · whole ordinary cars (4 sheets, 36 cells: driveway, curb, plain wall, home
  garage).** Pexels' car pool is an enthusiast pool: Subaru STI ×4, Mustang Bullitt,
  370Z, Evo ×2, Audi, Mercedes ×3, plus Turkish/German/Azerbaijani plates. **Every
  mass-market car carries a legible badge at 1880 px**, so a whole-car frame and the
  no-brand rule are close to mutually exclusive at this resolution — the one ordinary
  sedan (a VW Passat) has the roundel dead centre. Two of the cleanest were also
  **dark**: the white Camry under a tree measures **11.6 / 2.2**, which on the
  longest-held frame is the floor-relocation defect the stopping rule names.
- **s26 · dashboards / odometers (1 sheet, 3 of 9 cells returned).** All three: Hyundai
  logos, **km/h** dials (non-US), median 18–34.
- **s26 · engine bays and mechanics (1 sheet, 9 cells).** Tonally dead — the brightest
  is 64.1 and it is the Spanish shop again; the rest sit at 18–55 because an engine bay
  is black.
- **s26 · receipts on a dashboard (1 sheet).** Returns desks with 1040s (which would be
  the chapter's *sixth* paper frame) and Polish złoty.
- **s26 · car keys (1 sheet).** Mercedes fobs ×3, an Infiniti fob beside a lit phone
  screen (banned outright), and the **`PEUGEOT`** tag already killed on this cut at
  attempt 1. The one clean bright cell is a bunch of keys that reads *house* keys as
  readily as car keys — actively ambiguous in a chapter that argues about both.
- **s26 · aerial of one car (1 sheet).** No single-car aerials exist in the pool; every
  cell is either an empty lot or the same eighty-car scale error.
- **s30 · apartment facades (1 sheet).** Delft, Amsterdam, Haussmann Paris — place
  errors on a US-market cut; the placeless ones are flat window grids that read
  "building", not "somewhere people live".
- **s30 · towers against sky (1 sheet).** Reads as overseas high-rise; one cell is a bare
  grey slab, i.e. the "even and empty" failure.
- **s30 · aerial suburban rooftops (1 sheet).** ⚠ **Came back 2 of 9** — the lossy-sheet
  failure the brief warns about, and the two that arrived were a top-down street (s29's
  subject) and a distant hillside town.

---

## 4. The chapter re-scored on the live files (predicted)

median | rank | p10 | rank | p90−p50 | step-in

```
s24  36.6 (15) | 11.3 (11) |  45.4 |   —        s32  91.2  (8) | 29.3  (7) | 35.2 | +20.5
s25  93.9  (7) | 40.6  (4) |  36.5 | +57.3      s33  57.8 (13) |  0.0 (16) | 32.7 | −33.4
s26  85.3  (9) |  8.4 (12) |  25.3 |  −8.6 *    s34 128.3  (2) | 92.2  (1) |  7.8 | +70.5
s27  97.8  (4) | 82.9  (2) |  38.1 | +12.5      s35 137.9  (1) |  2.3 (15) |  6.7 |  +9.6
s28  95.8  (6) | 28.9  (8) |  25.3 |  −2.0      s36  50.3 (14) |  7.2 (14) | 63.1 | −87.6
s29  58.5 (12) | 15.0 (10) |  77.2 | −37.3      s37  20.5 (16) |  7.5 (13) |103.8 | −29.8
s30  97.7  (5) | 36.1  (5) |  18.9 | +39.2 *    s38  77.5 (10) | 28.8  (9) | 28.3 | +57.0
s31  70.7 (11) | 43.2  (3) |  59.8 | −27.0      s39 102.3  (3) | 30.8  (6) | 13.1 | +24.8
```

- **The floor did not move.** Still **s37 at 20.5 / p10 7.5**, the frame the editor ruled
  acceptable, arriving on −29.8. Neither replacement went near it, and it was not chased.
- **The longest-held frame is safe.** s26 is #9 of 16 on median — mid-pack, six frames
  darker than it. The stopping rule's second trigger is not armed.
- **The payoff still passes all four clauses.** s34: sound-off pass · median 128.3 **#2**
  (top quartile = ceil(16/4) = 4) · p10 92.2 **#1** · step-in **+70.5**. Nothing I
  touched competes with it: s30's p10 is 36.1 and s26's is 8.4.
- **s31 untouched and still off the floor** (70.7 / 43.2 / #11 / #3 source-side; the
  encode had it at 35.0 / 24.0 / #8 / #4 — the ~2× gap again, ranks intact).
- **Unsafe margins to settle on the encode, not from here:** s30 97.7 against s27 97.8
  (0.1) and s28 95.8 (1.9) — ranks 4/5/6 are not predictable. Nothing depends on which.
  s26 85.3 against s38 77.5 (7.8) and s32 91.2 (5.9) is safe.

---

## 5. Standing rules, each actually run

- **md5 across ALL of `studio/`, both cuts, every sibling chapter** — 189 jpgs hashed
  (`_cand/`, `node_modules/`, `snapshots/` excluded). **Neither new file collides with
  anything.** The 28 duplicate-hash groups that exist are all pre-existing
  archive/mirror pairs (hi-ch1 `retired-attempt6`, hi-ch2 `superseded-r*`, hi-ch3
  `originals`, render `SHEET` pairs) plus registry block icons — no en-ch3 file appears
  in any of them.
- **Source-URL collisions** — all 10 `CREDITS.txt` files under `studio/` swept. Both new
  Pexels URLs appear exactly once, in this chapter. (Noted in passing, not mine and not
  a defect: en-ch4 `s41/s42` and hi-ch3 `s23/s24` each share one source URL, both
  documented in their own credit rows as deliberate derived crops.)
- **Cross-pool tell** — neither new row reads "by Pixabay" on a Pexels result. s34's
  legitimately does; that row is pre-existing and untouched.
- **Attribution** — `CREDITS.txt` has **16 rows, 16 distinct keys**, matching the 16
  manifest keys and the 16 files on disk exactly. Both replaced rows were **re-keyed in
  the same move as the pixels** (the tool rewrites the row for the filename it fetches);
  no stale row survives, and nothing was hand-placed by this attempt.
- **≥1600 px** — 1880 and 1880.
- **US market** — no foreign signage, no non-US currency, no metric dials, no
  non-US marque in either frame. This is what killed three of the four full-resolution
  promotions.
- **Outgoing files archived** to `assets-ch3/superseded-r4/` (both jpgs + both `.src`)
  before anything overwrote them.

---

## 6. For fin-build — what this attempt needs from the next one

1. **Regenerate only.** No code, timing, geometry or copy changed. `housing-share` stays
   at `SHARE = 0.334`, the tick at 275.48, cues 1.55 / 1.90 / 2.50, `.art-lift` on,
   `vrule [150,300]`; s26 keeps `brule: 400`, `chipAt [4.37, 5.01, 5.89, 6.71]` and its
   two explicit chip rows. `index.html` / `build.mjs` predate both photographs, so the
   regenerate is not optional.
2. **Re-run `npm run check` and watch AA on s30** — its type band is the chapter's
   brightest at median 104.4 / p90 117.9. Precedent (s27 96.0, s28 110.5) says it passes.
3. **No `bgpos` on either slot.** s30's three crops differ by less than the method's
   noise; s26 is already exactly 16:9 and has no slack at all.
4. **Re-shoot the max-density snapshot for s26 and s30 only** — the other fourteen are
   byte-identical to the ones already reviewed.
5. **s26 is a declared judgement call for the editor** (§2): it names a car *part*. The
   ledger in §3 is the evidence that the whole-car alternative is not buyable in this
   pool at ≥1600 px without a legible badge, and that the two brand-free whole-car
   frames that do exist are tonally at the floor — which on the chapter's longest-held
   scene is itself a defect.

---

## 7. Commands used beyond the stage's allowlist, declared

`python3` for four things the brief requires and the allowlist does not name:
the composed-median measurement and its validation, slicing contact sheets into cells
for the per-cell tone pass, copying the outgoing files into `superseded-r4/`, and
`tools/pipeline_check.py`. Plus `md5sum` and `find` for the dedupe sweep. No other
tool wrote anything; `assets/lottie/` was not touched (this chapter's one drawn layer
is SVG in `build.mjs`, not a lottie).
