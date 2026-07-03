#!/usr/bin/env bash
#
# YouTube Search Scraper - one-command runner
# -------------------------------------------
# Sets everything up the first time, then runs what you ask for.
#
#   ./run.sh                 # launch the terminal UI (ytauto) - pick a task, hit Enter
#   ./run.sh scrape          # CLI scrape (reads urls.txt) -> youtube_results.tsv
#   ./run.sh scrape myurls.txt --fast   # CLI scrape a different file / with flags
#   ./run.sh ideas           # AI content plan from the data (needs Claude access)
#   ./run.sh diff            # compare the two most recent history snapshots
#   ./run.sh --update        # update yt-dlp first (fixes most YouTube breakages), then launch
#
# First time only, make it executable:   chmod +x run.sh
#
set -euo pipefail

# Always work from the folder this script lives in (so paths are predictable).
cd "$(dirname "$0")"

VENV_DIR="venv"
PY="$VENV_DIR/bin/python"
REQS="backend/requirements.txt"
# Python code lives in backend/; data files (urls.txt, outputs) stay here at root.
export PYTHONPATH="$PWD/backend${PYTHONPATH:+:$PYTHONPATH}"

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
    echo "Installing dependencies from $REQS..."
    "$PY" -m pip install -r "$REQS" -q
    echo "Setup done."
    echo
fi

# 3. Optional: update yt-dlp (YouTube changes often; this fixes most breakages).
if [ "${1:-}" = "--update" ]; then
    echo "Updating yt-dlp to the latest version..."
    "$PY" -m pip install -U yt-dlp -q
    echo "yt-dlp updated."
    echo
    shift   # drop --update so the rest of the args are handled below
fi

# 4. Sub-commands. No sub-command -> the terminal UI.
case "${1:-}" in
    scrape)
        shift
        exec "$PY" backend/youtube_scraper.py "$@"
        ;;
    ideas)
        shift
        exec "$PY" backend/ideas.py "$@"
        ;;
    diff)
        shift
        exec "$PY" backend/history.py "$@"
        ;;
    ''|tui)
        # Make sure the TUI dependency exists even in a venv created before it
        # was added (run.sh only pip-installs at venv-creation time).
        "$PY" -c 'import textual' 2>/dev/null || {
            echo "Installing terminal-UI dependencies..."
            "$PY" -m pip install -r "$REQS" -q
        }
        exec "$PY" -m tui
        ;;
    *)
        echo "Unknown command: $1"
        echo "Try:  ./run.sh            (terminal UI)"
        echo "      ./run.sh scrape     (CLI scrape)"
        echo "      ./run.sh ideas | diff"
        exit 2
        ;;
esac
