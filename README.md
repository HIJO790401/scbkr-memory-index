# scbkr-memory-index

Public-facing frontend project for **SCBKR Memory Index**.

## What this is / 專案定位

SCBKR Memory Index is an **open indexing layer** for long-term AI memory organization.
It is designed for structured indexing, replayability, auditability, and routing.

SCBKR 記憶庫索引是面向長期 AI 記憶組織的**開放式索引層**，重點是結構化索引、可重播、可稽核與可路由。

The public site is a fixed structured showcase (not a freeform playground).
公開網站為固定結構化示範（不是自由輸入沙盒）。

> This is **not** a full governance engine and does not include the closed governance/judgment core.
>
> 本專案**不是**完整治理引擎，不包含封閉治理/判斷核心。

## Why this is not just memory storage / 為何不只是記憶儲存

This project does not only store memory files; it organizes memory with SCBKR fields so recall can be replayed,
audited, and routed with clear responsibility traces.

本專案不只是把資料存起來，而是透過 SCBKR 欄位建立可重播、可稽核、可路由的記憶索引。

> The R field is not automatically equivalent to truth. Responsibility should not be silently replaced by an algorithm; users should consciously decide who bears each memory item.
>
> 「R 欄位不是自動等於真相。責任不該被演算法悄悄取代；使用者應在使用前，明確決定每筆記憶由誰承擔。」

## Project map / 路徑說明

- `repo root/` (this folder): overall source root.
- `main-root/`: static public frontend (GitHub Pages target).
- `main-root/starter-package/`: downloadable starter data + `auto_index.py` utility.

## Deploy frontend / 部署前端

1. Push repository to GitHub.
2. Open **Settings → Pages**.
3. Publish from branch/folder and set folder to `main-root`.

Local preview:

```bash
cd main-root
python3 -m http.server 8080
```

Then open: <http://localhost:8080>


## Practical usage / 實際使用路徑

If your goal is to actually use memory indexing (not just view the webpage), start here:

```bash
cd main-root/starter-package
python3 tools/auto_index.py --source ./memory-index --output ./memory-index/index.scbkr.generated.json
```

Use files under `main-root/starter-package/memory-index/` as your working memory source folders.
