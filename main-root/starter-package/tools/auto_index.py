#!/usr/bin/env python3
"""Generate a basic SCBKR index from local memory files.

Usage:
  python3 tools/auto_index.py --source ./memory-index --output ./memory-index/index.scbkr.generated.json
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path

SKIP_DIRS = {".git", "__pycache__"}
SKIP_FILES = {"index.scbkr.json", "index.scbkr.generated.json"}


@dataclass
class MemoryItem:
    id: str
    S: str
    C: str
    B: str
    K: list[str]
    R: str
    route: str


def infer_route(path: Path) -> str:
    lower = str(path).lower()
    if "drive" in lower:
        return "cloud-drive-lane"
    if "local" in lower:
        return "local-private-lane"
    if "json" in lower:
        return "json-memory-lane"
    return "general-memory-lane"


def iter_files(root: Path):
    for p in root.rglob("*"):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if p.is_file() and p.name not in SKIP_FILES:
            yield p


def build_item(root: Path, file_path: Path, idx: int) -> MemoryItem:
    rel = file_path.relative_to(root)
    stat = file_path.stat()
    modified = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat()
    return MemoryItem(
        id=f"mem-{idx:05d}",
        S=file_path.stem,
        C=f"Imported from {rel.parent}",
        B="Local indexing only; governance decisions handled outside open layer.",
        K=[f"file:{rel.as_posix()}", f"modified:{modified}"],
        R="user-owner",
        route=infer_route(rel),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Auto-generate SCBKR index JSON")
    parser.add_argument("--source", required=True, help="Folder to scan")
    parser.add_argument("--output", required=True, help="Output JSON path")
    args = parser.parse_args()

    source = Path(args.source).resolve()
    output = Path(args.output).resolve()

    if not source.exists() or not source.is_dir():
        raise SystemExit(f"source folder not found: {source}")

    files = sorted(iter_files(source))
    items = [asdict(build_item(source, f, i + 1)) for i, f in enumerate(files)]

    payload = {
        "schema": "SCBKR-1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": str(source),
        "count": len(items),
        "items": items,
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Generated {len(items)} item(s) -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
