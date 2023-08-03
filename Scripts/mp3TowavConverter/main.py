# import ffmpeg
# import os
# import luna_GlobalScript.misc.input_folder as pat
# import sys
# # import compact as compact
# import luna_GlobalScript.music_file.mp32wav as mp32wav
# import luna_GlobalScript.music_file.wav2mp3 as wav2mp3
# import luna_GlobalScript.music_file.wav2flac as wav2flac
# import luna_GlobalScript.music_file.ogg2wav as ogg2wav
# import luna_GlobalScript.music_file.flac2wav as flac2wav

# # select.py
# print("利用可能: 1. mp3 -> wav \n2. wav -> mp3  \n3. ogg -> wav \n4. flac -> wav \n5. wav -> flac  |")
# modes = int(input("変換モードを選択(番号指定): "))

# modes %= 1 
# if 0 < modes < 6:
#     if modes == 1:
#         mode = "mp32wav"
#     elif modes == 2:
#         mode = "wav2mp3"
#     elif modes == 3:
#         mode = "ogg2wav"
#     elif modes == 4:
#         mode = "flac2wav"
#     elif modes == 5:
#         mode = "wav2flac"

# # FFmpegコマンドの生成
# #ffmpeg.input(input_file).output(output_file).run()

# # compact.py
# check_dict = {
#     "mp32wav": mp32wav,
#     "wav2mp3": wav2mp3,
#     "wav2flac": wav2flac,
#     "ogg2wav": ogg2wav,
#     "flac2wav": flac2wav
# }

# # フォルダのパス
# path = input("対象ディレクトリ: ")

# # リストアップ
# listdir = os.listdir(path)

# # 因数の取得
# arg = mode

# # フォルダ内のファイルを順番に名前を付けていく
# for filename in listdir:
#     arg.main(filename, path)


import LGS.music_file.flac2wav as f2w
import os

dir = input("Target Directory: ")

lists = os.listdir(dir)

for x in lists:
    f2w.main(x, dir)