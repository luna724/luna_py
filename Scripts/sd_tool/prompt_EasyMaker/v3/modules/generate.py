import gradio as gr
import os
from typing import *
import LGS.misc.jsonconfig as jsoncfg

import modules.shared as shared
from modules.v1_component import delete_duplicate_comma
from modules.lib import multiple_replace
from modules.shared import ROOT_DIR, noneimg
from modules.generate_util import prompt_character_resizer, control_lora_weight
from modules.generate_util import get_lora_list as get_lora_list_manual
from modules.lib import keycheck, get_index, get_keys_from_dict, get_keys_from_list, multiple_replace
from modules.regional_prompter import visualize

def get_template(variant="update", target_dn="NONE"): # target_dn = Target DisplayName
  """
  variant: ["update", "manual", "full"]
  
  update: for webUI return gr.Dropdown.update(): dict
  manual: return template keys list: list
  full:   return template full dict: dict
  """
  
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
    rtl = []
    
    for key, x in template.items():
      rtl.append(x["displayName"])
    
    return rtl
    
def get_template_value(name: str, rtl_resized_name:bool=False):
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
    if rtl_resized_name and value:
      return name
  except KeyError as e:
    print(f"Exchange displayName: {name} ->", end="")
    tmp = get_key_by_dn(get_template("full"), name)
    value = get_template("full")[tmp]
    print(f" {tmp}")
    
    if rtl_resized_name:
      return tmp
    
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
  load_extend: bool,
  use_adetailer_plus: bool,
  apply_positive: bool,
  apply_negative: bool,
  positive_weight: float,
  negative_weight: float,
  lora2: str,
  lora_weight2: float,
  location2: str,
  face2: str,
  header2: str,
  lower2: str,
  modes="ui"
):
  """DISCONTINUED Function
  New Method -> generate.py:template_convert"""
  lang = shared.language("err_manager", "raw")
  # lora = none?
  if lora == "" or None:
    print("Catch: lora == None")
    raise gr.Error(lang["err_cant_find_lora"])
      
  # template を取得 
  data, template_ver = get_template_value(template_type)
  
  if template_ver == "v3":
    values = data["Values"]
    
    prompt = values["Prompt"]
    negative = values["Negative"]
    ad_prompt = values["AD_Prompt"]
    ad_negative = values["AD_Negative"]
    
    prompt = prompt_character_resizer(
      prompt, lora_weight, lora, isextend=load_extend
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
    
    if use_adetailer_plus:
      if apply_positive:
        ad_prompt = ad_prompt.strip(",")
        if not positive_weight == 1.0:
          ad_prompt += f', ({face.strip(",")}:{positive_weight})'
        else:
          ad_prompt += ", "+face
      if apply_negative:
        ad_negative = ad_negative.strip(",")
        if not negative_weight == 1.0:
          ad_negative += f', ({face.strip(",")}:{negative_weight})'
        else:
          ad_negative += ", "+face
    
    if not header == "":
      header += ", "
    if not lower == "":
      lower = ", "+lower
      
    prompt = header + prompt + lower.strip()
    
    if keycheck(data, "Method_Release", 0) > 2:
      # v3 or above
      rpsp = keycheck(data["Regional_Prompter"], "Secondary_Prompt", {"isEnabled": False, "gFaL_from_Main": False})
      if data["Regional_Prompter"]["isEnabled"]:
        sec_prompt = rpsp["prompt"]
        sp =multiple_replace(
          sec_prompt,
          replace_key=[
            ("$LOCATION", location)
          ]
        )
    
    if modes != "ui":
      return delete_duplicate_comma(prompt), negative, ad_prompt, ad_negative, data, template_ver
    return delete_duplicate_comma(prompt), negative, ad_prompt, ad_negative, "OK."

  else:
    gr.Error(lang["err_unknown_template"])

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
    if not os.path.exists(ex_image) or ex_image == noneimg:
      ex_image = noneimg
      ex_image_show_state = False
    
    if character_data in get_lora_list_manual("manual"):
      print("Found character_data in get_lora_list-manual")
      character_data, lora, name, prompt, extend = get_lora_list_manual("manual", True, character_data)

  # Builtins
    resolution = check(data["Resolution"])
    sampler = check(data["Sampler"])
    clip = check(data["Clip"], mode='num')
    
    method_ver = f'{keycheck(data, "Method_Release", 0)}'
  
    # 3.0.3 or above  /  Regional Prompter
    rp = keycheck(data, "Regional_Prompter", {"isEnabled": False})
    rp_show_state = keycheck(rp, "isEnabled", False)
    
    rp_rp_mode, rp_mode, rp_base, rp_common_raw, rp_lora_stop_step_raw, rp_resolution_raw, rp_split_mode, rp_split_ratio, rp_base_ratio = get_keys_from_dict(
      rp, [
        "rp_mode", "mode", "base", "common", "lora_stop_step", "resolution",
        "split_mode", "split_ratio", "base_ratio"
      ]
    )
    rp_common, rp_common_negative = get_keys_from_list(rp_common_raw, if_fail_value=False)
    rp_lora_stop_step, rp_lora_hires_stop_step = get_keys_from_list(rp_lora_stop_step_raw, if_fail_value=False)
    rp_width, rp_height = get_keys_from_list(rp_resolution_raw, if_fail_value=512)
    
    if rp_show_state:
      rp_image, rp_template = visualize(
        rp_mode, rp_split_ratio, rp_width, rp_height, rp_common, rp_base, rp_base_ratio, rtl_template=True
      )
    else:
      rp_image = shared.noneimg
      rp_template = ""
    
    # 3.0.3 or above  /  Lora Weight
    ex = data["Example"]
    ex_lora_weight = get_keys_from_dict(
      ex, [
        "Weight"
      ], 1.0
    )
    
    # 3.0.3 or above  /  Secondary Prompt (Regional Prompter) 
    rpsp = keycheck(rp, "Secondary_Prompt", {"gFaL_from_Main": False})
    get_face_and_location_from_main = keycheck(rpsp, "gFaL_from_Main", False)
    second_prompt_root = False
    
    rpsp.pop("gFaL_from_Main")
    rpsp_prompt, rpsp_character, rpsp_weight, rpsp_lora, rpsp_name, rpsp_ch_prompt, rpsp_face, rpsp_location, rpsp_header, rpsp_lower = get_keys_from_dict(
      rpsp, list(rpsp.keys()), ""
    )
    
    if not rpsp_prompt == "":
      second_prompt_root = True
    
    if get_face_and_location_from_main:
      rpsp_face, rpsp_location = get_keys_from_dict(
        ex, [
          "Face", "Location"
        ], ""
      )
  
  return character_data, lora, ex_lora_weight, name, prompt, isextend, face, location, header, lower, csn, ex_image, resolution, clip, sampler, gr.Dropdown.update(visible=hires_show_state), hires_sampler, hires_steps, hires_denoise, hires_upscale, gr.Dropdown.update(visible=cn_show_state), cn_mode, cn_weight, cn_image, gr.Dropdown.update(visible=rp_show_state), rp_mode, rp_base, rp_common, rp_common_negative, rp_lora_stop_step, rp_lora_hires_stop_step, rp_width, rp_height, rp_split_mode, rp_split_ratio, rp_base_ratio, rp_image, rp_template, gr.Dropdown.update(visible=second_prompt_root), rpsp_character, rpsp_weight, rpsp_lora, rpsp_name, rpsp_ch_prompt, rpsp_face, rpsp_location, rpsp_header, rpsp_lower, method_ver, gr.Dropdown.update(visible=second_prompt_root)

def applicate_opts(template):
  data, _ = get_template_value(template)
  
  if keycheck(data, "Method_Release", 0) >= 3:
    # 3.0.3+ Only
    lw = get_keys_from_dict(
      data["Example"], [
        "Weight"
      ], 1.0
    )
    rp_active = keycheck(data["Regional_Prompter"], "isEnabled", False)
  
    return gr.update(visible=rp_active), lw

def applicate_lora(lora_template):
  _, lora, name, prompt, _ = get_lora_list_manual("manual",True,lora_template)
  return lora, name, prompt

def template_convert(
  template:str,
  lora_name:str,
  lora_id:str,
  ch_name:str,
  ch_prompt:str,
  location:str,
  face:str,
  header:str,
  lower:str,
  lora_weight:float,
  has_extend:bool,
  adetailer_plus:bool,
  apply_positive:bool,
  apply_negative:bool,
  apply_weight_to_positive:bool,
  apply_weight_to_negative:bool,
  sp_lora_name:str,
  sp_lora_id:str,
  sp_ch_name:str,
  sp_ch_prompt:str,
  sp_location:str,
  sp_face:str,
  sp_header:str,
  sp_lower:str,
  sp_sync_some:bool,
  sp_lora_weight:float,
  sp_has_extend:bool,
  convert_break_to_template:bool=False # beta Function. convert BREAK to Template value (e.g. BREAK -> ADDCOL)
):
  def r(x:str) -> str:
    return x.strip().strip(",")
  
  hastwo = False
  lang = shared.language("err_manager", "raw")
  
  # first prompt
  #Error Handling
  if lora_name == "" and lora_id == "":
    print("Catched: lora_name == None and lora_id == None")
    raise gr.Error(lang["err_cant_find_lora"])
  
  data, template_ver = get_template_value(template)
  
  # opts from lora_name
  if lora_name != "" and lora_id == "":
    _, lora, name, character_prompt, ch_extend = get_lora_list_manual(
      "manual", True, lora_name
    )
  
  # opts manually
  elif lora_id != "":
    lora = lora_id
  
  else:
    lora = lora_id
  
 
  if lora == lora_id:
    name = ch_name
    character_prompt = ch_prompt
    if not "ch_extend" in locals():
      ch_extend = ""
  

  values = data["Values"]
  
  prompt = values["Prompt"]
  negative = values["Negative"]
  ad_prompt = values["AD_Prompt"]
  ad_negative = values["AD_Negative"]
  
  lora = control_lora_weight(lora, lora_weight)
  
  lora, name, character_prompt, location, face = r(lora), r(name), r(character_prompt), r(location), r(face)
  
  if has_extend and isinstance(ch_extend, str):
    character_prompt += ", "+r(ch_extend)
  
  prompt1 = multiple_replace(
    prompt, [
      ("$LORA", lora),("%LORA%", lora),("$NAME",name),("%CH_NAME%",name),
      ("$PROMPT", character_prompt),("%CH_PROMPT%", character_prompt),
      ("$LOCATION", location),("%LOCATION%", location),("$FACE", face),
      (r"%FACE%", face)
    ]
  )
  prompt1 = r(r(header)+", "+r(prompt1)+", "+r(lower))+",".strip()
  
  
  if keycheck(data, "Regional_Prompter", {"isEnabled": False})["isEnabled"]:
    # RP == on
    rp = data["Regional_Prompter"]["Secondary_Prompt"]
    prompt = rp["prompt"]
    
    if lora_name == "" and lora_id == "":
      print("Catched: lora_name == None and lora_id == None (in sp)")
      raise gr.Error(lang["err_cant_find_lora"])
    
    ch_extend = ""
    if lora_name != "" and lora_id == "":
      _, lora, name, character_prompt, ch_extend = get_lora_list_manual(
        "manual", True, sp_lora_name
      )
    elif lora_id != "":
      lora = sp_lora_id
    else:
      lora = sp_lora_id
    
    if lora == sp_lora_id:
      name = sp_ch_name
      character_prompt = sp_ch_prompt
    
    # sync face, header, lower and location with first
    if sp_sync_some:
      sp_face = face
      sp_header = header
      sp_lower = lower
      sp_location = location
    
    lora = control_lora_weight(lora, sp_lora_weight)
    lora, name, character_prompt, location, face = r(lora), r(name), r(character_prompt), r(sp_location), r(sp_face)
    if sp_has_extend and isinstance(ch_extend, str):
      character_prompt += ", "+r(ch_extend)
    
    prompt2 = multiple_replace(
    prompt, [
      ("$LORA", lora),("%LORA%", lora),("$NAME",name),("%CH_NAME%",name),
      ("$PROMPT", character_prompt),("%CH_PROMPT%", character_prompt),
      ("$LOCATION", location),("%LOCATION%", location),("$FACE", face),
      (r"%FACE%", face)
    ])
    
    prompt2 = r(r(sp_header)+", "+r(prompt2)+", "+r(sp_lower))+",".strip()
    
    hastwo = True

  if hastwo and convert_break_to_template:
    # sp がある場合に BREAK を Template に変換するかどうか
    rp = data["Regional_Prompter"]
    _, rp_mode, rp_base, rp_common, rp_stop, rp_res, rp_split, rp_ratio = get_keys_from_dict(
      rp, [
        "rp_mode", "mode", "base", "common", "lora_stop_step", "resolution",
        "split_mode", "split_ratio", "base_ratio"
      ]
    )
    
    _, templates = visualize(
      rp_mode, rp_split, rp_res[0], rp_res[1], rp_common[0], rp_base, rp_ratio, rtl_template=True
    )
    # templates の数と prompt の BREAK(改行) の数が一致するかどうか
    if not (prompt1+"\n"+prompt2).count("\n") == templates.count("\n"):
      print("WARN: didn't matched prompt's BREAK count and template count")
      print("Skipped..")
      pass
    else:
      # プロンプトの分け目の BREAK を検出する
      if len(templates) == 1:
        prompt = prompt1 + r(templates.strip("\n")) + "\n" + prompt2
      else: # len(templates) >= 2:
        p1 = len(prompt1.split("\n"))
        p2 = len()
  return prompt1+"\n"+prompt2, negative, ad_prompt, ad_negative, "OK."