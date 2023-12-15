import gradio as gr
import os
from typing import *

from py import lib as v1_lib
from modules.shared import ROOT_DIR, DB_DIR

def get_lora_list(variant:Literal(["update", "manual"]) ="update",parse:bool=False,name:str=""):
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