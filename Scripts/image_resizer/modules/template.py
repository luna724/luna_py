import numpy as np
from PIL import Image

def invert(i:Image.Image) -> Image.Image:
  img = np.invert(np.array(i))
  return Image.fromarray(img)

def rotate(i:Image.Image, angle:float) -> Image.Image:
  return i.rotate(angle, expand=True)

def monochrome(i:Image.Image) -> Image.Image:
  img = np.array(i)
  img = np.mean(img, axis=2, dtype=np.uint8)
  return Image.fromarray(img)

