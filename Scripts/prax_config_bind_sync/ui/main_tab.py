import gradio as gr
import os
from tkinter import Tk, filedialog

from translation import lang
from pcbs import main_function

def build():
  l = lang["main_tab.py"]
  downloads = os.path.join(os.path.expanduser("~"), "Downloads")
  prax_path = os.path.join(os.path.expanduser("~"), "AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/RoamingState", "Prax/config")
  
  def get_visuals():
    return [
      ""
    ]
  
  def browse_file():
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    
    filenames = filedialog.askopenfilename()
    if len(filenames) > 0:
        root.destroy()
        return str(filenames)
    else:
        filename = "Files not seleceted"
        root.destroy()
        return str(filename)
    return
  
  def parse_file_data(cfg_path):
    return ["this"]
  
  with gr.Blocks() as i:
    with gr.Column():
      with gr.Blocks():
        with gr.Row():
          target_cfg_path = gr.Textbox(
            label=l[0], value=downloads)
          target_db_path = gr.Textbox(
            label=l[2], value=prax_path
          )
          
        with gr.Row():
          tcp_get = gr.Button(l[1])
          tcp_get.click(
              fn=browse_file,
              inputs=[],outputs=[target_cfg_path]
            )
          tdp_get = gr.Button(l[3])
          tdp_get.click(
            fn=browse_file,
            inputs=[], outputs=[target_db_path]
          )
        
      with gr.Blocks():
        with gr.Row():
          replace_bind = gr.Checkbox(label=l[4], value=True)
          strict = gr.Checkbox(label=l[5], value=False)
        with gr.Row():
          convert_bind = gr.Checkbox(label=l[6], value=True)
          easy_load = gr.Checkbox(label=l[7], value=True)
      
      with gr.Tab(label=l[8]):
        convert_targets = gr.Dropdown(choices=parse_file_data(target_cfg_path), every=2, value=get_visuals(), label=l[10])
        convert_visuals = gr.Checkbox(label=l[11], value=True)

    status = gr.Textbox(label="Status", interactive=False)
    infer = gr.Button(l[12])
    infer.click(
      fn=main_function,
      inputs=[target_cfg_path, target_db_path, replace_bind, gr.Checkbox(value=False), easy_load,
              strict, convert_visuals, convert_targets, convert_bind],
      outputs=[status]
    )
  
  
  return (l[9], i, 1)