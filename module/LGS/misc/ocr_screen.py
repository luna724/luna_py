import pytesseract
from PIL import ImageGrab
import luna_GlobalScript.misc.global_math as cur

def img2txt(x1, x2, y1, y2, bx, by, detect=False, lang=""): 
# x1 y1 x2 y2 = box
# detect = 検出対象文字
# Trueの場合、booleanで返す
# bx, by = 位置を取得した画面のpx
# lang = 検出対象の言語 
# 指定されない場合、jpnとengを指定
  x1 = cur.cursor_exchanger(x1, bx, "x")
  x2 = cur.cursor_exchanger(x2, bx, "x")
  y1 = cur.cursor_exchanger(y1, by, "y")
  y2 = cur.cursor_exchanger(y2, by, "y")
  if lang == "":
    lang = "jpn+eng"
  screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
  text = pytesseract.image_to_string(screenshot, lang=lang)
  if detect:
    if text.count(detect) >= 1:
      return True
    else:
      return False
  else:
    return text