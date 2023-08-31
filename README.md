# lunapy v1.1.0pre9

-----------
| Feature Name | Latest Version | Type |
|---|---|---|
| Audio Duration Calculator | v1.0pre3 | QoL |
| Audio Augmentation | v1.0.2 | Data Augmentation |
| Audio Properties Auto Setting | v1.1 | Macro |
| CurseForge AutoDownload | v2.1 | Web Scraping |
| Dataset Collector | v4.0pre3 | Web Scraping |
| jpg To png Converter | v1.1.1 | Converter |
| Luna's Global Script | v2.0.1 | Python Module |
| Picture Collector | v1.2.4 | Web Scraping |
| MP3 To wav Converter | v1.1.0 | Converter |
| Music Collector | v1.0pre5 | Web  Scraping |
| Taskkiller for Minecraft | β2.1 | Unknown |
| Quick Launcher | v1.0pre1 | Launcher |
| Light Changer | v1.0 | QoL |
| lunapy GradioUI | v1.0pre5 | QoL |

-----------

## 参考、使用、パクったコードやアプリたち

FFmpeg, SoX, Google magenta Code, Google Tesseract, ChromeDriver, cWebp

## 事前準備

スクリプトによっては FFmpeg, SoX, Tesseract, cwebp, ChromeDriver を要求するため、インストール+システム環境変数 "PATH" への追加

あとは old_setup.batを実行するだけ

## Changelogs

- Curseforge Autodownload v2.1
  - クールダウンの指定を可能に
  - WebUIの対応
  - MOD名のみでダウンロードを可能に
  - Seleniumを利用したWebDriverによる画面の動きを制限しない取得をサポート
  - Modrinthをサポート
  - Versionチェックをサポート
  - 前提MODの取得をサポート
  - ランダム取得をサポート  

-----------

lunapy v1.1.0までに作るものたち

- Curseforge autodownload v1.0.0 (-> v2)
  - クールダウンのユーザー側での指定
  - 変更されたCFのサイトへの対応
  - MOD名のみを入力するだけでダウンロードできる機能を追加

- Music Collector v1.0pre5 (-> v1.0)
  - ファイル名取得の完全サポート
  - MP3形式でのダウンロードのサポート
  - flacの初期の無音時間消去
  - ダウンロードフィルタの追加
  - mp3 to wav Converterの組み込みによる、flac2wavのサポート

- Picture Collector v1.2.3 (-> v1.3)
  - フィルタ設定の修正
  - ファイルのリネームの設定の見直し

### 何のために作られたのか

私がpythonやそれに関係する様々な言語や内部的使用について理解、学習することを目的とした何とも言えんものとゴミの集合
