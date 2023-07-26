import requests;import os;import luna_GlobalScript.downloading_script.count;import luna_GlobalScript.downloading_script.file_copy
import time
# https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_{y}_{z}_rip/voice_ev_shuffle_28_01_{x}_{id}.mp3
# (id, Unit_ID, dl, cd, dlc, x, y, z)
# x = "01"; y = "01"; z = "01"   x = 100~
# id = 01 ~ 26
# メイン関数
def main(id, Unit_ID, dl, cd, dlc, x, y, z):
    download_response = []

    while dlc > 0: # 実行数が残っている場合実行
        # 特訓前のみ
        return_url = dl

        response = requests.get(return_url)
        try: # Story Text Num 
            response.raise_for_status()  # ステータスコードがエラーなら例外を発生させる
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 404:
                # 404エラーの場合の処理
                continue
        download_response.append(response)
        dlc -= 1
        #with open(os.path.join(save_folder, save_name), 'wb') as f:  # 新しく保存
        #    f.write(response.content)
        #    print('画像を', os.path.join(save_folder, save_name), "に保存しました")
        #if not response.ok: #レスポンス処理
        #    print(f"画像の取得に失敗しました。status: {response.status_code}, reason: {response.reason}")
        #else:
        #    print(f"画像の取得に成功しました。 status: {response.status_code}, reason: {response.reason}")
