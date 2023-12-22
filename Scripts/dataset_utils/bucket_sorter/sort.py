import sys
sys.path.append("..\\")
import os
from tkinter import Tk, filedialog
import shutil
from PIL import Image
from LGS.misc.nomore_oserror import file_extension_filter

def browse_folder():
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()

    filename = filedialog.askdirectory()
    if filename:
        if os.path.isdir(filename):
            root.destroy()
            return str(filename)
        else:
            root.destroy()
            return str(filename)
    else:
        filename = "Folder not selected"
        root.destroy()
        return str(filename)
      
def load_res(image_path: str):
  with Image.open(image_path) as image:
    w, h = image.size
  return w, h, image_path

def find_nearest_resolution(target_resolution, resolution_dict):
  nearest_resolution = min(resolution_dict.values(), key=lambda x: abs(x[0] - target_resolution[0]) + abs(x[1] - target_resolution[1]))
  # 対応するキーを取得
  bucket = next(key for key, value in resolution_dict.items() if value == nearest_resolution)
  return bucket, nearest_resolution

def calc_near_bucket(bucket_dict: dict, image_data_dict: dict, adv_calc: bool):
  image_bucket_info = {}
  
  for x, y in image_data_dict.items():
    image_bucket_info[x] = [f"{y[0]}x{y[1]}", find_nearest_resolution((y[0], y[1]), bucket_dict)]
  
  return image_bucket_info

def bucket_size_checker(bucket_list: list, minimum_pixels: int):
  delete_list = []
  for x in bucket_list:
    if x[0] * x[1] < minimum_pixels:
      delete_list.append(x)
  for x in delete_list:
    print(f"Deleted Bucket: {x}\nbucket pixels < minimum_pixels")
    bucket_list.remove(x)
  
  return bucket_list
    
def main(calc_target_dir: str, # Target Directory
          bucket_size: list, # All Bucket Size (Syntax: [(w, h), (w, h)...])
          dont_use_simply_calculate: bool # Simply Calculate = Use 「w×h」 and use the closest result
          ):
  bucket_size = bucket_size_checker(bucket_size, 262114)
  
  print("WARNING: only Supported \"1:1 Pictures\"")
  dont_use_simply_calculate = False
  img_dict = {}
  bucket_dict = {}
  
  bucket_resolutions = []
  # bucket のソート
  y = 0
  for x in bucket_size:
    bucket_dict[f"bucket{y}"] = x
    y += 1
  
  print(f"bucket_dict: {bucket_dict}")
  
  for file in file_extension_filter(os.listdir(calc_target_dir), [".png"]):
    width, height, image_path = load_res(os.path.join(calc_target_dir, file))
    
    img_dict[image_path] = [width, height]
    
  print(f"img_dict: {img_dict}")
  
  if len(img_dict) == 0:
    raise FileNotFoundError("Cannot find PNG File from target_dir")
  
  img_info = calc_near_bucket(bucket_dict, img_dict, not dont_use_simply_calculate)
  print(f"img_info: {img_info}")
  
  for filename, value in img_info.items():
    src = filename
    filedir = os.path.dirname(filename)
    basename = os.path.basename(filename)
    ext = os.path.splitext(filename)[1]
    filename = basename + ext
    filepath = os.path.join(filedir, f"{value[1][0]}_{value[1][1][0]}x{value[1][1][1]}", filename)
    basedir = os.path.join(filedir, f"{value[1][0]}_{value[1][1][0]}x{value[1][1][1]}")
    
    os.makedirs(basedir, exist_ok=True)
    shutil.copy(src, filepath)


if __name__ == "__main__":
  targetDirectory = "Folder not selected"
  while targetDirectory == "Folder not selected" or targetDirectory == "":
    targetDirectory = browse_folder()
  
  main(
    targetDirectory,
    [(512, 512), (1024, 1024)], True
  )