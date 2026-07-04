---
summary: The shot list for Video #2 — 10 screen clips, NO VOICE ANYWHERE. Record with OBS/any screen recorder at 1080p, one file per clip, named as below. Everything else (narration, documentary clips, cards, music, edit) is Claude's job.
updated: 2026-07-04
source: script-v2-tts.md screen cues
---

# Video #2 — Recording guide (10 clips, zero voice)

## Setup (once, before recording)
- Screen recorder: OBS or anything → **1920×1080, 30fps**, record the full screen or the app window.
- **No microphone needed. Do not record audio at all.**
- Terminal + editor in a **dark theme**, font size bumped up (readable at 480p).
- **Hide personal stuff:** close email/notification popups; no API keys on screen; hide bookmarks bar.
- Move the mouse **slowly** — half your normal speed. Pause 1s after every click.
- One clip = one file. Name exactly as below, drop them in:
  `~/Documents/ClaudeHyperFrame/videos/video-02-claude-edits-video/assets/clips/`
- Mistake? Just pause 2s and redo the action — I cut the flub out. Long is fine, short is not.

## The clips

**clip-01-brief.mp4** (~60s) — Claude Code in the terminal, inside the a-century-of-travel project.
Paste this brief and hit enter; let Claude start responding (~20s of streaming is enough):
> Create a cinematic, vintage parallax photo slideshow telling the history of travel decade by decade. Archival black-and-white photos, giant year numbers, elegant serif titles, gentle camera drift, film grain, slow nostalgic score. About 4 minutes.
*Must be visible: the prompt text + Claude's response streaming.*

**clip-02-design.mp4** (~40s) — Open `videos/a-century-of-travel/DESIGN.md` in your editor.
Scroll slowly top → bottom, pausing ~3s on the color palette table and ~3s on the "Motion language" section.
*Must be visible: the palette table and the Ken Burns/parallax lines.*

**clip-03-timeline.mp4** (~25s) — Open any timeline editor (CapCut / DaVinci — free is fine) with any project that has several clips on the timeline. Drag a clip, scrub the playhead back and forth, hover over the layers. It should look busy/manual.
*Must be visible: a cluttered multi-track timeline + the playhead moving.*

**clip-04-scene-prompt.mp4** (~60s) — Claude Code again. Type this and let it work:
> Create the 1907 scene: the Mauretania ocean liner photo, giant year number "1907", title "Queens of the Atlantic" on a dark band, caption "Four and a half days to cross an ocean.", slow drift left per DESIGN.md.
*Must be visible: your plain-English request + the scene file being written.*

**clip-05-scene-code.mp4** (~25s) — Open one scene HTML file from the project (any scene under the video's folder). Scroll slowly; then rest the cursor/selection on the `data-start` and `data-duration` attributes for ~4s.
*Must be visible: those two attributes, sharp and readable.*

**clip-06-render.mp4** (2 short takes, ok as one file) — Terminal in the project:
(a) run the render command and capture the first ~20s of progress output;
(b) later, capture the moment it finishes and prints the output file (~10s).
Don't record the whole 20 minutes — start + finish is all I need.
*Must be visible: the command line itself + progress + the "done"/output line.*

**clip-07-kokoro.mp4** (~30s) — Trigger one TTS generation in the project (any single line through the audio pipeline). Then show the resulting .wav in the file manager or play its waveform in any audio app.
*Must be visible: the generation happening + a waveform/file appearing.*

**clip-08-studio-toggle.mp4** (~40s) — YouTube Studio → upload any placeholder video (you can delete the draft after) → go to the "Altered content" question → read it for 2s → click **Yes**. Then open studio's Audio Library page and scroll for 5s.
*Must be visible: the altered-content question text + clicking Yes + the Audio Library.*
⚠️ Make sure your channel name/email shown is the one you're OK showing — else crop-safe: keep the browser window narrow.

**clip-09-fix.mp4** (~45s) — WAIT for my go on this one. I will first prepare the title-card fix in the project; then you record: paste the one-sentence fix prompt I give you → the re-render of that scene → open the fixed frame.
*Must be visible: prompt → render → the clean title card.*

**clip-10-files.mp4** (~20s) — File manager (or `tree` in terminal) inside `videos/a-century-of-travel/`: browse slowly through assets/ → voice wavs → scenes → renders/.
*Must be visible: the folder structure + the 14 voice files + the renders.*

## Already covered — do NOT record
The documentary itself (I have both renders), its frames, DESIGN.md/runbook text for
graphics, all cards/stamps/verdict chips (rendered in HyperFrames), the frozen-scroll
bot clip (I generate from our 2026-07-02 test), music (YT Audio Library — I'll
shortlist 2 tracks for you to download), and ALL narration (Kokoro).

## What happens next (the build, my side)
1. You record clips 01–08 + 10 (09 waits for my fix prep) → tell me they're in the folder.
2. I audition Kokoro voices on 3 sample lines → you pick one (default: bm_george, the documentary's voice — poetic symmetry).
3. I build in the ClaudeHyperFrame project: DESIGN.md (video-02) → STORYBOARD locked to script-v2-tts → generate all 46 VO lines → scenes → sound design → `check` → render 1080p.
4. You watch the render → notes → I iterate → final master + thumbnail assets + description text (links, disclosure line, giveaway).
