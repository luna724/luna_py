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

lunapyでは Gradio を使用した 実行用ウェブインターフェース<details><summary>leak</summary>とFlask を利用した html でのうっすい説明(jp / (upcoming en))</details>の表示をサポートしています

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

### SD - PromptEasyMaker v1.1.2

- ControlNet Image を入力せずにWebUIから保存した場合 "None.png"ではなく "Nong.png" が入力され、FileNotFoundError がスローされる問題を解決
- V1 Method と V2.1 Method にて出力数が異なる問題を修正
- 正直どうでもいいものを多少修正


### MusicCollector v2pre2




