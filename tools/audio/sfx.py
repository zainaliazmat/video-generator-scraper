#!/usr/bin/env python3
"""ElevenLabs sound effects + music beds — stdlib only, no deps.

The kit (prompts, durations, levels) lives in `tools/audio/kit.json`; the
generated mp3s land in `studio/library/{sfx,music}/`. That split is deliberate
and matches how the pipeline already treats images and voice: the **prompt** is
the git-tracked reproducing text, the **audio** is regenerable output under the
gitignored `studio/`.

    tools/audio/sfx.py --kit                 # the 7 SFX (skips what exists)
    tools/audio/sfx.py --kit --music         # ...and the 2 music beds
    tools/audio/sfx.py --one stamp --force   # regenerate a single entry
    tools/audio/sfx.py --list               # what's in the kit and what's on disk
    tools/audio/sfx.py --selftest           # offline, no API, no credits

**Cached by name.** These assets are shared by every video, so the whole kit
costs ~9 API calls ONCE, not per cut. A run that finds every file present makes
zero calls — that is the normal case, and why `--kit` is safe to leave in the
pipeline's preflight.

Every file is peak-normalised to the level named in kit.json, so the build can
place a sound without re-judging its loudness. SFX sit far under the voice: the
mix lands at -14 LUFS, so a -20 dBFS peak reads as punctuation.

Exit codes: 0 ok · 2 terminal (bad key, 4xx) · 3 retryable (429, 5xx, network).
FIN_FAKE_APIS=1 synthesises local tones instead of calling the API.
"""
import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

EXIT_TERMINAL, EXIT_RETRYABLE = 2, 3
API = "https://api.elevenlabs.io/v1"
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KIT = os.path.join(ROOT, "tools", "audio", "kit.json")
OUT = {"sfx": os.path.join(ROOT, "studio", "library", "sfx"),
       "music": os.path.join(ROOT, "studio", "library", "music")}


def load_env(path=None):
    """KEY=VALUE lines; never overrides a var already set in the environment."""
    path = path or os.path.join(ROOT, ".env")
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))


def api_key():
    key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not key:
        sys.exit("ERROR: ELEVENLABS_API_KEY is empty — put it in .env")
    return key


def post_audio(path_frag, payload, key, soft=False):
    """POST JSON, expect audio/mpeg back. `soft` returns None on a 4xx instead
    of exiting — used for music, which is optional and gated behind an account
    permission the SFX kit does not need."""
    req = urllib.request.Request(
        f"{API}/{path_frag}", data=json.dumps(payload).encode("utf-8"),
        headers={"xi-api-key": key, "Content-Type": "application/json",
                 "Accept": "audio/mpeg"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=600) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")[:800]
        retryable = e.code == 429 or e.code >= 500
        if soft and not retryable:
            print(f"  ! {e.code} from /{path_frag}: {body}")
            return None
        print(f"ERROR {e.code} from ElevenLabs /{path_frag}: {body}", file=sys.stderr)
        sys.exit(EXIT_RETRYABLE if retryable else EXIT_TERMINAL)
    except urllib.error.URLError as e:
        print(f"ERROR: could not reach ElevenLabs ({e.reason})", file=sys.stderr)
        sys.exit(EXIT_RETRYABLE)


def fake_tone(path, seconds, freq):
    """A local stand-in so a dry run exercises every code path for free."""
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi",
                    "-i", f"sine=frequency={freq}:duration={seconds}",
                    "-q:a", "5", path], check=True)


def peak_dbfs(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af", "astats",
                        "-f", "null", "-"], capture_output=True, text=True)
    peaks = [float(l.split(":")[1]) for l in r.stderr.splitlines()
             if "Peak level dB" in l and "inf" not in l.split(":")[1]]
    return max(peaks) if peaks else None


def normalise(path, target_db):
    """Peak-normalise in place so the build never has to re-judge loudness."""
    cur = peak_dbfs(path)
    if cur is None:
        return None
    tmp = path + ".tmp.mp3"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", path,
                    "-af", f"volume={target_db - cur:.2f}dB", "-q:a", "3", tmp],
                   check=True)
    os.replace(tmp, path)
    return peak_dbfs(path)


def generate(kind, name, spec, key, force=False):
    """One kit entry → one normalised mp3. Returns (path, made_a_call)."""
    os.makedirs(OUT[kind], exist_ok=True)
    path = os.path.join(OUT[kind], f"{name}.mp3")
    if os.path.exists(path) and not force:
        print(f"  skip (cached)  {kind}/{name}.mp3")
        return path, False

    secs = spec["seconds"]
    if os.environ.get("FIN_FAKE_APIS") == "1":
        # deterministic pitch per name so fake files are distinguishable
        fake_tone(path, min(secs, 3), 200 + (abs(hash(name)) % 12) * 40)
    elif kind == "sfx":
        audio = post_audio("sound-generation", {
            "text": spec["prompt"], "duration_seconds": secs,
            "prompt_influence": 0.45}, key)
        open(path, "wb").write(audio)
    else:
        audio = post_audio("music", {
            "prompt": spec["prompt"], "music_length_ms": int(secs * 1000)},
            key, soft=True)
        if audio is None:
            print(f"  -- music/{name}.mp3 NOT generated. Two ways forward:\n"
                  f"     1. add the `music_generation` permission to the "
                  f"ElevenLabs API key (or upgrade the plan), then re-run;\n"
                  f"     2. drop a bed at studio/library/music/{name}.mp3 by hand — "
                  f"the YouTube Audio Library is free, has no channel-count limit, "
                  f"and is the only source with a first-party guarantee it won't be "
                  f"claimed through Content ID.\n"
                  f"     Either way the build looks for the same filename.")
            return None, False
        open(path, "wb").write(audio)

    got = normalise(path, spec["peak_dbfs"])
    size = os.path.getsize(path)
    print(f"  OK  {kind}/{name}.mp3  {secs}s  {size:,}b  peak {got} dBFS"
          f"  ({spec.get('helper', 'bed')})")
    return path, True


def run(kinds, only=None, force=False):
    kit = json.load(open(KIT, encoding="utf-8"))
    key = None if os.environ.get("FIN_FAKE_APIS") == "1" else api_key()
    calls = 0
    for kind in kinds:
        entries = {k: v for k, v in kit[kind].items() if not only or k == only}
        if only and not entries:
            continue
        print(f"{kind}:")
        for name, spec in entries.items():
            _, made = generate(kind, name, spec, key, force)
            calls += made
    print(f"\n{calls} API call(s) made"
          f"{' (FAKE)' if os.environ.get('FIN_FAKE_APIS') == '1' else ''}")
    return calls


def show():
    kit = json.load(open(KIT, encoding="utf-8"))
    for kind in ("sfx", "music"):
        print(f"\n{kind}:")
        for name, spec in kit[kind].items():
            p = os.path.join(OUT[kind], f"{name}.mp3")
            here = f"{os.path.getsize(p):,}b peak {peak_dbfs(p)} dBFS" if os.path.exists(p) else "— not generated"
            print(f"  {name:<12} {spec['seconds']:>5}s  target {spec['peak_dbfs']:>4} dBFS"
                  f"  {here}")
            print(f"               → {spec.get('helper', 'music bed')}")


def _selftest():
    """Offline: exercises generate → normalise → cache-skip with no API."""
    import shutil
    import tempfile
    global OUT
    real, d = OUT, tempfile.mkdtemp(prefix="sfxkit-")
    os.environ["FIN_FAKE_APIS"] = "1"
    try:
        OUT = {"sfx": os.path.join(d, "sfx"), "music": os.path.join(d, "music")}
        kit = json.load(open(KIT, encoding="utf-8"))
        assert len(kit["sfx"]) == 7, f"kit should hold 7 sfx, has {len(kit['sfx'])}"
        for name, spec in kit["sfx"].items():
            assert spec["peak_dbfs"] < -10, f"{name} peak target is too hot"
            assert spec["helper"], f"{name} has no motion helper — it shouldn't be in the kit"

        n1 = run(["sfx"])
        assert n1 == 7, f"first run should generate 7, made {n1}"
        p = os.path.join(OUT["sfx"], "stamp.mp3")
        got = peak_dbfs(p)
        want = kit["sfx"]["stamp"]["peak_dbfs"]
        assert abs(got - want) < 1.0, f"stamp normalised to {got}, wanted {want}"

        before = open(p, "rb").read()
        n2 = run(["sfx"])
        assert n2 == 0, f"cached run should make 0 calls, made {n2}"
        assert open(p, "rb").read() == before, "cached run overwrote a file"

        n3 = run(["sfx"], only="stamp", force=True)
        assert n3 == 1, f"--force --one should make exactly 1 call, made {n3}"
        print("\nselftest OK")
    finally:
        OUT = real
        os.environ.pop("FIN_FAKE_APIS", None)
        shutil.rmtree(d, ignore_errors=True)


def main(argv=None):
    p = argparse.ArgumentParser(description="ElevenLabs SFX + music kit")
    p.add_argument("--kit", action="store_true", help="generate the SFX kit (cached)")
    p.add_argument("--music", action="store_true", help="include the music beds")
    p.add_argument("--one", help="a single kit entry by name")
    p.add_argument("--force", action="store_true", help="regenerate even if cached")
    p.add_argument("--list", action="store_true", help="show the kit and what's on disk")
    p.add_argument("--selftest", action="store_true")
    a = p.parse_args(argv)

    if a.selftest:
        _selftest()
        return 0
    if a.list:
        show()
        return 0
    load_env()
    if a.one:
        return 0 if run(["sfx", "music"], only=a.one, force=a.force) >= 0 else 1
    if a.kit:
        run(["sfx"] + (["music"] if a.music else []), force=a.force)
        return 0
    p.error("nothing to do — try --kit, --list or --selftest")


if __name__ == "__main__":
    sys.exit(main())
