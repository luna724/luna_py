# lunapy v1.1.0pre8

-----------
| Feature Name | Latest Version | Type |
|---|---|---|
| Audio Duration Calculator | v1.0pre3 | QoL |
| Audio Augmentation | v1.0.2 | Data Augmentation |
| Audio Properties Auto Setting | v1.1 | Macro |
| CurseForge AutoDownload | v1.0.0 | Web Scraping |
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
  
- lunapy GradioUI v1.0pre5
  - JPG2PNG, Audio Duration Calculator, Audio Augmentation, Audio Properties Auto Setting のサポート
  - レイアウトの見直し

- Dataset Collector v4.0pre3
  - バーチャルライブからの取得をサポート
  - キャラクターストーリーからの取得をサポート
  - マルチプロセス化による取得時間の短縮
  - プロセス進行度、成功数などの可視化

- Audio Augmentation v1.0.2
  - 拡張適用確率を設定できるように

- Audio Duration Calculator v1.0pre3
  - 音声ファイルの合計時間を計算する
  - 特定の時間分のファイルの摘出する機能を追加
  
- Audio Properties Auto Setting v1.1
  - 実装
  - 音声ファイルのプロパティ (タイトル、アーティスト、アルバム、ジャンル、作曲者) の自動設定を行う
  - 作曲者の自動取得をサポート
  - 曲名をタイトルに代入をサポート

-----------

lunapy v1.1.0までに作るものたち

- Audio Augmentation v1.0 (-> v2.0)
  - 様々なオーディオ拡張の追加
  - 例: 音声反響、ピッチ変更2重ボーカル、正則化 etc..
  - ogg2wavによるoggのサポート
  - mp4などの動画ファイルからの音声摘出を利用したmp4のサポート

- Dataset Collector β4 (-> v5.0)
  - エミュレータ等を使用して5644Kbps(wav)での録音データの取得 (pyautogui)
    - いっちゃんだけの実装を予定
    - それ以外はファイル分けは手動
  - イベント分け
    - キャラによってそのキャラが一切喋らないイベントもあるので、指定されたIDに基づいた指定を行えるように
  - イベントURLの指定
    - 現在、Leo/need以外ユーザー処理になっているイベントの取得ベースURLをすべてexist_event.py url_dictに追加
  - サイレントモード
    - アウトプットプロンプトへの表示の抑制

- Curseforge autodownload v1.0.0 (-> v1.1)
  - クールダウンのユーザー側での指定
  - 変更されたCFのサイトへの対応

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
