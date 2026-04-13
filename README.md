scbkr-memory-index

我把這個專案做成一個**可下載、可執行、可擴充**的 SCBKR 開放式記憶索引層。  
I built this project as a **downloadable, runnable, and extensible** open SCBKR memory indexing layer.

我不把它包裝成完整治理引擎。  
它的工作很明確：**先把記憶整理好，再做責任鏈截斷，最後只把可進決策的內容交給下一層使用。**  
I do not package this as a full governance engine.  
Its role is very specific: **structure memory first, apply responsibility-chain cutoff, and only pass decision-ready memory to the next layer.**

---

## 我這個專案在做什麼 / What I am building

我用 **SCBKR（S / C / B / K / R）** 把跨來源記憶整理成可：

- 查詢  
- 重播  
- 稽核  
- 路由  

的索引結構。

I use **SCBKR (S / C / B / K / R)** to structure cross-source memory into indexes that are:

- queryable  
- replayable  
- auditable  
- routable  

我提供一個 **starter-package**，讓你下載 ZIP 後就能直接跑起來，不需要先理解整套封閉治理核心。  
I provide a **starter package** so you can run it directly after downloading the ZIP, without needing access to the closed governance core.

我把核心規則寫得很死：  
**沒有責任鏈，不進決策。**  
I enforce one hard rule:  
**No responsibility chain, no decision path.**

---

## 這個專案不是什麼 / What this project is not

我沒有把封閉治理核心開源。  
I do not open-source the closed governance core.

我沒有把它包裝成完整的企業合規產品。  
I do not present this as a full enterprise compliance product.

我沒有做成自動責任判定器。  
I do not provide automatic responsibility adjudication.

它不是萬能 AI 殼，也不是聊天玩具。  
它是一個**開放式索引層**。  
It is not a universal AI shell or a chatbot toy.  
It is an **open indexing layer**.

---

## 下載後直接可用流程 / Runnable flow after ZIP download

```bash
cd main-root/starter-package
./run_open_layer.sh
python3 services/scbkr_api_server.py --index ./memory-index/index.scbkr.decision-ready.json --port 9000

這個流程會做三件事：

1. 建立索引
index.scbkr.generated.json


2. 套用責任鏈截斷
index.scbkr.decision-ready.json


3. 啟動本地 API
(/health, /query)



This flow does three things:

1. Build the index
index.scbkr.generated.json


2. Apply responsibility-chain cutoff
index.scbkr.decision-ready.json


3. Start the local API
(/health, /query)




---

開源層工具清單 / Open-layer tools

目前公開 repo 內的工具包括：

tools/auto_index.py

tools/scbkr_human_gate.py

services/scbkr_api_server.py

tools/build_optimized_index.py (experimental)

tools/r_field_recommender.py (experimental)

services/scbkr_llm_bridge.py (experimental)


The current public repo includes:

tools/auto_index.py

tools/scbkr_human_gate.py

services/scbkr_api_server.py

tools/build_optimized_index.py (experimental)

tools/r_field_recommender.py (experimental)

services/scbkr_llm_bridge.py (experimental)


也就是說，現在已經能做的不是空展示，而是：

自動索引

責任鏈截斷

decision-ready 輸出

本地查詢 API

查詢優化骨架

R 欄位候選建議

LLM prompt payload 橋接骨架


In other words, this is not just a concept page.
It already provides:

auto indexing

responsibility-chain cutoff

decision-ready output

local query API

an optimization skeleton

R-field candidate suggestions

an LLM prompt-payload bridge skeleton



---

商業層邊界 / Commercial layer boundary

商業層不放在這個公開 repo 裡。
它包含：

治理權重與參數引擎

模型上層白盒規則

企業審計與導入支援


The commercial layer is not inside this public repo.
It includes:

governance weights and parameter engine

white-box rules above model outputs

enterprise audit and onboarding support


請看：
COMMERCIAL_LAYER_OVERVIEW.md

See:
COMMERCIAL_LAYER_OVERVIEW.md


---

前端展示 / Frontend showcase

cd main-root
python3 -m http.server 8080

首頁的重點不是行銷包裝，而是：

可執行命令

SCBKR 結構

責任鏈邏輯

開源層 / 商業層邊界


The homepage is not designed as marketing fluff.
It is designed to show:

executable commands

the SCBKR structure

responsibility-chain logic

the boundary between the open layer and the commercial layer



---

相關文件 / Related docs

GENERAL_AUDIENCE_GUIDE.md

DEVELOPER_OVERVIEW.md

main-root/starter-package/GETTING_STARTED_IMPROVEMENTS.md



---

一句話總結 / One-line summary

這不是完整治理引擎。
這是一個讓記憶在進入決策前，先被整理、先被切邊界、先被接上責任鏈的開放式索引層。

This is not a full governance engine.
It is an open indexing layer that structures memory, applies boundary control, and connects responsibility before memory enters any decision path.

