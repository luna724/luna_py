from augmentation.func.functions import Augment

from PIL import Image
from typing import *
import random
import os

class invertHorizontal(Augment):
  def __init__(self):
    super().__init__()
  
    self.augment_name = "Zoom-out"
  
  def augment(self, image: Image.Image, fn:str, **kw):
    zoom_factor = random.randrange(105, 120, 1) / 100
    
    # 元の画像サイズを取得
    original_width, original_height = image.size
    
    # ズームアウト後のサイズを計算
    new_width = int(original_width * zoom_factor)
    new_height = int(original_height * zoom_factor)
    
    # 画像をズームアウト（縮小）
    zoomed_out_image = image.resize((new_width, new_height), Image.LANCZOS)
    
    # 新しい画像を作成（透明な背景を持つキャンバスを作成）
    new_image = Image.new("RGBA", (original_width, original_height), (255, 255, 255, 0))
    
    # 新しいキャンバスの中心にズームアウトした画像を貼り付ける
    offset = ((original_width - new_width) // 2, (original_height - new_height) // 2)
    new_image.paste(zoomed_out_image, offset)
    
    # RGBA使用のため png に変換
    fn = os.path.splitext(fn)[0] + "-zoomed_out" + ".png"
    return new_image, fn