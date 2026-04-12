SCBKR Memory Index Starter Package

This package provides the OPEN INDEXING LAYER (not the closed governance core).
本套件提供開放索引層（不包含封閉治理核心）。

FASTEST USAGE:
- cd main-root/starter-package
- python3 tools/auto_index.py --source ./memory-index --output ./memory-index/index.scbkr.generated.json
- put your files in memory-index/json, drive-import, local-private

Folder map / 路徑地圖:
- repo root: whole project
- main-root: static public frontend
- main-root/starter-package: starter data + indexing tool

Quick start (from repo root):
1) cd main-root/starter-package
2) python3 tools/auto_index.py --source ./memory-index --output ./memory-index/index.scbkr.generated.json

Quick start (from main-root):
1) cd starter-package
2) python3 tools/auto_index.py --source ./memory-index --output ./memory-index/index.scbkr.generated.json

Optional owner example:
python3 tools/auto_index.py --source ./memory-index --output ./memory-index/index.scbkr.generated.json --default-owner "Shen-Yao 888π / Wen-Yao Hsu"

SCBKR
- S = Subject
- C = Cause
- B = Boundary
- K = Key Evidence
- R = Responsibility

Note:
R is not just metadata. Responsibility should be consciously assigned by users.
