# DEVELOPER OVERVIEW
# 開發者總覽

This document is a boundary-first technical map for the current open repo.
本文件以「邊界優先」方式整理目前公開 repo 的技術層次。

---

## 1) Current available tools / 現有工具

Located under `main-root/starter-package/`:

1. `tools/auto_index.py`
2. `tools/build_optimized_index.py` (**experimental**)
3. `tools/r_field_recommender.py` (**experimental**)
4. `services/scbkr_llm_bridge.py` (**experimental**)

---

## 2) What each tool does / 每個工具做什麼

### `auto_index.py`
- Scans memory folders.
- Generates baseline SCBKR index JSON (`items`, `S/C/B/K/R`, route).
- Acts as the canonical starter entry point.

### `build_optimized_index.py` (experimental)
- Reads generated index JSON.
- Builds lookup maps by route/date/keyword/responsibility.
- Outputs optimization-friendly JSON for faster extension experiments.

### `r_field_recommender.py` (experimental)
- Reads index JSON.
- Applies simple heuristic rules from filename/subject/evidence/route.
- Outputs candidate `R` suggestions with confidence label + notes.

### `scbkr_llm_bridge.py` (experimental)
- Loads index JSON.
- Finds top relevant memory items using simple term matching.
- Builds generic prompt payload for downstream adapters.

---

## 3) What each tool does NOT do / 每個工具不做什麼

### `auto_index.py` does NOT
- make final governance decisions.
- guarantee semantic correctness of all fields.

### `build_optimized_index.py` does NOT
- provide production-grade search engine performance.
- guarantee benchmarked latency targets.

### `r_field_recommender.py` does NOT
- auto-assign final responsibility.
- replace human review for R field decisions.

### `scbkr_llm_bridge.py` does NOT
- call provider APIs directly.
- include API key management or production orchestration.

---

## 4) Current data flow / 目前資料流

```text
Input files (json / drive-import / local-private)
  -> auto_index.py
  -> index.scbkr.generated.json
  -> (optional) build_optimized_index.py
  -> index.scbkr.optimized.json
  -> (optional) r_field_recommender.py
  -> r-field.suggestions.json
  -> (optional) scbkr_llm_bridge.py
  -> generic prompt payload JSON for your own adapter
```

---

## 5) Suggested extension path / 建議擴充順序

1. Stabilize input conventions for S/C/B/K/R population.
2. Expand optimized lookup strategy and index schema versioning.
3. Add pluggable query scoring strategy (still local/offline first).
4. Build provider adapters as separate modules (OpenAI/Claude/etc.).
5. Add audit/report utilities and template packs by domain.

Keep each step modular and testable; avoid turning starter utilities into a monolith.
每一步建議保持模組化與可測試，避免把 starter 工具做成難維護巨石。

---

## 6) Why this is called an indexing layer / 為什麼叫 indexing layer

Because the repo focuses on memory structuring, retrieval preparation, and routing context—
not final governance judgment.

因為這個 repo 的核心是「記憶結構化、查詢前處理、路由上下文」，
而不是最終治理判斷。

---

## Hard boundaries (current public repo) / 邊界聲明（目前公開 repo）

- No direct provider API integration.
- No full governance engine.
- No automatic responsibility adjudication.
- No finished enterprise compliance package.
- Current tools are starter + experimental skeletons.

- 沒有真實 provider API 直連。
- 沒有完整治理引擎。
- 沒有自動責任判定。
- 沒有企業合規完成版。
- 現有工具屬於 starter + experimental skeleton。
