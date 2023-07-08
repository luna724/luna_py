import os
import time
import requests
import Deleter as delete

# 定義づけ、ユーザー入力
members = input("画像を取得したいキャラクターの名前を入力(例: ichika)\nALLにも対応: ")
#trainingonly = int(input("特訓状況を入力(0 = 両方 1 = 特訓前のみ, 2 = 特訓後のみ): "))
trainingonly = 0
#dl_cooldown = input("ダウンロード時のクールダウンを設定(数字のみで入力 秒単位): ")
dl_cooldown = 0.0001
counted = input("実行回数を入力(数字のみ): ")
#counted = 100
save_dir = input("ファイルの保存位置を入力")
#save_dir = "E:\\TEMP"
#savefolder = input("セーブするフォルダのパスを入力してください (例: C:\\\\Users\\\\ichik\\\\Downloads): ")

# スクリプト使用用に変換
# 各キャラごとにファイル名、url名を指定
if members == "ichika":
    member_name = "星乃一歌"
    member_id = "001"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "saki":
    member_name = "天馬咲希"
    member_id = "002"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "honami":
    member_name = "望月穂波"
    member_id = "003"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "shiho":
    member_name = "日野森志歩"
    member_id = "004"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "kanade":
    member_name = "宵崎奏"
    member_id = "017"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "mafuyu":
    member_name = "朝比奈まふゆ"
    member_id = "018"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "ena":
    member_name = "東雲絵名"
    member_id = "019"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "mizuki":
    member_name = "暁山瑞希"
    member_id = "200"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "nene":
    member_name = "草薙寧々"
    member_id = "015"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "minori":
    member_name = "花里みのり"
    member_id = "005"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "haruka":
    member_name = "桐谷遥"
    member_id = "006"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "airi":
    member_name = "桃井愛莉"
    member_id = "007"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "shizuku":
    member_name = "日野森雫"
    member_id = "008"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "kohane":
    member_name = "小豆沢こはね"
    member_id = "009"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "ann":
    member_name = "白石杏"
    member_id = "010"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members == "emu":
    member_name = "鳳えむ"
    member_id = "014"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
elif members =="ALL":
    member_name = "取得機能未実装"
    member_id = "021"
    print(f"Successfully Setup for Charactor\nName:{member_name} ID:{member_id}")
else:
    print("そのキャラクターは存在しない、またはスクリプトで未実装か、入力方法が間違っています")
    exit("Error Code 404-2 \nCharactor Not Found")
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
# else:                     # 未実損
#    print("特訓状況を正しく入力してください")
#    exit()
# クールダウン
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
# 保存先のフォルダがない場合は作成する
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

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

#NA_folder = f"{save_folder}NA\\"
#delete.move_files(save_folder, "E:\\TEMP FILE\\NAN")
#elif
#