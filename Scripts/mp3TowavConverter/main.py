import LGS.misc.nomore_oserror as los
import ffmpeg
import LGS.misc.compact_input as cin
import os

directory = input("Target Directory: ")
os.chdir(directory)
delete_old_format = cin.tfgen_boolean(input("変換前のフォーマット形式のファイルを削除 (0 / 1): "))

# 変換タイプの選択
print(f"変換タイプの選択: \n\
0. Automatic -> x \n\
1. mp3 -> wav\n\
2. wav -> mp3\n\
3. flac -> wav\n\
4. wav -> flac \n\
5. ogg -> wav \n")

types = input("番号を入力: ")

if not types in ["0", "1", "2", "3", "4", "5"]:
  raise ValueError("値が不明です。")

# 0 なら
if types == "0":
  types_ = input("変換先 (wav / flac / mp3): ").lower()
  if not types_ in ["wav", "flac", "mp3"]:
    raise ValueError("値が不明です。")
  
  allow_extension = [".wav", ".wave", ".mp3", ".flac", ".ogg"]
  filelist = los.file_extension_filter(os.listdir(directory), allow_extension)
  
  # 変換
  for filename in filelist:
    # def main(filename="Example.flac", directory=f"os.getcwd()", output_format="wav"):
    file_name, file_extension = os.path.splitext(filename)
    # # ファイルのフルパスを取得
    # file_fullpath = os.path.join(directory, filename)
    # output_path = f"{directory}/{file_name}.{output_format}"
    output_name = f"{file_name}.{types_}"
    # ffmpeg.input(file_fullpath).output(output_path, format=output_format).overwrite_output().run(quiet=True)
    ffmpeg.input(filename).output(output_name, format=types_).overwrite_output().run(quiet=True)
    

# それ以外
elif types == "1":
  # mp32wav
  types_ = "wav"
  allow_extension = [".mp3"]
  filelist = los.file_extension_filter(os.listdir(directory), allow_extension)
  
  for filename in filelist:
    file_name = os.path.splittext(filename)[0]
    output = f"{file_name}.{types_}"
    ffmpeg.input(filename).output(output, format=types_).overwrite_outputs.run(quiet=True)
  
elif types == "2":
  # wav2MP3
  types_ = "mp3"
  allow_extension = [".wav"]
  filelist = los.file_extension_filter(os.listdir(directory), allow_extension)
  
  for filename in filelist:
    file_name = os.path.splittext(filename)[0]
    output = f"{file_name}.{types_}"
    ffmpeg.input(filename).output(output, format=types_).overwrite_outputs.run(quiet=True)

elif types == "3":
  # flac2wav
  types_ = "wav"
  allow_extension = [".flac"]
  filelist = los.file_extension_filter(os.listdir(directory), allow_extension)
  
  for filename in filelist:
    file_name = os.path.splittext(filename)[0]
    output = f"{file_name}.{types_}"
    ffmpeg.input(filename).output(output, format=types_).overwrite_outputs.run(quiet=True)
  
elif types == "4":
  # wav2flac
  types_ = "flac"
  allow_extension = [".wav"]
  filelist = los.file_extension_filter(os.listdir(directory), allow_extension)
  
  for filename in filelist:
    file_name = os.path.splittext(filename)[0]
    output = f"{file_name}.{types_}"
    ffmpeg.input(filename).output(output, format=types_).overwrite_outputs.run(quiet=True)
  
elif types == "5":
  # ogg2wav
  types_ = "wav"
  allow_extension = [".ogg"]
  filelist = los.file_extension_filter(os.listdir(directory), allow_extension)
  
  for filename in filelist:
    file_name = os.path.splittext(filename)[0]
    output = f"{file_name}.{types_}"
    ffmpeg.input(filename).output(output, format=types_).overwrite_outputs.run(quiet=True)

if delete_old_format:
  for file_path in filelist:
    os.remove(file_path)
  
print("Done.\n")