## rvc_visual_compare (Visual comparison of RVC result)
### [WARNING] This is Not a Auto-Compare Software!!!

---

### 使用法 (~v1 / ipynb mode)
1. 命名規則に従ったファイルを 指定位置(デフォルト:`rvc_visual_compare/target`) に移動

命名規則: `{number}-{model_name}-{based_fn}.{aud_format}` (デフォルト)

2. `generate_ipynb.bat` を実行 (必要であれば引数を追加)
3. 生成させた `{datetime}_note.ipynb` を Jupyter Notebook Viewer で開く

---

### 使用法 (~v1 / gradio mode)
1. 命名規則従ったファイルを指定位置に移動
2. `gradio_infer.bat` を実行
3. 表示されたリンクにアクセス (デフォルト: `localhost:7859`)

---

### 設定の変更
#### 設定の変更ツール
`edit_config_gui.bat` を実行し、表示されたリンクにアクセスすることでconfigマネージャーを起動できます

#### 設定の値及び概要
これら情報は `設定の変更ツール` にも記載されています

| 設定名 | 設定内部名 | デフォルト値 | 概要 |
| --- | --- | --- | --- |
| ファイル位置 | target_fp | "target" | 使用法1 にある指定位置。rvc_visual_compare からの相対パスだが、//から開始するとフルパスと認識する |
|
| ファイルの命名規則 | file_named_rule | "{num}-{model_name}-{based_fn}.{aud_format}" | <strong> 現状変更不可能！ </strong> 使用法1 にある命名規則。{model_name}, {based_fn}, {aud_format} がないとエラーを返す。{num} は任意追加。{aud_format}は mp3, wav, flac にのみ適用される |
| 生成ブックのパスの命名規則 | ipynb_dir_rule | "./ipynb/outputs" | Jupyter notebookの出力親パス名。変数は {datetime} のみが指定可能。 |
| 生成ブックの命名規則 | ipynb_name_rule | "{datetime}_note" | 使用法(ipynb mode)3にあるファイル名。変数は {datetime}, {model_name}, {sha} を受け付ける。すべては任意で {datetime}は現在時刻、{model_name}は`モデルの絞り込み`で指定されたモデル名、{sha}はランダム文字列の sha256。これらは {datetime} -> {model_name} -> {sha} の順に解析され、前のものでエラーが発生した場合、後ろの機能は動作しない |
| Gradio IP | gradio_ip | 0.0.0.0 | Gradio UIに使用するIP。?を指定すると Gradio に None を渡す |
| Gradio Port | gradio_port | 7859 | Gradio UIに使用するポート。?を指定するとGradio に Noneを渡す |
| luna's RVC-WebUIによるデータの取得 | lunapy_compatibility | false | オーディオと同じ名前の .info ファイルをそのオーディオの生成情報として評価モードの合計値の平均値、中央値の算出に使用する。現在は何の意味もない |
| 元ファイルの比較モード | based_file_compare | false | モデルではなく、変換に使用した元ファイルによる違いの比較を行う |
| Share UI | _ui_share | false | Gradio UIの share 引数の値。--share と引数に追加することでも設定可能 |
| 追加推論の無効化 | disable_additional_inference | true | 追加推論機能の無効化。無効化を行うと、PyTorch等のインポートも停止され、使用RAM量が大幅に軽減されたり、CUDA未インストール環境でも実行可能になる。 |


---
<br/>

#### Sys config
| 内部名 | 初期値 | 概要 |
| --- | --- | --- |
| ipynb_basic | "/ipynb/basic.ipynb" | 生成されるノートブックのテンプレート |
| md_template | "/ipynb/basic.md" | 生成されるmdのテンプレート |
| crt_method | "%Y%m%d%H%M%S" | datetime.datetime.now().strftime() にて使われる値 |


---

#### Changelogs
##### β1.0-r1 ipynb mode - full
+ ipynbモードのフルサポートを追加 (一部のグローバルconfigを除く)