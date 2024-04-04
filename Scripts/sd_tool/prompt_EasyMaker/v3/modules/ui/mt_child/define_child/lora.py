import gradio as gr
import os
from typing import List
import LGS.misc.jsonconfig as jsoncfg

from modules.shared import ROOT_DIR, language
from webui import js_manager, show_state_from_checkbox, manage_lora_template
from webui import UiTabs, get_lora_list

class Lora(UiTabs):
  l = language("/ui/mt_child/define/lora.py", "raw")
  
  def __init__(self, path):
    super().__init__(path)
  
  def variable(self):
    return [Lora.l["tab_title"]]
  
  def index(self):
    return 2
      
  def ui(self, outlet):
    l = Lora.l

    with gr.Blocks():
      with gr.Group():
        display_name = gr.Textbox(label=l["display_name"], placeholder=l["dn_ph"])
      
      with gr.Row():
        lora_id = gr.Textbox(label=l["lora"])
        name = gr.Textbox(label=l["name"])
      
      with gr.Row():
        prompt = gr.Textbox(label=l["prompt"])
        extend = gr.Textbox(label=l["extend"])
      
      with gr.Row():
        overwrite = gr.Checkbox(label=l["overwrite"])
      
      status = gr.Textbox(label=l["status"])
      save = gr.Button(l["save"])
      
      gr.Markdown("<br />")
      with gr.Group():
        with gr.Accordion(l["load_root"], open=False):
          with gr.Row():
            target = gr.Dropdown(
              choices=get_lora_list("manual"), label=l["target"]
            )
            refresh = gr.Button(l["refresh"])
            refresh.click(get_lora_list, outputs=target)
          
          load = gr.Button(l["load"], variant="primary")
          load.click(
            manage_lora_template.load,
            [target, display_name, lora_id, name, prompt, extend, overwrite],
            [status, display_name, lora_id, name, prompt, extend, overwrite]
          )
          save.click(
            manage_lora_template.save,
            [display_name, lora_id, name, prompt, extend, overwrite],
            status
          )