# lunapy v1.1.0pre12

-----------
| Feature Name | Latest Version | Type |
|---|---|---|
| Audio Duration Calculator | v1.0pre3 | QoL |
| Audio Augmentation | v1.0.2 | Data Augmentation |
| Audio Properties Auto Setting | v1.1 | Macro |
| CurseForge AutoDownload | v2.6 | Web Scraping |
| Dataset Collector | v4.0pre3 | Web Scraping |
| jpg To png Converter | v1.1.1 | Converter |
| Luna's Global Script | {version} | Python Module |
| Picture Collector | v1.2.4 | Web Scraping |
| MP3 To wav Converter | v1.1.0 | Converter |
| Music Collector | v1.0pre5 | Web Scraping |
| Light Changer | v1.0 | QoL |
| SD Tool | v1.0 | QoL |
| RVC Tool | v1.0 | QoL |
| RVC WebUI | v0.1 | QoL |
| json To Something | v1.1 | Converter |
| lunapy GradioUI | v1.0pre5 | QoL |

-----------

## 使用しているアプリやコードたち

- [`FFmpeg`](https://ffmpeg.org/)
- [`SoX`](https://sox.sourceforge.net/)
- [`ChromeDriver`](https://chromedriver.chromium.org)
- [`Aria2`](https://github.com/aria2/aria2)
- [`Google / Tessseract`](https://github.com/tesseract-ocr/tesseract)
- [`ddPn08 / RVC-WebUI`](https://github.com/ddPn08/rvc-webui)

## 事前準備

スクリプトによっては FFmpeg, SoX, Tesseract, cwebp, ChromeDriver を要求するため、インストール+システム環境変数 "PATH" への追加

あとは old_setup.batを実行するだけ

## Changelogs (v1.1.0pre12)

- RVC WebUI v0.2
  - ALL Changelogs [Issue #5](https://github.com/luna724/luna_py/issues/5)

-----------

lunapy v1.1.0までに作るものたち

- Luna's Global Script
  - 旧Import名Luna_GlobalScriptを完全廃止

- Curseforge autodownload v2.1 -> v3
  - ModrinthのMCVerチェック対応
  - マルチプロセスモードの実装
  - マルチプロセス数の設定
  - Crash Reportの解析ツールの追加 (主に 前提MOD不足をキャッチ)
  - API Link Cacheからの検索を行わない拘束取得のポート

- Picture Collector v1.2.3 (-> v1.3)
  - フィルタ設定の修正
  - ファイルのリネームの設定の見直し
  - Cwebpをちゃんとサポート

### WebUIの実行
  `launch_webui.bat`を実行