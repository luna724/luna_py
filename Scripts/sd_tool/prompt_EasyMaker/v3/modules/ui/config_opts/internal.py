import gradio as gr
import os
from typing import List
import importlib

from modules.shared import ROOT_DIR, language
from webui import js_manager
from webui import UiTabs

from modules.config.get import cfg as config

class Tab(UiTabs):
  l = language("/ui/config.py", "raw")["internal"]
  
  # def __init__(self, path):
  #   super().__init__(path)
    
  #   self.child_path = os.path.join(UiTabs.PATH, "mt_child/define_child")
  
  def variable(self):
    return [Tab.l["tab_title"]]
  
  def index(self):
    return 2
      
  def ui(self, outlet):
    l = Tab.l
    
    with gr.Blocks():
      with gr.Column():
        use_average_weights = gr.Checkbox(label=l["use_average_weights"], value=config.use_average_weights)
        disable_display_name_exist_check = gr.Checkbox(label=l["disable_display_name_exist_check"], value=config.disable_display_name_exist_check)
        