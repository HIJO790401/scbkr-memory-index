# GENERAL AUDIENCE GUIDE
# 一般使用者導覽

## 這個專案在做什麼？

它在做「記憶索引」，不是在做神祕 AI 魔法。

你可以把它想成：
- 先把資料整理成 SCBKR 欄位（S/C/B/K/R）
- 再用責任鏈規則決定哪些記憶可以進決策

核心原則：
**沒有責任鏈，不進決策。**

---

## 為什麼不是普通資料夾？

普通資料夾只告訴你「檔案在哪裡」。
SCBKR 會多告訴你：
- 事件主題（S）
- 背景原因（C）
- 使用邊界（B）
- 可驗證證據（K）
- 誰負責（R）

---

## 你現在下載 ZIP 能做什麼？

可以直接做：
1. 自動建立索引
2. 做責任鏈截斷（human gate）
3. 啟動本地 API 查詢

指令（最短）：

```bash
cd main-root/starter-package
./run_open_layer.sh
python3 services/scbkr_api_server.py --index ./memory-index/index.scbkr.decision-ready.json --port 9000
```

---

## 目前還不能做什麼？

目前不包含：
- 完整治理引擎
- 自動責任判定
- 企業合規完成版
- 供應商 API 直連完整服務

---

## 開源層 vs 商業層

- 開源層：你可下載、可跑、可擴充
- 商業層：治理權重、白盒規則、企業導入

詳見：`COMMERCIAL_LAYER_OVERVIEW.md`
