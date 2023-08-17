# lunapy v1.1.0pre7

-----------
| Feature Name | Latest Version | Type |
|---|---|---|
| CurseForge AutoDownload | v1.0.0 | Web Scraping |
| Dataset Collector | v4.0pre2 | Web Scraping |
| jpg To png Converter | v1.1.0 | Converter |
| Luna's Global Script | v2.0.1 | Python Module |
| Picture Collector | v1.2.3 | Web Scraping |
| MP3 To wav Converter | v1.1.0 | Converter |
| Music Collector | v1.0pre5 | Web  Scraping |
| Taskkiller for Minecraft | β2.1 | Unknown |
| Quick Launcher | v1.0pre1 | Launcher |
| Light Changer | v1.0 | QoL |
| Audio Augmentation | v1.0.1 | Data Augmentation |
| lunapy GradioUI | v1.0pre2 | QoL |

-----------

## 参考、使用、パクったコードやアプリたち

FFmpeg, SoX, Google magenta Code, Google Tesseract, cWebp

## 事前準備

スクリプトによっては FFmpeg, SoX, Tesseract, cwebp を要求するため、インストール+システム環境変数 "PATH" への追加

あとは old_setup.batを実行するだけ

## Changelogs

- Audio Augmentation v1.0.1
  - 一部非対応の拡張関数を無効化
  
- lunapy GradioUI v1.0pre2
  - LightChanger, Audio Augmentationの対応

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
