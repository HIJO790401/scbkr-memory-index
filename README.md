# scbkr-memory-index

我把這個專案做成一個可下載、可執行、可擴充的 **SCBKR 開放式記憶索引層**。  
I built this project as a downloadable, runnable, and extensible **open SCBKR memory indexing layer**.

我不把它包裝成完整治理引擎；它的工作是先把記憶整理好，再做責任鏈截斷。  
I do not package this as a full governance engine; its job is to structure memory first, then apply responsibility-chain cutoff.

---

## 我這個專案在做什麼 / What I am building

- 我用 SCBKR（S/C/B/K/R）把跨來源記憶整理成可查詢、可重播、可稽核、可路由的索引。
- 我提供 starter-package，讓你下載 ZIP 後可以直接跑起來。
- 我把核心規則寫死：**沒有責任鏈，不進決策。**

- I use SCBKR (S/C/B/K/R) to structure cross-source memory into queryable, replayable, auditable, and routable indexes.
- I provide a starter package so you can run it directly after downloading ZIP.
- I enforce one core rule: **No responsibility chain, no decision path.**

---

## 這個專案不是什麼 / What this project is not

- 我沒有開源封閉治理核心。
- 我沒有把它做成完整企業合規產品。
- 我沒有做自動責任判定器。

- I do not open-source the closed governance core.
- I do not claim this is a full enterprise compliance product.
- I do not provide automatic responsibility adjudication.

---

## 下載後直接可用流程 / Runnable flow after ZIP download

```bash
cd main-root/starter-package
./run_open_layer.sh
python3 services/scbkr_api_server.py --index ./memory-index/index.scbkr.decision-ready.json --port 9000
```

這個流程會做三件事：
1. 建立索引 `index.scbkr.generated.json`
2. 套用責任鏈截斷 `index.scbkr.decision-ready.json`
3. 啟動本地 API (`/health`, `/query`)

This flow does three things:
1. build index `index.scbkr.generated.json`
2. apply responsibility-chain cutoff `index.scbkr.decision-ready.json`
3. start local API (`/health`, `/query`)

---

## 開源層工具清單 / Open-layer tools

- `tools/auto_index.py`
- `tools/scbkr_human_gate.py`
- `services/scbkr_api_server.py`
- `tools/build_optimized_index.py`（experimental）
- `tools/r_field_recommender.py`（experimental）
- `services/scbkr_llm_bridge.py`（experimental）

---

## 商業層說明 / Commercial layer boundary

商業層不放在這個公開 repo，包含治理權重、白盒規則、企業導入支援。  
The commercial layer is not inside this public repo and includes governance weights, white-box rules, and enterprise onboarding support.

請看：`COMMERCIAL_LAYER_OVERVIEW.md`

---

## 前端展示 / Frontend showcase

```bash
cd main-root
python3 -m http.server 8080
```

首頁重點是「可執行命令 + 責任鏈邏輯」，不是行銷頁。  
The homepage focuses on executable commands and responsibility-chain logic, not marketing fluff.

---

## 相關文件 / Related docs

- `GENERAL_AUDIENCE_GUIDE.md`
- `DEVELOPER_OVERVIEW.md`
- `main-root/starter-package/GETTING_STARTED_IMPROVEMENTS.md`
