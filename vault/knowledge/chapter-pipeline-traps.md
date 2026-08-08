---
summary: The tooling trap ledger for chapter-wise production — every entry cost real time on a real cut, most of them on japanese-money-methods (2026-08-04/06). Renderer timeouts, Lottie sizing, stale sheet files, symlinked assets, lying stock metadata. Rescued from that video's HANDOVER.md when it shipped, because a session file dies with its session and these recur.
updated: 2026-08-06
source: japanese-money-methods HANDOVER §6/§7 (sessions of 2026-08-04/05/06), plus the tool fixes made from them
---

# Chapter-pipeline traps

Companion to [[design-chapter-archetypes]] (what a chapter should look like) and
[[design-chapter-sound]] (what it should sound like). This note is **what breaks
while building one**, and how it presents. Rules of evidence are in
[[evidence-discipline]]; these are mechanics.

## Rendering

- **`hyperframes render` on a full-length cut is killed by the ffmpeg encode
  timeout.** Capture takes ~26 min; the encode then runs ALONE at ~0.17× — about
  72 min — against a default ceiling of 41.8 min. It dies around frame 11,000 of
  18,800, writes **no mp4**, and buries the reason thousands of log lines deep.
  Always set `FFMPEG_ENCODE_TIMEOUT_MS=10800000` (`cut_assemble.py` prints it).
- **`hyperframes render` in a long backgrounded chain dies silently** — twice in
  one round, mid-chapter, leaving a `.hf-transaction-*` and a `work-*` dir and no
  error. Render one chapter per foreground call, check the mp4 mtime, and clean
  those two dirs before retrying.
- **A wait-loop that watches only for the output file cannot see a dead render.**
  It waits forever on a process that already exited. Break on the process, not
  the artifact — this cost three idle hours on top of the 90-minute render it was
  watching. (Same rule, generalised, in [[evidence-discipline]].)
- **`hyperframes check` cannot pass a full master** — `Navigation timeout of
  10000 ms exceeded`, because 92 scenes with ~100 images do not paint inside the
  tool's 10 s navigation budget and `--timeout` does not raise it. Run `check` on
  **chapter projects**, judge the master from the **encode**.
- **Frame quantisation:** every chapter's frame count rounds UP independently, so
  a concatenated preview runs a few frames long. `tools/chapter_preview.py`
  prints the table and says so; the single full-length render cannot drift.

## Layout and animation

- **A `<p>` under `position: absolute` keeps its UA margin.** That is the whole
  `.measure-lab` defect — every other text class in `blockframe.css` sets
  `margin: 0` explicitly and this one was missed. Invisible in source, obvious on
  the encode. Adding an absolutely-positioned text component: set `margin: 0` and
  pin `line-height`.
- **lottie-web sizes its `<svg>` from the container's box at `loadAnimation()`
  time.** A stage with `inset: -8%` and no explicit width/height renders the
  artwork at **native size, pinned top-left** — one chapter's phone came out
  640×420 in the corner of an empty navy frame, and `hyperframes check` passed.
  Give a Lottie stage pixel dimensions and force `svg { width: 100% !important }`.
- **Lottie has two silent-blank modes** (absolute-composition-time seeking, and
  `discover()` sweeping in every registered animation). Always verify from the
  encoded mp4 — see [[design-icons-emoji-lottie]].
- **`data-framings` is checked for its SUM, not for existence.** A scene can
  declare two framings, hold one photo for the whole span, and pass.
  `chapter_project.py` refuses a spec whose framings do not sum to the shipped
  duration, but the cosmetic-framing hole is still open. **Not fixed.**

## Files that lie about which file they are

- **`frames_sheet.py` picks the FIRST `SHEET*.json` it finds, sorted.** A stale
  `SHEET-ch3.json` beats a fresh `SHEET.json` (`-` sorts before `.`), so the
  cross-chapter sheet silently rebuilds from the previous round's samples. Delete
  old per-chapter sheets before rebuilding FRAMES. Cost one wrong 100-vs-96 frame
  count.
- **`assets/` inside a hand-built chapter can be a SYMLINK to the shipped cut's
  `assets/`.** Three paths, one file: writing a chapter-local `audio.json` there
  would overwrite the full-cut list without a word. **Check whether a project's
  `assets/` is a link before writing into it.**
- **`tools/archive_cut.py` used to key its plan by destination**, so any studio
  dir whose suffix was not exactly `-hi`/`-en`/`-thumbs` collided and was
  silently dropped — 18 of 22 directories on this very video, while the run
  printed "archived" and exited 0. Fixed 2026-08-06 (dest is the suffix itself,
  unique by construction) with a regression in `--self-check`. The general shape:
  **a dict keyed by a lossy derivation of the input silently discards work.**

## Sourcing

- **The contact sheet is for shortlisting; the full-resolution read is the actual
  check.** Full-res reads in one round killed a legible "Prime Rate + 12.74%"
  card agreement, a Turkish price tag in a `$` cut, Polish and IKEA receipts, and
  a Russian Play Store list. **Every one passed the contact sheet.**
- **A stock provider's own metadata lies about nationality.** Pexels labelled a
  Chinese copybook "Japanese". Read the image, not the caption.
- **A photograph that looks exactly like what it was chosen to look like is the
  one that gets through.** Two wrong images survived a first review round and
  were caught by reading `CREDITS.txt`, not by looking at the frame.
- **The contact sheet is lossy** — `tools/stock/…/_cand/<slot>.jpg` renders only
  a trailing subset when any preview fails; `_cand/<slot>.json` always holds all
  N. **Not fixed.**
- **A `@commons` fetch can return a 5472×3648 / 15.8 MB original.** Chrome
  re-decodes it every frame. Downscale to the cut's long edge (1880 px) before it
  reaches the renderer.
- **`commons.wikimedia.org` does not resolve from this environment.** Use
  `en.wikipedia.org/w/api.php`.
- **Commons attribution is a licence condition, not bookkeeping.** `CREDITS.txt`
  must ship, and the check must assert against **what `index.html` renders** —
  34 images were once on screen with no credit row because the check iterated a
  stale `manifest.json`. See [[evidence-discipline]].

Related: [[design-chapter-archetypes]] · [[design-chapter-sound]] ·
[[evidence-discipline]] · [[design-icons-emoji-lottie]] ·
[[../videos/japanese-money-methods/index]]
