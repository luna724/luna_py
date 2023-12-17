from typing import *



def multiple_replace(str: str, replace_key: list =[("src", "dst")]):
  for x in replace_key:
    str = str.replace(x[0], x[1])
  
  return str