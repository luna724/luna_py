# 事前準備

**setup.bat** を実行する

# lunapy v1.0.4pre3

- curseforge-autodownload (v1.0.0)
- Dataset Collector V3 (v4.0pre1)
- jpg to png Converter (v1.0.3)
- Luna's Global Script (v1.0.3-r9)
- Picture Collector (v1.2.3)
- Music Collector (β1)
- MP3 to wav Converter (v1.0.0)
- Taskkiller for Minecraft (β2.1)
- Output Cleaner (β1.1)

-----------

Changelog lunapy v1.0.4pre3

- Luna's Global Script v1.0.2-r8 -> v1.0.3-r9
  - pjsekai/uca/id/any_roma2idxname.py
    - 02dモード、ユニットモードをサポート
  - __init__.py
    - 不足していた位置に追加
  
- Dataset Collector β4  v3.0.4 -> v4.0pre1
  - Singleモード(一人を対象)のサポート
  - Multiモード(ユニットごと)のサポート
  - Leo/need以外のキャラクターもサポート
  - 視覚的なログを追加(Output Promptに)
  - luna_GlobalScriptとの依存関係を改善
    - 相互importが起こらないように
  (現在 main.pyが未完全なので実行不可能)

- luna.py.ipynb
  - 一時的に更新を停止

-----------

lunapy v1.0.4 作りたいなと思うもの の残り

- Dataset Collector
  - wav形式の取得を追加

-----------
| Feature Name | Latest Version | Type |
|---|---|---|
| CurseForge AutoDownload | v1.0.0 | Web Scraping |
| Dataset Collector | v4.0pre1 | Web Scraping |
| jpg to png Converter | v1.0.3 | Converter |
| Luna's Global Script | v1.0.3-r9 | Python Module |
| Picture Collector | v1.2.3 | Web Scraping |
| MP3 to wav Converter | v1.0.0 | Converter |
| Music Collector | β1 | Web  Scraping |
| Taskkiller for Minecraft | β2.1 | Unknown |
| Output Cleaner | β1.1 | Unknown | Windows |
