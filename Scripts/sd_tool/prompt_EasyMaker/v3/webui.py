import gradio as gr
import os
import sys

sys.path.append("..\\")
sys.path.append("..\\./py")

from a1111_ui_util import *
from py import template_generator, lib

from modules.generate import get_template
from modules.generate_util import get_lora_list
import modules.shared as shared 



with gr.Blocks() as main_iface:
  with gr.Tab("Generate"):
    with FormRow():
      template = gr.Dropdown(label="Target template", choices=get_template("manual"))
      template_refresh = ToolButton("\U0001f504")
      template_refresh.click(
        fn=get_template,
        inputs=[],outputs=[template]
      )
    
    with gr.Blocks():
      with FormRow():
        with FormColumn():
          lora = gr.Dropdown(label="Select Character Template", choices=get_lora_list("manual"))
          
          with FormRow():
            # Example Column (1)
          #   elora = gr.Textbox(label="LoRA ID", placeholder="<lora:ichika3:1.0>")
          #   ename = gr.Textbox(label="Character Name", placeholder="luna")
          # with FormRow():
          #   eprompt = gr.Textbox(label="Character Prompt", placeholder="melody hair, multicolored hair")
          #   eAprompt = gr.Textbox(label="Character Prompt Extender", placeholder="aqua eyes")
          # with FormRow():
          #   elocation = gr.Textbox(label="Draw Location", placeholder="indoor, bookshelf, library")
          #   eface = gr.Textbox(label="Character Face", placeholder="facing at bookshelf, unemotional")
          # with FormRow():
          #   eheader = gr.Textbox(label="Prompt Header", placeholder="(masterpiece, best quality:1.005), 1girl, solo")
          #   elower = gr.Textbox(label="Prompt Lower", placeholder="<lora:detail_tweaker:-0.15>, <lora:masusu_breastsandnipples:0.45>")
          # Moved to -> Template Previewer
          

  



main_iface.queue(64)
main_iface.launch()