import gradio as gr
import os
import shutil

import modules

def ui():
  make_ui:gr.Blocks = modules.create_ui.create()
  make_ui.queue(64).launch(
    inbrowser=True
  )
  