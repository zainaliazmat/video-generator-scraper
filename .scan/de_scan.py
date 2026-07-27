"""Scan German-language YouTube for the 5 candidate niches; rank channels by views.

Run:  venv/bin/python .scan/de_scan.py > .scan/de_scan.json 2> .scan/de_scan.log
"""
import sys, json, collections
sys.path.insert(0, "backend")
import youtube_scraper
from youtube_scraper import build_search_url, scrape_url

# ponytail: list-only pull — we only need channel/subs/views, not likes/tags.
# Full-detail mode opens every video page (~50x slower).
youtube_scraper.FETCH_FULL_VIDEO_DETAILS = False
youtube_scraper.FETCH_CHANNEL_INFO = False

NICHES = {
    "geschichte": ["deutsche geschichte dokumentation", "geschichte doku deutsch"],
    "wissenschaft": ["weltraum doku deutsch", "wissenschaft erklärt deutsch"],
    "truecrime": ["wahre kriminalfälle deutschland", "true crime deutsch doku"],
    "technik_geld": ["finanzen einfach erklärt deutsch", "technik erklärt deutsch"],
    "lost_places": ["lost places doku deutsch", "ingenieurskatastrophen deutsch"],
}

out = {}
for niche, kws in NICHES.items():
    rows = []
    for kw in kws:
        url = build_search_url(kw, period="year")
        try:
            rows += scrape_url(url, 25, progress=lambda m: None)
        except Exception as e:
            print(f"!! {kw}: {e}", file=sys.stderr)
        print(f".. {niche}/{kw}: {len(rows)} rows", file=sys.stderr, flush=True)

    seen, chans = set(), {}
    for r in rows:
        vid = r.get("video_id")
        if not vid or vid in seen:
            continue
        seen.add(vid)
        name = r.get("channel") or "?"
        c = chans.setdefault(name, {
            "subscribers": r.get("subscribers") or 0,
            "url": r.get("channel_url", ""),
            "videos": 0, "views": 0, "titles": [],
        })
        c["subscribers"] = max(c["subscribers"], r.get("subscribers") or 0)
        c["videos"] += 1
        c["views"] += r.get("views") or 0
        if len(c["titles"]) < 2:
            c["titles"].append({"t": (r.get("title") or "")[:70], "v": r.get("views")})

    ranked = sorted(({"channel": k, **v} for k, v in chans.items()),
                    key=lambda x: x["views"], reverse=True)
    for c in ranked:
        c["avg_views"] = round(c["views"] / c["videos"]) if c["videos"] else 0
    out[niche] = ranked[:15]
    print(f"== {niche}: {len(seen)} videos, {len(chans)} channels", file=sys.stderr, flush=True)

print(json.dumps(out, ensure_ascii=False, indent=1))
