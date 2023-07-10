# luna_py

lunapy v1.0.3pre2

- curseforge-autodownload (v1.0.1)
- Dataset Collector V3 (v3.0.3)
- jpg to png Converter (v1.0.1)
- Picture Collector (v1.2.1)
- Taskkiller for Minecraft (β2.1)
- Output Cleaner (β1.1)

-----------

Changelogs (v1.0.3)

- curseforge-autodownload v1.0.1
  - 簡易実行用にrun.batを追加

- Dataset Collector v3.0.3
  - 簡易実行用にrun.batを追加
  - よくわからんメモファイルを削除

- jpg to png Converter v1.0.1
  - 簡易実行用にrun.batを追加

- Picture Collector v1.2.1
  - 簡易実行用にrun.batを追加

- Taskkiller for Minecraft β2.1
  - 簡易実行用にrun.batを追加

- Output Cleaner β1.1
  - 簡易実行用にrun.batを追加

- Lunapy v1.0.3
  - Jupyter Notebookからの簡易実行用にmain_script.pyとその他関連ファイルを追加

-----------

lunapy v1.0.3 作りたいなと思うもの

- jpg to png Converter
  - 右クリックメニューからの変換の追加
  - jpeg にも対応

- Picture Collector
  - luna_GlobalScript の使用によるコンパクト化

- luna.py.ipynb
  - lunapyの簡易実行(Jupyter Notebookから実行可能に)
  
- lunapy
  - venvの統一、requirements.txtなどでのモジュール一括管理
  - luna_GlobalScriptの統一

-----------

# Windows以外の環境での実行

main.pyを直接実行
ipynbの簡易起動では、batchファイルを介して実行しているため、Windows環境以外ではPythonファイルを直接実行する必要がある。