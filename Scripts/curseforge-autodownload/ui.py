import gradio as gr
import pyautogui_mode
import new_main
import os
import random_get
from tkinter import Tk, filedialog
at_mcver_list = ["1.6.4", "1.7.10", "1.8.9", "1.10.2", "1.11.2", "1.12.2", "1.13.2", "1.14.4", "1.15.2", "1.16.5",
            "1.17.1", "1.18.2", "1.19.4", "1.20.1"]
dl_mcver = ["1.7.10", "1.12.2", "1.14.4", "1.16.5",
            "1.17.1", "1.18.2", "1.19.4", "1.20.1"]
vdate = "v2.5"

def preprocessing_auto(indata, cd, mcver):
  with open("./url_write_here.txt", "w") as f:
    f.write(indata)
  
  pyautogui_mode.launch(mcver, cd)

def browse_folder():
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()

    filename = filedialog.askdirectory()
    if filename:
        if os.path.isdir(filename):
            root.destroy()
            return str(filename)
        else:
            root.destroy()
            return str(filename)
    else:
        filename = "フォルダが選択されませんでした。"
        root.destroy()
        return str(filename)
      
# def preprocessing_en(indata, mcver, modname_search, search_engine, sm):
#   with open("./EN_f80fwa80d80afinsaxawioe2104ej1jw.txt", "w") as f:
#     f.write(indata)
  
#   new_main.main("./EN_f80fwa80d80afinsaxawioe2104ej1jw.txt", mcver, modname_search, search_engine, sm)
  
#   return "### Done."
  
def preprocessing_ja(indata, mcver, modname_search, search_engine, sm, of,
                    use_legacy, adblock, multi_count, target_loader):
  if multi_count == 1:
    use_multi = False
  else:
    use_multi = True
  
  with open("./jsondata/.txt", "w") as f:
    f.write(indata)

  new_main.main("./jsondata/.txt", mcver, modname_search, search_engine, sm, of, use_legacy, use_multi, adblock, multi_count, target_loader)
  
  return "### 処理終了"

with gr.Blocks() as iface:
  gr.Markdown(f"lunapy \n### Curseforge Autodownload {vdate}\n\
  Download mc-mod from Modrinth or Curseforge using MOD name or URL")
  
  with gr.Tab("通常ダウンロード"):
    gr.Markdown('''- Modrinthでは対応バージョンチェックは利用できません。\n
                  - Modrinthでは広告ブロッカーは利用できません。\n
                  - Modrinth, Legacy Curseforge では安定モードは利用できません。\n
                  - Curseforgeでは前提MODの自動ダウンロードは利用できません。(Legacy Curseforge の場合可能)\n
                  - マルチプロセスモードは実験段階です。''')
    ja_sm = gr.Checkbox(label="ダウンロードにMOD名を使用する", value=True)
    ja_indata = gr.Textbox(label="ダウンロードするMODの名前 または URL", max_lines=150, placeholder="MODの名前を使用する場合は、MOD名を使用するを有効化してください", lines=3)
    gr.Markdown("<br>")
    with gr.Row():
      ja_mcv = gr.Dropdown(label="Minecraftバージョン", choices=dl_mcver, value="1.12.2")
      ja_tl = gr.Dropdown(label="ModLoader", choices=new_main.available_modloader, value="Forge")
    ja_se = gr.Radio(choices=["modrinth.com", "curseforge.com"], label="MOD名の検索に使用するサイト", value="curseforge.com")    
    with gr.Row():
      jasm = gr.Checkbox(label="安定モード (有効化した場合、時間がかかる)", value=False, visible=False)
      jamulti_count = gr.Slider(1, 5, value=1, label="マルチプロセス実行数 (1で無効化) (Experimental)", step=1)
      jalegacy = gr.Checkbox(label="Legacy Curseforgeサイトを使う", value=False)
    with gr.Row():
      jamultimode = gr.Checkbox(label="マルチプロセスモード (Experimental)", value=False, visible=False)
      adblock_path = gr.Textbox(label="広告ブロッカー拡張機能manifestパス", value="E:/System/ichika/AppData/Local/Google/Chrome/User Data/Default/Extensions/cjpalhdlnbpafiamejdnhcphjbkeiagm")
      jaadblock = gr.Checkbox(label="広告をブロックする (Experimental)", value=False)
    with gr.Row():
      ja_outfile = gr.Textbox(label="ダウンロード先フォルダ", value="E:/System/ichika/Downloads")
      ja_brbtn = gr.Button("フォルダ選択")
      ja_brbtn.click(fn=browse_folder,
                    outputs=ja_outfile)
    
    ja_btn = gr.Button("スタート")
    ja_out = gr.Markdown("")
    ja_btn.click(fn=preprocessing_ja,
                inputs=[ja_indata, ja_mcv, ja_sm, ja_se, jasm, ja_outfile, jalegacy, jaadblock, jamulti_count, ja_tl],
                outputs=ja_out)
  
  with gr.Tab("自動操作ダウンロード"):
    gr.Markdown('''- PCが操作できなくなります''')
    auto_url = gr.Textbox(label="ダウンロードするMODのURL", max_lines=50, placeholder="URLを一行づつペースト OneTabが後ろにつけるものは消さなくてもよい", lines=10)
    at_mcver = gr.Dropdown(label="Minecraftバージョン", choices=at_mcver_list, value="1.12.2")
    auto_cd = gr.Slider(0.1, 3, value=1.25, step=0.01, label="クールダウン設定 (2秒以上推奨)")
    gr.Markdown("<br>")
    auto_btn = gr.Button("スタート")
    gr.Markdown("# Chromeをフルスクリーンにして選択してください \n\
# 選択後、スクリプトの終了まで操作しないでください")
    auto_btn.click(fn=preprocessing_auto,
                  inputs=[auto_url,auto_cd,at_mcver]
                  )
    
  with gr.Tab("ランダムダウンロード"):
    gr.Markdown('''- ダウンロード先はCurseforgeのみ対応\n
              - Forgeのみ対応\n
              - 開始したら、フルスクリーンの大きさ90%のChromeを表示して放置してください''')
    rd_mcv = gr.Dropdown(label="Minecraftバージョン", choices=["1.12.2", "1.16.5"], value="1.12.2")
    # rd_sortby = gr.Dropdown(label="ソート順 (Curseforge)", choices=["Relevancy (関連順)", "Popularity (人気順)", "Latest update (最終更新日時順)", "Creation Date (作成順)", "Total Downloads (ダウンロード数順)", "A-Z (アルファベット順)"], value="Popularity")
    rd_database = gr.Radio(choices=["500MOD", "5000MOD", "10000MOD (1.16.5のみ)"], value="5000MOD")
    rd_randtar = gr.Slider(0, 10000, step=1, label="抽選対象数", value=5000)
    rd_chance = gr.Slider(0.01, 100, value=0.1, label="抽選チャンス (%)", step=0.01)
    rd_modc = gr.Slider(0, 1250, value=25, label="MOD数", step=1)
    
    gr.Markdown("<br>")
    with gr.Row():
      rd_btn = gr.Button("ロール")
      rd_stn = gr.Button("ダウンロードスタート")
    rd_out = gr.Markdown("")
    rd_stn.click(fn=pyautogui_mode.launch,
                inputs=[rd_mcv, auto_cd])
    rd_btn.click(fn=random_get.choice_,
                inputs=[rd_mcv, rd_randtar, rd_chance, rd_modc, rd_database],
                outputs=rd_out)
    
  with gr.Tab("クラレポ解析"):
    gr.Markdown("- GPTを使用し、crash_report.txtからクラッシュ原因を突き止める\n\
      - GPTを使用しない場合、NoClassFoundError(前提MOD不足) のみ取得可能")
    
    gr.Markdown("")
    cr_use_gpt = gr.Checkbox(label="GPTを使用して解析能力を強化", value=True)
    cr_apikey = gr.Textbox(label="OpenAI APIKey")
    cr_model = gr.Radio(choices=["GPT-3.5 turbo", "GPT-3.5 text-davinci-002", "GPT-4 turbo (Experimental)"], label="使用モデル (GPT-4の使用には ChatGPT Plus が必要)", value="GPT-3.5 turbo")
    cr_autoget = gr.Checkbox(value=False, label="MOD名の自動取得")
    
    with gr.Accordion("追加設定 (書かなくてもいい)"):
      with gr.Row():
        cr_mcver = gr.Dropdown(choices=at_mcver_list, label="Minecraftバージョン", value="N/A")
        cr_loader = gr.Dropdown(choices=["Forge", "Fabric", "Quilt", "NeoForge"], label="ModLoaderタイプ", value="N/A")

iface.launch(inbrowser=True, server_port=7600)