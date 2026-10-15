#!/usr/bin/env python3
"""Generate the narration, one file per segment, with word timings.

    python tools/tts.py ar        # or: en
    python tools/tts.py ar a4     # regenerate one segment only

Reads voice/script.<lang>.json and writes build/voice/<lang>/<id>.mp3 and
<id>.json (the words, with start and end in seconds). Uses Microsoft's neural
voices through the edge-tts package (pip install edge-tts). Behind a proxy,
HTTPS_PROXY is passed through.
"""
import asyncio
import json
import os
import subprocess
import sys
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parent.parent
TICKS = 10_000_000  # edge-tts offsets are in 100 ns units


def probe_duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(path)],
        capture_output=True, text=True, check=True).stdout
    return float(out.strip())


async def synth(seg, cfg, out_dir):
    comm = edge_tts.Communicate(
        seg["say"], cfg["voice"], rate=cfg.get("rate", "+0%"),
        pitch=cfg.get("pitch", "+0Hz"), boundary="WordBoundary",
        proxy=os.environ.get("HTTPS_PROXY"))
    audio, words = bytearray(), []
    async for chunk in comm.stream():
        if chunk["type"] == "audio":
            audio += chunk["data"]
        elif chunk["type"] == "WordBoundary":
            start = chunk["offset"] / TICKS
            words.append({"text": chunk["text"], "start": round(start, 3),
                          "end": round(start + chunk["duration"] / TICKS, 3)})
    mp3 = out_dir / f"{seg['id']}.mp3"
    mp3.write_bytes(audio)
    meta = {"id": seg["id"], "say": seg["say"], "voice": cfg["voice"],
            "rate": cfg.get("rate"), "pitch": cfg.get("pitch"),
            "duration": round(probe_duration(mp3), 3), "words": words}
    (out_dir / f"{seg['id']}.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    return meta


async def main(lang, only=None):
    cfg = json.loads((ROOT / "voice" / f"script.{lang}.json").read_text(encoding="utf-8"))
    out_dir = ROOT / "build" / "voice" / lang
    out_dir.mkdir(parents=True, exist_ok=True)
    total = 0.0
    for seg in cfg["segments"]:
        if only and seg["id"] not in only:
            continue
        for attempt in range(4):
            try:
                meta = await synth(seg, cfg, out_dir)
                break
            except Exception as err:  # the service drops connections now and then
                print(f"  retry {seg['id']}: {err}")
                await asyncio.sleep(2 ** attempt)
        else:
            raise SystemExit(f"could not synthesize {seg['id']}")
        speech = meta["words"][-1]["end"] if meta["words"] else meta["duration"]
        total += speech + seg.get("gap", 0.4)
        print(f"{seg['id']:>4}  {meta['duration']:6.2f}s file  {speech:6.2f}s speech  {len(meta['words'])} words")
    print(f"total ≈ {total:.1f}s of narration")


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1], set(sys.argv[2:]) or None))
