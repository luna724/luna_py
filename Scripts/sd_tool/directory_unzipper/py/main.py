import os
import shutil
import sys
sys.path.append("..\\..\\..\\") # Scripts/
from jpgTopngConverter.main import convert_jpg_to_png
from LGS.misc.nomore_oserror import nest_listfile
from LGS.misc.nomore_oserror import file_extension_filter

def launch(target_root_directory):
  # root -> content
  # /root
  content_list = nest_listfile(target_root_directory)
  os.chdir(target_root_directory)
  
  for content in content_list:
    # png -> jpeg に変換
    filename, extension = os.path.splitext(content)
    if extension == ".jpeg" or extension == ".jpg":
      os.makedirs("./delete_cache", exist_ok=True)
      shutil.move(content, f"./delete_cache/{content}")
    else:
      jpeg_content = "{}.jpeg".format(filename)
      convert_jpg_to_png(os.path.join(target_root_directory, content),
                        output_path=os.path.join(target_root_directory, jpeg_content),
                        convertTo="JPEG")
  
  # 終わったら *.png を消す
  pnglist = file_extension_filter(content_list, [".png"])
  for x in pnglist:
    shutil.move(x, "./delete_cache/{}".format(x))
  
  # outputs の中身を摘出 (くそ適当)
  for x in os.listdir():
    if os.isdir(x):
      # root -> 2023_we_outputs
      shutil.move(f"./{x}/outputs/txt2img-grids", f"./{x}/")
      # /outputs/txt2img-grids -> /txt2img-grids/20230303/*.jpeg
      for y in os.listdir(f"./{x}/txt2img-grids"):
        if not y > 1:
          os.rename(y, "grids")
        else:
          print("ERROR: txt2img-grids/* にてディレクトリが2つ以上存在します")
      if os.path.exist(f"./{x}/txt2img-grids/grids"):
        shutil.move(f"./{x}/txt2img-grids/grids", f"./{x}/")
      # /outputs/txt2img-grids/2023023032 -> /grids/
      
      # /outputs/txt2img-images/2023023032 -> /*
      for z in os.listdir(f"./{x}/outputs/txt2img-images/"):
        if not z > 1:
          os.rename(z, "image")
          shutil.move(f"./{x}/outputs/txt2img-images/image", f"./{x}/")
          # png ファイルを摘出
          for p in file_extension_filter(os.listdir(f"./{x}/image"), [".jpeg"]):
            shutil.move(f"./{x}/image/{p}", f"./{x}") 
    
if __name__ == "__main__":
  a = input("Target Directory: ")
  
  launch(a)