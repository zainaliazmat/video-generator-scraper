"""Backfill subscriber counts for indie (non-broadcaster) channels from the scan."""
import sys, json
sys.path.insert(0, "backend")
from youtube_scraper import fetch_channel_info

BROADCASTERS = ("ZDF","ARTE","NDR","WELT","RTL","Kabel","rbb","Terra X","STRG_F","MDR","SWR","BR","ARD","3sat","phoenix")
d = json.load(open(".scan/de_scan.json"))
out = {}
for niche, chans in d.items():
    keep = [c for c in chans if not any(b.lower() in c["channel"].lower() for b in BROADCASTERS)]
    res = []
    for c in keep[:6]:
        info = fetch_channel_info(c["url"]) if c.get("url") else {}
        res.append({**c, "subs": info.get("subscribers") or "?",
                    "desc": (info.get("channel_description") or "")[:160]})
        print(f".. {niche}/{c['channel']}: {res[-1]['subs']}", file=sys.stderr, flush=True)
    out[niche] = res
print(json.dumps(out, ensure_ascii=False, indent=1))
