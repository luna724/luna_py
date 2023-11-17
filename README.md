# lunapy

-----------
## Feature List

[This list is Not Supported. <br>Feature list is Moved to module_description.md](./docs/docs/module_description.md)


-----------

## 使用しているアプリやコードたち

- [`FFmpeg`](https://ffmpeg.org/)
- [`SoX`](https://sox.sourceforge.net/)
- [`ChromeDriver`](https://chromedriver.chromium.org)
- [`Aria2`](https://github.com/aria2/aria2)
- [`Google / Tessseract`](https://github.com/tesseract-ocr/tesseract)

## 事前準備

スクリプトによっては FFmpeg, SoX, Tesseract, cwebp, ChromeDriver を要求するため、インストール+システム環境変数 "PATH" への追加

あとは old_setup.batを実行するだけ

## WebUI

lunapyでは Gradio を使用した 実行用ウェブインターフェースと
Flask を利用した html でのうっすい説明(doc)の表示をサポートしています

GradioUI は `launch_webui.sh` を
Flask での Docstring の表示は `what_is_lunapy？.sh` を実行すると開くことができます。

<details> <summary> <strong> Windowsなんだけど？ </strong> </summary> 
Windows環境の場合 Git Bash を使用して Shell Script を実行することができます
</details>

<details><summary> その他のUI </summary>
- Curseforge_Autodownload (`./Scripts/curseforge-autodownload/ui.bat`)
- sd_tool / Prompt EasyMaker (`./Scripts/sd_tool/prompt_EasyMaker/webui.bat`)
</details>

## Changelogs

### SD - PromptEasyMaker v1.1.1

- V2 Methodにて CFG Scale,  Header Additional, Lower Additionalが動作していない問題を修正
- webuiの誤字を修正
- V1 Methodのデータを生成モードにて使用できない問題を修正 ([#6](https://github.com/luna724/luna_py/issues/6))
- comma duplicate deleter を修正
- ControlNet画像にて何も設定されていない場合にエラーが発生する問題を修正
- LoRA Database Setup セーブ時にキー名が "loraname" になる問題を修正