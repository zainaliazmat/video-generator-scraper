---
summary: How stock photos get sourced for studio videos — the scripted Pixabay fetcher, the verified hit-rate per market, the object-led rule from the 50-30-20 build, and (2026-08-07) the grade rule: never buy high-key stock, because the locked grayscale/brightness grade turns any white-dominant subject into a flat charcoal slab.
updated: 2026-08-07
source: 50-30-20-rule-hi / -en build, 2026-07-27. ~35 fetches, every one eyeballed before it went in a composition.
---

# Stock-photo sourcing (Pixabay)

## The tool

`tools/stock/pixabay_fetch.py` — stdlib only, reads `PIXABAY_API_KEY` from `.env`.

```bash
# whole scene set from a manifest {"s1.jpg": "query", …}
python3 tools/stock/pixabay_fetch.py --manifest studio/videos/<proj>/assets/img/manifest.json

# one swap; "#3" takes the 3rd result instead of the 1st — the retry knob
python3 tools/stock/pixabay_fetch.py --query "coin jar savings#3" --out assets/img/s6.jpg --force
```

Downloads `largeImageURL` (1280px wide — what every existing `studio/videos/*`
project uses), skips files that already exist unless `--force`, and appends
`CREDITS.txt` (page URL + author + licence) next to the images. `--selftest`
runs offline.

## Hit rate — the finding that matters

**Verify every image before it goes in a composition.** Measured on this build:

| Query type | First-try usable |
|---|---|
| Generic Western/US ("apartment for rent sign", "young man smartphone city dusk") | ~90% |
| Generic objects ("coin jar", "calculator notebook", "empty wallet") | ~80% |
| **India-specific with people** ("indian man using smartphone street") | **~20%** |

India-people queries returned, in order: a Black man on a US street, Japanese
commuters on a Tokyo train, a Varanasi tourist bazaar, and a rural overloaded
autorickshaw. Pixabay's India library is **heritage- and tourist-heavy** and
almost empty of contemporary urban-professional life — which is exactly the
audience the India finance videos target ([[niches/india-finance-market]]).

Other traps caught by eyeballing:
- **Demonetised ₹500 notes** (pre-2016 yellow-green series) are all over the
  "indian rupee" results. Current series = stone grey. An Indian viewer clocks it.
- **US dollars answering finance queries** — "bank passbook money counting"
  returned stacks of $100 bills. Fine for a `-en` cut, fatal in a `₹` one.
- **Readable brand marks** — payment-terminal and card shots carry `ingenico`,
  `VR-Bank`, `V PAY`. Never put a real brand on screen.
- **"Hand holding a phone" is a brand minefield.** Both cuts' S8 shipped a defect
  caught only by pulling frames from the finished render: the Hindi one showed
  `AT&T` + "slide to unlock" on a dated iPhone, the English one a **Facebook login
  screen with the logo legible** plus Scrabble tiles spelling "SOCIAL MEDIA".
  Neither survives a look; both were invisible to me until I looked at the render.
  **Never use a phone-screen photo as a background** — the screen is someone
  else's brand, and it's the brightest thing in frame.
- **Chart direction** — a trading-app screenshot with a *falling* line under a
  "this makes you richer" VO line. Check what the picture is actually saying.

## The rule that came out of it: object-led, not scene-led

Photos in this design system sit under `grayscale(.32) brightness(.62)` with
heavy type on top — they are **texture, not information**. So don't hunt for a
literal depiction of the sentence. Pick the object that carries the cultural and
emotional signal:

> **The ₹500 notes and Indian coins say "India" more reliably than any stock
> photo of an Indian person — and they're actually available.**

Corollaries, all proven on 50-30-20:
- **The densest scene gets the calmest background.** Proven twice: the count-up
  scene (S7) and the climax/action scene (S8) both ended up on plain textures —
  wood, concrete, charred wood. Anything with a subject fights the type and
  smuggles in text or branding. Reach for a texture *first* on any scene carrying
  more than ~4 stacked elements, not as a fallback.
- Near-black textures need a per-scene grade override — the system's
  `brightness(.62)` crushes them flat. Inline `filter:` on that one `.bg` (the
  English S8 runs `brightness(1.45)`).
- Faces fight the typography; hands and objects don't.
- **Drop a cut-in rather than fake it.** Four planned cut-ins were cut from the
  Hindi build because nothing honest existed. Single-photo scenes read fine.

## Standing rejections (restate these to fin-assets every run)

Found 2026-08-01 on japanese-money-methods; each has shipped undetected before.

- **Currency photographs: check whether two notes in one frame SHARE A SERIAL, not
  whether one serial is valid.** Prop and film money is printed from a single plate, so
  the tell is repetition inside the frame, not anything about an individual note.
  Found 2026-08-08 on passive-income-number hi ch2 s16 — the **hero corpus frame**, the
  payoff of the chapter — where two visibly distinct ₹500 notes both read `ILR 176177`.
  It had a standing DO-NOT-RE-FETCH on it and had been *verified*: the earlier check
  confirmed the notes were post-2016 current series at full resolution, which was true
  and beside the point. The rule it was written against was demonetisation; the defect
  was counterfeit. **A check that reads one serial and clears the frame is answering a
  different question than the one that matters.**
  Known-bad serials, both surfaced repeatedly across ₹ queries — reject on sight:
  `ILR 176177` and the entire `6UW 643492` shoot (hit on five separate queries).
  This matters more than an ordinary sourcing miss: prop money in a finance video aimed
  at an Indian audience is a credibility failure the audience is better equipped to spot
  than we are.

- **A DERIVED CROP must be re-derived when its source file changes.** A crop records a
  geometry against a parent, and re-fetching the parent silently orphans it: the crop
  still exists, still passes every check, and now shows an unrelated photograph. Found
  2026-08-08 on passive-income-number hi ch2, where s15 is a 91.754% crop of s14's source
  and s14 was being re-fetched in the same pass — un-caught, the continuous zoom would
  have dissolved mid-hold into a different picture **with every check green**. The credit
  row goes stale in the same instant and must be re-keyed too. Record the parent in the
  manifest so the dependency is visible to the next fetch, which will not remember it.

- **Never a phone or laptop SCREEN as a scene background.** Script beats about apps,
  subscriptions or "check your statement" pull screen photos by gravity, and a screen
  in frame dates the video, brands it, and fights the type. Shoot around it: glow only
  with the handset edge-on, a silhouette, or a **printed** document standing in for the
  on-screen list. **This defect shipped three times before anyone named it.**
- **Pixabay tops out at 1280px on this key** (`largeImageURL`; `fullHDURL` and `imageURL`
  need full API access we do not have — verified against the API 2026-08-01). Pexels
  `large2x` is 1880px. Under any full-bleed architecture a 1280px file is drawn ~1.63×
  at `inset:-8%`. **Route every hero, SOLO and closing frame to Pexels**; let Pixabay
  carry the texture-under-scrim scenes, where the grade plus 5% grain reads as soft
  focus rather than as an upscale.
- **Currency must be genuine current notes, never prop money**, and never the other
  cut's currency.
- **The contact sheet cannot be trusted.** Across this run, nine images passed their
  sheet and failed the full-resolution read (a legible price, an IRS table, brand
  cartons, a Polish receipt total, Halloween pumpkins, an identifiable child, four
  bitcoin coins, a fake-kanji shopfront, and a Chinese menu board sold as Japanese).
  One pick even came back byte-identical to another scene in the same cut and only the
  md5 sweep saw it. **Read every promoted file at full resolution, and md5 it.**
- **md5 dedupe has a hole, and it is not a rare one (2026-08-08).** en ch2's s14 came
  back byte-unique and was still the *Hindi cut's own s16*: **Pexels has ingested part of
  Pixabay's library**, so the same photograph lives in both pools at different
  resolutions and therefore different hashes. It would have shipped the identical ledger
  in both language cuts of the same video — the one thing cross-cut dedupe exists to
  prevent — with every check green.
  - **The cheap tell:** Pexels credits some of those contributors as *"by Pixabay"*.
    Treat that credit line as a dedupe warning, not as attribution trivia.
  - **The reliable check:** read the promoted file at full resolution against the
    *sibling cut's* asset log. That is what actually caught it.
  - **A perceptual sweep finds it mechanically** — 8×8 dHash, flag any pair within
    Hamming ~6. Run it per chapter across BOTH cuts. It is deliberately **not** wired
    into `pipeline_check`: every derived crop the pipeline makes on purpose (s3→s4,
    s10→s10b, hi ch2's s13→s14 continuous zoom) sits at Hamming 5 or less, so as a hard
    gate it would cry wolf on the pipeline's own design. Run it, then read the hits —
    a hit is a question, not a verdict.

## The grade decides the photo: never buy high-key stock (2026-08-07)

Found on passive-income-number-hi ch1, where three of seven backgrounds looked
like unrelated defects and had one cause. **The blockframe grade is locked** —
`filter: grayscale(.32) brightness(.62) contrast(1.05)` in
`tools/scaffold/assets/blockframe.css`, with per-scene overrides forbidden by the
storyboard's §9 — so the photograph is chosen *knowing* it will be darkened by
38% and desaturated by a third.

**A white-dominant subject cannot survive that.** White marble, a pale card on
pale wood, white paper in a white office all land as the same flat charcoal
slab. One frame (s4: "a single closed brown envelope on a bare wooden table")
delivered exactly what its query asked for and still rendered as a grey panel
with no flap, seam or depth — it satisfied the letter of `image_per_scene` and
broke its intent, saying nothing sound-off. Checked at both ken extremes, so it
was the photograph, not the crop.

Three rules, all cheap to follow at query time and expensive to fix afterwards:

1. **Ask for low-key / warm originals: the subject lit against a dark ground.**
   Add the lighting to the query, not just the object. "Chai glass on a
   windowsill, warm morning light, dark interior behind" survives the grade;
   "steel glass of chai tea india" returns an overhead food-blog flat lay on
   white marble.
2. **Replacing one white photo with another white photo re-breaks it.** When a
   frame reads grey, the fix is a differently-lit original, not a re-crop.
   ⚠ Note the tension with the 50-30-20 corollary above ("near-black textures
   need a per-scene grade override"): that escape hatch exists under the plain
   blockframe architecture, but the **chapter archetype layer closes it** —
   `storyboard-*.md §9` permits no per-scene grade, so under a chapter cut the
   photograph is the only variable you have. Check which regime you are in
   before reaching for an inline `filter:`.
3. **A bright detail that carries the meaning must survive `.62`.** A phone
   face-down whose screen-glow "spills onto the wood" is the right *idea*, but
   if the glow is subtle in the raw it is gone in the encode. Buy the brighter
   frame than looks right unlit.

### Measure it: source `YHIGH ≥ 110`, enforced

The predictor is the **highlight ceiling, not average brightness** — and it is
counter-intuitive enough that two review rounds and a re-fetch missed it. On
ch1, s3 (YAVG 56.5, YHIGH 134) reads fine while s4 (YAVG 59.4, YHIGH **93**)
rendered as a black slab: s4 was the *brighter* of the two on average. A frame
with no highlights has nothing for the grade to leave behind.

```bash
ffprobe -v error -f lavfi -i "movie=<file>,signalstats" \
  -show_entries frame_tags=lavfi.signalstats.YHIGH -of csv=p=0
```

`pipeline_check check assets --chapter <N>` now fails any promoted image under
110, calibrated on the 20 images of ch1+ch2: s4 = 93, a 30-point gap, s11b = 123
(looked at and passed), everything else ≥ 134. **One-sided on purpose** — the
opposite failure, a high-key flat *texture* reading as a UI panel, is real
(ch2's s16) but luma does not predict it: ch2's s10 measures 246 and reads fine
because numerals and pins give it structure. That end still needs eyes.

Two things that make the gate cheap instead of annoying:

- **Measure the contact sheet's cells, not the promoted file.** `crop=512:288:x:y,signalstats`
  per cell is a *pre-fetch* filter — four rejections on s4's third pass cost six
  ffprobe calls and zero downloads.
- **⚠ RETIRED 2026-08-08 — `R−B ≥ +40` on the raw was never reachable.** It read as a
  screening rule for two videos and cost real fetch rounds. It said: *"warmth has its
  own predictor: mean `R−B` on the raw, reject under about +40. Measured on ch1: s5
  (+61.7) and s7 (+43.6) render warm; s2 (+14.6) and s3 (+3.3) do not."* Those
  observations are real; the inference from them was wrong, because every one of them
  was taken on the SOURCE FILE and never on the encoded frame.

  fin-render measured the encoded frames of passive-income-number-en ch1 and derived
  the pass-through from scene pairs, no model:

  ```
  encoded R−B = 0.0927 × source R−B − 6.43        residual std 1.43, 5 pairs
  ```

  **Only ~9% of a photograph's warmth reaches the screen, under a fixed −6.43 from the
  layer stack.** The proof is s1: source **+73.53**, three times warmer than anything
  else in the chapter, landing at **+0.76** on screen — 7.9 units from the terrazzo
  slab it was supposed to beat. To hit neutral a photograph needs source R−B ≈ **+69**;
  to hit the old +40 target it needs ≈ **+500**, which does not exist.

  So warmth is **chrome, not photograph**. The `--bg` ink is `#0d1017` (R−B −10) and it
  is all four `.scrim` layers, the `.band`, *and* the far stop of `.field`
  (`linear-gradient(158deg, var(--f1) 0%, var(--bg) 64%)`) — past 64% of the diagonal
  the "warm ground" is the cool ink. Several `--f1` values are themselves cool
  (`#161f2b` is −21, `#1a1e24` is −10). Raising `.has-photo .field` opacity makes a
  chapter **colder**, not warmer, because the gradient it strengthens runs into `--bg`.

  **What to do instead:** screen `YHIGH` (which does predict survival) and judge warmth
  on the ENCODED FRAME. Do not reject a candidate on source R−B, and never send a slot
  back a second time for warmth — that is a chrome edit, and `--bg` is a global
  `blockframe.css` token shared by every cut on the channel, so it is a channel-level
  decision, not a per-chapter or per-photograph one.

  The general lesson, which this repo keeps re-learning: **a rule measured on the source
  is a rule about the source.** The encoded frame is the only thing the viewer sees, and
  it is the only place a visual rule may be calibrated.
- **When a slot fails twice on brightness, change the MATERIAL, not the lighting
  adjective.** Kraft paper is diffuse: round 1 lit it badly, round 2 lit it well
  against black, both measured dead. Enamel, glass, glazed ceramic, polished
  metal and wet stone have a specular ceiling; matte paper, cardboard and
  unfinished wood do not. s4 was only solved by abandoning the envelope for a
  white enamel door plaque (YHIGH 203, tonal spread 97 against round 2's 14) —
  and the best-*looking* candidate on that sheet, brass "505" on brown wood, was
  killed at 106 as round 1's failure wearing a different prop.

Corollary for anything the pipeline draws rather than fetches: masking a figure
is not the same as removing every trace of what it is. The ch1 notification
Lottie masked its amount correctly (the open loop is the point) but carried no
currency glyph at all, so sound-off it said "a notification arrived" rather than
"money arrived" — on the one beat a 35-second cold open exists to deliver.

## When Pixabay isn't enough

Escalate only if a scene genuinely needs a specific depiction: Wikimedia
Commons / Library of Congress for historical (see
[[../videos/video-hist-01-travel/asset-sourcing]]), or generate the image
per [[scene-image-prompt-rules]]. For the finance format, object-led Pixabay
has been sufficient.
