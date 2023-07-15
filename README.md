# 事前準備

**setup.bat** を実行する

# lunapy v1.1.0pre2

- curseforge-autodownload (v1.0.0)
- Dataset Collector V3 (v4.0pre2)
- jpg to png Converter (v1.0.3)
- Luna's Global Script (v1.1.0-r24)
- Picture Collector (v1.2.3)
- Music Collector (v1.0pre1)
- MP3 to wav Converter (v1.0.0)
- Taskkiller for Minecraft (β2.1)
- Output Cleaner (β1.1)

-----------


-----------

lunapy v1.1.0までに作るものたち

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
-----------
| Feature Name | Latest Version | Type |
|---|---|---|
| CurseForge AutoDownload | v1.0.0 | Web Scraping |
| Dataset Collector | v4.0pre2 | Web Scraping |
| jpg to png Converter | v1.0.3 | Converter |
| Luna's Global Script | v1.0.4-r11 | Python Module |
| Picture Collector | v1.2.3 | Web Scraping |
| MP3 to wav Converter | v1.0.0 | Converter |
| Music Collector | v1.0pre1 | Web  Scraping |
| Taskkiller for Minecraft | β2.1 | Unknown |
| Output Cleaner | β1.1 | Unknown | Windows |
