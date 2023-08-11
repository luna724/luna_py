import ffmpeg
import os

def main(filename, directory=f"{os.getcwd()}", output_format="wav"):
  file_name = os.path.splitext(filename)[0]
  # ファイルのフルパスを取得
  file_fullpath = os.path.join(directory, filename)
  output_path = f"{directory}/{file_name}.{output_format}"
  ffmpeg.input(file_fullpath).output(output_path, format=output_format).overwrite_output().run(quiet=True)