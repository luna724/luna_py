import gradio as gr
import os
from typing import List
import importlib

from modules.shared import ROOT_DIR, language
from webui import js_manager
from webui import UiTabs

from modules.config import visuals

class Visual(UiTabs):
  l = language("/ui/config.py", "raw")["visual"]
  
  # def __init__(self, path):
  #   super().__init__(path)
    
  #   self.child_path = os.path.join(UiTabs.PATH, "mt_child/define_child")
  
  def variable(self):
    return [Visual.l["tab_title"]]
  
  def index(self):
    return 1
      
  def ui(self, outlet):
    l = Visual.l
    
    with gr.Blocks():
      with gr.Row():
        apply_changes = gr.Button(l["apply_changes"], variant="primary", scale=13)
        restart = gr.Button(l["restart"], variant="secondary", scale=8)
        apply_changes.click(
          None)
        restart.click(
          None
        )
      
      ui_theme = gr.Dropdown(choices=visuals.get_themes(), value=visuals.get_themes("current"), label=l["ui_theme"])
      