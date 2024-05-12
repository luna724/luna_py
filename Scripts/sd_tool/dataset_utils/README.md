## Dataset utils
Stable-diffusion の主に Kohya-ss を使った LoRA のトレーニングをアシストするツール

### 機能一覧

#### Image scraping
Google画像検索 または Google検索で出てきた画像ファイルを取得する
`Powerful Pixiv Downloader` で取得した画像を処理することも可能

保存されるファイル名のパターン
`{ファイル番号:d06}-{検索語句 / またはユーザー定義 / またはスクリプト実行開始時間}.{png / jpg / keep}`

起動方法 (WebUI)
`python launch.py --m image_scraping --webui`

起動方法 (without WebUI)
`python launch.py --m image_scraping --image {画像検索対象パス または Google検索語句 または Pixiv Downloader の出力先ディレクトリ} --fn {ファイル名 (任意)} --ext {ファイル拡張子 (png / jpg / keep(キープ)) (任意 デフォルト: png)} --manual_cd {クールダウンの時間 (任意)} --safemode --api `

| 引数 | 値 | 概要 | 要求 | デフォルト |
| --- | --- | --- | --- | --- |
| --image | - | 画像検索に使用する画像のパス または<br />Google検索語句 または<br />Pixiv Downloader の出力先ディレクトリ | ✅ | None |
| --fn | FileName | 保存画像に使用するファイル名 | × | None |
| --ext | [png / jpg / keep] | ファイル拡張子 keep の場合 ダウンロード時の拡張子をキープする | × | png |
| --manual_cd | float / int | 画像ごとのクールダウンの時間 | × | None |
| --safemode | なし | 指定した場合、1枚取得するたびに保存を行う。速度は遅くなるが、スクリプトにエラーが発生した際に今までの取得情報が消滅しない | × | False |
| --api | なし | WebUIを使用しないことを明確に表記する | × | False |

---