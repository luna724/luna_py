import sys
import subprocess
import os
# 実行関数たち
def crun(x):
    os.chdir(x)
    subprocess.run("run.bat")
    
def curseforge_autodownload():
    # cf_autodlの処理
    crun("./Scripts/curseforge-autodownload")

def datasetcollector_v3():
    # ds_collectorの処理
    crun("./Scripts/DatasetCollectorV3")

def jpg2png_converter():
    # jpg2pngの処理
    crun("./Scripts/jpgTopngConverter")

def music_collector():
    # music_collectorの処理
    crun("./Scripts/MusicCollector")

def picture_collector():
    # pic_collectorの処理
    crun("./Scripts/PictureCollector")

def taskkiller_minecraft():
    # taskkill4mcの処理
    crun("./Scripts/TaskKiller for Minecraft")

def mp32wav_converter():
    crun("./Scripts/mp3TowavConverter")
    
def unmatch_check(x):
    # 文字列不一致の処理
    print(f"不明な因数が指定されました ({x})")
    exit()

# check変数は呼び出しスクリプトの検出に使用
# 呼び出された際の因数を取得
check = sys.argv[1]

def checker(x, return_arg): # 関数とか
    check_dict = {
    "cf_autodl": curseforge_autodownload,
    "ds_collector": datasetcollector_v3,
    "jpg2png": jpg2png_converter,
    "music_collector": music_collector,
    "mp32wav_c": mp32wav_converter,
    "pic_collector": picture_collector,
    "taskkill4mc": taskkiller_minecraft
    }

    if x in check_dict:
        check_dict[x]()
    else:
        unmatch_check(x)


# main
checker(check, "a")