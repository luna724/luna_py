import gradio as gr
import os
import LGS.misc.jsonconfig as jsoncfg

from modules.shared import ROOT_DIR, language
from webui import UiTabs, some_tiny_tweaks

class Randkeyword(UiTabs):
  l = language("/ui/stt_child/randkeyword.py", "raw")
  
  def variable(self):
    return [Randkeyword.l["tab_title"]]
  
  def index(self):
    return len(self.variable())
  
  def ui(self, outlet):
    l = Randkeyword.l
    
    with gr.Blocks():
      with gr.Row():
        target = gr.Textbox(label=l["target_prompt"], lines=4)
        output = gr.Textbox(label=l["output_prompt"], lines=4)
      
      with gr.Row():
        copy = gr.Checkbox(label=l["auto_copy"])
        keep_sorting = gr.Textbox(label=l["keep_sorting"], placeholder="e.g. 1,2,3 == don't sort index 1, 2, 3", value="")
        
      infer = gr.Button(l["infer"])
      infer.click(
        some_tiny_tweaks.randkeyword,
        [target, copy, keep_sorting], output
      )