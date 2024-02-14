## DISCONTINUED: Music Collector

`Docs: None | Music Collector: v2pre2`

`Latest Version: v2pre2`
`Latest Preview Version: v2pre2`
`Support Ending Version: v2pre2`


## - Feature

pjsekai 収録曲の カバー / 原曲(Gamesize)を [Sekai Viewer / DNARoma](https://sekai.best) から取得。

フィルタによるが、セッションごとに最大 912 までしか送らないので、サーバー負荷は小さい
しかし、取得に Selenium / ChromeDriver を使用しているため、クライアント負荷は大きく、かかる時間も長い (MP非対応)

### 引数リスト / 説明
| arg | options | description |
| --- | --- | --- |
| --webui | `None` | WebUIの起動処理 |
| --unit | <details><summary>11 Options</summary>[*, leo/need, more more jump!, nightcode at 25ji, wonderlands×showtime, vivid bad squad, leo2, 25, mmj, vvbs, dasyo]</details> | 取得対象ユニットの指定 |
| --another_vocal | `None` | アナザーボーカル取得の有無 |
| --module | <details><summary>2 Options</summary>[v2, v1]</details> | モジュールモード |
| --virtual_singer | `None` | バーチャルシンガーの取得の有無 (原曲Gamesize) |
| --mode | <details><summary>2 Options</summary>[legacy, instant]</details> | --module 引数の旧型 |
| --noloop | `None` | 以前に取得した曲を再取得しない |
| --v1 | `None` | なにこれ |
| --info_arg | `None` | このリストをプロンプト上に出力する |
| --output | Music file Output path | 出力先を指定 |
| --share_webui | `None` | webuiの起動時に share オプションを追加する |
| --dev | `None` | 詳細なスクリプトの状態を出力する |



## Launch

[`./Scripts/MusicCollector/user_manual.bat`](/Scripts/MusicCollector/dev.bat) を実行
Gradio UI のポートは 25570 を使用　(`127.0.0.1:25570`)

<br>

### Changelogs

- v2pre2
  - Selenium 実行中に取得する Instant モードの実装