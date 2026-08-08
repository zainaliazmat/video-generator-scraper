---
summary: Milestone note for japanese-money-methods — the channel's first LONG tier (≈11 min, 92 scenes, 8 chapters per cut), first chapter-wise production at full scale, first vidIQ-optimised packaging, and first AI-enhanced thumbnails. Both cuts LIVE 2026-08-06. The durable lessons are §3: a thumbnail is downstream of its title; a thumbnail must name its SUBJECT, not just its stake; and the premise correction binds packaging as hard as it binds the script.
updated: 2026-08-06
source: run.json, the 2026-08-01→06 session logs, the two publish packs, and the vidIQ pass of 2026-08-06
---

# Japanese Money Methods — «Japan Ke 3 Tarike» / «3 Japanese Money Rules»

The four-method video (Mottainai · Hara Hachi Bu · Kakeibo · Taru wo Shiru),
built as the channel's **first LONG tier**: ~11 minutes, 92 scenes, 8 shipped
YouTube chapters per cut, produced chapter-by-chapter and folded back into one
master by `tools/cut_assemble.py`.

| | hi — @cashguruguides | en — @moneymavens101 |
|---|---|---|
| runtime | **10:59.2** (659.200 s, 19,775 f @ 30) | **10:26.8** (626.800 s, 18,803 f @ 30) |
| voice | ElevenLabs "Harsh" | ElevenLabs "Brian" |
| loudness | −14.0 LUFS / −1.7 dBTP | −14.20 LUFS / −1.69 dBTP |
| captions | 134 cues | 180 cues |

## 1 · The premise correction — the spine of the whole run

`fin-facts` J7 killed the topic's own popular framing. Horioka (NBER WP 33181,
§3 / §9–10) states culture, tradition and national character are **not** a major
determinant of Japan's saving rate, and the National-Accounts household rate was
**about 1 %** in 2024. So the video does **not** claim Japanese people are great
savers or that culture explains saving, and carries **no** Japan-vs-India or
Japan-vs-US saving-rate comparison.

What replaced it: **Japan's own two published numbers for one year** — 37.8 %
(FIES, salaried-worker households) against ~1 % (SNA, everybody), a gap Horioka
calls "more than 30 times as high". The four methods stay, as behavioural tools.

**This correction outlived the script and bound the packaging twice**, which is
the reusable part:
- The **title** could not use it — `37 percent` has no finance corpus in the US
  (body fat, the dating rule) and `japan savings rate` returns NO SUGGESTIONS.
- The **thumbnail** could not use it either. When the creator asked for a tile
  saying "three methods in Japanese culture **that make them wealthy**", that
  was the refuted premise arriving through the art department. It was declined
  and the tile ships naming the methods as Japanese (true) and offering them for
  adoption (true), claiming nothing about Japanese wealth.

→ **A premise correction is not a script-stage decision. Write it into
`run.json` and re-read it at every packaging stage**, because the pressure to
restore the catchy version is strongest furthest from the research.

## 2 · Firsts

- **First LONG tier** on either channel, and the **2nd consecutive** long-form
  per-line-chapter cut. ⚠️ A third in a row makes *length* stop varying too;
  with `architecture_lock: blockframe-9` removing layout as an anti-sameness
  lever, only tier, transitions, the SFX kit and the music bed remain. Worth a
  deliberate choice at the next `run.json`, not a discovery at the next pack.
- **First chapter-wise production at full scale** — 16 chapter projects
  (8 per cut), each built, audited by `fin-editor`, reviewed by `fin-ceo`,
  re-rendered, then assembled. See [[../../knowledge/design-chapter-archetypes]]
  and [[../../knowledge/design-chapter-sound]].
- **First vidIQ-optimised packaging** — §3.
- **First AI-enhanced thumbnails** — [[../../knowledge/design-thumbnail-ai-enhance]].

## 3 · The packaging lessons — the durable part of this run

### 3a · vidIQ changed the titles, the tags and the descriptions

Full evidence in [[youtube-metadata-hi]] / [[youtube-metadata-en]]; the method
is now [[../../knowledge/vidiq-mcp]] + `.claude/skills/vidiq/`.

| | before | after |
|---|---|---|
| hi title CTR | 84 | **94** |
| en title CTR | 80 | **84** |

The gain was one pattern both times: **replace the list-plus-number with the
verdict question.** "Here are three methods and a number" → "which one survives
your month?"

Two failures the scores alone would have caused, both avoided by requiring
score **and** demand to agree:
- vidIQ's best English titles (85) all led with `37.8 %` — a string with no US
  search demand. **A high CTR on zero impressions is nothing.**
- `japanese money habits` has 4× the volume of the phrase in the title and
  scored **77 against an 80 baseline**. Volume like that belongs in the tags,
  where it costs no click-through.

**The tag lesson generalises past this video:** autocomplete proves a phrase is
*typed*; it cannot say *how often*, and it cannot surface a phrase nobody
thought to seed. All 20 Hindi tags sat inside `kakeibo` — **3,507 searches/month
in India**, a term whose top-5 markets do not include India — while
`personal finance` (303,719), `money management` (51,885), `financial planning`
(31,514) and `budgeting` (25,064) went unreached. Both sources, every time.

### 3b · A thumbnail is downstream of its title

The thumbnail was rebuilt **four times in one day**, and only the first rebuild
was about the artwork:

| | what it said | why it died |
|---|---|---|
| (a) | `37.8% YA 1%` / `DONO SACH` | fine — until the title changed |
| (c) | `₹30,000` / `TIKEGA KAUN?` | matched the new title, but contained **no Japanese word and no Japanese object** |
| (d) | `MOTTAINAI · KAKEIBO · HARA HACHI BU` / `JAPAN KE 3 TARIKE` / `₹30,000 PE BHI` | shipped |
| AI | (d), enhanced | shipped |

**Two rules out of it.** First: *when the title changes, the thumbnail is
already wrong* — a tile selling the 37.8 % paradox beside a title asking which
method survives your salary offers two different videos in one browse row.
Second, and the one the creator had to say out loud: **a thumbnail must name its
SUBJECT, not just its stake.** `₹30,000` + a question is a money video; nothing
in it says *Japanese*. Naming the three methods fixed it and cost nothing — those
words are also the lane's real search terms.

⚠️ It also cost a rule: the tile ships **four text blocks**, over the creator's
2026-07-29 "max 3 elements" discipline. That rule was written to stop a build
with a 36-character sub-line; a tile that must explain itself needs the fourth
block. No body copy, no sub-line — that half still holds.

### 3c · The colour system finally used green

`--fund` green means *what the viewer does*. Every prior thumbnail on both
channels left it unused because nothing on a thumbnail was an action. Naming the
salary the methods must survive (`₹30,000 PE BHI` / `EVEN ON $4,000 A MONTH`) is
the viewer's side of it — so green applies, and it buys a third contrast tier
the two-colour builds never had.

## 4 · Still owed

- 🔴 **The AI-enhanced thumbnail PNGs are not in this repo.** They were produced
  in the creator's Google Flow session and are the files actually on YouTube.
  `i.ytimg.com` 404s because the uploads are scheduled, so they could not be
  recovered here. `src/thumbs/` holds the **pre-enhance renders**; the
  **enhance prompts that reproduce them** are in both publish packs. Drop
  `thumbnail-{hi,en}-ai.png` into `src/thumbs/` when convenient.
- **Thumbnail CTR scores.** `vidiq_score_thumbnail` needs the video in vidIQ's
  index; `get_videos_by_ids` returned empty for both ids and a score call errored
  on 2026-08-06 — the index lags a scheduled upload. Re-run both once they
  resolve. This is the third time this measurement has been deferred and it is
  the only unmeasured thing about these tiles.
- **Analytics after 28 days** (≈2026-09-03): `channel_analytics`
  `report='audience_retention'` + `traffic_sources`. ⚠️ **Only @moneymavens101
  is authorized in vidIQ**, so the `-en` cut can be measured and the `-hi` cut
  cannot until the creator connects @cashguruguides.
- 🔴 **@moneymavens101's live YouTube About text is the Hindi channel's copy** —
  "Paisa School", "real rupee examples", "every video is 2–3 minutes" on the
  US/$ channel, against an 10:26 dollar-denominated upload. A YouTube Studio
  edit, not a packaging one.
- **`-hi` s17 still carries a balanced brass scale on screen** under
  `ONE GOVERNMENT. ONE YEAR. / 30 TIMES` — the documented `image_relevance`
  failure. `-en` was fixed in the 08-06 image round; `-hi` never got the
  equivalent. One frame of 92, in an approved cut; a re-render is the creator's
  call.

## 5 · Where the reusable knowledge went

Nothing durable from this run lives only here:

- [[../../knowledge/design-chapter-archetypes]] — the four scene layouts, the
  plate, the ground-temperature arc.
- [[../../knowledge/design-chapter-sound]] — the cue-density fix, creator-approved
  levels.
- [[../../knowledge/design-thumbnail-ai-enhance]] — the AI pass, new here.
- [[../../knowledge/evidence-discipline]] §9 (judge a master from the encode) and
  **§10 (a fixHint is a guess — bisect the diff first)**, both written from this
  run.
- [[../../knowledge/vidiq-mcp]] + `.claude/skills/vidiq/SKILL.md` — the whole
  measurement layer.

## Published + archived (2026-08-06)

**State: LIVE on YouTube · source archived · studio dir deleted.**

| Cut | Channel | URL | Thumbnail |
|---|---|---|---|
| en | @moneymavens101 | https://youtu.be/Uu4CT_4FLVI | `src/thumbs/thumbnail-en.png` |
| hi | @cashguruguides | https://youtu.be/xJO11XfIjhQ | `src/thumbs/thumbnail-hi.png` |

**Source: `src/`** — composition, meta/package JSON, `gen_vo_*.sh`, the VO lines
(`assets/voice/*.txt`), the image prompts (`assets/img/*.src`), stock CREDITS and the
thumbnail PNGs. `studio/videos/japanese-money-methods*` is **deleted** per the finished-video rule
(`vault/CLAUDE.md`). **Re-render is reproducible, not free** — the scene photos and VO
mp3s are gone, so a rebuild re-pays image gens + ElevenLabs off the archived prompts
and lines. `gen_vo_*.sh` still `cd`s into the deleted studio path — repoint it first.

Still owed: analytics after 28 days.
