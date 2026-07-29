# PRODUCTION PACK — Watercolor-Ink Brand Film (Hyperframes)

### Style target: "Historical Memories" aesthetic → applied to a NEW topic

### Format: 16:9, 1920×1080, 30 fps, ~4:00, music + on-screen text (optional VO layer)

> **How to use this pack:** This document holds the creative + content side (topic, research, script, storyboard, assets). The _exact Claude Code prompts_ live in the companion file **CLAUDE-CODE-PROMPTS.md**. The visual technique is demonstrated in **reference-scene.html**. Source the assets in the checklist, drop them into the folder structure, then run the prompts in order.

---

## 0. THE ONE THING THAT MAKES THIS WORK

The whole style is **one reusable scene template**. Every scene is the same machine with different content:

```
aged paper canvas
  → photo masked by an ink shape that SPREADS open (the "paint-in")
  → photo edges made watery by an SVG turbulence/displacement filter
  → desaturated base + a second full-color copy bleeding through the same mask (selective color)
  → slow Ken Burns push
  → script title + uppercase serif subtitle fading up
  → film grain + vignette over everything
  → ink-splatter wipe into the next scene
```

Build that ONE scene perfectly first (Prompt 1). After that, every other scene is copy-paste-swap-content. **Do not try to build 24 scenes from scratch.** Perfect the template, then mass-produce.

---

## 1. TOPIC SELECTION

You asked me to pick. Here's my decision and the reasoning, so you can swap with confidence if you prefer.

### ✅ RECOMMENDED: **"The Soul of Coffee — From Origin to Ritual"**

A heritage-brand film for a (real or fictional) specialty coffee house.

**Why this topic wins for this exact style:**

- **Tonal match is perfect** — warmth, craft, nostalgia, sepia, hands, steam, earth. The watercolor-ink look was practically made for it.
- **Bulletproof free asset availability** — Unsplash/Pexels are saturated with high-quality, commercial-free coffee-origin, harvest, roasting, and brewing imagery. You will not get stuck sourcing tonight.
- **Commercially believable at $5k** — this reads as a premium brand film a coffee roaster would actually pay for. Strong portfolio piece.
- **Naturally 4 minutes** — the bean's journey (origin → harvest → process → roast → brew → ritual → invitation) is a built-in 5-act structure.

### Alternates (the system is identical — only content + photos change):

- **B) "Of Vine & Time" — a heritage vineyard / winery film.** Equally elegant; slightly fewer free hero shots than coffee.
- **C) "Echoes of Antiquity" — heritage travel / lost cities.** This is the _closest_ to the reference (same subject family), so it's the **lowest-risk choice if your #1 goal is "looks exactly like the sample."** Infinite free imagery. Less "client brand," more showcase.

> **Decision guidance:** If the client brief is open and you want the strongest _premium-brand_ impression → **Coffee**. If the client literally said "make it look like this sample" → **Echoes of Antiquity** is the safest match. Everything below is written for **Coffee**, but the script beats, storyboard structure, and 100% of the prompts work for any of the three — swap the words and the images, keep the machine.

---

## 2. RESEARCH BRIEF (Coffee)

Enough grounding to make the script authentic. (Timeless background — no need to verify.)

- **Origin myth:** Legend credits a 9th-century Ethiopian goat herder, _Kaldi_, who noticed his goats grew lively after eating bright red cherries from a certain shrub. Coffee's domestication traces to the Ethiopian highlands.
- **The plant:** Two species dominate — _Coffea arabica_ (smoother, higher-grown, ~60% of world supply) and _Coffea canephora / Robusta_ (stronger, more caffeine, hardier).
- **The belt:** Coffee grows in the "Bean Belt" between the Tropics of Cancer and Capricorn — Ethiopia, Colombia, Brazil, Guatemala, Kenya, Vietnam, Indonesia.
- **The cherry:** Coffee is a fruit. Each cherry holds (usually) two seeds — the "beans." Premium coffee is hand-picked, cherry by cherry, only when ripe.
- **Processing:** _Washed_ (fruit removed before drying → clean, bright) vs _Natural_ (dried with fruit on → fruity, heavy). Beans rest, then are sorted by hand.
- **The roast:** Green beans are roasted; the "first crack" marks the turn from grassy to aromatic. Roast level shapes flavor from bright/floral (light) to deep/bitter-sweet (dark).
- **The ritual:** Grind, bloom, pour, wait. From Ethiopian _jebena_ ceremonies to the modern pour-over, coffee is a daily ritual of patience and attention.

**Narrative spine for the film:** A bean's journey is a metaphor for _care over time_ — origin, patience, transformation, ritual, connection. That's the emotional throughline.

---

## 3. THE SCRIPT (≈4:00)

**Two layers per scene:**

- **VO** = optional voiceover narration (generate with ElevenLabs if you want it; the reference had none — music + text only. VO elevates a brand film but adds a pipeline step. It's marked optional.).
- **ON-SCREEN** = the text that animates on screen (this is the primary layer, matching the reference). `TITLE` = script font (Pinyon Script). `SUB` = uppercase serif (Marcellus SC). `LINE` = small supporting serif (Spectral).

Pacing note: 30fps, ~4:00 = ~7,200 frames. Scenes average 8–10s. 24 scenes incl. intro/outro.

---

### COLD OPEN / INTRO — 0:00–0:11

**VO (opt):** _"Before the cup… there was the cherry. And before the cherry… there was the soil, the rain, and the patience of those who waited."_
**ON-SCREEN:**

- TITLE: _The Soul of Coffee_
- SUB: A FILM ABOUT ORIGIN, CRAFT & RITUAL
- (brand mark inks in beneath)

---

### ACT I — ORIGIN (0:11–0:47)

**Scene 1 — 0:11–0:20**
VO: _"High in the Ethiopian highlands, where the air is thin and the mornings are cool…"_
TITLE: _Where It Begins_ · SUB: ETHIOPIAN HIGHLANDS · LINE: 1,500 metres above the sea

**Scene 2 — 0:20–0:29**
VO: _"…a wild shrub has been growing for over a thousand years."_
TITLE: _The First Forest_ · SUB: COFFEA ARABICA · LINE: born of shade and altitude

**Scene 3 — 0:29–0:38**
VO: _"Legend says a herder watched his goats dance, and dared to taste what they had found."_
SUB: A SHEPHERD'S DISCOVERY · LINE: the legend of Kaldi, 9th century

**Scene 4 — 0:38–0:47**
VO: _"From those hills, a single seed would travel the world."_
TITLE: _The Bean Belt_ · SUB: BETWEEN THE TROPICS · LINE: a ribbon of green around the earth

---

### ACT II — THE HARVEST (0:47–1:25)

**Scene 5 — 0:47–0:56**
VO: _"Coffee is not a bean. It is a fruit — and it ripens on its own time."_
TITLE: _The Cherry_ · SUB: TWO SEEDS, ONE FRUIT · LINE: red is the only signal that matters

**Scene 6 — 0:56–1:06**
VO: _"Each cherry is chosen by hand. Only the ripe. Never the rest."_
SUB: HAND-PICKED · LINE: cherry by cherry, never by the branch

**Scene 7 — 1:06–1:15**
VO: _"A single harvest can take months, and a lifetime to master."_
TITLE: _Patience_ · SUB: THE SLOW HARVEST · LINE: there are no shortcuts in the highlands

**Scene 8 — 1:15–1:25**
VO: _"What the hands gather, the sun and water must finish."_
SUB: WASHED & SUN-DRIED · LINE: the fruit gives way to the seed

---

### ACT III — THE TRANSFORMATION / ROAST (1:25–2:03)

**Scene 9 — 1:25–1:34**
VO: _"Green and silent, the seed waits for fire."_
TITLE: _Before the Fire_ · SUB: THE GREEN BEAN · LINE: grassy, dense, asleep

**Scene 10 — 1:34–1:44**
VO: _"In the roaster, sugars caramelize, oils awaken, and aroma is born."_
SUB: THE ROAST · LINE: where flavor is forged in heat

**Scene 11 — 1:44–1:53**
VO: _"Listen for the first crack — the sound of a bean becoming itself."_
TITLE: _First Crack_ · SUB: THE TURNING POINT · LINE: grassy becomes golden

**Scene 12 — 1:53–2:03**
VO: _"Seconds decide everything. Too little is raw. Too much is lost."_
SUB: THE ROASTER'S JUDGMENT · LINE: an art measured in seconds

---

### ACT IV — THE RITUAL (2:03–2:50)

**Scene 13 — 2:03–2:12**
VO: _"At home, the ritual begins again — slower than the world around it."_
TITLE: _The Ritual_ · SUB: THE DAILY CEREMONY · LINE: a pause, on purpose

**Scene 14 — 2:12–2:22**
VO: _"The grind. The bloom. The first breath of steam."_
SUB: GRIND · BLOOM · POUR · LINE: aroma before the very first sip

**Scene 15 — 2:22–2:31**
VO: _"From the jebena of Ethiopia to the cup in your hands — the same patience."_
TITLE: _An Old Ceremony_ · SUB: FROM JEBENA TO POUR-OVER · LINE: a thousand years, one gesture

**Scene 16 — 2:31–2:40**
VO: _"Water meets ground, and time does the rest."_
SUB: THE POUR · LINE: slow water, dark gold

**Scene 17 — 2:40–2:50**
VO: _"And finally — the cup. Warm, certain, earned."_
TITLE: _The Cup_ · SUB: EARNED, NOT MADE · LINE: the end of a long journey

---

### ACT V — CONNECTION & INVITATION (2:50–3:38)

**Scene 18 — 2:50–2:59**
VO: _"Coffee was never only about coffee."_
SUB: MORE THAN A DRINK · LINE: it is how we gather

**Scene 19 — 2:59–3:09**
VO: _"It is a table shared. A conversation that stays."_
TITLE: _Together_ · SUB: THE SHARED TABLE · LINE: stories poured between cups

**Scene 20 — 3:09–3:18**
VO: _"Every cup carries the hands that grew it, and the fire that made it."_
SUB: FROM MANY HANDS · LINE: origin you can taste

**Scene 21 — 3:18–3:28**
VO: _"This is the soul of coffee — care, given time."_
TITLE: _Care, Given Time_ · SUB: OUR PROMISE · LINE: nothing rushed, nothing wasted

**Scene 22 — 3:28–3:38**
VO: _"We invite you to taste the whole journey."_
TITLE: _Taste the Journey_ · SUB: [BRAND NAME] · LINE: roasted in small batches, with patience

---

### OUTRO / LOGO — 3:38–4:00

**VO (opt):** _"[Brand Name]. The soul of coffee — from origin to ritual."_
**ON-SCREEN:**

- TITLE: _The Soul of Coffee_
- (LOGO inks in)
- SUB: [BRAND NAME]
- LINE: [website] · [tagline]
- (slow fade to paper texture)

---

## 4. STORYBOARD (scene-by-scene)

Columns: **#** · **In–Out** · **Image asset** · **Ink-reveal style** · **Ken Burns move** · **Selective color** · **Transition out**

Ink-reveal styles: `bloom` (single ink blot spreads from center), `sweep` (ink wipes L→R), `scatter` (multiple splatters fill in), `drip` (reveals top→down).
Ken Burns: direction + scale (e.g., `push-in 1.0→1.08`, `pan-left`, `pull-out`).

| #     | In–Out    | Image (file)             | Reveal       | Ken Burns         | Selective color           | Transition out  |
| ----- | --------- | ------------------------ | ------------ | ----------------- | ------------------------- | --------------- |
| Intro | 0:00–0:11 | 00-hills-dawn.jpg        | bloom (slow) | push-in 1.0→1.06  | warm dawn gold            | ink-wipe        |
| 1     | 0:11–0:20 | 01-highlands.jpg         | bloom        | push-in 1.0→1.08  | green valleys             | scatter-wipe    |
| 2     | 0:20–0:29 | 02-arabica-shrub.jpg     | scatter      | pan-left          | leaf green                | ink-wipe        |
| 3     | 0:29–0:38 | 03-goats-herder.jpg      | sweep        | push-in           | earth/red                 | drip-wipe       |
| 4     | 0:38–0:47 | 04-world-map-vintage.jpg | drip         | pull-out 1.08→1.0 | sepia + faint blue        | ink-wipe        |
| 5     | 0:47–0:56 | 05-red-cherries.jpg      | bloom        | push-in 1.0→1.10  | cherry red (strong)       | scatter-wipe    |
| 6     | 0:56–1:06 | 06-hands-picking.jpg     | scatter      | pan-right         | red + skin tone           | ink-wipe        |
| 7     | 1:06–1:15 | 07-harvest-baskets.jpg   | sweep        | push-in           | red/brown                 | drip-wipe       |
| 8     | 1:15–1:25 | 08-drying-beds.jpg       | drip         | pan-left          | warm sand                 | ink-wipe        |
| 9     | 1:25–1:34 | 09-green-beans.jpg       | bloom        | push-in           | muted green               | scatter-wipe    |
| 10    | 1:34–1:44 | 10-roaster-drum.jpg      | scatter      | push-in 1.0→1.10  | amber/fire orange         | ink-wipe        |
| 11    | 1:44–1:53 | 11-roasted-beans.jpg     | bloom        | pull-out          | deep brown + amber        | drip-wipe       |
| 12    | 1:53–2:03 | 12-roaster-hands.jpg     | sweep        | pan-right         | warm brown                | ink-wipe        |
| 13    | 2:03–2:12 | 13-grinder.jpg           | bloom        | push-in           | warm grey                 | scatter-wipe    |
| 14    | 2:12–2:22 | 14-bloom-steam.jpg       | scatter      | push-in 1.0→1.08  | crema brown + steam white | ink-wipe        |
| 15    | 2:22–2:31 | 15-jebena-pour.jpg       | sweep        | pan-left          | terracotta                | drip-wipe       |
| 16    | 2:31–2:40 | 16-pour-over.jpg         | drip         | push-in           | dark gold                 | ink-wipe        |
| 17    | 2:40–2:50 | 17-finished-cup.jpg      | bloom        | push-in 1.0→1.06  | crema + warm              | scatter-wipe    |
| 18    | 2:50–2:59 | 18-cafe-window.jpg       | scatter      | pan-right         | warm interior             | ink-wipe        |
| 19    | 2:59–3:09 | 19-shared-table.jpg      | sweep        | push-in           | warm skin/wood            | drip-wipe       |
| 20    | 3:09–3:18 | 20-hands-cup-closeup.jpg | bloom        | push-in           | crema + skin              | ink-wipe        |
| 21    | 3:18–3:28 | 21-beans-scattered.jpg   | scatter      | pull-out          | rich brown                | scatter-wipe    |
| 22    | 3:28–3:38 | 22-barista-portrait.jpg  | bloom        | push-in 1.0→1.08  | warm portrait             | ink-wipe (slow) |
| Outro | 3:38–4:00 | 23-cup-on-wood.jpg       | bloom (slow) | push-in 1.0→1.05  | warm, fading              | fade to paper   |

**On-screen text positions** (consistent = professional): titles lower-left third, subtitles directly under titles, supporting line under subtitle. Keep a 7–8% safe margin from all edges. Occasional faint Latin/handwritten text fragments float in the negative space (decorative only — like the reference). Music swells at Act transitions (scenes 5, 9, 13, 18) and resolves on the outro.

---

## 5. ASSET LIST (source these → drop into the folder structure)

> ⚠️ **For a paid client deliverable, verify each asset's commercial license and keep a record.** Unsplash/Pexels = free for commercial use, no attribution required. Pixabay = Pixabay license (free commercial). Google Fonts = open source (commercial OK). LottieFiles / Freepik = check the individual asset license; many free assets require attribution. Music libraries vary — read the license per track.

### Folder structure (Claude Code expects these paths)

```
soul-of-coffee/
├── index.html
├── assets/
│   ├── textures/
│   │   ├── paper.jpg              # aged cream paper, ≥3840px wide
│   │   ├── grain.png             # film-grain overlay (transparent)
│   │   ├── vignette.png          # optional; can be CSS instead
│   │   ├── watercolor-1.png      # watercolor wash, transparent PNG
│   │   ├── watercolor-2.png
│   │   ├── watercolor-3.png
│   │   ├── ink-splatter-1.png    # black ink shape, transparent — used as MASK
│   │   ├── ink-splatter-2.png
│   │   ├── ink-splatter-3.png
│   │   └── ink-splatter-4.png
│   ├── mattes/                    # OPTIONAL enhancement (see note)
│   │   └── ink-reveal.json        # Lottie ink-spread reveal (optional)
│   ├── fonts/
│   │   ├── PinyonScript-Regular.woff2
│   │   ├── MarcellusSC-Regular.woff2
│   │   └── Spectral-Regular.woff2  (+ Spectral-Medium, Spectral-Italic)
│   ├── images/
│   │   ├── 00-hills-dawn.jpg ... 23-cup-on-wood.jpg   # 24 photos (see storyboard)
│   ├── audio/
│   │   ├── music.mp3              # ~4:00 cinematic/acoustic bed
│   │   ├── sfx-ink-whoosh.wav     # ink splatter transition sound
│   │   ├── sfx-paper.wav          # subtle paper texture sound
│   │   └── vo/ (optional)         # 24 ElevenLabs VO clips if using narration
│   └── brand/
│       ├── logo.svg               # client logo, transparent
│       └── brand-colors.txt       # client hex codes if provided
```

### A) Style backbone (reusable across ALL scenes — source these FIRST, they unlock the look)

| Asset                        | What to search                                           | Source                            | Notes                                                                                                        |
| ---------------------------- | -------------------------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Aged paper texture           | "old paper texture", "vintage parchment"                 | Unsplash / Pixabay                | Cream/grey, subtle, high-res. This is your canvas.                                                           |
| Film grain overlay           | "film grain png transparent", "grain overlay"            | Pixabay / search PNG              | Transparent PNG; used with `mix-blend-mode: overlay`.                                                        |
| Watercolor washes (×3)       | "watercolor wash png transparent"                        | Pixabay / Freepik (check license) | For color bleeds. Muted, earthy.                                                                             |
| Ink splatter shapes (×4)     | "ink splatter png transparent black"                     | Pixabay / Freepik (check license) | **Critical — these become the reveal masks.** Get varied shapes (round blot, scattered, elongated).          |
| Ink-reveal Lottie (optional) | "ink reveal", "watercolor reveal", "brush stroke reveal" | LottieFiles                       | OPTIONAL. The code generates the spread itself; a Lottie matte makes it more organic if you find a good one. |

> **Note on the "paint-in":** You do **not** need a perfect animated matte. The reference look is achieved in code — an ink-splatter PNG used as a CSS `mask-image`, scaled up by GSAP, with an SVG turbulence filter warping the edges. The Lottie matte is a _nice-to-have_, not a blocker. Don't get stuck hunting for it tonight.

### B) Fonts (Google Fonts — download the .woff2 and self-host for deterministic render)

| Role                          | Font              | Why                                                               |
| ----------------------------- | ----------------- | ----------------------------------------------------------------- |
| Display script (titles)       | **Pinyon Script** | Elegant copperplate calligraphy — the reference's signature look. |
| Uppercase labels (subtitles)  | **Marcellus SC**  | Refined Roman small-caps; vintage, legible.                       |
| Supporting serif (body lines) | **Spectral**      | Warm, literary serif; Regular + Medium + Italic.                  |

> All three are open-source and free for commercial use. **Avoid** Playfair/Cormorant/EB Garamond/Cinzel — Hyperframes' skill bans them and they read as "default vintage." The trio above is more distinctive.
> Download: fonts.google.com → get the `.woff2` files → put in `assets/fonts/`. Self-hosting (not the Google CDN link) guarantees the headless renderer has them.

### C) Imagery (24 photos — Unsplash / Pexels, free commercial)

Search terms per scene (grab the highest-res landscape/16:9-croppable version):

- 00 `coffee plantation hills dawn` · 01 `ethiopia highlands landscape` · 02 `coffee plant arabica shrub` · 03 `goat herder mountains` (or vintage goat illustration) · 04 `vintage world map` · 05 `red coffee cherries branch` · 06 `hands picking coffee cherries` · 07 `coffee harvest basket` · 08 `coffee drying beds sun` · 09 `green coffee beans` · 10 `coffee roaster drum machine` · 11 `roasted coffee beans closeup` · 12 `roaster hands coffee` · 13 `coffee grinder` · 14 `coffee bloom pour steam` · 15 `ethiopian jebena coffee pot` · 16 `pour over coffee` · 17 `cup of coffee crema` · 18 `cafe window warm light` · 19 `people sharing coffee table` · 20 `hands holding coffee cup` · 21 `coffee beans scattered wood` · 22 `barista portrait` · 23 `coffee cup on wooden table`

> Aim for images that are **already a bit warm/earthy** — the watercolor treatment amplifies what's there. Avoid busy, cool-toned, or low-res shots.

### D) Audio

| Asset               | What to look for                                                              | Source                  | License caution                                                                                |
| ------------------- | ----------------------------------------------------------------------------- | ----------------------- | ---------------------------------------------------------------------------------------------- |
| Music bed (~4:00)   | "cinematic acoustic emotional", "documentary piano", "warm folk instrumental" | Pixabay Music / Uppbeat | **Verify commercial license for client use.** Uppbeat free tier needs credit; paid removes it. |
| SFX: ink whoosh     | "whoosh", "ink splash", "swoosh transition"                                   | Pixabay / Freesound     | One good whoosh, reused per transition.                                                        |
| SFX: paper/ambience | "paper rustle", "soft ambience"                                               | Pixabay / Freesound     | Subtle, low volume.                                                                            |
| VO (optional)       | ElevenLabs — warm, measured narrator voice                                    | ElevenLabs              | 24 lines from the script. Adds a pipeline step; optional.                                      |

### E) Brand (from your client — ask for these)

- Logo as transparent **SVG** (preferred) or high-res PNG.
- Brand hex colors (if any) — otherwise we use the warm sepia palette below.
- Website + tagline for the outro.
- Any approved product/lifestyle photos (can replace stock in Act IV–V).

---

## 6. DESIGN TOKENS (hand these to Claude Code with Prompt 1)

```
/* Palette — warm sepia/heritage */
--paper:      #efe7d6;   /* visible paper tone */
--ink:        #2b2622;   /* near-black warm ink for text */
--ink-soft:   #5a5048;   /* muted brown for supporting text */
--accent:     #8c5a3c;   /* roasted-bean warm accent */
--accent-dim: #c9a87f;   /* faded gold */
--bleed-warm: #b5762e;   /* color-bleed tint (warm) */
--bleed-cool: #4a6a78;   /* occasional cool bleed (skies) */

/* Type */
--font-script: "Pinyon Script", cursive;     /* titles */
--font-label:  "Marcellus SC", serif;        /* uppercase subtitles */
--font-body:   "Spectral", serif;            /* supporting lines */

/* Scene rhythm */
--scene-default: 9s;
--reveal-dur:    1.8s;   /* ink paint-in duration */
--text-delay:    0.9s;   /* text fades up after reveal starts */
--kenburns-scale: 1.08;
```

Letter-spacing on the uppercase labels (`Marcellus SC`) should be generous (~0.18em). Titles (`Pinyon Script`) large — 90–130px on 1080p. The whole frame sits at ~88% brightness with grain on top — never pure white, never pure black.

---

## 7. REALITY CHECK & THE SMART PATH FOR THE MORNING

Read this once — it's the difference between delivering and panicking.

1. **Can code match an After Effects watercolor template exactly?** Same _family_, yes — convincingly. Pixel-identical, no. The "paint-in" + watery edges are reproduced with an SVG turbulence filter + animated ink mask (specified in Prompt 1). With good sourced ink-splatter + paper + grain PNGs, it reads as the same style at a glance. That's a deliverable.
2. **4 minutes is a big render.** ~7,200 frames captured from headless Chrome takes real time and iteration. So: **build and perfect ONE hero scene first (Prompts 0–1), render it as a still + a 9-second clip, and confirm the look.** Only then mass-produce.
3. **Build in deliverable checkpoints.** After Prompt 4 you'll have a polished ~40-second slice (intro + a few scenes + outro) — that alone is a respectable teaser you could send if time runs out. After Prompt 7 you have the full 4 minutes.
4. **If you're short on time:** ship a tight, _fully polished_ **75–90 second cut** (intro + 6 best scenes + outro) rather than a rushed, rough 4 minutes. A short film that's flawless beats a long one that stutters. Tell the client it's the "hero cut" and the full-length follows. (Prompt 6b covers this.)
5. **Lock the template before scaling.** 90% of "it looks off" problems are in scene 1. Get scene 1 right and the rest inherits it.

You've got this. Source the backbone assets (paper, grain, 4 ink splatters, 3 fonts) + the first 3–4 photos, then run Prompt 0 and Prompt 1 tonight. That's the whole game.
