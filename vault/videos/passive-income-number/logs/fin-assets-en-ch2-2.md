---
summary: en ch2 attempt 2 — targeted single-slot re-fetch of s20 only. The blocker (a person's torso and arms in an objects-only cut) is gone: the new frame is a US grocery produce shelf with dollar-per-pound price tags, no person, no hand, no face. Source p90 138 → 195, predicted encoded p90 35 → ~50, so the s19→s20 joint narrows from −23 to about −8. The storyboard's declared car-back-seat bags frame could NOT be sourced object-only — 17 contact sheets, ~100 candidates — and the doorstep-bags fallback turned out to be byte-identical to ch1's s6.
updated: 2026-08-08
source: fin-assets attempt 2, chapter 2, en cut — editor-en-ch2-1 blocker `s20_person`; storyboard-en §10; VO 2.12.
---

# fin-assets — passive-income-number / en / chapter 2 / attempt 2 (targeted, one slot)

**PASS `python3 tools/pipeline_check.py check assets --slug passive-income-number --cut en --chapter 2`.**

**Accepted 1 · rejected ~101 candidate cells across 17 contact sheets · dropped 0.**
Only `s20.jpg` was touched. The other fifteen images, their credit rows and their manifest
entries are byte-unchanged; the filename is unchanged, so no rebuild is implied.

| | outgoing | incoming |
|---|---|---|
| subject | seated person, torso + both arms + plaid shirt, hugging a bag of vegetables on a deck | US grocery produce shelf — eggplant, zucchini, peppers, lettuce — with handwritten **$/LB price tags** |
| person in frame | **yes** (the blocker) | **no** |
| source | Pexels, Ron Lach, *teenage boy holding paper bag with vegetables* | Pexels, Greta Hoffman, `.../vegetable-stall-at-supermarket-9705830/` |
| W×H | 1880×1253 | 1880×1253 |
| source p90 (YHIGH) | 138 | **195** |
| source YAVG | 75 | 86 |
| md5 | `cf0d55a8…` | `7…` unique across all 142 jpgs in `studio/` |

## The one fact this fetch existed to guarantee

**I read `s20.jpg` at full resolution (1880×1253) and then re-read three 2× zoom tiles across
it. There is NO person, NO torso, NO arm, NO hand and NO face anywhere in the frame.** The
subject is produce crates, a shelf rail and price cards. Nothing organic in frame is human.

Also cleared on the same read: every word in the frame is **English**, every price is in
**dollars per LB** (`$3.99 LB`, `$5.99 LB`, `$1.99 LB`, `$2.99`, `$3.99 LB`), and there is **no
brand mark** — the only non-price text is produce names (`REGULAR EGGPLANT`, `ITALIAN PEPPER`,
`ITALIAN EGGPLANT`, `GREEN SQUASH`, `LONG HOT PEPPER`, `HOLLAND RED/YELLOW PEPPER` — variety
names, not places). The sticker on one eggplant is an unreadable barcode oval.
⚠ One cosmetic note for the draft: the centre-right tag is the store's own handwritten typo,
`GREEN SOUASH`. It is a real sign in a real shop, ~7% of frame width, and it will grade down,
but it is legible enough at 1:1 that someone may see it.

## Tone — the number, by the ch3 method

Grade is locked at `grayscale(.32) brightness(.62) contrast(1.05)`, so
`y' = ((0.62y/255 − 0.5)·1.05 + 0.5)·255` on the source percentile.

| | source p90 | predicted post-grade p90 | **predicted ENCODED p90** |
|---|---|---|---|
| s19 (unchanged) | 228 | 142 | 59 *(measured by fin-editor)* |
| s20 **old** | 138 | 83 | 35 *(measured by fin-editor)* |
| s20 **new** | **195** | **121** | **≈ 50** |
| s21 (unchanged) | 144 | 86 | ≈ 36 |

The encoded column is calibrated, not assumed: ch2's two measured scenes give
encoded/predicted = 59/142 = **0.415** and 35/83 = **0.420**, i.e. a constant ~0.418 that is the
scene's `.scrim` + compositing, not the grade. Applying it to 121 predicts **≈50** for the new
s20 — a **+15 encoded lift** on the frame the editor called the chapter's darkest.

Consequences at the two joints, both worth stating plainly:

- **s19→s20 goes from Δ−23 to Δ≈−8**, and it is no longer produce-at-home → produce-at-home:
  it is a dark domestic table → a lit shop shelf. Two places, and now nearly level.
- **s20→s21 becomes Δ≈−15** (it was ≈+1). The drop has moved, not vanished. I think that is
  the right place for it: s21 is the `hero` landing ($254,225) on a single loaf under hard side
  light, the darkening runs *into* the payoff, and shop → studio still-life is an unambiguous
  change of place. If fin-editor disagrees, the lever is s21, not s20.

## Why this is not the storyboard's declared frame — and what it cost to find out

Storyboard §10 / the editor's ruling both name **"two paper grocery bags on a car's back seat,
daylight, no plates visible"**. That frame does not exist object-only in either pool. Seven
sheets went at it directly:

`brown paper grocery bags on the back seat of a car daylight no people@pexels` ·
`paper bag full of groceries on a car seat inside the car@pexels` ·
`paper grocery bags in the open trunk of a car in a parking lot@pexels` ·
`grocery bags in car trunk` (pixabay) · `grocery bags on the back seat of a car@pexels#6` ·
`open car trunk with shopping bags@pexels` · `paper bag on the front passenger seat of a car
daylight@pexels`.

**Bags-in-a-car is a delivery-driver genre.** Every usable cell put a driver's torso, arms or
gloved hands in the right third of the frame — the identical composition, from three different
shoots. The remaining cells were lifestyle shopping-haul shoots (three women and a hatchback),
empty back seats with no groceries at all, or an American-flag cushion. Pixabay answered the
car queries with bananas, a leather satchel and a South African price tag (`R24⁹⁹`), and its
`largeImageURL` is 1280 px anyway — under the 1600 floor, so the pool is unusable for this slot
regardless.

Cropping the driver out was considered and rejected on arithmetic: `--pick` returns Pexels at
`dpr=2&w=940` = 1880 px, and cutting the right third leaves ~1220 px, below the 1600 floor for
a scene with a ken push. (The s10b precedent works only because s10 came back 1732 px wide.)

### The fallback that md5 caught — the one worth carrying forward

Sheet 13, `grocery delivery paper bags left on a doorstep in sunlight@pexels`, cell 2 was
excellent: groceries in a tote on a sunlit stone step, no people, source p90 **215**, US
suburban screen door. It was promoted, read at full resolution, and *then* failed the dedupe:

```
7e982160bfa6ac3a8ba3757225d60db3  …-en-ch1/assets-ch1/final/s6.jpg
7e982160bfa6ac3a8ba3757225d60db3  …-en-ch2/assets-ch2/final/s20.jpg
```

**It is ch1's s6, the same photograph, byte-identical** — ch1 already spends "paper grocery bags
on the front doorstep". So the whole doorstep family is out for this cut, not just that file,
and sheet 21 (a second doorstep sweep) was discarded unread-in-detail for the same reason. The
dedupe ledger has now caught a *within-cut, cross-chapter* repeat, which the chapter-first flow
makes easy to ship: nothing in a chapter's own directory hints that a sibling chapter used the
picture. Run the md5 sweep across `studio/videos/*/assets-ch*/final/*.jpg`, not just the
chapter you are working in.

## The other twelve sheets, and why nothing else survived

| query | why every cell died |
|---|---|
| `two full brown paper grocery bags standing on a kitchen counter…@pexels` | 6/6 people (a hand-only cell is still not permitted — §10 lists s18/s33/s45/s53/s58 as the only hand frames, and s20 is not one) |
| `paper bags of groceries on a kitchen counter@pexels#10` | 5/6 people; the one object-only cell measured **p90 131 / YAVG 45** — *darker* than the frame being replaced |
| `brown paper grocery bag full of food@pexels#12` | 5/6 people, incl. the outgoing image's own sibling from the same shoot |
| `still life paper bag of groceries…` · `vegetables in a brown paper bag@pexels` | high-key white marble, or produce-on-a-table = a second s19, or bread = a second s21 |
| `shopping cart full of brown paper grocery bags in a supermarket parking lot@pexels` | 6/6 **empty** carts; one cell is a LIDL storefront |
| `shopping cart full of groceries in a supermarket aisle@pexels` cell 2 → promoted, then killed at full resolution | **Italian supermarket**: `TERRICCIO FIORE BELLO`, `Tovaglioli`, `Piatti fondi`, comma-decimal euro prices `0,69 / 1,39`, `KETER HOLLYWOOD`. Invisible at 512×288, unmissable at 1880 |
| `open refrigerator full of food…@pexels` | store coolers, dense branding, one Indonesian (`Greenfields · Pilih 100% Fresh Milk`) |
| `kitchen pantry shelves…@pexels` | 5/6 cells only; canning jars read "preserves", not "the grocery bill"; one hand |
| `close up of price tags on a bright supermarket shelf@pexels` | Coca-Cola/Pepsi/Fanta walls with Chinese tags, and a German `Liebe Kunden` shelf |
| `farm stand crates of fruit with dollar price signs…@pexels` | tropical/foreign markets, or people |
| `empty american grocery store aisle with shopping cart bright@pexels` | Chinese signage, `Cart park` (British phrasing), or no food |
| `flat lay top view of groceries in a paper bag on a light wooden table@pexels` | brightest cell (p90 232) is a kitchen produce flat-lay = s19 again; another cell has a lit phone screen |

**A trick worth keeping: measure the contact sheet, don't promote to measure.** The sheet is a
1536×576 tile of six 512×288 cells, so
`ffprobe -f lavfi -i "movie=_cand/s20.jpg,crop=512:288:<x>:<y>,signalstats"` gives per-cell
YAVG/YHIGH before any full-size fetch. It killed three sheets on tone in one command each, and
it is how the counter-bags cell (p90 131) was rejected without a download.

## Sound-off test on the accepted frame

1. **Words covered, is the point legible?** A shop shelf of vegetables with dollar-per-pound
   price cards: this is what food costs. VO 2.12 is *"about eight hundred and forty-seven
   dollars a month, walked out of a store in bags."*
2. **Does it argue?** No. Prices in dollars under `PER MONTH · $847` and a foot reading
   *"$10,169 divided by 12"* all point the same way.
3. **Is the named thing in frame?** *Store* — yes, unambiguously. *Bags* — no, and that is the
   one thing lost relative to the declared spec. It is the price paid for object-only, and the
   trade was: an off-spec picture, or an off-**rule** picture.
4. **Repeat in the chapter?** No. s19 is a dark domestic table shot top-down; s20 is a lit
   retail shelf shot straight on; s21 is a studio loaf. Three different places.
5. **Place, era, currency?** US, present-day, dollars, imperial pounds. This is now the only
   frame in the chapter that shows the cut's own currency.

One flag for fin-build/fin-editor: this is a **dense** frame with ~7 high-contrast white price
cards. The largest numeral in it is roughly a third the height of the `$847` card, so the
hierarchy holds, but if the stack lands on top of a tag the fix is a nudge, not a re-fetch.

## Housekeeping

- Outgoing file archived, not deleted: `…/assets-ch2/final/_cand/_archived-s20-attempt1-person.jpg`
  (+ its `.src`). `_cand/` is the throwaway sheet directory — not in the manifest, not shipped.
- `manifest.json` s20 query updated in the same move as the file:
  `grocery store produce display with dollar price signs@pexels`. All 16 keys intact.
- `CREDITS.txt` re-keyed by the tool (it rewrites the row for a slot rather than appending):
  `s20.jpg  https://www.pexels.com/photo/vegetable-stall-at-supermarket-9705830/  by Greta Hoffman  Pexels License`.
  16 images, 16 rows. The page URL is unique across every CREDITS.txt in `studio/`.
- `assets/lottie/` untouched. Chapters 1 and 3 untouched.
