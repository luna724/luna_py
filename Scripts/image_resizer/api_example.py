import gradio as gr
import os
from tkinter import Tk, filedialog
from PIL import Image
import shutil
from typing import Tuple
import sys

class ui_scripts:
  @staticmethod
  def browse_dir() -> str:
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    
    filenames = filedialog.askdirectory()
    if len(filenames) > 0:
        root.destroy()
        return str(filenames)
    else:
        filename = "Files not seleceted"
        root.destroy()
        return str(filename)
  
  @staticmethod
  def change(m) -> tuple:
    def u(v):
      return gr.update(visible=v)
    
    if m == "Color Converter":
      return u(True), u(False)
    else:
      return u(False), u(True)
  
  @staticmethod
  def tunnel(path, mode, *arg):
    outs = []
    for i in os.listdir(path):
      if not os.path.splitext(i)[1].lower() in [".png", ".jpg", ".jpeg"]:
        continue
      
      i = os.path.realpath(os.path.join(path, i))
      image = Image.open(i)
      
      outs.append(
        (i, convert.tunnel(image, mode, *arg))
      )
    
    out_path = os.path.realpath(os.path.join(path, "lunapy_outputs"))
    if os.path.exists(out_path):
      shutil.rmtree(out_path)
    
    os.makedirs(out_path, exist_ok=True)
    
    for i in outs:
      i: Tuple[str, Image.Image]
      out = os.path.join(path, "lunapy_outputs", i[0])
      
      image = i[1]
      image.save(
        out, "PNG"
      )
    
    return "Done."


def create_interface() -> gr.Blocks:
  with gr.Blocks() as i:
    mode = gr.Dropdown(choices=["Color Converter", "Template Converter"], label="mode", value="Color Converter")
    
    with gr.Row():
      path = gr.Textbox(label="target path")
      browse = gr.Button("Browse")
      browse.click(ui_scripts.browse_dir, outputs=path)
    
    with gr.Group(visible=True) as color_converter:
      with gr.Row():
        convert_from = gr.ColorPicker(
          label="Convert from"
        )
        convert_to = gr.ColorPicker(
          label="Convert to"
        )
      
      with gr.Row():
        to_invisible = gr.Checkbox(label="Convert to Invisible (255, 255, 255, 0)", value=True)
      
      out_cc = gr.Textbox(label="Status")

      infer_cc = gr.Button("Run", variant="primary")
      infer_cc.click(
        ui_scripts.tunnel, inputs=[path, mode, convert_from, convert_to, to_invisible], outputs=out_cc
      )  
    
    with gr.Group(visible=False) as template_converter:
      with gr.Row():
        invert = gr.Checkbox(label="Invert")
        rotate = gr.Slider(0, 359, value=0, step=1, label="Rotate")
      with gr.Row():
        monochrome = gr.Checkbox(label="Monochrome")
      
      
      out_tc = gr.Textbox(label="Status")
      
      infer_tc = gr.Button("Run", variant="primary")
      infer_tc.click(
        ui_scripts.tunnel, inputs=[path, mode, invert, rotate, monochrome], outputs=out_tc
      )
    
    mode.change(
      ui_scripts.change, mode, [color_converter, template_converter]
    )
    
  return i

if __name__ == "__main__":
  sys.path.append("..\\")
  import modules.convert as convert
  
  create_interface().queue(64).launch()