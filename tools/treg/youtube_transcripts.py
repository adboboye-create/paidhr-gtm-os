#!/usr/bin/env python3
"""Pull YouTube transcripts via treg and save one Markdown file per video.

Usage:
  python3 tools/treg/youtube_transcripts.py VIDEO_ID [VIDEO_ID ...] --out DIR
  python3 tools/treg/youtube_transcripts.py --channel GetPaidHR --list   # list videos only

Cost (treg catalog, 2026-11-11): $0.00188 per transcript or channel page
(scrapecreators). Cached results (newer than --cache-days, default 30d) cost $0.
Transcripts are YouTube auto-captions: verify names and numbers before quoting.
"""
import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
TREG = os.path.join(HERE, "treg.sh")


def treg_call(endpoint, *queries):
    cmd = [TREG, "call", endpoint]
    for q in queries:
        cmd += ["--query", q]
    res = subprocess.run(cmd, capture_output=True, text=True)
    cost = re.findall(r"charged \$[0-9.]+", res.stderr)
    if res.returncode != 0 or not res.stdout.strip():
        sys.exit(f"treg call failed for {endpoint}: {res.stderr.strip()[-300:]}")
    return json.loads(res.stdout), (cost[-1] if cost else "charged $0 (cached or free)")


def title_of(vid):
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    try:
        with urllib.request.urlopen(url, timeout=15) as r:
            return json.load(r)["title"]
    except Exception:
        pass
    # Fallback: python.org builds on macOS often lack SSL certs; system curl works.
    try:
        out = subprocess.run(["curl", "-fsS", "--max-time", "15", url], capture_output=True, text=True)
        return json.loads(out.stdout)["title"]
    except Exception:
        return vid


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]


def paragraphs(segments, block_ms=30000):
    out, cur, start, t0 = [], [], None, 0
    for s in segments:
        ms = int(s["startMs"])
        if start is None:
            start, t0 = s["startTimeText"], ms
        cur.append(s["text"].strip())
        if ms - t0 >= block_ms:
            out.append(f"**[{start}]** " + " ".join(cur))
            cur, start = [], None
    if cur:
        out.append(f"**[{start}]** " + " ".join(cur))
    # house rule: no em dashes
    return "\n\n".join(out).replace("—", ", ")


def list_channel(handle):
    token, n = None, 0
    while True:
        q = [f"handle={handle}"] + ([f"continuationToken={token}"] if token else [])
        d, cost = treg_call("scrapecreators.x.v1-youtube-channel-videos", *q)
        print(f"# page ({cost})", file=sys.stderr)
        for v in d.get("videos") or []:
            n += 1
            print(f"{v.get('id')} | {v.get('publishedTimeText')} | {v.get('lengthText')} | {v.get('title')}")
        token = d.get("continuationToken")
        if not token:
            break
    print(f"# {n} videos", file=sys.stderr)


def transcribe(vid, out_dir, cache_days):
    d, cost = treg_call(
        "scrapecreators.x.v1-youtube-video-transcript",
        f"url=https://www.youtube.com/watch?v={vid}",
        f"cache_max_age={cache_days}",
    )
    segs = d.get("transcript") or []
    title = title_of(vid)
    path = os.path.join(out_dir, f"{vid}-{slug(title)}.md")
    today = datetime.date.today().isoformat()
    with open(path, "w") as f:
        f.write(
            f"# {title}\n\n"
            f"- **Video:** https://www.youtube.com/watch?v={vid}\n"
            f"- **Transcript source:** YouTube auto-captions (language: {d.get('language')}), via treg (scrapecreators) on {today}.\n"
            f"- **Accuracy warning:** auto-captions. Verify names, brands and numbers against the video before quoting.\n\n"
            f"## Raw transcript (timestamped, ~30s blocks)\n\n{paragraphs(segs)}\n"
        )
    print(f"{vid}: {len(segs)} segments, {cost} -> {path}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("ids", nargs="*", help="YouTube video IDs")
    p.add_argument("--out", default="context/docs/research/customer-videos/transcripts")
    p.add_argument("--channel", help="channel handle without @, e.g. GetPaidHR")
    p.add_argument("--list", action="store_true", help="list channel videos and exit")
    p.add_argument("--cache-days", default="30d", choices=["1d", "3d", "7d", "14d", "30d"],
                   help="reuse a cached transcript newer than this at $0 (default 30d)")
    a = p.parse_args()
    if a.channel and a.list:
        return list_channel(a.channel)
    if not a.ids:
        p.error("give video IDs, or --channel HANDLE --list")
    os.makedirs(a.out, exist_ok=True)
    for vid in a.ids:
        transcribe(vid, a.out, a.cache_days)


if __name__ == "__main__":
    main()
