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
from modules.shared import ROOT_DIR, currently_version, currently_template_versionID
import modules.shared as shared
from PIL import Image
from typing import Literal
from re import Pattern
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
  
  if negative.strip() == "" or ".":
    negative = shared.negative
  if ad_prompt.strip() == "" or ".":
    ad_prompt = shared.ad_pos
  if ad_negative.strip() == "" or ".":
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