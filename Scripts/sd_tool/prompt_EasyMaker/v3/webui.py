import gradio as gr
import os
import sys

sys.path.append("..\\")
sys.path.append("..\\./py")

from a1111_ui_util import *
from py import template_generator, lib

from modules.generate import get_template
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
          with FormRow():
            lora = gr.
  
  



main_iface.queue(64)
main_iface.launch()