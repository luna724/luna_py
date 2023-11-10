"""
pyautoguiによる自動操作 + ocrによるテキスト取得で、SongIDに応じた曲名を取得
    """
    
import LGS.misc.jsonconfig as jsonconfig
import LGS.misc.global_math as cur
import pyautogui
import pyperclip
import time
import os
import LGS.misc.ocr_screen as ocr
from LGS.misc.re_finder import extract as r

# URLリストを作成
if os.path.exists("./song_info.json"):
    ndict = jsonconfig.read("./song_info.json")
else:
    ndict = {}
    
url_list = []

# 382曲存在
for x in range(1, 383):
    url_list.append(f"https://sekai.best/music/{x}")
    print(f"Debug: Added list to \"https://sekai.best/music/{x}\"")

print(url_list)

print("\n取得を開始します。\nChromeをフルスクリーンで選択し、操作しないでください。")
time.sleep(10)

# メイン処理
# Script forked by curseforge-autodownload

for url in url_list:
    # ダウンロード結果から得られる情報に変換
    dldata = r(pattern=r"music/(\d+)", str=url)
    dldata = "{:04d}".format(int(dldata))
    # アドレスバーをクリックして選択する
    x = cur.cursor_exchanger(600, 1280, "x")
    y = cur.cursor_exchanger(50, 800, "y")
    pyautogui.click(x=x, y=y)  # def 1280, 800  click = 600, 50
    time.sleep(0.5)

    # すでにあるURLをクリーンアップ
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'backspace')
    # URLを入力する
    print(f"Trying Open {url}")
    pyperclip.copy(url)  # URLをクリップボードにコピー
    pyautogui.hotkey("ctrl", "v")  # クリップボードの内容を貼り付け
    pyautogui.press('enter')
    time.sleep(30)
    
    # Sekai Viewer側の読み込みを待機
    
    # 245, 145 | 1280, 800 to 1000 190
    # 特定の位置にある文字をOCRを使用し取得
    result = ocr.img2txt(245, 1000, 145, 190, 1280, 800)
    print(f"取得内容: URL: {dldata} | str: {result}")
    
    # jsonに書き込み準備
    ndict[dldata] = result
    

# 書き込み
jsonconfig.write(ndict, "./song_info.json")