import pyperclip
import gradio as gr
import random
import re
from typing import List

from modules.v1_component import delete_duplicate_comma
from modules.config.get import cfg as config
from modules.lib import re4prompt, multiple_replace
from modules.generate import get_template

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

def keyword_updater(prompt, copy) -> str:
  return re.sub(r'%LORA:([0-9]*\.?[0-9]+)%', "$LORA", multiple_replace(
    prompt, [
      ("%LORA%", "$LORA"), ("%CH_NAME%", "$NAME"), ("%CH_PROMPT%", "$PROMPT"),
      ("%FACE%", "$FACE"), ("%LOCATION%", "$LOCATION")
    ]
  ))

def randprompt(copy:bool, blacklist:List[str]=[], count:str=0, weights:float=1.0, weight_max:float=1.0, remove_duplicate:bool=True) -> str:
  custom_weight_enable = weights != weight_max
  
  pass_word = ["<lora:", "$LORA", "$NAME", "$PROMPT", "$FACE", "$LOCATION", "$$HEADER", "$$LOWER", "$FACE2", "$LOCATION2", "$CLOTH", "$CLOTH2", "$ACCESSORY", "$VARIABLE", "%LORA%", "%CH_NAME%", "%CH_PROMPT%", "%FACE%", "%LOCATION%"] + ["$VARIABLE{}".format(x) for x in range(1, 11)]
  spec_word = ["(", ")", "[", "]"]
  
  prompts = ""
  word_list = []
  for prompt in get_template("full").values():
    if prompt["Key"] in blacklist:
      continue
    for x in prompt["Values"]["Prompt"].split(","):
      word_list.append(x)
  
  if len(word_list) <= 0:
    raise gr.Error("At least one template must be defined")
  
  for _ in range(count):
    loop = True
    while loop:
      word = multiple_replace(random.choice(word_list),
        [(sc, "") for sc in spec_word]
      )
      
      if not word in "<lora:":
        word = re.sub(
          r"(:[0-9]+\.?[0-9]+)", "", word)

      if word in pass_word or word in "<lora:":
        continue
      
      if word in prompts.strip(", ") and remove_duplicate:
        continue
      
      if custom_weight_enable:
        weight = random.randrange(
          weights*100, weight_max*100, step=1
        ) / 100
        
        word = "("+word+":{})".format(weight)
      
      break
    
    prompts += word+", "
    
  return prompts.strip(", ")