# scbkr-memory-index

SCBKR Memory Index is an open-source **indexing layer** for long-term memory organization.
SCBKR 記憶庫索引是一個開源的長期記憶**索引層**。

It helps people structure memory into SCBKR fields (S/C/B/K/R) so memory can be queried, replayed, audited, and routed.
它把記憶整理成 SCBKR（S/C/B/K/R）欄位，讓資料更容易查詢、重播、稽核與路由。

---

## What this project is / 這個專案是什麼

- An open indexing layer for memory files across sessions and sources.
- A practical starter package with runnable scripts.
- A public, extendable foundation you can connect to your own model stack.

- 用於跨會話、跨來源記憶檔案的開放式索引層。
- 提供可直接執行的 starter package。
- 提供可擴充的公開基礎，讓你自行接模型與流程。

## What this project is not / 這個專案不是什麼

- **Not** a full governance engine.
- **Not** the closed judgment core.
- **Not** a finished enterprise compliance product.
- **Not** a one-click “complete AI agent platform.”

- **不是**完整治理引擎。
- **不是**封閉判斷核心。
- **不是**已完成的企業合規產品。
- **不是**一鍵完成的 AI agent 平台。

## What you can do today / 你今天就能用它做什麼

Today, the repo already provides these runnable tools:
目前 repo 已可直接使用以下工具：

1. `tools/auto_index.py` — generate SCBKR index JSON from local files.
2. `tools/build_optimized_index.py` — build lookup-friendly maps (**experimental**).
3. `tools/r_field_recommender.py` — output R-field candidate suggestions (**experimental**, user review required).
4. `services/scbkr_llm_bridge.py` — create generic LLM prompt payload from indexed memories (**experimental**).

## Who this is for / 這適合誰使用

- People who want structured memory, not just loose folders.
- Developers building memory-enabled assistants and need a clear indexing layer.
- Teams that care about auditability and explicit responsibility traces.

- 想要「結構化記憶」而不只是資料夾的人。
- 正在做具記憶能力應用、需要清楚索引層的開發者。
- 重視可稽核性與責任追蹤的團隊。

## Quick mental model / 一句話理解它在幹嘛

**SCBKR Memory Index = a reusable memory table-of-contents layer, not the final decision engine.**

**SCBKR 記憶庫索引 = 可重用的記憶目錄層，不是最終決策引擎。**

---

## What you get after download / 下載後你會得到什麼

- Static frontend at `main-root/` (for GitHub Pages showcase).
- Starter package at `main-root/starter-package/`.
- Example memory folders + runnable indexing scripts.
- Experimental extension utilities for search-friendly indexing and integration scaffolding.

- `main-root/`：可部署的靜態前端展示。
- `main-root/starter-package/`：可直接使用的起始套件。
- 範例記憶資料夾與可執行索引腳本。
- 可擴充的實驗性工具骨架（查詢友善層與橋接層）。

---

## Project map / 路徑說明

- `repo root/`: overall source root.
- `main-root/`: static public frontend (GitHub Pages target).
- `main-root/starter-package/`: starter data + indexing tools.

Additional reading:
- `GENERAL_AUDIENCE_GUIDE.md` (non-technical guide)
- `DEVELOPER_OVERVIEW.md` (technical boundary + extension guide)
- `main-root/starter-package/GETTING_STARTED_IMPROVEMENTS.md` (3-minute hands-on path)

## Quick start in 3 minutes / 3 分鐘快速開始

```bash
cd main-root/starter-package
python3 tools/auto_index.py \
  --source ./memory-index \
  --output ./memory-index/index.scbkr.generated.json
```

Then optionally run experimental utilities:

```bash
python3 tools/build_optimized_index.py \
  --source ./memory-index/index.scbkr.generated.json \
  --output ./memory-index/index.scbkr.optimized.json

python3 tools/r_field_recommender.py \
  --source ./memory-index/index.scbkr.generated.json \
  --output ./memory-index/r-field.suggestions.json

python3 services/scbkr_llm_bridge.py \
  --index ./memory-index/index.scbkr.generated.json \
  --query "onboarding policy risk" \
  --top-k 3
```

## Deploy frontend / 部署前端

```bash
cd main-root
python3 -m http.server 8080
```

Open: <http://localhost:8080>

---

## Roadmap & Planned Improvements / 改進路線圖

The following items are **planned improvements** for the open indexing layer. They are not shipped as completed capabilities yet.

以下內容屬於**規劃中改進項目**，用於提升開放式索引層的可用性；目前不代表已完成或已全面上線。

| Priority | Status | Problem / 問題 | Solution / 解法 | Expected Impact / 預期效果 | Estimated Effort / 估計工作量 | Target Timeline / 預計時程 |
|---|---|---|---|---|---|---|
| **P1. Getting Started & Developer Experience** | In Planning / 規劃中 | Users often get blocked after running `auto_index.py` because the next step is unclear. 使用者常在跑完 `auto_index.py` 後，不清楚下一步查詢與驗證流程。 | Add a shortest-path onboarding flow, strengthen starter-package run instructions, and document sample input/output/query walkthrough. 補上最短上手路徑、強化 starter-package 可跑性說明，並增加 sample input/output/query 流程。 | Faster first success in ~3 minutes and fewer setup drop-offs. 降低首次上手流失，提高 3 分鐘內跑通率。 | Small–Medium / 小到中 | Target: Q2 2026 initial docs refresh / 目標：2026 Q2 首版文件強化 |
| **P2. LLM Bridge / Query Adapter** | In Planning / 規劃中 | Indexed JSON exists, but integration patterns to OpenAI/Claude/generic LLM are not standardized. 目前已有索引輸出，但對接 OpenAI/Claude/通用 LLM 的方式尚未標準化。 | Define a minimal viable bridge (prototype-level) to pass SCBKR retrieval results into model prompts with memory relevance filtering. 先做最小可行橋接層（原型），把 SCBKR 查詢結果送入模型並支援關聯過濾。 | Lower integration friction for early adopters without claiming a full SDK. 降低整合成本，但維持「非完整 SDK」定位。 | Medium / 中 | Expected: prototype design in Q2–Q3 2026 / 預期：2026 Q2–Q3 完成原型設計 |
| **P3. Performance Layer** | In Planning / 規劃中 | Current flow may rely on straightforward scans for many usage patterns. 目前部分使用情境仍可能以線性掃描為主。 | Plan indexing/query optimization path (e.g., B-Tree, HashMap, cached lookup) based on real dataset profiles. 規劃索引與查詢優化方向（如 B-Tree、HashMap、快取查找），並以實際資料型態驗證。 | **Target:** sub-100ms query latency on typical local datasets; expected improvement from linear scan to indexed lookup. **目標：**在典型本地資料集達到 sub-100ms 查詢延遲；預期由線性掃描改善為索引查找。 | Medium–Large / 中到大 | Target: phased experiments across Q3 2026 / 目標：2026 Q3 分階段驗證 |
| **P4. Responsibility Field Recommender** | In Planning / 規劃中 | Manually assigning `R` can be slow and inconsistent across teams. 手動填寫 `R` 欄位可能耗時且不一致。 | Provide heuristic suggestions from filename/subject/evidence/route, but require final human confirmation. 依 filename/subject/evidence/route 提供候選建議，最終仍由使用者確認。 | Better consistency while preserving explicit human accountability. 提升一致性，同時維持「責任不可被悄悄自動化」。 | Small–Medium / 小到中 | Expected: initial heuristic rules in Q3 2026 / 預期：2026 Q3 初版規則 |
| **P5. Enterprise Templates** | In Planning / 規劃中 | Teams ask for domain starter structures but project currently ships a general starter only. 團隊常需要產業起始範本，但目前僅有通用 starter。 | Prepare future template packs (finance, healthcare, SaaS, AI safety) as optional scaffolds. 規劃未來產業範本包（金融、醫療、SaaS、AI Safety）作為可選模板。 | Faster adoption in regulated contexts without claiming full compliance automation. 加速導入，但不宣稱已具備完整合規自動化能力。 | Medium / 中 | Target: after core onboarding + bridge milestones (post-Q3 2026) / 目標：核心上手與橋接完成後（2026 Q3 之後） |
