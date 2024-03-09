import gradio as gr
import os
import LGS.misc.jsonconfig as jsoncfg

from modules.shared import ROOT_DIR, language
from webui import UiTabs, some_tiny_tweaks

class _2space(UiTabs):
  l = language("/ui/stt_child/_2space.py", "raw")
  
  def variable(self):
    return [_2space.l["tab_title"]]
  
  def index(self):
    return len(self.variable())
  
  def ui(self, outlet):
    l = _2space.l
    
    with gr.Blocks():
      with gr.Row():
        target = gr.Textbox(label=l["target_prompt"], lines=4)
        output = gr.Textbox(label=l["output_prompt"], lines=4)
      
      with gr.Row():
        auto_copy = gr.Checkbox(label=l["auto_copy"])
        reverse = gr.Checkbox(label=l["reverse"])
      
      infer = gr.Button(l["infer"])
      infer.click(
        some_tiny_tweaks._2space, inputs=[target, auto_copy, reverse], outputs=[output]
      )