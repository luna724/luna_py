import pyperclip
import gradio as gr
import random
from typing import List

from modules.v1_component import delete_duplicate_comma
from modules.lib import re4prompt

def _2space(target, cp:bool, reverse:bool) -> str:
  v =[]
  for x in target.split(","):
    x:str = x.strip()
    
    if x.count("<lora:") >= 1:
      v.append(x)
      continue
      
    print(x)
    if reverse:
      x = x.replace(" ", "_")
    else:
      x = x.replace("_", " ")
    v.append(x)
  
  item = ""
  for x in v:
    item += x+", "
  
  if cp:
    print("Previous copied item: "+pyperclip.paste())
    pyperclip.copy(delete_duplicate_comma(item))
  
  return delete_duplicate_comma(item)

def randkeyword(target, cp:bool, except_sorting:str="") -> str:
  """ randkeyword
  Keyword shuffler / randkeyword.py """
  def intcheck(x) -> bool:
    try:
      int(x)
      return True
    except ValueError:
      return False
    
  v = []
  t = [x.strip() for x in target.strip().strip(",").split(",") if isinstance(x, str)]

  except_sorting = [
    int(x.strip()) for x in except_sorting.split(",") if intcheck(x)
  ]

  value = []
  
  # value に key:int0000~9999: value, index を代入
  def randint(min=0,max=0,step=1) -> int:
    v = random.randrange(min, max, step)
    while v in except_sorting:
      v += random.randrange(min+1, max-v)
      if v >= max:
        v = random.randrange(min, max)
    return v
    
  for i, d in enumerate(t):
    i+=1
    value.append((d, randint(0, len(t))))
    
    if i in except_sorting:
      value.append((d, i))
  
  
  def sort(item):
    return item[1]
  value = sorted(value, key=sort)
  
  item = ""
  for v, _ in value:
    item += v+", "
  item = item.strip(", ")+","
  
  if cp:
    print("Previous copied item: "+pyperclip.paste())
    pyperclip.copy(delete_duplicate_comma(item))
  
  return item


def add_targets(text:str, targets: list) -> dict:
  """ Anti keyword extend function"""
  if text.count(",") < 1:
    return gr.Textbox.update(visible=True), gr.Dropdown.update(visible=True)
  if targets is None:
    targets = []
  
  target = text.split(",")[0]
  text = text.replace(target+",", "")
  
  if not target in targets:
    targets.append(target)
  
  return gr.Textbox.update(value=text), gr.Dropdown.update(value=targets, choices=targets)

def anti_keyword(prompt, target, copy, sensitive) -> str:
  def r(x:str) -> str:
    if sensitive:
      return x.strip()
    return x.strip().strip(",").strip()
  
  prompt = ""
  words = [
    r(x) for x in r(prompt).split(",")
  ]
  target = [
    r(x) for x in target
  ]
  
  for x in words:
    if x in target:
      continue
    prompt += x+", "
  
  return prompt.strip(", ")