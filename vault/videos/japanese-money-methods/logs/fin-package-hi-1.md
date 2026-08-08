# fin-package — japanese-money-methods · cut hi · attempt 1

**Date:** 2026-08-01 · **Tier:** long · **Status:** ok

## What was produced

| Artifact | Path |
|---|---|
| Publish pack | `vault/videos/japanese-money-methods/youtube-metadata-hi.md` |
| Thumbnail (the deliverable) | `studio/videos/japanese-money-methods-thumbs/thumbnail-hi.png` |
| Thumbnail source | `studio/videos/japanese-money-methods-thumbs/index.html` §v2 |
| This log | `vault/videos/japanese-money-methods/logs/fin-package-hi-1.md` |

Recommended title: **`Japan Ke 3 Paise Wale Tarike — Kakeibo, Mottainai Aur 37.8% Ka Sach`**

## Inputs read

`vault/CLAUDE.md` · `tools/format.json` · `run.json` (incl. `premise_correction`) ·
`script-hi.md` (title options, chapter table, §Fact trace) · `storyboard-hi.md` §1 (colour
semantics) · `facts-staging.md` §§0–4 · `vault/knowledge/video-studies/japanese-money-methods.md`
(§Packaging + §Conclusions) · the milestone notes for good-debt-vs-bad-debt, credit-history,
first-lakh-first-thousand (thumbnail + sameness history) · `first-lakh-first-thousand/youtube-metadata-hi.md`
(house style) · `studio/videos/japanese-money-methods-hi/index.html` (scene `data-start`, `.foot`
citations, watermark) · `assets/img/CREDITS.txt` · `library.db`.

## Thumbnail — ONE build, v2 style

- New HyperFrames project `studio/videos/japanese-money-methods-thumbs/` (one section, `#v2`).
  Assets copied from the hi cut: `s17.jpg` (+ its `.src` and CREDITS row), `grain.png`, the
  vendored font, gsap.
- Composition: muted chip `JAPAN 2024` · amber `37.8% YA 1%` · red mega `30 GUNA FARQ` · red
  rule · ink sub `ek hi sarkar. ek hi saal. do aankde.` Left-aligned over the video's OWN
  scene photo for line 2.7 (the brass balance scale that carries `ONE GOVERNMENT. ONE YEAR. /
  30 TIMES` in the render), re-graded (`grayscale .58 / brightness .86 / contrast 1.14`) and
  re-framed (`background-size: 152%; background-position: 88% 46%`).
- `npm run check`: **0 lint · 0 runtime · 0 layout (9 samples) · 0 motion · 20/20 WCAG AA.**
- Export: `npx hyperframes snapshot --at 0.5 --no-end -o snapshots` → copied to `thumbnail-hi.png`
  (1280×720 RGB).
- **Legibility assert (measured, not estimated):** downscaled to 320×180, the red mega spans
  x 16→264 = **249 px = 77.8 %** of frame width (threshold ≥40 %). Amber line 53.8 %.
- **≤12 chars / ≤2 lines:** 11 and 12. Pass.
- **Numeral discipline:** 37.8 · 1 · 30 · 2024 — all four are on screen in the render and traced
  in `script-hi.md` §Fact trace (2.3/2.5, 2.6, 2.7, and the s13/s15/s16 foots).
- **Currency firewall:** zero `$` in the thumbs project; zero in the hi render.

### Two decisions worth keeping

1. **37.8% is AMBER, not red.** The generic v2 recipe says "red hook text", but this video's own
   colour semantics (`storyboard-hi` §1) reserve red for *the drain and the lie about the drain*
   and explicitly forbid rendering 37.8% in red — *"it is real … argues against the script."*
   Resolved by giving red the **gap** (`30 GUNA FARQ`, which storyboard §1 does put in red at
   2.7/2.10) and amber the **two figures**. Focal red + accent amber; the v2 family is intact and
   the thumbnail does not contradict the video.
2. **Rounded chip, not the squared swiss module.** The previous pack (first-lakh) used squared
   `.swiss-band` grammar because that cut rendered in swiss-band. This cut renders in
   `blockframe-9`, so the thumbnail reverts to `border-radius: 999px`. The rule is *follow the
   cut*, not *follow the previous thumbnail*.

### Sameness (last 3 built for @cashguruguides)

good-debt v2 (`208 MAHINE`/`17 SAAL`, credit card) · credit-history v2 (`EXTRA BYAJ`/`₹4.5 LAKH`,
blueprint) · first-lakh v2 (`PEHLA LAKH`/`20 MAHINE`, coin macro — built, not uploaded).
Family match is intended (creator rule). **Nearest relative named: credit-history v2.** Not a
near-duplicate — first percentage-pair thumbnail on the channel, first *relationship* in the mega
slot rather than a quantity, first non-money object plate, and the accent line carries its own
contrasting figure in amber.

## Publish pack

- **Chapter timestamps are real**, read from the render's own `data-start` values (not the script's
  estimates, which were 2–5 s off): 0:00 · 0:55 · 2:09 · 3:42 · 5:17 · 6:50 · 8:35 · 9:59.
  Eight chapters, first at 0:00, smallest gap 73.5 s. Nobody in the study packet ships chapters.
- **Description** carries the on-screen source citations verbatim from the render's `.foot`
  elements (Statistics Bureau FIES 2024 Table I-2-2, Horioka NBER WP 33181 pp.2–3/7 and §§3/9–10,
  BOJ Flow of Funds Chart 2, Fujin no Tomo Sha + National Diet Library, AMFI, DEA PPF notification),
  plus the ILLUSTRATIVE label on the computed 90/3 split and the "four categories are a later
  addition" caveat. Education-not-advice disclaimer included.
- **20 tags, 470 chars** (limit 500). Every string is quoted verbatim from a completion returned by
  today's pull. Nothing invented.
- **Premise firewall verified programmatically:** the description block contains no `$`, no
  "india", no "bharat", and no saving-rate comparison. The retired title question is not restored.

### Autocomplete evidence — 25 seeds, `tools/autocomplete.py`, gl=in hl=hi, 2026-08-01

**The find:** `kakeibo method in hindi` is a live completion — rank 4 of the bare `kakeibo` seed,
rank 3 of `kakeibo method`, the **only** completion of `kakeibo hindi`, and a terminal node
(returns itself). `kakeibo method` returns **six language requests in its top ten** (urdu, hindi,
tagalog, tamil, bengali, malayalam): this lane's viewers search for the method in their own
language, which is what this cut is. Recommended title #1 carries `Kakeibo`.

**Four honest empties, all recorded in the pack:**
- `japanese money methods` → NO SUGGESTIONS (the slug's own phrase is not a query)
- `japanese money secrets hindi` → NO SUGGESTIONS (the format twin's own title tail does not autocomplete)
- `kakeibo budget hindi` → NO SUGGESTIONS, while `kakeibo method in hindi` returns cleanly — the demand word is **method**, not **budget**
- `37 percent japan` → NO SUGGESTIONS — the hook number has no search demand, which is precisely why it belongs on the thumbnail and not in the title's lead

**Two wrong-corpus traps found and avoided:**
- `japan bachat` → `japan bachata`, `fukuoka japan bachata` (**the dance**). Not used anywhere.
- `mottainai` → nine of ten completions are a children's picture book, a board game or a flea
  market. Kept as a tag and in the title's *supporting* position only; a Mottainai-led title
  lands in the wrong index.
- Every "Japan + paise" Hindi seed (`japan paise kaise bachate hain`, `japan ke log paise`,
  `japani tarike paise`, `japan ke tarike`) returns currency/immigration strings. That is why the
  titles carry `Kakeibo` or the numbers rather than "Japan ke tarike" alone.

### Competitor scoreboard

`library.db` (2,970 rows) has **7** rows in this lane — thin, and recorded as thin. The format twin
(`Story of Success`, 73,772 views @ 4,690 subs) is the only on-topic Hindi competitor. Its title
grammar (countable promise + envy question + language tag) is kept **minus the envy question**,
because that question is the retired premise. Named as a deliberate CTR trade, on the record.

## Gate 2

- **Altered-content toggle: "No"**, with the reasoning written into the pack: synthetic narration
  (ElevenLabs Harsh) but **no realistic synthetic media presented as real** — all 94 image files are
  licensed Pexels/Pixabay stock, no AI scene, no synthetic person, no real likeness or voice
  imitated. **Therefore no on-screen disclosure is required and none appears in the render**; the
  pack states where the toggle lives if the creator elects to disclose anyway (YouTube Studio →
  Video details → Altered content), and that no re-render would be needed.
- **Persona rule clean** — faceless, no name/face/credentials, second person throughout; PPF and the
  AMFI SIP minimum appear as price evidence only, with the on-screen foots saying so verbatim.
- **Channel watermark present on every frame** via `#root.cut-hi::after` → `assets/img/wm-hi.png`.
- **Sameness: NOT flagged.** Against the last five @cashguruguides cuts this changes tier (LONG,
  a channel first), runtime (10:59 vs a ~3-min band), scene count (92 vs 9), chapter model and
  structure. ⚠️ **Named for the next run:** the architecture name returns to `blockframe-9` because
  of `architecture_lock` — a decision, not drift, but it means layout is permanently off the table
  as an anti-sameness lever, and this is the **2nd consecutive long-form per-line-chapter cut**. A
  third would take *length* off the table too, leaving only transitions / SFX / music. That should
  be a deliberate choice in the next `run.json`, not a discovery at the next pack.

## Nothing blocked

No gate failed. One thing owed downstream, unchanged from the last two packs: **no CTR/analytics has
ever been read back from a live upload**, so every packaging claim on this channel remains
unvalidated by outcome.
