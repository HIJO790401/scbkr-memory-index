#!/usr/bin/env python3
"""Build an experimental lookup-friendly index from generated SCBKR JSON.

This is an early utility for the open indexing layer. It is intentionally simple
and intended as a starting point for future query optimization work.

Capabilities (prototype-level):
- Route lookup map
- Date lookup map (YYYY-MM-DD extracted from evidence/metadata)
- Keyword lookup map (lightweight tokenization from S/C/B/K/R)
- Responsibility (R-field) lookup map

Example:
  python3 tools/build_optimized_index.py \
    --source ./memory-index/index.scbkr.generated.json \
    --output ./memory-index/index.scbkr.optimized.json
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

WORD_RE = re.compile(r"[A-Za-z0-9_\-]{2,}")
DATE_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")


def load_source(path: Path) -> dict[str, Any]:
    if not path.exists() or not path.is_file():
        raise SystemExit(f"source JSON not found: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON input: {path} ({exc})") from exc


def normalize(value: str) -> str:
    return value.strip().lower()


def collect_dates(item: dict[str, Any]) -> set[str]:
    dates: set[str] = set()
    for evidence in item.get("K", []):
        if not isinstance(evidence, str):
            continue
        for found in DATE_RE.findall(evidence):
            dates.add(found)
    return dates


def collect_keywords(item: dict[str, Any]) -> set[str]:
    parts: list[str] = []
    for field in ("S", "C", "B", "R", "route"):
        value = item.get(field)
        if isinstance(value, str):
            parts.append(value)
    for evidence in item.get("K", []):
        if isinstance(evidence, str):
            parts.append(evidence)

    tokens = {normalize(tok) for tok in WORD_RE.findall(" ".join(parts))}
    return {tok for tok in tokens if len(tok) >= 2}


def build_optimized(payload: dict[str, Any]) -> dict[str, Any]:
    items = payload.get("items")
    if not isinstance(items, list):
        raise SystemExit("input JSON missing list field: items")

    by_route: dict[str, list[str]] = defaultdict(list)
    by_date: dict[str, list[str]] = defaultdict(list)
    by_keyword: dict[str, list[str]] = defaultdict(list)
    by_responsibility: dict[str, list[str]] = defaultdict(list)
    id_to_item: dict[str, dict[str, Any]] = {}

    for item in items:
        if not isinstance(item, dict):
            continue
        item_id = str(item.get("id", "")).strip()
        if not item_id:
            continue
        id_to_item[item_id] = item

        route = normalize(str(item.get("route", "general-memory-lane")))
        by_route[route].append(item_id)

        responsibility = normalize(str(item.get("R", "")))
        if responsibility:
            by_responsibility[responsibility].append(item_id)

        for date in collect_dates(item):
            by_date[date].append(item_id)

        for keyword in collect_keywords(item):
            by_keyword[keyword].append(item_id)

    meta = {
        "experimental": True,
        "note": (
            "Early utility for lookup-oriented indexing. "
            "Not a finalized performance engine."
        ),
        "built_at": datetime.now(timezone.utc).isoformat(),
        "source_schema": payload.get("schema", "unknown"),
        "source_count": len(id_to_item),
    }

    return {
        "meta": meta,
        "lookups": {
            "by_route": dict(by_route),
            "by_date": dict(by_date),
            "by_keyword": dict(by_keyword),
            "by_responsibility": dict(by_responsibility),
        },
        "items_by_id": id_to_item,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Build an experimental optimized lookup JSON from SCBKR generated index. "
            "Prototype utility for future query optimization work."
        )
    )
    parser.add_argument("--source", required=True, help="Input generated index JSON path")
    parser.add_argument("--output", required=True, help="Output optimized JSON path")
    args = parser.parse_args()

    source = Path(args.source).resolve()
    output = Path(args.output).resolve()

    payload = load_source(source)
    optimized = build_optimized(payload)

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(optimized, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Built optimized index -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
