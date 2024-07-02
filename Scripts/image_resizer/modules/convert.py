from PIL import Image

import multiprocessing as mp

def hex_to_rgb(hex_code: str) -> tuple:
  # '#' を取り除く
  hex_code = hex_code.lstrip('#')
  
  # RGB値に変換
  rgb = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
  
  return rgb[0], rgb[1], rgb[2]

def remove_color(image:Image.Image, target_color:tuple= (255,255,255), convert_to:tuple= (0,0,0,0), **kw) -> Image.Image:
  img:Image.Image = image.convert("RGBA")  # RGBAモードに変換して透明度を持たせる
  data = img.getdata()  # 画像のピクセルデータを取得
  
  if isinstance(target_color, str):
    target_color = hex_to_rgb(target_color)
  if isinstance(convert_to, str):
    a,b,c = hex_to_rgb(convert_to)
    convert_to = (a,b,c,255)
  
  new_data = []
  for item in data:
    # RGBカラーを取得
    rgb = item[:3]
    # 指定した色が見つかった場合は透明にする (条件に合う色が赤色の場合)
    if rgb == target_color:
      new_data.append(convert_to)  # 透明なピクセルを追加
    else:
      new_data.append(item)  # 元のピクセルを追加
  
  img.putdata(new_data)  # 新しいピクセルデータを画像に適用
  return img

def tunnel(i:Image.Image, mode, *arg, **kw):
  if mode == "Color Converter":
    print(arg)
    
    if arg[2]:
      ct = (255, 255, 255, 0)
    else:
      ct = arg[1]
    
    return remove_color(
      i, arg[0], ct
    )
  
  elif mode == "Template Converter":
    from modules.template import invert, rotate, monochrome
    if arg[0]:
      i = invert(i)
    if arg[2]:
      i = monochrome(i)
    
    return rotate(i, arg[1])