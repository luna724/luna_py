from augmentation.func.functions import Augment

from PIL import Image
from typing import *
import os

class invertHorizontal(Augment):
  def __init__(self):
    super().__init__()
  
    self.augment_name = "Invert (Horizontal)"
  
  def augment(self, image: Image.Image, fn:str, **kw):
    img = image.transpose(Image.FLIP_LEFT_RIGHT)
    
    fn = os.path.splitext(fn)[0] + "-inverted" + os.path.splitext(fn)[1]
    return img, fn