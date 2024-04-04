import gradio as gr
import os
import LGS.misc.jsonconfig as jsoncfg

from modules.shared import ROOT_DIR, language
from webui import UiTabs, some_tiny_tweaks

class Keyword_updater(UiTabs):
  l = language("/ui/stt_child/keyword_updater.py", "raw")
  
  def variable(self):
    return [Keyword_updater.l["tab_title"]]
  
  def index(self):
    return len(self.variable())
  
  def ui(self, outlet):
    l = Keyword_updater.l
    
    with gr.Blocks():
      with gr.Row():
        target = gr.Textbox(label=l["target_prompt"], lines=4)
        output = gr.Textbox(label=l["output_prompt"], lines=4)
      
      with gr.Row():
        auto_copy = gr.Checkbox(label=l["auto_copy"])
      
      infer = gr.Button(l["infer"])
      infer.click(
        some_tiny_tweaks.keyword_updater, inputs=[target, auto_copy], outputs=[output]
      )