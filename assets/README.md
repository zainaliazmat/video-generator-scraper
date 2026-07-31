# assets/ — the shared media library

Git-tracked, **outside `studio/`**, and deliberately so: `studio/` is gitignored
and a cut is deleted from it the moment the video ships (the finished-video rule
in `vault/CLAUDE.md`). Anything that should outlive one video lives here.

The rule, in one line: **reuse before you fetch, and save back what you fetch.**
Every video that has to go out and find a graphic puts the result here, so the
next video finds it locally. The collection compounds; the fetching doesn't.

```
assets/lottie/<name>.json     the PRISTINE animation, exactly as downloaded
assets/lottie/<name>.png      a still preview — how the next video sees it without rendering
assets/lottie/index.json      tags, source, author, licence, frames/fps/seconds, used_in
assets/icons/<name>.svg       reusable inline-SVG icons
assets/tts-samples/           voice reference clips (mp3s are gitignored)
```

## Lottie

```bash
tools/lottie/search.py "piggy bank saving"            # library first, then the free catalogue
tools/lottie/search.py "piggy bank saving" --sheet    # contact sheets to LOOK at
tools/lottie/search.py --save "07=piggy-bank-coins" --tags "piggy,savings,coins"
tools/lottie/tint.py piggy-bank-coins studio/videos/<slug>-hi/assets/lottie/pig.js "#22c55e"
```

Stored **untinted**. The accent is the scene's role colour, not a property of
the asset — `tint.py` colours a copy into the cut and records which cut used it
(`used_in`), so "have we leaned on this one already?" is answerable.

Licence for everything here: **Lottie Simple License** (LottieFiles free
catalogue) — commercial use, modification, no attribution required; don't
redistribute the raw files. Nothing from the paid marketplace goes in this
directory.

## Icons

An icon is an inline `<svg viewBox="0 0 100 100">` with **no colours and no
classes** — `blockframe.css`'s `.icon` supplies the stroke via `currentColor`,
so the same file reads green in one video and amber in the next. Give every
animatable path an `id` prefixed `i-`; the build renames them per scene.

Add one by writing the file. `ls assets/icons/` is the index — with a filename
this descriptive, a JSON catalogue would be a second home for the same fact.

The full rationale, the traps, and how a cut consumes both:
`vault/knowledge/design-icons-emoji-lottie.md`.
