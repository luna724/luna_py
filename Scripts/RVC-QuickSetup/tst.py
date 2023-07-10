import random
import librosa
import os
import luna_GlobalScript.misc.str_checker as checker
import luna_GlobalScript.misc.music_normalizer as normalizer

# 変数
pitch_shift_count = 0
double_success = 0
change_speed_count = 0
error_count = 0
n_mfcc = 13
hop_length = 512
success_list = []

# ユーザー制御
user = input("入力拡張子 (mp3 / wav): ")
if user == "mp3" or user == "wav":
    print(f"Loading Extension.. ({user})")
else:
    print(f"Can't Loading Extension.\nPlease Select (mp3 or wav)")
    exit("Invalid Syntax")

print("Starting Directory Setup (chdir)")
os.chdir("./input_test")
print("Starting Directory Listup")
listdir = os.listdir()
print("Starting Normalize, Randomize")
total_files = len(listdir)
completed_files = 0
for x in listdir:
    # 音声ファイルの読み込み   # 正則化、MFCC摘出
    audios, srs = librosa.load(x, sr=None)
    print("Success Loading")
    # MFCCの抽出
    mfcc = librosa.feature.mfcc(audios, sr=srs, n_mfcc=n_mfcc, hop_length=hop_length)
    print("Success MFCC Extract")
    # 正則化
    normalized_mfcc = normalizer.normalize(mfcc)
    print("Success Normalized")
    ext = os.path.splitext(x)[1]
    names = os.path.splitext(x)[0]  # 名前取得
    output_path = f"./out/{names}_normalizer.mp3"  # ファイル名設定からの書き出し
    print("Start Saving")
    librosa.output.write_mp3(output_path, normalized_mfcc, srs)
    print("Success Saving")
    completed_files += 1
    progress = (completed_files / total_files) * 100
    print(f"Progress: {progress:.2f}%")
    if ext == f".{user}":
        if random.random() <= 0.075:
            # 7.5%の確率で成功する処理
            success_list.append(x)
        else:
            print(f"Rolled 92.5%.\nSkipped {x}") # ファイル数が少ない場合、確率を上げつ必要あり
    else:
        print(f"Not Matched Extension.\nSkipped {x}")
print(success_list)
print(f"{len(success_list)} Files Found")
for x in success_list:
    audio, sr = librosa.load(x, sr=None) # 読み込み
    if random.random() <= 0.3: # 30%で実行する 70%で失敗
        shifted_audio = librosa.effects.pitch_shift(audio, sr, n_steps=random.uniform(-1.9, 1.9)) # 時間軸のシフト
        pitch_shift_count += 1
    elif random.random() <= 0.8: # 50%で実行 　(一致確立 35%)
        shifted_audio = librosa.effects.time_stretch(audio, random.uniform(0.88, 1.12))
        change_speed_count += 1
    elif random.random() <= 1: # 20%で (一致確立 7%)
        shifted_audio = librosa.effects.pitch_shift(audio, sr, n_steps=random.uniform(-1.9, 1.9))
        y = shifted_audio
        shifted_audio = librosa.effects.time_stretch(y, random.uniform(0.88, 1.12))
        double_success += 1
    else:
        print(">>> Error <<<\nRandom Role Failed.")
        shifted_audio = audio
        error_count += 1

    output_path = f"./out/{x}"
    librosa.output.write_mp3(output_path, shifted_audio, sr)
