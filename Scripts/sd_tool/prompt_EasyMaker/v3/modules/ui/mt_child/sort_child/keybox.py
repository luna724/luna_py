import gradio as gr
import os
from typing import List
import LGS.misc.jsonconfig as jsoncfg

from modules.shared import ROOT_DIR, language
from webui import manage_keybox, start_sorting
from webui import UiTabs

class Keybox(UiTabs):
  l = language("/ui/mt_child/sort.py", "raw")["children"]
  
  def __init__(self, path):
    super().__init__(path)
  
  def index(self):
    return 3
  
  def variable(self):
    return [Keybox.l[f"title-{str(self.index())}"]]
      
  def ui(self, outlet):
    l = Keybox.l
    
    with gr.Blocks():
      trigger = gr.Textbox(visible=False, value="keybox_template")
      gr.Markdown(l["info"].replace("localhost:7859", "localhost:7857"))
      
      with gr.Row():
        lists = gr.Dropdown(
          label=self.variable()[0]+" Templates",
          choices=manage_keybox.get_keybox("manual"), interactive=True
        )
        refresh1 = gr.Button(l["refresh"])
        refresh1.click(fn=manage_keybox.get_keybox, outputs=lists)
        
      gr.Markdown("<br />")
      start = gr.Button(l["start"], variant="primary")
      
      status = gr.Textbox(label=l["status"],lines=4,max_lines=20,interactive=False)
      
      start.click(
        start_sorting, trigger, [status, start])
      