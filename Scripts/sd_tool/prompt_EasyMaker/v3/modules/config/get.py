from pydantic import BaseModel
from LGS.misc.jsonconfig import read as r_json
import os
from typing import *

from modules.shared import DB_PATH

class Config(BaseModel):
  """include all Config values."""
  # Visuals
  ui_themes: Literal["dark", "light", "aurora midnight"]
  """UI のテーマ"""
  
  # Internal Config
  use_average_weights: bool 
  """prompt resize時に複数の weight が一つのキーワードで発見された場合、
  それらの平均値を使用する"""
  disable_display_name_exist_check:bool
  """ https://github.com/luna724/luna_py/issues/11#issuecomment-2018480322"""
  
  # ControlNet UI Variables
  controlnet_type:list
  controlnet_control_modes:list
  controlnet_models:dict
  controlnet_preprocessors:dict
  controlnet_resize_mode:list
  
  # ADetailer UI Variables
  adetailer_models:list



class Values(BaseModel):
  """include all UI Default values.
  Only Supported latest ui (current: v3.0.6)"""
  low_vram_mode:bool
  cn_type:str
  pixel_perfect:bool
  mask_upload:bool
  cn_img2img:bool
  activate_controlnet:bool

cfg_data:dict = r_json(os.path.join(DB_PATH, "configs.json"))
value_data:dict= cfg_data["ui_default_values"]
cfg = Config(**cfg_data)
vls = Values(**value_data)