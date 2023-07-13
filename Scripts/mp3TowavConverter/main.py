import ffmpeg
import os
import luna_GlobalScript.misc.input_folder as pat
import sys
import compact as compact
import luna_GlobalScript.music_file.mp32wav as mp32wav
import luna_GlobalScript.music_file.wav2mp3 as wav2mp3
import luna_GlobalScript.music_file.wav2flac as wav2flac
import luna_GlobalScript.music_file.ogg2wav as ogg2wav
import luna_GlobalScript.music_file.flac2wav as flac2wav

# FFmpegコマンドの生成
#ffmpeg.input(input_file).output(output_file).run()

# フォルダのパス
path = pat.input(True)

# リストアップ
listdir = os.listdir(path)

# 因数の取得
arg = sys.argv[1]

# フォルダ内のファイルを順番に名前を付けていく
for filename in listdir:
    if arg in compact.check_dict:
        compact.check_dict[arg](filename, path)
    else:
        print(f"正しい因数を指定してください: {filename}")

    