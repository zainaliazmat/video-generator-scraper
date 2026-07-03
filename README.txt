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
automatically, then launches the TERMINAL UI: a menu you drive with the arrow
keys. Pick a task (Scrape / Predict / Compare), press Enter, answer the prompts,
hit Generate — no flags to remember, no urls.txt to edit by hand.
(If you get "permission denied", run:  chmod +x run.sh  once.)

Want to type one word from anywhere instead of ./run.sh? Put the launcher on
your PATH once:

      ln -s "$(pwd)/ytauto" ~/.local/bin/ytauto

Then just run:  ytauto

Windows (or if you prefer manual control):
      python -m venv venv
      venv\Scripts\python -m pip install -r backend\requirements.txt
      set PYTHONPATH=%CD%\backend
      venv\Scripts\python -m tui                 # the terminal UI
      venv\Scripts\python backend\youtube_scraper.py   # or the plain CLI scrape


==========================================================
THE COMMANDS
==========================================================
The terminal UI covers everything below with menus. These commands are still
here for scripting / muscle memory:

  ./run.sh                      launch the terminal UI (the default)
  ./run.sh scrape               scrape urls.txt into youtube_results.tsv
  ./run.sh scrape --update      update yt-dlp first (fixes most breakages), then scrape
  ./run.sh scrape --keywords keywords.txt   scrape from plain search terms
  ./run.sh scrape --fast        quick mode: list-only, skips likes/comments/subs/tags
  ./run.sh scrape --limit 30    grab 30 videos per keyword instead of 60
  ./run.sh scrape --cookies chrome   use your browser login if YouTube shows a bot check
  ./run.sh diff                 compare the two most recent snapshots in history/
  ./run.sh ideas                AI content plan (needs Claude access - see below)

You can mix scrape flags:  ./run.sh scrape --keywords keywords.txt --limit 40 --filter month

Full flag list:  ./run.sh scrape --help


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
THE TERMINAL UI  (ytauto)
==========================================================
The front end is a terminal app — no browser, no Node.js, no web server. It
drives the SAME scraper, diff, and AI as the commands above; everything runs on
your own machine, in-process.

RUN IT
        ./run.sh          # or `ytauto` if you symlinked it onto your PATH

HOW IT WORKS
  1. A menu appears. Move with the arrow keys, press Enter to pick a task:
        Scrape YouTube  ·  Predict content ideas  ·  Compare snapshots  ·  Quit
  2. Scrape asks its questions on screen:
        - paste your search URLs or plain keywords (one per line) — right in the
          app, no editing urls.txt
        - pick a time range and how many videos per link
        - Fast mode on/off (on = list-only, much faster; off = full detail)
     Then hit Generate and watch the progress stream live. When it finishes it
     saves youtube_results.tsv + a dated history snapshot, and offers to run a
     prediction on the fresh data.
  3. Predict analyses the last scrape (or any saved snapshot) and streams a
     Claude prediction. Needs Claude access (see "THE AI CONTENT PLAN" above);
     without it you get a plain "couldn't reach Claude" message.
  4. Compare picks two snapshots and shows what changed (same as ./run.sh diff).

  Press Esc to go back a screen (or cancel a running task). Press q at the menu
  to quit.

BOT-CHECK ("Sign in to confirm you're not a robot")
  This is YouTube's occasional check. Use the CLI's --cookies for it:
        ./run.sh scrape --cookies chrome
  (or edge/firefox/brave — whichever you're logged into YouTube on). Close that
  browser fully first so the tool can read its cookies.


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
  run.sh               one-command runner (launches the terminal UI by default)
  ytauto               launcher you can symlink onto your PATH
  urls.txt             your search URLs (default CLI input)     <- you edit these
  keywords.txt         plain search terms (alternative input)   <- you edit these
  README.txt           this file

  backend/             all the Python
    youtube_scraper.py   the scraper
    history.py           snapshots + the run-over-run diff
    analyze.py           the Excel analysis dashboard
    ideas.py             the AI content plan + prediction
    requirements.txt     Python dependencies
    tui/                 the terminal UI (Textual) — the front end
    tests/               the test suite

  Outputs (youtube_results.tsv, history/, youtube_content_ideas.md) are written
  here at the project root, next to urls.txt — your data stays where you edit.
