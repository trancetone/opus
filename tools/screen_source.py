#!/usr/bin/env python3
"""Screen a YouTube source against the sourcing criteria before spending Opus credits.

Costs 1 quota unit per call (videos.list). Contrast with search.list at 100.

Usage:
    python3 tools/screen_source.py <url-or-video-id> [more ...]

Requires YOUTUBE_API_KEY in the environment. Set it in the environment
configuration rather than a shell export: session containers are disposable.

Checks, per .claude/skills/yt-sourcing/CRITERIA.md:
  - duration at or above the ten minute floor
  - licence, flagging Creative Commons
  - channel identity, which is the provenance check: an institution's own
    upload versus somebody's copy of it
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request

API = "https://www.googleapis.com/youtube/v3/videos"
MIN_SECONDS = 600  # ten minute source floor


def video_id(s):
    """Accept a watch URL, a youtu.be link, a shorts link, or a bare id."""
    s = s.strip()
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", s):
        return s
    u = urllib.parse.urlparse(s)
    if u.netloc.endswith("youtu.be"):
        return u.path.lstrip("/").split("/")[0]
    q = urllib.parse.parse_qs(u.query).get("v")
    if q:
        return q[0]
    m = re.search(r"/(shorts|embed|v)/([A-Za-z0-9_-]{11})", u.path)
    if m:
        return m.group(2)
    raise ValueError(f"could not extract a video id from {s!r}")


def iso8601_seconds(d):
    """PT1H2M3S -> 3723. Returns None if unparseable."""
    m = re.fullmatch(r"P(?:(\d+)D)?T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", d or "")
    if not m:
        return None
    days, hours, mins, secs = (int(x) if x else 0 for x in m.groups())
    return days * 86400 + hours * 3600 + mins * 60 + secs


def fetch(ids, key):
    params = urllib.parse.urlencode({
        "part": "snippet,contentDetails,status",
        "id": ",".join(ids),
        "key": key,
    })
    with urllib.request.urlopen(f"{API}?{params}", timeout=20) as r:
        return json.load(r)


def main(argv):
    key = os.environ.get("YOUTUBE_API_KEY")
    if not key:
        sys.exit("YOUTUBE_API_KEY is not set. Put it in the environment "
                 "configuration, not a shell export.")
    if not argv:
        sys.exit(__doc__)

    try:
        ids = [video_id(a) for a in argv]
    except ValueError as e:
        sys.exit(str(e))

    data = fetch(ids, key)
    found = {item["id"]: item for item in data.get("items", [])}

    failures = 0
    for vid in ids:
        item = found.get(vid)
        if not item:
            print(f"\n{vid}\n  NOT FOUND (private, deleted, or wrong id)")
            failures += 1
            continue

        snip, content, status = item["snippet"], item["contentDetails"], item.get("status", {})
        secs = iso8601_seconds(content.get("duration"))
        lic = status.get("license", "unknown")

        print(f"\n{snip['title']}")
        print(f"  https://www.youtube.com/watch?v={vid}")
        print(f"  channel   {snip['channelTitle']}  ({snip['channelId']})")
        print(f"  published {snip['publishedAt'][:10]}")

        if secs is None:
            print("  duration  unknown")
        else:
            verdict = "ok" if secs >= MIN_SECONDS else f"BELOW {MIN_SECONDS // 60} MIN FLOOR"
            print(f"  duration  {secs // 60}m {secs % 60}s  [{verdict}]")
            if secs < MIN_SECONDS:
                failures += 1

        print(f"  licence   {lic}" + ("  [Creative Commons]" if lic == "creativeCommon" else ""))
        print("  provenance: confirm the channel above is the institution itself. "
              "A copy is not an official upload.")

    print()
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
