import luna_GlobalScript.music_file.record_highOption as record
import os
import pyautogui as pygui
import time
import luna_GlobalScript.misc.global_math as cur
import luna_GlobalScript.autogui.convertRGBToHex as convert
import pyperclip as pyclip
from pydub import AudioSegment
from pydub.silence import split_on_silence


# 関数
def remove_silent(audio):
    n += 1
    # 音声ファイルを読み込む
    audio = AudioSegment.from_wav(audio)

    # 無音領域で分割する
    chunks = split_on_silence(audio, min_silence_len=3000, silence_thresh=-40)

    # 分割された音声ファイルを保存する
    for i, chunk in enumerate(chunks):
        chunk.export(f"./out/split/output_{i+n}.wav", format="wav")
    
def record():
    global num
    num += 1
    out_n = f"./out/wav_outputs_{num}.wav"        # ファイル名の設定
    record.wav_32bit(12,44100,256,2,out_n)
    return out_n

def ez_click(x, y, click):
    x = cur.cursor_exchanger(x, 1440, "x")
    y = cur.cursor_exchanger(y, 900, "y")
    pygui.moveTo(x, y)
    if click == True:
        pygui.click()
    elif click == False:
        return True
    else:
        return False

# 事前処理
num = 0
n = 0
canigonext = False
end = False
os.makedirs("./out", exist_ok=True)
print("LDPlayerにフォーカスをあて、保存したいストーリーの最後まで会話を見た状態のログを一番上にスクロールした状態で待機してください。\nLDPlayerはフルスクリーンにしてください。")
time.sleep(30)

# prsk起動確認 (10s待機)
print("取得したいストーリーを開いて、最後のログまで開いている状態にしてください")
time.sleep(3)


# 再生ボタンを押して、12秒待機
while end == False: # 終了が渡されるまでループ
    if convert.c_hex("#00CCBB"): # Hex Codeが一致する場合
        out = record() # 録音 
        ez_click(1020, 260, True) # 1020, 260 click
        time.sleep(12)
    else: # 不一致の場合 5pixel ずつ下に下がる
        while canigonext == False: # 終了が渡されるまで
            ez_click(1020, 260+5, False)
            if convert.c_hex("#00CCBB"):
                canigonext = True # 一致したら終了を渡し
                out = record()
                pygui.click() # クリック
                time.sleep(12)
            elif convert.c_hex('#004275'): 
                end = True # タスクバーの色に一致したら
                break      # 終了をわたし、break
        canigonext = False
    time.sleep(0.3) # 無音(終盤)を消す
    remove_silent(out)
    time.sleep(1.2) # end = Falseの場合ループ
    pygui.scroll("-1") # ちょっと下へ
    
# メイン処理終了
