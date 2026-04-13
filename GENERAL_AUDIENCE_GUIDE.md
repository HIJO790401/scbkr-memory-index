# GENERAL AUDIENCE GUIDE
# 一般讀者導覽

## 1) SCBKR 是什麼？ / What is SCBKR?

SCBKR 是一種記憶整理格式，把每筆記憶分成 5 個欄位：
SCBKR is a memory structure with 5 fields:

- **S (Subject)**：這筆記憶在講誰／什麼主題
- **C (Cause)**：背景原因或脈絡
- **B (Boundary)**：限制、範圍、不能做什麼
- **K (Key Evidence)**：關鍵證據或來源
- **R (Responsibility)**：誰要對這筆記憶負責

簡單說：它不是把資料塞進資料夾，而是把記憶做成可追溯的結構。
In short: this is not just filing documents; it is structuring memory with traceable context.

---

## 2) 為什麼這不是普通的資料夾整理？
## Why this is not just folder organization

普通資料夾通常只回答「檔案放在哪裡」。
A normal folder mostly tells you where a file is.

SCBKR 會補上：
SCBKR also records:
- 這筆記憶的脈絡（Cause）
- 使用邊界（Boundary）
- 證據鏈（Key Evidence）
- 責任歸屬（Responsibility）

因此你不只找到檔案，還能理解「這筆記憶可不可以用、怎麼用、誰負責」。
So you can review not just *where* memory is, but *how* and *whether* to use it.

---

## 3) 為什麼 R 欄位特別重要？
## Why is the R field especially important?

R（Responsibility）不是裝飾欄位。
R (Responsibility) is not decorative metadata.

它代表：
It represents:
- 誰對這筆記憶的採用與風險承擔責任
- 出現爭議時可以回溯到誰做了決定

這個專案強調：**責任不能被悄悄自動化**。
This repo explicitly treats responsibility as a human decision, not silent automation.

---

## 4) 為什麼強調責任、重播、可查詢？
## Why focus on responsibility, replay, and queryability?

因為長期記憶系統最常見問題不是「找不到檔案」，而是：
Because long-term memory systems usually fail not at storage, but at usage quality:

- 找到內容卻不知道是否可信
- 不知道這筆資訊從哪裡來
- 不知道誰該負責
- 下一次想重現同樣判斷時做不到

SCBKR 的核心目的，是讓每筆記憶更可解釋、可回溯、可重播。
The goal is to make memory easier to explain, trace, and replay.

---

## 5) 目前這個 repo 已經能做什麼？
## What can this repo do today?

目前可用能力（2026-04-13）：
Current available capabilities (as of 2026-04-13):

1. `auto_index.py`：從資料夾自動產出 SCBKR 索引 JSON。
2. `build_optimized_index.py`（experimental）：把索引轉成查詢友善查找表。
3. `r_field_recommender.py`（experimental）：提供 R 欄位候選建議（需人工確認）。
4. `scbkr_llm_bridge.py`（experimental）：把查詢結果包成通用 prompt payload。

---

## 6) 目前還不能做什麼？
## What it still does NOT do

這個 repo 目前**不包含**：
This repo currently does **not** include:

- 完整治理引擎
- 封閉判斷核心
- 自動責任最終判定器
- 企業合規完整產品
- 真實 provider API 直連（例如直接呼叫 OpenAI/Claude）

如果你需要這些，必須在此索引層之上自行整合。
If you need those, you should build them on top of this indexing layer.

---

## 7) 如果我是一般使用者，我可以怎麼開始？
## If I am a non-technical user, how should I start?

最簡單路徑：
Simple path:

1. 先看首頁了解用途（`main-root/index.html`）。
2. 下載 ZIP 並解壓。
3. 進入 `main-root/starter-package/`。
4. 請懂基本命令列的人協助執行 `auto_index.py`。
5. 打開產生的 JSON，觀察每筆記憶的 S/C/B/K/R。

如果你不是工程師，也可以先把這個專案當成「記憶結構標準」，先統一欄位再談模型整合。
If you are not a developer, you can still use SCBKR as a memory-structure standard before model integration.
