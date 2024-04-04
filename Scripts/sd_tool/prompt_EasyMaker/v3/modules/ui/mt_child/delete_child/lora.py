import gradio as gr
import os
from typing import List
import LGS.misc.jsonconfig as jsoncfg

from modules.shared import ROOT_DIR, language
from webui import manage_lora_template, get_lora_list
from webui import UiTabs

class Lora(UiTabs):
  l = language("/ui/delete", "raw")
  
  def __init__(self, path):
    super().__init__(path)
  
  def index(self):
    return 1

  def variable(self):
    return [Lora.l[f"title-{str(self.index())}"]]
      
  def ui(self, outlet):
    l = Lora.l
    
    with gr.Blocks():
      with gr.Row():
        template = gr.Dropdown(
          multiselect=True,
          label=l["target_template"],
          choices=get_lora_list("manual")
          )
        refresh = gr.Button(l["refresh"])
        refresh.click(
          get_lora_list, outputs=template
        )
      
      with gr.Row():
        permanent = gr.Checkbox(label=l["permanent"], value=False)
      
      status = gr.Textbox(label=l["status"], interactive=False)
      btn = gr.Button(l["run"], variant="primary")
      btn.click(
      manage_lora_template.multi_delete,
      [template, permanent], [status, template]
      )