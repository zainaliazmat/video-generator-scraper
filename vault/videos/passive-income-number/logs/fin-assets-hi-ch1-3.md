---
summary: Finishes the chapter-1 rework that a session limit interrupted mid-flight. Two items were owed and both are closed — the s3 Lottie now carries ONE ₹ glyph (the 06:13 source had two, and the glyph itself was drawn wrong enough to read as ₣), and s7's empty level balance is replaced by a loaded pan with its counterweight in frame. Records a rejection that only a full-resolution read could catch: a promoted candidate Pexels titles "powder on a platform balance".
updated: 2026-08-07
source: this run — vault/videos/passive-income-number/logs/editor-hi-ch1-1.md findings 3 and 7, run.json paused.ch1_rework_state, storyboard-hi.md §7/§8/§9
stage: fin-assets, cut hi, chapter 1, attempt 3
---

# fin-assets — passive-income-number · hi · chapter 1 · attempt 3

**Scope.** Finishing only. s2, s4, s5, s6 were replaced by attempt 2 and were not
touched, not re-read and not re-fetched. Chapter 2's s8–s19 untouched. Two items
were owed by `run.json paused.ch1_rework_state`; both are done.

## Item 1 — the s3 Lottie blocker (editor finding 3)

**The 06:13 source was wrong on both counts, and the second fault was the worse one.**

1. It drew **two** ₹ glyphs — one in the app-mark square, one at the head of the
   amount bar. The interrupted agent's stated plan was app-mark only.
2. **The glyph did not read as ₹.** The reduction drew the bowl as a left stem plus
   a horizontal *floor*, which put a THIRD full-width bar under the two real ones.
   Rendered at the 46 px it actually ships at, it reads as **₣**. A wrong currency
   mark on a currency video is worse than no mark — it is the demonetised-₹500
   failure in another alphabet.

Fixed by tracing Noto Sans Bold's own U+20B9 at 184 px and rebuilding the bowl as
a cubic that closes back to the left. Four candidate skeletons were rendered side
by side against the font at 46 px, 184 px and 30 px before one was taken; the
chosen one cannot be confused with $ / € / £ / ¥ / ₣ at any of those sizes.

Also removed the second glyph and restored the amount bar to its original
`AMT_X=-204, AMT_W=196`, flush-left with the title — the pre-glyph geometry, which
the 04:51 build confirms.

**The declared open loop survives.** The digits are still bars, the amount is still
unreadable, the phone is still face-down. The only change is that the card now says
*money* rather than *a notification arrived* (storyboard §8 intact).

**Proof, not assertion.** The built file was loaded through a `<script src>` exactly
as `index.html` loads it, against the project's own `assets/js/lottie.min.js`:

- `window.L_phone_notify_credit` — **defined**
- **75 frames @ 30 fps = 2.50 s** — unchanged, so `playLottie(s3art, S.s3 + 0.30, 2.50)`
  in `index.html` needs no edit and the asset still completes at 12.30 s, before the
  12.33 s dissolve
- glyph rendered and read at 1:1 over the real graded `s3.jpg`, with the real
  `blockframe.css` + `chapter-design.css`

The grade is on `.bg` only, and `.v-lstage` is not inside `.art`, so neither
`brightness(.62)` nor the `.has-photo .art {opacity:.30}` rule touches the card —
the glyph renders at full strength.

Tinted with **`#98a2b3` (`--muted`)**, the same accent as the reviewed 04:51 build:
one variable changed, not two. `assets/lottie/` (the shared library) was written only
through the toolchain. `used_in` is 2 cuts — no over-reuse.

⚠ `passive-income-number-hi/assets/lottie/` and `…-hi-ch1/assets/lottie/` are the
**same inodes** (hardlinked), so the tint landed in both projects in one write. Worth
knowing before someone "syncs" them and silently forks the pair.

## Item 2 — s7 (editor finding 7)

Original: both pans empty and level, brass weights outside the delivered frame.

**Four sheets, 24 cells, one promoted-and-rejected, one accepted.** Every cell was
judged on the sound-off test for line 1.7 («हर सीढ़ी पर वो शर्त भी साथ रहेगी») —
a figure travels *with* its condition, so the frame needs two things together.

| query | outcome |
|---|---|
| `balance scale with brass weights on a wooden table@pexels` | all 6 fail |
| `vintage weighing scale with brass weights on dark background@pexels` | 1 promoted, rejected at full res; 1 accepted after re-pick, rejected on aspect |
| `balance scale with a folded paper document in one pan@pexels` | all 6 fail — pulls the law-office pool |
| same query `#7` | **accepted, cell 4** |

**The rejection worth recording.** A cell that read at grid size as a grey heap on a
balance pan beside an open weights box promoted to a full-resolution frame Pexels
itself titles *"powder on a platform balance"* — a heap of white powder with a
figure in a coat looming behind it. Sound-off, on a money channel, under **THE
CONDITION**, that reads as a drug scene. Invisible on the contact sheet; obvious in
two seconds at full size. This is the full-resolution rule earning its place again.

**A second rejection the trap list does not yet name: ASPECT.** The re-pick after it
was a genuinely fine photograph — a cast-iron balance, one pan loaded, dark
painterly ground — at **4200×3300 (1.27:1)**. `.bg` is `cover` with `inset:-8%`, so a
1.27:1 original loses ~40% of its height into a 16:9 frame; graded, the scale had
vanished and the frame said nothing. s1–s6 are all 1.5:1 and crop gently. **A
candidate's aspect ratio is a promote-time check, not a taste call** — `_cand/<slot>.json`
carries `w`/`h` for every candidate, so it costs one read, and paging the same good
query with `#7` returned six cells all at 1.5:1.

**Accepted:** a brass hanging balance pan, loaded, its bell-shaped counterweight on
its cord in frame at the left, on dark wood. 1880×1253, 1.5:1, low-key warm original
against a dark ground per the standing grade rule. No people, no faces, no text, no
brand mark, no currency. Read at full resolution *and* rendered graded with its own
type stack before acceptance — the pan and its pale contents are the brightest thing
in frame and hold up under `brightness(.62)`.

**No per-scene `filter:` override set** — none is needed and the one-per-video budget
stays unspent.

Other cells rejected across the four sheets: a portrait photograph (a face) · a
`HANSON … 25 Pounds` dial and a `水晶度磅秤 / 2476-0441` dial (readable brand marks,
and imperial/foreign units) · a `YBARRA` box · white doctor's beam scales and a
digital kitchen scale with a legible LCD (high-key, and they re-break the grade the
way s2/s4/s5 did) · a lawyer at a desk and a "Balance Sheet" magnifier pun · a macro
of paper page edges, which is the exact stack-of-paper frame that killed s5 in
attempt 1 · the hanging pan of dried mushrooms shot against pantry jars, dropped
because it echoes s5's jars inside the same 7-scene chapter.

## Counts

| | |
|---|---|
| Accepted | 1 photograph (s7) + 1 Lottie rebuilt |
| Rejected | 23 cells at sheet size, **2 after promotion at full resolution** |
| Dropped | nothing — no slot lost its background |
| API calls | **4 Pexels searches**, 24 previews, 3 full-size fetches. 0 Pixabay, 0 Commons, 0 LottieFiles (the Lottie is in-house, regenerated from `assets/lottie/src/`) |

## Verified before returning

- 20 shipped images across ch1 + ch2 → **20 distinct md5s**, zero collisions
- s7 = 1880 px wide, above the ≥1600 px rule for its 6.599 s `ken` push-in
- all 7 ch1 slots: on disk ✓ `.src` sidecar ✓ CREDITS row ✓ named in the manifest ✓
- both manifests (`assets-ch1/final/` and the cut's `assets/img/`) carry the query
  that actually produced the file, so they cannot contradict the `.src`
- CREDITS gained the s3 Lottie line. `assets/lottie/index.json` already records it as
  in-house with nothing to attribute, so only the name is copied — one home per fact

## Still owed to the tools (unchanged, already escalated in attempt 1)

`pipeline_check check assets --slug … --cut hi` is still hard-wired to
`studio/videos/<slug>-<cut>/assets/img/` (`check_assets`), which holds no images on
the chapter-by-chapter flow. It reports all 78 slots missing and **its licence
assertion still never reaches a single chapter-scoped image** — the check whose
comment says it cannot go stale is blind for the entire current pipeline. Ran the
chapter-scoped equivalent by hand instead (the table above). This is the second run
in a row that this fault has cost a manual audit.

## Writes

- `assets/lottie/src/phone-notify-credit.py` — corrected `rupee()` geometry, one glyph
- `assets/lottie/phone-notify-credit.json` — regenerated (library, via its generator)
- `studio/videos/passive-income-number-hi{,-ch1}/assets/lottie/phone_notify_credit.js`
  — re-tinted (one write; the two paths are the same inode)
- `studio/videos/passive-income-number-hi-ch1/assets-ch1/final/` — `s7.jpg`,
  `s7.jpg.src`, `CREDITS.txt`, `manifest.json`
- `studio/videos/passive-income-number-hi/assets/img/manifest.json` — s7 query synced
- `_cand/` sheets left in place; throwaway, not in the manifest
