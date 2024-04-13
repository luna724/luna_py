import gradio as gr
import os
import LGS.misc.jsonconfig as jsoncfg

from modules.shared import ROOT_DIR, language
from webui import UiTabs, some_tiny_tweaks, get_template

class TabData(UiTabs):
  l = language("/ui/stt_child/randprompt.py", "raw")
  
  def variable(self):
    return [TabData.l["tab_title"]]
  
  def index(self):
    return len(self.variable())
  
  def ui(self, outlet):
    l = TabData.l
    
    with gr.Blocks():
      output = gr.Textbox(label=l["output_prompt"], interactive=False,
                          show_copy_button=True, lines=4)
      
      with gr.Accordion(l["blacklist_root"], open=False, _js=None):
        blacklist = gr.Dropdown(
          choices=get_template("manual"), multiselect=True
        )
      
      with gr.Row():
        ranges = gr.Slider(1, 200, value=24, step=1, label=l["range"])
        with gr.Row():
          weights = gr.Slider(-1, 2, value=1.0, step=0.01, label=l["weight_range"])
          weight_max = gr.Slider(-1, 2, value=1.0, step=0.01, label=l["weight_range_max"])
      
      with gr.Row():
        copy = gr.Checkbox(label=l["auto_copy"], valueF=False)
        dupe = gr.Checkbox(label=l["dupe"], value=True)
      
      generate = gr.Button(l["infer"], variant="primary")
      generate.click(
        some_tiny_tweaks.randprompt,
        [copy, blacklist, ranges, weights, weight_max, dupe], output
      )