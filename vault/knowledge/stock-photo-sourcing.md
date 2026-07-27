---
summary: How stock photos get sourced for studio videos — the scripted Pixabay fetcher, the verified hit-rate per market, and the object-led rule that came out of the 50-30-20 build.
updated: 2026-07-27
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

## When Pixabay isn't enough

Escalate only if a scene genuinely needs a specific depiction: Wikimedia
Commons / Library of Congress for historical (see
[[../videos/video-hist-01-travel/asset-sourcing]]), or generate the image
per [[scene-image-prompt-rules]]. For the finance format, object-led Pixabay
has been sufficient.
