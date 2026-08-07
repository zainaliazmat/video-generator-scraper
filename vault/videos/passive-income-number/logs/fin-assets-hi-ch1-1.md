---
summary: fin-assets for passive-income-number hi cut, CHAPTER 1 only («वो सुबह», the cold open). 7 bg slots needed, 7 on disk, 0 dropped. 1 Lottie reused from the library, no fetch. Records two rejections that only a full-resolution read could catch (a law-office scale with a person and empty pans; foreign silver coins in a balance pan) and two tooling faults found in flight (tint.py emits invalid JS for a hyphenated output name; pipeline_check check_assets has no chapter mode).
updated: 2026-08-07
source: this run — vault/videos/passive-income-number/storyboard-hi.md §7/§8/§9, script-hi.md ch1 cue lines, tools/format.json, vault/knowledge/stock-photo-sourcing.md
stage: fin-assets, cut hi, chapter 1, attempt 1
---

# fin-assets — passive-income-number · hi · chapter 1 · attempt 1

**Scope.** Chapter 1 = VO lines 1.1–1.7 = scenes 1–7 = bg slots `s1.jpg`–`s7.jpg`.
No cut-ins in this chapter (`s11b`/`s32b` are ch2/ch4). `s14.jpg` is a later-chapter
crop of s13's source and was **not** fetched, per the run brief.

**Result: 7 slots needed · 7 on disk · 0 dropped · 0 faked.**

Files: `studio/videos/passive-income-number-hi-ch1/assets-ch1/final/s{1..7}.jpg`
(+ `.src` prompt sidecar each, + `CREDITS.txt`, + chapter `manifest.json`).
Path chosen because `cut_assemble.py` symlinks `assets-ch<N>/` wholesale into the
assembled cut and the archived reference chapter (`japanese-money-methods hi-ch1`)
renders its backgrounds from `url(assets-ch1/final/sN.jpg)`.

## API calls

| Source | Searches | Notes |
|---|---|---|
| **Pexels** | **15** | 7 first-pass sheets + 8 retry sheets. All 7 promoted picks except none — see s7. |
| **Pixabay** | **3** | s2 and s5 pool-change attempts (both failed), s7 pool-change attempt (failed at 1:1). |

Every promoted file came from Pexels: `--pick` returns `dpr=2&w=940` = **1880 px**,
against Pixabay's 1280 px ceiling. Chapter 1 is the cold open and every scene takes a
full-bleed ken, so 1280 px was refused on principle (s7's Pixabay pick was rejected
partly for it).

## What landed

| slot | line | subject | px | mean lum | source |
|---|---|---|---|---|---|
| s1 | 1.1 | twin-bell alarm clock on wood, warm morning light, clock face carries **no maker's mark** | 1880×1253 | 164 | Pexels |
| s2 | 1.2 | single ribbed **cutting-chai glass** of masala chai + ginger | 1880×1253 | 168 | Pexels |
| s3 | 1.3 | phone on dark wood, **screen off and blank**, warm reflected glow | 1880×1253 | **49** | Pexels |
| s4 | 1.4 | one **closed** kraft envelope, squared, bare wooden table, nothing legible | 1733×1300 | 175 | Pexels |
| s5 | 1.5 | tall stack of clipped white documents on a desk, no people, no currency | 1880×1059 | 180 | Pexels |
| s6 | 1.6 | narrow stone steps **rising** between rock faces, empty, POV at the bottom | 1880×1253 | 107 | Pexels |
| s7 | 1.7 | antique two-pan brass balance on a shelf, beam slightly off level | 1880×1253 | 110 | Pexels |

All seven md5s distinct. Cross-project sweep found **no collision** — but note the
ledger is nearly empty by construction: the archive rule deletes every shipped cut's
JPEGs, so only these 7 plus one `video-hist-01-travel` file exist on disk anywhere.
The dedupe check is therefore currently weak evidence, not strong.

### s3 luminance — checked, no override taken

Mean 49/255, the only near-black frame. **No per-scene `filter:` override set**, and the
one-per-video budget stays unspent. Reason: this is not the "near-black texture crushed
flat" case. The frame carries a bright reflected-glow band across the phone glass and the
window bokeh, so under `grayscale(.32) brightness(.62) contrast(1.05)` the subject holds at
~110–130 while the wood falls away — which is exactly what a night scene with a screen glow
should do. Storyboard §9 forbids overrides in this cut and nothing here needs one.

## Rejections — and the two that only 1:1 caught

**Caught at contact-sheet size** (cheap): two chaiwala frames with identifiable faces;
a Samsung wordmark on a phone bezel; an AirPods case; four phone-screen-up frames with
live UI; a `SALTER` scale dial; a `SNOWFLAKE CAKE WHEAT FLOUR` bag; `PHILIP ROTH` and
`Javier Marías` book spines; a stained-glass church rose window answering "tea by a
window"; a scale-of-justice figurine; a suited man holding folders; two roseate
spoonbills answering "electricity bill".

**Caught only at full resolution** — the sheet passed both:

1. **s7, first pick** — the sheet for that query rendered **1 cell of 6** (previews
   failed; reproducible across two runs), so I promoted from `_cand/s7.json` on the
   title `a-balance-scale-on-a-table`. At 1:1 it was a **law office**: an identifiable
   man in a suit at a desk, a banker's lamp, and **both pans empty and level**. Empty
   and level asserts *equal / nothing weighed* against a line whose whole point is that
   a condition travels with every figure — the "contradicting frame is worse than a
   bland one" failure, plus a person in a frame the storyboard restricts to objects.
2. **s7, second pick** (Pixabay, after re-query) — a brass balance with **two foreign
   silver coins in the pan**. Wrong currency on a ₹ cut, on the frame that establishes
   the video's central condition. Invisible on the grid; unmistakable at 1:1. Also
   1280 px, under the bar for a 6.599 s full-bleed zoom (the chapter's longest scene).

Third pick (Pexels, `antique brass weighing scale with brass weights on a table`) is
clean: no people, no currency, no brand, a cast `3kg` capacity mark only, and the beam
sits **slightly off level**, so it does not assert equality.

**Also refused on the currency rule**: a Pixabay sheet for `electricity bill india`
returned a pile of **demonetised pre-2016 ₹500 notes** as cell 2, and a Pexels sheet for
`indian electricity bill` returned a **Polish 100 złoty note on a Polish VAT invoice**
and a **US one-dollar bill**. Both pools were exhausted for that framing.

## The three storyboard briefs that could not be photographed as written

Each was walked down the retry ladder (`#N` → other pool → synonym) before changing the
brief. **Nothing was dropped; all three keep a real photograph**, per the replace-never-drop rule.

| slot | brief asked for | what shipped | why |
|---|---|---|---|
| **s2** | chai glass **on a windowsill**, morning street behind | chai glass, no window | 3 rounds, both pools. Pexels drifted to coffee-and-cookies and street vendors; Pixabay to a church rose window and legible book spines. The chai glass is the load-bearing India signal, the window is not. |
| **s5** | Indian household bills fanned — electricity, grocery slip, rent receipt | neutral stack of clipped white documents | 5 rounds. Both pools answer this with foreign currency and faces (see above). A currency-neutral object beats a wrong-currency one. |
| **s7** | brass balance, **one pan holding a folded paper slip** | brass balance, pans bare, beam off level | the styled paper-slip shot does not exist in either pool; the balance itself carries the beat and the off-level beam avoids asserting "equal". |

### Two consequences later chapters must absorb

- **s77 (7.7) rhymes with the chai GLASS, not the window.** Its brief currently reads
  "window with an empty steel chai glass on the sill at full daylight". Since s2 has no
  window, re-brief s77 as *the same ribbed chai glass, empty, in full daylight* or the
  callback lands on an object the cold open never showed.
- **s25 (3.6) must be visibly different from s7.** s7 is now a bare two-pan brass
  balance. s25's brief ("two brass weights of clearly different mass on a shop balance")
  still works, but chapter 3's asset pass must ensure the weights are actually in frame
  and the surface is a shop counter — otherwise the two frames read as one picture used
  twice, which is the sound-off rule's defect #4.

## Sound-off test, per line

| line | covering the words, the image says | argues? | named thing in frame |
|---|---|---|---|
| 1.1 alarm did not go off | a clock in morning light | no | अलार्म — yes |
| 1.2 tea, the window, one buzz | Indian chai, freshly made | no | चाय — yes (window absent) |
| 1.3 money arrived while you slept | a phone at rest at night, screen dark | no | phone — yes; the *arrival* is the Lottie, which is the only honest way to say it |
| 1.4 you just reached a number | a sealed envelope — contents withheld | no | the open loop — yes |
| 1.5 electricity, ration, rent | a stack of obligations waiting | no | bills, generically |
| 1.6 rung by rung, smallest first | steps rising, viewer at the bottom | no | सीढ़ी — yes, and the POV matches "smallest first" |
| 1.7 every figure ships with its rate | the instrument that weighs a claim | no | the condition — yes |

No image is used twice. No faces. No hands (the chapter has none of the three
hand-permitted slots). No currency of any kind in any of the seven frames — deliberate,
since the cut's first rupee figure is withheld until 6.7.

## Lottie — `phone-notify-credit` on s3 (1.3)

**Library reuse, zero fetches, zero searches.** `assets/lottie/phone-notify-credit.json`
was already in the git-tracked library. Read its `.png` preview before taking it: an
abstract notification banner — no currency symbol drawn in, no brand mark, no legible
text (the copy is bars), authored in `--panel`/`--edge`/`--ink`/`--muted`. Vector only,
**0 embedded bitmaps**.

- **For fin-build: 75 frames @ 30 fps = 2.50 s**, 820×300.
- **Load `assets/lottie/phone_notify_credit.js` → `window.L_phone_notify_credit`.**
- Tinted with **`#98a2b3` (`--muted`)**, not a role colour. `tint_required` is a hard
  constant, but storyboard §8 forbids pushing this asset into a role colour 1.3 has not
  earned. `--muted` is the neutral end of the very ramp the asset was authored on
  (panel → muted → ink), so the tint is near-identity and introduces no role colour.
  Both constraints satisfied without special-casing either.
- `index.json` `used_in` now records **2 cuts** (japanese-money-methods-hi-ch1 s1, this
  one). Two is reuse working as intended, not sameness — flagging it because the tool
  asked me to and because a third would start to be.

## Two tool faults found in flight (I cannot write `tools/` — escalating)

1. **`tools/lottie/tint.py` emits invalid JavaScript for any hyphenated output name.**
   It builds the wrapper identifier from the output basename verbatim, so
   `…/phone-notify-credit.js` was written as `window.L_phone-notify-credit={…}` which
   throws `Invalid left-hand side in assignment`, leaving `window.L_*` undefined —
   i.e. `loadLottie()` renders **a blank scene that passes every check**, the exact
   failure `design-icons-emoji-lottie.md` exists to prevent. Every library name in
   `assets/lottie/` is hyphenated, so this is the default path, not an edge case.
   Worked around by naming the output `phone_notify_credit.js`; the hyphenated path was
   overwritten with a comment so nothing can load it silently.
   **Root-cause fix belongs in `tint.py`**: sanitise `name` with
   `re.sub(r"\W", "_", name)` before the `window.L_` write — one line, and it fixes every
   future caller instead of every future agent remembering.
2. **`pipeline_check check assets` has no chapter mode.** It is hard-wired to
   `studio/videos/<slug>-<cut>/assets/img/` (`check_assets`, line 288), so on the
   chapter-by-chapter flow — which is now the default — it reports all 78 slots missing
   and **its licence assertion never reaches a single chapter-scoped image**. The check
   whose comment says it "cannot go stale" is blind for the entire current pipeline.
   Ran the chapter-scoped equivalent by hand instead: 7 slots, 7 on disk, 7 credit rows,
   7 `.src` sidecars, no orphans, chapter manifest ≡ cut manifest for s1–s7 — all pass.

## Writes

- `studio/videos/passive-income-number-hi-ch1/assets-ch1/final/` — `s{1..7}.jpg`,
  `s{1..7}.jpg.src`, `CREDITS.txt`, `manifest.json` (7 chapter slots).
- `studio/videos/passive-income-number-hi/assets/lottie/phone_notify_credit.js` (loadable
  wrapper) and `phone-notify-credit.js` (a comment, superseded — see fault 1).
- `studio/videos/passive-income-number-hi/assets/img/manifest.json` — s1–s7 queries
  synced to the queries that actually produced the files, so the cut manifest and the
  archived `.src` sidecars do not contradict each other. s8–s78 untouched.
- `assets/lottie/index.json` — `used_in` appended by `tint.py`.
- `_cand/` contact sheets left in place; they are throwaway and not in the manifest.
