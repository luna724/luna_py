BASIC_raw = { # . = Use Database Default Value
  "key": {
    "Method": "v3",
    "Method_Release": 2,
    "Key": "$KEY",
    "Values": {
      "Prompt": "1girl",
      "Negative": ".",
      "AD_Prompt": ".",
      "AD_Negative": "."
    },
    "ControlNet": {
      "isEnabled": False,
      "Mode": "OpenPose",
      "Weight": "0.75",
      "Image": "/path/to/image"
    },
    "Hires": {
      "isEnabled": False,
      "Upscale": -1,
      "Sampler": "None",
      "Denoising": -1,
      "Steps": -1
    },
    "Example": {
      "isEnabled": False,
      "Character": "None",
      "Lora": "None",
      "Name": "None",
      "Prompt": "None",
      "isExtend": True,
      "Face": "None",
      "Location": "None",
      "Header": "None",
      "Lower": "None",
      "Image": "/path/to/image",
      "isEnableCSN": False,
      "CustomNegative": ""
    },
    "Regional_Prompter": {
    "isEnabled": False,
    "rp_mode": "Matrix",
    "Secondary_Prompt": {
      "prompt": "",
      "characters": "",
      "weight": 1.0,
      "lora": "",
      "name": "",
      "ch_prompt": "",
      "face": "",
      "location": "",
      "header": "",
      "lower": "",
      "gFaL_from_Main": False
    },
    "mode": "Attention",
    "base": False,
    "common": [False, False],
    "lora_stop_step": [0, 0],
    "resolution": [0, 0],
    "split_mode": "Rows",
    "split_ratio": "1:1",
    "base_ratio": 0.2
    },
    "Resolution": "None",
    "Sampler": "None",
    "Clip": 2,
    "displayName": "Example dict",
    "DatabasePath": "/path/to/this_database"
  } 
}


BASIC = BASIC_raw["key"]

import LGS.misc.jsonconfig as jsoncfg
from modules import regional_prompter as rp
from modules.delete_prompt_template import delete_selected
from modules.versions.prompt import template_style
from modules.lib import error_handling_helper
from modules.shared import ROOT_DIR, currently_version, currently_template_versionID, language
import modules.shared as shared
from PIL import Image
from typing import Literal
from re import Pattern
import gradio as gr
from LGS.misc.nomore_oserror import filename_resizer
import os

def get_index_list(target_list: list = [["index0", "index1"], ["hello", ", ", "world!"]], index: int =0, ignore_error: bool = True):
  rtl = []
  for x in target_list:
    try:
      value = x[index]
      rtl.append(value)
    except IndexError as e:
      if ignore_error:
        print(f"IndexError: {e}\nin get_index_list function.\nskipping..")
        pass
      else:
        print(f"IndexError: {e}\nin get_index_list function.")
        raise ValueError("ignore_error == False")
  
  return rtl

def check(text):
  if text == None or text == "" or str(text).strip() == "" or text == None:
    return "None"
  else:
    return text
  
def enablecheck(dicts: dict):
  for key, value in dicts.items():
    if key == "isEnabled" or key == "Image":
      continue
    if key == "None" or key == None:
      return

def range_checker(value: int | float, accept_range=[(1.0, 4.0)], resize_if_over: bool = True):
  #ranges = [(1, 5), (10, 15), (20, 25)]
  value = float(value)
  if any(start <= value <= end for start, end in accept_range):
    return value
  else:
    if resize_if_over:
      min_list = get_index_list(accept_range)
      minimum = min(min_list)
      max_list = get_index_list(accept_range, 1)
      maximum = max(max_list)

      if value < minimum:
        return minimum
      elif maximum < value:
        return maximum
      else:
        return "None"
    else:
      return "None"

def vcheck(target, accept_range):
  if not check(target) == "None":
    return range_checker(target, accept_range)
  else:
    return "None"

def save(
  displayName: str, #Template Display Name
  prompt: str, # Basic Prompt
  negative: str, # Basic Negative (Optional)
  ad_prompt: str, # ADetailer Prompt (Optional)
  ad_negative: str, #ADetailer Negative (Optional)
  cn_enabled: str, # (optional)
  cn_mode: str, # CN Mode (Optional)
  cn_weight: float, # CN Weight (Optional)
  cn_image, # PIL Image  ControlNet Unit Image (Optional)
  hires_enabled: bool, # Hires.fix Option is Enabled? (Optional)
  h_upscl: float, # Hires.fix Upscale (Optional) (1.0 ~ 4.0)
  h_sampler: str, # Hires.fix Sampler (Optional)
  h_denoise: float, # Hires.fix Denoising Strength (Optional) (0 ~ 1)
  h_steps: int, # Hires.fix Steps (Optional) (0 ~ 150)
  resolution: str, # Resolution (Optional)
  sampler: str, # Sampler (Optional)
  ex_enabled: bool, # Example Option is enabled? (Optional)
  ex_character_name: str, # Example Character Name (Optional)
  ex_lora: str, # Example Lora (Optional)
  ex_lora_weight: float, # Example Lora's Weight
  ex_name: str, # Example Name (Optional)
  ex_prompt: str, # Example Prompt (Optional)
  ex_isExtend: bool, # is it have extend? (Optional)
  ex_face: str, # Example Face (Optional)
  ex_location: str, # Example Location (Optional)
  ex_header: str, # Example Header (Optional) 
  ex_lower: str, # Example Lower (Optional)
  ex_image, # PIL Image  Exampel Image path (Optional)
  custom_negative: str, # CustomNegative (Optional)
  clip_skip: str, # Clip skip (Optional)
  overwrite: bool, # Overwrite
  rp_enabled: bool, # Regional Prompter option is enabled?
  rp_mode: Literal["Attention", "Latent"], # Generation Mode
  rp_use_base: bool, # use base prompt
  rp_use_common: bool, # use common prompt
  rp_use_common_negative: bool, # use common negative prompt
  rp_base_ratio: float, # base ratio
  rp_lora_stop: int, # lora stop step
  rp_lora_hires: int, # lora hires stop step
  rp_split_mode: Literal["Rows", "Columns", "Random"], 
  rp_split_ratio: str, # division ratio
  rp_width: int, # width
  rp_height: int, # height
  rp_second_prompt: str, # secondary prompt
  rp_ex_c: str, # secondary prompt's example - character template
  rp_ex_l: str, # lora
  rp_ex_lw: float, # lora weight
  rp_ex_n: str, # name
  rp_ex_h: str, #header
  rp_ex_ep: str, # character prompt
  rp_ex_f: str, # face
  rp_ex_lc: str, # locatoin
  rp_ex_lo: str, #lower
  rp_ex_gFaL: bool, # get face and location from main
  share_load_target: str, # Sharing jsonfile path optional
  share_delete_loaded: bool, # delete jsonfile after successfully loaded
):
  """
  DISCONTINUED FUNCTION
  
  alternate function -> .new_save()
  """
  # debug
  for x, y in locals().items():
    print(f"[dev]: [{x}] = {y}")
  
  rp_dict = {
    "isEnabled": rp_enabled,
    "rp_mode": "Matrix",
    "Secondary_Prompt": {
      "prompt": rp_second_prompt,
      "characters": rp_ex_c,
      "weight": rp_ex_lw,
      "lora": rp_ex_l,
      "name": rp_ex_n,
      "ch_prompt": rp_ex_ep,
      "face": rp_ex_f,
      "location": rp_ex_lc,
      "header": rp_ex_h,
      "lower": rp_ex_lo,
      "gFaL_from_Main": rp_ex_gFaL
    },
    "mode": rp_mode,
    "base": rp_use_base,
    "common": [rp_use_common, rp_use_common_negative],
    "lora_stop_step": [rp_lora_stop, rp_lora_hires],
    "resolution": [rp_width, rp_height],
    "split_mode": rp_split_mode,
    "split_ratio": rp_split_ratio,
    "base_ratio": rp_base_ratio
  }
  
  

  cn_ImagePath = "/path/to/image"
  if cn_image:
    cn_ImagePath = os.path.join(
      ROOT_DIR, "database", "v3", "image", f"{filename_resizer(displayName, replaceTo='_')}.png"
    )
    if os.path.exists(cn_ImagePath):
      print(f"WARN: Image is already exists. ({cn_ImagePath})\nBackup and replace..")
      if os.path.exists(cn_ImagePath + ".old.png"):
        os.remove(cn_ImagePath + ".old.png")
      os.rename(cn_ImagePath, f"{cn_ImagePath}.old.png")
    cn_image.save(
      cn_ImagePath, "PNG")
  else:
    cn_ImagePath = shared.noneimg
    
  controlnet = {
    "isEnabled": cn_enabled,
    "Mode": check(cn_mode),
    "Weight": check(cn_weight),
    "Image": check(cn_ImagePath)
  }
    

  hires_fix = {
    "isEnabled": hires_enabled,
    "Upscale": float(vcheck(h_upscl, [(1.0, 4.0)])),
    "Sampler": check(h_sampler),
    "Denoising": float(vcheck(h_denoise, [(0, 1)])),
    "Steps": int(vcheck(h_steps, [(1, 150)]))
  }
  csn = custom_negative
  
  ex_ImagePath = "/path/to/image"
  # import numpy as np
  # def is_valid_image(image):
  #   if not isinstance(image, np.ndarray):
  #       return False  # NumPy 配列でない場合は保存不可とみなす
  #   if image.ndim != 3:
  #       return False  # 3次元でない場合は保存不可とみなす
  #   if image.shape[2] not in (1, 3):
  #       return False  # チャンネル数が1または3でない場合は保存不可とみなす
  #   if not np.issubdtype(image.dtype, np.integer):
  #       return False  # データ型が整数型でない場合は保存不可とみなす
  #   return True
  
  # if is_valid_image(ex_image):
  if ex_image:
    ex_ImagePath = os.path.join(
      ROOT_DIR, "database", "v3", "image", f"{filename_resizer(displayName, replaceTo='_')}.png"
    )
    if os.path.exists(ex_ImagePath):
      print(f"[Save]: WARN: Image is already exists. ({ex_ImagePath})\nBackup and replace..")
      os.rename(ex_ImagePath, f"{ex_ImagePath}.old.png")
    ex_image.save(
      ex_ImagePath, "PNG")
  else:
    ex_ImagePath = shared.noneimg
  
  example = {
    "isEnabled": ex_enabled,
    "Character": check(ex_character_name),
    "Weight": float(ex_lora_weight),
    "Lora": check(ex_lora),
    "Name": check(ex_name),
    "Prompt": check(ex_prompt),
    "isExtend": ex_isExtend,
    "Face": check(ex_face),
    "Location": check(ex_location),
    "Header": check(ex_header),
    "Lower": check(ex_lower),
    "Image": ex_ImagePath,
    "CustomNegative": csn
  }
  
  if negative.strip() == "":
    negative = shared.negative
  if ad_prompt.strip() == "":# or ".":
    ad_prompt = shared.ad_pos
  if ad_negative.strip() == "":# or ".":
    ad_negative = shared.ad_neg
  
  template_data = {
    "Method": currently_version,
    "Method_Release": currently_template_versionID,
    "Key": displayName,
    "Values": {
      "Prompt": prompt,
      "Negative": negative,
      "AD_Prompt": ad_prompt,
      "AD_Negative": ad_negative
      },
    "ControlNet": controlnet,
    "Hires": hires_fix,
    "Example": example,
    "Regional_Prompter": rp_dict,
    "Resolution": check(resolution),
    "Sampler": check(sampler),
    "Clip": vcheck(clip_skip, [(1, 12)]),
    "displayName": displayName,
    "DatabasePath": BASIC["DatabasePath"]
  }
  
  prv_data: dict = jsoncfg.read(
    os.path.join(ROOT_DIR, "database", "v3" ,"template_list.json")
  )
  
  if not overwrite and displayName in prv_data.keys():
    return "Error: this name is already taken."
  elif displayName in prv_data.keys():
    print(f"[Save]: WARN: previous {displayName}'s Key data is deleted.")
    _, _ = delete_selected(displayName, True)
  prv_data[displayName] = template_data
  
  jsoncfg.write(
    prv_data,
    os.path.join(ROOT_DIR, "database", "v3" ,"template_list.json")
  )
  
  return "Success!"


def load(target, already_dname=None):
  from modules.generate import get_template
  lang = language("/modules/make_prompt_template.py", "raw")
  if already_dname != "":
    raise gr.Error(lang["name_exists"])
  
  d = get_template("full")[target]
  # 朱徳取得取得
  # v3.0.3+
  if d["Method_Release"] >= 3:
    display_name = d["Key"]
    prompt = d["Values"]["Prompt"]
    negative = d["Values"]["Negative"]
    adetailer_prompt = d["Values"]["AD_Prompt"]
    adetailer_negative = d["Values"]["AD_Negative"]
    activate_controlnet = d["ControlNet"]["isEnabled"]
    cn_mode = d["ControlNet"]["Mode"]
    cn_weight = d["ControlNet"]["Weight"]
    cn_image = d["ControlNet"]["Image"]
    activate_hires = d["Hires"]["isEnabled"]
    upscaled = d["Hires"]["Upscale"]
    upscaler = d["Hires"]["Sampler"]
    denoise = d["Hires"]["Denoising"]
    hires_step = d["Hires"]["Steps"]
    resolution = d["Resolution"]
    sampler = d["Sampler"]
    activate_example = d["Example"]["isEnabled"]
    characters = d["Example"]["Character"]
    lora = d["Example"]["Lora"]
    lora_weight = d["Example"]["Weight"]
    name = d["Example"]["Name"]
    character_prompt = d["Example"]["Prompt"]
    hasextend = d["Example"]["isExtend"]
    face = d["Example"]["Face"]
    location = d["Example"]["Location"]
    header = d["Example"]["Header"]
    lower = d["Example"]["Lower"]
    image = d["Example"]["Image"]
    clip = d["Clip"]
    overwrite = True
    activate_rp = d["Regional_Prompter"]["isEnabled"]
    rp = d["Regional_Prompter"]
    rp_mode = rp["rp_mode"]
    use_base = rp["base"]
    use_common = rp["common"][0]
    use_ncommon = rp["common"][1]
    base_ratio = rp["base_ratio"]
    lora_stop = rp["lora_stop_step"][0]
    lora_hires = rp["lora_stop_step"][1]
    split_mode = rp["split_mode"]
    split_text = rp["split_ratio"]
    rp_width = rp["resolution"][0]
    rp_height = rp["resolution"][1]
    sp = rp["Secondary_Prompt"]
    second_prompt = sp["prompt"]
    sec_characters = sp["characters"]
    sec_lora = sp["lora"]
    sec_weight = sp["weight"]
    sec_name = sp["name"]
    sec_head = sp["header"]
    sec_prompt = sp["ch_prompt"]
    sec_face = sp["face"]
    sec_location = sp["location"]
    sec_lower = sp["lower"]
    sync_with_main = sp["gFaL_from_Main"]
    memo = ""
      
    # v3.0.3 ~ v3.0.4 ONLY
    if 4 >= d["Method_Release"] >= 3:
      memo = d["Example"]["CustomNegative"]
    # v3.0.5+
    if d["Method_Release"] >= 5:
      memo = d["Example"]["Memo"]
    
    status = "Done."
    return status, display_name, prompt, negative, adetailer_prompt,\
                      adetailer_negative, activate_controlnet,\
                      cn_mode, cn_weight, cn_image, activate_hires,\
                      upscaled, upscaler, denoise, hires_step, resolution,\
                      sampler, activate_example, characters, lora, lora_weight,\
                      name, character_prompt, hasextend,\
                      face, location, header, lower, image, memo,\
                      clip, overwrite, activate_rp, rp_mode, use_base,\
                      use_common, use_ncommon, base_ratio, lora_stop,\
                      lora_hires, split_mode, split_text, rp_width,\
                      rp_height, second_prompt, sec_characters,\
                      sec_lora, sec_weight, sec_name, sec_head,\
                      sec_prompt, sec_face, sec_location, sec_lower,\
                      sync_with_main
  else:
    raise gr.Error(lang["too_low"])


def new_save(
  Key, Values0Prompt, Values0Negative, Values0AD_Prompt, Values0AD_Negative, 
  ControlNet0isEnabled, ControlNet0Mode, ControlNet0Weight, 
  ControlNet0Image, Hires0isEnabled, Hires0Upscale, Hires0Sampler, 
  Hires0Denoising, Hires0Steps, Resolution, Sampler, 
  Example0isEnabled, Example0Character, Example0Lora, 
  Example0Weight, Example0Name, Example0Prompt, Example0isExtend,
  Example0Face, Example0Location, Example0Header, Example0Lower, 
  Example0Image, Example0Memo, Clip, overwrite, Regional_Prompter0isEnabled, 
  RP0rp_mode, RP0mode, RP0common, RP0ncommon, RP0base_ratio, 
  RP0lora_stop_step, RP0lora_hires_stop, RP0split_mode, RP0split_ratio,
  RP0resolution, PASS0resh, RP0SP0prompt, RP0SP0characters, 
  RP0SP0lora, RP0SP0weight, RP0SP0name, RP0SP0header, RP0SP0ch_prompt,
  RP0SP0face, RP0SP0location, RP0SP0lower, RP0SP0sync, PASS0db_load, 
  PASS0delete_after_load, CODE0enable_load,
  PASS0ver_info="v3.0.6"
):
  def instance_check(base, instance) -> bool:
    return isinstance(base, instance)      
  
  # バージョンに応じて初期辞書を取得
  base_data = template_style.get_dict(PASS0ver_info)()
  saves = base_data
  
  # 調整
  RP0resolution = [
    RP0resolution, PASS0resh
  ]
  
  # 値
  data_root_key_list = [
    k for k in base_data.keys()
  ] + ["RP"]
  spec_word = ["RP", "SP"]
  spec2real = {
    "RP": "Regional_Prompter",
    "SP": "Secondary_Prompt"
  }
  continue_words = ["PASS", "CODE"]
  
  # 動的に設定
  for k, v in locals().items():
    # 0 がついている場合ネストとみなす
    if k.count("0") >= 1:
      # ネスト元が存在するなら
      if k.split("0")[0] in data_root_key_list:
        # 存在する場合そこにネストするキーを取得
        kv0 = k.split("0")[0]
        if kv0 in spec_word:
          # 短縮後場合、再変換
          kv0 = spec2real[kv0]
        
        kv2 = k.split("0")[1]
        kls = [k for k in base_data[kv0].keys()]
        
        # さらにネスト？
        if kv2.split("0") >= 1:
          kv3 = kv2.split("0")[0]
          if kv3 in kls:
            # 同じ動作
            if kv3 in spec_word:
              kv3 = spec2real[kv3]
            
            kv4 = kv2.split("0")[1]
            kls = [k for k in base_data[kv0][kv3].keys()]
            # 置き換え
            saves[kv0][kv3][kv4] = v
            
        # しない場合
        else:
          saves[kv0][kv2] = v
      else:
        # 存在しない場合
        # エラーハンドリング
        if not k.split("0")[0] in continue_words:
          raise ValueError(f"Exception. \nvariables save at {error_handling_helper(locals(), __name__)}")
        else:
          kv = k.split("0")[0]
          if kv == "PASS":
            continue
          elif kv == "CODE":
            if k == "CODE0enable_load":
              if v:
                # enable_load とその他のものを使用して処理を行う
                h = "a"
              else:
                continue