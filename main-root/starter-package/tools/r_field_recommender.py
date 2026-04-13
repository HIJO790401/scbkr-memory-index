#!/usr/bin/env python3
"""Experimental R-field recommender for SCBKR items.

This tool provides lightweight heuristic suggestions for the Responsibility (R)
field. It does NOT modify source files and does NOT auto-assign final ownership.
User review is always required.

Heuristic inputs:
- filename clues from K evidence (e.g., file:path)
- subject / cause / boundary text
- evidence text
- route name

Example:
  python3 tools/r_field_recommender.py \
    --source ./memory-index/index.scbkr.generated.json \
    --output ./memory-index/r-field.suggestions.json
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


RULES: list[tuple[str, str, str]] = [
    ("ops", "Ops Lead", "ops-related keyword"),
    ("incident", "Ops Lead", "incident signal"),
    ("policy", "Compliance Owner", "policy signal"),
    ("legal", "Compliance Owner", "legal signal"),
    ("finance", "Finance Owner", "finance signal"),
    ("billing", "Finance Owner", "billing signal"),
    ("medical", "Healthcare Owner", "medical signal"),
    ("health", "Healthcare Owner", "health signal"),
    ("engineering", "Engineering Lead", "engineering signal"),
    ("release", "Engineering Lead", "release signal"),
]


def load_items(path: Path) -> list[dict[str, Any]]:
    if not path.exists() or not path.is_file():
        raise SystemExit(f"source JSON not found: {path}")

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON input: {path} ({exc})") from exc

    items = payload.get("items")
    if not isinstance(items, list):
        raise SystemExit("input JSON missing list field: items")
    return [x for x in items if isinstance(x, dict)]


def extract_text(item: dict[str, Any]) -> str:
    chunks: list[str] = []
    for key in ("S", "C", "B", "route"):
        val = item.get(key)
        if isinstance(val, str):
            chunks.append(val)
    for evidence in item.get("K", []):
        if isinstance(evidence, str):
            chunks.append(evidence)
            file_match = re.search(r"file:([^\s]+)", evidence)
            if file_match:
                chunks.append(file_match.group(1))
    return " ".join(chunks).lower()


def confidence_label(score: int) -> str:
    if score >= 3:
        return "high"
    if score == 2:
        return "medium"
    return "low"


def suggest_candidates(item: dict[str, Any], top_n: int = 3) -> list[dict[str, Any]]:
    text = extract_text(item)
    hits: Counter[str] = Counter()
    reasons: dict[str, set[str]] = {}

    for keyword, owner, reason in RULES:
        if keyword in text:
            hits[owner] += 1
            reasons.setdefault(owner, set()).add(f"{keyword}: {reason}")

    # route-based extra nudges
    route = str(item.get("route", "")).lower()
    if "local" in route:
        hits["Local Data Steward"] += 1
        reasons.setdefault("Local Data Steward", set()).add("route: local")
    if "drive" in route:
        hits["Cloud Document Owner"] += 1
        reasons.setdefault("Cloud Document Owner", set()).add("route: drive")

    suggestions: list[dict[str, Any]] = []
    for owner, score in hits.most_common(top_n):
        suggestions.append(
            {
                "candidate": owner,
                "heuristic_score": score,
                "confidence": confidence_label(score),
                "notes": sorted(reasons.get(owner, set())),
            }
        )

    if not suggestions:
        suggestions.append(
            {
                "candidate": "Manual Review Required",
                "heuristic_score": 0,
                "confidence": "low",
                "notes": ["No clear heuristic signals found"],
            }
        )

    return suggestions


def build_output(items: list[dict[str, Any]]) -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    for item in items:
        item_id = str(item.get("id", "unknown"))
        results.append(
            {
                "id": item_id,
                "current_r": item.get("R", ""),
                "user_review_required": True,
                "candidates": suggest_candidates(item),
            }
        )

    return {
        "experimental": True,
        "note": (
            "Prototype heuristic recommender. Suggestions only; do not auto-assign "
            "Responsibility without human review."
        ),
        "count": len(results),
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Generate experimental R-field suggestion candidates from SCBKR index JSON. "
            "This tool does not modify source data."
        )
    )
    parser.add_argument("--source", required=True, help="Input generated index JSON path")
    parser.add_argument("--output", required=True, help="Output suggestions JSON path")
    args = parser.parse_args()

    source = Path(args.source).resolve()
    output = Path(args.output).resolve()

    items = load_items(source)
    payload = build_output(items)

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote R-field suggestions -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
