# scbkr-memory-index

SCBKR Memory Index 是一個「可下載、可執行、可擴充」的**開源記憶索引層**。  
它不是完整治理引擎，而是先把記憶整理成可查詢、可重播、可稽核、可路由的 SCBKR 結構。

---

## 你下載 ZIP 之後可以直接做什麼

1. 把資料放進 `main-root/starter-package/memory-index/`
2. 自動產生索引
3. 經過責任鏈截斷（human gate）
4. 啟動本地 API 查詢

快速流程（建議）：

```bash
cd main-root/starter-package
./run_open_layer.sh
python3 services/scbkr_api_server.py --index ./memory-index/index.scbkr.decision-ready.json --port 9000
```

---

## 開源層（你現在就能用）

位置：`main-root/starter-package/`

- `tools/auto_index.py`：從資料夾產生 SCBKR 索引 JSON
- `tools/scbkr_human_gate.py`：責任鏈截斷，輸出 decision-ready / review-required
- `services/scbkr_api_server.py`：本地 REST 查詢（`/health`, `/query`）
- `tools/build_optimized_index.py`（experimental）：建立查找表
- `tools/r_field_recommender.py`（experimental）：R 欄位候選建議（不自動判定）
- `services/scbkr_llm_bridge.py`（experimental）：LLM payload 橋接骨架（不直連 provider）

---

## 這個專案不是什麼（邊界）

- 不是完整治理引擎
- 不是封閉判斷核心
- 不是企業合規完成版產品
- 不是自動責任判定器

你的核心規則是：
**沒有責任鏈，不進決策。**

---

## 前端展示位置

- 靜態展示頁：`main-root/index.html`
- 本機預覽：

```bash
cd main-root
python3 -m http.server 8080
```

---

## 商業層（不在開源 repo 內）

你可以在商業版本提供：

- SCBKR 治理權重與參數引擎
- 模型上層白盒規則
- 企業審計策略模板與導入服務

說明文件：`COMMERCIAL_LAYER_OVERVIEW.md`

---

## 相關文件

- `GENERAL_AUDIENCE_GUIDE.md`：一般使用者說明
- `DEVELOPER_OVERVIEW.md`：開發者與資料流
- `main-root/starter-package/GETTING_STARTED_IMPROVEMENTS.md`：上手指引
