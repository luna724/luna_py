import gradio as gr
import os
import re
from typing import *

from py import lib as v1_lib
from modules.lib import *
from modules.shared import ROOT_DIR

def get_lora_list(variant:Literal["update", "manual"] ="update",parse:bool=False,name:str=""):
  if variant == "manual":
    lora_raw = v1_lib.jsoncfg.read(
      os.path.join(ROOT_DIR, "database", "v3", "lora_list.json")
    )
    
    rtl = list(lora_raw.keys())
    
    if parse:
      if not name in rtl:
        return f"Failed. {name} is not in lora_list", "", "", "", ""
      data = lora_raw[name][1]
      
      return name, data["lora"], data["name"], data["prompt"], data["extend"]
    
    return rtl
  elif variant == "update":
    return gr.Dropdown.update(choices= list(v1_lib.jsoncfg.read(
      os.path.join(ROOT_DIR, "database", "v3", "lora_list.json")
    ).keys()))
  return None

def control_lora_weight(lora_string: str, weight: float = 1.0):
  # 変換
  new_lora_string = re.sub(r"<lora:.*:(.+)>", weight, lora_string, count=1)
  print(f"[lora Weight controller]: {lora_string} -> {new_lora_string}")
  
  return new_lora_string

def prompt_character_resizer(prompt:str, weight:float, key:str):
  key, lora, name, ch_prompt, extend = get_lora_list("manual",parse=True,name=key)
  lora = control_lora_weight(lora, weight)
  
  prompt.replace(
    "%LORA%", lora).replace(
    "%CH_NAME%", name).replace(
    "%CH_PROMPT%", ch_prompt + extend).replace(
    )
  
  if "%LORA:" in prompt:
    # v1 / v2 Lora Weight Controller System
    # Lora weight を 1.0 に設定
    lora = control_lora_weight(lora, 1.0)
    lw, replacefrom = v1_lib.get_loraweight(prompt)
    prompt = prompt.replace(
      replacefrom, f"{lora}$WEIGHT"
    )
    prompt = prompt.replace(
      ":1.0>$WEIGHT", f":{lw}>"
    )
    
  # v3 method
  prompt = multiple_replace(
    prompt,
    replace_key=[
      ("$LORA", lora),
      ("$NAME", name),
      ("$PROMPT", ch_prompt + extend)
    ])

def lora_saver(
  json_key_name: str,
  lora_id: str = "<lora:example:1.0>",
  lora_name: str = "example",
  lora_prompt: str = "long hair, aqua hair",
  lora_prompt_extended: str = "cute",
  overwrite: bool = False
):
  lora_db = {
    json_key_name: ["v3", {
      "lora": lora_id,
      "name": lora_name,
      "prompt": lora_prompt,
      "extend": lora_prompt_extended
    }]
  }
  
  prv_lora_db = v1_lib.jsoncfg.read(
      os.path.join(ROOT_DIR, "database", "v3", "lora_list.json")
    )
  
  if json_key_name in prv_lora_db and overwrite:
    return f"stderr: this name is already taken."
  
  prv_lora_db.update(lora_db)
  
  v1_lib.jsoncfg.write(
    os.path.join(ROOT_DIR, "database", "v3", "lora_list.json")
  )
  return "Done."

def lora_updater(overwrite):
  v1_lora_dict = v1_lib.jsoncfg.read(
    os.path.join(ROOT_DIR, "database", "charactor_lora.json")
  )
  v1_lora_dict_prompt = v1_lib.jsoncfg.read(
    os.path.join(ROOT_DIR, "database", "charactor_prompt.json")
  )
  # 結合
  for key, p in v1_lora_dict_prompt.items():
    if key in v1_lora_dict.keys():
      prv_list = v1_lora_dict[key]
      new_list = prv_list.append(p)
      v1_lora_dict[key] = new_list
  
  new_lora_dict = v1_lib.jsoncfg.read(
    os.path.join(ROOT_DIR, "database", "v3", "lora_list.json")
  )
  skip_list = []
  
  for prv_key, prv_list in v1_lora_dict.items():
    if prv_key in new_lora_dict.keys() and not overwrite:
      skip_list.append(prv_key)
      continue
    else:
      new_lora_dict[prv_key] = [
        "v3", {
          "lora": prv_list[0],
          "name": prv_list[1],
          "prompt": prv_list[2],
          "extend": ""
        }
      ]
      del v1_lora_dict[prv_key] 
  
  # Skipped list
  print(f"Skipped List: {skip_list}")
  
  return "done."