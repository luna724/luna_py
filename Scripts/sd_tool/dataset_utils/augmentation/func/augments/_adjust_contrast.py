from augmentation.func.functions import Augment

from PIL import Image, ImageEnhance
from typing import *
import random
import os

class invertHorizontal(Augment):
  def __init__(self):
    super().__init__()
  
    self.augment_name = "Adjust-contrast"
  
  def augment(self, image: Image.Image, fn:str, **kw):
    factor = random.choice([random.randrange(80, 95, 1) / 100, random.randrange(105, 125, 1) / 100])
    fn = os.path.splitext(fn)[0] + f"-contrast{factor}" + os.path.splitext(fn)[1]
    
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(factor)
    
    return enhanced_image, fn 