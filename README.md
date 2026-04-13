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
