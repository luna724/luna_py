import gradio as gr
from typing import Literal

from lunapy_module_importer import Importer

def main(mode:Literal["ce"]):
  if mode == "ce":
    generate_common = Importer("modules.generate.common")
    character_exchanger = Importer("modules.ce_all")
    
    with gr.Blocks() as iface:
      with gr.Row():
        mode = gr.Dropdown(choices=["lora", "name", "prompt"], label="mode", value=["lora", "name", "prompt"], multiselect=True)
      
      with gr.Row():
        template = gr.Dropdown(label="template", choices=generate_common.obtain_lora_list.manual())
        refresh = gr.Button("refresh")
        refresh.click(generate_common.obtain_lora_list.update, outputs=template)
      
      with gr.Row():
        target = gr.Textbox(label="input", lines=4, scale=10)
        outs = gr.Textbox(label="output", interactive=False, show_copy_button=True, lines=4, scale=9)
      
      with gr.Blocks():
        with gr.Row():
          template_mode = gr.Checkbox(label="for template")
        
      status = gr.Textbox(label="status", interactive=False)
      run = gr.Button("run", variant="primary")
      run.click(
       character_exchanger.call,
        [mode, target, template, template_mode],
        [outs, status]
      )
    
  iface.queue(64).launch(server_port=9999)