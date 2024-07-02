import gradio as gr
from modules.convert import tunnel

def ui() -> gr.Blocks:
  def change(m) -> tuple:
    def u(v):
      return gr.update(visible=v)
    
    if m == "Color Converter":
      return u(True), u(False)
    else:
      return u(False), u(True)
  
  with gr.Blocks() as i:
    mode = gr.Dropdown(choices=["Color Converter", "Template Converter"], label="mode", value="Color Converter")
    image = gr.Image(label="Target Image", type="pil")
    
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
      
      out_cc = gr.Image(label="Result", image_mode="RGBA", interactive=False, show_download_button=True, type="pil", width=512, height=512)

      infer_cc = gr.Button("Run", variant="primary")
      infer_cc.click(
        tunnel, inputs=[image, mode, convert_from, convert_to, to_invisible], outputs=out_cc
      )  
    
    with gr.Group(visible=False) as template_converter:
      with gr.Row():
        invert = gr.Checkbox(label="Invert")
        rotate = gr.Slider(0, 359, value=0, step=1, label="Rotate")
      with gr.Row():
        monochrome = gr.Checkbox(label="Monochrome")
      
      
      out_tc = gr.Image(label="Result", interactive=False, type="pil", width=512, height=512)
      
      infer_tc = gr.Button("Run", variant="primary")
      infer_tc.click(
        tunnel, inputs=[image, mode, invert, rotate, monochrome], outputs=out_tc
      )
    
    mode.change(
      change, mode, [color_converter, template_converter]
    )
    
  return i