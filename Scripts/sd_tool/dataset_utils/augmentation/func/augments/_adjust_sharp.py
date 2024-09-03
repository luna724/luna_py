from augmentation.func.functions import Augment

from PIL import Image, ImageEnhance
from typing import *
import random
import os

class invertHorizontal(Augment):
  def __init__(self):
    super().__init__()
  
    self.augment_name = "Adjust-sharpness"
  
  def augment(self, image: Image.Image, fn:str, **kw):
    factor = random.choice([random.randrange(25, 85, 1) / 100, random.randrange(145, 225, 1) / 100])
    fn = os.path.splitext(fn)[0] + f"-sharp{factor}" + os.path.splitext(fn)[1]
    
    enhancer = ImageEnhance.Sharpness(image)
    enhanced_image = enhancer.enhance(factor)
    
    return enhanced_image, fn