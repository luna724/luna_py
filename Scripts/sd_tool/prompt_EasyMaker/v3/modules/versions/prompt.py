from typing import *
class template_style:
  """Static class.
  Do not Initialize!!! """
  def __init__(self, **kwargs):
    raise ValueError("this Class is not Callable.")
  def __call__(self, **kwargs):
    self.__init__()
  
  @staticmethod
  def get_dict(ver_info:str) -> Callable:
    key_from_VI = {
      "v3.0.6": template_style.v306,
      "v3.0.7": None
    }
    return key_from_VI[ver_info]
  
  @staticmethod
  def v306() -> dict:
    return {
      "Method": "v3.0.6",
      "Method_Release": 6,
      "Key": "dict's Key",
      "Values": {
        "Prompt": "Prompt",
        "Negative": "Negative Prompt",
        "AD_Prompt": "ADetailer Prompt",
        "AD_Negative": "ADetailer Negative Prompt"
      },
      "ControlNet": {
        "isEnabled": False,
        "Mode": "ControlNet Mode",
        "Weight": 0,
        "Image": "image relpath",
        "Control": "Control Mode (e.g. balanced)",
        "preprocessor": "ControlNet Preprocessor",
        "Model": "ControlNet Models",
        "img2img": False
      },
      "Hires": {
        "isEnabled": False,
        "Upscale": -1,
        "Sampler": "Hires Sampler",
        "Denoising": -1,
        "Steps": -1
      },
      "Example": {
        "isEnabled": False,
        "Character": "Character Template Key",
        "Lora": "lora",
        "Weight": -1,
        "Name": "name",
        "Prompt": "ch_prompt",
        "isExtend": False,
        "Face": "face",
        "Location": "location",
        "Header": "header",
        "Lower": "lower",
        "Image": "Image relpath from Shared.DB_PATH",
        "Memo": "Creator's Memo",
        "Cloth": "clothes",
        "Accessory": "accessory",
        "Other": "other",
        "Face2": "face2",
        "Location2": "location2",
        "Cloth2": "clothes2"
      },
      "Regional_Prompter": {
        "isEnabled": False,
        "rp_mode": "Regional prompter mode",
        "Secondary_Prompt": {
          "prompt": "",
          "characters": "",
          "weight": -1,
          "lora": "lora id",
          "name": "ch name",
          "ch_prompt": "ch prompt",
          "face": "face",
          "location": "",
          "header": "",
          "lower": "",
          "sync": False,
          "cloth": "cloth",
          "cloth2": "cloth2",
          "face2": "",
          "location2": "",
          "accessory": "",
          "other": "other variable"
        },
        "mode": "RP matrix control mode",
        "base": False,
        "common": False,
        "ncommon": False,
        "lora_stop_step": 0,
        "lora_hires_stop": 0,
        "resolution": [
          512,
          512
        ],
        "split_mode": "split mode (Columns / Rows / Randoms)",
        "split_ratio": "split ratio (e.g. 1:1)",
        "base_ratio": 0.2
      },
      "Resolution": "512×768",
      "Sampler": "Euler a",
      "CFG": 7,
      "Clip": 2,
      "images": None # for share 
    }