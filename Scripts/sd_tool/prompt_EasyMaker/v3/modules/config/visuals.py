from modules.config import variable
current_value = variable.get_current()

import gradio as gr
from typing import *

def get_themes(iscurrent=None) -> (str | List[str]):
  if iscurrent is not None:
    return current_value["ui_themes"]
    
  return variable.available_ui_themes

