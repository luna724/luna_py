import gradio as gr
import os
from typing import List
import importlib

from modules.shared import ROOT_DIR, language
from webui import js_manager
from webui import UiTabs

class Define(UiTabs):
  l = language("/ui/mt_child/define.py", "raw")
  
  def __init__(self, path):
    super().__init__(path)
    
    self.child_path = os.path.join(UiTabs.PATH, "mt_child/define_child")
  
  def variable(self):
    return [Define.l["tab_title"]]
  
  def index(self):
    return 1
      
  def ui(self, outlet):
    with gr.Blocks():
      js_manager(__name__)
      with gr.Tabs():
        with gr.Tabs():
          tabs = self.get_ui()
          for tab in tabs:
            with gr.Tab(tab.variable()[0]):
              tab()