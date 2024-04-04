import gradio as gr
import os
from typing import List
import LGS.misc.jsonconfig as jsoncfg

from modules.shared import ROOT_DIR, language
from webui import js_manager, FormColumn, FormRow, show_state_from_checkbox
from webui import UiTabs, browse_file, manage_keybox

class Keybox(UiTabs):
  l = language("/ui/mt_child/define/keybox.py", "raw")
  
  def __init__(self, path):
    super().__init__(path)
  
  def variable(self):
    return [Keybox.l["tab_title"]]
  
  def index(self):
    return 3
      
  def ui(self, outlet):
    l = Keybox.l
    
    with gr.Blocks():
      name = gr.Textbox(label=l["display_name"])

      with gr.Row():
        keyword = gr.Textbox(label=l["keyword"])
        sequence = gr.Radio(label=l["sequence"], choices=["$WORD", "%WORD%"], value="$WORD")
      
      with gr.Group():
        prompt = gr.Textbox(label=l["prompt"],lines=2)
        
        with gr.Row():
          info = gr.Textbox(label=l["info"])
      
      with gr.Row():
        overwrite = gr.Checkbox(label=l["overwrite"])
        hide = gr.Checkbox(label=l["hide"])
        multiseq = gr.Checkbox(label=l["multiseq"])
        multikey = gr.Checkbox(label=l["multikey"])
        
      with gr.Accordion(label=l["multikey_opts"], visible=False) as multiseq_opts:
        multikey.change(show_state_from_checkbox, multiseq, multiseq_opts)
        keys = gr.Textbox(label=l["multikeys"], placeholder=l["multikeys_ph"])
        
      status = gr.Textbox(label=l["status"], interactive=False)
      save = gr.Button(l["run"], variant="primary")
      save.click(
        manage_keybox.save, [
          name, keyword, multikey, keys, sequence, multiseq, prompt, info,
          overwrite, hide
        ], status
      )
      
      gr.Markdown("<br />")
      with gr.Group():
        with gr.Accordion(label=l["loads"], open=False):
          with gr.Blocks():
            with gr.Row():
              loads = gr.Textbox(label=l["load_keyboxes"])
              browse = gr.Button(l["browse"])
              browse.click(browse_file, outputs=loads)
            
            load = gr.Button(l["Load"], variant="primary")
            load.click(
              None
            )
          gr.Markdown("<br />")
          with gr.Blocks():
            with gr.Row():
              target = gr.Dropdown(
                choices=manage_keybox.get_keybox("manual"), label=l["target"]
              )
              refresh = gr.Button(l["refresh"])
              refresh.click(manage_keybox.get_keybox, outputs=target)
            
            load1 = gr.Button(l["load"], variant="primary")
            load1.click(
              manage_keybox.load_from_exists,
              [target, name, keyword, sequence, prompt, info, hide, multiseq, multikey, keys],
              [name, keyword, sequence, prompt, info, hide, multiseq, multikey, keys, status]
            )