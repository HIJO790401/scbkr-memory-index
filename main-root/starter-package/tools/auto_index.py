#!/usr/bin/env python3
"""Generate a basic SCBKR index from local memory files.

Usage examples:
  python3 tools/auto_index.py \
    --source ./memory-index \
    --output ./memory-index/index.scbkr.generated.json

  python3 tools/auto_index.py \
    --source ./memory-index \
    --output ./memory-index/index.scbkr.generated.json \
    --default-owner "Shen-Yao 888π / Wen-Yao Hsu"
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

# Folders/files to skip while scanning user memory sources.
SKIP_DIRS = {".git", "__pycache__"}
SKIP_FILES = {"index.scbkr.json", "index.scbkr.generated.json"}
DEFAULT_OWNER = "user-owner"


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


def build_item(root: Path, file_path: Path, idx: int, default_owner: str) -> MemoryItem:
    rel = file_path.relative_to(root)
    stat = file_path.stat()
    modified = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat()

    # Demo-safe fallback: owner/responsibility remains explicit and human-chosen.
    owner = default_owner.strip() if default_owner.strip() else DEFAULT_OWNER

    return MemoryItem(
        id=f"mem-{idx:05d}",
        S=file_path.stem,
        C=f"Imported from {rel.parent}",
        B="Local indexing only; governance decisions handled outside open layer.",
        K=[f"file:{rel.as_posix()}", f"modified:{modified}"],
        R=owner,
        route=infer_route(rel),
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Auto-generate a SCBKR index JSON from local files. "
            "This tool is for open indexing-layer demos, not final governance judgment."
        )
    )
    parser.add_argument("--source", required=True, help="Folder to scan for memory files")
    parser.add_argument("--output", required=True, help="Output JSON path for generated index")
    parser.add_argument(
        "--default-owner",
        default=DEFAULT_OWNER,
        help=(
            "Optional default owner for SCBKR R (Responsibility) field. "
            "Example: --default-owner 'Shen-Yao 888π / Wen-Yao Hsu'"
        ),
    )
    args = parser.parse_args()

    source = Path(args.source).resolve()
    output = Path(args.output).resolve()

    if not source.exists() or not source.is_dir():
        raise SystemExit(f"source folder not found: {source}")

    files = sorted(iter_files(source))
    items = [asdict(build_item(source, f, i + 1, args.default_owner)) for i, f in enumerate(files)]

    payload = {
        "schema": "SCBKR-1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": str(source),
        "count": len(items),
        "default_owner": args.default_owner,
        "items": items,
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Generated {len(items)} item(s) -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
