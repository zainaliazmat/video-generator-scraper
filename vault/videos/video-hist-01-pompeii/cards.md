---
summary: Build-ready CONTENT SPEC for every CARD (parchment motion-graphic + the timestamp-chip UI) in "Pompeii Ka Akhri Din". Each entry = id, segment, exact on-screen text (Roman-Urdu + any Latin/refs), the data for diagrams/maps, and the HyperFrames motion. Design tokens/fonts live in [[DESIGN]]; scene list in [[storyboard]]. CARDs need no sourcing — built in HyperFrames.
updated: 2026-07-13
source: script [[script-v1-urdu]] · film rules [[DESIGN]] · storyboard [[storyboard]]
status: DRAFT v1 — Quran verse wording (C-61b/c) MUST be verified vs an authoritative Urdu tafsir before record.
---

# Pompeii — CARD content specs (build in HyperFrames)

**How to read this:** every card is `[C-##]`. "Text" = paste verbatim on screen (Roman-Urdu per creator rule,
English titles/refs as noted). "Motion" = the HyperFrames animation. Style/tokens (parchment `#e8dcc0`,
pompeii-red `#9c342a`, ink `#f4f1ea`, fonts Inter/Mukta 600–800 for Urdu, Playfair for Latin/headlines) are
fixed in [[DESIGN]] — don't restate per card. All cards get the persistent grain + faint paper texture.

---

## ★ Recurring UI — the TIMESTAMP CHIP (the story spine)
- **Where:** bottom-left, small, uppercase, tracked sans, `--ink` on a faint dark band. Appears from seg 07.
- **Motion:** each new value cross-fades/flips in place; small 2.5D parallax (travels ~25–35% of image travel).
- **Sequence (in order of appearance):**
  `6:00 AM` (07) → `7:00 AM` (15) → `8:00 AM` (17) → `9:00 AM` (18) → `10:00 AM` (18B) → `12:00 PM` (22)
  → `2:00 PM` → `3:00 PM` → `4:00 PM` (31) → `7:00 PM` (35) → `3:00 AM` (40) → `6:30 AM` (43)
  → then it becomes a **date** chip: `AUG 2024` (54) → `NOV 2024` (56) → `APR 2026` (61).
- After the eruption the chip IS the spine — keep it on screen through the disaster beats.

---

## SECTION 1

### [C-06] TITLE CARD · seg 06 · over 06A (epic wide)
- **Text (display serif, burns in):** `POMPEII KA AKHRI DIN`
- **Subtitle (smaller, fades under):** `Jab pura shehar ek raat ma patthar ban gaya`
- **Motion:** slow scale-in + fade over the held 06A drift; pompeii-red underline wipe.

### [C-07] REFRAME CARD · seg 07 · parchment
- **Text (two lines, line 2 emphasized red):**
  `ERUPTION NAHI.`
  `US SA PEHLI SUBAH.`
- **Foot (small):** `— us subah ki kahani`
- **Then:** the `6:00 AM` timestamp chip appears bottom-left (first time).
- **Motion:** line-by-line reveal; beat of silence after line 2, then the chip slides in.

---

## SECTION 2

### [C-08] MAP CARD · seg 08 · textured animated map (How-So style)
- **Sequence + labels:** `ROMAN EMPIRE` (highlight extent) → zoom → `KHAARI-E-NAPLES / Bay of Naples`
  → pin drops → `POMPEII`. Date chip on map: `79 AD`.
- **Motion:** continuous zoom-in from empire to the city pin; textured relief map; pin bounce.

### [C-11] VOLCANO CARD · seg 11 · Latin-dictionary style, parchment
- **Layout:** a dictionary entry with the headword and an EMPTY definition:
  `volcano`  ·  *(Latin, 79 AD)*
  `———————————————`  ← blank definition line
- **Beat:** hold in silence (the point: the word/definition did not exist).
- **Motion:** headword types in; the definition line stays blank; a faint `?` fades in, then out.

---

## SECTION 3

### [C-16] GRAFFITI CARD · seg 16 · over the real wall (EVIDENCE S3-16A), kinetic Urdu overlay
- **Show 3 real-style graffiti with Roman-Urdu translation appearing one by one:**
  1. `"C · IVLIVM · POLYBIVM"` → `"Polybius ko vote do"` (election notice — real Pompeii name)
  2. `"HIC FVI"` → `"Ma yahan tha."` (the universal I-was-here)
  3. a love line → `"...ne yahan pyaar likha."` (keep generic; no fabricated names)
- **Foot:** `2000 saal — insan kabhi nahi badla.`
- **Motion:** kinetic type, one translation line at a time.

### [C-22] CALENDAR CARD · seg 22 · open-loop #2, parchment calendar
- **Sequence:** `24 AUG ?` flashes → **glitch** → `24 OCT ?` → a stamp slams: `AKHIR MA` (jawab baad ma).
- **Then:** timestamp chip flips to `12:00 PM`.
- **Motion:** glitch/RGB-split transition between the two dates; stamp impact.

---

## SECTION 4

### [C-24] SCALE CARD · seg 24 · parchment infographic (vertical)
- **Compare two heights, bars growing upward:**
  - `JAHAAZ ✈  ~10 km` (small plane icon at the 10 km line)
  - `ERUPTION COLUMN  33 km` (ash column towering to 33)
- **Caption:** `Jahan se jahaaz urta ha, us se ~3 guna upar.`
- **Motion:** tilt-up as the 33 km column grows past the 10 km plane line; number counters tick up.

### [C-25] MAP + PLINY QUOTE · seg 25 · map + fading quote
- **Map:** `MISENUM` ↔ `VESUVIUS` across the bay; draw a `~30 km` distance line.
- **Quote (fades in, serif for gravity):**
  `"Badal ki shakal cheer ke darakht jaisi thi —`
  `lamba tana, upar ja kar phailti hui shakhain."`
- **Attrib (small):** `— Pliny, 17 saal · Misenum`
- **Motion:** distance line draws; quote fades in line-by-line.

### [C-28] DECISION CARD · seg 28 · full-screen over the frozen family (28A)
- **Text (big, centered, pompeii-red):** `BHAAGO … ya CHHUPO?`
- **Motion:** hard appear on the freeze, hold (no drift). The question that decides everything.

---

## SECTION 5

### [C-33] QUOTE CARD · seg 33 · Pliny the Elder
- **Latin (Playfair):** `FORTES FORTUNA IUVAT`
- **Urdu (under):** `"Qismat bahadur ka sath hoti ha."`
- **Attrib:** `— Pliny (Roman navy admiral)`
- **Motion:** Latin appears; Urdu fades beneath; ember accent underline.

### [C-36] PHYSICS CARD · seg 36 · parchment diagram — ⚠ PITCHED tiled roof (NOT flat)
- **Diagram:** a **pitched terracotta-tile roof** with grey pumice piled on it + downward weight arrows.
- **Big label:** `100+ KG / m²`
- **Caption:** `Har square meter par 100 kilo se zyada wazan — chhatain gir gayin.`
- **Motion:** pumice piles on the roof, weight arrows grow, a beam cracks. (Fact-fix: roofs were pitched-tiled,
  not flat — see [[storyboard]] S5 fact-check.)

### [C-37] PYROCLASTIC CARD · seg 37 · parchment definition, ember accent
- **Text:**
  `PYROCLASTIC FLOW`
  `= aag + gas + raakh`
  `· ~500 °C`
  `· 100+ km/h`
  `· bhaagna namumkin`
- **Motion:** lines appear one by one; ember-orange glow builds behind the type.

### [C-38] MAP CARD · seg 38 · first surges hit Herculaneum
- **Map:** the mountain; a surge arrow sweeps to `HERCULANEUM` (far side) FIRST, then toward `POMPEII`.
- **Label:** `Pehla nishana: HERCULANEUM.`
- **Motion:** glowing surge arrow sweeps down the flank to the coast.

---

## SECTION 7

### [C-49] LOOP-RESOLVE CARD · seg 49 · sets up the cast reveal
- **Text:** `Wo mashhoor "laashain"… asal ma laashain nahi hain.`
- **Motion:** type-in; holds, then dissolves into C-50.

### [C-50] FIORELLI METHOD CARD · seg 50 · parchment, 4-step diagram
- **Header:** `FIORELLI METHOD — 1863`
- **Steps (icons + Urdu, reveal in sequence):**
  1. `Khokhla gap dhoondo` (raakh ma jism ka khali sancha)
  2. `Plaster daalo`
  3. `Set hona do`
  4. `Raakh hatao → shakl saamne`
- **Motion:** each step reveals with a small icon; a plaster-into-void micro-animation on step 2–4.

---

## SECTION 8

### [C-57] DNA REVEAL CARD · seg 57 · PATTERN INTERRUPT #3 — full-screen, silence, no music
- **Text (single fact, Von Restorff):**
  `DNA: MARD.`
  `KOI RISHTA NAHI.`
- **Sub (small, after a beat):** `"Maa or bacha" — 100 saal ka sach ulat gaya.`
- **Motion:** hard cut to full-screen; the two lines snap in; hold in dead silence.

### [C-59] CHECKLIST CARD · seg 59 · "August?" fails — pairs with EV-59A carbonised figs
- **Header:** `24 AUGUST?`
- **Items (each gets a red ✗ one by one):**
  - `Khazaan ka phal — anaar, akhrot, anjeer  ✗` (August ma nahi hota)
  - `Garam ooni kapre  ✗`
- **Conclusion:** `→ ya to garmi nahi… ya August nahi.`
- **Motion:** items list; red ✗ stamps each; arrow to conclusion.

### [C-60] DATE-STAMP CARD · seg 60 · decode the charcoal inscription (pairs with 60A, creator-sourced)
- **Decode:** `XVI K NOV`  →  `= 17 OCTOBER, 79 AD`
- **Stamp (slams in, pompeii-red):** `17 OCT 79 ✓`
- **Caption:** `Charcoal jaldi mit jata ha → usi saal likha gaya. Case closed — August nahi, October.`
- **Motion:** Latin decodes to the date; stamp impact.

---

## SECTION 9 — IBRAH (⚠ reverent; verse wording MUST be tafsir-verified before record)

> **GUARDRAIL:** parchment cards only, kinetic Urdu line-by-line, slow + a beat of silence. NEVER assert
> "Allah destroyed Pompeii" as fact. Pompeii is NOT claimed to be the Quranic city (C-61d says so). The
> Roman-Urdu verse renderings below are **faithful DRAFTS — confirm exact wording against an authoritative
> Urdu translation/tafsir (e.g. Kanz-ul-Iman, Bayan-ul-Quran, Tafheem-ul-Quran) before finalizing.**

### [C-61b] QURAN CARD 1 · seg 61b · "travel & see the end of past nations"
- **Ref (small, Latin+Arabic numerals):** `Ar-Rum 30:9  ·  Muhammad 47:10`
- **Urdu (kinetic, line by line — DRAFT, verify):**
  `"Kya ya zameen ma chal phir kar nahi dekhte`
  `ka un se pehle walon ka anjaam kya hua?`
  `Wo in se zyada taaqatwar thay, zyada aabaad —`
  `phir jab hadd paar ki, to mit gaye.`
  `Allah ne un par zulm nahi kiya —`
  `unho ne khud apni jaanon par zulm kiya."`
- **Motion:** slow line-by-line; beat of silence at the end.

### [C-61c] QURAN CARD 2 · seg 61c · Qaum-e-Lut — overturned + rained with stones
- **Ref:** `Al-Ankabut 29:34–35  ·  Hud 11:82`
- **Urdu (DRAFT, verify):**
  `"Hum is basti walon par aasman se azaab nazil karne wale hain… (29:34)`
  `phir hum ne us basti ko ulat diya — upar ka hissa neeche —`
  `or un par paki hui mitti ke patthar barsaye. (11:82)`
  `Or hum ne us ma aql walon ke liye ek khuli nishani chhod di. (29:35)"`
- **Imagery:** the overturned-ruin still (S9-61c) — NOT a depiction of the event. Beat of silence.

### [C-61d] SODOMA GOMORA CARD · seg 61d · the history→reflection bridge
- **Center (reproduce the charcoal — the real one is illegible), aged charcoal script:**
  `SODOMA`
  `GOMORA`
- **Small below:** `— House IX.1.26, Pompeii. Kisi zinda bachne wale ne isi raakh ma likha tha.`
- **Bridge line:** `Us waqt bhi ek insan ne yahan wohi nishani dekhi… jo aaj hum dekh rahe hain.`
- **⚠ Do NOT** state Pompeii is the Quranic city; dating is debated → "kisi ne likha tha." Reverent, slow.

---

## SECTION 10

### [C-65] OUTRO CARD · seg 65 · standing outro rule
- **Elements:** channel logo + big `SUBSCRIBE` (standing outro rule) → next-video teaser frame.
- **Teaser text:** `Agli video — ek or subah, ek or shehar.`
- **Motion:** logo + subscribe button appear; teaser still fades in (belongs to the next video — placeholder now).

---

## Build order & notes
- Cards are HyperFrames motion-graphic layers (no image gen, no sourcing). Reuse the parchment/red/ink tokens.
- The timestamp chip is ONE persistent component whose value changes — build it once, drive the value.
- English stays only in refs/labels the script keeps English (dates, verse refs, Latin quotes, SUBSCRIBE);
  all narration-facing text is Roman-Urdu per creator rule.
- **Before record:** verify C-61b/C-61c verse wording vs tafsir (script fact-table items 21–22); confirm
  C-36 draws a pitched (not flat) roof; C-60 pairs with the real charcoal photo (creator-sourced 60A).
