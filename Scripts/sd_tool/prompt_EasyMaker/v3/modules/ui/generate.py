import gradio as gr
import os
import importlib

from modules.shared import ROOT_DIR, language
from webui import js_manager
from webui import UiTabs

class Generate(UiTabs):
  l = language("/ui/generate.py", "raw")
    
  def variable(self):
    return (Generate.l["tab_title"])
  
  def index(self):
    return 2
  
  # def has_child(self):
  #   return [100000001, "generate", "generate."]
  
  def ui(self, outlet):
    with gr.Blocks():
      js_manager(__name__)
      gr.Textbox(label="hi, world")
  
  def child(self, import_name="modules.ui.generate_child.", subclass=None):
    self.haschild = True
    
    subclass= Generate
    super().child(import_name, subclass)
    root_data = UiTabs("generate")
    
    tabs:list = self.tabs
    
    def outlet():
      with gr.Tabs():
        with gr.Tab(root_data.variable()[0]):
          root_data()
          
          for tab in tabs:
            with gr.Tab(tab.variable()[0]):
              tab()
    
    return self.ui(outlet)
  
  def __call__(self):
    return self.child()