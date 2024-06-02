# lunapy

<details> <summary> !WARNING! </summary>
Do not use modules that were previously committed in this repositories and have now been removed(Archived doesn't including "removed".).
They have been deemed problematic for distribution.
I will not be liable for any and all damages caused by their use by third parties.

If you know of any existing ones that you deem problematic for distribution, please contact me.

/

このリポシトリで過去にコミットされていて、現在削除(アーカイブ化は「削除」に含まれません)されているモジュールは使用しないでください。
それらは配布するには問題があると判断したものです。
それらを第三者が使用することによって生じた全ての損害に対して私は一切の責任を負いません。

現存しているもので配布には問題があると判断されるものがある場合、連絡してください。

Provide / Translated by. ChatGPT
</details>


-----------

<h2> <center> 機能リスト (アーカイブは除く) </center></h2>

| モジュール名 | 詳細 |
| --- | --- |
| Auto chrome | chromedriver と起動エンジンを提供し、 SeleniumによるChromeの自動化をサポートするツール。ビルドインモジュールは 3 つ | v1-selenium4 |
| jpg2png Converter | 画像フォーマットを変換するツール。 jpg>png 以外もサポートしている | v1.1.1 |
| LightChanger | Windowsの明るさを変更する。 | v1.1 |
| wav2mp3 Converter | 音声フォーマットを変換するツール。 多分動かない | v1.1.0 |
| SD Tools | Stable-Diffusion に関する外部ツールを内蔵。 Audio Tools とは違い All in one ではない | - |
| SD-PEM | SD Tools/prompt_EasyMaker の略称。 <br />主に様々なテンプレに沿ってプロンプトを効率的に形成するもの <br/>現在luna_pyで活発的に開発されている唯一のモジュールだったので独立した |
| RVC Visual Compare | 命名規則に従った音声ファイルを ipynb および gradio で評価できるようにするツール |

<details> <summary> 詳細なリスト </summary>

| モジュール名 | 最新ver | 最新更新日 | 関数モードの有無 | WebUIの有無 | アーカイブ化 | 開発中か | ライセンス | APIモード |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Audio augmentation | v1.0.2 | [2023/09/02](https://github.com/luna724/luna_py/commit/85a728a80a83f26f26720b1845fb52145cfb2621) | ✅ | × | ✅ | × | MIT | × |
| Audio length calculator | v1.0pre3 | [2023/08/26](https://github.com/luna724/luna_py/commit/56e77137f8844af20d4c794fbb02c41f10e19066) | ✅ | ✅ | ✅ | × | MIT | × |
| Audio tools | - | [2023/12/15](https://github.com/luna724/luna_py/commit/f9998fa5c89d7675ba1925474fe3d46b3fb17f9b) | ✅ | ✅ | ✅ | × | MIT | × |
| Auto chrome | v1-selenium4 | [2024/04/28](https://github.com/luna724/luna_py/commit/463b5cb7d054e695258b34017a2c5def1438cbf0) | ✅ | × | × | ✅ | MIT | △ (拡張機能を前提としている) | 
| JPG2PNG Converter | v1.1.1 | [2023/09/02](https://github.com/luna724/luna_py/commit/85a728a80a83f26f26720b1845fb52145cfb2621) | ✅ | ✅ | × | × | MIT | × |
| LightChanger | v1.1 | [2024/01/09](https://github.com/luna724/luna_py/commit/2ddbe38f0ced862d047350fb85b3fbe38668c9cd) | ✅ | × | ✅ | × | MIT | × |
| WAV2MP3 Converter | v1.1.0 | [2023/08/11](https://github.com/luna724/luna_py/commit/b2f631256a3bc167476b1b444e337c05fbe6f233) | ✅ | × | ✅ | × | MIT | × |
| SD Tools/dataset utils | - | [2024/01/16](https://github.com/luna724/luna_py/commit/7667148df490f441af885edc5eda8119b3907365) | × | ✅ | × | ✅ | MIT | × |
| SD-PEM | β4.0-CE-preview | [2024/05/13](https://github.com/luna724/luna_py/commit/bee0413d98b6ad522ccfa73a6a7986a68e87ff99) | ✅ | ✅ | × | ✅ | AGPL-3.0 | △ (SDPDBに対してのみ) |
| Prax config switcher | v1.2 | [2024/02/17](https://github.com/luna724/luna_py/commit/509e45a1cf714be9b31c6fcb95eb1e8d3c756be1) | ✅ | ✅ | ✅ | × | MIT | × |
| LGS (Luna's Global Scripts) | - | [2024/04/04](https://github.com/luna724/luna_py/commit/70ca9a7a2a2916ff41e4addb1b9f2e44b8591ed5) | ✅ | × | × | ✅ | MIT | ✅ (pythonモジュール) |
| RVC Visual Compare | β1.0-r1 ipynb - full | [2024/06/02](https://github.com/luna724/luna_py/commit/4620853dd4bb30932e3b3b424d2b0f66767d7949) | ✅ | × | × | ✅ | MIT | × |

</details> 

---

## 依存関係

<details><summary> FFmpeg </summary>
<a href="https://ffmpeg.org"> <center> 公式サイト (ffmpeg.org) </center> </a><br />
<a href="https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z">  <center>  >> ダウンロード (win-7.0-full) <<  </center> </a>
<br />
<a><h4>必要とするモジュール</h4></a>

| モジュール名 | 要求バージョン (テスト済み) |
| --- | --- |
| Audio Augmentation | full-7.0+ |
| Audio-length calculator | full-7.0+ |
| Audio properties Auto generator | full-7.0+ |
| Audio tools | full-7.0+ |
| mp3 to wav Converter | full-7.0+ |
| lunapy webui | full-7.0+ |


</details>

<details><summary> SoX </summary>
<a href="https://sox.sourceforge.net"> <center> 公式サイト (sourceforge) </center> </a> <br />
<a href="https://sourceforge.net/projects/sox/files/latest/download"> <center> >> ダウンロード (sourceforge) << </center></a>
<br />
<a><h4>必要とするモジュール</h4></a>

| モジュール名 | 要求バージョン (テスト済み) |
| --- | --- |
| Audio Augmentation | 14.4.2-win32+ |


</details>

<details><summary> Windows OS </summary>
<a href="https://www.microsoft.com/ja-jp/software-download/windows10"> <center> 公式サイト (microsoft) </center></a><br />
<a href="https://www.microsoft.com/ja-jp/software-download/windows10ISO"> <center> >> ダウンロード << </center></a>
<br />
<a><h4>必要とするモジュール</h4></a>

| モジュール名 | 要求バージョン (テスト済み) |
| --- | --- |
| Light Changer | win10-Pro (AMD64bit)+ |
| Auto chrome (Automatic Chromedriver installerのみ) | Chrome driverがサポートするすべてのwindows (64bit) なくても手動でインストールすることで実行可能 |


</details>

