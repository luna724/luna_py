# 何のために作られたのか

私がpythonやそれに関係する様々な言語や内部的使用について理解、学習することを目的とした何とも言えんものとゴミの集合

# 参考、使用、パクったコードやアプリたち

FFmpeg, SoX, google-magenta sourceCode

# 事前準備

スクリプトによっては FFmpeg, SoX, Tessetactを要求するため、インストール+システム環境変数 "PATH" への追加

あとは old_setup.batを実行するだけ

# lunapy v1.1.0pre6

-----------
| Feature Name | Latest Version | Type |
|---|---|---|
| CurseForge AutoDownload | v1.0.0 | Web Scraping |
| Dataset Collector | v4.0pre2 | Web Scraping |
| jpg to png Converter | v1.0.3 | Converter |
| Luna's Global Script | v2.0.1 | Python Module |
| Picture Collector | v1.2.3 | Web Scraping |
| MP3 to wav Converter | v1.0.0 | Converter |
| Music Collector | v1.0pre5 | Web  Scraping |
| Taskkiller for Minecraft | β2.1 | Unknown |
| Quick Launcher | v1.0pre1 | Launcher |
| Light Changer | v1.0 | QoL |
| Audio Augmentation | v1.0pre2 | Data Augmentation |
| lunapy GradioUI | v1.0pre1 | QoL |

-----------

# Changelogs

- Music Collector v1.0pre4 -> v1.0pre5
  - ファイル名取得のサポート
  - Wav変換、MP3変換のサポート

-----------

lunapy v1.1.0までに作るものたち

- Audio Augmentation v1.0pre3 (-> v1.0)
  - 様々なオーディオ拡張の追加
  - 例: 音声反響、ピッチ変更2重ボーカル、正則化 etc..
  - FFmpeg, SoXの組み込み
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

- Curseforge autodownload v1.0.0 (-> v1.0.1)
  - クールダウンのユーザー側での指定

- jpg to png Converter v1.0.3 (-> v1.1)
  - もっとたくさんのパターンを追加したい

- Music Collector β1 (-> v1.0)
  - そもそも動かんから作成
  - flac, MP3形式でのダウンロードのサポート
  - flacの初期の無音時間消去
  - ダウンロードフィルタの追加
  - それでもバラバラなので、構造的にpyautogui, bs4, chromedriverでは厳しそう

- Picture Collector v1.2.3 (-> v1.3)
  - 特訓後、特訓前、両方の設定をしっかりと
  - ファイルのリネームの設定の見直し

- 

