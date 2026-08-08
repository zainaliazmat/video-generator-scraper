---
summary: en ch3 attempt 3 — verification-only pass over the two files attempt 2 replaced before it was killed. Both s27 and s31 are KEPT with measured evidence: the composed-median method was first re-validated against the 14 untouched scenes (reproduces fin-build's table to ≤0.5 pt), then applied. s31 moves 7.1 → 70.6 median (16th → 10th), p10 0.0 → 43.2 (#3), step-in −52.8 → +8.5, so the chapter's largest figure is off the floor; s27 moves 25.4 → 97.0 (#4), p10 0.0 → 82.2 (#2). The orchestrator's flat-charcoal prediction is measured FALSE (white under the locked grade lands at ~160, not charcoal) — the real risk was emptiness, and both pass the sound-off gate at full resolution. Payoff clause re-scored: s34 still passes all four. Zero files changed on disk; one bgpos recommendation and one relocated-floor escalation handed to fin-build.
updated: 2026-08-09
source: fin-assets attempt 3, chapter 3, en cut — verification of attempt 2's unlogged replacements; measured against studio/videos/passive-income-number-en-ch3/build.mjs §5 table + tools/scaffold/assets/blockframe.css `.bg`.
stage: fin-assets, cut en, chapter 3, attempt 3
---

# fin-assets — passive-income-number / en / chapter 3 / attempt 3

**Accepted 2 · rejected 0 · re-fetched 0 · dropped 0. FILES CHANGED ON DISK: NONE.**
This was a verification attempt, not a sourcing attempt. Attempt 2 replaced `s27.jpg`
and `s31.jpg` and was killed before it verified or logged either. Both files are
**KEPT**. Nothing under `studio/` was written, moved, renamed or deleted by this
attempt; `manifest.json`, `CREDITS.txt`, the `.src` notes and
`superseded-invariant-r1/` are exactly as attempt 2 left them and were audited, not
edited. The only file this attempt writes is this log.

`python3 tools/pipeline_check.py check assets --slug passive-income-number --cut en --chapter 3`
→ **PASS assets-en** (with `--chapter 3`, so the licence assertion reaches
`assets-ch3/final/`, not ch1's manifest).

---

## 0. The method was validated BEFORE it was trusted

The brief says source-side predictions have been wrong about the composed frame
five times on this run. So the measurement was not re-invented — it was
**reproduced against fin-build's own §5 table on the fourteen scenes nobody
touched**, and only then pointed at s27/s31.

Composed = cover-crop the source to 16:9 with the scene's `background-position`,
take the central 86.2% that `inset:-8%` actually shows, then the locked grade
(`grayscale(.32)` is chroma-only and does not move luma; `brightness(.62)` then
`contrast(1.05)`), then percentiles on Rec.601 luma.

| scene | fin-build median | mine | Δ |
|---|---|---|---|
| s24 | 37.7 | 36.6 | −1.1 |
| s25 | 92.0 | 93.9 | +1.9 |
| s28 | 95.7 | 95.8 | +0.1 |
| s30 | 59.8 | 62.1 | +2.3 |
| s34 | 128.1 | 128.3 | +0.2 |
| s35 | 139.2 | 137.8 | −1.4 |
| s37 | 21.6 | 20.5 | −1.1 |
| **superseded s27** | **25.5** | **25.4** | **−0.1** |
| **superseded s31** | **7.1** | **7.2** | **+0.1** |

Both outgoing files reproduce to a tenth of a point. **The instrument agrees with
the one it is being compared against**, which is the only reason the new numbers
below are worth anything. Largest disagreement anywhere is 2.3 (s30).

## 1. THE ORCHESTRATOR'S PREDICTION WAS WRONG, AND THE RIGHT WORRY IS A DIFFERENT ONE

The brief's warning: *"a white-dominant subject can only become FLAT CHARCOAL."*
Measured, that is false under this grade. Pure white 255 through
`brightness(.62) contrast(1.05)` lands at

```
((255·0.62/255 − 0.5)·1.05 + 0.5)·255 = 159.6
```

**mid-grey, not charcoal.** The locked grade darkens midtones and lifts nothing;
it cannot crush a white subject to black because `brightness()` is a multiply, so
a bright source stays the brightest thing available. Both replacements measured
BRIGHTER than everything they replaced, in the direction the brief wanted.

The real failure mode for a white-dominant subject here is the *other* one the
brief names in the same paragraph — **"a blank field is both even and empty."**
That is the test both files were actually put through, and it is why neither was
accepted on its percentiles.

## 2. s27 — **KEPT**

`car door handle on a white car body in bright daylight close up@pexels`
· 1880×1253 · Pexels, Jan van der Wolf · md5 `0826d350…`

| | outgoing (chrome on dark sedan) | **incoming** |
|---|---|---|
| composed median | 25.4 — **14th of 16** | **97.0 — 4th of 16** |
| p10 | 0.0 — 14th | **82.2 — 2nd** |
| p90 − p50 | 50.9 | 26.1 |
| median step-in (from s26 92.6) | **−67.0** | **+4.4** |

**Sound-off gate: PASS.** Type covered, the frame is a car door handle in its
recess on a car's flank, with the door shut-line running down the left. A viewer
names "a car" without a word of help. Line 3.4 is rung two, the car corpus — the
thing the line names is the thing in frame.

**Full-resolution read (and a 1.5× crop-zoom on the handle, which is the only
place text could hide):** no badge, no keyhole brand, no wordmark, and **no
legible reflection** — the specular highlights on the handle are cloud, not
signage or a photographer. Clean. This is the slot that killed a `PEUGEOT` fob at
full resolution on attempt 1; the same read was run and found nothing.

**Why it is kept despite being the chapter's emptiest photograph.** ~75% of the
composed frame is a smooth panel gradient. That is a real observation and it is
declared, not argued away — but it is not a defect *here*: s27 is `arch: "b"`,
`ctr: true`, and carries a rate `.sub`, a `$332,950` mega, a foot and the 156px
§9a measure bar. §10 routes the heaviest type frames to the quietest photograph,
and the type-band luminance is **median 96.0 with p10 88.5** — flatter and
therefore *more* legible than s28, which already passed 14/14 AA at band median
110.5. There is no AA risk from this swap, by precedent rather than by hope.

### ⚠ One recommendation for fin-build: `bgpos: "center top"` on s27

The default centre crop **clips the top of the handle recess against the frame
edge**, which is the one thing that weakens the sound-off read. The source is
1880×1253 against a 16:9 box, so `cover` leaves 196px of vertical slack and
spending it upward brings the whole handle in with clearance. Measured all three:

| bgpos | median | p10 | p90 − p50 | handle |
|---|---|---|---|---|
| center (current) | 97.0 | 82.2 | 26.1 | clipped at the top edge |
| **center top** | **97.8** | **82.9** | **38.1** | **fully in frame** |
| center bottom | 95.9 | 80.8 | 12.4 | clipped harder |

`center top` is free on median and p10 and buys +12.0 of spread; `center bottom`
is the wrong knob and collapses spread to 12.4, which is the "even and empty"
direction. **Verified by looking, not only by measuring** — both crops were
rendered graded at composed size and read side by side. The handle then sits
upper-right and the `.centred` stack owns frame centre, so they do not collide;
`ken: "o"` opens tight and pulls back, so the object *arrives* rather than
leaving. fin-build owns the knob — this is a measured recommendation, not an edit.

## 3. s31 — **KEPT**

`sunlit entryway of an american home white front door brass knob@pexels`
· 1880×1253 · Pexels, Joel Zar · md5 `03d4b215…`

| clause | outgoing | **incoming** | target |
|---|---|---|---|
| composed median | 7.1 — **LAST of 16** | **70.6 — 10th of 16** | mid-pack |
| p10 | 0.0 — 15th | **43.2 — 3rd of 16** | a real p10 |
| p90 − p50 | 95.0 (widest, a specular knob) | 59.9 (a sunlit window + a shadowed hall) | real structure |
| median step-in (from s30 62.1) | **−52.8** | **+8.5** | non-negative |

**The brief's target is met on every clause it named.** The chapter's largest
figure, `$656,650`, is no longer on the chapter's luminance floor, no longer
arrives on a −52.8 step, and no longer has a crushed-black p10.

**Sound-off gate: PASS, and strongly.** An ornate brass escutcheon with a cut-glass
knob on a white panelled door, standing open onto a sunlit front entry with a
mullioned storm door beyond. Type covered, it says *a way into a home* — which is
rung three, housing. It is also unambiguously **American vernacular**: a crystal
knob on a Victorian brass backplate is an early-20th-century US house fitting, and
the storm door with a stained-glass sidelight behind it is a US entryway. Place,
era and currency are all right.

**Full-resolution read + a crop-zoom on the background door, window and
stained-glass panel** — the only regions that could carry text: **no house number,
no signage, no brand, no maker's mark.** The background is bokeh at f-wide; the
storm-door glass resolves to nothing readable. (Attempt 1 killed this slot's first
pick for `R.M.I.` engraved on a key bow; the same read was run here.)

**The spread is earned, not an artefact.** 59.9 comes from a genuinely sunlit
window on the right third against a shadowed hall — two real regions, not a
specular pinprick, which is exactly the distinction p90 was retired for. Type-band
median 76.6 / p90 122.4 sits inside the range already proven AA (s25's band p90 is
127.8 and passed).

**Margins, honestly.** Median 70.6 clears its neighbours by 8.5 (s30) and 6.7
(s38), so **rank #10 is safe**. Its p10 of 43.2 leads s25's 40.6 by only **2.6 —
under the ~3-point threshold, so #3 vs #4 on p10 is UNSAFE and may flip on the
encode.** Nothing depends on which it is; both are off the floor.

## 4. The chapter re-scored, and the payoff clause re-checked

The thing most likely to have been broken by attempt 2 is the payoff designation,
because s27 leapt into the top of the p10 ranking. Re-scored on the live files:

| clause | s34 | verdict |
|---|---|---|
| sound-off pass | a contract page with a pen | **PASS** |
| top quartile on median (top 4) | 128.3, **#2** | **PASS** |
| #1 or #2 on p10 | 92.1, **#1** | **PASS** |
| non-negative median step-in | s33 57.9 → 128.3 = **+70.4** | **PASS** |

All four still hold. **But the headroom has shrunk and that is declared:** s34's
p10 lead was +61.6 over the field in fin-build's table; it is now **+9.9 over s27**.
s34 is still the brightest-floored frame in the chapter, but no longer by a mile.

Full ranking on the live files (median | p10 | p90−p50 | step-in):

```
s24 36.6 (15) | 11.3 (12) | 45.4 |  —      s32 91.2  (8) | 29.3 (6) | 35.2 | +20.6
s25 93.9  (6) | 40.6  (4) | 36.4 | +57.3   s33 57.9 (13) |  0.0 (16)| 32.7 | −33.3
s26 92.6  (7) | 19.5  (9) | 32.6 |  −1.3   s34 128.3 (2) | 92.1 (1) |  7.8 | +70.4
s27 97.0  (4) | 82.2  (2) | 26.1 |  +4.4   s35 137.8 (1) |  2.3 (15)|  6.8 |  +9.5
s28 95.8  (5) | 28.9  (7) | 25.3 |  −1.2   s36 50.3 (14) |  7.2 (14)| 62.7 | −87.5
s29 58.6 (12) | 15.0 (10) | 77.0 | −37.2   s37 20.5 (16) |  7.5 (13)|103.8 | −29.8
s30 62.1 (11) | 12.6 (11) | 16.3 |  +3.5   s38 77.3  (9) | 28.8 (8) | 28.4 | +56.8
s31 70.6 (10) | 43.2  (3) | 59.9 |  +8.5   s39 102.3 (3) | 30.8 (5) | 13.1 | +25.0
```

### ⚠ ESCALATION — fixing s31 RELOCATED the floor onto s37, it did not abolish it

**The chapter's luminance floor is now s37: median 20.5, p10 7.5, arriving on
−29.8, carrying line 3.14** — the second of the two fine-print quotation beats.
This is not damage from attempt 2: s37 was already 15th at 21.6 in fin-build's own
table and only became last because s31 climbed past it. But the invariant's first
clause is about **whoever is on the floor**, so the clause has moved to a new
tenant and the gate should rule on it with the number in hand rather than discover
it in the draft. It is a quotation scene, not a figure scene, so the argumentative
weight is lower than s31's — but 3.14 is one of the two beats the whole fine-print
run exists to deliver, and s37 also carries the chapter's widest spread (103.8),
which is a lit page against a dark room. **Not actioned: outside this attempt's
brief, which was s27 and s31.** One re-fetch fixes it if the gate wants it.

⚠ Second thing to declare: **s26 / s27 / s28 now sit at 92.6 / 97.0 / 95.8** — a
4.4-point band across three consecutive scenes, with the s27↔s28 margin at 1.2 and
s26↔s27 at 4.4. Both are inside the ~3-point unsafe window, so **their relative
order is not predictable from the source and fin-render must settle it from the
encode.** As a shape this is defensible (rung two is a substantive beat and the
mailbox/lot frames flanking it are bright by design), but three near-equal frames
in a row is the ch1 CEO's sameness complaint inverted, and it should be looked at
on the mp4 rather than taken on trust.

## 5. Standing rules, each actually run

- **md5 across ALL of `studio/`, sibling chapters swept** — 126 jpgs hashed
  (`_cand/`, `node_modules/`, `snapshots/` excluded). **Neither s27 nor s31
  collides with anything.** The 15 duplicate-hash groups that exist are all
  pre-existing archive/mirror pairs on the **hi** cut (`style-a/` ↔ `final/`,
  `superseded-r*/` ↔ `final/`, `retired-attempt6/`, `originals/`) plus two
  render `SHEET.jpg` ↔ `SHEET-chN.jpg` pairs. No en-ch3 file appears in any of
  them.
- **Source-URL collisions** — both Pexels URLs appear in exactly one CREDITS.txt
  in the whole of `studio/` (this chapter's). No en-ch3 URL is duplicated
  anywhere on either cut.
- **Cross-pool tell** — neither credit row reads "by Pixabay" on a Pexels result.
  (Note s34's legitimately does; that is a pre-existing ch3 row, untouched.)
- **Attribution** — `CREDITS.txt` has **16 rows, 16 distinct keys, zero missing**;
  manifest keys, files on disk and credit keys are the same 16-element set, with
  no stale row left behind by the s27/s31 re-key. Nothing was hand-placed by this
  attempt, so nothing could have moved pixels away from its credit.
- **≥1600 px** — both 1880 px wide.
- **US market** — no non-US signage, no foreign-language text, no currency in
  either frame.

## 6. What fin-build must do before this chapter is drafted

`index.html` and `build.mjs` are **18:23, older than both photographs** — the
composition has never been rendered against the files it now points at. This
attempt changed no code and no timing, so a plain regenerate is enough, but it is
not optional:

1. Regenerate from `build.mjs` and re-run `npm run check` — the two frames whose
   backgrounds changed most in the chapter are both AA-relevant. Precedent says
   they pass (band medians 96.0 and 76.6, against s28's already-passing 110.5),
   but "says" is not "checked".
2. Consider `bgpos: "center top"` on s27 (§2 above) — measured, +12.0 spread, free
   on median and p10, and it uncrops the object.
3. Re-shoot the max-density snapshot for **s27 and s31 only**; the other fourteen
   are byte-identical to the ones already looked at.
4. `#s27-rate` / `#s31-rate` and the 156.0px / 307.7px measure bars are untouched
   by this attempt — no numerator or denominator moved.
5. The relocated floor at s37 (§4) is a ruling for the gate, not a build fix.
