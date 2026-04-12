# SCBKR Starter: Deploy + Auto Index Guide

## 1) Fast local run (no backend)

### Option A: Python static server
```bash
cd main-root
python3 -m http.server 8080
```
Open: http://localhost:8080

### Option B: GitHub Pages
1. Push repo to GitHub.
2. Settings → Pages.
3. Deploy from branch and set folder to `main-root`.

---

## 2) Auto build SCBKR index from your files

This starter includes `tools/auto_index.py`.

### Run
```bash
cd starter-package
python3 tools/auto_index.py --source ./memory-index --output ./memory-index/index.scbkr.generated.json
```

### What it does
- Scans files under `memory-index/`.
- Creates SCBKR entries with simple defaults:
  - `S`: file name
  - `C`: source path context
  - `B`: default local-boundary note
  - `K`: file path + modified timestamp
  - `R`: `user-owner`
- Builds simple route tags by folder keyword (`json`, `drive`, `local`, etc.).

You can then edit generated fields manually or let your own model enrich them.

---

## 3) Suggested workflow
1. Put memory files in `memory-index/json`, `memory-index/drive-import`, `memory-index/local-private`.
2. Run auto-index script.
3. Connect your own model / orchestration to perform recall, route, replay.
4. Keep governance logic in your own private layer.
