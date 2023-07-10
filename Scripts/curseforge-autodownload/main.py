import preprocessing as url
import pyautogui
import pyperclip
import time
import luna_GlobalScript.misc.global_math as cur

next_check = []
load_url = []
lines = []
legacy = []
url_based = "https://"

# バージョンチェック
mcver = input("Minecraft Version(e.g: 1.12.2): ")
# ファイルから読み込み
with open('url_write_here.txt', 'r') as file:
    lines = file.readlines()

# 読み込んだ内容を処理
for check in lines:
    check = check.replace(check[check.find(" "):], "")
    check.strip()
    if check.startswith(url_based):
        print(f"Success: {check}")
        next_check.append(check)
    else:
        print(f"Failed: {check}\nText type does not start with {url_based}")

for check in next_check:
    if check.startswith("https://www.curseforge.com"):
        load_url.append(check)
        print(f"Double Check Success: {check}")
    elif check.startswith("https://legacy.curseforge.com"):
        print(f"Can't Load Legacy URL")
        legacy.append(check)
    else:
        print(f"Double Check Failed: {check}")

if len(load_url) > 0:
    print("Starting Download..")
    get = load_url
    openwith_def = []
    for pre in load_url:
            pre = pre[0]
            if pre.count("/comments") >= 1: # 拡張URLがついている場合、消す
                pre = pre.replace("/comments", "/")
            elif pre.count("/files") >= 1:
               pre = pre.replace("/files", "/")
            elif pre.count("/screenshots") >= 1:
             pre = pre.replace("/screenshots", "/")
            else:
              if pre.startswith("https://www.curseforge.com/minecraft/mc-mods/"):
                 # minecraft/mc-mods の、Minecraft MODタイプのURLの場合、普通に / を追加
                  pre = f"{pre}/"
                  print(f"{pre}")
              else:
                  print(f"{pre}\nThis URL was excluded because it is not a Minecraft MOD")

            # pre処理後の処理
            pre = f"{pre}files?version={mcver}"
            openwith_def.append(pre)

            # URLを開いて、ダウンロードを実行する処理
    url_list = openwith_def
    print(url_list)
    fail_url = []
    #   Chromeのアプリケーションウィンドウを探す
    print("Chromeを選択してください")
    print('選択後、スクリプトの終了まで操作しないでください')
    # Chromeのウィンドウをアクティブにする
    time.sleep(10)

                # 新しいウィンドウを作成する
    pyautogui.hotkey("ctrl", "n")
    pyautogui.hotkey("win", "up")

    for durl in openwith_def:
        print(durl)
        durl = durl[0]
        # アドレスバーをクリックして選択する
        x = cur.cursor_exchanger(600, 1280, "x")
        y = cur.cursor_exchanger(50, 800, "y")
        pyautogui.click(x=x, y=y)  # def 1280, 800  click = 600, 50
        time.sleep(0.2)

        # URLを入力する
        print(f"Trying Open {durl}")
        pyperclip.copy(durl)  # URLをクリップボードにコピー
        pyautogui.hotkey("ctrl", "v")  # クリップボードの内容を貼り付け
        pyautogui.press('enter')
        time.sleep(3.5)

        # Latest Releaseをクリック
        x = cur.cursor_exchanger(655, 1280, "x")  # 655, 210
        y = cur.cursor_exchanger(210, 800, "y")
        pyautogui.click(x=x, y=y)
        time.sleep(0.5)
        x = cur.cursor_exchanger(1272, 1280, "x")  # 1272,287
        y = cur.cursor_exchanger(287, 900, "y")  # 1270, 211
        pyautogui.click(x=x, y=y)
        pyautogui.mouseDown(button='left')
        time.sleep(1.5)  # 長押しする時間（ここでは2秒）
        pyautogui.mouseUp(button='left')
        time.sleep(0.5)
        x = cur.cursor_exchanger(830, 1280, "x")
        y = cur.cursor_exchanger(615, 800, "y")
        pyautogui.click(x=x, y=y)
        time.sleep(1)

        # 710, 705
        x = cur.cursor_exchanger(710, 1280, "x")
        y = cur.cursor_exchanger(705, 800, "y")
        pyautogui.click(x=x, y=y)
        time.sleep(3)

        # 成功したか、チェック
        x = cur.cursor_exchanger(600, 1280, "x")  # アドレスバーのクリック
        y = cur.cursor_exchanger(50, 800, "y")
        pyautogui.click(x=x, y=y)  # def 1280, 800  click = 600, 50
        time.sleep(0.2)

        pyautogui.hotkey("ctrl", "c")  # コピー
        time.sleep(0.1)
        copied_text = pyperclip.paste()  # 内容取得
        if copied_text.count("/download/") >= 1:
            print(f"Download Success: {copied_text}")
        else:
            print(f"Download Failed: time.sleep関数の値を大きくしてみて下さい")
            fail_url.append(copied_text)
        print("END")
        time.sleep(1)  # 負化防止の停止処理