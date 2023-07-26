import random
import os
import subprocess
import luna_GlobalScript.misc.compact_input as ci
import luna_GlobalScript.misc.random_roll as roll
from luna_GlobalScript.misc.nomore_oserror import file_extension_filter as filter_files_by_extension
import shutil
import luna_GlobalScript.music_file.flac2wav as flac2wav
import luna_GlobalScript.audio_tool.pitch_shift as pitch_shifts
import luna_GlobalScript.audio_tool.volume_exchange as vol_change
import luna_GlobalScript.audio_tool.time_shfit as time_shifts_OLD
import time
import sys
sys.path.append("..\\..\\")
import module.LGS.audio_tool.white_noise as wn
import audio_tool.time_shfit as time_shifts
import audio_tool.any_noise as noise

# 入力処理 / 事前処理
use_type_stretch = input("タイムストレッチの使用 (0 or 1): ")
use_type_stretch = ci.tfgen_boolean(use_type_stretch)
chance = float(input("オプション拡張の適用率 (0.1 ~ 100): "))

# 実行ディレクトリを保存
white_noise_dir = os.getcwd()
white_noise_dir = f"{white_noise_dir}\\white_noise\\"

# ホワイトノイズがあるか確認
if not os.path.exists("./white_noise/wn_0.1.wav"):
    print(f"White Noise Data Not Found.\nCreating White Noise..")
    subprocess.Popen("create_whitenoise.bat", shell=True)
    time.sleep(12)

# 音声リストを取得 
input_dir = input("拡張音声ディレクトリ: ")
allowed_extensions = ["wav", "flac", "mp3"] # 許可する拡張子
flac = ["flac"]
os.chdir(input_dir)
file_list = os.listdir("./") # /augmentationを作成、ファイルのリストアップ
audio_list = filter_files_by_extension(file_list, allowed_extensions)
if len(audio_list) < 1: # ファイルがない場合
    print(f"""Audio File Not Found. (Only can Input "wav", "flac", "mp3")""")
    exit()
os.makedirs("./augmentation", exist_ok=True)
if len(os.listdir("./augmentation")) != 0:  # もし何か入ってるなら
    if os.path.exists("./old_augmentation"):
        os.remove("./old_augmentation") # リネーム、古いほうを削除
    os.rename("./augmentation", "./old_augmentation")
    os.makedirs("./augmentation", exist_ok=True)
    os.makedirs("./augmentation/cache", exist_ok=True)
else:
    os.makedirs("./augmentation/cache", exist_ok=True)

# flacはwavに変換
flac_list = filter_files_by_extension(audio_list, flac)
if len(flac_list) > 0:
    os.makedirs("./augmentation/cache/flac", exist_ok=True)
    for x in flac_list:
        shutil.move(f"./{x}", "./augmentation/cache/flac")
    # 移動したのち、リストアップし、wavに変換
    directory = os.listdir("./augmentation/cache/flac")
    path = f"{input_dir}\\augmentation\\cache\\flac"
    for x in directory: 
        flac2wav.main(x, path) # 変換
    # 変換したものを戻す
    directory = os.listdir("./augmentation/cache/flac")
    flac2wav_list = filter_files_by_extension(directory, ["wav"])
    for x in flac2wav_list:
        shutil.move(f"./augmentation/cache/flac/{x}", "./")
# MP3はwavではなく、mp3で書き出しするように。
mp3_list = filter_files_by_extension(audio_list, ["mp3"])
if len(mp3_list) > 0:
    in_mp3 = True
    os.makedirs("./augmentation/cache/mp3", exist_ok=True)
    for x in mp3_list:
        shutil.move(f"./{x}", "./augmentation/cache/mp3")
else:
    in_mp3 = False

# 作業位置の変更    


# 関数
def pitch_shift(audio_file):
    pitch_factor = round(random.uniform(0.65, 1.6), 5)
    print(f"Starting Convert \"Pitch Shift\"\n \
            Pitch Factor: {pitch_factor}  |  Target Audio: {audio_file}")
    pitch_shifts.librosa_mode(audio_file, pitch_factor, True, f"./augmentation/outputs/{audio_file}.wav")
    
def volume_exchange(audio_file):
    volume_factor = round(random.uniform(0.5, 1.5), 5)
    print(f"Starting Convert \"Volume Exchange\"\n \
            Volume Factor: {volume_factor}  |  Target Audio: {audio_file}")
    vol_change.librosa_mode(audio_file, volume_factor, True, f"./augmentation/outputs/{audio_file}.wav")

def time_shift(audio_file):
    time_shift_factor = round(random.uniform(0.5, 1.5), 5)
    print(f"Starting Convert \"Time Shift(Using SoX Mode)\"\n \
            Time Shift Factor: {time_shift_factor} | Target Audio: {audio_file}")
    time_shifts.sox_mode(audio_file, time_shift_factor, f"./augmentation/outputs/{audio_file}.wav")

def white_noise(audio_file):
    noise_strength = round(random.uniform(0.001, 0.01), 4)
    print(f"Starting Convert  \"White Noise\"\n\
            White Noise Strength: {white_noise}  |  Target Audio: {audio_file}")
    if roll.random_roll(0.5):
        # 50% で SoXモード
        wn.sox_mode(audio_file, f"{white_noise_dir}wn_{str(noise_strength)}.wav", f"./augmentation/outputs/{audio_file}.wav")
    else:
        # ロールしなかった場合Librosaモード
        wn.librosa_mode(audio_file, noise_strength, True, f"./augmentation/outputs/{audio_file}.wav")
    
def time_stretch(audio_file):
    
# 拡張リスト # ランダム値に基づき、これらが実行される
augmentations = [pitch_shift, volume_exchange, time_shift, white_noise]
# Treuの場合追加
if use_type_stretch:
    augmentations.append(time_stretch)

# 各ファイルに対して拡張を適用
for audio_file in audio_list:
    # ランダムに拡張を選択
    chosen_augmentation = random.choice(augmentations)
    
    # 確率に基づいて処理を行う
    if roll.random_roll(0.7):
        if roll.random_roll(chance):
            # 選ばれた拡張をファイルに適用
            augmented_audio = chosen_augmentation(audio_file)
        if roll.random_roll(0.35): # 35%でホワイトノイズモード
            augmented = white_noise(audio_file)
        else:
            # ノイズの強さ、タイプのロール
            noise_strength = round(random.uniform(0.001, 0.05), 4)
            noise_type = random.choice(["whitenoise", "pinknoise", "brownnoise"])
            noise.add_noise(audio_file, f"./augmentation/outputs/{audio_file}.wav", noise_strength, noise_type)
        # ロール時の処理を行う
        # ...

    # ロールされなかった場合の処理を行う