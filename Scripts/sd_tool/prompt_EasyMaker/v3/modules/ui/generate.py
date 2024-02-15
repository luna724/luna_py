import gradio as gr
import os
from typing import List
import importlib

from modules.shared import ROOT_DIR, language
from webui import js_manager
from webui import UiTabs

class Generate(UiTabs):
  l = language("/ui/generate.py", "raw")
  
  def __init__(self, path):
    super().__init__(path)
    
    self.child_path = os.path.join(UiTabs.PATH, "generate_child")
  
  def variable(self):
    return (Generate.l["tab_title"])
  
  def index(self):
    return 2
  
  def get_ui(self) -> List[UiTabs]:
    tabs = []
    files = [file for file in os.listdir(self.child_path) if file.endswith(".py")]

    for file in files:
      module_name = file[:-3]
      module_path = os.path.relpath(
        self.child_path, UiTabs.PATH 
      ).replace("/", ".").strip(".")
      module = importlib.import_module(f"modules.ui.{module_path}.{module_name}")
      
      attrs = module.__dict__
      TabClass = [
        x for x in attrs.values() if type(x) == type and issubclass(x, UiTabs) and not x == UiTabs
      ]
      if len(TabClass) > 0:
        tabs.append((file, TabClass[0]))
      
    tabs = sorted([TabClass(file) for file, TabClass in tabs], key= lambda x: x.index())
    return tabs
      
  def ui(self, outlet):
    with gr.Blocks():
      js_manager(__name__)
      
      with gr.Tabs():
        tabs = self.get_ui()
        for tab in tabs:
          with gr.Tab(tab.variable()[0]):
            tab()
            