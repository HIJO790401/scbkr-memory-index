# DEVELOPER OVERVIEW
# 開發者總覽

## 1) 專案定位

這個 repo 是 **open indexing layer**：
- 做記憶索引
- 做責任鏈截斷
- 做本地查詢服務

不是完整治理引擎，也不提供封閉判斷核心。

---

## 2) 目前可用工具（starter-package）

- `tools/auto_index.py`
- `tools/scbkr_human_gate.py`
- `services/scbkr_api_server.py`
- `tools/build_optimized_index.py`（experimental）
- `tools/r_field_recommender.py`（experimental）
- `services/scbkr_llm_bridge.py`（experimental）

---

## 3) 最短可跑資料流

```text
source files
  -> auto_index.py
  -> index.scbkr.generated.json
  -> scbkr_human_gate.py
  -> index.scbkr.decision-ready.json + gate-report
  -> scbkr_api_server.py (/query)
```

一鍵入口：

```bash
cd main-root/starter-package
./run_open_layer.sh
```

---

## 4) 每個工具做什麼 / 不做什麼

### auto_index.py
做：建立基礎 SCBKR 索引。  
不做：最終治理判斷。

### scbkr_human_gate.py
做：責任鏈截斷，標記 decision-ready。  
不做：自動替人類承擔責任。

### scbkr_api_server.py
做：提供本地 REST 查詢接口。  
不做：企業級認證、RBAC、API gateway 安全控制。

### build_optimized_index.py（experimental）
做：建立查詢友善查找表。  
不做：保證固定性能數字。

### r_field_recommender.py（experimental）
做：給 R 欄位候選建議。  
不做：自動責任判定。

### scbkr_llm_bridge.py（experimental）
做：組裝 LLM prompt payload。  
不做：直連 OpenAI/Claude provider API。

---

## 5) 商業層邊界

開源 repo 不包含：
- 治理權重引擎
- 白盒規則參數管理
- 企業合規完成版能力

商業層說明請看：`COMMERCIAL_LAYER_OVERVIEW.md`
