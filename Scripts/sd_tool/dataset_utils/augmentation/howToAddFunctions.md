## Add Augmentation to this function
1. create py file in `func/augments/`
2. import `Augment` class from `augmentation.func.functions` 
3. below, example override code

`func/augments/example.py`
```py
import PIL.Image
import numpy as np
from typing import *

from augmentation.func.functions import Augment

class YourAugment(Augment):
  def __init__(self):
    super().__init__()

    # Augment name in WebUI "Augmentations" List
    self.augment_name:str = "Invert (color)"

    # Augment index in WebUI "Augmentations List
    ## Optional (Default: -1)
    self.augment_index:int = 0

    # Augment default value
    ## Optional (Default: True)
    self.augment_default:bool = True

    # Augment exclude from random function
    # CURRENTLY, THIS VARIABLES NOT AFFECT TO CODE!
    ## Optional (Default: False)
    self.exclude_random:bool = False

  def augment(self, image: PIL.Image, fn:str, **kw) -> Tuple[PIL.Image, str]:
    # Augment main function
    # Arg1: Image class. (PIL.Image), arg2: Filename (str)
    # return will be (PIL.Image, str)
    # str are filename

    inverted = np.invert(image)
    return PIL.Image.fromarray(inverted), fn
```