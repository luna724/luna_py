import gradio as gr
import os

from modules.shared import ROOT_DIR, language
from webui import js_manager
from webui import UiTabs

class Generate(UiTabs):
  l = language("/ui/generate.py", "raw")
  
  def variable(self):
    return (Generate.l["tab_title"])
  
  def index(self):
    return 2
  
  def has_child(self):
    return [100000001, "generate", "generate."]
  
  def ui(self, outlet):
    with gr.Blocks():
      js_manager(__name__)
      
      