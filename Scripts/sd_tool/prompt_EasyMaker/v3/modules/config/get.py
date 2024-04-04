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
  
  # ControlNet UI Variables
  controlnet_main_processor:list
  controlnet_control_modes:list
  controlnet_models:dict
  controlnet_preprocessors:dict

cfg_data:dict = r_json(os.path.join(DB_PATH, "configs.json"))
cfg = Config(**cfg_data)