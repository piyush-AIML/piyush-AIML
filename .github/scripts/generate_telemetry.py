#!/usr/bin/env python3
"""Generate the contribution "energy field" SVG for the profile README.

Fetches REAL contribution data from GitHub's contribution graph page and
renders it as a glow field: each day is a cell whose brightness maps to
GitHub's own contribution level (0-4). Every render is timestamped in the
image itself. If the fetch fails, an honest OFFLINE placeholder is written
instead — the workflow then has nothing new to commit, so no noise is
created and no data is ever invented.

Run locally too:  python3 .github/scripts/generate_telemetry.py
"""

import argparse
import datetime
import re
import sys
import urllib.request

CELL = 11            # px per day cell
GAP = 4              # px gap between cells
PITCH = CELL + GAP   # 15
WEEKS = 53           # GitHub's graph window
GRID_X, GRID_Y = 40, 78
GRID_W = WEEKS * PITCH - GAP

LEVEL_FILL = {
    0: "#0D1526",
    1: "#0E3A4A",
    2: "#0F5C70",
    3: "#00A9C0",
    4: "#00F7FF",
}

FONT = "'JetBrains Mono','IBM Plex Mono',Consolas,'SF Mono',Menlo,monospace"


def fetch_contributions(user: str) -> list[tuple[datetime.date, int]]:
    url = f"https://github.com/users/{user}/contributions"
    req = urllib.request.Request(
        url, headers={"User-Agent": "piyush-AIML-profile-telemetry/1.0"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        html = resp.read().decode("utf-8", "replace")
    days = []
    for m in re.finditer(
        r'data-date="(\d{4}-\d{2}-\d{2})"[^>]*data-level="([0-4])"', html
    ):
        days.append((datetime.date.fromisoformat(m.group(1)), int(m.group(2))))
    if not days:
        raise RuntimeError("no contribution cells parsed — page shape may have changed")
    return days


def group_weeks(days):
    """Split (date, level) into weeks keyed by (iso-year, iso-week), oldest first."""
    weeks = {}
    for date, level in days:
        iso = date.isocalendar()
        weeks.setdefault((iso[0], iso[1]), []).append((date, level))
    ordered = sorted(weeks.items())
    out = []
    for _, entries in ordered:
        entries.sort()
        row = [0] * 7  # Sunday-first, GitHub style
        for date, level in entries:
            row[(date.weekday() + 1) % 7] = level
        out.append(row)
    return out[-WEEKS:]


def stats(days, today):
    """Honest readouts: active days and streaks, all derived from real data."""
    active = {(d, lvl) for d, lvl in days if lvl > 0}
    active_days = {d for d, _ in active}
    # current streak: count back from today, but allow today to be a zero day
    cursor = today if today in active_days else today - datetime.timedelta(days=1)
    current = 0
    while cursor in active_days:
        current += 1
        cursor -= datetime.timedelta(days=1)
    # longest streak, single pass over the sorted active dates
    longest = run = 0
    prev = None
    for d in sorted(active_days):
        run = run + 1 if prev is not None and (d - prev).days == 1 else 1
        longest = max(longest, run)
        prev = d
    active_365 = sum(1 for d in active_days if (today - d).days < 365)
    return active_365, current, longest


def shell(inner: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 230" width="100%" '
            f'role="img" aria-labelledby="t d"><title id="t">Contribution energy field — '
            f'real GitHub data</title><desc id="d">Each cell is one real day of contributions; '
            f'brightness follows GitHub contribution levels. Regenerated daily by a GitHub '
            f'Action and timestamped in-image.</desc>'
            f'<rect width="1000" height="230" fill="#05070D"/>'
            f'<rect x="20" y="20" width="960" height="190" rx="10" fill="none" stroke="#16243C" '
            f'stroke-width="1"/>{inner}</svg>')


def build_grid(weeks):
    cells = []
    for wk, row in enumerate(weeks):
        for dow, level in enumerate(row):
            x = GRID_X + wk * PITCH
            y = GRID_Y + dow * PITCH
            cells.append(f'<use href="#c{level}" xlink:href="#c{level}" x="{x}" y="{y}"/>')
    return "".join(cells)


def build_readout(x, y, label, value):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="11" letter-spacing="2" '
            f'fill="#5A6B85">{label}</text>'
            f'<text x="{x}" y="{y + 34}" font-family="{FONT}" font-size="32" font-weight="700" '
            f'letter-spacing="2" fill="#00F7FF">{value}</text>')


def render_online(user, today_utc, days):
    weeks = group_weeks(days)
    active_365, current, longest = stats(days, today_utc)
    ts = today_utc.strftime("%Y-%m-%d %H:%M UTC")

    defs = "".join(
        f'<rect id="c{l}" width="{CELL}" height="{CELL}" rx="2" fill="{LEVEL_FILL[l]}"/>'
        for l in range(5)
    )

    body = (
        f'<defs>{defs}</defs>'
        f'<text x="40" y="46" font-family="{FONT}" font-size="15" letter-spacing="3" '
        f'fill="#C9D4E3">// CONTRIBUTION ENERGY FIELD</text>'
        f'<text x="960" y="46" text-anchor="end" font-family="{FONT}" font-size="11" '
        f'letter-spacing="1" fill="#5A6B85">LAST SYNCED: {ts}</text>'
        + build_grid(weeks)
        + f'<line x1="790" y1="70" x2="790" y2="188" stroke="#16243C" stroke-width="1"/>'
        + build_readout(820, 96, "ACTIVE DAYS · 365D", str(active_365))
        + f'<text x="820" y="180" font-family="{FONT}" font-size="11" letter-spacing="2" '
        f'fill="#5A6B85">CURRENT STREAK: {current}</text>'
        + f'<text x="820" y="198" font-family="{FONT}" font-size="11" letter-spacing="2" '
        f'fill="#5A6B85">LONGEST STREAK: {longest}</text>'
        + f'<text x="40" y="196" font-family="{FONT}" font-size="10" letter-spacing="2" '
        f'fill="#3A4A63">REGENERATED DAILY BY GITHUB ACTION</text>'
        + f'<text x="760" y="196" text-anchor="end" font-family="{FONT}" font-size="10" '
        f'letter-spacing="2" fill="#3A4A63">REAL DATA — NOTHING FABRICATED</text>'
    )
    return shell(body), len(days)


def render_offline(today_utc):
    ts = today_utc.strftime("%Y-%m-%d %H:%M UTC")
    body = (
        f'<text x="500" y="140" text-anchor="middle" font-family="{FONT}" font-size="22" '
        f'letter-spacing="4" fill="#E879F9">SYNC OFFLINE</text>'
        f'<text x="500" y="166" text-anchor="middle" font-family="{FONT}" font-size="12" '
        f'letter-spacing="1" fill="#4A5B78">could not reach github.com this cycle — '
        f'retry on the next scheduled run</text>'
        f'<text x="40" y="196" font-family="{FONT}" font-size="10" letter-spacing="2" '
        f'fill="#3A4A63">LAST ATTEMPT: {ts}</text>'
        f'<text x="960" y="196" text-anchor="end" font-family="{FONT}" font-size="10" '
        f'letter-spacing="2" fill="#3A4A63">NO DATA INVENTED</text>'
    )
    return shell(body), 0


def main():
    ap = argparse.ArgumentParser(description="Render real contribution data as an energy field.")
    ap.add_argument("--user", default="piyush-AIML")
    ap.add_argument("--out", default="assets/generated/contributions.svg")
    args = ap.parse_args()

    today_utc = datetime.datetime.now(datetime.timezone.utc).date()
    try:
        days = fetch_contributions(args.user)
        svg, n = render_online(args.user, today_utc, days)
        print(f"ok: {n} days parsed for {args.user} — wrote {args.out}")
    except Exception as exc:  # noqa: BLE001 — deliberate: offline state is a feature
        svg, n = render_offline(today_utc)
        print(f"offline: {exc} — wrote honest placeholder to {args.out}")
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(svg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
