import pyperclip
import pyautogui
import time
import luna_GlobalScript.misc.global_math as cur

def open(url_list):
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

    for url in url_list:
        url = url[0]
        # アドレスバーをクリックして選択する
        x = cur.cursor_exchanger(600, 1280, "x")
        y = cur.cursor_exchanger(50, 800, "y")
        pyautogui.click(x=x, y=y) # def 1280, 800  click = 600, 50
        time.sleep(0.2)

        # URLを入力する
        print(f"Trying Open {url}")
        pyperclip.copy(url)  # URLをクリップボードにコピー
        pyautogui.hotkey("ctrl", "v")  # クリップボードの内容を貼り付け
        pyautogui.press('enter')
        time.sleep(3.5)

        # Latest Releaseをクリック
        x = cur.cursor_exchanger(655, 1280, "x") # 655, 210
        y = cur.cursor_exchanger(210, 800, "y")
        pyautogui.click(x=x, y=y)
        time.sleep(0.5)
        x = cur.cursor_exchanger(1272, 1280, "x") #1272,287
        y = cur.cursor_exchanger(287, 900, "y")# 1270, 211
        pyautogui.click(x=x,y=y)
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
        x = cur.cursor_exchanger(600, 1280, "x") # アドレスバーのクリック
        y = cur.cursor_exchanger(50, 800, "y")
        pyautogui.click(x=x, y=y)  # def 1280, 800  click = 600, 50
        time.sleep(0.2)

        pyautogui.hotkey("ctrl", "c") # コピー
        time.sleep(0.1)
        copied_text = pyperclip.paste() # 内容取得
        if copied_text.count("/download/") >= 1:
            print(f"Download Success: {copied_text}")
        else:
            print(f"Download Failed: time.sleep関数の値を大きくしてみて下さい")
            fail_url.append(copied_text)
        print("END")
        time.sleep(1) # 負化防止の停止処理