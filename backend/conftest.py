"""Put the backend/ directory on sys.path so the top-level modules
(youtube_scraper, analyze, history, ideas, tui) import cleanly when pytest
is run from anywhere."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
