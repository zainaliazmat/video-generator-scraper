---
summary: Milestone note for Video #2, TechToolTester's launch piece — **LIVE 2026-07-31** as "Claude AI Made This Entire Video — No Premiere, No Timeline (100% Free)" (youtu.be/iB39QrexQ8c). Source archived to `src/`, studio dir deleted. The build history and the render-ops lessons live in [[build-log]]; this note holds the shipped state.
updated: 2026-07-31
source: [[build-log]] + the archived composition in `src/`
---

# Video #2 — "Claude AI Made This Entire Video" (SHIPPED · milestone)

The AI-tools channel's launch piece and the **first video this repo took end to end**:
Claude Code + HyperFrames build an entire cinematic video with no NLE, narrated by
Kokoro TTS, with the creator supplying only screen recordings ([[recording-guide]]).
It is also the video that teaches the workflow «A Century of Travel» was made with —
the cross-feed [[../../knowledge/channels]] describes.

- **Script:** [[script-v2-tts]] (canonical, Kokoro edition) · [[script-v1]] (human-VO,
  superseded) · [[script-v3-urdu]]
- **Build history + render-ops lessons:** [[build-log]] — the lessons themselves are
  promoted into [[../../skills/hyperframes_production]] §6.
- **Design system:** [[../../knowledge/design-techtooltester]]

## Published + archived (2026-07-31)

**State: LIVE on YouTube · source archived · studio dir deleted.**

| Cut | Channel | URL | Thumbnail |
|---|---|---|---|
| single (EN) | @techtooltester | https://youtu.be/iB39QrexQ8c | `src/THUMBNAIL-video-02-make-cinematic-video.png` |

**Source: `src/`** — `storyboard.mjs` (the beats) + `build.mjs` (the generator) →
`index.html`, `DESIGN.md`, `gen-vo.sh` / `process-vo.sh` (the Kokoro VO pipeline),
`audio_request.json` / `audio_meta.json`, `timing.txt` and the shipped thumbnail.
`studio/videos/video-02-claude-edits-video` and its `compositions/` text mirror are
**deleted** per the finished-video rule ([[../../CLAUDE]]).

**Re-render is not free, and this one is the least reproducible of the archives:** the
composition is built around the creator's **own OBS screen recordings** (7 clips, the
trimmed/sub-cut derivatives, and excerpts cut from the Century master). Those lived under
the `assets` symlink into `studio/library/projects/`, which no longer exists — so a
rebuild needs the screen clips **re-recorded** off [[recording-guide]], not just
re-generated. The Kokoro VO and the synthesized SFX do regenerate from the archived
scripts and `gen-vo.sh`.

Still owed: analytics after 28 days · confirm the AI-disclosure toggle was set on the
upload (draft placeholder #3 in [[build-log]] made that a ship-day promise).
