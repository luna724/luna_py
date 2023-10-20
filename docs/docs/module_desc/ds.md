## Dataset Collector

`Docs: v1.0 | Dataset Collector: v4.0pre3`

`Latest Version: v4.0pre4`
`Support Ending Version: v4.0`


## - Feature

pjsekai キャラクターの会話音声を [sekai viewer](https://sekai.best) から取得。

セッションごとに 約30000 のリクエストを送信するため、何度も実行したりすることは非推奨


## Launch

[`./Scripts/dataset_collector_v4/launch_ui.bat`](/Scripts/dataset_collector_v4/launch_ui.bat) を実行
chromeなどで `127.0.0.1:25567` に接続

<br>

### Changelogs

- 4.0pre5 (Upcoming)
  - 他ユニットのサポート
  - CPUコア数に縛られない URL Status Checking (Multi)の実装
  - ID別にbase_filename を指定できるように 

- 4.0pre4 (Latest)
  - V4 main Release
  - WebUIを実装
  - aria2c のサポート
  - multiprocessingのサポート
  - ユニット: `MORE MORE JUMP!` のサポート

- None