#!/usr/bin/env python3
"""Experimental SCBKR query API server (deployment-oriented baseline).

This service exposes minimal REST endpoints for local integration:
- GET  /health
- POST /query

Boundary notes:
- This is still part of the open indexing layer.
- It does not implement full governance engine behavior.
- Decision-ready filtering is conservative and rule-based.
"""

from __future__ import annotations

import argparse
import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

from scbkr_llm_bridge import load_index, search_memories

DEFAULT_BLOCKLIST_R = {"", "manual review required", "unknown"}


def is_decision_ready(item: dict[str, Any]) -> bool:
    boundary = str(item.get("B", "")).strip()
    responsibility = str(item.get("R", "")).strip().lower()
    evidence = [x for x in item.get("K", []) if isinstance(x, str) and x.strip()]

    if not boundary:
        return False
    if responsibility in DEFAULT_BLOCKLIST_R:
        return False
    if len(evidence) == 0:
        return False
    return True


class APIServer(BaseHTTPRequestHandler):
    index_payload: dict[str, Any] = {}

    def _send_json(self, payload: dict[str, Any], status: HTTPStatus = HTTPStatus.OK) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        if self.path == "/health":
            self._send_json({"status": "ok", "service": "scbkr-api", "experimental": True})
            return
        self._send_json({"error": "not found"}, status=HTTPStatus.NOT_FOUND)

    def do_POST(self) -> None:  # noqa: N802
        if self.path != "/query":
            self._send_json({"error": "not found"}, status=HTTPStatus.NOT_FOUND)
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            data = json.loads(self.rfile.read(length) if length > 0 else b"{}")
        except json.JSONDecodeError:
            self._send_json({"error": "invalid json payload"}, status=HTTPStatus.BAD_REQUEST)
            return

        query = str(data.get("query", "")).strip()
        if not query:
            self._send_json({"error": "query is required"}, status=HTTPStatus.BAD_REQUEST)
            return

        top_k = max(1, int(data.get("top_k", 5)))
        filter_r = str(data.get("filter_by_responsibility", "")).strip().lower()
        require_decision_ready = bool(data.get("require_decision_ready", True))

        raw = search_memories(self.index_payload, query, top_k=max(top_k * 3, top_k))

        results: list[dict[str, Any]] = []
        for item in raw:
            current_r = str(item.get("R", "")).strip().lower()
            if filter_r and current_r != filter_r:
                continue
            if require_decision_ready and not is_decision_ready(item):
                continue
            results.append(item)
            if len(results) >= top_k:
                break

        self._send_json(
            {
                "status": "success",
                "experimental": True,
                "query": query,
                "top_k": top_k,
                "require_decision_ready": require_decision_ready,
                "count": len(results),
                "results": results,
            }
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Run experimental SCBKR REST query API server")
    parser.add_argument("--index", required=True, help="Path to SCBKR index JSON")
    parser.add_argument("--host", default="127.0.0.1", help="Bind host")
    parser.add_argument("--port", type=int, default=9000, help="Bind port")
    args = parser.parse_args()

    index_path = Path(args.index).resolve()
    APIServer.index_payload = load_index(index_path)

    server = ThreadingHTTPServer((args.host, args.port), APIServer)
    print(f"SCBKR API server running on http://{args.host}:{args.port} (experimental)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
