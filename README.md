SCBKR Memory Index

SCBKR 記憶庫索引

SCBKR Memory Index is an open indexing layer for long-term AI memory organization.
SCBKR Memory Index 是一個用來處理 長期 AI 記憶組織 的 開放式索引層。

This project is not a full governance engine.
It does not include my closed governance or judgment core.
本專案不是完整治理引擎，
也不包含我封閉的治理／判斷核心。

What I open-source here is the indexing layer: a structured way to organize memory so it becomes:

queryable

replayable

auditable

routable


我在這裡開放的是 索引層：
用一套結構化方式去整理記憶，讓它具備：

可查詢

可重播

可稽核

可路由



---

Website

展示網站

Public showcase / 公開展示站：

https://hijo790401.github.io/scbkr-memory-index/main-root/index.html#download

This website is a fixed structured showcase, not a freeform input sandbox.
It is designed to explain the framework clearly, not to expose the closed core through a toy interface.
這個網站是 固定展示站，不是可自由輸入的沙盒。
它的目的，是把這套索引框架清楚展示出來，而不是用玩具式介面去假裝碰到封閉核心。


---

Core Positioning

核心定位

This is NOT a full governance engine

This is an open indexing layer for long-term AI memory organization

It uses the SCBKR structure

It supports 3 fixed demo routes

It can be downloaded as a repo ZIP and used locally

It does not include the closed governance / judgment core

這不是完整治理引擎

這是長期 AI 記憶組織的 開放索引層

它使用 SCBKR 結構

它支援 3 個固定示範路由

它可以透過 repo ZIP 下載後本地使用

它不包含封閉治理／判斷核心



---

What SCBKR Means

SCBKR 是什麼

SCBKR is the core indexing structure used in this project:

S = Subject

C = Cause

B = Boundary

K = Key Evidence

R = Responsibility


SCBKR 是本專案使用的核心索引結構：

S = Subject（主體）

C = Cause（原因）

B = Boundary（邊界）

K = Key Evidence（關鍵證據）

R = Responsibility（責任）


This is different from a typical RAG-only approach.
RAG-only systems usually focus on retrieving matching fragments.
SCBKR Memory Index focuses on structured memory organization across time, with explicit routing, replay, and responsibility tracking.

這和一般只做 RAG 的方式不同。
RAG-only 系統通常偏向「撈到相關片段」，
而 SCBKR Memory Index 更重視的是：跨會話、跨來源、跨時間的結構化記憶組織，並且把路由、重播與責任鏈一起保留下來。


---

Fixed Demo Routes

固定示範路由

This project contains 3 fixed showcase routes:

本專案包含 3 個固定示範路由：

1. JSON Route

JSON memory items → SCBKR Index → Route → Replay / Audit
JSON 記憶節點 → SCBKR 索引 → 路由 → 重播／稽核

2. Google Drive Route (conceptual showcase)

Drive Folder → Document Set → SCBKR Index → Route → Replay
Drive 資料夾 → 文件集合 → SCBKR 索引 → 路由 → 重播

3. OpenClaw Local Route (conceptual showcase)

Local Folder / Memory Files → SCBKR Index → Your Model → Recall / Route / Replay
本地資料夾／記憶檔 → SCBKR 索引 → 你的模型 → Recall / Route / Replay

These are fixed demonstrations, not freeform user input tools.
這些都是 固定示範，不是開放使用者自由輸入的工具。


---

What This Repository Includes

這個倉庫包含什麼

This repository includes:

a public static frontend showcase

a downloadable starter package

a simple auto-index CLI tool

starter schema and sample structure

GitHub Pages-friendly layout


本倉庫包含：

公開靜態展示前端

可下載的 starter package

簡單可跑的 auto-index CLI 工具

starter schema 與範例結構

GitHub Pages 友善布局



---

How to Actually Use It

真正要怎麼使用

If you want to actually use the memory indexing layer, go directly to:

如果你真的要使用這套記憶索引層，請直接進入：

main-root/starter-package/

That folder is the actual usage area.
這個資料夾才是真正的實作使用區。

Your working memory folders are:

你的工作資料夾如下：

main-root/starter-package/memory-index/json/
main-root/starter-package/memory-index/drive-import/
main-root/starter-package/memory-index/local-private/

Use them like this:

json/ → JSON memory items

drive-import/ → imported cloud documents

local-private/ → local private memory files


使用方式如下：

json/ → JSON 記憶項目

drive-import/ → 雲端匯入文件

local-private/ → 本地私有記憶資料



---

Quick Start

快速開始

Step 1 — Download and unzip the repo

第一步：下載並解壓 repo

Download the repository ZIP, then go directly to:

下載整個 repo ZIP 後，直接進入：

main-root/starter-package/

Do not stay at the public frontend layer if your goal is actual usage.
如果你的目標是實際使用，就不要停留在前端展示層。


---

Step 2 — Put your memory files into the memory-index folders

第二步：把記憶檔案放進 memory-index 子資料夾

Put your files into:

把你的資料放進：

json/

drive-import/

local-private/



---

Step 3 — Generate the SCBKR index, then connect your own model

第三步：產生 SCBKR 索引，再接上你自己的模型

Run:

執行：

cd main-root/starter-package
python3 tools/auto_index.py \
  --source ./memory-index \
  --output ./memory-index/index.scbkr.generated.json

After that, let your own model read the generated index file for:

接著，讓你自己的模型讀取產生出來的索引檔，用來做：

recall

route

replay


This helps keep memory across sessions in a trackable structure, reducing forgetting and drift.
這能把跨會話記憶維持在可追蹤的結構中，降低遺忘與漂移。


---

auto_index.py

auto_index.py 說明

File location / 檔案位置：

main-root/starter-package/tools/auto_index.py

Purpose / 用途：

scan the memory-index/ folder

generate a SCBKR index JSON file

create a starter routing structure for later model use

掃描 memory-index/ 資料夾

產生 SCBKR 索引 JSON

建立後續模型可接用的初版路由結構


Required arguments

必要參數

--source

--output


Optional argument

可選參數

--default-owner


If provided, it writes that value into each item’s R field.
If omitted, the safe default is user-owner.

如果提供，會把該值寫進每筆記憶的 R 欄位。
如果不提供，安全預設值是 user-owner。

Example / 範例：

python3 tools/auto_index.py \
  --source ./memory-index \
  --output ./memory-index/index.scbkr.generated.json \
  --default-owner "Shen-Yao 888π / Wen-Yao Hsu"


---

Responsibility Philosophy

R 欄位與責任哲學

The R field is not ordinary metadata.
It should not be treated as a decorative label or silently auto-replaced by an algorithm.

R 欄位 不是 普通 metadata。
它不應該被當成裝飾欄位，也不應該被演算法悄悄自動取代。

The R field is not automatically equivalent to truth.
Responsibility should not be silently replaced by an algorithm;
users should consciously decide who bears each memory item.

R 欄位不是自動等於真相。
責任不該被演算法悄悄取代；
使用者應在使用前，明確決定每筆記憶由誰承擔。

That is why this project opens only the indexing layer.
Governance and judgment are not automatically solved by storage or retrieval.
這也是為什麼本專案只開放索引層。
治理與判斷，不會因為你把資料存起來或撈回來就自動成立。


---

Project Structure

專案結構

repo-root/
├─ README.md
└─ main-root/
   ├─ index.html
   ├─ styles.css
   ├─ README.md
   └─ starter-package/
      ├─ DEPLOY_AND_AUTOINDEX.md
      ├─ README.txt
      ├─ tools/
      │  └─ auto_index.py
      └─ memory-index/
         ├─ index.scbkr.json
         ├─ json/
         ├─ drive-import/
         └─ local-private/

This means:

repo-root/ = repository root

main-root/ = public static frontend

main-root/starter-package/ = actual usage area for the open indexing layer


也就是說：

repo-root/ = 倉庫根目錄

main-root/ = 公開靜態展示前端

main-root/starter-package/ = 開放索引層真正的使用區



---

Deployment

部署

Public frontend

公開前端

This project is GitHub Pages friendly.
Deploy the public frontend from:

本專案適合部署到 GitHub Pages。
請從以下位置部署前端：

main-root/

Local preview

本地預覽

cd main-root
python3 -m http.server 8080

Then open / 然後打開：

http://localhost:8080


---

Founder / Governance Contact

Founder / 治理聯絡

Founder: Shen-Yao 888π / Wen-Yao Hsu
創建者： Shen-Yao 888π / Wen-Yao Hsu

Governance collaboration, licensing, and coordination should go through the founder.
治理合作、授權、協作與聯絡，請透過 founder 對接。

Founder website / 創辦人網站：
https://hijo790401.github.io/shen-yao-portal/


---

One-Line External Description

一句話對外簡述

SCBKR Memory Index is an open indexing layer for long-term AI memory organization: structure memory using S/C/B/K/R, generate an index from your files, and connect your own model for recall, route, and replay.

SCBKR Memory Index 是一個長期 AI 記憶組織的開放索引層：用 S/C/B/K/R 結構化整理記憶，從你的資料生成索引，再接上你自己的模型做 recall、route 與 replay。


---

Final Boundary

最終邊界聲明

This repository opens the indexing layer, not the closed governance core.
本倉庫開放的是 索引層，不是 封閉治理核心。

If you want to understand the system, the public site is enough.
If you want to use the system, go to main-root/starter-package/.
如果你想理解系統，看公開網站就夠。
如果你想真正使用，就進 main-root/starter-package/。

That is the intended boundary of this project.
這就是本專案設計好的邊界。
