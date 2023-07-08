import os
from PIL import Image

def convert_jpg_to_png(input_path, output_path): # 変換変数
    image = Image.open(input_path)
    image.save(output_path, "PNG")

extension = [".jpeg", ".jpg", ".webp"] # 指定

directory = input("Target Directory: ")
os.chdir(directory)

file_list = os.listdir(directory)
for file_path in file_list:
    file_name, file_extension = os.path.splitext(file_path)

    print("File Name:", file_name)
    print("File Extension:", file_extension)

    if any(ext in file_extension for ext in extension) >= 1:
        input_file = file_path
        output_file = f"{file_name}.png"
        convert_jpg_to_png(input_file, output_file)
        os.remove(file_path)