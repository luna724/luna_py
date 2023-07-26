import os
import ffmpeg

def main(filename, path):
    if filename.endswith(".wav"):
        # ファイルのフルパスを取得
        file_path = os.path.join(path, filename)
        output_path = file_path.replace(".wav", ".mp3")
        ffmpeg.input(file_path).output(output_path, format= "mp3").overwrite_output().run()