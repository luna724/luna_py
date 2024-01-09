from typing import *
import re


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