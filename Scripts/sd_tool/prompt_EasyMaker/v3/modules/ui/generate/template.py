import gradio as gr
import os

from modules.shared import ROOT_DIR, language
from webui import template_generate, example_view
from webui import UiTabs

class Template(UiTabs):
  l = language("/ui/generate/template.py", "raw")
  
  def variable(self):
    return (Template.l["tab_title"])
  
  def index(self):
    return 2
  
  def child(self):
    return ("generate.template", "generate")
  
  def child_index(self):
    return 1
  
  def ui(self, outlet):
    l = Template.l
    with gr.Blocks():
      with gr.Row():
        template = gr.Dropdown(label=l["template"])