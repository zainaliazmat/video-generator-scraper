==========================================================
  YouTube Content-Research System
  (started life as "replace Instant Data Scraper")
==========================================================

WHAT THIS DOES NOW
------------------
It started as a scraper that pulls YouTube search results into a data file.
It has grown into a small content-research system with three parts:

  1. SCRAPE    - read your search keywords/URLs, pull rich data for every video
                 (views, likes, comments, subscribers, upload date, tags,
                 category, language, channel description + topics, thumbnail).
  2. TRACK     - save a dated snapshot every run and show what changed since last
                 time (new videos, biggest climbers, who dropped out).
  3. PLAN (AI) - optional: send the data to Claude and get a content plan back
                 (theme map, content gaps, 10 ready-to-make video ideas).

Output files (in this folder):
  youtube_results.tsv            - every video, one row each, tab-separated
                                   (opens in Excel/Sheets; tabs keep commas safe)
  history/youtube_results_<date>.tsv  - dated snapshot of each run
  youtube_content_ideas.md       - the AI content plan (only if you run "ideas")


==========================================================
QUICK START  (Linux / Mac)
==========================================================
Open a terminal in this folder and run:

      ./run.sh

The first time, it creates a virtual environment and installs dependencies
automatically, then scrapes urls.txt into youtube_results.tsv.
(If you get "permission denied", run:  chmod +x run.sh  once.)

Windows (or if you prefer manual control):
      python -m venv venv
      venv\Scripts\python -m pip install -r backend\requirements.txt
      set PYTHONPATH=%CD%\backend
      venv\Scripts\python backend\youtube_scraper.py


==========================================================
THE COMMANDS
==========================================================
  ./run.sh                      scrape urls.txt into youtube_results.tsv
  ./run.sh --update             update yt-dlp first (fixes most breakages), then scrape
  ./run.sh --keywords keywords.txt   scrape from plain search terms (no URLs needed)
  ./run.sh --fast               quick mode: list-only, skips likes/comments/subs/tags
  ./run.sh --limit 30           grab 30 videos per keyword instead of 60
  ./run.sh --cookies chrome     use your browser login if YouTube shows a bot check
  ./run.sh diff                 compare the two most recent snapshots in history/
  ./run.sh ideas                AI content plan (needs ANTHROPIC_API_KEY - see below)

You can mix scrape flags:  ./run.sh --keywords keywords.txt --limit 40 --filter month

Full flag list:  ./run.sh --help


==========================================================
CHOOSING YOUR KEYWORDS
==========================================================
Two ways:

A) keywords.txt  (easiest) - just plain search terms, one per line. The script
   builds the YouTube URL and applies an upload-date filter for you.
   Run with:  ./run.sh --keywords keywords.txt
   Change the date filter with --filter year|month|week|today|none (default: year).

B) urls.txt  - paste full YouTube search URLs (one per line). Use this if you
   want exact control over filters. To get a URL: do a YouTube search, apply
   your filters, copy the address bar. This is the default file.


==========================================================
WHAT EACH COLUMN MEANS  (youtube_results.tsv)
==========================================================
  keyword              which search the video came from
  title                video title
  channel/channel_url  channel name + link
  channel_id           YouTube channel id
  subscribers          channel subscriber count (number)
  channel_verified     Yes/No
  views, likes, comments   engagement numbers
  duration/duration_sec    length (12:34 and in seconds)
  upload_date          YYYY-MM-DD
  tags, categories, language   from the video page
  channel_description, channel_tags   from the channel page
  video_url, video_id, thumbnail

Notes:
  - "likes" can be blank when a channel hides its like count - that's YouTube,
    not a bug. "tags" can be blank when a creator sets none.
  - FAST MODE (--fast) skips the per-video and per-channel lookups, so likes,
    comments, subscribers, tags and channel description come back blank. Use it
    when you just want the video list quickly.


==========================================================
TRACKING CHANGES OVER TIME
==========================================================
Every scrape drops a dated copy into history/. After two or more runs:

      ./run.sh diff

shows new videos, the biggest view gains since last time (your trend signal),
and which videos dropped out. A full diff is written to history/diff_*.tsv.
Re-run weekly to watch the niche move.


==========================================================
THE AI CONTENT PLAN  (optional)
==========================================================
Turns the data into a strategy: theme map, content gaps, and 10 video ideas.

This runs on your CLAUDE SUBSCRIPTION via the Claude Agent SDK (the same auth
the Claude Code CLI uses) - no separate API key or pay-as-you-go billing.

  1. One-time: install the Claude Code CLI and log in with your subscription:
        npm install -g @anthropic-ai/claude-code
        claude            # then /login
     (Make sure ANTHROPIC_API_KEY is NOT set, so it bills your subscription.)
  2. Run:      ./run.sh ideas

Writes youtube_content_ideas.md. Uses the Claude model claude-opus-4-8 (falls
back to claude-sonnet-4-6 if your plan can't reach Opus).


==========================================================
THE WEB APP  (Voyara Signal)
==========================================================
A local browser version of the tool: paste keywords, run a scrape with live
progress, sort/filter the results, get an AI "next video" prediction, and
download the TSV - all in your browser. It drives the SAME scraper and AI as
the CLI; nothing is sent to any server. It runs only on your own machine.

PREREQUISITES
  - Python (already needed for the CLI).
  - Node.js 18+ and npm  (only to BUILD the UI the first time).
        Get it from https://nodejs.org/  (or your package manager).
  - For the AI tab: the Claude Code CLI, logged in (see "THE AI CONTENT PLAN"
    above). Without it, the AI tab shows a "log in to use AI" message.

RUN IT
        ./run.sh web                 # builds the UI the first time, then serves it
        ./run.sh web 8080            # use a different port (default 8000)

  The FIRST run downloads npm packages and builds the UI (can take a few
  minutes). Later runs start instantly. When it's up, open the printed URL
  (default http://127.0.0.1:8000) in your browser. Press Ctrl-C to stop.

  Port already in use? Pick another:  ./run.sh web 8090

CHOOSING A MODE  (you pick before each run)
  - Fast - titles & views only. Seconds. No breakout column, no AI prediction
    (those need subscriber counts, which fast mode skips).
  - Full - breakout + AI. Opens every video/channel, so it takes ~15-30 min for
    a big run. This is the full product; use it when you want breakout analysis.

BOT-CHECK ("Sign in to confirm you're not a robot")
  On the setup screen, set "Use browser login" to the browser you're logged
  into YouTube on (Chrome/Firefox/Edge/Brave), then re-run. Close that browser
  fully first so the app can read its cookies. (Same as the CLI's --cookies.)

WINDOWS
  There's no run.sh on Windows. From the project folder, with the venv active:
        venv\Scripts\python -m pip install -r backend\requirements.txt
        cd frontend && npm install && npm run build && cd ..
        set PYTHONPATH=%CD%\backend
        venv\Scripts\python -m uvicorn server.app:app --host 127.0.0.1 --port 8000
  Then open http://127.0.0.1:8000 .


==========================================================
SETTINGS  (defaults, in backend/youtube_scraper.py near the top)
==========================================================
  RESULTS_PER_KEYWORD = 60        videos per search  (override: --limit)
  PAUSE_BETWEEN_URLS  = 2         seconds between searches
  COOKIES_FROM_BROWSER = None     "chrome" etc.       (override: --cookies)
  FETCH_FULL_VIDEO_DETAILS = True likes/comments/subs/tags (off with --fast)
  FETCH_CHANNEL_INFO = True       channel description+topics (off: --no-channel-info)

Command-line flags always override these defaults.


==========================================================
TROUBLESHOOTING
==========================================================
"0 videos" or "Sign in to confirm you're not a bot"
  YouTube's occasional bot check. Run with:  ./run.sh --cookies chrome
  (or edge/firefox/brave - whichever you're logged into YouTube on). Close that
  browser fully first so the script can read its cookies.

"Unsupported URL" / extraction errors / lots of empty rows
  yt-dlp is probably out of date (YouTube changes often). Fix:
      ./run.sh --update

"A few videos were skipped" (e.g. 59 instead of 60)
  Normal - that video is an upcoming premiere, members-only, or was removed.
  The script skips it and keeps going.

"It's slow"
  Full-detail mode opens every video page, so 8 keywords x 60 can take 15-30
  minutes. Use --fast for a quick list, or --limit to grab fewer per keyword.

Want to keep each run's results separately
  Snapshots already pile up in history/. For the main files, rename them after a
  run, or change OUTPUT_BASENAME / use --output to write a different basename.


==========================================================
PROJECT LAYOUT
==========================================================
  run.sh               one-command runner for everything
  urls.txt             your search URLs (default input)        <- you edit these
  keywords.txt         plain search terms (alternative input)  <- you edit these
  README.txt           this file
  Voyara Signal.dc.html   the UI design prototype (reference)

  backend/             all the Python
    youtube_scraper.py   the scraper
    history.py           snapshots + the run-over-run diff
    analyze.py           the Excel analysis dashboard
    ideas.py             the AI content plan + web prediction
    requirements.txt     Python dependencies
    server/              the local web API (FastAPI)
    tests/               the test suite

  frontend/            the web UI (Svelte) -> builds to frontend/dist/

  Outputs (youtube_results.tsv, history/, youtube_content_ideas.md) are written
  here at the project root, next to urls.txt — your data stays where you edit.
