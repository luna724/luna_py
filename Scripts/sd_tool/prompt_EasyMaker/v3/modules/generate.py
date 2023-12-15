import gradio as gr
import os
from typing import *

from py import lib as v1_lib
from modules.shared import ROOT_DIR

def get_template(variant="update"):
  if variant == "manual":
    return list(
      v1_lib.jsoncfg.read(
        os.path.join(ROOT_DIR, "database", "v3", "template_list.json")
      ).keys()
    )
  elif variant == "full":
    return v1_lib.jsoncfg.read(
      os.path.join(
        ROOT_DIR, "database", "v3", "template_list.json"
      )
    )
    
  elif variant == "update":
    return gr.Dropdown.update(
      choices=list(
      v1_lib.jsoncfg.read(
        os.path.join(ROOT_DIR, "database", "v3", "template_list.json")).keys()))

def get_template_value(name: str):
  # 読み込み
  try:
    value = get_template("full")[name]
  except KeyError as e:
    print(f"KeyError: {e}")
    return "KeyError occurred. (try refresh the template list)"
  
  if len(value) == 4:
    version = "v1"
  elif value[0] == "v2":
    version = "v2"
  elif value["value"] == "v3":
    version = "v3"
  else:
    raise ValueError("Could not analyze method version")
  
  return value, version