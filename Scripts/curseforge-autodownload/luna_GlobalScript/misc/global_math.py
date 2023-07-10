import math
import pyautogui

def cursor_exchanger(click_pos, baseResolution, type): # カーソルの相対位置を作り
    # 実行環境の解像度に合わせた座標を返す
#                   h
    #                   normalized_position = click_position / resolution
#                                        actual_position = normalized_position * target_resolution
    # 画像サイズを取得
    x, y = pyautogui.size()

    # 計算に使うタイプを取得
    if type == "x":
        ThisResolution = x
    elif type == "y":
        ThisResolution = y
    else:
        print("関数へ入力する変数 \"x, y\"が定義されていません。")
        return 0

    try: # いずれかの値が0の場合、ZeroDivisionが発生するため、事前にチェックをする
        click_pos / baseResolution
    except ZeroDivisionError:
        print(f"ZeroDivisionError Occurpted in {click_pos} / {baseResolution}")
        return 0
    except Exception as error:
        print(f"Unknown Error Occurpted in luna_GlobalScript/misc/global_math in cursor_exchanger function.\nError: {error}")
        return 0

    normalized_position = click_pos / baseResolution
    return_position = normalized_position * ThisResolution

    return return_position