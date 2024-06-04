import gradio as gr
import os
from tkinter import Tk, filedialog

from modules.config_manager import config, sys_config
from modules.ui import UiTabs
from modules.config_ui import *

class Config(UiTabs):
  def title(self):
    return "Inference"
  
  def index(self):
    return 0
  
  def ui(self, outlet):
    def browse_dir(v=None) -> str:
      vv = None
      if v is not None:
        if hasattr(config, v):
          vv = getattr(config, v)
        elif hasattr(sys_config, v):
          vv = getattr(sys_config, v)
      
        if vv is not None:
          vv = config.convert_path(vv)
        
      
      root = Tk()
      root.attributes("-topmost", True)
      root.withdraw()
      
      filenames = filedialog.askdirectory(initialdir=vv)
      if len(filenames) > 0:
          root.destroy()
          return str(filenames)
      else:
          filename = "Files not seleceted"
          root.destroy()
          return str(filename)
    
    def get_config(v):
      if hasattr(config, v):
        vv = getattr(config, v)
      elif hasattr(sys_config, v):
        vv = getattr(sys_config, v)
      
      return vv
    
    def get_config_for_path(v):
      return config.convert_path(get_config(v))
    
    with gr.Blocks():
      gr.Markdown("gradio inference - β1.1-r1 - gradio support")
      
      with gr.Tab("Generate"):
        gr.Markdown("Ver. β1.1-r1")
        
        with gr.Column():
          with gr.Row():
            tf_ID= gr.Textbox("target_fp", visible=False)
            target_fp = gr.Textbox(
              label= "オーディオ対象パス", value=os.path.join(os.getcwd(), config.target_fp),
              scale=6
            )
            tf_browse = gr.Button("参照", variant="primary", scale=3)
            tf_browse.click(
              browse_dir, inputs=tf_ID, outputs=target_fp
            )
            tf_reload = gr.Button("♲", scale=1)
            tf_reload.click(
              get_config_for_path, inputs=tf_ID, outputs=target_fp
            )