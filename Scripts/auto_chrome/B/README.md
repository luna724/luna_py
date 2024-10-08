## Auto chrome
launch.py が最新の `chromedriver` を提供し、Chromeの作業を自動化する

### 使用方法
`auto_chrome/{mode_name}` にディレクトリを作成
ディレクトリ内に呼び出し元となる `launch.py` を作成し、その中に `def launch(url=None)` 関数を追加
ルートにある `launch.py` から DRIVER_PATH などをインポートしてChromeの自動化を行う。<br/>
そのモードで使用するURLが一定の場合、if url == "auto" の処理を行うことで --url 引数を簡略化できたりもするが<br/>
このスクリプトに柔軟性はないため、カスタマイズできる部分は少ない

### builtins mode

| mode_name | desc | auto_url |
| --- | --- | --- |
| tokyo_shoseki | 東京書籍教科書授業インターネット講座の再生を自動化する。実行には別途 `tokyo_shoseki/login_data.json` の書き込みが必要 | enable |
| example | url に与えられた値を google.com で検索する | enable |


<details> <summary> モジュールの作り方 </summary>
1. <code>auto_chrome/</code> にモジュール名のディレクトリを作る
2. その中に <code>launch.py</code> を作成し、その中にurlとargsを引数として受け取る <code>launch 関数</code>を作成
例:
<code>
def launch(url=None, argparse_args=None) -> None:
  print("Data obtained!\nurl: ", url)
</code>

### 引数の追加
argparse の parser へ引数を追加し、スクリプトに渡したい場合は
<code>module_root/parser.py:\<function preload\></code> を作成。
例:
<code>
# parser.py
def preload(parser) -> None:
  parser.add_argument("--example_argument", required=False, default="")

</code>

</details>