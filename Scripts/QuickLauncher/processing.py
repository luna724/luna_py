import subprocess
import os
import time
import luna_GlobalScript.misc.nomore_oserror as file_checker
import luna_GlobalScript.misc.compact_input as incheck
import luna_GlobalScript.misc.jsonconfig as jsoncfg
import luna_GlobalScript.misc.shortcut_generator as scg

check = input("ショートカット名の自動設定\n(0(No) or 1(Yes)): ")
check = check.strip() # 入力をチェック
userinput = incheck.tfgen_boolean(check)
# run辞書の取得
run = jsoncfg.read("./run_data.json")
# cdの取得
os.chdir("..\\")
sc_cache = {}
cd_nr = os.getcwd()
cd = cd_nr.replace("\\", "/")
if not cd.count("luna_py/Scripts") > 1:
    lunapy_dir = cd.replace("luna_py/Scripts", "luna_py")
else:
    os.chdir("..\\")
    lunapy_dir = os.getcwd()
    os.chdir("./Scripts")
os.chdir("./QuickLauncher")

if userinput:
    curseforge_autodownload = "cf_autodl"
    dataset_collector = "ds_collector"
    jpg_to_png_converter = "jpg2png"
    light_changer = "light_changer"
    mp3_to_wav_converter = "mp32wav"
    music_collector = "music_collector"
    picture_collector = "pic_collector"
    taskkiller_for_minecraft = "taskkill4mc"
    print(f"Curserforge AutoDownload: {curseforge_autodownload}\n \
            DatasetCollector: {dataset_collector}\n \
            jpg To png Converter: {jpg_to_png_converter}\n \
            Light Changer: {light_changer}\n \
            MP3 to Wav Converter: {mp3_to_wav_converter}\n \
            Music Collector: {music_collector}\n \
            Picture Collector: {picture_collector}\n \
            Taskkiller For Minecraft: {taskkiller_for_minecraft}\n \
            \n \
            自動設定が完了しました。")
    
elif not userinput:
    print("ショートカット名を入力してください。")
    curseforge_autodownload = input("Curseforge AutoDownload: ")
    dataset_collector = input("Dataset Collector: ")
    jpg_to_png_converter = input("jpg To png Converter: ")
    light_changer = input("Light Changer: ")
    mp3_to_wav_converter = input("MP3 to Wav Converter: ")
    music_collector = input("Music Collector: ")
    picture_collector = input("Picture Collector: ")
    taskkiller_for_minecraft = input("Taskkiller For Minecraft: ")
    print(f"Curserforge AutoDownload: {curseforge_autodownload}\n \
            DatasetCollector: {dataset_collector}\n \
            jpg To png Converter: {jpg_to_png_converter}\n \
            Light Changer: {light_changer}\n \
            MP3 to Wav Converter: {mp3_to_wav_converter}\n \
            Music Collector: {music_collector}\n \
            Picture Collector: {picture_collector}\n \
            Taskkiller For Minecraft: {taskkiller_for_minecraft}\n \
            \n \
            設定が完了しました。")
    
else:
    print("正しい値を入力してください。\n(0 or 1)\n自動設定が使用されました。")
    curseforge_autodownload = "cf_autodl"
    dataset_collector = "ds_collector"
    jpg_to_png_converter = "jpg2png"
    light_changer = "light_changer"
    mp3_to_wav_converter = "mp32wav"
    music_collector = "music_collector"
    picture_collector = "pic_collector"
    taskkiller_for_minecraft = "taskkill4mc"
    print(f"Curserforge AutoDownload: {curseforge_autodownload}\n \
            DatasetCollector: {dataset_collector}\n \
            jpg To png Converter: {jpg_to_png_converter}\n \
            Light Changer: {light_changer}\n \
            MP3 to Wav Converter: {mp3_to_wav_converter}\n \
            Music Collector: {music_collector}\n \
            Picture Collector: {picture_collector}\n \
            Taskkiller For Minecraft: {taskkiller_for_minecraft}\n \
            \n \
            自動設定が完了しました。")
   
   
feature = [curseforge_autodownload, dataset_collector, jpg_to_png_converter, light_changer, mp3_to_wav_converter, music_collector\
    , picture_collector, taskkiller_for_minecraft]
cant_filename = []
replace_filename = []
filename = feature
n = 0

# ファイル名用処理
for x in feature:
    for y in file_checker.wincannotaddfilename:
        if x.count(y) > 0: # ファイルに追加できない名前がある場合
            cant_filename.append(x)
            x = file_checker.filename_resizer(x, "filename", "")
            replace_filename.append(x)
            filename[n] = x
    n += 1 # len処理用数値
    
# ファイル名の設定
run_id = 0
run_id_dict = {0: "curseforge-autodownload",
                1: "DatasetCollectorV3",
                2: "jpgTopngConverter",
                3: "LightChanger",
                4: "mp3TowavConverter",
                5: "MusicCollector",
                6: "PictureCollector",
                7: "TaskKiller for Minecraft"
                }
for x in filename:
    # ディレクトリ名の設定
    type = run_id_dict[run_id]
    sc_cache[type] = x
    target_file = f"{cd}/{type}/run.bat"
    shortcut_name = f"{x}.lnk" 
    os.makedirs("./cache/sc", exist_ok=True)
    scg.create_shortcut(target_file, shortcut_name, "./cache/sc")
    run_id += 1

print("%windir%/System32 にショートカットの書き込みを行います。\n停止する場合は、Ctrl+Cを10秒以内に押してください。")
time.sleep(10)
subprocess.Popen("./xcopy_sc.bat", shell=True, elevate=True)

run["directory"] = lunapy_dir
run["status"] = "Yes"
jsoncfg.write(run, "./run_data.json")
jsoncfg.write(sc_cache, "./sc_data.json")

exit()