import gradio as gr
import os
from typing import *

import LGS.misc.jsonconfig as jsoncfg
from modules.v1_component import delete_duplicate_comma
from modules.lib import multiple_replace
import modules.shared as shared
from modules.shared import ROOT_DIR, noneimg
from modules.generate_util import prompt_character_resizer
from modules.generate_util import get_lora_list as get_lora_list_manual

def get_template(variant="update", target_dn="NONE"): # target_dn = Target DisplayName
  if variant == "manual":
    return list(
      jsoncfg.read(
        os.path.join(ROOT_DIR, "database", "v3", "template_list.json")
      ).keys()
    )
  elif variant == "full":
    return jsoncfg.read(
      os.path.join(
        ROOT_DIR, "database", "v3", "template_list.json"
      )
    )
    
  elif variant == "update":
    return gr.Dropdown.update(
      choices=list(
      jsoncfg.read(
        os.path.join(ROOT_DIR, "database", "v3", "template_list.json")).keys()))

  elif variant == "webui":
    template = get_template("full")
    try:
      rtl = []
      
      for key, x in template.items():
        rtl.append(x["displayName"])
    except IndexError as e:
      print(f"Catched V2 or V1 Dict: {key}")
      rtl.append(key)
      print(f"IndexError: {e}")
      pass
    except KeyError as e:
      print(f"Catched V2 or V1 Dict: {key}")
      rtl.append(key)
      print(f"KeyError: {e}")
      pass
      
    return rtl
    
def get_template_value(name: str):
  def get_key_by_dn(data, target_value):
    for key, value in data.items():
      if not isinstance(value, dict):
        pass
      if value["displayName"] == target_value:
        return key
    raise ValueError("\nCan't find key from displayName. try refresh template list. or you're using custom dict?")
  # 読み込み
  try:
    value = get_template("full")[name]
  except KeyError as e:
    print(f"Exchange displayName: {name} ->", end="")
    tmp = get_key_by_dn(get_template("full"), name)
    value = get_template("full")[tmp]
    print(f" {tmp}")
    pass
    #print(f"KeyError: {e}")
    #return "KeyError occurred. (try refresh the template list)", "Unknown"
  
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
  
  if template_ver == "v3":
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

  elif template_ver == "v2":
    return

  elif template_ver == "v1":
    return
  
  else:
    raise ValueError("Unknown Template Version")

def example_view(template_name):
  def check(target, mode: Literal["str","num"]="str"):
    if mode == "str":
      if not isinstance(target, str):
        if isinstance(target, int) or isinstance(target, float):
          return check(target, mode="num")
        return target
      if target == "None":
        return ""
      else:
        return target
    elif mode == "num":
      if isinstance(target, str):
        if target == "None":
          target = "-1.0"
        target = float(target)
      if isinstance(target, int):
        return target
      if isinstance(target, float):
        return target
      else:
        return -2
    else:
      return None
      
  def keycheck(dicts, target, rtl_if_fail=""):
    if not isinstance(target, str):
      return ""
    try:
      rtl = dicts[target]
    except KeyError:
      rtl = rtl_if_fail
      
      print(f"Traceback:\nKeyError: {target} in dict \n{dict}")
    return rtl
  data, version = get_template_value(template_name)
  
  if not version in shared.data.generate_py.acceptable_version or keycheck(data, "Method_Release", 0) <= 1:
    raise ValueError("v3 UI's Example View System is only supported v3.0.2 and above Template System")
  

  # ControlNet
  if keycheck(data, "Method_Release", 0) >= 2:
    cn_show_state = data["ControlNet"]["isEnabled"]
    if cn_show_state:
      cn_image = data["ControlNet"]["Image"]
      cn_image_show_state = True
      if not os.path.exists(cn_image):
        cn_image = noneimg
        cn_image_show_state = False
    else:
      cn_image = noneimg
      cn_image_show_state = False
    cn_mode = check(data["ControlNet"]["Mode"])
    cn_weight = check(data["ControlNet"]["Weight"], mode="num")

  # Hires
    hires_show_state = data["Hires"]["isEnabled"]
    hires_upscale = check(data["Hires"]["Upscale"], mode="num")
    hires_sampler = check(data["Hires"]["Sampler"])
    hires_denoise = check(data["Hires"]["Denoising"], mode="num")
    hires_steps   = check(data["Hires"]["Steps"], mode='num')
  
  # Example
    ex_show_state = data["Example"]["isEnabled"]
    character_data = check(data["Example"]["Character"])
    lora = check(data["Example"]["Lora"])
    name = check(data["Example"]["Name"])
    prompt = check(data["Example"]["Prompt"])
    face = check(data["Example"]["Face"])
    location = check(data["Example"]["Location"])
    header = check(data["Example"]["Header"])
    lower = check(data["Example"]["Lower"])
    csn = check(data["Example"]["CustomNegative"])
    isextend = data["Example"]["isExtend"]
    
    ex_image = check(data["Example"]["Image"])
    ex_image_show_state = True
    if not os.path.exists(ex_image):
      ex_image = noneimg
      ex_image_show_state = False
    
    if character_data in get_lora_list_manual("manual"):
      character_data, lora, name, prompt, extend = get_lora_list_manual("manual", True, character_data)
  
  # Builtins
    resolution = check(data["Resolution"])
    sampler = check(data["Sampler"])
    clip = check(data["Clip"], mode='num')
    
    method_ver = f'{keycheck(data, "Method_Release", 0)}'
  
  return character_data, lora, name, prompt, isextend, face, location, header, lower, csn, gr.Dropdown.update(visible=ex_image_show_state), ex_image, resolution, clip, sampler, gr.Dropdown.update(visible=hires_show_state), hires_sampler, hires_steps, hires_denoise, hires_upscale, gr.Dropdown.update(visible=cn_show_state), cn_mode, cn_weight, cn_image, method_ver