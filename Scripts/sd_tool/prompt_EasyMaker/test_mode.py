import gradio as gr
from typing import Literal

from test_script import ce
from lunapy_module_importer import Importer

def main(mode:Literal["ce"]):
  if mode == "ce": #Archived (tests/ce.py)
    iface = ce.get()
  
  elif mode == "g_template":
    
    
    with gr.Blocks() as iface:
      with gr.Row():
        template = gr.Dropdown(label="Template", choices=)
    
  iface.queue(64).launch(server_port=9999)