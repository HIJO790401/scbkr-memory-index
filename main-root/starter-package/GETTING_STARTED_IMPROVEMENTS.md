# Getting Started / 快速上手

這份文件只做一件事：
讓你下載後 3 分鐘內把 open layer 跑起來。

---

## 1) 最快方式（建議）

```bash
cd main-root/starter-package
./run_open_layer.sh
```

輸出重點：
- `memory-index/index.scbkr.generated.json`
- `memory-index/index.scbkr.gate-report.json`
- `memory-index/index.scbkr.decision-ready.json`

---

## 2) 啟動本地 API

```bash
cd main-root/starter-package
python3 services/scbkr_api_server.py \
  --index ./memory-index/index.scbkr.decision-ready.json \
  --port 9000
```

測試：

```bash
curl http://127.0.0.1:9000/health

curl -X POST http://127.0.0.1:9000/query \
  -H "Content-Type: application/json" \
  -d '{"query":"policy risk","top_k":3}'
```

---

## 3) 如果你想用進階工具（experimental）

```bash
# 查詢友善索引
python3 tools/build_optimized_index.py \
  --source ./memory-index/index.scbkr.decision-ready.json \
  --output ./memory-index/index.scbkr.optimized.json

# R 欄位候選建議
python3 tools/r_field_recommender.py \
  --source ./memory-index/index.scbkr.generated.json \
  --output ./memory-index/r-field.suggestions.json

# LLM payload bridge（不直連 provider）
python3 services/scbkr_llm_bridge.py \
  --index ./memory-index/index.scbkr.decision-ready.json \
  --query "onboarding policy risk" \
  --top-k 3
```

---

## 4) 常見問題

### Q1：為什麼 query 結果很少？
因為 API 預設只回傳 decision-ready 記憶（責任鏈截斷）。

### Q2：這是不是完整治理引擎？
不是。這是 open indexing layer。

### Q3：商業層在哪裡？
開源 repo 不含商業治理引擎，請看 `COMMERCIAL_LAYER_OVERVIEW.md`。
