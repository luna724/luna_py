import math
import pyautogui as pygui

def cursor_exchanger(click_pos, baseResolution, type): # カーソルの相対位置を作り
    # 実行環境の解像度に合わせた座標を返す
#                   h
    #                   normalized_position = click_position / resolution
#                                        actual_position = normalized_position * target_resolution
    # 画像サイズを取得
    x, y = pygui.size()

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

def cursor_relative_position(addPoint, type, moveTo): 
    # 推奨  x.cursor_relative_position(x.cursor_exchanger(追加する値, 入力したPCの解像度, "x or y"))
    # 現在の座標を取得
    current_x, current_y = pygui.position()

    # 移動先の座標を計算
    target_y = current_y + addPoint
    target_x = current_x + addPoint
    
    if moveTo == True:  # もし移動もここで処理するなら
        if type == "x":
            pygui.moveTo(target_x, current_y)
        elif type == "y":
            pygui.moveTo(current_x, target_y)
        else:
            print("関数へ入力する変数 \"x, y\"が定義されていません。")
            pygui.moveTo(target_x, target_y)
    else:  
        if type == "x":
            return target_x
        elif type == "y":
            return target_y
        else:
            print("関数へ入力する変数 \"x, y\"が定義されていません。")
            return target_x, target_y
    
    
        