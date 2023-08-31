# import preprocessing as urls
import pyautogui
import pyperclip
import time
import luna_GlobalScript.misc.global_math as cur
import win32gui
def launch(mcver, cd=1):
    next_check = []
    load_url = []
    lines = []
    legacy = []
    url_based = "https://"

    # バージョンチェック
    #mcver = input("Minecraft Version(e.g: 1.12.2): ")
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
        openwith_def = []
        for url in load_url: # ダブルチェック成功URLをひとつづつ実行
            if url.count("/comments") >= 1: # 拡張URLがついている場合、消す
                    url = url.replace("/comments", "/")
            elif url.count("/files") >= 1:
                url = url.replace("/files", "/")
            elif url.count("/screenshots") >= 1:
                url = url.replace("/screenshots", "/")
            else:
                if url.startswith("https://www.curseforge.com/minecraft/mc-mods/"):
                    # minecraft/mc-mods の、Minecraft MODタイプのURLの場合、普通に / を追加
                    url = f"{url}/"
                    print(f"Based: {url}")
                else:
                    print(f"{url}\nThis URL was excluded because it is not a Minecraft MOD")
            # pre処理後の処理
            pre = f"{url}files?version={mcver}"
            print(f"Open URL Set: {pre}")
            openwith_def.append(pre)
                # URLを変化させ、保存
        url_list = openwith_def
        print(f"All Open URL: {url_list}")
        
        # URLを開く処理
        fail_url = []
        #   Chromeのアプリケーションウィンドウを探す
        print("Chromeをフルスクリーンにして選択してください")
        print('選択後、スクリプトの終了まで操作しないでください')
        # Chromeのウィンドウをアクティブにする
        # 実行ファイル名が"chrome.exe"のウィンドウを取得する
        hwnd = win32gui.FindWindow(None, "chrome.exe")
        if hwnd != 0:
            win32gui.SetForegroundWindow(hwnd)
        
        time.sleep(cd * 12) # Debug用待機

        # 新しいウィンドウを作成し、最大化する
        # pyautogui.hotkey("ctrl", "n")
        # pyautogui.hotkey("win", "up")

        for durl in openwith_def:
            # アドレスバーをクリックして選択する
            x = cur.cursor_exchanger(600, 1280, "x")
            y = cur.cursor_exchanger(50, 800, "y")
            pyautogui.click(x=x, y=y)  # def 1280, 800  click = 600, 50
            time.sleep(cd * 0.5)

            # すでにあるURLをクリーンアップ
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'backspace')
            # URLを入力する
            print(f"Trying Open {durl}")
            pyperclip.copy(durl)  # URLをクリップボードにコピー
            pyautogui.hotkey("ctrl", "v")  # クリップボードの内容を貼り付け
            pyautogui.press('enter')
            time.sleep(cd * 3.5)

            # Latest Releaseをクリック
            x = cur.cursor_exchanger(372, 1440, "x")  # 372, 815
            y = cur.cursor_exchanger(815, 900, "y")
            pyautogui.click(x=x, y=y)
            time.sleep(cd * 0.5)
            x = cur.cursor_exchanger(760, 1440, "x")  # 760, 300
            y = cur.cursor_exchanger(300, 900, "y")  # 1270, 211
            pyautogui.click(x=x, y=y)
            time.sleep(cd * 3)

            # 成功したか、チェック
            x = cur.cursor_exchanger(600, 1280, "x")  # アドレスバーのクリック
            y = cur.cursor_exchanger(50, 800, "y")
            pyautogui.click(x=x, y=y)  # def 1280, 800  click = 600, 50
            time.sleep(cd * 0.5)

            pyautogui.hotkey("ctrl", "c")  # コピー
            time.sleep(cd * 0.5)
            copied_text = pyperclip.paste()  # 内容取得
            if copied_text.count("/download/") >= 1:
                print(f"Download Success: {copied_text}")
            else:
                print(f"Download Failed: time.sleep関数の値を大きくしてみて下さい")
                fail_url.append(copied_text)
            time.sleep(cd * 2)  # 負化防止の停止処理

        # 終了時の処理
        for legacy in legacy:
            print(f"Can't Load legacy URL: {legacy}")
        for failed in fail_url:
            print(f"Failed: {failed}")
            print("time.sleep関数の値を大きくしてみて下さい。")
        
        print("処理終了")
    else:
        print("ロード可能なURLがありません。")
        exit()
        

if __name__ == "__main__":
    launch("1.12.2", 2.25)