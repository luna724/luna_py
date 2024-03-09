import gradio as gr
import os

from modules.shared import ROOT_DIR, language
from webui import UiTabs, js_manager

class Some_tiny_tweaks(UiTabs):
  l = language("/ui/some_tiny_tweaks.py", "raw")
  
  def __init__(self, path):
    super().__init__(path)
    
    self.child_path = os.path.join(UiTabs.PATH, "stt_child")
  
  def variable(self):
    return [Some_tiny_tweaks.l["tab_title"]]

  def index(self):
    return 5
  
  def ui(self, outlet):
    l = Some_tiny_tweaks.l
    with gr.Blocks():
      js_manager(__name__)
    
      with gr.Tabs():
        tabs = self.get_ui()
        for tab in tabs:
          with gr.Tab(tab.variable()[0]):
            tab()
    