#!/usr/bin/env python3
"""Best-effort downloader for known paper metadata/full-text URLs.

This script intentionally avoids non-standard dependencies. It downloads only URLs
that are already listed in this repository and writes small status logs so failed
publisher downloads remain auditable.
"""
from __future__ import annotations

import csv
import ssl
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "download_attempts.csv"
LOG = ROOT / "papers" / "downloads" / "download-log.md"

HEADERS = {"User-Agent": "Mozilla/5.0 academic-misconduct-evidence-archive/0.1"}
SKIP_STATUSES = {"not_attempted", "downloaded"}


def fetch(url: str, dest: Path) -> tuple[str, str]:
    if url == "待补充" or not url.startswith(("http://", "https://")):
        return "not_attempted", "missing URL"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30, context=ssl.create_default_context()) as response:
            data = response.read()
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            return "downloaded", f"HTTP {response.status}; {len(data)} bytes"
    except urllib.error.HTTPError as exc:
        return "failed", f"HTTP {exc.code}: {exc.reason}"
    except Exception as exc:  # noqa: BLE001 - this is a diagnostic downloader
        return "failed", f"{type(exc).__name__}: {exc}"


def main() -> int:
    rows = list(csv.DictReader(MANIFEST.open(encoding="utf-8")))
    lines = ["# Download log", "", "Best-effort run for known paper URLs.", ""]
    updated = []
    for row in rows:
        status = row["status"]
        if status in SKIP_STATUSES or row["url"] == "待补充":
            lines.append(f"- SKIP `{row['person_id']}` `{row['paper_id']}` `{row['item_type']}`: {status} ({row['notes']})")
            updated.append(row)
            continue
        dest = ROOT / row["local_path"]
        new_status, note = fetch(row["url"], dest)
        row["status"] = new_status
        row["notes"] = note
        lines.append(f"- {new_status.upper()} `{row['person_id']}` `{row['paper_id']}` `{row['item_type']}`: {note}")
        updated.append(row)
    with MANIFEST.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(updated)
    LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
