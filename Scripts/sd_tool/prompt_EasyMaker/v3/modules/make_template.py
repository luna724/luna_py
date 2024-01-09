BASIC_raw = { # . = Use Database Default Value
  "key": {
    "Method": "v3",
    "Key": "$KEY",
    "Values": {
      "Prompt": "1girl",
      "Negative": ".",
      "AD_Prompt": ".",
      "AD_Negative": "."
    },
    "ControlNet": {
      "Mode": "OpenPose",
      "Weight": "0.75",
      "Image": "/path/to/image"
    },
    "Hires": {
      "Upscale": -1,
      "Sampler": "None",
      "Denoising": -1,
      "Steps": -1
    },
    "Example": {
      "Lora": "None",
      "Name": "None",
      "Prompt": "None",
      "isExtend": True,
      "Face": "None",
      "Location": "None",
      "Header": "None",
      "Lower": "None",
      "Image": "/path/to/image",
      "CustomNegative": ""
    },
    "Resolution": "None",
    "Sampler": "None",
    "Clip": 2,
    "displayName": "Example dict",
    "DatabasePath": "/path/to/this_database"
  } 
}


BASIC = BASIC_raw["key"]

from py.lib import jsoncfg
from modules.shared import ROOT_DIR, currently_version
import modules.shared as shared
from PIL import Image
from typing import Iterable
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
  if text == None or text == "" or str(text).strip() == "":
    return "None"
  else:
    return text

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
  ex_name: str, # Example Name (Optional)
  ex_prompt: str, # Example Prompt (Optional)
  ex_isExtend: bool, # is it have extend? (Optional)
  ex_face: str, # Example Face (Optional)
  ex_location: str, # Example Location (Optional)
  ex_header: str, # Example Header (Optional) 
  ex_lower: str, # Example Lower (Optional)
  ex_image, # PIL Image  Exampel Image path (Optional)
  ex_useCustomNegative: bool, # use Custom Negative (Optional)
  custom_negative: str, # CustomNegative (Optional)
  clip_skip: str, # Clip skip (Optional)
  database_path: str, # DISCONTINUED
  overwrite: bool # Overwrite
):
  if cn_enabled:
    cn_ImagePath = "/path/to/image"
    if cn_image:
      cn_ImagePath = os.path.join(
        ROOT_DIR, "database", "v3", "image", f"{filename_resizer(displayName, replaceTo='_')}.png"
      )
      if os.path.exists(cn_ImagePath):
        print(f"WARN: Image is already exists. ({cn_ImagePath})\nBackup and replace..")
        os.rename(cn_ImagePath, f"{cn_ImagePath}.old.png")
      cn_image.save(
        cn_ImagePath, "PNG")
    
    controlnet = {
      "Mode": check(cn_mode),
      "Weight": check(cn_weight),
      "Image": check(cn_ImagePath)
    }
    
  else:
    controlnet = {
      "Mode": check(None),
      "Weight": check(None),
      "Image": check(None)
    }
  
  if hires_enabled:
    hires_fix = {
      "Upscale": float(vcheck(h_upscl, [(1.0, 4.0)])),
      "Sampler": check(h_sampler),
      "Denoising": float(vcheck(h_denoise, [(0, 1)])),
      "Steps": int(vcheck(h_steps, [(1, 150)]))
    }
  else:
    hires_fix = BASIC["Hires"]
  
  if ex_enabled:
    if ex_useCustomNegative:
      csn = custom_negative
    else:
      csn = ""
    
    ex_ImagePath = "/path/to/image"
    if ex_image:
      ex_ImagePath = os.path.join(
        ROOT_DIR, "database", "v3", "image", f"{filename_resizer(displayName, replaceTo='_')}.png"
      )
      if os.path.exists(ex_ImagePath):
        print(f"WARN: Image is already exists. ({ex_ImagePath})\nBackup and replace..")
        os.rename(ex_ImagePath, f"{ex_ImagePath}.old.png")
      ex_image.save(
        ex_ImagePath, "PNG")
    
    example = {
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
    
  else:
    example = BASIC["Example"]
  
  if negative.strip() == "" or ".":
    negative = shared.negative
  if ad_prompt.strip() == "" or ".":
    ad_prompt = shared.ad_pos
  if ad_negative.strip() == "" or ".":
    ad_negative = shared.ad_neg
  
  template_data = {
    "Method": currently_version,
    "Key": displayName.strip().lower().replace(" ", "_"),
    "Values": {
      "Prompt": prompt,
      "Negative": negative,
      "AD_Prompt": ad_prompt,
      "AD_Negative": ad_negative
      },
    "ControlNet": controlnet,
    "Hires": hires_fix,
    "Example": example,
    "Resolution": check(resolution),
    "Sampler": check(sampler),
    "Clip": vcheck(clip_skip, [(1, 12)]),
    "displayName": displayName,
    "DatabasePath": BASIC["DatabasePath"]
  }
  
  tmp = {
    displayName.strip().lower().replace(" ", "_"): template_data
  }
  
  prv_data: dict = jsoncfg.read(
    os.path.join(ROOT_DIR, "database", "v3" ,"template_list.json")
  )
  
  if not overwrite and displayName.strip().lower().replace(" ", "_") in prv_data.keys():
    return "Error: this name is already taken."
  elif displayName.strip().lower().replace(" ", "_") in prv_data.keys():
    print(f"WARN: previous {displayName.strip().lower().replace(' ', '_')}'s Key data is deleted.")
  prv_data[displayName.strip().lower().replace(" ", "_")] = template_data
  
  jsoncfg.write(
    prv_data,
    os.path.join(ROOT_DIR, "database", "v3" ,"template_list.json")
  )
  
  return "Success!"