from augmentation.func.functions import Augment

from PIL import Image
from typing import *
import os
import numpy as np

class invertHorizontal(Augment):
  def __init__(self):
    super().__init__()
  
    self.augment_name = "Invert (Color)"
    self.augment_default = False
  
  def augment(self, image: Image.Image, fn:str, **kw):
    img = Image.fromarray(
      np.invert(image)
    )
    
    fn = os.path.splitext(fn)[0] + "-color_inverted" + os.path.splitext(fn)[1]
    return img, fn