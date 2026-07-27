---
summary: Nano Banana (Gemini 2.5 Flash Image, Google AI Studio, ~free 200/day) scene-image prompt log for Pompeii Ka Akhri Din. One prompt per script scene; realistic COLORED cinematic reconstruction (the recon layer of the 3-layer visual system — NOT the B&W travel grade). Style standard gets LOCKED after scene 1 is approved, then reused for every scene.
updated: 2026-07-10
source: script [[script-v1-urdu]] · look = "AI reconstruction" cues in the script · design context [[../../knowledge/design-cinematic-history]] (recon layer only, in colour)
---

# Pompeii — Nano Banana scene-image prompts

**Tool:** Google AI Studio → Nano Banana (Gemini 2.5 Flash Image). Set aspect ratio **16:9**
(1920×1080). ~200 free images/day. Workflow: generate scene → creator reviews → tweak →
approve → lock, then next scene. Approving scene 1 sets the STANDARD below for all others.

## PROMPT RULES (standing — creator 2026-07-10)

1. **Fact-check EVERY scene from the internet before writing its prompt** — architecture,
   clothing, objects, the eruption, the mountain, the sea, people. Log the sources in the scene.
2. **One-shot budget:** creator has ~200 gens/day and wants **1 image per scene** (→ 200
   scenes/day, not 100). So each prompt must be **so detailed and specific that a single
   generation lands** — no re-rolls. Over-specify: subject, action, wardrobe, materials,
   architecture, props, background, light, lens, grade, negatives.
3. **Photoreal always** — every scene (blast, mountain, sea, children, casts) must look like a
   real documentary photograph, never "AI/CGI". The whole video's engagement depends on it.
4. **Force STILLS, not video** (learned 2026-07-12): Flow turned the "SHOT 13A/14A" prompts —
   both led with motion verbs (*street waking*, *baker sliding*) — into **videos**. So: don't lead
   a prompt with "SHOT"; avoid strong motion verbs in the main phrase; and add "still photograph,
   not a video" to the section setup. Keep a parseable id for the downloader in another form
   (e.g. "Scene 14B — …" — update the extension's id regex to match it).
5. **NON-AGENT mode** (Section 4 onward, 2026-07-12): prompts are entered one at a time with NO
   chat memory and NO reference to prior images — so the per-section SETUP block / "same as before"
   protocol below does NOT apply. Every prompt must be **fully self-contained**: bake the entire
   style DNA into each one (photoreal 35mm film still · 16:9 · natural dynamic range/no HDR · muted
   realistic colour · fine film grain · real documentary photograph, not painting/3D/video ·
   historically accurate 79 AD, no modern objects/text) and **re-describe any recurring character in
   full** each time. Carry the id as "Scene 24A". Full Section-4 + gap prompts live in [[storyboard]].

## STYLE STANDARD (candidate — confirm after scene 1 v2)

Fixed suffix that goes on EVERY scene so all images feel like one film:

> _"Shot on 35mm film, 50mm lens, shallow depth of field, natural dynamic range (no HDR),
> rich but realistic muted colour, fine film grain, authentic skin texture and dust.
> Indistinguishable from a real documentary photograph — not a painting, not a 3D render.
> No modern objects, no legible modern text."_

- Look: photoreal cinematic film still, **full colour** (never B&W), 79 AD Pompeii, historically accurate.
- **"Real photo, not AI" fix** (v1 renders looked too clean/HDR): 35mm film + natural dynamic
  range + film grain + dust/sweat + "not a 3D render" kills the glossy-AI look.
- Vesuvius rule: **NOT in frame until segment 05** (script reveals the mountain there — continuity).

## Nano Banana chat-agent consistency protocol (creator-found 2026-07-10)

Nano Banana's chat module keeps style + characters consistent **within one conversation**. So:

1. **One chat per storyboard SECTION.** Start it by pasting that section's **SETUP block** (style DNA
   + world rules + time-of-day + which locked characters appear). End with *"Reply 'ready' and wait."*
2. Then paste each shot prompt one at a time — kept **focused** (the agent already holds the style).
3. **Recurring character?** Add *"same [name] as before — identical face, hair, build, clothing."*
4. **Match cut (recon→real):** generate the recon, then *"now the SAME framing, but as the real
   weathered excavated ruin/artifact today — desaturated, cool, forensic."*
5. Face/detail drifted? Regenerate referencing the earlier good image in the chat.

## Character lock sheet (the recurring cast — keep IDENTICAL across all their scenes)

| ID | Appears | Locked description |
|---|---|---|
| **BREAD-MAN** | 01, 63 | weathered working man ~40, dark curly hair, short beard, undyed knee-length wool tunic, rope belt, worn leather sandals |
| **BAKER** | 01, 14 | stocky balding man ~50, short grey tunic, forearms & apron white with flour |
| **STEW-WOMAN** | 02, 63 | plebeian woman ~35, simple belted tunic + headscarf, expressive hands |
| **THE HORSE** | 03, 52, 64 | large powerful well-bred bay horse, glossy chestnut coat, fine leather halter — a rich man's prized animal (Civita Giuliana payoff) |
| **THE BOY** | 04, 63 | boy ~10, plain tunic, holds a wax tablet + bronze stylus |
| **GLADIATOR** | 04 | muscular young man, leather subligaculum, oiled skin |
| **YOUNG PLINY** | 25 | slim 17-yr-old in a good tunic, on a terrace across the bay (Misenum) |
| **PLINY THE ELDER (admiral)** | 33–34 | dignified older Roman commander, ~55, cloak — leads the rescue fleet |
| **REGIO-IX WOMAN + BOY** | 54–55 | woman on a bed w/ gold/pearl jewellery + a key; a teen boy near the blocked doorway |

## Pompeii architecture — verified cheat-sheet (for accurate prompts)

Sources: [World History Encyclopedia — Bakery of Popidius Priscus](https://www.worldhistory.org/image/11294/the-bakery-of-popidius-priscus-in-pompeii/) ·
[History & Archaeology Online — Baking in Pompeii](https://historyandarchaeologyonline.com/baking-and-bakeries-in-pompeii/) ·
[Pompeii Archaeological Park — Urban Layout](https://pompeiiarchaeologicalpark.com/urban-layout-of-pompeii/) ·
[seepompeii — the streets of Pompeii](https://seepompeii.com/en/the-characteristic-streets-of-ancient-pompeii/). Verified 2026-07-10.

- **Bakery (pistrinum) = a workshop, oven is INDOORS.** Rooms: milling, dough-prep, baking. NOT an open-street oven.
- **Mills (mola):** tall **hourglass / double-cone** stones of grey porous lava, in a row indoors; turned by donkey or slave.
- **Oven (furnus):** big **domed brick** oven with an arched mouth + a flue, fuelled by **vine wood**; bread cooled on **wall shelves** (peg holes in the wall).
- **Selling bread:** most bakeries had **no shop** → sold wholesale to shops / street-vendors (*libani*). SOME had a **masonry sales counter built into the street-front** (*taberna*). Modestus's bakery = ~80 carbonized loaves found in the oven (the script's "81 rotiyan").
- **Bread:** *panis quadratus* — round loaf scored into **8 wedges**, a baker's **stamp** in the centre, sometimes tied with cord.
- **VESUVIUS shape (79 AD) — SINGLE tall vineyard/forest-covered cone, ONE summit, craggy top, taller than today. NOT the modern double-hump** (that caldera formed IN this eruption). Vineyards on the fertile lower slopes. Ref: House of the Centenary "Bacchus & Vesuvius" fresco. Use this in every mountain shot. ([Wikipedia — Mount Vesuvius](https://en.wikipedia.org/wiki/Mount_Vesuvius) · [House of the Centenary](https://en.wikipedia.org/wiki/House_of_the_Centenary), verified 2026-07-10.)
- **City look:** most buildings faced with **brilliant white ground-marble stucco** — a gleaming city. **Port** at the mouth of the **Sarno river** (exact site debated), Roman **merchant ships** (single square sail), quays stacked with amphorae (wine, oil, garum).
- **Streets:** paved with **large polygonal grey basalt blocks**, deep **cart ruts**; **raised sidewalks** with a ~30 cm curb; **stepping-stones** to cross; small white stones set in the paving to catch moonlight.
- **Buildings:** 1–2 storeys, street frontage = rows of **tabernae** (wide doorways, wooden **fold-away shutters**, masonry counters); **terracotta tile roofs** (tegulae/imbrices); projecting **wooden balconies**; corner **street shrines** & **public fountains**.
- **WALLS — smooth plaster, NOT rough stone** (v2 renders got this wrong). Masonry was coated
  in **smooth lime plaster (stucco)**. *Exterior street façades:* **whitewashed pale cream/white**
  with a **Pompeian-red painted dado** (lower band); over it, big **hand-painted election notices**
  — candidate's name in **large red brush capitals**, rest in **black** — + scratched graffiti;
  aged/softly cracked but **smooth**. *Interior walls* (villas, some shop interiors): the **Four
  Styles** frescoes — polished plaster, fields of **Pompeian red (cinnabar), black, yellow ochre,
  white**, framed mythological panels/architecture (Fourth Style current in 79 AD). **Ornate
  frescoes = interiors only; street façades = plain painted plaster + notices.**

## Prompt log

### Scene 01 — bakery, buying bread (HOOK) · `6:00 AM` recon
Script: "Ak admi bread khareed raha ha. Garam, taaza bread." Cue: warm morning light, hand taking bread.

**v1** (4 renders, good but oven+mill wrongly out on the open street; too clean/HDR) → **v2 below** fixes architecture + realism.

**v2 — refined:**

> Photorealistic cinematic film still, wide 16:9, a narrow street in ancient Pompeii at dawn,
> 79 AD. Foreground: a working-class Roman man in a plain undyed knee-length wool tunic and
> leather sandals stands on a raised stone sidewalk, both hands taking a round golden loaf
> scored into eight wedges (*panis quadratus*, a baker's stamp pressed in the centre). He
> takes it across a low masonry sales counter built into the street-front of a bakery. Behind
> the counter a flour-dusted baker in a short tunic hands it over; through the wide shop
> doorway behind him the bakery interior is visible in shadow — a large **domed brick oven
> glowing deep inside**, a row of tall **hourglass-shaped grey volcanic-lava millstones**,
> wooden bread peels, and loaves cooling on wall shelves. The folded wooden shutters of the
> shop stand open against the wall. The façade is plastered and painted in faded Pompeian red
> and ochre, a weathered red-painted election notice on it, terracotta roof tiles above and a
> wooden upper balcony jutting over the street. The street is paved with large polygonal grey
> basalt blocks worn by cart ruts, a raised curb dividing sidewalk from road; a few figures
> walk in the misty distance. Warm low golden dawn light rakes down the street with soft haze
> and floating dust. Shot on 35mm film, 50mm lens, shallow depth of field, natural dynamic
> range (no HDR), rich but realistic muted colour, fine film grain, authentic skin texture and
> dust. Indistinguishable from a real documentary photograph — not a painting, not a 3D render.
> No modern objects, no legible modern text, no volcano in view.

**v2 verdict** (creator 2026-07-10): **characters + composition approved** (esp. render #1) —
but **walls wrong**: rendered as rough bare/crumbling stone. Real Pompeii walls = smooth painted
plaster. → **v3 fixes the walls, keeps everything else.** Wall research: [The Archaeologist — Four
Pompeian Styles](https://www.thearchaeologist.org/blog/roman-wall-painting-the-four-styles-of-pompeian-decoration) ·
[Pompeian Styles (Wikipedia)](https://en.wikipedia.org/wiki/Pompeian_Styles) ·
[pompeiiinpictures I.11.2 — a real shopfront](https://pompeiiinpictures.com/pompeiiinpictures/R1/1%2011%2002.htm).

**v3 — LOCK candidate (one-shot):**

> Photorealistic cinematic film still, wide 16:9, a narrow street in ancient Pompeii at dawn,
> 79 AD. Foreground: a weathered working-class Roman man, dark curly hair and short beard, in a
> plain undyed knee-length wool tunic belted with rope and worn leather sandals, both hands
> taking a round golden loaf scored into eight wedges (*panis quadratus*, a baker's stamp pressed
> in the centre). He takes it across a low masonry sales counter built into the street-front of a
> bakery. Behind the counter a stocky flour-dusted baker in a short grey tunic, forearms white
> with flour, hands the loaf over; through the wide shop doorway behind him the bakery interior is
> visible in warm shadow — a large **domed brick oven glowing deep inside**, a row of tall
> **hourglass-shaped grey volcanic-lava millstones**, long wooden bread peels, and round loaves
> cooling on wooden wall shelves. Folded wooden shutters stand open against the wall. The building
> façade is **smooth lime-plastered stucco, not bare stone — whitewashed pale cream with a broad
> Pompeian-red painted dado along its base**; across it, **large hand-painted Latin election
> notices in faded red and black brush-capitals** and a few lightly scratched graffiti; the
> plaster aged and softly cracked but smooth. Terracotta tile roof above, a wooden upper balcony
> jutting over the street. The street is paved with large polygonal grey basalt blocks worn by
> cart ruts, a raised stone curb dividing sidewalk from road; a mule cart and a few tunic-clad
> figures move in the misty distance. Warm low golden dawn light rakes down the street with soft
> haze and floating dust. Shot on 35mm film, 50mm lens, shallow depth of field, natural dynamic
> range (no HDR), rich but realistic muted colour, fine film grain, authentic weathered skin
> texture and dust. Indistinguishable from a real documentary photograph — not a painting, not a
> 3D render. No modern objects, no legible modern text, no volcano in view.

Fix vs v2: **walls** = smooth whitewashed plaster + red dado + red/black painted election notices
(was rough bare stone) · kept the approved characters (described so they carry over) · kept
oven-inside, hourglass mills, basalt street, sidewalk/curb, film-stock realism.

Status: **awaiting v3 generation.**
