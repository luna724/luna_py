import gradio as gr
import os
import LGS.misc.jsonconfig as jsoncfg

from modules.shared import ROOT_DIR, language
from webui import UiTabs, some_tiny_tweaks

class Anti_keyword(UiTabs):
  l = language("/ui/stt_child/anti_keyword.py", "raw")
  
  def variable(self):
    return [Anti_keyword.l["tab_title"]]
  
  def index(self):
    return len(self.variable())
  
  def ui(self, outlet):
    l = Anti_keyword.l
    
    with gr.Blocks():
      text = gr.Textbox(label=l["text"], lines=4, placeholder=l["text_placeholder"])
      targets = gr.Dropdown(label=l["targets"], multiselect=True)
      text.change(
        some_tiny_tweaks.add_targets,
        [text, targets], [text, targets]
      )
      
      with gr.Row():
        target = gr.Textbox(label=l["target_prompt"], lines=4)
        output = gr.Textbox(label=l["output_prompt"], lines=4)
      
      with gr.Row():
        auto_copy = gr.Checkbox(label=l["auto_copy"])
        sensitive = gr.Checkbox(label=l["sensitive_check"])
      
      infer = gr.Button(l["infer"])
      infer.click(
        some_tiny_tweaks.anti_keyword, inputs=[target, targets, auto_copy, sensitive], outputs=[output]
      )