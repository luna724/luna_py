from augmentation.func.augments._rotate import rotate
from augmentation.func.functions import Augment
import os

class Rotate90(Augment):
  def __init__(self):
    super().__init__()
    self.augment_name = "Rotate270"
  
  def augment(self, img, fn, **kw):
    return rotate(img, 270), f"{os.path.splitext(fn)[0]}-rotate270{os.path.splitext(fn)[1]}"