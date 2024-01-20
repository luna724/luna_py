import gradio as gr
import os

from a1111_ui_util import *
from modules.test.utils import *

with gr.Blocks() as iface:
  with InputAccordion(False, label="Accordion") as acc:
    with acc.extra():
      FormHTML(value="hello", min_width=0)

    gr.Textbox(label="Textbox inside accordion")

  btn = gr.Button("Get accordion value")
  btn.click(fn=lambda: gr.Info(acc.value))