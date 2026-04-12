# SCBKR Memory Index Frontend (`main-root`)

A pure frontend, bilingual (繁中 + English) website for **SCBKR Memory Index**, built for static deployment such as GitHub Pages.

## Run locally

Because this project is static HTML/CSS, you can run it with any static file server:

```bash
cd main-root
python3 -m http.server 8080
```

Then open: <http://localhost:8080>

## Deploy (GitHub Pages)

1. Push the repository to GitHub.
2. Open **Settings → Pages**.
3. Publish from branch/folder and set folder to `main-root`.

## Notes

- No backend / no DB / no login / no production API.
- Includes demo route UI for JSON, Google Drive workflow, and OpenClaw local workflow.
- Download button on homepage points to repository ZIP.
- After unzipping, deploy the static frontend from `main-root/`.


## If your goal is memory indexing usage / 如果你的目標是實際使用記憶索引

Do not start from frontend styling files. Start from:

```bash
cd main-root/starter-package
python3 tools/auto_index.py --source ./memory-index --output ./memory-index/index.scbkr.generated.json
```

Working folders:
- `memory-index/json/`
- `memory-index/drive-import/`
- `memory-index/local-private/`
