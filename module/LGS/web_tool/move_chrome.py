import pyautogui
import time
import pyperclip
from LGS.misc.global_math import cursor_exchanger as cur

def forcemove_pyautogui(url):
  pyautogui.hotkey('ctrl', 't')
  time.sleep(2.5)
  x = cur(600, 1280, "x")
  y = cur(50, 800, "y")
  pyautogui.click(x=x, y=y)  # def 1280, 800  click = 600, 50
  time.sleep(0.5)
  
  pyperclip.copy(url)  # URLをクリップボードにコピー
  pyautogui.hotkey("ctrl", "v")  # クリップボードの内容を貼り付け
  pyautogui.press('enter')
  time.sleep(3)