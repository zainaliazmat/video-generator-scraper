#!/usr/bin/env python3
"""ElevenLabs text-to-speech — stdlib only, no deps.

Reads ELEVENLABS_API_KEY from the project-root .env (or the environment).

  # verify the key + see your available voices and their IDs:
  python3 tools/tts/elevenlabs_tts.py --list-voices

  # generate from inline text:
  python3 tools/tts/elevenlabs_tts.py --voice <VOICE_ID> --text "ٹھیک ہے، سنو" --out assets/tts-samples/test.mp3

  # generate from a text file (e.g. one script segment):
  python3 tools/tts/elevenlabs_tts.py --voice <VOICE_ID> --file segment.txt --out out.mp3

Default model is eleven_multilingual_v2 (supports Urdu). Override with --model.

Exit codes: 0 ok · 2 terminal (bad/missing key, 4xx) · 3 retryable (429, 5xx,
network unreachable). Set FIN_FAKE_APIS=1 to synthesize a local sine-tone mp3
instead of calling the API (zero-cost pipeline dry runs).
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


def load_env(path=None):
    """Minimal .env parser: KEY=VALUE lines, ignores # comments and blanks.
    Does NOT override a var already set in the real environment."""
    path = path or os.path.join(ROOT, ".env")
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key, val = key.strip(), val.strip().strip('"').strip("'")
            os.environ.setdefault(key, val)


def api_key():
    key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not key:
        print("ERROR: ELEVENLABS_API_KEY is empty. Paste your key into .env "
              "(see .env.example) then re-run.", file=sys.stderr)
        sys.exit(EXIT_TERMINAL)
    return key


def _request(url, key, data=None, method="GET"):
    headers = {"xi-api-key": key}
    if data is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(data).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        print(f"ERROR {e.code} from ElevenLabs: {body}", file=sys.stderr)
        sys.exit(EXIT_RETRYABLE if e.code == 429 or e.code >= 500 else EXIT_TERMINAL)
    except urllib.error.URLError as e:
        print(f"ERROR: could not reach ElevenLabs ({e.reason}).", file=sys.stderr)
        sys.exit(EXIT_RETRYABLE)


def list_voices(key):
    raw = _request(f"{API}/voices", key)
    voices = json.loads(raw).get("voices", [])
    if not voices:
        print("No voices found on this account.")
        return
    print(f"{'VOICE ID':<24}  NAME  (labels)")
    for v in voices:
        labels = ", ".join(f"{k}={x}" for k, x in (v.get("labels") or {}).items())
        print(f"{v['voice_id']:<24}  {v.get('name','?')}  ({labels})")


def fake_synthesize(text, out):
    """FIN_FAKE_APIS=1: a local sine-tone mp3 sized from char count. A tone, not
    silence, so the pipeline's silent-clip guard still passes on dry runs.
    13 chars/s sits within the ±35% duration check for both 12.5 and 15."""
    dur = max(1.2, len(text) / 13.0)
    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-f", "lavfi",
         "-i", "sine=frequency=440:sample_rate=44100",
         "-t", f"{dur:.2f}", "-q:a", "2", out], check=True)
    print(f"OK (FAKE): wrote {dur:.2f}s tone -> {out}")


def synthesize(key, voice, text, out, model, stability, similarity,
               style=0.0, speed=1.0, prev_text=None, next_text=None, seed=None):
    if os.environ.get("FIN_FAKE_APIS") == "1":
        fake_synthesize(text, out)
        return
    url = f"{API}/text-to-speech/{voice}"
    payload = {
        "text": text,
        "model_id": model,
        "voice_settings": {
            "stability": stability,
            "similarity_boost": similarity,
            "style": style,           # 0..1 — higher = more dramatic/expressive
            "speed": speed,           # 0.7..1.2 — <1 slower/weightier
            "use_speaker_boost": True,
        },
    }
    # request stitching — keep prosody continuous across chunked segments
    if prev_text:
        payload["previous_text"] = prev_text
    if next_text:
        payload["next_text"] = next_text
    if seed is not None:
        payload["seed"] = seed
    audio = _request(url, key, data=payload, method="POST")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    tmp = out + ".tmp"
    with open(tmp, "wb") as fh:
        fh.write(audio)
    os.replace(tmp, out)  # never observed half-written
    print(f"OK: wrote {len(audio):,} bytes -> {out}")


def main(argv=None):
    p = argparse.ArgumentParser(description="ElevenLabs TTS (stdlib only)")
    p.add_argument("--list-voices", action="store_true", help="list account voices + IDs, then exit")
    p.add_argument("--voice", help="voice ID (get one from --list-voices)")
    p.add_argument("--text", help="text to speak")
    p.add_argument("--file", help="path to a UTF-8 text file to speak")
    p.add_argument("--out", default="assets/tts-samples/out.mp3", help="output .mp3 path")
    p.add_argument("--model", default="eleven_multilingual_v2", help="model id (default supports Urdu)")
    p.add_argument("--stability", type=float, default=0.5, help="0..1 — low=expressive/varying, high=steady")
    p.add_argument("--similarity", type=float, default=0.75, help="0.75..0.85 recommended (1.0 over-enunciates)")
    p.add_argument("--style", type=float, default=0.0, help="0..1 — higher=more dramatic/expressive")
    p.add_argument("--speed", type=float, default=1.0, help="0.7..1.2 — <1 slower/weightier")
    p.add_argument("--prev-text", help="preceding text (request stitching, continuity across chunks)")
    p.add_argument("--next-text", help="following text (request stitching)")
    p.add_argument("--seed", type=int, help="fixed seed for reproducible takes")
    p.add_argument("--skip-existing", action="store_true",
                   help="skip if --out already exists and is non-empty (resume without re-spending credits)")
    p.add_argument("--selftest", action="store_true", help="offline check of the .env parser")
    args = p.parse_args(argv)

    if args.selftest:
        _selftest()
        return

    load_env()
    key = api_key()

    if args.list_voices:
        list_voices(key)
        return

    text = args.text
    if args.file:
        with open(args.file, encoding="utf-8") as fh:
            text = fh.read().strip()
    if not text:
        sys.exit("ERROR: give --text or --file.")
    if not args.voice:
        sys.exit("ERROR: give --voice (run --list-voices to find one).")
    if args.skip_existing and os.path.exists(args.out) and os.path.getsize(args.out) > 0:
        print(f"skip (exists): {args.out}")
        return

    synthesize(key, args.voice, text, args.out, args.model, args.stability, args.similarity,
               style=args.style, speed=args.speed, prev_text=args.prev_text,
               next_text=args.next_text, seed=args.seed)


def _selftest():
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".env", delete=False, encoding="utf-8") as fh:
        fh.write('# comment\n\nELEVENLABS_API_KEY = "abc123"\nOTHER=x\n')
        tmp = fh.name
    os.environ.pop("ELEVENLABS_API_KEY", None)
    os.environ.pop("OTHER", None)
    load_env(tmp)
    assert os.environ["ELEVENLABS_API_KEY"] == "abc123", os.environ.get("ELEVENLABS_API_KEY")
    assert os.environ["OTHER"] == "x"
    os.remove(tmp)
    print("selftest OK")


if __name__ == "__main__":
    main()
