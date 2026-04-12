# SCBKR Memory Index Frontend (`main-root`)

A pure frontend, bilingual (繁中 + English) website for **SCBKR Memory Index**, built for static deployment such as GitHub Pages.

## Run locally

Because this project is static HTML/CSS, you can run it with any static file server:

```bash
cd main-root
python3 -m http.server 8080
```

Then open: <http://localhost:8080>

## Notes

- No backend / no DB / no login / no production API.
- Includes demo route UI for JSON, Google Drive workflow, and OpenClaw local workflow.
- ZIP download button points to a real local starter package: browser-built ZIP from `starter-package/*` (via Download button).
- Starter package includes `DEPLOY_AND_AUTOINDEX.md` and `tools/auto_index.py` to help users deploy and generate index files quickly.
- No committed binary ZIP is required; ZIP is built in-browser to avoid binary compatibility issues in diffs/review pipelines.
