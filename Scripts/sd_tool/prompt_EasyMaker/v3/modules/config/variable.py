### ALL Selectable Variables.
### for WebUI Config tab's choices

from typing import *
def get_current():
  import LGS.misc.jsonconfig as jc
  import os
  from modules.shared import DB_PATH
  return jc.read(os.path.join(DB_PATH, "configs.json"))

available_internal_ui_themes:List[str] = ["dark", "light"]
available_ui_themes:List[str] = ["aurora midnight"]+available_internal_ui_themes


# WebUI's Dropdown choices
controlnet_main_processor = [
  "OpenPose", "Lineart"
]

