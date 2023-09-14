# lunapy v1.1.0pre10

-----------
| Feature Name | Latest Version | Type |
|---|---|---|
| Audio Duration Calculator | v1.0pre3 | QoL |
| Audio Augmentation | v1.0.2 | Data Augmentation |
| Audio Properties Auto Setting | v1.1 | Macro |
| CurseForge AutoDownload | v2.5 | Web Scraping |
| Dataset Collector | v4.0pre3 | Web Scraping |
| jpg To png Converter | v1.1.1 | Converter ||
| Luna's Global Script | {version} | Python Module |
| Picture Collector | v1.2.4 | Web Scraping |
| MP3 To wav Converter | v1.1.0 | Converter |
| Music Collector | v1.0pre5 | Web  Scraping |
| Light Changer | v1.0 | QoL |
| lunapy GradioUI | v1.0pre5 | QoL |

-----------

## 使用しているアプリたち

FFmpeg, SoX, Google Tesseract, ChromeDriver, cWebp

## 事前準備

スクリプトによっては FFmpeg, SoX, Tesseract, cwebp, ChromeDriver を要求するため、インストール+システム環境変数 "PATH" への追加

あとは old_setup.batを実行するだけ

## Changelogs

- Curseforge Autodownload v2.5
  - 細かな修正
  - マルチプロセスモードの実装
  - ランダム取得で1.16.5のサポート
  - 細かな変更

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

- Music Collector v1.0pre5 (-> v1.0)
  - ファイル名取得の完全サポート
  - MP3形式でのダウンロードのサポート
  - flacの初期の無音時間消去
  - ダウンロードフィルタの追加
  - mp3 to wav Converterの組み込みによる、flac2wavのサポート

- Picture Collector v1.2.3 (-> v1.3)
  - フィルタ設定の修正
  - ファイルのリネームの設定の見直し
  - Cwebpをちゃんとサポート

### 何のために作られたのか

私がpythonやそれに関係する様々な言語や内部的使用について理解、学習することを目的とした何とも言えんものとゴミの集合
