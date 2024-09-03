from augmentation.func.functions import Augment

from PIL import Image
from typing import *
import random
import os

class invertHorizontal(Augment):
  def __init__(self):
    super().__init__()
  
    self.augment_name = "Zoom-in"
  
  def augment(self, image: Image.Image, fn:str, **kw):
    zoom_factor = random.randrange(115, 150, 1) / 100
    
    # 元の画像サイズを取得
    original_width, original_height = image.size
    
    # ズームイン後の切り取りサイズを計算
    crop_width = int(original_width / zoom_factor)
    crop_height = int(original_height / zoom_factor)
    
    # 中心座標を計算
    center_x, center_y = original_width // 2, original_height // 2
    
    # 切り取る領域の左上と右下の座標を計算
    left = center_x - crop_width // 2
    upper = center_y - crop_height // 2
    right = center_x + crop_width // 2
    lower = center_y + crop_height // 2
    
    # 画像を切り取り
    cropped_image = image.crop((left, upper, right, lower))
    
    # 切り取った画像を元のサイズにリサイズ
    zoomed_image = cropped_image.resize((original_width, original_height), Image.LANCZOS)
    
    fn = os.path.splitext(fn)[0] + "-zoomed_in" + os.path.splitext(fn)[1]
    return zoomed_image, fn