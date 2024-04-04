import gradio as gr
import os

from modules.shared import ROOT_DIR, language
from webui import example_view, get_template, get_lora_list, FormRow
from webui import character_exchanger
from webui import UiTabs

class Exchanger(UiTabs):
  l = language("/ui/generate/exchanger.py", "raw")
  
  def variable(self):
    return [Exchanger.l["tab_title"]]
  
  def index(self):
    return 4
  
  def ui(self, outlet):
    l = Exchanger.l
    with gr.Blocks():
      with gr.Row():
        mode = gr.Dropdown(choices=["lora", "name", "prompt"], label=l["mode"], value=["lora", "name", "prompt"], multiselect=True)
      
      with gr.Row():
        template = gr.Dropdown(label=l["to"], choices=get_lora_list("manual"))
        refresh = gr.Button(l["refresh"])
        refresh.click(get_lora_list, outputs=template)
      
      with gr.Row():
        target = gr.Textbox(label=l["target"], lines=4, scale=10)
        outs = gr.Textbox(label=l["output"], interactive=False, show_copy_button=True, lines=4, scale=9)
      
      with gr.Blocks():
        with gr.Row():
          strict_lora = gr.Checkbox(label=l["strict"], value=True)
          auto_copy = gr.Checkbox(label=l["clip"], value=True)
        with gr.Row():
          template_mode = gr.Checkbox(label=l["4template"])
        
      status = gr.Textbox(label=l["status"], interactive=False)
      run = gr.Button(l["run"], variant="primary")
      run.click(
       character_exchanger,
        [mode, target, template, strict_lora, auto_copy, template_mode],
        [outs, status]
      )