import gradio as gr
import os
from typing import List
import LGS.misc.jsonconfig as jsoncfg

from modules.shared import ROOT_DIR, language
from webui import manage_keybox
from webui import UiTabs

class Keybox(UiTabs):
  l = language("/ui/delete", "raw")
  
  def __init__(self, path):
    super().__init__(path)
  
  def index(self):
    return 3

  def variable(self):
    return [Keybox.l[f"title-{str(self.index())}"]]
      
  def ui(self, outlet):
    l = Keybox.l
    
    with gr.Blocks():
      with gr.Row():
        template = gr.Dropdown(
          multiselect=True,
          label=l["target_template"],
          choices=manage_keybox.get_keybox("manual")
          )
        refresh = gr.Button(l["refresh"])
        refresh.click(
          manage_keybox.get_keybox, outputs=template
        )
      
      with gr.Row():
        permanent = gr.Checkbox(label=l["permanent"], value=False)
      
      status = gr.Textbox(label=l["status"], interactive=False)
      btn = gr.Button("COMING SOON..", variant="primary")
      btn.click(
      None,
      [template, permanent], [status, template]
      )