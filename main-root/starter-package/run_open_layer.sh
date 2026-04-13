#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

python3 tools/auto_index.py \
  --source ./memory-index \
  --output ./memory-index/index.scbkr.generated.json

python3 tools/scbkr_human_gate.py \
  --index ./memory-index/index.scbkr.generated.json \
  --report ./memory-index/index.scbkr.gate-report.json \
  --decision-ready-output ./memory-index/index.scbkr.decision-ready.json

echo "Open-layer index ready: ./memory-index/index.scbkr.decision-ready.json"
echo "To start local API:"
echo "  python3 services/scbkr_api_server.py --index ./memory-index/index.scbkr.decision-ready.json --port 9000"
