==========================================================
  ytauto — YouTube Content-Research Terminal App
==========================================================

WHAT THIS DOES
--------------
A terminal app (no browser, no web server) with three tasks, all driven from a
menu on your own machine:

  1. SCRAPE   - paste search keywords/URLs; pull rich data for every video
                (views, likes, comments, subscribers, upload date, tags,
                category, language, channel description + topics, thumbnail).
  2. COMPARE  - every scrape saves a dated snapshot; compare two of them to see
                what changed (new videos, biggest climbers, who dropped out).
  3. PREDICT  - send the data to Claude and get back the single best NEW video to
                make next (plus 4 alternatives), with the evidence behind it.

Output files (in this folder):
  youtube_results.tsv                 - every video, one row each, tab-separated
  history/youtube_results_<date>.tsv  - dated snapshot of each run


==========================================================
QUICK START  (Linux / Mac)
==========================================================
Open a terminal in this folder and run:

      ./run.sh

The first time, it creates a virtual environment and installs dependencies
automatically, then launches the terminal UI. Drive it with the arrow keys:
pick a task, press Enter, answer the on-screen prompts, hit Generate.
(If you get "permission denied", run:  chmod +x run.sh  once.)

Type one word from anywhere instead of ./run.sh — put the launcher on your PATH:

      ln -s "$(pwd)/ytauto" ~/.local/bin/ytauto      # then just run:  ytauto

Update yt-dlp first (fixes most YouTube breakages), then launch:

      ./run.sh --update

Windows:
      python -m venv venv
      venv\Scripts\python -m pip install -r backend\requirements.txt
      set PYTHONPATH=%CD%\backend
      venv\Scripts\python -m tui


==========================================================
HOW THE APP WORKS
==========================================================
  1. A menu appears. Move with the arrow keys, Enter to pick a task:
        Scrape · Predict · Compare · Browse library · Quit
  2. SCRAPE asks its questions on screen:
        - paste your search URLs or plain keywords (one per line)
        - pick a time range and how many videos per link
        - Fast mode on/off (on = list-only, much faster; off = full detail)
        - Browser cookies (only if YouTube shows a bot check)
     Hit Generate and watch progress stream live. Every video is deduped into
     the central library (see below): you'll see "N already in library" per
     search, and when a search is mostly already-seen it pages deeper for
     brand-new videos (or tells you there are none left). When it finishes it
     saves youtube_results.tsv + a dated history snapshot, and offers to Predict.
  3. PREDICT analyses the last scrape (or any saved snapshot) and streams a
     Claude prediction. Needs Claude access (see below); without it you get a
     plain "couldn't reach Claude" message — never a fabricated number.
  4. COMPARE picks two snapshots and shows what changed.
  5. BROWSE LIBRARY searches everything you've ever scraped (one row per video,
     with its latest view/sub counts and how many times you've seen it).

THE LIBRARY (library.db)
  A single SQLite file at the project root is the permanent knowledge base:
  one row per video, keyed by video_id. Re-scraping a known video refreshes its
  numbers instead of duplicating it (a blank from fast mode never wipes a real
  value a full scrape found). It's plain SQLite — query it with any tool.

  Esc goes back a screen (or cancels a running task). q at the menu quits.

FAST MODE skips the per-video and per-channel lookups, so likes, comments,
subscribers, tags and channel description come back blank. Use it when you just
want the video list quickly. Prediction needs subscriber counts, so scrape with
Fast mode OFF if you plan to predict.


==========================================================
THE AI PREDICTION  (Claude access)
==========================================================
The Predict task runs on your CLAUDE SUBSCRIPTION via the Claude Agent SDK (the
same auth the Claude Code CLI uses) — no separate API key or pay-as-you-go bill.

  One-time: install the Claude Code CLI and log in with your subscription:
        npm install -g @anthropic-ai/claude-code
        claude            # then /login
  (Make sure ANTHROPIC_API_KEY is NOT set, so it bills your subscription.)

Uses model claude-opus-4-8 (falls back to claude-sonnet-4-6 if your plan can't
reach Opus).


==========================================================
TROUBLESHOOTING
==========================================================
"0 videos" or "Sign in to confirm you're not a bot"
  YouTube's occasional bot check. On the Scrape screen, set "Browser cookies" to
  the browser you're logged into YouTube on (chrome/firefox/edge/brave) and try
  again — close that browser fully first so the tool can read its cookies. Also
  worth running ./run.sh --update.

"Unsupported URL" / extraction errors / lots of empty rows
  yt-dlp is probably out of date (YouTube changes often). Fix:  ./run.sh --update

"A few videos were skipped" (e.g. 59 instead of 60)
  Normal — that video is an upcoming premiere, members-only, or was removed.

"It's slow"
  Full-detail mode opens every video page, so 8 keywords x 60 can take 15-30
  minutes. Use Fast mode, or a smaller "videos per link".


==========================================================
PROJECT LAYOUT
==========================================================
  run.sh               one-command runner (sets up the venv, launches the TUI)
  ytauto               launcher you can symlink onto your PATH
  README.txt           this file

  backend/             all the Python
    tui/                 the terminal UI (Textual) — the front end
    youtube_scraper.py   the scrape engine (+ dedup/top-up against the library)
    library.py           the central SQLite library (dedup, refresh, search)
    history.py           snapshots + the run-over-run diff
    analyze.py           metric helpers (scoring, aggregations) for the digest
    ideas.py             the Claude prediction
    requirements.txt     Python dependencies
    tests/               the test suite

  Outputs (youtube_results.tsv, history/, library.db) live at the project root.
