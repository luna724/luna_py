import gradio as gr
import os
from typing import List
import LGS.misc.jsonconfig as jsoncfg

from modules.shared import ROOT_DIR, language
from webui import js_manager, FormColumn, FormRow, show_state_from_checkbox
from webui import UiTabs, get_lora_list, rp, browse_file, make_prompt_template

class Prompt(UiTabs):
  l = language("/ui/mt_child/define/prompt.py", "raw")
  
  def __init__(self, path):
    super().__init__(path)
    
    self.child_path = os.path.join(UiTabs.PATH, "generate_child")
  
  def variable(self):
    return [Prompt.l["tab_title"]]
  
  def index(self):
    return 1
      
  def ui(self, outlet):
    l = Prompt.l
    splitter = None
    
    with gr.Blocks():
      display_name = gr.Textbox(label=l["displayname"], placeholder=l["displayname_placeholder"])
      with FormColumn():
        prompt = gr.Textbox(label=l["prompt"], lines=4)
        negative = gr.Textbox(label=l["negative"], placeholder=l["negative_placeholder"], lines=4)
        
        
        splitter
        with gr.Group():
          activate_adetailer = gr.Checkbox(label=l["activate_adetailer"], value=False)
          with gr.Accordion(label=l["adetailer_root"], visible=False) as adetailer_root:
            activate_adetailer.change(
              show_state_from_checkbox, activate_adetailer, adetailer_root
            )
            with FormRow():
              adetailer_prompt = gr.Textbox(label=l["adetailer_prompt"], lines=3)
              adetailer_negative = gr.Textbox(label=l["adetailer_negative"], lines=3)
          
        
        splitter
        with gr.Group():
          activate_controlnet = gr.Checkbox(label=l["activate_controlnet"], value=False)
          with gr.Accordion(label=l["controlnet_opts"], visible=False) as controlnet_root:
            activate_controlnet.change(
              fn=show_state_from_checkbox, inputs=[activate_controlnet], outputs=[controlnet_root]
            )
            with FormRow():
              cn_mode = gr.Textbox(label=l["control_mode"], value="OpenPose")
              cn_weight = gr.Slider(-1, 2.0, label=l["control_weight"], value=0.75, step=0.01)
            cn_image = gr.Image(label=l["control_image"], type='pil', source="upload")
            
            
        splitter
        with gr.Group():
          activate_rp = gr.Checkbox(label=l["activate_rp"], value=False)
          with gr.Accordion(label=l["rp_root"], open=True, visible=False) as rp_root:
            activate_rp.change(show_state_from_checkbox,
                               activate_rp, rp_root)
            with gr.Accordion(open=True, label=l["secondary_prompt"]):
              tmpl = l
              l:dict = l["secondary_items"]
              
              second_prompt = gr.Textbox(label=l["prompt"], lines=4)
              
              with gr.Row():
                with gr.Column():
                  with gr.Row():
                    sec_characters = gr.Dropdown(
                      label=l["lora_template"], choices=get_lora_list("manual")
                    )
                    sec_characters_r = gr.Button("\U0001f504", size="sm")
                    sec_characters_r.click(
                      get_lora_list, outputs=[sec_characters]
                    )
                  with gr.Row():
                    sec_lora = gr.Textbox(label=l["lora"])
                    sec_weight = gr.Slider(-2.0, 2.0, 0.75, step=0.01, label=l["weight"])
                  
                  sec_name = gr.Textbox(label=l["name"])
                  sec_head = gr.Textbox(label=l["header"])
                with gr.Column():
                  sec_prompt = gr.Textbox(label=l["character_prompt"])
                  sec_face = gr.Textbox(label=l["face"])
                  sec_location = gr.Textbox(label=l["location"])
                  sec_lower = gr.Textbox(label=l["lower"])
              sync_with_main = gr.Checkbox(label=l["sync_with_first"])
            
            with FormRow():
              l = tmpl
              rp_mode = gr.Radio(choices=["Attention", "Latent"], value="Attention", label=l["rp_mode"])
            
            with FormRow():
              use_base = gr.Checkbox(label=l["use_base"], value=False)
              use_common = gr.Checkbox(label=l["use_common"], value=False)
              use_ncommon = gr.Checkbox(label=l["use_negative_common"], value=False)
            base_ratio = gr.Number(label=l["base_ratio"], value=0.2)
            
            with FormRow():
              lora_stop = gr.Slider(0, 150, label=l["stop_step"], value=0, step=1)
              lora_hires = gr.Slider(0, 150, label=l["stop_hires"], value=0, step=1)
            
            with gr.Blocks():
              with gr.Row():
                with gr.Column():
                  split_mode = gr.Radio(choices=["Rows", "Columns", "Random"], value="Columns", label=l["matrix"])
                  split_text = gr.Textbox(label=l["division"], value="1:1")
                with gr.Column():
                  rp_width = gr.Slider(1, 2048, label=l["width"], step=1, value=512)
                  rp_height= gr.Slider(1, 2048, label=l["height"], step=1, value=512)
              try_visualize = gr.Button(l["visualize"])
              rp_image = gr.Image(label=l["rp_image"], type='pil', height=256, width=256)

              try_visualize.click(
                fn=rp.visualize,
                inputs=[
                  split_mode, split_text, rp_width, rp_height,
                  use_common, use_base, base_ratio
                ], outputs=[rp_image]
              )
              
        splitter
        with gr.Group():
          activate_hires = gr.Checkbox(label=l["activate_hires"], value=False)
          with gr.Accordion(label=l["hires_root"], visible=False) as hires_root:
            activate_hires.change(
              show_state_from_checkbox, activate_hires, hires_root
            )
            with FormRow():
              upscaler = gr.Textbox(label=l["upscaler"],value="R-ESRGAN 4x+ Anime6B")
              hires_step = gr.Slider(0, 150, step=1, label=l["steps"], value=8)
            with FormRow():
              denoise = gr.Slider(0, 1.0, step=0.01, label=l["denoising"], value=0.45)
              upscaled = gr.Slider(1.0, 4.0, value=2.0, step=0.01, label=l["upscaled"])
        
        splitter
        with gr.Group():
          activate_example = gr.Checkbox(label=l["activate_example_data"], value=False)
          with gr.Accordion(label=l["example_root"], visible=False) as example_root:
            activate_example.change(
              show_state_from_checkbox, activate_example, example_root
            )
            with FormRow():
              characters = gr.Dropdown(
                label=l["lora_template"], choices=get_lora_list("manual")
              )
              characters_r = gr.Button("\U0001f504", size="sm")
              characters_r.click(get_lora_list, outputs=characters)
            with FormRow():
              #with gr.Column():
              lora = gr.Textbox(label=l["lora"])
              lora_weight = gr.Slider(-2.0, 2.0, step=0.01, value=0.75, label=l["weight"])
              name = gr.Textbox(label=l["name"])
            with FormRow():
              character_prompt = gr.Textbox(label=l["character_prompt"])
              hasextend = gr.Checkbox(label=l["isextend"], value=True)
            with FormRow():
              face = gr.Textbox(label=l["face"])
              location = gr.Textbox(label=l["location"])
            with FormRow():
              header = gr.Textbox(label=l["header"])
              lower = gr.Textbox(label=l["lower"])
            with gr.Group():
              memo = gr.Textbox(label=l["memo"], placeholder="hello, world!")
            
            image = gr.Image(label=l["image"], source="upload")
        
        splitter
        activate_builtins = gr.Checkbox(label=l["activate_builtins"], value=False)
        with gr.Accordion(label=l["builtins_root"], visible=False) as builtins_root:
          activate_builtins.change(
            show_state_from_checkbox, activate_builtins, builtins_root
          )
          with FormRow():
            sampler = gr.Textbox(label=l["sample"], value="DPM++ 2M Karras")
            resolution = gr.Textbox(label=l["resolution"], value="512x768")
          with FormRow():
            clip = gr.Slider(0, 15, label=l["clip"], value=2)
        
        splitter
        with gr.Row():
          db_load_file = gr.Textbox(label=l["path"])
          db_load_browse = gr.Button("\U0001f504", size="sm")
          db_load_browse.click(browse_file, outputs=db_load_file)
        
        with gr.Row():
          status = gr.Textbox(label=l["status"])
        
        with FormRow():
          overwrite = gr.Checkbox(label=l["overwrite"])
          delete_loaded = gr.Checkbox(label=l["delete_after_load"], value=True)
        
        save = gr.Button(l["save"])
        save.click(fn=make_prompt_template.save,
                  inputs=[
                    display_name, prompt, negative, adetailer_prompt,
                    adetailer_negative, activate_controlnet,
                    cn_mode, cn_weight, cn_image, activate_hires,
                    upscaled, upscaler, denoise, hires_step, resolution,
                    sampler, activate_example, characters, lora, lora_weight,
                    name, character_prompt, hasextend,
                    face, location, header, lower, image, memo,
                    clip, overwrite, activate_rp, rp_mode, use_base,
                    use_common, use_ncommon, base_ratio, lora_stop,
                    lora_hires, split_mode, split_text, rp_width,
                    rp_height, second_prompt, sec_characters,
                    sec_lora, sec_weight, sec_name, sec_head,
                    sec_prompt, sec_face, sec_location, sec_lower,
                    sync_with_main, db_load_file, delete_loaded
                  ],
                  outputs=[status])
  