import pyperclip
import re
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