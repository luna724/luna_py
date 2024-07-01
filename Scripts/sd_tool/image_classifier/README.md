## Image Classifier / 画像分類機

### 概要
特定パスに含まれる画像を、Deepbooruを用いて分類する

### 実行方法
0. 事前インストールしたい Deepbooru モデルがある場合、/dd_models/any.t4 のように /dd_models/ 内に入れておく (プロジェクトも読み込み可)
1. `launch.bat` を介してファイルを実行
2. <a href="localhost:7855"> localhost:7855 </a> に接続
3. 設定し、実行
4. 出力パスを見に行く


### config.json 説明
WebUIでは変更をサポートしていない変数などが入っている

説明
| Key | Default Values | type | summary |
| --- | --- | --- |
| model_directory  | "dd_models" | str | Deepdanbooruモデルの検出親ディレクトリ(相対パス) |
| custom_tags" | [] | List[str] | Deepdanbooru のカスタムタグ。主に自作プロジェクト用 |
| cache | {..} | Dict[v: k, ..] | WebUI引数のキャッシュ。次回以降の入力の手間を省く |
| use_model_cache | true | bool | modelのキャッシュを行うかどうか。falseの場合、各画像につきモデルが読み込まれるため非常に速度が落ちる |
| $Version | null | None (or) str | config.jsonのバージョン |

### 他モジュールとの連携機能
なし
