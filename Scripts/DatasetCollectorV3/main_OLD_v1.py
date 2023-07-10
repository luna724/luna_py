# https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_84_01_rip/voice_ev_shuffle_28_01_11_01.mp3
import time
import requests
import os
import luna_GlobalScript.downloading_script.main as lunadl

# 定義、入力待ち
urls = "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_[EventID_CharaUnit]_[SNum]_rip/voice_ev_shuffle_28_01_[ChatC]_[CID].mp3"
members = input("画像を取得したいキャラクターの名前を入力(例: ichika)\nALLにも対応: ")
DL_Limit = int(input("音声ファイル最大取得数を入力(例: 500)\n0で無制限(終わらないので非推奨): "))
x = "01"
y = "01"
z = "01"
cd = 10
ec_result = False
Disable_Sleep = False
dlc = 0

def DL_Count_Setup(xx): #　ダウンロードカウントの後処理
    global dlc
    global cd
    global ec_result
    if xx <= 0:
        print("Failed Analyse&Compile for DL_Limit.\nProgram Skipped.")
        dlc = xx
        return -1
    elif xx <= 70:
        print("\n")
        cd = 0.5
        xx += 1
        ec_result = True
        time.sleep(cd)
        dlc = xx
        return 0
    elif xx <= 200:
        cd = 3
        xx += 1
        ec_result = True
        time.sleep(cd)
        dlc = xx
        return 0
    elif xx <= 600:
        cd = 6
        xx += 1
        ec_result = True
        time.sleep(cd)
        dlc = xx
        return 0
    elif xx <= 1500:
        cd = 12.5
        xx += 1
        ec_result = True
        time.sleep(cd)
        dlc = xx
        return 0
    elif xx <= 5000:
        cd = 20
        xx += 1
        ec_result = True
        time.sleep(cd)
        dlc = xx
        return 0
    else:
        cd = 600
        xx += 0
        ec_result = False
        time.sleep(0)
        dlc = xx
        return -1
# スクリプト使用用に変換
# 各キャラごとにファイル名、url名を指定
if members == "ichika":
    member_name = "星乃一歌"
    member_id = "01"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "saki":
    member_name = "天馬咲希"
    member_id = "02"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "honami":
    member_name = "望月穂波"
    member_id = "03"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "shiho":
    member_name = "日野森志歩"
    member_id = "04"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "kanade":
    member_name = "宵崎奏"
    member_id = "17"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "mafuyu":
    member_name = "朝比奈まふゆ"
    member_id = "18"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "ena":
    member_name = "東雲絵名"
    member_id = "19"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "mizuki":
    member_name = "暁山瑞希"
    member_id = "20"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "nene":
    member_name = "草薙寧々"
    member_id = "15"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "minori":
    member_name = "花里みのり"
    member_id = "5"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "haruka":
    member_name = "桐谷遥"
    member_id = "6"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "airi":
    member_name = "桃井愛莉"
    member_id = "7"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "shizuku":
    member_name = "日野森雫"
    member_id = "8"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "kohane":
    member_name = "小豆沢こはね"
    member_id = "9"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "ann":
    member_name = "白石杏"
    member_id = "10"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "emu":
    member_name = "鳳えむ"
    member_id = "14"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members =="ALL":
    member_name = "取得機能未実装"
    member_id = "21"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
else:
    print("そのキャラクターは存在しない、またはスクリプトで未実装か、入力方法が間違っています")
    exit("Error Code 404-2 \nCharactor Not Found")

# DL_Limitの変換
if -1 < DL_Limit:
    if type(DL_Limit) == int:
      if DL_Limit == 0:
         DL_Limit = 10 ** (10 ** (10 ** 10))
      print(f"Download Limit:{DL_Limit}")
    elif type(DL_Limit) == float:
        if 0 <= DL_Limit < 1:
            DL_Limit = 10 ** (10 ** (10 ** 10))
        else:
             DL_Limit = DL_Limit / 1
             DLLimitCut = DL_Limit % 1
             print(f"Floatはサポートされていません。\n{DLLimitCut}は切り捨てられました。  設定数値:{DL_Limit}")
    else:
        print("サポートされている整数値で入力してください。")
        exit("Error Code 403 \nInvalid Syntax")
else:
    print("サポートされている整数値で入力してください。")
    exit("Error Code 403 \nInvalid Syntax")
print("\n\n Loading Setup... ")
status = DL_Count_Setup(DL_Limit) # 変換関数の呼び出し
if status == -1: # ステータスの確認
    statuss = f"Compile= False\nInvalid Number(x <= 0)"
elif status == 0:
    statuss = f"compile= True"
else:
    statuss = f"compile= False\nCan't get function data \"DL_Count_Setup\""
if Disable_Sleep == True: # クールダウン無効設定
    cd = 0
    cds = "Disabled"
else:
    cds = str(cd)
url = f"https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_{y}_{z}_rip/voice_ev_shuffle_28_01_{x}_{member_id}.mp3"
print(
      f"Selecting Charactor: {member_name}\n"
      f"(Charactor ID: {member_id})\n"
      f"Download Base URL: {urls}\n"
      f"Example: {url}\n"
      f"Cooldown per Downloads: {cds}\n"
      f"Download Count: {dlc}\n"
      f"Compile Check: {statuss}\n"
      "Error Collusion: {ec-result} (COMING SOON)\n\n")
if not os.path.exists("./result"):
    os.mkdir("./result")

# ダウンロードスクリプトを実行
time.sleep(10)
lunadl.main_function(member_name, member_id, url, cds, dlc)