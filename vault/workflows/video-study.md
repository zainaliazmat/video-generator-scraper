---
summary: The competitor-study mechanism — how Claude fetches top/mid/low videos on a topic, watches/reads them, and turns the comparison into compounding vault knowledge.
updated: 2026-07-04
source: built + smoke-tested 2026-07-04 (backend/study.py)
---

# Workflow: video study (topic → evidence → knowledge)

**Purpose:** before scripting a topic, learn from what already ran — what the top
performer did, what the low performer botched — and bank the findings so every
future script starts smarter. Claude-driven, from a Claude Code session.

## Steps

1. **Topic comes from the gates.** Only study topics that passed Gate 0/1
   ([[../skills/youtube_channel_skill]]). Scrape first if the library is thin.
2. **Build the packet:**
   `venv/bin/python backend/study.py "<topic query>"` (repo root)
   - Picks TOP / MID / LOW by views from `library.db` (comparable long-form only:
     ≥240s, ≥100 views), downloads each at ≤480p into `research/<slug>/`
     (gitignored — regenerable, never committed), grabs YouTube captions →
     timestamped `transcript.txt`, extracts keyframes (1/5s over the hook 0–30s,
     1/30s after), writes `manifest.md` (views/subs/likes/chapters).
   - Explicit picks: `--ids <id>…` · captions-only recon: `--skip-video`.
   - ⚠️ **yt-dlp needs cookies or every pick returns 0 transcripts** (2026-08-07,
     passive-income-number): YouTube answers unauthenticated fetches with *"Sign
     in to confirm you're not a bot"*, which is an auth wall — unlike a 429 it
     never clears on retry, and it kills the whole packet, not one pick. Fixed at
     the root in `study.py`: export **`YTAUTO_COOKIES=/path/to/cookies.txt`**
     (Netscape format) or **`YTAUTO_COOKIES_BROWSER=chrome|chromium|firefox|brave`**
     before running. Opt-in on purpose — the jar is a logged-in session, so the
     tool never opens a browser profile unasked.
   - **When cookies aren't available, the packet has a paid substitute:** vidIQ
     `video_transcript` (5 credits/video, `.claude/skills/vidiq/SKILL.md` R2) is
     the sanctioned input for step 3 and needs no YouTube auth. It gives you the
     words only — no keyframes, so the visual half of the analysis is owed until
     a real packet exists. Say so in the study note rather than quietly skipping it.
3. **Analyze** (Claude reads/views the packet):
   - **Hook (0–30s):** transcript vs [[../skills/long_form_scripting]] §4 — hook
     type, when the payoff promise lands, open loop vs announcement; hook frames
     for the visual (result-first? text overlays? pattern interrupt?).
   - **Structure:** chapters + transcript → beat map with timestamps; where value
     is delivered vs withheld; but/therefore vs and-then transitions; CTA count
     and placement; the ~70% beat.
   - **views/sub ratio** per video (breakout vs channel-size effect — a giant's
     views ≠ format proof).
   - **Low-performer autopsy:** name the concrete failure (hook, packaging,
     pacing, topic, slop) — "low views" alone teaches nothing.
   - **Unclear? Download another** (`--ids`) until confident — accuracy beats
     economy, the files are small.
4. **Write the knowledge:**
   - Study note → `knowledge/video-studies/<slug>.md` (template:
     [[../templates/video-study]]).
   - Transferable findings → append as dated evidence lines in
     [[../knowledge/best-practices]].
   - **Promotion rule:** a pattern confirmed by ~3 independent studies gets
     promoted INTO the relevant skill (bump its version, note the evidence).
     That is the improve-over-time loop: observe → accumulate → promote.

## Honest limits (ponytail)
- Transcripts = YouTube captions; a caption-less video is flagged in the manifest
  (add whisper only when that actually blocks a study).
- Frames ≈ watching stills, not motion — pacing/cut-rhythm judgments stay rough.
- Retention graphs are private to each creator; we infer structure, we cannot
  measure their drop-offs.
