import os
import pyautogui
import psutil
import subprocess
import luna_GlobalScript.runner.app.chrome_controlMode as chrome
import luna_GlobalScript.project_sekai.analyser.any_id_analyser as analyse_member_id
import luna_GlobalScript.project_sekai.analyser.charactor_analyser as analyse_member
import luna_GlobalScript.project_sekai.analyser.unit_analyser as analyse
import luna_GlobalScript.project_sekai.dataset as pjdata
import luna_GlobalScript.autogui.chrome_optimizer.url_moving as move
import luna_GlobalScript.autogui.chrome_optimizer.clicker as click
import time
import requests

# Debug
mx = 1440
my = 900
isInput = True
isInput = input("入力確認処理を行いますか？\n(デフォルト Leo/need, 星乃一歌 フィルタ)\nTrue / False: ")

if isInput == "True":
    print("processing..")
elif isInput == "False":
    print("Selected: False\nprocessing..")

# ユーザ入力
# charactor (キャラフィルタ検出処理 一部キャラ非対応 選択したものだけ表示)
charactor = str(input("キャラクターの選択フィルタ 名前、またはID(例: ichika)\n(Noneで無効化): "))
unit_select = str(input("ユニットフィルタ ユニット名、またはID(例: Leo/need)\nこれを選択した場合、キャラクターフィルタは適用されません。: "))
use_emulator = input("エミュレータ(ChromeDriverによる仮想環境)での実行 (非推奨)\n(True / False): ")
filter_mv = str(input("2DMBなどのありなしフィルタ(例: 3DMV)\n(3DMV / 2DMV / Original-MV / Static-Image / None): "))
print_only = input("楽曲名や、アーティスト情報だけの書き出し\n(True / False): ")

# 処理
if print_only == "True" or print_only == "False":
    NA = 0
else:
    print("print_onlyの値を正常に入力してください。(True / False)")
    exit("Can't Running Syntax")
if use_emulator == "True" or use_emulator == "False":
    NA = 0
    if use_emulator == "True":
        cdriver = input("Chromeドライバのフルパスを入力: ")
else:
    print("use_emulatorの値を正常に入力してください。(False)")
    exit("Can't Running Syntax")
if unit_select == "Virtual Singer":
    print("Virtual Singerは現在未実装です。")
    exit()
else:
    unit_select_status = analyse.full(unit_select, True)
    if unit_select_status in pjdata.unit_list:
        unit = pjdata.unit_list.get(unit_select_status)
        unit_select_status = "True"
    else:
        unit_select_status = "False"

if unit_select_status == "Unknown" or unit_select_status == "False":
    member_check = True
    member = analyse_member.full(charactor, False, "Ro-ma")
    member_id = analyse_member_id.full(charactor, False, "str")
    member_name = analyse_member.full(charactor, False, "ja")
elif unit_select_status == "True":
    print("Unitフィルタがオンのため、キャラクターフィルタのチェックはスキップされました。")
    member = ""
    member_id = ""
    member_check = False

else:
    print("Noneまたは何かしらの一致しない値の入力が検知されたため、キャラクターフィルタのチェックはスキップされました。")
    member_check = False

if filter_mv == "3DMV" or "2DMV" or "Static-Image" or "Original-MV" or "None":
    NA = 0
else:
    print("filter_mvの値を正常に入力してください。(None / 3DMV / 2DMV / Static-Image / Original-MV)")
    exit("Can't Running Syntax")

# 関数を呼び出し
Err = False
url = "https://sekai.best/music"

# URLが生きてるかの処理
print('Trying to get Response..')
response = requests.get(url)
if response.status_code == 200:
    print(f"Success (Response:{response.status_code})\n")
else:
    print(f"Failed (Response:{response.status_code})\n")

# 初期処理
# subprocess(chrome.summon)
def waiting(cd):
    print("Chromeを選択状態にしてください。")
    time.sleep(cd)

# 操作
waiting(20)

# 選択中のプロセスの実行ファイル名を取得
selected_process_path = psutil.Process().exe()
selected_process_filename = os.path.basename(selected_process_path)
print(f"Process: {selected_process_filename}") # Process: chrome.exe
if selected_process_filename == "chrome" or selected_process_filename == "Chrome" or selected_process_path == "Chrome.exe": # Google Chromeかどうかを検知
    print(f"Success Inject to {selected_process_filename}")
else:
    print("選択状態にないか、実行ファイル名が \"chrome.exe\"でありません。")
    if Err == True:
        exit("実行に二回失敗しました。")
    Err = True
    waiting(30)

# 新しいタブを呼び出し
checker = move.goto(url, True, 600, 50, mx, my)

while check == True: # 関数処理が終わったかチェック
    if checker == "Done":
        check = True
        break
    else:
        check = False

    time.sleep(3)

# メイン処理
# フィルタの確認 # Pos: 1350, 220
time.sleep(5) # 5秒間の待機処理

if member_check == False and unit_select_status == "False" and filter_mv == "None":
    NA = 0 # フィルタ機能の設定をスキップ
else:
    click.click(1350, 220, mx, my)  # 1350, 220を各解像度に対応させ、クリック
    if member_check == False:
        if unit_select_status == "False":
            if filter_mv == "3DMV": # Pos 415, 415
                click.click(415, 415, mx, my)
            elif filter_mv == "2DMV": # Pos 490, 415
                click.click(490, 415, mx, my)
            elif filter_mv == "Static-Image": # Pos 675, 415
                click.click(675, 415, mx, my)
            elif filter_mv == "Original-MV": # Pos 572, 415
                click.click(572, 415, mx, my)
            else:
                print("Error in main.py  Filter_MV Check")
                exit()
        elif unit_select_status == "True":
            if unit == "Leo/need": # 480, 365
                click.click(480, 365, mx, my)
            elif unit == "MORE MORE JUMP!": # 800, 325
                click.click(800, 325, mx, my)
            elif unit == "Vivid Bad Squad": # 512, 325
                click.click(512, 325, mx, my)
            elif unit == "Nightcode": # 1110, 325
                click.click(1110, 325, mx, my)
