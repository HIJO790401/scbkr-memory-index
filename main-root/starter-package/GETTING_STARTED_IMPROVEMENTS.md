# Getting Started with Improvements / 改進功能快速上手

This document describes **practical enhancements to the existing starter-package workflow**, not a brand-new product.

本文件說明的是對現有 starter-package 的**實用增強規劃**，不是新產品或完整治理引擎。

---

## 1) Scope first / 先釐清範圍

- Current available tool: `tools/auto_index.py`
- Current deliverable: generated SCBKR index JSON
- Current positioning: open indexing layer (not closed governance core)

- 目前可用工具：`tools/auto_index.py`
- 目前可產出：SCBKR 索引 JSON
- 目前定位：開放式索引層（非封閉治理核心）

---

## 2) 3-minute shortest path / 最短 3 分鐘流程

> Goal: download → run indexer → inspect output → understand next query step.
>
> 目標：下載後快速完成「產生索引、檢查結果、理解下一步查詢」。

```bash
# 1) Move into starter package
cd main-root/starter-package

# 2) (Optional) create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3) Install dependencies (current tool uses Python stdlib only)
# kept for environment consistency
python3 -m pip install --upgrade pip

# 4) Run auto index
python3 tools/auto_index.py \
  --source ./memory-index \
  --output ./memory-index/index.scbkr.generated.json

# 5) Verify generated output
python3 -m json.tool ./memory-index/index.scbkr.generated.json | head -n 40
```

If the command succeeds, you should see:
- `schema: "SCBKR-1.0"`
- `count: <number>`
- `items: [...]`

若指令成功，輸出 JSON 會包含：
- `schema: "SCBKR-1.0"`
- `count: <筆數>`
- `items: [...]`

---

## 3) Sample input → sample output → query flow

### Sample input / 範例輸入
Put files under:

```text
memory-index/json/
memory-index/drive-import/
memory-index/local-private/
```

### Sample output / 範例輸出
The generated `index.scbkr.generated.json` item will look like:

```json
{
  "id": "mem-00001",
  "S": "sample-memory",
  "C": "Imported from json",
  "B": "Local indexing only; governance decisions handled outside open layer.",
  "K": ["file:json/sample-memory.json", "modified:2026-..."],
  "R": "user-owner",
  "route": "json-memory-lane"
}
```

### Query flow today / 目前查詢流
1. Generate index JSON via `auto_index.py`
2. Load JSON in your app/script
3. Filter by SCBKR fields (`S/C/B/K/R`) and `route`
4. Pass filtered memory into your own model prompt

1. 使用 `auto_index.py` 產生索引 JSON
2. 由你的程式載入 JSON
3. 依 `S/C/B/K/R` 與 `route` 做過濾
4. 把過濾結果餵給你的模型提示詞

```bash
# Experimental utility: build lookup-oriented optimized index
python3 tools/build_optimized_index.py \
  --source ./memory-index/index.scbkr.generated.json \
  --output ./memory-index/index.scbkr.optimized.json

# Experimental utility: generate R-field suggestion candidates (review required)
python3 tools/r_field_recommender.py \
  --source ./memory-index/index.scbkr.generated.json \
  --output ./memory-index/r-field.suggestions.json

# Experimental utility: build generic prompt payload (no direct provider API call)
python3 services/scbkr_llm_bridge.py \
  --index ./memory-index/index.scbkr.generated.json \
  --query "onboarding policy risk" \
  --top-k 3

# planned future command (not implemented yet)
# python3 tools/query_index.py --index ./memory-index/index.scbkr.generated.json --q "onboarding risk"
```

---

## 4) Troubleshooting / FAQ 與排錯

### Q1. `source folder not found`
- Ensure you are in `main-root/starter-package`
- Confirm `./memory-index` exists

- 請確認目前路徑是 `main-root/starter-package`
- 請確認 `./memory-index` 目錄存在

### Q2. Output JSON exists but `items` is empty
- You may not have placed files under `memory-index/*`
- Check whether files are filtered as skipped files

- 可能尚未放入任何資料檔
- 請確認不是只剩被略過的檔名

### Q3. How to set default responsibility owner?

```bash
python3 tools/auto_index.py \
  --source ./memory-index \
  --output ./memory-index/index.scbkr.generated.json \
  --default-owner "Your Name / Team"
```

### Q4. Is this already a complete LLM SDK?
- No. `services/scbkr_llm_bridge.py` is an experimental bridge skeleton that only prepares payloads and does not call provider APIs directly.

- 不是。`services/scbkr_llm_bridge.py` 目前僅是實驗性橋接骨架，用於準備 payload，並不直接呼叫供應商 API。
