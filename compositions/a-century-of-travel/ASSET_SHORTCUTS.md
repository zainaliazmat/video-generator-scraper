# 🔎 ASSET SHORTCUTS — click-through sourcing for "A Century of Travel"

The only thing Claude Code can't do for you is find the 13 photos. This turns that into
clicking links. Each row gives a **primary** (public-domain) and a **backup** source, pre-queried.

**How to grab a file (30 sec each):**

- **Wikimedia Commons** → open image → _Download_ (right side) → pick the **largest** size.
- **Library of Congress** → open the item → _Download_ dropdown → choose the **largest JPEG/TIFF**.
- Save it into `assets/images/` and **rename to the exact filename** in column 1. That's it.
- ≥1920 px wide is ideal. B&W or color both fine — DESIGN.md grades everything to match.

> You do **not** need all 13 to start. Get 6–8, run Prompt 1, and the placeholders cover the rest.
> Drop the rest in as you find them and tell Claude Code "new images are in assets/images — wire them in."

---

## Photos

| Save as                    | Primary (public domain)                                                                                                                                   | Backup                                                                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `s00_title.jpg`            | [LOC — railway terminal](https://www.loc.gov/photos/?q=railroad%20station%20terminal)                                                                     | [Commons — ocean liner at dock](https://commons.wikimedia.org/wiki/Special:MediaSearch?search=ocean%20liner%20dock%20historic&type=image)                   |
| `s01_1841_cook.jpg`        | [LOC — excursion train](https://www.loc.gov/photos/?q=excursion%20train)                                                                                  | [Commons — Victorian railway 1850s](https://commons.wikimedia.org/wiki/Special:MediaSearch?search=Victorian%20railway%201850s%20train%20station&type=image) |
| `s02_1869_suez.jpg`        | [Commons — Suez Canal 1869 opening](https://commons.wikimedia.org/wiki/Special:MediaSearch?search=Suez%20Canal%201869%20opening&type=image)               | [LOC — Suez Canal](https://www.loc.gov/photos/?q=Suez%20Canal)                                                                                              |
| `s03_1883_orient.jpg`      | [Commons — Orient Express dining car](https://commons.wikimedia.org/wiki/Special:MediaSearch?search=Orient%20Express%20dining%20car%20vintage&type=image) | [LOC — railroad dining car](https://www.loc.gov/photos/?q=railroad%20dining%20car)                                                                          |
| `s04_1897_liner.jpg`       | [LOC — steamship ~1900](https://www.loc.gov/photos/?q=ocean%20liner%20steamship%201900)                                                                   | [Commons — liner departure, funnels](https://commons.wikimedia.org/wiki/Special:MediaSearch?search=ocean%20liner%20departure%201900%20funnels&type=image)   |
| `s05_1907_mauretania.jpg`  | [Commons — RMS Mauretania 1907](https://commons.wikimedia.org/wiki/Special:MediaSearch?search=RMS%20Mauretania%201907&type=image)                         | [LOC — Mauretania](https://www.loc.gov/photos/?q=Mauretania%20ship)                                                                                         |
| `s06_1912_grand_liner.jpg` | [Commons — ocean liner at dock 1910s](https://commons.wikimedia.org/wiki/Special:MediaSearch?search=ocean%20liner%20dock%201910s&type=image)              | [LOC — liner at pier](https://www.loc.gov/photos/?q=ocean%20liner%20pier) — _avoid disaster imagery_                                                        |
| `s07_1927_aviation.jpg`    | [LOC — aviator / airplane 1927](https://www.loc.gov/photos/?q=aviator%201927%20airplane)                                                                  | [Commons — Spirit of St. Louis 1927](https://commons.wikimedia.org/wiki/Special:MediaSearch?search=Spirit%20of%20St%20Louis%201927&type=image)              |
| `s08_1936_queenmary.jpg`   | [Commons — RMS Queen Mary 1936](https://commons.wikimedia.org/wiki/Special:MediaSearch?search=RMS%20Queen%20Mary%201936&type=image)                       | [LOC — liner grand staircase](https://www.loc.gov/photos/?q=ocean%20liner%20grand%20staircase)                                                              |
| `s09_1939_clipper.jpg`     | [Commons — Pan Am Clipper flying boat](https://commons.wikimedia.org/wiki/Special:MediaSearch?search=Pan%20American%20Clipper%20flying%20boat&type=image) | [LOC — Pan American clipper](https://www.loc.gov/photos/?q=Pan%20American%20clipper)                                                                        |
| `s10_1952_jet.jpg`         | [Commons — de Havilland Comet](https://commons.wikimedia.org/wiki/Special:MediaSearch?search=de%20Havilland%20Comet%20airliner&type=image)                | [LOC — jet airliner 1950s](https://www.loc.gov/photos/?q=jet%20airliner%201950s)                                                                            |
| `s11_1970_747.jpg`         | [Commons — Boeing 747 1970s](https://commons.wikimedia.org/wiki/Special:MediaSearch?search=Boeing%20747%201970s&type=image)                               | [LOC — airport terminal 1970s](https://www.loc.gov/photos/?q=airport%20terminal%201970s)                                                                    |
| `s12_today.jpg`            | [Unsplash — airport departures](https://unsplash.com/s/photos/airport-departures)                                                                         | [Pexels — airport terminal](https://www.pexels.com/search/airport%20terminal/)                                                                              |

---

## Audio — `assets/audio/score.mp3`

Mood: _wistful nostalgic orchestral, soft piano + warm strings, gentle swell, vintage documentary._ ~4:05.

- [Pixabay — "nostalgic cinematic"](https://pixabay.com/music/search/nostalgic%20cinematic/)
- [Pixabay — "wistful orchestral"](https://pixabay.com/music/search/wistful%20orchestral/)
- [Uppbeat — cinematic](https://uppbeat.io/browse/music/cinematic) · [Free Music Archive — search](https://freemusicarchive.org/search?quicksearch=nostalgic%20orchestral)

> Check the length — you want one continuous ~4-min track, not a 90-sec loop. If you'd rather not
> hunt, Prompt 2A can have HyperFrames generate a fitting score locally.

---

## Texture — `assets/textures/paper.png`

Faint aged-paper / old-newspaper overlay (the recurring vintage texture in the reference).

- [Commons — aged paper texture](https://commons.wikimedia.org/wiki/Special:MediaSearch?search=aged%20paper%20texture&type=image)
- [Unsplash — old paper texture](https://unsplash.com/s/photos/old-paper-texture)
- [Pixabay — old newspaper](https://pixabay.com/images/search/old%20newspaper/)

> Optional. Skip it if you're tight on time — Claude Code generates deterministic film grain with an
> SVG filter (no asset needed), and the paper texture is a nice-to-have on top of that.

---

## Licensing note (paid deliverable)

Keep a one-line **source + license** per image (Public Domain / CC0 is safest). On Commons the license is
on each file's page; LOC items show rights under "Rights & Access." Skip anything watermarked or
"editorial-only." Jot them in a `CREDITS.txt` as you go — future-you will thank you.
