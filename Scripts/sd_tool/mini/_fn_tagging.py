from typing import *
import os, re
import string
from tkinter import Tk, filedialog

def browse_directory():
  root = Tk()
  root.attributes("-topmost", True)
  root.withdraw()
  
  filenames = filedialog.askdirectory()
  if len(filenames) > 0:
    root.destroy()
    return str(filenames)
  else:
    raise ValueError("Please enter directory.")

def call():
  target = browse_directory()
  os.chdir(target)
  print(f"target: {target}")
  
  pattern = r"^([a-zA-Z_]+)(\d+)?.*"
  files = os.listdir(target)
  
  for f in files:
    fn, ext = os.path.splitext(f)
    if ext == ".txt":
      continue
    
    match = re.match(pattern, f)
    
    if not match:
      print(f"{fn}: isn't matched pattern")
      continue
    
    caption = match.group(1)
    print(f"{fn}: Matched {caption}")
    
    with open(f"{fn}.txt", "r") as file:
      captions = file.read()
    
    if len(captions) != 0:
      caption = f", {caption}"
    else:
      pass
    
    with open(f"{fn}.txt", "w", encoding="utf-8") as file:
      file.write(captions+caption)

call()

"""README

概要: 対象ファイル名をキャプションファイルの最後に追加する
キャプションファイルは .txt、Deepbooruスタイルにのみ対応

対象ファイル命名規則: 
"^([a-zA-Z_]+?)(\d+?).*"
(例: ankh40.png) (例: ankh-rotated.png) (例: ankh420-rotate90.png) -> ankh
"""