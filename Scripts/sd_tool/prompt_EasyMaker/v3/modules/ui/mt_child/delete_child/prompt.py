import gradio as gr
import os
from typing import List
import LGS.misc.jsonconfig as jsoncfg

from modules.shared import ROOT_DIR, language
from webui import get_template, delete_prompt_template
from webui import UiTabs

class Prompt(UiTabs):
  l = language("/ui/delete", "raw")
  
  def __init__(self, path):
    super().__init__(path)
  
  def index(self):
    return 1

  def variable(self):
    return [Prompt.l[f"title-{str(self.index())}"]]
      
  def ui(self, outlet):
    l = Prompt.l
    
    with gr.Blocks():
      with gr.Row():
        template = gr.Dropdown(
          multiselect=True,
          label=l["target_template"],
          choices=get_template("manual")
          )
        refresh = gr.Button(l["refresh"])
        refresh.click(
          get_template, outputs=template
        )
      
      with gr.Row():
        permanent = gr.Checkbox(label=l["permanent"], value=False)
      
      status = gr.Textbox(label=l["status"], interactive=False)
      btn = gr.Button(l["run"], variant="primary")
      btn.click(
      delete_prompt_template.delete_multi,
      [template, permanent], [status, template]
      )