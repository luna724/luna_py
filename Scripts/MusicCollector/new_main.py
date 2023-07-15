import os
import pyautogui as pygui
import subprocess
import time
import requests
import pyperclip as pyclip
import luna_GlobalScript.autogui.convertRGBToHex as convert
import webbrowser
import mv_filtering as mvf
import luna_GlobalScript.autogui.clicker as click
import luna_GlobalScript.project_sekai.unit_charactor_analyser.id.any_roma2idxname as lunaidanalyse
import luna_GlobalScript.misc.compact_input as compact
import luna_GlobalScript.misc.output_folder as out_gen
from luna_GlobalScript.misc.global_math import cursor_relative_position as relative
import win32gui
from luna_GlobalScript.misc.global_math import cursor_exchanger as cur

isWhite, end = False, False
a = 0
mx, my = 1440, 900 # デフォルトのx, y の値
def lowfile_remover(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and filename.lower().endswith(".txt"):
            if os.path.getsize(filepath) < 1:  # ファイルサイズが1bytes未満の場合
                os.remove(filepath)
                print(f"Deleted: {filename}")
def ez_click(x, y):
    click.click(x, y, mx, my, False)

# 入力処理
members = str(input("取得したいキャラクターまたはユニット (未入力で全員)\n (e.g: ichika) or (e.g: Leo/need): "))
filter_mv = str(input("MVタイプのフィルタを行いますか? (0 or 1): "))
ExperimentalMode = input("実験的モード (非推奨) (True / False / ?): ")

# 実験モードのプリントアウト
if ExperimentalMode == "?":
    print("""
    実験的モードとは                             \n
現在開発中の、画面操作機能を使用したモードです。    \n
例外処理やif文処理等が不完全なため、実験的モードとしての\n
実装をしている。                                  \n
""")
    ExperimentalMode = input("実験的モード (非推奨) (True / False): ")    
# 前処理
if not members == "": # 入力があったらチェック
    name, id = lunaidanalyse.returnmode_02d(members, True)
else: # 未入力なら実行
    print("Successfully Getting Charactor Data\nName:Any ID:range(1,27)")
    print("\n\n警告: キャラクターフィルタなしでの実行はベータ版です")
    NoCharactorFilter = True

if compact.tfgen_boolean(filter_mv): # MVフィルタオンの場合
    mv3d, mv2d, mv_original, mv_static = mvf.main()
else:
    NoMVFilter = True


# フィルタは存在するか
if not NoMVFilter and NoCharactorFilter:
    filtering = False
else:
    filtering = True
    
# アウトプットフォルダ
out_gen.output(False)
output_folder = "./outputs"

# メイン処理
url = "https://sekai.best/music"  # 開くURLを指定
webbrowser.get("chrome").open(url)  # Chromeを起動して指定したURLを開く
# Chromeの取得
chrome_window = pygui.getWindowsWithTitle("Google Chrome")[0]  # ウィンドウのタイトルで特定のウィンドウを取得
# フォーカス + フルスクリーン
pygui.hotkey("win", "up")
time.sleep(10)

# フィルタ処理
if filtering == True: # もしフィルタがあるなら
    print("フィルタが実験的モードで実行されました。")
    time.sleep(3)
    # フィルタ画面を開く
    click.click(1350, 220, mx, my, False)  # 1350, 220を各解像度に対応させ、クリック
    time.sleep(1.5) 
    if not NoCharactorFilter == True: # キャラフィルタがある場合
        if id == "80": # 480, 365  # IDでのフィルタ
            click.click(480, 365, mx, my, False)
        elif id == "81": # 800, 325
            click.click(800, 325, mx, my, False)
        elif id == "83": # 512, 325
            click.click(512, 325, mx, my, False)
        elif id == "84": # 1110, 325
            click.click(1110, 325, mx, my, False)
        elif id == "82": # 980, 290
            click.click(980, 290, mx, my, False)
        elif id == "01": # 475, 460
            click.click(475, 475, mx, my, False)
        elif id == "02": # 655, 460
            ez_click(655, 460)
        elif id == "03": # 830, 460
            ez_click(830, 460)
        elif id == "04": # 1020, 460
            ez_click(1020, 460)
        elif id == "05": # 1220, 460
            ez_click(1220, 460)
        elif id == "06": # 475, 500
            ez_click(475, 500)
        elif id == "07": # 630, 500
            ez_click(630, 500)
        elif id == "08": # 820, 500
            ez_click(820, 500)
        elif id == "09": # 1010, 500
            ez_click(1010, 500)
        elif id == "10": # 1200, 500
            ez_click(1200, 500)
        elif id == "11": # 470, 540
            ez_click(470, 540)
        elif id == "12": # 650, 540
            ez_click(650, 540)
        elif id == "13": # 810, 540
            ez_click(810, 540)
        elif id == "14": # 970, 540
            ez_click(970, 540)
        elif id == "15": # 1130, 540
            ez_click(1130, 540)
        elif id == "16": # 1300, 540
            ez_click(1300, 540)
        elif id == "17": # 465, 580            
            ez_click(465, 580)
        elif id == "18": # 650, 585
            ez_click(650, 585)
        elif id == "19": # 855, 585
            ez_click(855, 585)
        elif id == "20": # 1030, 580
            ez_click(1030, 580)
        elif id == "21": # 1200, 580
            ez_click(1200, 580)
        elif id == "22": # 465, 626
            ez_click(465, 625)
        elif id == "23": # 655 625
            ez_click(655, 625)
        elif id == "24": # 830, 625
            ez_click(830, 625)
        elif id == "25": # 950, 625
            ez_click(950, 625)
        elif id == "26": # 1050, 625
            ez_click(1050, 625)
        elif id == "85": # 580, 290
            ez_click(580, 290)
        else:
            NoCharactorFilter = True
    if not NoMVFilter == True:
        if mv3d == True: # Pos 415, 415
            click.click(415, 415, mx, my, False)
        elif mv2d == True: # Pos 490, 415
            click.click(490, 415, mx, my, False)
        elif mv_static == True: # Pos 675, 415
            click.click(675, 415, mx, my, False)
        elif mv_original == True: # Pos 572, 415
            click.click(572, 415, mx, my, False)
        else:
            NoMVFilter = True
    
    click.click(1350, 220, mx, my, False)
    time.sleep(12)
    print("Starting Download..")
else: # ないなら
    print("""Starting Download..""")
    
# 本当のメイン処理
# 333, 270が #121212じゃないなら
click.click(333, 270, mx, my, True) # 333, 270 Move
if not convert.c_hex("#121212"):
    ez_click(350, 224) # 350, 224
    time.sleep(0.5)

if ExperimentalMode == "True": # 実験的モード
    print("実験的モードでの実行が開始されました。")
    time.sleep(10)
    # そこにUIがあるなら 
    click.click(1273, 333, mx, my, True)
    if convert.c_hex("#1E1E1E"):
        pygui.rightClick() # 1273, 333
        relative(-10, "y", True)
        time.sleep(0.2)
        pygui.click()
    elif convert.c_hex("#121212"):
        print("これ以上ミュージックページUIが見つかりませんでした。")
        exit()
    else:
        print("例外エラー\nカラーコードが一致しません")
        exit()

    # 二段目 -10px
    click.click(1273, 475, mx, my, True)
    if convert.c_hex("#1E1E1E"):
        pygui.rightClick() # 1273, 475
        relative(-10, "y", True)
        time.sleep(0.2)
        pygui.click()
    elif convert.c_hex("#121212"):
        print("これ以上ミュージックページUIが見つかりませんでした。")
        skip = True
    else:
        print("例外エラー\nカラーコードが一致しません")
        exit()
        
    # 三段目
    if not skip == True:
        click.click(1273, 610, mx, my, True)
        if convert.c_hex("#1E1E1E"):
            pygui.rightClick() # 1273, 610
            relative(-10, "y", True)
            time.sleep(0.2)
            pygui.click()
        elif convert.c_hex("#121212"):
            print("これ以上ミュージックページUIが見つかりませんでした。")
            skip = True
        else:
            print("例外エラー\nカラーコードが一致しません")
            exit()

    # 四段目
    if not skip == True:
        click.click(1273, 750, mx, my, True)
        if convert.c_hex("#1E1E1E"):
            pygui.rightClick() # 1273, 750
            relative(-10, "y", True)
            time.sleep(0.2)
            pygui.click()
        elif convert.c_hex("#121212"):
            print("これ以上ミュージックページUIが見つかりませんでした。")
            skip = True
        else:
            print("例外エラー\nカラーコードが一致しません")
            exit()
    exit("実験的モードでの実行が正常に終了しました")

else: # 通常モード
    # 824, 252 が白になるまでTABを押す
    while isWhite: # 白ならおわり
        click.click(824, 252, mx, my, True)
        if convert.c_hex("#FFFFFF"):
            isWhite = True
            break
        else: # 白検出までTAB
            pygui.press("tab")
        time.sleep(0.5)
    pygui.hotkey("ctrl", "enter") # 新たなタブで開く
    click.click(1399, 872, mx, my, True) # 1399, 872をホバー
    
    while end:
        if a == 10: # 10回実行ごとに10秒待機
            a = 0
            time.sleep(10)
        else:
            a += 1
        pygui.press("tab")
        time.sleep(0.1) # TAB押して 0.1秒待機
        pygui.hotkey("ctrl", "enter")
        time.sleep(0.3) # 新しいタブ開いて0.3秒待機
        
        # C44C76なら停止
        if convert.c_hex("#C44C76"): # 1399, 872
            end = True
            break
        else: # ちがうなら0.5秒待って繰り返し
            time.sleep(0.5)
    
    click.click(840, 75, mx, my, True) # 840, 75
    pygui.rightClick() #" 右クリック"
    time.sleep(0.5)
    click.click(855, 412, mx, my, True)
    if convert.c_hex("#01397F"): # 855, 412
        # 700, 540
        time.sleep(5) # 右側のタブをすべてOneTabに送る
        ez_click(700, 540)
    time.sleep(10)
    
    ez_click(28, 16) # OneTabに移動
    a = False
    
    # ロードし、ダウンロードする処理
    while a == True:
        subprocess.run("del url_write_here.txt", shell=True)
        subprocess.run("type nul > ./url_write_here.txt", shell=True)
        print("メモ帳に、OneTabにて、開いたページのURLをすべてまとめてペーストして下さい。\nメモ帳を消して続行")
        subprocess.run("notepad.exe url_write_here.txt", shell=True)
        time.sleep(0.5)
        lowfile_remover("./")
        if os.path.exists("./url_write_here.txt"):
            a = True
            break
        else:
            a = False
    
    time.sleep(5)
    a = 0
    url_based = "https://sekai.best/music/"
    can_load = []
    # ファイルから読み込み
    with open('url_write_here.txt', 'r') as file:
        urls = file.readlines()
    
    # 読み込んだ内容を処理
    for check in urls:
        check = check.replace(check[check.find(" "):], "")
        check.strip()
        if check.startswith(url_based):
            print(f"Loading Success: {check}")
            can_load.append(check)
        else:
            print(f"Failed: {check}\nText type does not start with {url_based}")
    
    print("Chrome(フルスクリーン)にフォーカスを充ててください")
    time.sleep(5)
    # 開いて、いろいろと
    hwnd = win32gui.FindWindow(None, "chrome.exe")
    if hwnd != 0: # Chromeをアクティブ化
        win32gui.SetForegroundWindow(hwnd)
    
    # 開いて色々するメイン処理
    e = 1
    ok = False
    
    # Start line forked From curseforge-autodownload/main.py
    
    for url in can_load:
        # アドレスバーをクリックして選択する
        x = cur.cursor_exchanger(600, 1280, "x")
        y = cur.cursor_exchanger(50, 800, "y")
        pygui.click(x=x, y=y)  # def 1280, 800  click = 600, 50
        time.sleep(0.5)
        
        # すでにあるURLをクリーンアップ
        pygui.hotkey('ctrl', 'a')
        pygui.hotkey('ctrl', 'backspace')
        # URLを入力する
        print(f"Trying Open {url}")
        pyclip.copy(url)  # URLをクリップボードにコピー
        pygui.hotkey("ctrl", "v")  # クリップボードの内容を貼り付け
        pygui.press('enter')
        time.sleep(7)
        
        #time.sleep(10) # ロード待機
        
    # End line forked From curseforge-autodownload/main.py

        # まずはそのままダウンロード
        # TAB を 8回
        while e < 9:
            pygui.hotkey("shift","tab")
            time.sleep(0.1)
            e += 1
        e = 1
        time.sleep(1)
        # 一致するなら # 452, 459
        click.click(452, 459, mx, my, True)
        while ok:
            if convert.c_hex("#FFFFFF"):
                pygui.press("enter") # 一致したら終わり
                ok = True
                break
            else: # コメントのせいでずれたなら
                pygui.hotkey("shift","tab")
                time.sleep(0.15) # 一致するまで
                ok = False
        ok = False # リセット
        time.sleep(3) # 多分これだけ待てばされるはず
        click.click(636, 261, mx, my, False) # 一人目のセレクト位置に移動
        time.sleep(1.3)
        if convert.c_hex("#298A7B"):
            t = "#298A7B"
        else:
            print(f"エラー: HEX不一致\n636, 261のHexが #298A7Bと一致しませんでした。\n{url}の処理はスキップされました。")
            continue
        #298A7B # 636 261 # 653 213
        # 開始位置に移動
        click.click(636, 261, mx, my, True)
        
        # 同じカラーはどこかなーw
        while ok:
            # ok が Falseなら
            while not convert.c_hex("#1F2726"):
                relative(1, "x", True) # tと現在の位置のコードが一致しないなら
                if convert.c_hex("#121212"): # 41 to 105
                    ok = True
                    break # もしフィールドオーバーしていたら
                time.sleep(0.05)
            if convert.c_hex(t):
                temp_x, temp_y = pygui.position() # 一致したら
                ez_click(452, 459) # ダウンロード
                # 待機
                time.sleep(3)
                pygui.moveTo(temp_x, temp_y + 64) # 重複実行停止処理
            elif ok == True:# 633, 5282段目にまだ何かあるなら
                pygui.moveTo(633, 528)
                if convert.c_hex("#1F2726"):
                    pygui.moveTo(620,528) # 620, 528
                    ok = False
            else: 
                print("エラー: 不明な理由でwhileループが終了しました\n (line 381)")
                ok = True
                break
            time.sleep(0.01)
        
        # 全部押し終えたら(多分)
        # 3回 SHIFT+TAB -> 右 を押してflacモード
        pygui.hotkey("shift", "tab")
        time.sleep(0.1)
        pygui.hotkey("shift", "tab")
        time.sleep(0.1)
        pygui.hotkey("shift", "tab")
        time.sleep(0.1)
        pygui.press("right")
        time.sleep(0.5)
        
        # 一人目へ
        click.click(636, 261, mx, my, False) # 一人目のセレクト位置に移動
        # ちょっと待って検出
        time.sleep(1.3)
        if convert.c_hex("#298A7B"):
            t = "#298A7B" # 一致したら
            # ダウンロード
            temp_x, temp_y = pygui.position() # 一致したら
            ez_click(452, 459) # ダウンロード
        
        
        while ok:
            # ok が Falseなら
            while not convert.c_hex("#1F2726"):
                relative(1, "x", True) # tと現在の位置のコードが一致しないなら
                if convert.c_hex("#121212"): # 41 to 105
                    ok = True
                    break # もしフィールドオーバーしていたら
                time.sleep(0.05)
            if convert.c_hex(t):
                temp_x, temp_y = pygui.position() # 一致したら
                ez_click(452, 459) # ダウンロード
                # 待機
                time.sleep(3)
                pygui.moveTo(temp_x, temp_y + 64) # 重複実行停止処理
            elif ok == True:# 633, 5282段目にまだ何かあるなら
                pygui.moveTo(633, 214)
                if convert.c_hex("#1F2726"):
                    pygui.moveTo(620,214) # 620, 528
                    ok = False
            else: 
                print("エラー: 不明な理由でwhileループが終了しました\n (line 381)")
                ok = True
                break
            time.sleep(0.01)
        
        