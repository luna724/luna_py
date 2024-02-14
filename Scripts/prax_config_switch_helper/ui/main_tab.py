import gradio as gr
import os
from tkinter import Tk, filedialog
from LGS.misc.jsonconfig import read

from translation import lang
from pcbs import main_function

def build():
  l = lang["main_tab.py"]
  downloads = os.path.join(os.path.expanduser("~"), "Downloads")
  prax_path = os.path.join(os.path.expanduser("~"), "AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/RoamingState", "Prax/config")
  
  def browse_file():
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    
    filenames = filedialog.askopenfilename(defaultextension="json")
    if len(filenames) > 0:
        root.destroy()
        return str(filenames)
    else:
        filename = "Files not seleceted"
        root.destroy()
        return str(filename)
    return
  
  
  def parse_file_data(cfg_path):
    cfg_path = cfg_path
    print("cfg_path: ", cfg_path)
    
    if not os.path.exists(cfg_path):
      return gr.Dropdown.update(choices=[l[13]],value=l[13])
    elif os.path.isdir(cfg_path):
      return gr.Dropdown.update(choices=[l[13]],value=l[13])
    elif not os.path.splitext(os.path.basename(cfg_path))[1] == ".json":
      return gr.Dropdown.update(choices=[l[13]],value=l[13])
    
    cfg = read(cfg_path)
    
    try:
      nameitem = []
      for x in cfg["modules"]:
        nameitem.append(x["name"])
    except KeyError or IndexError:
      return gr.Dropdown.update(choices=[l[15]],value=l[15])
    
    return gr.Dropdown.update(choices=nameitem)
  
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
        convert_targets = gr.Dropdown(choices=[l[14]], value=None, label=l[10], multiselect=True)
        target_cfg_path.change(fn=parse_file_data, inputs=[target_cfg_path], outputs=[convert_targets])
        convert_visuals = gr.Checkbox(label=l[11], value=True)

    status = gr.Textbox(label="Status", interactive=False)
    infer = gr.Button(l[12])
    infer.click(
      fn=main_function,
      inputs=[target_cfg_path, target_db_path, replace_bind, gr.Checkbox(value=False,visible=False), easy_load,
              strict, convert_visuals, convert_targets, convert_bind],
      outputs=[status]
    )
    
    
  
  
  return (l[9], i, 1)