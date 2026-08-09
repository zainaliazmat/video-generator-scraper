---
summary: Deep design research on Swiss/International Typographic Style (specifically Vignelli) as a video style for the finance channels, under the hard constraint that every frame carries a photograph. Answers the central tension with primary sources, then specs four implementable directions.
updated: 2026-07-30
source: The Vignelli Canon (RIT Vignelli Center PDF, read directly), NPS Unigrid Design Specifications (npshistory.com, read directly), plus secondary sources on Müller-Brockmann, Hofmann, Matter, Ruder, Gerstner, NYCTA. Read-only research pass; no repo files modified.
status: research — not yet a decision. blockframe-9 remains the architecture_lock.
---

# Swiss / Vignelli as a finance-video style

**The question is not "what does Swiss look like."** It is: *does this tradition
have a real mechanism for putting a photograph in a strict grid, such that every
frame carries one?*

**Answer: yes, and it is written down.** Vignelli specified it twice — once in
the Canon, once as a production system (Unigrid) for the National Park Service,
which is the closest historical analogue to what this pipeline is: a
template-driven, mass-produced, photograph-heavy series made by many hands to a
fixed spec. That is the finding that decides everything below.

---

## 1. The tradition, from primary sources

### 1.1 What Vignelli actually says

All quotations below are from *The Vignelli Canon* (Massimo Vignelli, 2009/2010),
read directly from the Vignelli Center PDF. Page numbers are the book's own.

**On the grid** (p.40) — FACT:

> "The basic understanding is that the smaller the module of the grid the least
> helpful it could be. We could say that an empty page is a page with an
> infinitesimal small grid. Therefore, it is equivalent to not being there.
> Conversely a page with a coarse grid is a very restricting grid offering too
> few alternatives. The secret is to find the proper kind of grid for the job at
> hand."

> "Sometimes, in designing a grid we want to have the outside margins small
> enough to provide a certain tension between the edges of the page and the
> content. After that we divide the page in a certain number of columns
> according to the content, three, two, four, five, six, etc. Columns provide
> only one kind of consistency, but we also need to have an horizontal frame of
> reference … Therefore, we will divide the page from top to bottom in a certain
> number of Modules, four, six, eight, or more."

The Canon illustrates exactly five grids: **2×4, 3×6, 4×8, 5×4, 6×6** (p.42).
Nothing finer. Column count is small; module count is small.

**On gutters** (p.52) — FACT:

> "Depending on the size of the book we like to keep the space between the
> columns and the modules rather tight - ideally the size of a line of type."

**On the typeface list** (p.54) — FACT. The famous four, from the exhibition
*A Few Basic Typefaces*: **Garamond, Bodoni, Century Expanded, Helvetica.**
Then "I can add Optima, Futura, Univers …, Caslon, Baskerville and a few other
modern cuts." The specimen page in the book (p.56) shows six: Garamond 1532,
Bodoni 1788, Century Expanded 1900, Futura 1930, Times Roman 1931, Helvetica 1957.

The load-bearing sentence for us is the one immediately before the list:

> "In other words, is not the type but what you do with it that counts. **The
> accent was on structure rather than type.**"

**JUDGEMENT:** that sentence is the licence to keep Noto Sans. See §6.

**On type sizes** (p.68, p.72) — FACT:

> "Basically we stick to no more then two type sizes on a printed page, but there
> are exceptions. We like to play off small type with larger type - usually twice
> as big (for instance, 10 pt text and 20 pt headings)."

> "Our first rule is to stick to one or two type sizes at the most. If necessary,
> there are other devices such as bold, light, roman and italic to differentiate
> different parts of a text, but even there, stick to the minimum."

> "Some people who talk loud and tend to scream trying to persuade you, love to
> increase the size and weight of type to make the message louder. That is
> exactly what I consider intellectual vulgarity … **In a world where everybody
> screams, silence is noticeable.** White space provides the silence."

**On alignment** (p.66) — FACT:

> "Most of the time we use *flush left*. … It also makes more sense since in our
> culture we read from left to right and it is better for the eye to go to the
> next line than having to cope with hyphens all the time. However, it is
> important to control the shape of the rugged side by shifting sometimes the
> text from line to line to obtain a better profile."

> "We use *centered* for lapidary text, invitations, or any rhetorical
> composition where it may be more appropriate."

> "*Justified* is used more for text books, but it is not one of our favorites
> because it is fundamentally contrived."

**On rules** (p.70) — FACT, and directly implementable:

> "When using rulers I set a hierarchy of weights to clarify the different parts
> of the text. In a form, for instance, bolder rulers (2 pt) will separate major
> parts of the text, light rulers (1/2 pt or 1 pt) will separate items within
> each part of the form. In that situation the type between the rulers will be 8
> pt, always set closer to the ruler above. **Type should always hang from the
> ruler, regardless of the size.** This is another little but important detail of
> my Canon."

**On colour** (p.78) — FACT, and this is the answer to the money-colour problem:

> "Most of the time we use color as a Signifier, or as an Identifier. Generally
> speaking **we do not use color in a pictorial manner.** Therefore, we tend to
> prefer a primary palette of Red, Blue, and Yellow. … we tend to use it more as
> symbol or as an identifier."

> "There are times for strong primary colors and times for subtle pastel colors;
> there are times for just black and white; and times where rich browns and
> hearty colors work more appropriately to the task at hand."

**On white space** (p.92) — FACT:

> "I often say that in typography the white space is more important than the
> black of the type. … Tight margins establish a tension between text, images and
> the edges of the page. Wider margins deflate the tension and bring about a
> certain level of serenity to the page."

**On visual power** (p.24) — FACT:

> "difference of scale within the same page can give a very strong impact. Bold
> type contrasting with light type creates visually dynamic impressions."

### 1.2 The other figures, briefly

- **Josef Müller-Brockmann** — *Grid Systems in Graphic Design* (1981) gives
  grids of **8 to 32 grid fields**. FACT (publisher/collection descriptions): the
  method is that pictorial elements are reduced to a few formats of the same
  size, and picture size is determined by the picture's importance to the
  subject, not by what looks nice. That is a rule the pipeline can execute
  mechanically.
- **Emil Ruder** — *Typographie* (1967). FACT: his own description of the
  nine-square grid is that the pattern "is the means of establishing a formal
  unity between the different amounts of text and different sizes and shapes of
  pictures." Ruder treated photography+typography as one communication medium,
  not type over an image.
- **Karl Gerstner** — *Designing Programmes* (1964), subtitle *"instead of
  solutions for problems, programmes for solutions."* FACT: Gerstner's
  morphological box itemises the parameters of a design problem and generates the
  solution space, rather than producing one artefact. **JUDGEMENT:** this is the
  single most relevant idea in the whole tradition for an automated pipeline —
  the thing being designed here is not a video, it is a parameter set that yields
  a different-but-consistent video every run. It is also the intellectual
  argument *against* the sameness that the architecture lock currently risks.
- **Armin Hofmann** — Basel. FACT (Poster House, Cooper Hewitt): in the 1959
  *Giselle* poster the dancer is cropped at head and foot so the photograph
  "becomes a graphic symbol of movement rather than a three-dimensional image,"
  and the white lettering is mathematically related to the placement of the other
  elements. **This is the key photographic move of the tradition — the photograph
  is reduced to a tonal shape that participates in the composition, not a window
  you look through.**
- **Herbert Matter** — FACT (MoMA, Cooper Hewitt): the 1934–36 Swiss National
  Tourist Office posters (*Pontresina·Engadin*, *Engelberg·Trübsee*,
  *Winterferien*) are among the earliest effective photomontage posters: extreme
  scale contrast, subjects cropped out past the frame edge, type set into the
  photographic space rather than beside it. Precedent for "type reversed on the
  photograph" being *native* to this tradition, not a compromise.
- **NYCTA Graphics Standards Manual** (Vignelli + Bob Noorda, Unimark, 1970).
  FACT: modular sign panels at 1'×2' (information), 1'×4' (direction), 1'×8'
  (station ID); typeface Standard Medium (Akzidenz-Grotesk) because Helvetica
  metal wasn't affordable to ship; the black bar / white band is the system's
  recurring device. Relevance: **the aperture is the identity.** A fixed
  recurring rectangle is what makes heterogeneous content read as one system.

---

## 2. The photography question, answered

### 2.1 The Unigrid spec — three named mechanisms

*Unigrid Design Specifications, National Park Service Informational Folder
Program* (Vignelli Associates, system from 1977; spec sheet read directly). This
is the primary evidence. It has a section headed **Pictorial Features** that
names exactly three ways a photograph enters the grid. FACT, quoted:

> "The Unigrid System handles text as text and illustration as illustration; the
> elements are separate and distinct. Pictorial treatments therefore follow
> certain approaches supporting this division.
>
> **The first of these is a band, or toned panel, in which pictures and
> photographs are clustered to set them off from text or map.** When color
> photographs are used, this band is often black for maximum contrast. Neutral
> background colors are used for more muted effects.
>
> **A second method is to locate pictorial subjects in the cover assembly.** This
> may be a single dramatic entry, or many pictures, presented in multiples of the
> grid from small parts up to two, three, or four large segments.
>
> **A third method is to assemble pictures and story in an illustrated essay in
> which visual images dominate.** The illustrated essay requires the full width
> of the broadside and lets pictures be composed against a toned field and set
> apart. Users can thus view a range of interpretive information much as they
> might an exhibit. As with illustrated charts, this technique juxtaposes large
> and small images in a pattern of major and minor pictorial themes. Text is
> integrated with pictures much like captions for an exhibit."

Three mechanisms, in the designer's own production spec, for a system whose whole
job was photographs in a grid at scale. **Mechanism 1 → Direction 1.
Mechanism 2 → Direction 2. Mechanism 3 → Direction 3.**

The same spec gives the type-over-photograph rule (FACT):

> "All titles reverse in white against a 100 point black edge bar. Park names
> with fewer than 12 letters are set in 60 point Helvetica Medium C/lc flush left
> with the first grid module. … All type is hung 10 points below the top trim.
> **The title bar is used in combination with a single-color cover panel, or it
> can be used with a pictorial panel.**"

And on bars (FACT):

> "the horizontals are accented through the placement of type, by the use of
> horizontal margins, and especially by the use of bars and toned divider panels.
> These devices organize and contain the layout. … The 25 point bottom and
> divisional bars, like the title bar at the top, are accented through the
> placement of type. **The dominant black tone of these dividing elements sets
> off text and other information, making it easier to locate.**"

And on the cover concept (FACT) — note that Vignelli explicitly *rejects* the
idea of a special hero frame, which maps directly onto "every scene is a scene":

> "The Unigrid cover concept insists on a purposeful approach to a folder's
> introductory passages. No longer is the cover a miniature poster set apart from
> the main body of the presentation. … The black band with its standardized site
> designation is, in a sense, the cover. Its complement is the folder's text,
> map, and pictures taken in their entirety."

Real module numbers from the spec, for calibration (FACT):

> "The vertical spaces between modules are always 1 pica wide. The horizontal
> spaces between modules are always 10 points high. For the B-module, the width
> is 7 picas, and the height is the same 80 points." (A-module: 6½ picas × 80 pt.)

> "Margins, like other components in the Unigrid System, must be handled with
> precision. The vertical margins are established by the grid. Horizontal margins
> must consistently carry a 40 point space above text entries to provide a
> fascia, or horizontal baseline. … The margin below a bank of text carries at
> least a 20 point drop."

So: **module ≈ 80pt tall, gutters 10–12pt, i.e. gutter ≈ 1/7 of the module.**
That ratio is what I use below.

### 2.2 The Canon's rules for photographs in a grid

FACT, Canon p.48 (Grids for Books):

> "It is a good practice to relate the grid to the proportion of the majority of
> pictures, so that there will be the least need for cropping their images."

FACT, Canon p.52 — this is the single most precise statement of the mechanism:

> "One element of refinement is to plan a grid in such a way that **type and
> illustrations follow the same exact grid**. To do that a specific leading
> should be determined for the type area of each module with **the illustration
> modules coinciding**. This gives great elegance of detail to the printed page."

FACT, Canon p.80 (Layouts):

> "Most publications are composed of text, images and captions and the task of
> the designer is to sift through the images to select those which best portray
> the essence of the content and possess the quality of becoming an icon. **An
> icon is an image that expresses its content in the most memorable way.**"

> "In defining the grid, one has to keep in mind what kind of visual material
> will comprise the layout. For square pictures a square grid may be better than
> a rectangular one, well suited for rectangular images. Or, if the publication
> has a consistent variety of the two formats, one could design a double grid
> accommodating both situations. **Or, otherwise, when appropriate, crop the
> picture to follow the grid.**"

### 2.3 The Sequence passage — a shot list, not a layout

FACT, Canon p.84. This is the most directly transferable thing in the book,
because it is about *rhythm across frames*, which is what a video is:

> "A publication, whether a magazine, a book, a brochure, or even a tabloid is a
> **cinematic object** where turning of the pages is an integral part of the
> reading experience. A publication is simultaneously the static experience of a
> spread and the cinematic experience of a sequence of pages."

> "We like the layouts to be forceful. **We do not like limpy layouts with little
> pictures spreaded around the pages - some bleeding here, some bleeding there in
> a casual way.**"

> "The book layout we tend to favor is a very simple format of **a page of text
> beside a picture on a full bleed page, followed by a full bleed picture spread,
> followed by a page with a full bleed picture facing a white page with a picture
> - either on the center or upper right corner.** A simple format gives rewarding
> results when the basic sequence is articulated in a way that is not repetitive."

**JUDGEMENT:** that is a three-beat cycle of layouts. For a nine-scene video it
is directly usable as the anti-sameness engine: the system is not one frame
repeated nine times, it is a declared sequence of apertures. This addresses the
exact risk the `architecture_lock` created — locking a layout is not the same as
locking a *frame*, and Vignelli's own practice locks the system while varying the
aperture.

### 2.4 Summary of mechanisms, as things a build agent can implement

| # | Mechanism | Named source | Photo placement | Type coexists by |
|---|---|---|---|---|
| M1 | **Toned band / picture strip** | Unigrid "Pictorial Features", method 1 | full-width horizontal band, fixed aspect, hard edges | living in a black title bar above and a flat panel below — never on the photo |
| M2 | **Cover assembly / picture block** | Unigrid method 2; Canon Sequence | one large block occupying an integer run of columns, full bleed on its outer edges | occupying the complementary columns, flush left on flat ground |
| M3 | **Illustrated essay / mosaic** | Unigrid method 3 | 2–4 rectangles, each an integer number of modules, major + minor themes | as captions inside or beside rectangles, hung from the rectangle's top rule |
| M4 | **Reversed field** | Hofmann *Giselle*; Matter tourism posters; Müller-Brockmann *Schützt das Kind* | full bleed, graded down to a tonal mass | reversed white, on a *hard-edged tone block* aligned to a column line — not a soft scrim |
| M5 | **Type hangs from a rule** | Canon p.70 | — | every text block sits under a rule that spans a known column run |
| M6 | **Grid derived from the picture** | Canon p.48, p.80 | choose the module so the majority of pictures need least cropping; else crop to the grid | — |

All five placement mechanisms carry a photograph. **None of them requires the
photograph to be absent.** The popular imitation of Swiss style is image-free;
the actual practice is not. That is the whole answer to the central tension.

---

## 3. Motion — what survives, what breaks

FACT: this is a print tradition. There is no canonical Swiss motion spec. The
honest state of the evidence: the recurring claim in motion-design writing is
that Swiss principles "perfectly work in digital motion", and the most-cited
concrete work is Jon Yablonski's CSS/JS re-creations of Hofmann, Neuburg and
Müller-Brockmann posters as animated compositions — i.e. an exercise, not a
broadcast package. Searches for a named 2025–26 broadcast package built on Swiss
grid principles returned nothing specific; motion-identity writing talks about
"consistent wipes and reveals" generically. **JUDGEMENT: treat the motion design
as ours to derive from the print principles, and say so, rather than pretending
there is a lineage to copy.**

### What survives animation — JUDGEMENT, derived from the principles

1. **The rule draw.** A rule is a line with a start and an end; drawing it
   (`scaleX` from 0, `transform-origin: left`) is the most native motion the
   tradition has. It is literally the gesture of ruling a line. 0.4–0.5s,
   `power2.out`.
2. **Type hanging from the rule.** Canon p.70 says type hangs from the ruler.
   In motion: the rule draws, then the type descends a *small* distance (10–16px,
   not 40) into its hanging position. The move has a reason, which is the test.
3. **The module wipe.** A rectangle is a grid cell; revealing it along its long
   axis with a hard `clip-path: inset()` edge is a grid operation. Crucially it
   is **hard-edged** — a wipe, not a fade. Fades are the anti-Swiss motion because
   they dissolve the edge, and the edge is the design.
4. **Scale contrast as an event.** Canon p.24: difference of scale gives impact.
   A number arriving at 4× the size of everything else, on a beat, is a Swiss
   move. It is also what the money hero already does.
5. **Sequence.** Canon p.84 already frames publication as cinematic. Changing the
   *partition* between scenes — the photograph moving from right block to full
   band to left block — is the motion at the video's scale.
6. **The grid reveal.** Drawing the hairline grid itself, once or twice per video,
   as a stagger. This is the only "decorative" move I'd permit, and it earns its
   place because it states the system out loud.

### What breaks — JUDGEMENT

- **Ken Burns at current amplitude.** `1.0 ↔ 1.16` with ±2.5 xPercent is a
  *soft, continuous, unmotivated* move. Inside a hard-edged aperture it reads as
  the picture sloshing in its frame. Halve it (1.0→1.06) inside a band or block;
  in a mosaic, run it on at most one rectangle.
- **The cross-dissolve.** `dissolve(0.45s)` between scenes is exactly the soft
  boundary the tradition avoids. **But**: it exists for a documented reason —
  `ffmpeg scdet` measured 5.85–10.72 boundary deltas and five of eight boundaries
  tripped a generic cut detector (blockframe doc §5 rule 0). Do not delete it.
  Replace it with a **hard wipe of the same duration** — a directional
  `clip-path` sweep is still a gradual pixel change over 0.45s, so it satisfies
  the cut detector, and it is stylistically correct. This needs measuring with
  `scdet` before shipping, not assuming.
- **`back.out(1.7)` overshoot** (`pop`, `popEach`, the stamp slam). Overshoot is
  expressive/cartoon easing. It has no place. `power3.out` / `power4.out` /
  `expo.out` only.
- **`breathe`.** A slow yoyo scale to "keep an element alive" is decoration with
  no reason. Retire it in `.swiss`. Silence is the point.
- **Rotation.** `.stamp { rotate(-4deg) }` breaks the grid by definition.
- **`drift`.** Same argument as breathe.

### The static-frame problem

blockframe doc §5 rule 2: *"No scene may hold a static frame beyond ~2s."* That
rule was written for an architecture where the photo *is* the frame, so the photo
had to move. In a Swiss variant the frame contains rules, blocks and apertures
that can move *instead of* the photograph. **JUDGEMENT: the rule should be
restated as "no frame may be motionless beyond ~2s," not "the photo must move."**
Otherwise the style is forced to keep the one move that fights it hardest.

---

## 4. Four directions

Common to all four:

- Body class on `#root`, e.g. `<div id="root" class="swiss-band">`. Same pattern
  as the existing `.rail`.
- **Every scene carries a photograph.** Non-negotiable; `format.json`
  `image_per_scene: true` and `doctor` already enforce it structurally.
- Typeface unchanged: `--font` / FinanceSans (Noto Sans var, 100–900, carries ₹).
- Tokens reused: `--bg --panel --ink --muted --fund --warn --target --pop --edge`.
- **All radii → 0.** `.chip`, `.claim`, `.colcard`, `.billrow`, `.cta` are
  rounded; in a Swiss variant they are square.
- **No rotation, no overshoot, no soft scrim, no per-scene `--tint`.**
- **Two type sizes per scene**, in roughly a 1:2.5–1:4 ratio, both drawn from the
  existing 16-step ladder. Third size permitted only for the 26px foot line.
- Flush left, ragged right. `text-align: left` everywhere.
- Grain layer stays (`opacity 0.05`, overlay). It is the one non-Swiss thing I'd
  keep, because it is the only thing preventing the frame reading as a PDF.

---

### Direction 1 — `.swiss-band` · **THE UNIGRID BAND**

*Unigrid Pictorial method 1: "a band, or toned panel, in which pictures and
photographs are clustered … often black for maximum contrast."*

**Grid (1920×1080).** 12 columns × 8 rows.
- Side margins **100px**. Column width **125px**, gutter **20px**.
  Check: `12×125 + 11×20 = 1500 + 220 = 1720`; `1720 + 200 = 1920`. ✓
- Column *n* (1-indexed) left edge: `x = 100 + (n−1)×145`.
- Top/bottom trim **60px**. Row pitch **120px**, 8 rows: `60 + 8×120 + 60 = 1080`. ✓
- Row *m* top edge: `y = 60 + (m−1)×120`.
- Gutter:module ratio 20:125 ≈ 1:6.25 — matches Unigrid's ~1:7. FACT-anchored.

**Where the photograph lives.** A **full-bleed horizontal band, rows 2–6**:
`x 0→1920, y 180→780`, **1920 × 600**, `background-size: cover`. Aspect **3.2:1**.
The band bleeds past the side margins — the grid governs its *height*, the frame
governs its width. This is the recurring aperture, identical in every scene of
every video: nine unrelated stock photos are cropped into one shape.

**Type.**
- **Title bar**, row 1: `x 0→1920, y 60→180`, solid `var(--bg)`, full bleed.
  Headline reversed `--ink`, flush left at `x=100`, **hung 26px below the bar's
  top edge** (Unigrid: type hangs 10pt below top trim). Size 84px / weight 800,
  tracking −1px. Right end of the bar: the 26px `--muted` kicker, flush right at
  `x=1820`, uppercase, tracking 4px.
- **Statement panel**, rows 7–8: `y 780→1020` on flat `--bg`. A **3px `--ink`
  rule at y=780** spanning `x 100→1820`; the statement **hangs from it**, top at
  `y=812`, flush left at `x=100`, 54px / weight 500, max 3 lines, measure capped
  at columns 1–9 (`x 100→1405`).
- **Foot**, `y 1020→1080`: 26px `--muted` source line flush left at `x=100`;
  scene index (`03 / 09`, tabular, weight 200) flush right at `x=1820`.

**The money number.** Two permitted forms, one per video:
1. *In the panel* — replaces the statement: 200px / weight 900, tabular, flush
   left at `x=100`, hanging from the same 3px rule. Currency mark at `0.5em` /
   weight 400 (Canon: play small type off large, roughly 2×).
2. *Reversed in the band* — 240px / weight 900 `--ink`, flush left at `x=100`,
   baseline on row 5 (`y=660`), sitting on the photograph. Permitted **only**
   when the image's left third has been measured below 25% luminance. This is the
   Hofmann *Giselle* move and it should happen **once per video**, on the hero.

**Motion.**
- Band opens: `clip-path: inset(50% 0 50% 0)` → `inset(0)`, 0.6s `power4.out` —
  the aperture irising open on its horizontal axis.
- Title bar type: rise **16px** only, 0.45s `expo.out`, +0.15s after the band.
- Statement rule: `scaleX 0→1`, origin left, 0.45s `power2.out`. Statement text
  hangs 12px down into place 0.15s later.
- Ken Burns inside the band at **half amplitude**: `1.0 ↔ 1.06`, `xPercent ∓1.2`.
  Alternate direction per scene as today.
- Scene boundary: **hard directional wipe**, 0.45s (same duration as today's
  dissolve, so the scene-arithmetic and the cut-detector argument both hold).

**Why this channel, not pastiche.** The 3.2:1 aperture is doing the job the
`grayscale(0.32)` grade currently does — unifying nine unrelated photographs —
but geometrically, which is more robust than a filter. And the title bar's right
slot is where the ₹/$ channel mark lives, which is Unigrid's standardised
site-designation doing brand work rather than an added logo.

**Stock video.** Best host of the four. A 1920×600 aperture over a 16:9 clip
shows only the middle **55%** of the frame, which is exactly where stock footage
is least incriminating — no watermark corners, no edge-of-set, faces usually
croppable out. Loop 6–10s, cross-fade the loop point inside the band. Grade to
`grayscale(0.6) brightness(0.6)`. **Turn Ken Burns off entirely when the band
holds video** — a moving image inside a moving aperture is two motions arguing.

---

### Direction 2 — `.swiss-col` · **THE PICTURE COLUMN**

*Unigrid Pictorial method 2 (cover assembly) + Canon p.84 ("a page of text beside
a picture on a full bleed page").*

**Grid.** Same 12 × 8 field as Direction 1 (125/20/100, 120/60).

**Where the photograph lives.** A **full-height block**, `y 0→1080`, occupying
columns 7–12 **plus the right margin**: `x = 100 + 6×145 = 970 → 1920`.
**950 × 1080**, ratio **0.88:1** — near-square, which per Canon p.80 is a
deliberate grid-to-picture decision, and which is a shape essentially no finance
channel uses.

**The alternation is the system.** Odd scenes: photo right (cols 7–12), type in
cols 1–5. Even scenes: photo left (`x 0→950`), type in cols 8–12
(`x 1115→1820`). This is Canon p.84's sequence rule, and it is the cheapest
deterministic variance axis available to the pipeline.

**Type.** Measure = columns 1–5, `x 100→805` (705px), flush left, ragged right.
- Kicker: hangs from a 2px `--muted` rule at `y=180`; 30px, uppercase, tracking 4px.
- Headline: top at `y=300`, 96px / weight 800, ≤4 lines.
- Money figure: hangs from a **4px `--ink` rule at `y=640`**, baseline block
  `y 672→872`, 200px / weight 900, tabular. Currency mark 0.55em / weight 400.
- Foot: `y=960`, 26px `--muted`.
- Scene index: vertical, `writing-mode: vertical-rl`, in the outer margin at
  `x=40`, weight 200, 30px, `--muted` at 0.5 opacity. (Reuses `.rail`'s
  `.raillabel` trick.)

**Money number.** As above — it is the only large element besides the headline,
and the two never appear together (blockframe §5 rule 4 survives unchanged).

**Motion.**
- Photo block: hard wipe `clip-path: inset(0 100% 0 0)` → `inset(0)`, 0.55s
  `power4.out`, direction matching the side the photo sits on.
- Each rule draws (0.35s), its type hangs down 12px 0.15s after (0.4s `expo.out`).
- Ken Burns **full amplitude** here (`1.0 ↔ 1.16`) — a tall narrow crop hides a
  scale move better than a wide one.
- Scene boundary: the photo block **slides across** the frame from one side to
  the other on the alternating scenes (0.5s `power4.out`), which is the module
  swap at its simplest and is genuinely striking.

**Why this channel.** The hard vertical edge on a column line plus a near-square
picture block is visibly a different product from the current centred stack.

**Stock video.** Second-best. A 950×1080 aperture is close to the standard 9:16
vertical crop, so most stock clips fit without exposing edges. Grade
`grayscale(0.5)`. Ken Burns off when video plays.

**Honest assessment — this is the weakest of the four.** It is a refinement of
`ledger-rail`, which has already been costed and which the creator saw and passed
over. The L/R alternation and the hanging-rule type are real improvements, but
"open a new world" this is not.

---

### Direction 3 — `.swiss-mosaic` · **THE MODULE MOSAIC**

*Unigrid Pictorial method 3: "assemble pictures and story in an illustrated essay
in which visual images dominate … juxtaposes large and small images in a pattern
of major and minor pictorial themes."*

**Grid.** A **16 × 9 field of 120px modules**, full bleed, zero margin.
`16 × 120 = 1920` ✓, `9 × 120 = 1080` ✓. The module is derived from the format
itself, which is Vignelli's own method (Unigrid derives all ten formats from the
B6 sheet). Live module 108px inside a 120px cell — 6px inset each side, so the
gutter between adjacent cells is 12px. Ratio 12:108 = 1:9. Tight, per Canon p.52.

**Where the photographs live.** Every scene is a **partition of the field into
2–4 rectangles**, each an integer number of modules. **Hard rule: photographic
rectangles must cover ≥ 50% of the field.** The frame is a picture with type in
it, never the reverse.

A closed set of partitions the pipeline picks from, one per scene, never repeating
within a video:

| id | split | photo | type |
|---|---|---|---|
| P1 | 10 \| 6 vertical | cols 1–10 (`0→1200`) | cols 11–16 (`1200→1920`) |
| P2 | 6 \| 10 | cols 11–16 | cols 1–10 |
| P3 | 16×5 over 16×4 | rows 1–5 (`0→600`) | rows 6–9 (`600→1080`) |
| P4 | 11 \| 5, type block split | cols 1–11 major photo; cols 12–16 rows 6–9 **minor photo** | cols 12–16 rows 1–5 |
| P5 | 8 \| 8 | two photographs, `0→960` and `960→1920`, both full height | reversed on the darker one, measured |

P4 and P5 are what make this direction worth the build: they give the
**keyword-imagery rule a structural home**. Today a cut-in is a floating overlay
timed to a spoken word; here the "major and minor pictorial themes" language of
the Unigrid spec makes the cut-in a *module*. When the VO names a concrete thing,
that thing occupies a named rectangle.

**Type.** Inside any rectangle: inset 40px from the rectangle edge, flush left,
hanging from a 3px rule at the rectangle's top inset. Two sizes, 1:3.

**The money number.** Gets its **own module block**: a solid rectangle of exactly
n×m modules in `--fund` / `--warn` / `--target`, with the figure reversed in
`--bg` at 180px / weight 900. This is Vignelli's colour-as-identifier (Canon
p.78) and it converts `.stamp` from a rotated sticker into architecture.

**Motion — the module swap.** This is the direction's real asset and it is
genuinely new to this pipeline. On a scene change the field **re-partitions**:
rectangles that persist across the boundary stay put; rectangles that change
wipe in along their long axis, staggered **0.08s** in reading order (top-left to
bottom-right). Nothing crossfades. The frame reassembles.

Within a scene: rule draws, type hangs, one rectangle may run Ken Burns.

**Stock video.** Yes — but **cap at one moving rectangle per frame**. Two
independently-moving apertures inside a static grid reads as a CCTV wall. The
still rectangles are what make the moving one read as deliberate.

**Honest assessment.** Highest ceiling and highest risk. Highest build cost of
the four (a partition system, not a stylesheet). Real failure mode: it drifts
into looking like a Squarespace template or a BI dashboard. Guardrails: **max 4
rectangles, minimum rectangle 4 modules wide, ≥50% photographic coverage, no
rectangle smaller than 4×3 modules.**

---

### Direction 4 — `.swiss-reverse` · **THE REVERSED FIELD**

*Hofmann* Giselle *· Matter's tourism posters · Müller-Brockmann's* Schützt das
Kind *— the photograph is the field, reduced to a tonal mass, with type reversed
on it and a hard-edged tone block guaranteeing contrast.*

**Grid.** 12 × 8, same as Directions 1–2.

**Where the photograph lives.** **Full bleed**, `inset: -6%`, exactly like today.
The change is what happens to it:

- **Grade: `grayscale(0.85) brightness(0.55) contrast(1.25)`.** This is a real
  departure from `0.32 / 0.62 / 1.05`. At 0.32 the photograph still competes for
  attention as an image; at 0.85 it becomes what Hofmann made it — a grey tonal
  mass that participates in the composition as a shape.
- **The four-layer radial scrim is deleted.** In its place: **one hard-edged tone
  block**, `rgba(13,16,23,0.74)`, covering exactly the columns the type occupies
  — e.g. cols 1–6, `x 0→970`, full height, with a **hard vertical edge on a
  column line**. This is Unigrid's "toned panel". The point is that contrast
  becomes a *deterministic geometric guarantee* instead of a probabilistic
  gradient that happens to work on most photographs.
- **`text-shadow` off everywhere** (`.rail` already sets this precedent). A glow
  is a soft device; the tone block replaces it.

**Type.** Reversed `--ink`, flush left at `x=100`, everything hanging from rules.
Two sizes: **160px / weight 900** and **40px / weight 500**. Kicker 30px.

**The money number.** 260px / weight 900, reversed on the tone block, with a 6px
`--ink` rule above it spanning the block's width (`x 100→870`).

**The signature move — the visible grid.** On **exactly two scenes per video**,
the 12×8 hairline grid draws itself in over the photograph:
`1px rgba(245,243,236,0.20)`, verticals then horizontals, staggered, 0.9s,
`ease: none`, and stays. Müller-Brockmann's own book shows the grid; Vignelli
would hide it. Showing it twice is the statement of the system and it is the one
thing in these four directions a viewer will remember and describe to someone.

**Motion.** Tone block wipes in (0.5s `power4.out`) → rule draws (0.4s) → type
hangs (0.4s). Photograph runs Ken Burns at **full amplitude** behind it (nothing
is constraining it). Boundary: hard wipe, 0.45s.

**Stock video.** Easiest of all four, because structurally this *is* today's
architecture — full-bleed layer, different grade, hard-edged overlay. If moving
footage ships at all, ship it here first.

**Why this channel.** Cheapest to build (a grade change, a scrim replacement, an
alignment change, a rule system) and it changes the register completely. Also the
one that most obviously belongs to the *photographic* Swiss tradition rather than
the flat-colour one, which is precisely the objection the creator raised.

---

### The sequence layer — applies across all four

**JUDGEMENT, from Canon p.84.** Whichever direction ships, do not use one
partition for nine scenes. Declare a **cycle**, the way Vignelli declares his
book rhythm. A nine-scene default:

```
s1  full-bleed reversed field        (D4)   — the hook
s2  band                             (D1)
s3  picture column, photo right      (D2)
s4  band                             (D1)
s5  mosaic, major + minor            (D3)   — the mechanism scene
s6  picture column, photo left       (D2)
s7  band                             (D1)
s8  full-bleed reversed field        (D4)   — the money scene
s9  band + CTA block                 (D1)
```

This is one grid, one type system, one motion vocabulary, four apertures. It
directly attacks the sameness risk that `architecture_lock` created without
reopening the lock decision — the lock says *which system*, the cycle says
*which aperture within it*. And it is Gerstner's point exactly: design the
programme, not the artefact.

---

## 5. Colour and the money problem

**The finance semantic does not have to bend. It is already Vignelli-legal.**

Canon p.78: *"Most of the time we use color as a Signifier, or as an Identifier.
Generally speaking we do not use color in a pictorial manner."* Green = kept,
red = loss, amber = under examination, orange = CTA **is** colour-as-signifier.
This is the same logic as the subway line colours and the NPS band colours. FACT:
the Unigrid spec carries a **24-colour standard palette** (process CMYK; PMS
451–454 beiges; 414–417 greys; 279/293/298/304 blues; 354/368/375 greens;
109/116 yellows; 144/159 oranges; Super Warm Red) — restricted, but not
monochrome. The "Swiss = one accent on white" idea is a modern simplification.

**What has to bend is quantity and form.** Four changes:

1. **One role colour visible per scene. Ever.** Today a scene can carry green
   chips, a red total and an amber stamp — three signifiers arguing inside one
   frame. In a Swiss variant that is a semantic failure, not just a busy one.
2. **Colour appears as a filled rectangle on the grid, or as a rule. Never as
   coloured text over photography, never as a border on a rounded pill.** The
   `.chip.fund` / `.chip.warn` pattern (3px coloured border, 999px radius) is the
   single most un-Swiss construct in the current CSS. Replace with a filled
   square module carrying reversed `--bg` text.
3. **Retire the per-scene `--tint`.** A 0.10–0.13 alpha colour wash across the
   frame is *pictorial colour* — the one use Vignelli names as wrong. Its job
   (emotional register per scene) is better carried by which role colour appears
   in the one filled module.
4. **`--pop` orange stays, once per video, as the CTA block only.** It is an
   identifier, not a mood.

**JUDGEMENT on the two markets.** Both channels keep the same four tokens. The
market marker is the currency glyph and the number formatting, not a palette
change — Vignelli's *Identity and Diversity* argument (Canon p.90: "enough
diversity must be provided to avoid sameness … too much diversity creates
fragmentation") says the two channels should be one system with one variable
changed, which is what they already are.

---

## 6. Typography — and why the font does not change

**Recommendation: keep FinanceSans (Noto Sans variable). Do not swap.**

The instinct is Helvetica. Resist it, for three reasons:

1. **Vignelli's own argument.** Canon p.54: *"is not the type but what you do
   with it that counts. The accent was on structure rather than type."* His four
   faces include Bodoni and Century Expanded — a Swiss grid does not require a
   grotesque. Noto Sans is a neutral humanist sans with a real 100–900 weight
   axis; used flush left, hung from rules, at two sizes, it is a legitimate voice
   in this tradition.
2. **The ₹.** The subset carries U+20B9 and 96 other codepoints. FACT from the
   repo: Archivo Black has no ₹ and no →, and four shipped cuts silently lost
   `@font-face` and rendered in Arial Black. A font swap has broken shipped
   videos here before. Price of swapping: re-subsetting, re-verifying ₹ and every
   glyph in both markets, and re-rendering — for a change no viewer can name.
3. **Helvetica's identity is borrowed, not earned.** Using it reads as costume.
   The distinctive thing about these directions is the aperture and the rule
   system, not the letterforms.

**What does change:**

- **Two sizes per scene**, ratio 1:2.5–1:4, both drawn from the existing 16-step
  ladder (Canon p.68/p.72). The ladder stays as the *allowed values*; the
  *per-scene budget* drops to two. This is the largest conflict with the current
  design doc.
- **Weight carries hierarchy, not size.** 900 for the hero, 500 for the
  statement, 200 for indices and numerals-as-furniture. The variable axis is the
  asset — Canon p.68: *"a logical use of bold, regular and light type weights."*
- **Flush left, ragged right, always.** Canon p.66. Centring is reserved for
  "lapidary text" — a video's spoken statements are not that.
- **Everything hangs from a rule.** Canon p.70. This is the detail that will make
  it look designed rather than merely aligned.
- **Tracking:** −1px at 84px+, 0 at 40–54px, +4px uppercase on the 26–30px
  kicker/foot. No optical fiddling beyond that.
- **Glyph constraint unchanged:** →, ▶, >, ~, ×, ≈, ¢ are absent from the subset
  and must stay drawn in CSS (`.arrow`, `.arr`, `.tri`, `.gt` already exist).
  Swiss design loves an arrow; the font cannot make one. Use the CSS ones.

---

## 7. Attractive, honestly — what it buys and what it risks

### What it genuinely buys — JUDGEMENT

1. **Nobody in finance YouTube looks like this.** The category is bright, loud,
   arrow-heavy, red-circle-heavy, shocked-face-heavy. Canon p.72: *"In a world
   where everybody screams, silence is noticeable."* That is not a nice
   aphorism here — it is a positioning argument, and it is the strongest one
   available.
2. **Authority for free.** This visual language is what institutions use — transit
   systems, national parks, museums, central banks. A faceless channel making
   money claims has an authority deficit by construction (no presenter to trust).
   Borrowing the grammar of public information design partially closes it.
3. **Legibility at phone size.** Flush-left, two sizes, hard-edged tone blocks,
   heavy weights on a grid — every one of those decisions survives a 3-inch
   screen better than a centred stack over a graded photograph does.
4. **It gives the pipeline something to compute.** A grid is a set of integers. A
   partition is a choice from a set. This is a style an automated system can
   execute *correctly*, which is not true of "compose it nicely."
5. **The thumbnail problem.** FACT from the audit: all ten shipped thumbnails are
   one layout, and `fin-package`'s sameness check compares the number and the
   photo, so it passes every time. A partition system gives thumbnails a real
   variance axis (which rectangle the photo occupies), and a channel page of
   Unigrid-band thumbnails would look like a *series* rather than a template.

### Failure modes and their guardrails — JUDGEMENT

| Failure | What it looks like | Guardrail |
|---|---|---|
| **Slide deck** | Title bar + a picture + a bulleted line = corporate PowerPoint | Ban bulleted/enumerated rows in `.swiss`. No `.chip` row. Max two type sizes. Never a title bar and a heading and a subhead in one frame |
| **Sterile / cold** | Nothing to look at, no warmth, viewer bounces | Keep the grain. Require ≥2 scenes per video where the photograph is full-bleed with type reversed on it (D4 move). Photographs must be *photographs* — object-led, human hands, textures — not abstractions |
| **Pastiche** | Red diagonal bar, rotated Helvetica, a big black circle | Ban rotation entirely. Ban diagonals. No decorative geometry with no informational job. The signature is the aperture and the rules, not ornament |
| **Sameness** | A strict grid is *more* same, not less — the exact risk the lock created | The sequence cycle (§4). Partition must vary by scene *and* the cycle offset must vary by video. This is mandatory, not optional |
| **Type dissolving into the photo** | The thing the four-layer scrim exists to prevent | Type never sits on ungoverned photography. Either flat `--bg`, or a hard-edged tone block, or a region whose luminance was **measured**. Add the measurement; do not reintroduce the gradient |
| **Dead frames** | A frame with no motion for 8 seconds | Restate the §5 rule 2 as *"no frame motionless beyond ~2s"* — rules and blocks can carry it, the photo need not |
| **Losing the cut-detector protection** | Hard wipes read as hard cuts to YouTube | Measure with `ffmpeg scdet` before shipping. A 0.45s `clip-path` sweep should behave like a dissolve to the detector, but that is a hypothesis, not a finding |
| **The checker fights it** | New contrast findings on reversed type | The existing `known_benign` discipline applies. Never edit a token to satisfy a checker (doc §9) |

### Ranking — JUDGEMENT, and I'd rather be blunt

- **Direction 1 (`.swiss-band`) — ship first.** Best ratio of distinctiveness to
  build cost, and it is the one mechanism Vignelli actually wrote a production
  spec for, in a system whose problem statement was near-identical to ours.
- **Direction 4 (`.swiss-reverse`) — ship second, or first if budget is tight.**
  Cheapest possible diff (a grade, a scrim swap, an alignment change), and the
  best host for stock video.
- **Direction 3 (`.swiss-mosaic`) — highest ceiling, build it third.** It is the
  one that could actually be "a new world", but it is a partition engine, not a
  stylesheet, and it fails ugly.
- **Direction 2 (`.swiss-col`) — weakest.** It is `ledger-rail` with better
  typography. Worth folding into the sequence cycle as one aperture among four;
  not worth shipping as *the* new style.

---

## 8. Contradictions with `vault/knowledge/design-finance-blockframe.md`

Listed so a build agent does not have to discover them by breaking things. None
of these say the existing doc is *wrong* — it is right about blockframe-9. They
are places where a Swiss variant must diverge, and the doc currently reads as
channel-wide law.

1. **§1 "The grade is load-bearing"** — `grayscale(0.32) brightness(0.62)
   contrast(1.05)` is declared "the single reason nine unrelated stock photos
   read as one film." In a Swiss variant that job is done by a **fixed recurring
   aperture**, which is more robust than a filter. The grade should go to
   ~`grayscale(0.85)` so the photograph reads as tonal mass (Hofmann), not as a
   window. The doc's claim is one solution to the problem, stated as the only one.
2. **§1 the four-layer scrim** — must be **deleted** in `.swiss`, not tuned. Soft
   radial gradients are the anti-Swiss device. Replace with a hard-edged tone
   block on a column line. (`.rail` already sets the precedent for switching it
   off, so this is not unprecedented.)
3. **§2 per-scene `--tint` at 0.10–0.13** — this is *pictorial colour*, the one
   use of colour Vignelli names as wrong (Canon p.78). Retire in `.swiss`.
4. **§3 the type ladder is 16 sizes** — Canon p.68/p.72: two sizes max on a page.
   The ladder survives as the allowed set; the **per-scene budget drops to two**.
   This is the largest conflict and the one most likely to be violated silently.
5. **§3 `text-shadow` on every text class** — off in `.swiss`. Contrast comes
   from geometry.
6. **§4 components are rounded and/or rotated** — `.chip` (999px radius),
   `.stamp` (`rotate(-4deg)`), `.claim`/`.billrow` (14px), `.colcard` (20px),
   `.cta` (14px). **All radii → 0, rotation → 0** in `.swiss`. `.stamp` in
   particular becomes a filled grid module, which is a better component anyway.
7. **§5 rule 1 (Ken Burns `1.0 ↔ 1.16`)** — must halve inside a band or block,
   and switch off entirely when the aperture holds video.
8. **§5 rule 2 ("no scene may hold a static frame beyond ~2s")** — written for an
   architecture where the photo *is* the frame. Restate as *"no frame may be
   motionless beyond ~2s"* so rules and blocks can carry the motion.
9. **§5 rule 0 (`dissolve` 0.45s as the default boundary)** — replaced by a hard
   directional wipe of the same duration. The cut-detector reasoning still holds
   in principle but **must be re-measured with `ffmpeg scdet`**, not assumed.
10. **`.scene { text-align: center }` / `.stack { align-items: center }`** — every
    `.swiss` scene is flush left. Centring is for "lapidary text" (Canon p.66).
11. **`motion.js` easing** — `back.out(1.7)` in `pop`/`popEach`, plus `breathe`
    and `drift`, are all expressive/decorative. `.swiss` uses `power2/3/4.out`
    and `expo.out` only, and does not call `breathe` or `drift`.
12. **`tools/format.json` `_stock_video_note`** — stock video is explicitly
    unproven against the deterministic renderer. Every direction above assumes a
    **still** today; the aperture spec is what makes video a cheap change later,
    not a claim that it works now.

---

## 9. Open questions this research did not settle

- **Does a 0.45s hard `clip-path` wipe satisfy `ffmpeg scdet` the way a
  cross-dissolve does?** Testable in an afternoon on an existing master. Until
  tested, the boundary change is a hypothesis.
- **Luminance measurement for reversed type.** D1's band-reversed number and D4's
  tone block both want a measured luminance for a region of the photograph.
  Nothing in the pipeline measures this today. It is a small tool (PIL crop +
  mean luminance at asset-fetch time), and without it "reversed type on a
  photograph" is a coin flip.
- **Whether the two-size-per-scene rule survives contact with real scripts.** Some
  scenes legitimately carry a kicker + statement + foot + number. That is four
  sizes. The proposed answer is weight-differentiation instead of size, but it
  needs one real storyboard run to confirm.
- **Stock video at all.** Unresolved per `format.json`. Directions are written so
  the answer changes one property.

---

## References

Primary, read directly:

- **Massimo Vignelli, *The Vignelli Canon*** — https://www.rit.edu/vignellicenter/sites/rit.edu.vignellicenter/files/documents/The%20Vignelli%20Canon.pdf
  (pp. 24, 40–42, 48, 52, 54–56, 66, 68, 70, 72, 78, 80, 84, 90, 92 cited above)
- **Unigrid Design Specifications, National Park Service Informational Folder
  Program** (Vignelli Associates) — https://npshistory.com/brochures/unigrid.pdf
  (the "Pictorial Features", "Bars and Dividers", "Titles", "Measurements",
  "Cover Illustrations and Color", "Preferred Colors" sections)

Secondary:

- New York City Transit Authority Graphics Standards Manual (Unimark, 1970) —
  https://archive.org/details/nycta-gs-manual
- Unigrids — https://en.wikipedia.org/wiki/Unigrids
- Josef Müller-Brockmann, *Grid Systems in Graphic Design* —
  https://monoskop.org/images/a/a4/Mueller-Brockmann_Josef_Grid_Systems_in_Graphic_Design_Raster_Systeme_fuer_die_Visuele_Gestaltung_English_German_no_OCR.pdf
- *Schützt das Kind!* (1953), Cooper Hewitt —
  https://collection.cooperhewitt.org/objects/18673645/
- Armin Hofmann 1920–2020, Poster House (the *Giselle* analysis) —
  https://posterhouse.org/blog/armin-hofmann-1920-2020/
- Herbert Matter, MoMA — https://www.moma.org/calendar/exhibitions/340 ; Cooper
  Hewitt *Engelberg, Trübsee* — https://collection.cooperhewitt.org/objects/18705675/
- Müller-Brockmann Musica Viva posters, SOCKS —
  https://socks-studio.com/2016/11/30/joseph-muller-brockmann-musica-viva-posters-for-the-zurich-tonhalle/
- Emil Ruder, *Typography: A Manual of Design*, Typotheque —
  https://www.typotheque.com/books/typography-a-manual-of-design
- Karl Gerstner, *Designing Programmes* (1964) —
  https://openlab.citytech.cuny.edu/langecomd3504sp2020/files/2018/10/Gerstner_DesigningProgrammes-1.pdf
- Swiss Style in Motion, GT3 —
  https://gt3themes.com/swiss-style-in-motion-animation-in-international-typographic-style/
  (the Jon Yablonski CSS poster re-creations; thin evidence, flagged as such in §3)
- International Typographic Style — https://en.wikipedia.org/wiki/International_Typographic_Style

Repo files read (read-only): `vault/knowledge/design-finance-blockframe.md`,
`tools/scaffold/assets/css/blockframe.css`, `tools/scaffold/assets/js/motion.js`,
`tools/format.json`, `vault/knowledge/finance-audit-2026-07-29/`.
