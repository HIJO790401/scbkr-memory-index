#!/usr/bin/env python3
"""Experimental SCBKR LLM bridge (initial utility).

This module is a starting point for integration only. It does not call OpenAI,
Claude, or any provider API directly. Instead, it provides generic helpers to:
- load index JSON
- search top relevant memory items
- build prompt payload data for your own adapter

Use this as a prototype bridge skeleton for the open indexing layer.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

TOKEN_RE = re.compile(r"[a-zA-Z0-9_\-]{2,}")


def load_index(index_path: str | Path) -> dict[str, Any]:
    path = Path(index_path)
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"Index file not found: {path}")

    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload.get("items"), list):
        raise ValueError("Invalid index format: missing list field 'items'")
    return payload


def _item_search_text(item: dict[str, Any]) -> str:
    parts: list[str] = []
    for field in ("S", "C", "B", "R", "route"):
        value = item.get(field)
        if isinstance(value, str):
            parts.append(value)
    for evidence in item.get("K", []):
        if isinstance(evidence, str):
            parts.append(evidence)
    return " ".join(parts).lower()


def search_memories(index_payload: dict[str, Any], query: str, top_k: int = 5) -> list[dict[str, Any]]:
    query_terms = {t.lower() for t in TOKEN_RE.findall(query)}
    if not query_terms:
        return []

    scored: list[tuple[int, dict[str, Any]]] = []
    for item in index_payload.get("items", []):
        if not isinstance(item, dict):
            continue
        text = _item_search_text(item)
        score = sum(1 for term in query_terms if term in text)
        if score > 0:
            scored.append((score, item))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [item for _, item in scored[: max(1, top_k)]]


def build_prompt_payload(query: str, relevant_items: list[dict[str, Any]]) -> dict[str, Any]:
    memory_context = []
    for item in relevant_items:
        memory_context.append(
            {
                "id": item.get("id"),
                "S": item.get("S"),
                "C": item.get("C"),
                "B": item.get("B"),
                "K": item.get("K", []),
                "R": item.get("R"),
                "route": item.get("route"),
            }
        )

    system_note = (
        "Experimental bridge payload from SCBKR open indexing layer. "
        "Use as context input; final governance/judgment remains external."
    )

    return {
        "experimental": True,
        "system_note": system_note,
        "query": query,
        "memory_context": memory_context,
    }


def _cli() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Experimental SCBKR LLM bridge CLI. "
            "Builds a generic prompt payload from query + index."
        )
    )
    parser.add_argument("--index", required=True, help="Path to SCBKR index JSON")
    parser.add_argument("--query", required=True, help="User query")
    parser.add_argument("--top-k", type=int, default=5, help="Top relevant items to include")
    parser.add_argument("--output", help="Optional output JSON path for prompt payload")
    args = parser.parse_args()

    payload = load_index(args.index)
    relevant = search_memories(payload, args.query, top_k=args.top_k)
    prompt_payload = build_prompt_payload(args.query, relevant)

    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(prompt_payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Wrote payload -> {out}")
    else:
        print(json.dumps(prompt_payload, ensure_ascii=False, indent=2))

    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
