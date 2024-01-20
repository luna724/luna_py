from typing import *
from tkinter import Tk, filedialog
import re
import os

from modules.shared import ROOT_DIR

def multiple_replace(str: str, replace_key: list =[("src", "rpl")]):
  for x in replace_key:
    str = str.replace(x[0], x[1])
  
  return str


def re4prompt(pattern: str | Pattern[str], text: str):
  # コンマで区切り、対象パターンを発見したらついかする
  prompt_piece = text.split(",")
  rtl = []
  
  for x in prompt_piece:
    x = x.strip()
    r = re.findall(pattern, x)
    if r:
      rtl.append(r[0])
  
  return rtl


def mkdir(path:list, tree:bool=False, root:str=ROOT_DIR):
  """

  Args:
      path (list): os.path.join's path
      tree (bool, optional): tree mkdir. Defaults to False.
      root (str, optional): root dir. Defaults to ROOT_DIR.

  Returns:
      str: Resized path
  """
  raw_path = path
  
  path = root
  for x in raw_path:
    path = os.path.join(path, x)
    if tree:
      if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
      if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)
  
  try:
    os.makedirs(path, exist_ok=True)
  except FileNotFoundError as e:
    print(f"Catched: FileNotFoundError: {e}\n Retrying with tree=True")
    return mkdir(raw_path, True, root=root)

  return path

def browse_file():
  root = Tk()
  root.attributes("-topmost", True)
  root.withdraw()
  
  filenames = filedialog.askopenfilenames()
  if len(filenames) > 0:
      root.destroy()
      return str(filenames)
  else:
      filename = "Files not seleceted"
      root.destroy()
      return str(filename)