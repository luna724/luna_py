import gradio as gr
import LGS.misc.jsonconfig as jsoncfg
import os

from modules.shared import ROOT_DIR, language
from webui import UiTabs, js_manager

class Config(UiTabs):
  l = language("/ui/config.py", "raw")
  
  def __init__(self, path):
    super().__init__(path)
    
    self.child_path = os.path.join(UiTabs.PATH, "config_opts")
  
  def variable(self):
    return [Config.l["tab_title"]]
  
  def index(self):
    return 9999
  
  def ui(self, outlet):
    with gr.Blocks():
      js_manager(__name__)
      
      with gr.Tabs():
        tabs = self.get_ui()
        for tab in tabs:
          with gr.Tab(tab.variable()[0]):
            tab()
    
    