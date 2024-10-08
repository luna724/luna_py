from typing import *
import os
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


def call(args:List[str]):
  os.chdir(
      browse_directory()
  )
  
  root = os.getcwd()
  print(f"root: {root}")
  files = os.listdir()
  dirs_name = os.path.basename(root)[-1]
  
  for f in files:
    fn, ext = os.path.splitext(f)
    
    if ext == ".txt":
      continue
    
    if not f"{fn}.txt" in files:
      print(f"{f}: aren't have Captions.txt")
      continue
      
    with open(f"{fn}.txt", "r", encoding="utf-8") as file:
      captions = file.read()
    
    if len(file) != 0:
      caption = f", {dirs_name}"
    else:
      caption = {dirs_name}
    
    with open(f"{fn}.txt", "w", encoding="utf-8") as file:
      file.write(captions+caption)
  
  print("ALL Tasks done.")

call([""])