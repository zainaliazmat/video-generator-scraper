# PRODUCTION RUNBOOK — *The Iron Horse of the Indus*

> Human-facing runbook only. HyperFrames never reads this file. It synthesizes the working docs (`docs/research.md`, `docs/script.md`, `docs/storyboard.md`, `docs/narration.md`, `ASSET_SHORTCUTS.md`, `DESIGN.md`, `CLAUDE.md`) into one place for the person assembling and rendering the film.

---

## 1. Overview

**The Iron Horse of the Indus — the North Western Railway and the making of a nation, 1860s→1970s.** A stately, elegiac B&W parallax photo-documentary tracing the railways of the Indus valley / colonial Punjab & Sindh: from the 1850s river steamers and the Scinde Railway charter, through the great Indus bridges and frontier passes, to Partition and the consolidation of Pakistan Railways in 1974. Reverent register — engineering triumph braided with the human cost of Partition, never spectacle. It should feel like a lost documentary title sequence.

**Format**
- **1920×1080 (16:9)**, `data-fps="30"`, **H.264 MP4**.
- **26 scenes** (s00 title + s01–s24 beats + s25 outro).
- **Total length ~536.8s (~8:57)** — last scene s25 starts at 510.8s, runs 26.0s, ends at 536.8s. Inside the 535–545s window.
- Optional later: a **1080×1350 (4:5) social cut**.

**Locked style (one paragraph).** Vintage blue-sepia B&W grade applied identically to every photo (`grayscale(1) contrast(1.08) brightness(0.92) sepia(0.12)` + a `rgba(28,40,56,0.18)` multiply wash). Palette: `--paper #0d0f12`, `--ink #f4f1ea` (warm off-white, never pure white), `--accent-warm #c9a86a` (sparing — numeral rule, kicker, dividers). Type: **Archivo Black** numeral/year (140–160px) and kicker (~22px uppercase), **Playfair Display** title (56–66px on a dark band) and italic caption (28–32px). Layout is left-aligned, vertically centered text with ≥160px title-safe padding, ordered kicker → numeral(+thin warm rule) → title → caption; title card (s00) and outro (s25) are centered with no band. Motion is Ken Burns on every photo (scale 1.0 → 1.12–1.16, `sine.inOut`, full scene, **direction alternates each scene**) with parallax text drifting ~25–35% of the photo's travel; transitions are slow ~1.0s cross-dissolves with a soft white bloom at three act breaks (s06, s14, s21). Persistent overlays: deterministic SVG `feTurbulence` film grain (fixed seed), CSS vignette, edge-anchored aged-paper texture.

**File structure**
```
iron-horse-of-the-indus/
  index.html                  # the composition (single HTML file → MP4)
  CLAUDE.md                   # framework/project contract (HyperFrames reads)
  DESIGN.md                   # brand truth: palette, grade, type, motion (HyperFrames reads)
  ASSET_SHORTCUTS.md          # sourcing links (human downloads images)
  PRODUCTION_RUNBOOK.md       # this file (human only)
  CREDITS.txt                 # source + license per asset (fill as you download)
  docs/
    research.md               # verified chronological spine (24 beats)
    script.md                 # timing ledger + 26-row scene table
    storyboard.md             # per-scene shot content + motion
    narration.md              # TTS-ready VO blocks (one per scene)
  assets/
    images/                   # sNN_keyword.jpg (s00 … s25)
    audio/                    # score.mp3 + vo_sNN.wav
    textures/                 # paper.png
```

---

## 2. Verified timeline

26 scenes. Title card s00 (0.0s, 15.0s). Body scenes s01–s24 are each **21.7s**, starting at `14.0 + (k−1)·20.7` so each begins **1.0s before** the previous ends → a clean **1.0s cross-dissolve overlap** throughout, no accumulated drift. Outro s25 runs **26.0s** (a touch longer for the quiet close). Sum: **536.8s**.

**Act-break blooms (soft white bloom on the IN of these three only):**
- **s06** — Act I → II (1878, bridge-building era begins)
- **s14** — Act II → III (1904, the system at its height)
- **s21** — Act III → IV (1947, Partition)

Every other scene IN = plain 1.0s cross-dissolve.

| # | scene | data-start | data-duration | ends | overlap w/ next |
|---|-------|-----------:|--------------:|-----:|----------------:|
| s00 | TITLE | 0.0 | 15.0 | 15.0 | 1.0 |
| s01 | beat 1 | 14.0 | 21.7 | 35.7 | 1.0 |
| s02 | beat 2 | 34.7 | 21.7 | 56.4 | 1.0 |
| s03 | beat 3 | 55.4 | 21.7 | 77.1 | 1.0 |
| s04 | beat 4 | 76.1 | 21.7 | 97.8 | 1.0 |
| s05 | beat 5 | 96.8 | 21.7 | 118.5 | 1.0 |
| **s06** | beat 6 ★bloom | 117.5 | 21.7 | 139.2 | 1.0 |
| s07 | beat 7 | 138.2 | 21.7 | 159.9 | 1.0 |
| s08 | beat 8 | 158.9 | 21.7 | 180.6 | 1.0 |
| s09 | beat 9 | 179.6 | 21.7 | 201.3 | 1.0 |
| s10 | beat 10 | 200.3 | 21.7 | 222.0 | 1.0 |
| s11 | beat 11 | 221.0 | 21.7 | 242.7 | 1.0 |
| s12 | beat 12 | 241.7 | 21.7 | 263.4 | 1.0 |
| s13 | beat 13 | 262.4 | 21.7 | 284.1 | 1.0 |
| **s14** | beat 14 ★bloom | 283.1 | 21.7 | 304.8 | 1.0 |
| s15 | beat 15 | 303.8 | 21.7 | 325.5 | 1.0 |
| s16 | beat 16 | 324.5 | 21.7 | 346.2 | 1.0 |
| s17 | beat 17 | 345.2 | 21.7 | 366.9 | 1.0 |
| s18 | beat 18 | 365.9 | 21.7 | 387.6 | 1.0 |
| s19 | beat 19 | 386.6 | 21.7 | 408.3 | 1.0 |
| s20 | beat 20 | 407.3 | 21.7 | 429.0 | 1.0 |
| **s21** | beat 21 ★bloom | 428.0 | 21.7 | 449.7 | 1.0 |
| s22 | beat 22 | 448.7 | 21.7 | 470.4 | 1.0 |
| s23 | beat 23 | 469.4 | 21.7 | 491.1 | 1.0 |
| s24 | beat 24 | 490.1 | 21.7 | 511.8 | 1.0 |
| s25 | OUTRO | 510.8 | 26.0 | 536.8 | — (final) |

Sum check: s25.end = **536.8s** ∈ [535, 545]. Every overlap = 1.0s.

---

## 3. Script table

| # | time | numeral | title | caption (italic) | VO |
|---|------|---------|-------|------------------|----|
| **s00** | 0.0 / 15.0 | *(none)* | The Iron Horse of the Indus | *The North Western Railway and the making of a nation, eighteen sixties to nineteen seventies.* | Before the rails, there was only the river. This is the story of how iron came to the valley of the Indus, and of the nation it helped to carry into being. |
| **s01** | 14.0 / 21.7 | 1850s | The River Highway | *Before the rails, the Indus carried everything northward from Karachi.* | Long before the first track was laid, the Indus itself was the highway of the valley. Country boats, and soon the steamers of the Indus Flotilla, carried freight and people up from Karachi toward Multan. The river was slow, and seasonal, and it was all there was. |
| **s02** | 34.7 / 21.7 | 1855 *(doc/map)* | A Line on Paper | *The Scinde Railway is chartered — the legal birth of the railways.* | In March of eighteen fifty-five, the Scinde Railway Company was founded by deed, and then by Act of Parliament. No track yet existed, and no engine had run. But on paper, the railways of this country had been born. |
| **s03** | 55.4 / 21.7 | 1861 | Karachi to Kotri | *The first track opens — one hundred and eight miles of new iron.* | On the thirteenth of May, eighteen sixty-one, the first public line opened between Karachi and Kotri. One hundred and eight miles of new iron tied the port to the lower river. For the first time, a train ran on the soil of what would one day be Pakistan. |
| **s04** | 76.1 / 21.7 | 1860 | The Fortress Station | *Lahore reaches Amritsar; a station built like a stronghold.* | Far to the north, the first train ran from Lahore to Amritsar in eighteen sixty. Lahore Junction was raised in those years as a fortress in disguise — turrets, loopholes, and walls thick enough to withstand a siege. The memory of eighteen fifty-seven was still very close. |
| **s05** | 96.8 / 21.7 | 1870 *(report/map)* | Four Become One | *The Scinde, Punjab and Delhi Railway — Karachi to Delhi under one hand.* | In eighteen seventy, four enterprises were joined into one: the Scinde Railway, the Punjab Railway, the Indus Steam Flotilla, and the Delhi Railway. Together they formed the Scinde, Punjab and Delhi Railway. Now a single operator reached from Karachi all the way to Delhi. |
| **s06** | 117.5 / 21.7 | 1878 | The Empress Bridge | *Iron vaults the Sutlej in the country of five rivers.* | On the seventh of June, eighteen seventy-eight, the Empress Bridge was opened across the Sutlej, between Bahawalpur and Adam Wahan. It was one of the first great crossings in the land of the five rivers. Each river the engineers reached was a wall, and each bridge a kind of victory. |
| **s07** | 138.2 / 21.7 | 1883 | Iron Over the Indus | *At Attock, rail finally crosses the great river of the north.* | At Attock, the Indus runs deep and fast through a narrow gorge. On the twenty-fourth of May, eighteen eighty-three, the railway at last vaulted that river on the road north to Peshawar. The great river of the north had been crossed. |
| **s08** | 158.9 / 21.7 | 1886 *(map/record)* | The Line Takes Its Name | *Many railways are forged into the North Western State Railway.* | In January of eighteen eighty-six, the older lines were gathered together — the Indus Valley, the Punjab Northern, and the frontier sections toward Kandahar. From them was forged the North Western State Railway. It is the system around which this whole story turns. |
| **s09** | 179.6 / 21.7 | 1886 | Through the Bolan | *Strategic track climbs the pass toward the Afghan frontier.* | That same year, eighteen eighty-six, the first rails reached Quetta through the Bolan Pass. This was track laid with one eye on the Afghan frontier — a railway as much for armies as for trade. The mountains here gave nothing away easily. |
| **s10** | 200.3 / 21.7 | 1887 | The Chappar Rift | *The Louise Margaret Bridge hangs high above a desert gorge.* | A second road to Quetta climbed through Harnai and the Chappar Rift, opened in eighteen eighty-seven. The Louise Margaret Bridge spanned a gorge more than two hundred feet above the bed. It was among the boldest and most beautiful engineering on the whole line. |
| **s11** | 221.0 / 21.7 | 1891 | The Mountain Pierced | *The first engine breaks through the long Khojak Tunnel.* | Beneath the Khwaja Amran range, men dug for three years toward each other in the dark. On the fifth of September, eighteen ninety-one, the first engine passed through the Khojak Tunnel. For more than a century it would remain the longest tunnel in the region. |
| **s12** | 241.7 / 21.7 | 1889 | Lansdowne at Sukkur | *On completion, the longest rigid span in the world.* | At Sukkur, the Lansdowne Bridge was completed in eighteen eighty-nine, joining its banks across the Indus. On the day it was finished, it was the longest rigid span anywhere in the world. The river that had divided the country was now stitched together with iron. |
| **s13** | 262.4 / 21.7 | 1894 | The All-Weather Road | *Through Mushkaf and Bolan, the first train runs clear to Quetta.* | The first roads to Quetta were fragile; landslips swept the alignment away again and again. So a new all-weather line was built through Mushkaf and the Bolan. In eighteen ninety-four, the first through train at last ran clear into Quetta. |
| **s14** | 283.1 / 21.7 | 1904 | The Heart of Steam | *At Mughalpura, the workshops that built and healed the line.* | Around nineteen oh four, the North Western Railway gathered its great workshops at Mughalpura, near Lahore. Here coaches, wagons, and locomotives were built, repaired, and made whole again. It was the industrial heart that kept the iron horses running. |
| **s15** | 303.8 / 21.7 | 1900s | Palaces of Steam | *Grand stations rise as civic statements across the network.* | The trunk stations — Karachi, Lahore, Rawalpindi, Multan, Peshawar — anchored the growing network. They were built not merely as shelters, but as statements, in a grand blend of colonial and Mughal stone. To arrive at one was to feel the weight of the whole system behind it. |
| **s16** | 324.5 / 21.7 | 1900s | The Human Machine | *Drivers, firemen, platelayers and clerks who ran the iron daily.* | Behind every train stood an army of people. Anglo-Indian drivers and supervisors, and a vast workforce of platelayers, gangmen, firemen, and clerks, ran the line day after day. The iron machine moved only because the human one never stopped. |
| **s17** | 345.2 / 21.7 | 1914–1918 | The Railway at War | *Troops, animals and matériel move to the frontier and the ports.* | When the Great War came, the railway that had been built for the frontier was fully called upon. It carried troops, animals, and supplies to the borders and down to the ports for distant fronts. The strategic logic that laid these rails was now tested in earnest. |
| **s18** | 365.9 / 21.7 | 1925 | Through the Khyber | *Thirty-four tunnels of broad gauge climb to Landi Kotal.* | On the third of November, nineteen twenty-five, the Khyber Pass Railway opened from Jamrud to Landi Kotal. Thirty-four tunnels and more than ninety bridges carried broad gauge straight through the famous pass. It was one of the boldest strategic railways ever attempted. |
| **s19** | 386.6 / 21.7 | 1920s–30s | The Everyday Timetable | *Mail trains and frontier branches — the network at its height.* | Between the wars, the North Western Railway reached its full maturity. Prestige mail trains and dense frontier traffic ran across Punjab, Sindh, and Balochistan. At its height, the timetable itself was a portrait of a country in motion. |
| **s20** | 407.3 / 21.7 | 1942 | The First Retreat | *A flood takes the Chappar Rift; a proud line is lifted away.* | Not every chapter was one of building. On a July night in nineteen forty-two, a flash flood swept away the bench beneath the Chappar Rift line. Within a year the track was closed and lifted — the first great retreat of the network. |
| **s21** | 428.0 / 21.7 | 1947 | A Line Divided | *At independence, one system is severed at a new border.* | In August of nineteen forty-seven, independence came, and with it a border. The single integrated railway was cut in two — the greater part to the new Pakistan, the remainder to India. Near Lahore and Amritsar, a line that had always been one was severed. |
| **s22** | 448.7 / 21.7 | 1947 *(SOBER)* | The Refugee Trains | *Across the new border, the carriages carried a whole people's grief.* | In those same weeks, the trains carried something heavier than freight. Hundreds of thousands fled across the new border in crowded carriages, seeking safety on the far side. Many never arrived. We remember them quietly, and let the empty platforms speak. |
| **s23** | 469.4 / 21.7 | 1961 | A New Name | *The North Western Railway becomes the Pakistan Western Railway.* | For years after partition, the old name endured on the trains of Pakistan. Then, on the first of February, nineteen sixty-one, the line was formally renamed the Pakistan Western Railway. An old system had begun, at last, to belong wholly to a new country. |
| **s24** | 490.1 / 21.7 | 1974 | One Name, One Nation | *The lines are consolidated as Pakistan Railways.* | After the loss of the eastern wing in nineteen seventy-one, the western network stood alone. In nineteen seventy-four it was reorganised into a single autonomous railway. From all those companies and crossings, one name finally remained — Pakistan Railways. |
| **s25** | 510.8 / 26.0 | *(none)* | The Iron Endures | *[CLIENT LOGO]* | The river still runs, and so do the trains beside it. From a charter on paper to a nation's railway, the iron horse of the Indus carried more than freight — it carried a country into being. And along the great river, it runs still. |

---

## 4. Storyboard digest

Ken Burns direction alternates: even scene index = **+1**, odd = **−1**. Every IN is a 1.0s cross-dissolve except the three ★ blooms. All body photos frame the **left third clear** for the text block; s00 and s25 are centered.

| # | image subject | Ken Burns | transition IN |
|---|---------------|-----------|----------------|
| s00 | Single rail line vanishing to a hazy dawn horizon, Indus implied as a pale band; empty, timeless. CENTERED title. | +1, push 1.12, drift down-right | fade up from black |
| s01 | Indus with a country boat / early Flotilla steamer mid-river heading upstream; open left bank. | −1, 1.14, drift left-up | cross-dissolve |
| s02 | **Document plate** — Scinde Railway charter / Act page / survey map of lower Sindh. No train. | +1, 1.13, drift right-down | cross-dissolve |
| s03 | Early loco + short rake on fresh track receding across lower-Indus scrub; open sky left. | −1, 1.15, drift right-up | cross-dissolve |
| s04 | Lahore Junction's fortified frontage, turrets/loopholes, low-angle loom; open forecourt left. | +1, 1.14, slow rise | cross-dissolve |
| s05 | **Map / company-report plate** — Karachi→Delhi as one line (SP&DR). No train. | −1, 1.12, drift down-left | cross-dissolve |
| s06 | Long iron lattice bridge across the wide **Sutlej**, low-angle; open water/sky left. | +1, 1.15, drift right | **★ soft white bloom** then settle |
| s07 | Attock crossing in its narrow gorge, dark rock walls, Indus fast below; gorge mouth/sky left. | −1, **1.16** (deepest), drift down into chasm | cross-dissolve |
| s08 | **Formation record / system map** of the new NWR. No train. | +1, 1.13, drift up-right | cross-dissolve |
| s09 | Switchback track climbing the bare Bolan Pass, small loco dwarfed; open valley/sky left. | −1, 1.15, upward drift | cross-dissolve |
| s10 | Louise Margaret Bridge across the Chappar gorge (200+ ft), vertiginous high-angle; void/sky left. | +1, 1.16, drift down | cross-dissolve |
| s11 | Khojak Tunnel portal, engine just emerging with smoke; lit approach left. | −1, 1.14, push in toward portal | cross-dissolve |
| s12 | Lansdowne cantilever at Sukkur, **single span only** (no 1962 Ayub Bridge); sky upper-left. | +1, 1.15, drift right along span | cross-dissolve |
| s13 | Through train on the new Mushkaf–Bolan alignment, stone embankment in arid hills; open ground left. | −1, 1.14, drift right-down | cross-dissolve |
| s14 | Mughalpura workshops interior, loco frames in a row under glazed roof; lit aisle left. | +1, 1.13, drift right down the locos | **★ soft white bloom** then settle |
| s15 | Grand trunk-station frontage (Lahore/Karachi register), colonial-Mughal stone; open plaza left. | −1, 1.14, slow rise up façade | cross-dissolve |
| s16 | Railway crew at work beside an engine (drivers/firemen/gang); open track/ground left. Faces honoured. | +1, 1.13, gentle drift toward crew | cross-dissolve |
| s17 | Wartime troop/supply train loading (soldiers, animals, matériel); empty platform end/sky left. | −1, 1.15, drift right tracking train | cross-dissolve |
| s18 | Khyber Pass Railway threading tunnel-and-bridge toward Landi Kotal, jagged ranges; open pass/sky left. | +1, 1.16, climbing drift up pass | cross-dissolve |
| s19 | Prestige mail train at speed across open Punjab/Sindh plain, plume of smoke; sky upper-left. | −1, 1.14, drift right with train | cross-dissolve |
| s20 | Abandoned Chappar Rift after the flood — a gap where iron used to be; empty gorge/sky left. Elegiac. | +1, 1.12 (slowed), drift down over gap | cross-dissolve |
| s21 | A single track running to a new border near Lahore/Amritsar, lonely marker; open sky left. | −1, 1.13, drift toward border point | **★ soft white bloom** then settle |
| s22 | **Quiet, non-graphic** — empty dusk platform, or packed carriage at distance/silhouette pulling away; long empty platform left. | +1, 1.12 (very slow, held), barely-there drift | cross-dissolve (gentle) |
| s23 | Engine/nameplate with the new "Pakistan Western Railway" identity; clean ground/sky left. | −1, 1.14, drift in toward lettering | cross-dissolve |
| s24 | Modern consolidated Pakistan Railways scene, train at a major station / rails to open horizon; open horizon left. | +1, 1.15, drift up-right toward horizon | cross-dissolve |
| s25 | Atmospheric centered plate echoing s00 — rails beside the broad Indus to a far horizon at last light. CENTERED title + `[CLIENT LOGO]`. | −1, 1.12 (calmest), drift toward horizon then settle | cross-dissolve in; **fade to black on the out** (longest hold, 26s) |

---

## 5. Asset list

**Licensing first:** prefer **Public Domain / CC0** — almost everything here is pre-1928 / British-Raj-era and overwhelmingly PD. Skip watermarked previews, "editorial use only" stock, and Getty/Alamy rights-managed items where a clean PD original exists (a museum may charge for a high-res *scan* of a PD photo — the image itself is still PD; find the free/Commons copy). **Record source + license in `CREDITS.txt` as you download.**

Save path convention: `assets/images/sNN_keyword.jpg`.

| save-as | primary archive | one-line caveat |
|---------|-----------------|------------------|
| `s00_rails.jpg` | WC MediaSearch "North Western Railway India track horizon" | Quiet receding-rails / open-horizon plate, no people, no datable building; reusable for s25; no modern colour. |
| `s01_flotilla.jpg` | WC MediaSearch "Indus Steam Flotilla steamer river" | Verify it pre-dates the rail (1850s–60s), not a mislabelled 1880s flotilla photo; engraving OK. |
| `s02_charter.jpg` | Grace's Guide — Scinde Railway | Want a **document/Act/prospectus/map**, NOT a train (no engine existed yet). |
| `s03_kotri.jpg` | WC MediaSearch "Karachi Kotri railway 1861" | Avoid the 1896–98 Karachi Cantonment station — wrong building, 35 yrs too late. |
| `s04_lahore.jpg` | WC Category: Lahore railway station | Fortified Lahore Junction; caption by the **photo's** date (towers strengthened over time), don't claim "1860" for a later view. |
| `s05_spdr_map.jpg` | WC Category: Rail transport maps of Pakistan | A **map/report** showing Karachi→Delhi reach, not a train; merger is **1870**, distinct from the 1861 opening. |
| `s06_empress.jpg` | WC MediaSearch "Empress Bridge Sutlej Adamwahan" | Spans the **Sutlej**, NOT the Indus (common mislabel). |
| `s07_attock.jpg` | WC MediaSearch "Attock railway bridge Indus" | Want the **original 1883 girder bridge**; reject 20th-c. replacement / double bridges. |
| `s08_nwr_map.jpg` | WC Category: North Western State Railway | A **system map / formation record / HQ**, not a single locomotive. |
| `s09_bolan.jpg` | WC MediaSearch "Bolan Pass railway Quetta" | The **1886 Bolan** route — distinct from the 1894 Mushkaf–Bolan (s13); don't merge dates. |
| `s10_chappar.jpg` | National Galleries of Scotland (Fred Bremner, Louise Margaret Bridge) | Show the **working era**, not the 1942 wash-out ruin; the Bremner view is iconic. |
| `s11_khojak.jpg` | WC MediaSearch "Khojak Tunnel Shelabagh portal" | The ornate **tunnel portal** (later on Pakistani currency); first engine through = 1891. |
| `s12_lansdowne.jpg` | CUL Royal Commonwealth Society (Y30244A construction album) | **Single Lansdowne span only** — any frame with the adjacent **1962 Ayub Bridge** is post-1962. |
| `s13_mushkaf.jpg` | IRFCA gallery ("Mushkaf Bolan" / "Quetta") | The **all-weather Mushkaf–Bolan** / first through train (1894); keep separate from 1886 Bolan (s09). |
| `s14_mughalpura.jpg` | WC MediaSearch "Mughalpura workshops North Western Railway" | Workshop interior/yard near Lahore; use documented **1904** date, not the unconfirmed "1912." |
| `s15_station.jpg` | WC Category: Railway stations in Pakistan | A grand trunk station; date the photo by the **building shown**, not the line's opening year. |
| `s16_workforce.jpg` | WC MediaSearch "Indian railway staff drivers platelayers 1900s" | Staff photos often **undated** — only use one with a credible year; don't over-claim a date. |
| `s17_war.jpg` | IWM collections "India railway troops First World War" | **Imagery thin** for NWR-specific WWI; a correctly-dated general Indian-railway logistics frame is OK, avoid European-front stock. |
| `s18_khyber.jpg` | National Army Museum ("opening of the Khyber railway, 1925") | The **1925 Jamrud–Landi Kotal opening** specifically; avoid 1930s camp photos and the 1919 ropeway. |
| `s19_mail.jpg` | WC MediaSearch "North Western Railway mail train timetable 1930s" | Need a **firm 1920s–30s** caption; don't pass off a 1900s image as 1930s. |
| `s20_chappar_lost.jpg` | National Galleries of Scotland (Fred Bremner, the rift intact) | Show the **intact** line (loss is narrated, not pictured); use a *different* Chappar frame than s10. |
| `s21_partition.jpg` | Partition Museum — "The Railways and Partition" (Google Arts & Culture) | The **split / new border** (Lahore–Amritsar–Wagah) — NOT the 1961 rename (s23), NOT a refugee-horror frame (s22). |
| `s22_refugee.jpg` | Partition Museum story (Google Arts & Culture) | **ETHICAL — quiet, non-graphic frame; verify date AND side.** Never gore / ghost-train / named-massacre; default to the emptier frame if unsure. |
| `s23_pwr.jpg` | WC Category: Pakistan Railways | The **1961 renaming** — a Pakistan Western Railway nameplate/loco/document; distinct from s21 (1947) and s24 (1974). |
| `s24_pakrail.jpg` | WC Category: Pakistan Railways | A Pakistan Railways loco/nameplate from the **1971→1974** transition (numeral 1974); prefer B&W / monochrome. |
| `s25_horizon.jpg` | WC MediaSearch "Indus river railway horizon" | Calm rails/horizon plate for the quiet close; reusing the s00 plate is fine and intentional (bookend). |

**Audio** — `assets/audio/score.mp3`: royalty-free, period-cinematic bed, **~9 min** (film is 536.8s). One long track, or loop a ~4–5 min bed with a faded seam (let the outro breathe). Mood string (paste verbatim): *"wistful nostalgic orchestral, soft piano and warm strings, gentle swell, vintage, period documentary."* Sources: Pixabay Music (no-copyright), Free Music Archive (check each CC license), Uppbeat (free w/ attribution). Prefer slow ~70–80 bpm piano-and-strings with one gentle swell — nothing percussive or trailer-modern. Log title/artist/URL/license in `CREDITS.txt`.

**Texture** — `assets/textures/paper.png`: aged-paper / old-newspaper overlay, CC0/PD. Sources: Wikimedia Commons "old paper texture aged", Internet Archive period docs (screenshot a blank/foxed margin), rawpixel CC0, Poly Haven. Want a high-res, evenly-lit aged sheet (foxing/fibre OK, no heavy printed text); transparent PNG or one keyed to multiply works best. Confirm CC0/PD and log it.

---

## 6. Staged build / troubleshooting prompts

Copy-paste prompts for a human iterating in Claude Code. Always end each stage with `npx hyperframes lint && npx hyperframes validate && npx hyperframes inspect` to 0 errors before moving on.

### Stage 1 — simple slideshow (placeholders only) · ALREADY BUILT
The base `index.html` exists with all 26 scenes, the timing from §2, the locked grade/type/motion from `DESIGN.md`, and placeholder `.photo` divs (no real images yet).

**Preview it:**
```
npx hyperframes lint
npx hyperframes validate
npx hyperframes preview
```
Confirm: 26 scenes, ~536.8s total, alternating Ken Burns, 1.0s dissolves, blooms on s06/s14/s21, text reads on the left, centered s00/s25.

### Stage 2 — drop in real images
Download every image per §5 into `assets/images/sNN_keyword.jpg`. Then swap each placeholder for a real `<img>`.

> **Prompt:** "For each scene s00–s25, replace the placeholder div inside that scene's `.photo` element with `<img src="assets/images/sNN_keyword.jpg" alt="">` (use the exact save-as filename from ASSET_SHORTCUTS.md / the runbook asset table). Keep the `.photo` element, the Ken Burns target, and the grade filters exactly as they are — only the inner content changes from a placeholder div to the `<img>`. Don't animate width/height; the image fills its full-bleed `.photo` parent. Then run lint, validate, and inspect and report any errors."

The slot→`<img>` swap, concretely: the placeholder
```html
<div class="photo"> <div class="placeholder">s07</div> </div>
```
becomes
```html
<div class="photo"> <img src="assets/images/s07_attock.jpg" alt=""> </div>
```
Re-run `lint`, `validate`, `inspect`. Use `npx hyperframes snapshot --at <t>` to eyeball framing (left third clear, single-span Lansdowne at s12, Sutlej at s06, etc.).

### Stage 2A — music
> **Prompt:** "Add `assets/audio/score.mp3` as an `<audio>` element that is a **direct child of `#root`** (the composition root), spanning the whole film. Set volume to ~0.9. Use the main timeline to fade it in over the first 1.5s and out over the final 2.0s. Keep it ducked roughly −8 dB under any voiceover. Then lint, validate, inspect."

Notes: `<audio>` must be a direct child of root (composition contract). Fades are driven by the single paused timeline, not CSS. If VO is present, the music sits ~−8 dB under it.

### Stage 2B-LOCAL — free Kokoro voiceover
Generate one WAV per scene from `docs/narration.md` (one block per scene):
```
npx hyperframes tts "<the s07 narration line>" --provider kokoro --voice bm_george --speed 0.95 -o assets/audio/vo_s07.wav
```
Repeat for s00–s25 (`vo_s00.wav` … `vo_s25.wav`).

> **Prompt:** "For each scene, add its `assets/audio/vo_sNN.wav` as an `<audio>` element that is a **direct child of `#root`** with `data-start` equal to that scene's start time from the timing ledger (s00=0.0, s01=14.0, … s25=510.8). Leave the music bed in place and keep it ducked ~−8 dB under the VO. Then lint, validate, inspect."

Each `vo_sNN.wav` is a direct child of root with `data-start` at that scene's start. (ElevenLabs / HeyGen are optional paid upgrades via `ELEVENLABS_API_KEY` / `HEYGEN_API_KEY`.)

### Stage 3 — polish + render
Final polish pass (framing, grade consistency, caption fit, audio levels), then:
```
npx hyperframes render --output iron-horse-of-the-indus-1080p.mp4
```

**Optional 4:5 social cut (1080×1350):** re-frame for portrait-safe centering (subjects pull toward center; left-third text may need re-centering) and render:
```
npx hyperframes render --output iron-horse-of-the-indus-1080x1350.mp4
```

---

## 7. Pre-delivery checklist

- [ ] `npx hyperframes lint` — **0 errors**.
- [ ] `npx hyperframes validate` (headless Chrome) — **0 errors** (no JS errors, no missing assets).
- [ ] `npx hyperframes inspect` — **0 errors**; total duration reads **~536.8s**, 26 clips, overlaps 1.0s.
- [ ] Snapshots reviewed across all 26 scenes (`snapshot --at <t>`): framing leaves the left third clear, s00/s25 centered.
- [ ] First frame and last frame are **not black** (s00 fades up from black into the plate; s25 holds before its fade-out).
- [ ] Captions and titles **not clipped** — single-line italic captions fit, Playfair titles fit on the band, ≥160px title-safe padding holds.
- [ ] `CREDITS.txt` filled — source institution, collection/shelfmark or Commons URL, photographer (if known), license tag for **every** image, the music track, and the paper texture.
- [ ] **Licensing confirmed** — every asset is PD/CC0 (or a verified free license); no watermarked / rights-managed / editorial-only items.
- [ ] **Audio levels** — music ~0.9 with 1.5s in / 2.0s out fades; VO ducks music ~−8 dB; no clipping; outro allowed to breathe.
- [ ] **Partition scenes handled with restraint** — s21 (the split, NOT the rename, NOT a horror frame), s22 (quiet/non-graphic frame, date AND side verified, no gore/ghost-train/named-massacre). When in doubt, the emptier, quieter frame.
- [ ] Date integrity spot-check: s06 Sutlej (not Indus), s12 single Lansdowne span (no 1962 Ayub Bridge), s14 = 1904 (not 1912), three Quetta routes kept distinct (s09 1886 / s10 1887 / s13 1894), s21≠s23≠s24 dates.
