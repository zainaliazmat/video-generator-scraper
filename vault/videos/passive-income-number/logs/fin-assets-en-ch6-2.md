# fin-assets · passive-income-number · en · chapter 6 · attempt 2

STATUS: ok — single-slot re-fetch of **s71 only**. Twelve other slots untouched (no
re-pick, no re-key, no candidate rebuild). `studio/videos/passive-income-number-en-ch5/`
never opened.

## Ran

1. Read `vault/CLAUDE.md`, `tools/format/fin-assets.json` → `assets` + `scene`,
   `tools/packs/fin-assets.md` (both BOXes). Did **not** open
   `vault/knowledge/stock-photo-sourcing.md` — no OPENED-BODY owed.
2. Read the blocker itself before touching anything: `review-en-ch6-1.md` finding 2,
   plus the live `s71-foot` string and the `<!-- -->` storyboard note in
   `studio/videos/passive-income-number-en-ch6/index.html:89-97`, so the acceptance
   question was set against the **caption**, not against the noun in the query.
3. Read the rejected `s71.jpg` at full resolution, and `s70.jpg` at full resolution —
   the two frames the replacement has to be different from.
4. Two contact sheets, `--only s71 --candidates 6`, one vision pass each. 6/6 cells
   returned on both (counted, not assumed).
5. `--pick "s71=2" --force` → full-res promote. Full-resolution Read of the promoted file.
6. Cross-project md5 dedupe (the `find` form). Chapter sheet rebuilt and Read.
   `pipeline_check check assets --chapter 6`.

## Failed

**Sheet 1 — `new hardcover book with a blank dust jacket lying face down on a desk@pexels`
— 0 of 6 usable.** The pool answers "book" with two things and nothing else:

| cell | what | rejected because |
|---|---|---|
| 1 | open antique volume + stack of leather spines | **the exact defect being re-fetched** — browned pages, worn boards |
| 2 | white notebook on a teal notebook, distressed wood | blank notebook, not a published book; twins `s81` (closed journal on wood) |
| 3 | two blank white book mock-ups on white seamless | product mock-up, no subject, no falloff — emptiness, not a photograph |
| 4 | stack of antique books, deckled edges | same defect as cell 1 |
| 5 | small dark notebook on kraft paper, top-down | twins `s81`; subject is ~8% of frame |
| 6 | macro of a book edge with **yellowed deckled page block** | the foxing tell in close-up — the purest form of the defect |

Root cause, recorded because it is the reusable part: `book` + `hardcover` + `dust jacket`
are **age-blind tokens**. Both pools return vintage props for them, because vintage props
are what book stock shoots are made of. `new` and `modern` are adjectives the search does
not weigh. The token that actually filtered was a **modern-only physical object** placed
in the frame — the same move as naming a denomination instead of saying "coins".

**Sheet 2 — `hardcover book with coloured sticky note tabs marking pages on a desk@pexels`
— 1 of 6 usable.** Neon plastic index flags cannot appear in a 19th-century frame, so the
whole antique family fell out of the result set in one edit.

| cell | what | verdict |
|---|---|---|
| 1 | open textbook on warm wood, yellow sticky + highlighter | **reject — twins `s70`**: same warm-wood ground, same open-page macro, same yellow highlight. Would have replaced one defect with a repetition finding |
| 2 | fanned page block hanging edge-on, neon flags, sage bokeh | **ACCEPT** |
| 3 | hands holding a tabbed book, people out of focus behind | reject — people/faces on a scene that carries a 112px figure |
| 4 | hand placing an orange flag on a charted printed sheet | reject — paper-document register twins `s70`; a small dark label in frame reads as a possible mark |
| 5 | handwritten notebook, glasses, laptop, tab strip, top-down | reject — twins `s78` (handwritten arithmetic) and drags a laptop in |
| 6 | blank black notebook on marble with a sticky pad | reject — blank-notebook flatlay, twins `s81` |

## Evidence

**The caption test, run explicitly** (the thing that failed at attempt 1):

- foot, verbatim from `index.html:97` — `Bengen's "Universal SAFEMAX", A Richer
  Retirement, Wiley, August 2025 — a wider asset mix, roughly 400 historical start
  dates, worst case still October 1968`
- figure — `4.7%`, `.targetc` amber, `pop` at scene +2.17
- **old s71** — hand-bound blue cloth volume, split text block, browned deckled leaves,
  grey studio sweep. Asserts *19th century*. Contradicts `August 2025` in the same frame.
- **new s71** — bright white page block, no yellowing anywhere, **four neon plastic index
  flags (orange · cyan · yellow · magenta)**. Plastic index flags are a present-day
  object; there is no era in which this frame could be an antique. It reads *a book that
  has been gone through and marked up* — which is what "he revised his own number
  upward" looks like, so the frame now argues **with** the caption rather than against it.

**Full-resolution read of the promoted file** (this is the pass a thumbnail cannot do):

- No legible title, figure, agency name, seal, letterhead or logo anywhere in frame.
  Storyboard §10 is satisfied the way the note intended — by the pose, not by a crop.
- The only ink is (a) illegible handwritten cursive on the magenta and orange flags and
  (b) two out-of-focus handwritten strokes on a page edge at upper right. Zero readable
  words. No institution is impersonated and no brand mark exists — the two failure modes
  ch6 already rejected at this gate (a real charity's financial statement, Turkish pharma
  branding) are both absent.
- No people, no hands, no face.
- No currency of any kind in frame — the currency trap cannot fire here.

**Repetition, on the rebuilt chapter sheet — 13/13 cells rendered, none dropped:**

| pair | separated on |
|---|---|
| s71 vs **s70** (the one review told us to KEEP) | ground **cool sage bokeh vs warm oak**; axis **vertical hanging block vs horizontal layered spread**; content **zero legible text vs ~40 words of body prose**; framing **edge-on vs flat macro**. Four independent axes — not a twin |
| s71 vs **s72** | s72 promoted as a warm amber **globe**, spherical, dense cartographic type. No relation |
| s71 vs **s78** | s78 is a flat top-down cream/pink ruled ledger dense with handwriting; s71 is edge-on, textless, cool. Distinct |
| s71 vs **s81** | s81 is a *closed* flat white notebook on dark wood, warm; s71 is an *open* page block in air, cool |
| s75/s76 | printed by the tool as `s75 (HOLD crop of s76)` — correct per `storyboard-en.md` §6b, not raised |

**Measured / verified:**

- `1880x1252`, `158,543 b` — matches the other eleven fetched slots at 1880 wide
  (`identify`), clears `assets.min_width_px` 1600 and `min_image_bytes` 10240.
- `pipeline_check check assets --slug passive-income-number --cut en --chapter 6` →
  **`PASS assets-en`**, which is the assertion of `min_source_yhigh` ≥ 110 (white page
  block, so highlights are not in doubt) and of one attribution row per rendered image.
- Cross-project dedupe, the `find` form, over **303** images in `studio/videos` +
  `vault/videos`: **empty output — no collision.** New hash
  `3d0de69de2702126be8d8275610dd587`. Checked against ch6's other 11 and ch5's 16 by
  construction, since the walk covers both trees.
- `CREDITS.txt` — **13 non-empty rows for 13 files, one row per file**, no orphan licence
  line. s71's row re-keyed in place by the tool to
  `https://www.pexels.com/photo/white-papers-in-close-up-shot-12585551/ · by BOOM 💥
  Photography · Pexels License`. (No Commons slot in this chapter, so today's
  `write_credit` newline fix was not exercised here.)
- `s71.jpg.src` rewritten by the tool to the new query — sidecar and `manifest.json`
  agree.

## Changed

- `studio/videos/passive-income-number-en-ch6/assets-ch6/final/manifest.json` — s71 query
  only: `hardback book lying face down and open spine up on a wooden table@pexels` →
  `hardcover book with coloured sticky note tabs marking pages on a desk@pexels`.
- `…/final/s71.jpg` — replaced (+ `s71.jpg.src`, + its `CREDITS.txt` row).
- `…/final/IMAGES-ch6.jpg` / `IMAGES-ch6.json` — rebuilt.
- `…/final/_cand/s71.*` — throwaway sheets, left in place per protocol.
- Nothing else. s69, s70, s72–s81 byte-unchanged; ch5 untouched.

## Owed

1. **fin-build:** the `<!-- -->` note above `#s71` still describes *"A hardback lying
   face-down and open, spine up"*. The object is now an open page block seen edge-on with
   index flags; the §10 justification it gives ("title not legible … satisfied by the pose
   rather than by a crop") still holds verbatim. Prose only — no timeline, no anchor, no
   duration touched, `data-duration 7.598` and the `+2.17` anchor stand.
2. **fin-review, one number to re-measure:** old s71 sat at YAVG **45.225**, mid-chapter.
   The replacement is materially brighter (white page block on a mid ground), so expect
   s71 to move **up** the chapter's luma ranking, plausibly near s78's 55.973 ceiling.
   That direction is safe under `outlier_limb_is_subordinate_to_the_invariant` — it cannot
   strand the {s79, s75} floor tie and cannot pull the payoff (s77) or CTA (s81) down —
   but the amber `4.7%` now sits on a lighter local field than it did, so the figure's
   contrast ratio is the one thing worth re-sampling on the encode.
3. **fin-review, cosmetic:** s71 is the one cool-cast frame inside the s70→s72 warm run.
   The scene's own `--tint:rgba(245,158,11,.12)` plus the locked `grayscale(.32)` should
   absorb most of it; flagging it so it is a measurement, not a surprise.
4. Review finding 1 (s77's five reference rungs invisible) is **not** an assets defect and
   was deliberately not touched — it is fin-build's `.flf` fill change.
