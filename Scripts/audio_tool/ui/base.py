import gradio as gr
import sys
sys.path.append("..\\")
from lib import normalizer

from lib.shared import *

def ui_launch():
  with gr.Blocks() as iface:
    gr.Markdown("lunapy/Audio_tool")
    
    with gr.Tab("Normalizer"):
      with gr.Column():
        norm_in = gr.Textbox(label="Target File", placeholder="/example/target.mp3")
        with gr.Row():
          norm_convall = gr.Checkbox(label="Convert All")
          norm_output_format = gr.Radio(choices=[".mp3", ".flac", ".wav", "Keep Previous Format"], value="Keep Previous Format", label="Output Format")
          
      norm_status = gr.Textbox(label="Status")
      norm_conv = gr.Button("Normalize")
      
      norm_log = gr.Textbox(label="Logs",
                            max_lines=25,
                            every=0.1)

      norm_conv.click(
        fn=normalizer.webui,
        inputs=[norm_in, norm_convall, norm_output_format],
        outputs=[norm_status]
      )
    
    with gr.Tab("Properties Auto Setter"):
      
  return iface