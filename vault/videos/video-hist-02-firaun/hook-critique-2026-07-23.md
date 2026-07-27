---
summary: Retention critique of the ch1-draft cold-open (68s) for «فرعون کا انجام», reviewed frame-by-frame against the script + storyboard. Writing is strong; the cut goes flat in its back half (59% static cards). Ranked fixes + decisions taken (storyboard segs 04–05 rewritten, P05c/P05d goat stills added).
updated: 2026-07-23
source: reviewed studio/videos/firaun-ka-anjaam/renders/ch1-draft.mp4 (68s, 1fps frame pull) vs [[storyboard]] Part 1 + [[script-v2-nastaliq-lines]] segs 01–05 + [[DESIGN]]
---

# Hook critique — ch1-draft (فرعون کا انجام)

**Verdict:** the *writing* of the hook is strong — well-built open loops, and the goat line is a
killer. The *cut betrays the script*: ~40 of the 68 seconds (**0:28→1:08, 59%**) sit on three
motionless text cards on flat cream/black — including the two best hooks. Root cause is mechanical,
not creative: [build.py](../../../studio/videos/firaun-ka-anjaam/build.py) `is_card` path (~L286)
sets `ref="C:"+key` and **drops the background image**, so a card *replaces* imagery instead of
overlaying it. The storyboard always intended imagery behind every card; the engine can't currently
do it.

## Timecode map of the rendered cut (68s)
| t | shot | VO seg |
|---|------|--------|
| 0:00–0:05 | museum hall wide (near-static, ~5s hold) | 01.1 |
| 0:05–0:13 | hands → red hair → rim-lit head (the reveal ladder) | 02.x |
| 0:13–0:15 | lit case w/ visitor silhouettes | 03.1 |
| 0:15–0:20 | CT scanner | 03.2 |
| 0:20–0:28 | B&W Le Bourget 1976 honour guard | 03.3–03.5 |
| **0:28–0:46** | **parchment card «تیرا بدن…نشانی» — flat cream, ~18s** | 04.1–04.4 |
| **0:46–0:58** | **«معجزہ نہیں۔ اُس سے اگلی صبح۔» — flat cream, ~12s** | 05.1–05.3 |
| **0:58–1:08** | **black card 2026/1881/3000 numbers — the GOAT line, ~10s** | 05.4–05.6 |

## What works (keep)
- The **reveal ladder** (hands→hair→head); withholding the face is correct *and* tantalising.
- **«ایک لاش کے لیے… سنو، ایک لاش کے لیے»** — best-written beat, real rhetorical torque.
- The **France red-carpet fact** (0:20) — a bizarre *true* detail; B&W footage sells it.
- The **subversion** — "not the night the sea split, the morning after" — a differentiated promise.

## Findings, ranked by retention impact
1. **Static-card back half (0:28→1:08) — biggest leak.** 3 naked cards, no motion behind them.
   → **Cards must overlay a moving still, never replace it.** No card holds >4s without the bg changing.
2. **The goat — the single best open loop — is invisible.** "3000 سال بعد ایک بکری کی وجہ سے دوبارہ کھل گئی"
   plays over a numbers card. → new **P05c** (goat at the cliff shaft) under the line; **tease it in the
   first 3s as a cold-open bookend.**
3. **Slow first 5s.** The corpse (the hook object) isn't seen until 0:05. → **open on the payload**
   (red hair / France) in second 1; trim the seg-01 hall hold ~5s → ~2s.
4. **Full-paragraph cards in Nastaliq, held 18s, duplicating the VO.** → **keyword punch** (2–4
   VO-synced words: «تیرا **بدن**»… «**نشانی**»), let the voice carry the sentence.
5. **Uniform Ken-Burns; scripted texture missing.** The storyboard's hard-cut-into-1976 jolt,
   sub-bass on «3000», shutter-click, drone-enters-on-the-question — none are in the cut. Vary cut
   rhythm even before full sound design.
6. **Idea↔image inversion.** All imagery is spent 0:00–0:28, all ideas 0:28–1:08 — backwards.
   **Interleave:** face under the Quran question, sea under "the morning after", goat under the goat.

## Decisions taken (2026-07-23)
- [[storyboard]] Part-1 rows **04 & 05 rewritten** to keyword-cards-over-imagery + interleave + goat;
  revision note added under the Part-1 table.
- **P05c** (goat at Deir el-Bahari cliff shaft) and **P05d** (the black shaft mouth) added to
  [image-prompts.txt](image-prompts.txt) — the one new hook generation. Fact base: the Deir
  el-Bahari royal cache (DB320, Luxor west bank), found by the Abd el-Rassul family, the goat legend,
  brought to light **1881**; Ramesses II was among its mummies. Timeless/pre-modern framing so it
  reads 1881.
- **Engine change DONE** (fix #1): [build.py](../../../studio/videos/firaun-ka-anjaam/build.py) now
  routes the hook card beats through the proven `.ov` overlay path (not the image-dropping `C:`
  branch) via a new `CARD_BG` map — each card rides a moving still. Wiring in ch1:
  - 02.3–02.4 + 04.1–04.2 → **P02d** (CLEAR museum mummy face — creator 2026-07-23, replaces the withheld
    P02c silhouette; resolves the "the face can still be recognized" dissonance) · 04.3–04.4 → **P03d**
    (France 1976). Firaun is not a revered figure; the real preserved museum mummy = the Quranic "sign", kept museum-respectful.
  - 05.1–05.3 → **P37c** (dark aftermath water = "the morning after"; P36 kept unspoiled) under the معجزہ نہیں card
  - 05.4–05.5 → **P05c goat** · 05.6 → **P05d shaft mouth** (cut, blooms into seg 06 dawn); no card,
    the era ribbon does the 3000→1881 strip. **Goat stills generated + wired 2026-07-23.**
  If a bg still is ungenerated it holds the previous real still + logs it (fallback, now unused here).
  Rebuild: `python3 build.py --chapter 1`. Still TODO (creator knobs): the cold-open bookend tease
  (fix #2), trimming the seg-01 hall hold ~5s→~2s (fix #3), and keyword-only cards (fix #4).

## Flicker fix (2026-07-23) — same still across lines = ONE continuous shot
Symptom (creator): held images "flicker" — a dip + scale jump each time the same still carries into
the next line. Cause: one-scene-per-line means a held image is re-rendered as a fresh scene and
**cross-dissolved with a second copy of itself** at a mismatched zoom → luminance dip + scale pop.
Fix in [build.py](../../../studio/videos/firaun-ka-anjaam/build.py):
- Consecutive scenes on the **same still** are grouped; between them the transition is an **invisible
  CUT** (not a dissolve), and the group runs **one continuous linear zoom** (`zc`, ease none) with the
  scale matched at every cut — so a run reads as a single smooth in/out. Groups alternate zoom
  in/out; the card overlay stays fixed (only the photo scales), so text stays legible.
- Only a **real image change** dissolves, and the dissolve is now **dip-free** (`xd`: incoming opaque
  photo fades in *over* the outgoing held at full opacity — no black shows through the mid-point).
- The intentional hard-cut jolt into the 1976 footage (03.3) is preserved.
Verified: brightness is monotonic across former flicker points (0.142→0.142, 0.225→0.225; no dip).

## Durable production principles (apply to every video)
1. **A text card is an overlay, never a background.** Kinetic Urdu always rides a moving still; no card
   holds >~4s without the frame changing; on-screen text is a VO-synced keyword punch, not the full
   spoken sentence. Marry each biggest *idea* to your best *image* — never spend all the imagery first
   and all the ideas last.
2. **The same still across consecutive lines is ONE shot, not N re-reads.** Cut invisibly between them
   and run a single continuous zoom; never cross-dissolve an image with itself (it flickers). Reserve
   dissolves for real image changes, and keep them dip-free.
→ fold both into [[DESIGN]].
