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
      venv\Scripts\python -m pip install -r requirements.txt
      venv\Scripts\python youtube_scraper.py


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
SETTINGS  (defaults, in youtube_scraper.py near the top)
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
FILES IN THIS FOLDER
==========================================================
  youtube_scraper.py   the scraper (run it, or use ./run.sh)
  history.py           saves snapshots + the run-over-run diff
  ideas.py             the optional AI content plan
  run.sh               one-command runner for all of the above
  urls.txt             your search URLs (default input)
  keywords.txt         plain search terms (alternative input)
  requirements.txt     dependencies
  README.txt           this file
