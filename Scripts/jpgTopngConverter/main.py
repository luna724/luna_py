import os
from PIL import Image
import LGS.misc.nomore_oserror as los
import LGS.misc.webp_convert as webp
import LGS.misc.compact_input as cin
def convert_jpg_to_png(input_path, output_path, convertTo="PNG"): # 変換変数
    image = Image.open(input_path)
    image.save(output_path, convertTo)

def Function_mode(mode="directory",
                  directory="./input",
                  filenames="./input/test.png",
                  output_path="./output",
                  delete_old_format=False,
                  convert_type="auto",
                  convert_to="jpg",
                  convert_from="png"):
  if convert_to=="jpg":
    PIL_format = "JPEG"
  
  else:
    PIL_format = convert_to.upper()
  
  if convert_from=="any":
    extension = [".jpeg", ".jpg", ".webp", ".cwebp", ".png", ".raw"]
    
  else:
    extension.append(f".{convert_from}")
  
  if mode == "directory":
    filelist = los.file_extension_filter(os.listdir(directory), extension)
    os.makedirs(output_path, exist_ok=True)
    
    for files in filelist:
      just_filename, ext = os.path.splitext(files)
      filename_ = f"{just_filename}{ext}"
      
      input_filename = os.path.join(directory, filename_)

      outputs = f"{output_path}/{just_filename}.{convert_to}"
      
      convert_jpg_to_png(input_filename, outputs, convertTo=PIL_format)
      if delete_old_format:
        os.remove(files)
    
  elif mode == "file":
    filelist = los.file_extension_filter(list(filenames), extension)
    os.makedirs(output_path, exist_ok=True)
      
    for files in filelist:
      filename, _ = os.path.splitext(files)
      # ファイル名の取得
      just_filename = os.path.basename(filename)
      
      # 出力パスの設定
      outputs = f"{output_path}/{just_filename}.{convert_to}"
      
      convert_jpg_to_png(files, outputs, convertTo=PIL_format)
      if delete_old_format:
        os.remove(files)

if __name__ == "__main__":
    directory = input("Target Directory: ")
    os.chdir(directory)

    # 選択
    delete_old_format = cin.tfgen_boolean(input("変換前のフォーマット形式のファイルを削除 (0 / 1): "))
    types = input("変換タイプを選択: \n\
    0. 自動検出 -> n (not recommended) \n\
    1. jpeg, jpg -> png (jpg2png) \n\
    2. png -> webp(非可逆式)  \n\
    3. png -> jpg  (png2jpg) \n\
    番号を入力 (0 / 1 / 2 / 3): ")

    if types == "0":
        types_ = input("変換先 (jpg / png / webp): ").lower()
        if not types_ in ["jpg", "png", "webp"]:
            raise ValueError("値が不明です。 jpg, png, webp のいずれかの値を入力してください。")
        
    if not types in ["0","1","2","3"]:
        raise ValueError("値が不明です。 0, 1, 2, 3 のいずれかの値を入力してください。")

    # 審査通ったら
    if types == "0":
        # 自動検出 (全ファイル変更)
        extension = [".jpeg", ".jpg", ".webp", ".cwebp", ".png", ".raw"]
        filelist = los.file_extension_filter(os.listdir(directory), extension)
        target = "." + types_
        target_format = f"{types_}".upper()
        if types_ == "jpg":
            target_format = "JPEG"

    elif types == "1":
        # jpg2png
        extension = [".jpeg", ".jpg"] # 指定
        filelist = los.file_extension_filter(os.listdir(directory), extension)
        target = ".png" 
        target_format = "PNG"

    elif types == "2":
        # png2cwebp
        extension = [".png"]
        filelist = los.file_extension_filter(os.listdir(directory), extension)
        target = ".webp"
        target_format = "WebP"

    else:
        # png2jpg
        extension = ["png"]
        filelist = los.file_extension_filter(os.listdir(directory), extension)
        target = ".jpg"
        target_format = "JPEG"

    if target_format == "WebP":
        # WebP変換の場合
        for file_path in filelist:
            file_name, file_extension = os.path.splittext(file_path)
            print("File Name:", file_name)
            print("File Extension:", file_extension)
            # if not delete_old_format:
            outputs = f"./{file_name}{target}"
            webp.main(file_path, outputs)
            
            if delete_old_format:
                os.remove(file_path)
    else:
        # それ以外
        for file_path in filelist:
            file_name, file_extension = os.path.splitext(file_path)

            print("File Name:", file_name)
            print("File Extension:", file_extension)

            
            input_file = file_path
            output_file = f"{file_name}{target}"
            convert_jpg_to_png(input_file, output_file, target_format)
            
            if delete_old_format:
                os.remove(file_path)