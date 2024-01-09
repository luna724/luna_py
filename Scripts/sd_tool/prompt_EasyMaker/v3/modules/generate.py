import gradio as gr
import os
from typing import *

from py import lib as v1_lib
from py.lib import delete_duplicate_comma
from modules.lib import multiple_replace
from modules.shared import ROOT_DIR
from modules.generate_util import prompt_character_resizer

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
  
  try:
    _ = value[0]
    if len(value) == 4:
      version = "v1"
    elif value[0] == "v2":
      version = "v2"
    elif value["Method"] == "v3":
      version = "v3"
    else:
      raise ValueError("Could not analyze method version")
  except IndexError as e:
    print(f"Catched: IndexError {e}")
    print("pass..  (generate.py / get_template_value)")
    if len(value) == 4:
      version = "v1"
    elif value["Method"] == "v3":
      version = "v3"
    else:
      raise ValueError("Couldn't analyze method version")
  except KeyError as e:
    print(f"Catched: KeyError {e}")
    print("pass.. (generate.py / get_template_value)")
    version = value["Method"]
  return value, version

def generate(
  template_type: str,
  lora: str,
  location: str,
  face: str,
  header: str,
  lower: str,
  lora_weight: float,
  use_face_for_adetailer: bool,
  activate_negative: bool,
  overall_weight: float,
  modes="ui"
):
  # template を取得 
  data, template_ver = get_template_value(template_type)
  values = data["Values"]
  
  prompt = values["Prompt"]
  negative = values["Negative"]
  ad_prompt = values["AD_Prompt"]
  ad_negative = values["AD_Negative"]
  
  prompt = prompt_character_resizer(
    prompt, lora_weight, lora
  )
  prompt = multiple_replace(
    prompt,
    replace_key=[
      ("$LOCATION", location.strip().strip(",")),
      ("%LOCATION%", location.strip().strip(",")),
      ("$FACE", face.strip().strip(",")),
      (r"%FACE%", face.strip().strip(","))
    ]
  )
  
  if use_face_for_adetailer:
    if overall_weight != 1.0:
      face = f'({face.strip().strip(",")}:{overall_weight})'
    face = ", " + face
    ad_prompt = ad_prompt + face
    if activate_negative:
      face = f'({face.strip().strip(",")}:-1.25)'
      ad_negative = ad_negative + ", " + face
  
  prompt = header.strip(",").strip() + prompt + lower.strip(",").strip()
  
  if modes != "ui":
    return delete_duplicate_comma(prompt), negative, ad_prompt, ad_negative, data, template_ver
  return delete_duplicate_comma(prompt), negative, ad_prompt, ad_negative, "OK."

