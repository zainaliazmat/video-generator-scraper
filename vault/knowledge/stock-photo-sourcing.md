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
- **Warmth has its own predictor: mean `R−B` on the raw, reject under about +40.**
  The grade desaturates by a third, so "warm enough by eye" is not warm enough by
  the time it renders. Measured on ch1: s5 (+61.7) and s7 (+43.6) render warm;
  s2 (+14.6) and s3 (+3.3) do not — and s2 is instructive, because it is a
  genuinely warm photograph (a chai glass on a sunlit sill) that simply had too
  little saturation to survive. Under the chapter archetype no override can
  rescue it, so the only lever is the candidate. Screen for this at the same time
  as `YHIGH`, on the same sheet cells.
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
