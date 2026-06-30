#!/usr/bin/env bash
#
# YouTube Search Scraper - one-command runner
# -------------------------------------------
# Sets everything up the first time, then runs what you ask for.
#
#   ./run.sh                 # scrape (reads urls.txt) -> youtube_results.tsv
#   ./run.sh myurls.txt      # scrape a different URL file
#   ./run.sh --update        # update yt-dlp first (fixes most YouTube breakages), then scrape
#   ./run.sh diff            # compare the two most recent history snapshots
#   ./run.sh ideas           # AI content plan from the data (needs ANTHROPIC_API_KEY)
#
# Any extra args after the scrape command pass through to youtube_scraper.py, e.g.:
#   ./run.sh --keywords keywords.txt --limit 30
#   ./run.sh --fast
#
# First time only, make it executable:   chmod +x run.sh
#
set -euo pipefail

# Always work from the folder this script lives in (so paths are predictable).
cd "$(dirname "$0")"

VENV_DIR="venv"
PY="$VENV_DIR/bin/python"

# 1. Find a Python 3.8+ interpreter.
if command -v python3 >/dev/null 2>&1; then
    SYS_PY="python3"
elif command -v python >/dev/null 2>&1; then
    SYS_PY="python"
else
    echo "ERROR: Python is not installed. Install Python 3.8+ from https://www.python.org/downloads/"
    exit 1
fi

$SYS_PY -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)' || {
    echo "ERROR: Python 3.8 or newer is required. Found: $($SYS_PY --version)"
    exit 1
}

# 2. Create the virtual environment the first time.
if [ ! -d "$VENV_DIR" ]; then
    echo "First-time setup: creating virtual environment..."
    $SYS_PY -m venv "$VENV_DIR"
    "$PY" -m pip install --upgrade pip -q
    echo "Installing dependencies from requirements.txt..."
    "$PY" -m pip install -r requirements.txt -q
    echo "Setup done."
    echo
fi

# 3. Sub-commands that aren't the scraper.
case "${1:-}" in
    diff)
        shift
        exec "$PY" history.py "$@"
        ;;
    ideas)
        shift
        exec "$PY" ideas.py "$@"
        ;;
esac

# 4. Optional: update yt-dlp (YouTube changes often; this fixes most breakages).
if [ "${1:-}" = "--update" ]; then
    echo "Updating yt-dlp to the latest version..."
    "$PY" -m pip install -U yt-dlp -q
    echo "yt-dlp updated."
    echo
    shift   # drop --update so the rest of the args pass through to the script
fi

# 5. Run the scraper, forwarding any remaining arguments (e.g. flags or a urls file).
exec "$PY" youtube_scraper.py "$@"
