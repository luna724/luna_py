# lunapy v1.1.0pre12

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
- RVC WebUI (`./rvc_webui/webui-user.bat`)
- sd_tool / Prompt EasyMaker (`./Scripts/sd_tool/prompt_EasyMaker/webui.bat`)
</details>

## Changelogs (v1.1.0pre12)
- SD - PromptEasyMaker (v1.1)
  - Rename (SD_Tool/PromptEasyMaker -> SD - PromptEasyMaker)
  - Add All Database / Dataset into to .gitignore
  - Template Generator is Support Multiple Generation (can up to 2, that's multiple..?)
  - LoRA Database Setup Support in WebUI
  - Template Generator (Many Type Generator) can include ControlNet Options / Image
  - Template Generator (Many Type Generator) is can include Resolution / Checkpoint / CFG Scale / Sampler / Hires.fix Method (all optional) (Experimental: Single mode only module)

### Music Collector v1.0pre3 -> v2pre1

- Virtual Singerの取得の有無の設定
- ファイル名およびsingerの正しい取得をサポート
- upcoming
  - webuiの実装
  - ユニットごとに取得するかどうかを決める
  - Full versionをyoutubeから取得 