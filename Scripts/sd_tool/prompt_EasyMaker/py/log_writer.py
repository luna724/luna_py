from datetime import datetime as d
import re
import shutil
import os
from random import randrange as ra

def w(target, in_prompt, ad_prompt):
  date = str(d.now())
  
  with open(target, "a") as f:
    f.write(f"\ndate: {date}\nPrompt ${in_prompt}\nADetailer Prompt ${ad_prompt}\n")
    

def r(target):
  
  if not os.path.exists(target):
    return "### Log File Not found."
  
  with open(target) as f:
      text = f.read()
      
  # mdけいしきにへんかん　
  text = text.replace("<", "\\<").replace(">", "\\>")
  
  # セットごとに分割
  sets = re.split('\n\n', text)
  print(sets)

  # データを格納するためのリスト
  data = []

  # 正規表現で日付とPromptの値、ADetailer Promptの値を抽出
  for set_text in sets:
      # '\ndate: 2023-08-28 14:43:41.795578\nPrompt $nsfw, <Lora:MODEL:1.2>, (tentacle clothes:1.2), tentacles, nipples, cowboy shot, blush+, <lora:MODEL>, ichika, , (best quality, masterpiece, detailed, incredibly fine illustration, kawaii), , light purple hair, light blue hair, blue eyes, straight hair, small twintale, 14 years old, cat ears\nADetailer Prompt $'
      lines = set_text.split('\n')
      date_match = re.search(r'date: (.+)', set_text)
      prompt_match = re.search(r'Prompt (.+)', set_text)
      adetailer_prompt_match = re.search(r'ADetailer Prompt (.+)', set_text)
      if date_match and prompt_match and adetailer_prompt_match:
          date = date_match.group(1)
          prompt_value = prompt_match.group(1)
          adetailer_prompt_value = adetailer_prompt_match.group(1)
          data.append((date, prompt_value, adetailer_prompt_value))

  # 目的のフォーマットに整形
  formatted_output = ""
  for date, prompt_value, adetailer_prompt_value in data:
      # prompt_value = prompt_value.replace(">", "\\>").replace("<", "\\<")
      # adetailer_prompt_value = adetailer_prompt_value.replace(">", "\\>").replace("<", "\\<")
    
      formatted_output += f"<details><summary>{date}</summary>\n"
      formatted_output += f"Prompt {prompt_value} <br>\n"
      formatted_output += f"ADetailer Prompt {adetailer_prompt_value} <br>\n"
      formatted_output += "</details>\n"
      
  
  return formatted_output


def delete(target):
  shutil.move(target, f"./cache/{target}{ra(0, 999999999):08d}.lunacache")