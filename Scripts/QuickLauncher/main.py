import subprocess
import time
import luna_GlobalScript.misc.compact_input as incheck
import luna_GlobalScript.misc.jsonconfig as jsonconfig
import os

if os.path.exists("./run_data.json"): # 既に実行したごとがあるなら
    run = jsonconfig.read("./run_data.json")
    if run["status"] == "Processing": # もし続行中なら
        print("不明なエラーが発生しました。\nほかのスクリプトが実行中でない場合は、\"luna_py/Scripts/QuickLaunher/run_data.json\"を削除してください。")
        time.sleep(10)
        exit()
    elif run["status"] == "Yes":
        cd = os.getcwd()
        if run["directory"] == cd:
            print("既に設定済みです。\nluna_pyの位置を変更した際にもう一度実行してください。")
            time.sleep(10)
            exit()
    elif run["status"] == "No":
        run = {"status": "Processing",
                "directory": ""}
    else:
        print("jsonの入力形式が一致しません。\n\"luna_py/Scripts/QuickLaunher/run_data.json\"を削除してください。")
        time.sleep(10)
        exit()

else:
    run = {"status": "",
           "directory": ""}
print("警告: このスクリプトは %windir%/System32 へ任意のファイル名の lnk(ショートカット)を作成します。")
check = input("QuickLaunch (Win+Rからの実行)を有効化してもよろしいですか？\n(0 = No / 1 = Yes): ")
check = check.strip() # 入力でチェック
userinput = incheck.tfgen_boolean(check)

if not userinput:
    print("処理を終了します。")
    run["status"] = "No"
    jsonconfig.write(run, "./run_data.json")
    exit()

elif userinput:
    print("Processing..") # 続行等の処理
    run["status"] = "Processing" 
    jsonconfig.write(run, "./run_data.json")
    time.sleep(5)
    subprocess.Popen("processing.bat", shell=True, elevate=True)

else:
    print("正しい値を入力してください (0 または 1)")
    time.sleep(5)
    exit()
    
