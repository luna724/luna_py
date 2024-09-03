from PIL import Image

def rotate(image:Image.Image, angle:int) -> Image.Image:
  return image.rotate(angle, expand=True)