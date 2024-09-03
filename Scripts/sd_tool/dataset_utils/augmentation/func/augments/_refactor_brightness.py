from augmentation.func.functions import Augment

from PIL import Image, ImageEnhance
from typing import *
import random
import os

class invertHorizontal(Augment):
  def __init__(self):
    super().__init__()
  
    self.augment_name = "Refactor-brightness"
  
  def augment(self, image: Image.Image, fn:str, **kw):
    factor = random.choice([random.randrange(80, 95, 1) / 100, random.randrange(103, 115, 1) / 100])
    fn = os.path.splitext(fn)[0] + f"-brightness{factor}" + os.path.splitext(fn)[1]
    
    # ImageEnhance.Brightnessを使って明度を調整
    enhancer = ImageEnhance.Brightness(image)
    enhanced_image = enhancer.enhance(factor)
    
    return enhanced_image, fn