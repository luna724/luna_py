import ffmpeg
import os

# FFmpegコマンドの生成
#ffmpeg.input(input_file).output(output_file).run()

# フォルダのパス
path = "./out"

listdir = os.listdir(path)

# カウンタ変数
counter = 1
icounter = 0
scounter = 0
hcounter = 0
sacounter = 0

# フォルダ内のファイルを順番に名前を付けていく
for filename in listdir:
    if "星乃一歌" in filename:
        icounter += 1
        base_name = "星乃一歌"
        new_filename = f"{base_name}_{icounter}.mp3"
    elif "天馬咲希" in filename:
        sacounter += 1
        base_name = "天馬咲希"
        new_filename = f"{base_name}_{sacounter}.mp3"
    elif "望月穂波" in filename:
        hcounter += 1
        base_name = "望月穂波"
        new_filename = f"{base_name}_{hcounter}.mp3"
    elif "日野森志歩" in filename:
        scounter += 1
        base_name = "日野森志歩"
        new_filename = f"{base_name}_{scounter}.mp3"
    if filename.endswith(".mp3"):
        # ファイルのフルパスを取得
        file_path = os.path.join(path, filename)
        output_path = file_path.replace(".mp3", ".wav")

        ffmpeg.input(file_path).output(output_path, format= "wav").overwrite_output().run()