import gradio as gr
from typing import *
from tkinter import Tk, filedialog
import re
import os

from modules.shared import ROOT_DIR

def multiple_replace(str: str, replace_key: list =[("src", "rpl")]):
  """

"""
  
  for x in replace_key:
    str = str.replace(x[0], x[1])
  
  return str


def re4prompt(pattern: str | Pattern[str], text: str):
  """ コンマで区切り、対象パターンのindex0のすべてを持つリストを返す
  
  """
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
    
    
def keycheck(dicts, target, rtl_if_fail="", silent=True):
  """ keyError を回避しながら辞書からの値取得を行う

  """
  if silent:
    def print(*args):
      return
  
  if not isinstance(target, str):
    return ""
  try:
    rtl = dicts[target]
  except KeyError:
    rtl = rtl_if_fail
    
    print(f"Traceback:\nKeyError: {target} in dict \n{dict}")
  return rtl


def get_index(lists, index: int=0, rtl_if_fail="", silent=True):
  """ indexError / TypeError を回避しながらリストからの値取得を行う"""
  
  if silent:
    def print(*args):
      return
    
  if not isinstance(index, int):
    return rtl_if_fail
  
  try:
    rtl = lists[index]
  
  except IndexError:
    print(f"Traceback:\nIndexError: {index}")
    return rtl_if_fail
  
  except TypeError:
    print(f"Traceback:\nTypeError: {lists}")
    return rtl_if_fail
  
  return rtl


def get_keys_from_dict(input_dict: dict ={}, keys_list=["", "keys"], if_fail_value=None): # 
  """This function is generated by. Colab AI
  
  KeyErrorを回避しながら辞書から複数の値の取得を行い、tuple形式で返す
  """
  return tuple(input_dict.get(key, if_fail_value) for key in keys_list)


def get_keys_from_list(input_list: list=[], indexes_list=[0, 1], if_fail_value=None): # 
  """IndexError を回避しながらリストから複数の値の取得を行い、tuple形式で返す"""
  return tuple(get_index(input_list, key, rtl_if_fail=if_fail_value) for key in indexes_list)


def show_state_from_checkbox(status: bool):
  return gr.update(visible=status)