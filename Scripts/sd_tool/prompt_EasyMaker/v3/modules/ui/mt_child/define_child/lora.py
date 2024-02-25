import gradio as gr
import os
from typing import List
import LGS.misc.jsonconfig as jsoncfg

from modules.shared import ROOT_DIR, language
from webui import js_manager, FormColumn, FormRow, show_state_from_checkbox
from webui import UiTabs

class Lora(UiTabs):
  l = language("/ui/mt_child/define/lora.py", "raw")
  
  def __init__(self, path):
    super().__init__(path)
  
  def variable(self):
    return [Lora.l["tab_title"]]
  
  def index(self):
    return 1
      
  def ui(self, outlet):
    l = Lora.l
    
    with gr.Blocks():
      display_name = gr.Textbox(label=l[""])