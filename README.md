# lunapy v1.1.0pre11

-----------
| Feature Name | Latest Version | Type |
|---|---|---|
| Audio Duration Calculator | v1.0pre3 | QoL |
| Audio Augmentation | v1.0.2 | Data Augmentation |
| Audio Properties Auto Setting | v1.1 | Macro |
| CurseForge AutoDownload | v2.6 | Web Scraping |
| Dataset Collector | v4.0pre3 | Web Scraping |
| jpg To png Converter | v1.1.1 | Converter ||
| Luna's Global Script | {version} | Python Module |
| Picture Collector | v1.2.4 | Web Scraping |
| MP3 To wav Converter | v1.1.0 | Converter |
| Music Collector | v1.0pre5 | Web  Scraping |
| Light Changer | v1.0 | QoL |
| SD Tool | v1.0 | QoL |
| RVC Tool | v1.0 | QoL |
| RVC webUI | v0 | QoL |
| json To Something | v1.1 | Converter |
| lunapy GradioUI | v1.0pre5 | QoL |

-----------

## 使用しているアプリたち

FFmpeg, SoX, Google Tesseract, ChromeDriver, cWebp

## 事前準備

スクリプトによっては FFmpeg, SoX, Tesseract, cwebp, ChromeDriver を要求するため、インストール+システム環境変数 "PATH" への追加

あとは old_setup.batを実行するだけ

## Changelogs

- RVC Tool v1.0
  - More Customizable WebUI
    - ddPn08氏による UI に追加してLRやその他いろいろと設定を行うことが可能なUI
    - まだゴミみたいな性能
    - 実装予定やらなんやらは Issue #5 を参照
    - RVC WebUI に移動

- RVC webUI v0
  - 実装アイテムやらなんやら [Issue #5](https://github.com/luna724/luna_py/issues/5)

- SD Tool (Scripts/sd_tool/*) v1.0
  - prompt_EasyMaker β2.5
    - Multiple Generation (Multidiffusion)のサポート
    - プロンプトデータセットの追加
    - Data Openerにてプロンプトに改行が含まれている場合正常に動作しない問題を修正
    - Template Generator (Two shot Mode) を追加
  - first_setup (NOT RELEASED)
    - WebUIが /content/stable-diffusion-webui/ にある場合にのみ初期情報を設定するもの
    - Negative, ADetailer Prompt, ADetailer Negative, Hires.fix にのみ対応予定

- json2n/model_setup v1.2
  - VAEのサポート
  - Checkpoint Information Viewer のサポート

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
