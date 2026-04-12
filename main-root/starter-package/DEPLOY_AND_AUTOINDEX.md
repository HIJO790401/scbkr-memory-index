# SCBKR Starter: Deploy + Auto Index Guide

> This package is the **open indexing layer** for long-term AI memory organization.
> It is **not** the closed governance / judgment core.
>
> 本套件是長期 AI 記憶組織的**開放索引層**，**不是**封閉治理/判斷核心。

## 1) Folder map / 路徑地圖

- `repo-root/`：整個專案根目錄
- `repo-root/main-root/`：公開靜態前端網站
- `repo-root/main-root/starter-package/`：可下載後立即使用的索引示範資料與工具

## 2) Run frontend locally / 本機啟動前端

From **repo root**:
```bash
cd main-root
python3 -m http.server 8080
```
Open: <http://localhost:8080>

## 3) Deploy to GitHub Pages / 部署到 GitHub Pages

1. Push repository to GitHub
2. Settings → Pages
3. Publish branch/folder and set folder to `main-root`

## 4) Auto build SCBKR index / 自動建立 SCBKR 索引

### Option A: start from repo root / 從 repo 根目錄開始
```bash
cd main-root/starter-package
python3 tools/auto_index.py --source ./memory-index --output ./memory-index/index.scbkr.generated.json
```

### Option B: start from main-root / 從 main-root 開始
```bash
cd starter-package
python3 tools/auto_index.py --source ./memory-index --output ./memory-index/index.scbkr.generated.json
```

### Optional owner / 可選責任預設值
```bash
python3 tools/auto_index.py \
  --source ./memory-index \
  --output ./memory-index/index.scbkr.generated.json \
  --default-owner "Shen-Yao 888π / Wen-Yao Hsu"
```

## 5) What auto_index.py does / 腳本做什麼

- Scans files under `memory-index/`
- Generates demo SCBKR fields (S/C/B/K/R)
- Infers route by folder keywords (`json`, `drive`, `local`)
- Outputs `index.scbkr.generated.json`

> Reminder / 提醒：
> Generated output is a **demo suggestion** for indexing flow.
> Responsibility and final judgment should be consciously decided by users.
