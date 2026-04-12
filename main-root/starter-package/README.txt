SCBKR Memory Index Starter Package

This ZIP contains the open indexing layer starter structure (not the closed governance core).

Quick start:
1) Put your memory files into memory-index/json, drive-import, or local-private.
2) Run the auto-index script to generate an SCBKR index file.
3) Connect your own model/tooling to route and replay indexed memory.

Commands:
- cd starter-package
- python3 tools/auto_index.py --source ./memory-index --output ./memory-index/index.scbkr.generated.json

Deploy guide:
- Read DEPLOY_AND_AUTOINDEX.md for local run + GitHub Pages steps.

SCBKR
- S = Subject
- C = Cause
- B = Boundary
- K = Key Evidence
- R = Responsibility
