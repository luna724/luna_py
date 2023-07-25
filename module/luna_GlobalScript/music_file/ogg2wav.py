import os
import ffmpeg

def main(filename, path):
    if filename.endswith(".ogg"):
        # ファイルのフルパスを取得
        file_path = os.path.join(path, filename)
        output_path = file_path.replace(".ogg", ".wav")
        ffmpeg.input(file_path).output(output_path, format= "wav").overwrite_output().run()