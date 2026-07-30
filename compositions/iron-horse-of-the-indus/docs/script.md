# The Iron Horse of the Indus — Narrator Script & Timing

**Film:** *The Iron Horse of the Indus — the North Western Railway and the making of a nation, 1860s→1970s*
**Format:** ~9-minute cinematic B&W parallax photo-slideshow, stately/premium, warm unhurried documentary voice.
**Source spine:** `docs/research.md` (verified chronological spine — obey its dates and sober-handling notes).

## Computed total duration

- **Scene count:** 26 (s00 title card + s01–s24 research beats + s25 outro).
- **Last scene (s25):** `data-start = 510.8s`, `data-duration = 26.0s` → ends at **536.8s**.
- **Total film length = 536.8s** (~8:57) — inside the 535–545s window. ✓
- **Overlaps:** every consecutive pair overlaps by ~1.0s for the cross-dissolve (see ledger). ✓

### Timing scheme (honest math)

- Title card s00: `start 0.0`, `dur 15.0` → ends 15.0.
- Body scenes s01–s24: `dur 21.7s` each; `start_k = 14.0 + (k−1)·20.7` (k = 1…24). Step of 20.7 = (21.7 − 1.0), so each clip begins 1.0s before the previous one ends → ~1.0s dissolve overlap.
- Outro s25: `start 510.8`, `dur 26.0` (a touch longer for the quiet close) → ends 536.8.
- Rounding note: all starts/durations are exact to one decimal; the only "round" is that step 20.7 is itself one-decimal exact, so overlaps are a clean 1.0s throughout with **no accumulated drift**. The single deliberate asymmetry is the shorter title (15.0s) and longer outro (26.0s); the s00→s01 overlap is therefore 1.0s (s01 starts at 14.0, s00 ends at 15.0) — consistent with the rest.

---

## TIMING LEDGER

| # | scene | data-start | data-duration | ends (start+dur) | overlap with next (this.end − next.start) |
|---|-------|-----------:|--------------:|-----------------:|------------------------------------------:|
| s00 | TITLE | 0.0 | 15.0 | 15.0 | 1.0 |
| s01 | beat 1 | 14.0 | 21.7 | 35.7 | 1.0 |
| s02 | beat 2 | 34.7 | 21.7 | 56.4 | 1.0 |
| s03 | beat 3 | 55.4 | 21.7 | 77.1 | 1.0 |
| s04 | beat 4 | 76.1 | 21.7 | 97.8 | 1.0 |
| s05 | beat 5 | 96.8 | 21.7 | 118.5 | 1.0 |
| s06 | beat 6 | 117.5 | 21.7 | 139.2 | 1.0 |
| s07 | beat 7 | 138.2 | 21.7 | 159.9 | 1.0 |
| s08 | beat 8 | 158.9 | 21.7 | 180.6 | 1.0 |
| s09 | beat 9 | 179.6 | 21.7 | 201.3 | 1.0 |
| s10 | beat 10 | 200.3 | 21.7 | 222.0 | 1.0 |
| s11 | beat 11 | 221.0 | 21.7 | 242.7 | 1.0 |
| s12 | beat 12 | 241.7 | 21.7 | 263.4 | 1.0 |
| s13 | beat 13 | 262.4 | 21.7 | 284.1 | 1.0 |
| s14 | beat 14 | 283.1 | 21.7 | 304.8 | 1.0 |
| s15 | beat 15 | 303.8 | 21.7 | 325.5 | 1.0 |
| s16 | beat 16 | 324.5 | 21.7 | 346.2 | 1.0 |
| s17 | beat 17 | 345.2 | 21.7 | 366.9 | 1.0 |
| s18 | beat 18 | 365.9 | 21.7 | 387.6 | 1.0 |
| s19 | beat 19 | 386.6 | 21.7 | 408.3 | 1.0 |
| s20 | beat 20 | 407.3 | 21.7 | 429.0 | 1.0 |
| s21 | beat 21 | 428.0 | 21.7 | 449.7 | 1.0 |
| s22 | beat 22 | 448.7 | 21.7 | 470.4 | 1.0 |
| s23 | beat 23 | 469.4 | 21.7 | 491.1 | 1.0 |
| s24 | beat 24 | 490.1 | 21.7 | 511.8 | 1.0 |
| s25 | OUTRO | 510.8 | 26.0 | 536.8 | — (final) |

**Sum check:** s25.end = 536.8s ∈ [535, 545]. ✓ Every overlap = 1.0s. ✓

---

## SCENE TABLE

| # | data-start | data-duration | NUMERAL / era-label | TITLE (Playfair) | CAPTION (italic, one line) | VO (warm, unhurried) |
|---|-----------:|--------------:|---------------------|------------------|----------------------------|----------------------|
| **s00** | 0.0 | 15.0 | *(none — title card, centered, no year/band)* | The Iron Horse of the Indus | *The North Western Railway and the making of a nation, eighteen sixties to nineteen seventies.* | Before the rails, there was only the river. This is the story of how iron came to the valley of the Indus, and of the nation it helped to carry into being. |
| **s01** | 14.0 | 21.7 | 1850s | The River Highway | *Before the rails, the Indus carried everything northward from Karachi.* | Long before the first track was laid, the Indus itself was the highway of the valley. Country boats, and soon the steamers of the Indus Flotilla, carried freight and people up from Karachi toward Multan. The river was slow, and seasonal, and it was all there was. |
| **s02** | 34.7 | 21.7 | 1855 *(imagery: charter document / map, not a train)* | A Line on Paper | *The Scinde Railway is chartered — the legal birth of the railways.* | In March of eighteen fifty-five, the Scinde Railway Company was founded by deed, and then by Act of Parliament. No track yet existed, and no engine had run. But on paper, the railways of this country had been born. |
| **s03** | 55.4 | 21.7 | 1861 | Karachi to Kotri | *The first track opens — one hundred and eight miles of new iron.* | On the thirteenth of May, eighteen sixty-one, the first public line opened between Karachi and Kotri. One hundred and eight miles of new iron tied the port to the lower river. For the first time, a train ran on the soil of what would one day be Pakistan. |
| **s04** | 76.1 | 21.7 | 1860 | The Fortress Station | *Lahore reaches Amritsar; a station built like a stronghold.* | Far to the north, the first train ran from Lahore to Amritsar in eighteen sixty. Lahore Junction was raised in those years as a fortress in disguise — turrets, loopholes, and walls thick enough to withstand a siege. The memory of eighteen fifty-seven was still very close. |
| **s05** | 96.8 | 21.7 | 1870 *(imagery: company report / map)* | Four Become One | *The Scinde, Punjab and Delhi Railway — Karachi to Delhi under one hand.* | In eighteen seventy, four enterprises were joined into one: the Scinde Railway, the Punjab Railway, the Indus Steam Flotilla, and the Delhi Railway. Together they formed the Scinde, Punjab and Delhi Railway. Now a single operator reached from Karachi all the way to Delhi. |
| **s06** | 117.5 | 21.7 | 1878 | The Empress Bridge | *Iron vaults the Sutlej in the country of five rivers.* | On the seventh of June, eighteen seventy-eight, the Empress Bridge was opened across the Sutlej, between Bahawalpur and Adam Wahan. It was one of the first great crossings in the land of the five rivers. Each river the engineers reached was a wall, and each bridge a kind of victory. |
| **s07** | 138.2 | 21.7 | 1883 | Iron Over the Indus | *At Attock, rail finally crosses the great river of the north.* | At Attock, the Indus runs deep and fast through a narrow gorge. On the twenty-fourth of May, eighteen eighty-three, the railway at last vaulted that river on the road north to Peshawar. The great river of the north had been crossed. |
| **s08** | 158.9 | 21.7 | 1886 *(imagery: map / formation record)* | The Line Takes Its Name | *Many railways are forged into the North Western State Railway.* | In January of eighteen eighty-six, the older lines were gathered together — the Indus Valley, the Punjab Northern, and the frontier sections toward Kandahar. From them was forged the North Western State Railway. It is the system around which this whole story turns. |
| **s09** | 179.6 | 21.7 | 1886 | Through the Bolan | *Strategic track climbs the pass toward the Afghan frontier.* | That same year, eighteen eighty-six, the first rails reached Quetta through the Bolan Pass. This was track laid with one eye on the Afghan frontier — a railway as much for armies as for trade. The mountains here gave nothing away easily. |
| **s10** | 200.3 | 21.7 | 1887 | The Chappar Rift | *The Louise Margaret Bridge hangs high above a desert gorge.* | A second road to Quetta climbed through Harnai and the Chappar Rift, opened in eighteen eighty-seven. The Louise Margaret Bridge spanned a gorge more than two hundred feet above the bed. It was among the boldest and most beautiful engineering on the whole line. |
| **s11** | 221.0 | 21.7 | 1891 | The Mountain Pierced | *The first engine breaks through the long Khojak Tunnel.* | Beneath the Khwaja Amran range, men dug for three years toward each other in the dark. On the fifth of September, eighteen ninety-one, the first engine passed through the Khojak Tunnel. For more than a century it would remain the longest tunnel in the region. |
| **s12** | 241.7 | 21.7 | 1889 | Lansdowne at Sukkur | *On completion, the longest rigid span in the world.* | At Sukkur, the Lansdowne Bridge was completed in eighteen eighty-nine, joining its banks across the Indus. On the day it was finished, it was the longest rigid span anywhere in the world. The river that had divided the country was now stitched together with iron. |
| **s13** | 262.4 | 21.7 | 1894 | The All-Weather Road | *Through Mushkaf and Bolan, the first train runs clear to Quetta.* | The first roads to Quetta were fragile; landslips swept the alignment away again and again. So a new all-weather line was built through Mushkaf and the Bolan. In eighteen ninety-four, the first through train at last ran clear into Quetta. |
| **s14** | 283.1 | 21.7 | 1904 | The Heart of Steam | *At Mughalpura, the workshops that built and healed the line.* | Around nineteen oh four, the North Western Railway gathered its great workshops at Mughalpura, near Lahore. Here coaches, wagons, and locomotives were built, repaired, and made whole again. It was the industrial heart that kept the iron horses running. |
| **s15** | 303.8 | 21.7 | 1900s | Palaces of Steam | *Grand stations rise as civic statements across the network.* | The trunk stations — Karachi, Lahore, Rawalpindi, Multan, Peshawar — anchored the growing network. They were built not merely as shelters, but as statements, in a grand blend of colonial and Mughal stone. To arrive at one was to feel the weight of the whole system behind it. |
| **s16** | 324.5 | 21.7 | 1900s | The Human Machine | *Drivers, firemen, platelayers and clerks who ran the iron daily.* | Behind every train stood an army of people. Anglo-Indian drivers and supervisors, and a vast workforce of platelayers, gangmen, firemen, and clerks, ran the line day after day. The iron machine moved only because the human one never stopped. |
| **s17** | 345.2 | 21.7 | 1914–1918 | The Railway at War | *Troops, animals and matériel move to the frontier and the ports.* | When the Great War came, the railway that had been built for the frontier was fully called upon. It carried troops, animals, and supplies to the borders and down to the ports for distant fronts. The strategic logic that laid these rails was now tested in earnest. |
| **s18** | 365.9 | 21.7 | 1925 | Through the Khyber | *Thirty-four tunnels of broad gauge climb to Landi Kotal.* | On the third of November, nineteen twenty-five, the Khyber Pass Railway opened from Jamrud to Landi Kotal. Thirty-four tunnels and more than ninety bridges carried broad gauge straight through the famous pass. It was one of the boldest strategic railways ever attempted. |
| **s19** | 386.6 | 21.7 | 1920s–30s | The Everyday Timetable | *Mail trains and frontier branches — the network at its height.* | Between the wars, the North Western Railway reached its full maturity. Prestige mail trains and dense frontier traffic ran across Punjab, Sindh, and Balochistan. At its height, the timetable itself was a portrait of a country in motion. |
| **s20** | 407.3 | 21.7 | 1942 | The First Retreat | *A flood takes the Chappar Rift; a proud line is lifted away.* | Not every chapter was one of building. On a July night in nineteen forty-two, a flash flood swept away the bench beneath the Chappar Rift line. Within a year the track was closed and lifted — the first great retreat of the network. |
| **s21** | 428.0 | 21.7 | 1947 | A Line Divided | *At independence, one system is severed at a new border.* | In August of nineteen forty-seven, independence came, and with it a border. The single integrated railway was cut in two — the greater part to the new Pakistan, the remainder to India. Near Lahore and Amritsar, a line that had always been one was severed. |
| **s22** | 448.7 | 21.7 | 1947 *(HANDLE SOBERLY — quiet, non-graphic frame)* | The Refugee Trains | *Across the new border, the carriages carried a whole people's grief.* | In those same weeks, the trains carried something heavier than freight. Hundreds of thousands fled across the new border in crowded carriages, seeking safety on the far side. Many never arrived. We remember them quietly, and let the empty platforms speak. |
| **s23** | 469.4 | 21.7 | 1961 | A New Name | *The North Western Railway becomes the Pakistan Western Railway.* | For years after partition, the old name endured on the trains of Pakistan. Then, on the first of February, nineteen sixty-one, the line was formally renamed the Pakistan Western Railway. An old system had begun, at last, to belong wholly to a new country. |
| **s24** | 490.1 | 21.7 | 1974 | One Name, One Nation | *The lines are consolidated as Pakistan Railways.* | After the loss of the eastern wing in nineteen seventy-one, the western network stood alone. In nineteen seventy-four it was reorganised into a single autonomous railway. From all those companies and crossings, one name finally remained — Pakistan Railways. |
| **s25** | 510.8 | 26.0 | *(none — outro, centered, no year/band)* | The Iron Endures | *[CLIENT LOGO]* | The river still runs, and so do the trains beside it. From a charter on paper to a nation's railway, the iron horse of the Indus carried more than freight — it carried a country into being. And along the great river, it runs still. |

---

## Handling notes carried from the research spine

- **s02 (1855) and s05 (1870)** are *paper milestones* — imagery should be a charter document, company report, or map, never an anachronistic "first train" photo. Kept distinct in the VO (1855 = charter; 1870 = SP&DR merger).
- **s06 Empress Bridge** spans the **Sutlej**, not the Indus — stated explicitly in caption and VO.
- **s09 / s10 / s13** keep the three Quetta routes separate: Bolan (1886), Chappar Rift/Harnai (1887), Mushkaf–Bolan through-train (1894).
- **s12 Lansdowne (1889)** — single span read; avoid any photo also showing the 1962 Ayub Bridge.
- **s14 Mughalpura** uses the documented **1904** (site) date, not the unconfirmed "1912."
- **s21 (partition split, 1947)** and **s23 (renaming, 1961)** are kept apart — the split is not the rename.
- **s22 Refugee trains** — handled with restraint and dignity: implied loss, empty platforms, packed carriages. No spectacle, no gore, no named massacre. Quiet, non-graphic frame only.
- **s24** presented as the **1971→1974** transition consolidated under one name, per the contested-dates note (numeral shown as 1974, the reorganisation year).
