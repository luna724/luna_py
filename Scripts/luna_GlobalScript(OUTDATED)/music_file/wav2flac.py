import os
import ffmpeg

def main(filename, path):
    if filename.endswith(".wav"):
        # ファイルのフルパスを取得
        file_path = os.path.join(path, filename)
        output_path = file_path.replace(".wav", ".flac")
        ffmpeg.input(file_path).output(output_path, format= "flac").overwrite_output().run()