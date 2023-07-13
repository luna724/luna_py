import os
import time
import requests
import subprocess
import luna_GlobalScript.misc.output_folder as lout
import luna_GlobalScript.project_sekai.unit_charactor_analyser.id.any_roma2idxname as roma2idxname
# 定義づけ、ユーザー入力
members = input("画像を取得したいキャラクターの名前を入力(例: ichika)\nALLにも対応: ")
#trainingonly = int(input("特訓状況を入力(0 = 両方 1 = 特訓前のみ, 2 = 特訓後のみ): "))
trainingonly = 0
dl_cooldown = input("ダウンロード時のクールダウンを設定(数字のみで入力 秒単位): ")
counted = input("実行回数を入力(数字のみ): ")
save_dir = lout.output(False)

# スクリプト使用用に変換
# 各キャラごとにファイル名、url名を指定
member_name, member_id = roma2idxname.returnmode_03d(members)

# 特訓状況
if trainingonly == 0:
    trainings = "ALL"
elif trainingonly == 1:
    trainings = "NOT"
elif trainingonly == 2:
    trainings = "ONLY"
else:
    print("指定された数値のいずれかを入力してください。")
    exit("Error Code 101 \nInvalid Count")
training_date = "Unknown"

if 0.0001 <= float(dl_cooldown) <= 30:
    cd = float(dl_cooldown)
else:
    print("クールダウンには1以上30以下の正の値を入力してください")
    exit("Error Code 101 \nInvalid Count")
# 　実行回数
if 1 <= int(counted) <= 1000:
    count = int(counted)
else:
    print("実行回数には1以上1000以下の正の値を入力してください")
    exit("Error Code 101 \nInvalid Count")
    
temp = "temp"
 # ファイルの保存先
#save_folder = savefolder
# 保存先のフォルダ名と保存するファイル名
x = int(1)
save_folder = save_dir
save_name = f"{x} {member_name} 特訓前.png"
num = 1
numis2 = False
numis3 = False
# image_url = [f'https://storage.sekai.best/sekai-assets/character/member/res{member_id}_no{num}_rip/card_normal.png']

# 処理開始通知
print("処理が開始されました。\n停止したい場合はctrl+Cを入力してください。")
# 画像をダウンロードし保存、一動作が終わったらエラーが発生する、またはユーザー指定の{num}の値になるまで繰り返す
if trainings == "ALL" or "NOT":
    while count > 0: # 実行数が残っている場合実行
        # 特訓前のみ
        if numis2 == False and numis3 == False:
            return_url = f'https://storage.sekai.best/sekai-assets/character/member/res{member_id}_no00{num}_rip/card_normal.png'
            training_data = 0
            if num < 10:
                num += 1
            elif 9 < num < 100:
                numis2 = True
        elif numis2 == True and numis3 == False:
            return_url = f'https://storage.sekai.best/sekai-assets/character/member/res{member_id}_no0{num}_rip/card_normal.png'
            training_data = 0
            if 9 < num < 100:
                num += 1
            elif 99 < num < 1000:
                numis3 = True
        elif numis2 == True and numis3 == True:
            return_url = f'https://storage.sekai.best/sekai-assets/character/member/res{member_id}_no{num}_rip/card_normal.png'
            training_data = 0
            if 99 < num < 1000:
                num += 1
            elif num >= 1000:
                return_url = ""
                numis2 = False
                print("numの値が1000に到達しました。\n処理を終了しました")
        else:
            print("プログラムの例外、または処理が終了しました")
            exit("Error Code 404-1 \nNot Found Available Download Count")
    # 画像をダウンロードして保存する
        if training_data == 1: #ダウンロードした画像した画像がトレーニング済みの場合
            # save_nameのtraining_dateを特訓後にする
            training_date == "特訓後"
        elif training_data == 0:
            training_date == "特訓前"
        else:
            training_date == "取得に失敗"
        save_name = f"{x} {member_name} {training_date}.png"
        response = requests.get(return_url)
        with open(os.path.join(save_folder, save_name), 'wb') as f:  # 新しく保存
            f.write(response.content)
            print('画像を', os.path.join(save_folder, save_name), "に保存しました")
        if not response.ok: #レスポンス処理
            print(f"画像の取得に失敗しました。status: {response.status_code}, reason: {response.reason}")
        else:
            print(f"画像の取得に成功しました。 status: {response.status_code}, reason: {response.reason}")
        x += int(1)  # ファイル名の変更
        time.sleep(cd)  # クールダウン
        count -= 1  # 実行回数の入力
        if trainings == "ALL":
            if numis2 == False and numis3 == False:
                return_url = f'https://storage.sekai.best/sekai-assets/character/member/res{member_id}_no00{num}_rip/card_after_training.png'
                training_data = 1
                if num < 10:
                    temp = temp
                elif 9 < num < 100:
                    numis2 = True
            elif numis2 == True and numis3 == False:
                return_url = f'https://storage.sekai.best/sekai-assets/character/member/res{member_id}_no0{num}_rip/card_after_training.png'
                training_data = 1
                if 9 < num < 100:
                    temp = temp
                elif 99 < num < 1000:
                    numis3 = True
            elif numis2 == True and numis3 == True:
                return_url = f'https://storage.sekai.best/sekai-assets/character/member/res{member_id}_no{num}_rip/card_after_training.png'
                training_data = 1
                if 99 < num < 1000:
                    temp = temp
                elif num >= 1000:
                    return_url = ""
                    numis2 = False
                    print("numの値が1000に到達しました。\n処理を終了しました")
            else:
                print("プログラムの例外、または処理が終了しました")
                exit("Error Code 404-1 \nNot Found Available Download Count")
            # 画像をダウンロードして保存する
            if training_data == 1:  # ダウンロードした画像した画像がトレーニング済みの場合
                # save_nameのtraining_dateを特訓後にする
                training_date == "特訓後"
            elif training_data == 0:
                training_date == "特訓前"
            else:
                training_date == "取得に失敗"
            save_name = f"{x} {member_name} {training_date}.png"
            response = requests.get(return_url)
            with open(os.path.join(save_folder, save_name), 'wb') as f:  # 新しく保存
                f.write(response.content)
                print('画像を', os.path.join(save_folder, save_name), "に保存しました")
            if not response.ok:  # レスポンス処理
                print(f"画像の取得に失敗しました。status: {response.status_code}, reason: {response.reason}")
            else:
                print(f"画像の取得に成功しました。 status: {response.status_code}, reason: {response.reason}")
            x += int(1)  # ファイル名の変更
            time.sleep(cd)  # クールダウン
            count -= 1  # 実行回数の入力


# なにこれ
subprocess.run("Deleter.py")