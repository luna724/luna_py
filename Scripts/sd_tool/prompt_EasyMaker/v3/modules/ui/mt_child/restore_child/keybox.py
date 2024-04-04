import gradio as gr
import os
from typing import List
import LGS.misc.jsonconfig as jsoncfg

from modules.shared import ROOT_DIR, language
from webui import DropdownMulti
from webui import UiTabs, manage_keybox

class Keybox(UiTabs):
  l = language("/ui/mt_child/restore.py", "raw")["children"]
  
  def __init__(self, path):
    super().__init__(path)
  
  def index(self):
    return 3
  
  def variable(self):
    return [Keybox.l[f"title-{str(self.index())}"]]
      
  def ui(self, outlet):
    l = Keybox.l
    
    with gr.Blocks():
      gr.Markdown("COMING SOON..")
      # with gr.Row():
      #   template = DropdownMulti(
      #     label=l["target"], choices=manage_lora_template.format_backup_filename(gr_update=False)
      #   )
      #   refresh = gr.Button(l["refresh"])
      #   refresh.click(
      #     manage_lora_template.format_backup_filename, outputs=template
      #   )
        
      # with gr.Row():
      #   advanced = gr.Checkbox(label=l["advanced"])
      #   deletion = gr.Checkbox(label=l["deletion"], value=True)
      
      # with gr.Row():
      #   prevent_dupe = gr.Checkbox(label=l["prevent_dupe"], value=True)
      #   only_delete = gr.Checkbox(label=l["only_deletion"])
      
      # with gr.Row():
      #   overwrite = gr.Checkbox(label=l["overwrite"])
      
      # status = gr.Textbox(label=l["status"], interactive=False)
      # btn = gr.Button(l["run"], variant="primary")
      # btn.click(manage_lora_template.multi_restore,
      #           inputs=[template, deletion, overwrite, prevent_dupe,
      #                   only_delete],
      #           outputs=[status, template])
      