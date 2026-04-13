#!/usr/bin/env python3
"""Human decision gate for SCBKR memory items.

Purpose:
- Enforce a responsibility-chain checkpoint before memory is used for decisions.
- Mark each item as `decision_ready` or `review_required`.
- Optionally export a filtered index with decision-ready items only.

This tool does NOT auto-decide truth. It provides a strict cutoff workflow where
human accountability remains required.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

BLOCKLIST_R = {"", "manual review required", "unknown"}


def load_index(path: Path) -> dict[str, Any]:
    if not path.exists() or not path.is_file():
        raise SystemExit(f"index file not found: {path}")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON: {path} ({exc})") from exc

    if not isinstance(payload.get("items"), list):
        raise SystemExit("input JSON missing items list")
    return payload


def evaluate_item(item: dict[str, Any]) -> dict[str, Any]:
    reasons: list[str] = []

    boundary = str(item.get("B", "")).strip()
    if not boundary:
        reasons.append("missing_boundary")

    responsibility = str(item.get("R", "")).strip().lower()
    if responsibility in BLOCKLIST_R:
        reasons.append("unresolved_responsibility")

    evidence = [x for x in item.get("K", []) if isinstance(x, str) and x.strip()]
    if len(evidence) == 0:
        reasons.append("missing_evidence")

    status = "decision_ready" if len(reasons) == 0 else "review_required"
    return {
        "id": item.get("id"),
        "status": status,
        "reasons": reasons,
        "current_r": item.get("R", ""),
    }


def build_reports(payload: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    items = [x for x in payload.get("items", []) if isinstance(x, dict)]

    evaluations = [evaluate_item(item) for item in items]
    ready_ids = {str(e["id"]) for e in evaluations if e["status"] == "decision_ready"}

    review_report = {
        "experimental": True,
        "purpose": "responsibility-chain human gate",
        "count": len(evaluations),
        "decision_ready_count": len(ready_ids),
        "review_required_count": len(evaluations) - len(ready_ids),
        "evaluations": evaluations,
    }

    filtered_index = {
        **payload,
        "gate": {
            "mode": "decision_ready_only",
            "decision_ready_count": len(ready_ids),
            "review_required_count": len(evaluations) - len(ready_ids),
        },
        "items": [item for item in items if str(item.get("id")) in ready_ids],
    }

    return review_report, filtered_index


def main() -> int:
    parser = argparse.ArgumentParser(description="Run SCBKR human decision gate checks")
    parser.add_argument("--index", required=True, help="Path to generated SCBKR index JSON")
    parser.add_argument("--report", required=True, help="Path to gate report JSON")
    parser.add_argument(
        "--decision-ready-output",
        help="Optional path to write filtered decision-ready index JSON",
    )
    args = parser.parse_args()

    index_path = Path(args.index).resolve()
    report_path = Path(args.report).resolve()

    payload = load_index(index_path)
    report, filtered = build_reports(payload)

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote gate report -> {report_path}")

    if args.decision_ready_output:
        out = Path(args.decision_ready_output).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(filtered, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Wrote decision-ready index -> {out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
