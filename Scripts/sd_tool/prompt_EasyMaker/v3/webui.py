import gradio as gr
import os
import sys

sys.path.append(".")
sys.path.append("..\\")
sys.path.append("..\\./py")

from a1111_ui_util import *
#from py import template_generator, lib

from modules.generate import get_template
from modules.generate import generate as template_generate, example_view
from modules.generate_util import get_lora_list
from modules.character_exchanger import character_exchanger
from modules import make_template, delete_prompt_template
import preprocessing
import modules.shared as shared 

import LGS.misc.jsonconfig as jsoncfg

with gr.Blocks() as main_iface:
  br = gr.Markdown("<br>")
  with gr.Tab("Database"):
    with FormColumn():
      gr.Textbox(label="Negative", value=shared.negative)
      gr.Textbox(label="ADetailer Positive", value=shared.ad_pos)
      gr.Textbox(label="ADetailer Negative", value=shared.ad_neg)
  with gr.Tab("Generate"):
    with gr.Tab("Template"):
      with FormRow():
        template = gr.Dropdown(label="Target template", choices=get_template("webui"))
        template_refresh = ToolButton("\U0001f504")
        template_refresh.click(
          fn=get_template,
          inputs=[],outputs=[template]
        )
      
      with gr.Blocks():
        with FormRow():
          with FormColumn():
            lora = gr.Dropdown(label="Select Character Template", choices=get_lora_list("manual"))
            
            with FormRow():
              location = gr.Textbox(label="Draw Location")
              face = gr.Textbox(label="Character Face")
            with FormRow():
              header = gr.Textbox(label="Prompt Header")
              lower = gr.Textbox(label="Prompt Lower")
            
            with gr.Accordion(label="Advanced Options", open=True):
              lora_weight = gr.Slider(minimum=-2.0,maximum=2.0,step=0.0001, label="Lora Weight", value=1.0)
              with InputAccordion(label="Use Face prompt for ADetailer Prompt", value=False) as use_face_for_adetailer:
                activate_negative = gr.Checkbox(label="Apply to Negative too")
                overall_weight_control = gr.Slider(-2.0, 2.0, 1.0, step=0.001, label="Overall Weight")
            
            out_prompt = gr.Textbox(label="Output Prompt", show_copy_button=True, lines=5)
            out_negative = gr.Textbox(label="Negative", show_copy_button=True, lines=5)
            with FormRow():
              out_ad_prompt = gr.Textbox(label="Output ADetailer", show_copy_button=True, lines=3)
              out_ad_negative = gr.Textbox(label="Output ADetailer Negative", show_copy_button=True, lines=3)
            
            status = gr.Textbox(label="Status", lines=1, interactive=False)
            br
            generate = gr.Button("Generate")
            ex_generate = gr.Button("Generate with Right Tab's Data")
            generate.click(
              fn=template_generate,
              inputs=[
                template, lora, location, face, header, lower,
                lora_weight, use_face_for_adetailer,
                activate_negative, overall_weight_control
              ],
              outputs=[
                out_prompt, out_negative, out_ad_prompt, out_ad_negative, status
              ]
            )
          with FormColumn():
            ex_view = gr.Button("View this Template's Value")
            ex_method_ver = gr.Textbox(label="Method Version", interactive=False)
            br
            
            with gr.Blocks():
              with gr.Blocks():
                with FormRow():
                  ex_characters_data = gr.Textbox(label="Selected Character Template")
                with FormRow():
                  ex_lora = gr.Textbox(label="LoRA ID", placeholder="<lora:ichika3:1.0>")
                  ex_name = gr.Textbox(label="Character Name", placeholder="luna")
                with FormRow():
                  ex_prompt = gr.Textbox(label="Character Prompt", placeholder="melody hair, multicolored hair")
                  ex_isextend = gr.Textbox(label="Character Prompt Extender")
                with FormRow():
                  ex_face = gr.Textbox(label="Character Face", placeholder="facing at bookshelf, unemotional")
                  ex_location = gr.Textbox(label="Draw Location", placeholder="indoor, bookshelf, library")
                with FormRow():
                  ex_header = gr.Textbox(label="Prompt Header", placeholder="(masterpiece, best quality:1.005), 1girl, solo")
                  ex_lower = gr.Textbox(label="Prompt Lower", placeholder="<lora:detail_tweaker:-0.15>, <lora:masusu_breastsandnipples:0.45>")
                ex_csn = gr.Textbox(label="CustomNegative", lines=3)
              
              br
              
              with gr.Blocks():
                with gr.Accordion(label="Example Data's Image", visible=False, open=True) as ex_image_root:
                  ex_image = gr.Image(label="", interactive=False)
                with FormRow():
                  ex_resolution = gr.Textbox(label="Resolution", placeholder="512x768")
                  ex_clip = gr.Slider(1, 15, step=0.1, label="Clip Skip")
                with FormRow():
                  ex_sampler = gr.Textbox(label="Sampler", placeholder="DPM++ 2M Karras")
              
              br
              with gr.Blocks():
                with gr.Accordion(label="Hires.fix", open=True, visible=False) as ex_hires_root:
                  with gr.Row():
                    ex_hires_sampler = gr.Textbox(label="Hires Sampler")
                    ex_hires_steps = gr.Slider(0, 150, step=1, label="Hires Step")
                  with gr.Row():
                    ex_hires_denoising = gr.Slider(0, 1, step=0.01, label="Denoising Strength")
                    ex_hires_upscale = gr.Slider(1, 4, step=0.01, label="Upscale to")
              
              br
              with gr.Blocks():
                with gr.Accordion(label="Control Net Unit0", open=True, visible=False) as ex_cn_root:
                  with gr.Row():
                    ex_cn_mode = gr.Textbox(label="Control Mode")
                    ex_cn_weight = gr.Slider(-1, 2, step=0.01, label="ControlNet Weight")
                  br
                  ex_cn_image = gr.Image(label="Unit Image")
              
              ex_view.click(
                fn=example_view,
                inputs=[template],
                outputs=[
                  ex_characters_data, ex_lora, ex_name,
                  ex_prompt, ex_isextend, ex_face,
                  ex_location, ex_header, ex_lower,
                  ex_csn, ex_image_root,
                  ex_image, ex_resolution,
                  ex_clip, ex_sampler, ex_hires_root,
                  ex_hires_sampler, ex_hires_steps,
                  ex_hires_denoising,
                  ex_hires_upscale,
                  ex_cn_root, ex_cn_mode,
                  ex_cn_weight, ex_cn_image,
                  ex_method_ver
                ]
              )
  
  with gr.Tab("Manage Template"):
    with gr.Tab("Define"):
      with gr.Tab("Prompt"):
        with gr.Blocks():
          dt_displayname = gr.Textbox(label="displayName", placeholder="Template's display Name in webUI", max_lines=1)
          with FormColumn():
            dt_prompt = gr.Textbox(label="Prompt", placeholder="Template Based Prompt keyword is below", lines=4)
            with gr.Accordion("Prompt Keyword", open=False):
              dt_kw_list = gr.Markdown(jsoncfg.read_text(
                os.path.join(shared.ROOT_DIR, "database", "v3", "dt_kw_list.md")
              ))
            br
            dt_negative = gr.Textbox(label="Negative", placeholder="Template's negative prompt (if blank, obtain from database/negative)", lines=4)
            
            with gr.Blocks():
              with InputAccordion(label="ADetailer Prompts", value=True) as dt_enable_adetailer:
                with FormRow():
                  dt_ad_prompt = gr.Textbox(label="Adetailer Prompt", lines=5)
                  dt_ad_negative = gr.Textbox(label="Adetailer Negative", lines=5)
            br
            with gr.Blocks():
              with InputAccordion(label="ControlNet", value=False) as dt_enabled_controlnet:
                with FormRow():
                  dt_cn_mode = gr.Textbox(label="Control Mode", placeholder="OpenPose")
                  dt_cn_weight = gr.Slider(-1, 2.0, label="ControlNet Weight", value=0.75, step=0.05)
                dt_cn_image = gr.Image(label="ControlNet Image", type="pil", source="upload")
            br
            with gr.Blocks():
              with InputAccordion(label="Hires.fix", value=True) as dt_enabled_h:
                with FormRow():
                  dt_h_sampler = gr.Textbox(label="Hires.fix Sampler", value="R-ESRGAN 4x+ Anime6B")
                  dt_h_steps = gr.Slider(0, 150, step=1,label="Hires Steps", value=8)
                with FormRow():
                  dt_h_denoise = gr.Slider(0, 1.0, step=0.01, label="Denoising Strength", value=0.45)
                  dt_h_upscl = gr.Slider(1.0, 4.0, value=2.0, step=0.01, label="Upscale")
            br
            with InputAccordion(label="Example Viewer's data", value=False) as dt_enabled_ex:
              with FormRow():
                dt_ex_characters_beta = gr.Dropdown(
                  choices=get_lora_list("manual"))
                dt_ex_characters_beta_r = ToolButton("\U0001f504")
                dt_ex_characters_beta_r.click(fn=get_template,inputs=[],outputs=[dt_ex_characters_beta])
              with FormRow():
                dt_ex_lora = gr.Textbox(label="LoRA", placeholder="in to \"$LORA\"")
                dt_ex_name = gr.Textbox(label="Name", placeholder="in to \"$NAME\"")
              with FormRow():
                dt_ex_prompt = gr.Textbox(label="Prompt", placeholder="in to \"$PROMPT\"")
                dt_ex_isExtend = gr.Checkbox(label="Apply character Extend", value=True)
              with FormRow():
                dt_ex_face = gr.Textbox(label="Face", placeholder="in to \"$FACE\"")
                dt_ex_location = gr.Textbox(label="Location", placeholder="in to \"$LOCATION\"")
              with FormRow():
                dt_ex_header = gr.Textbox(label="Header", placeholder="in to prompt header")
                dt_ex_lower = gr.Textbox(label="Lower", placeholder="in to prompt lower")
              with InputAccordion(label="use custom Negative Prompt", value=False) as dt_enabled_csn:
                with FormColumn():
                  dt_ex_csn = gr.Textbox(label="Custom Negative", placeholder="", lines=4)
              br
              dt_ex_image = gr.Image(label="ControlNet Image", type="pil", source="upload")
              
            br
            with gr.Accordion("Builtins", open=True):
              with FormRow():
                dt_sampler = gr.Textbox(label="Sampling Method", value="DPM++ 2M Karras", placeholder="Euler a")
                dt_resolution = gr.Textbox(label="Recommended Image Resolution", value="512x512", placeholder="{width}x{height}")
              with FormRow():
                dt_clip = gr.Slider(0, 15, label="Clip Skip", value="2")

          dt_db_path = gr.Textbox(label="Database Path", interactive=False)
          dt_status = gr.Textbox(label="Status")
          with FormRow():
            dt_overwrite = gr.Checkbox(label="Overwrite previous template (if exists)", value=False)
            dt_save = gr.Button("Save")
          dt_save.click(
            fn=make_template.save,
            inputs=[
              dt_displayname, dt_prompt, dt_negative, dt_ad_prompt,
              dt_ad_negative, dt_enabled_controlnet, dt_cn_mode,
              dt_cn_weight, dt_cn_image, dt_enabled_h, dt_h_upscl,
              dt_h_sampler, dt_h_denoise, dt_h_steps, dt_resolution,
              dt_sampler, dt_enabled_ex, dt_ex_characters_beta,
              dt_ex_lora, dt_ex_name, dt_ex_prompt, dt_ex_isExtend,
              dt_ex_face, dt_ex_location, dt_ex_header, dt_ex_lower,
              dt_ex_image, dt_enabled_csn, dt_ex_csn, dt_clip,
              dt_db_path, dt_overwrite],outputs=[dt_status])

    with gr.Tab("Delete"):
      with gr.Tab("Prompt"):
        with FormRow():
          del_p_template = gr.Dropdown(label="Target template", choices=get_template("webui"))
          del_p_template_refresh = ToolButton("\U0001f504")
          del_p_template_refresh.click(
            fn=get_template,
            inputs=[],outputs=[del_p_template]
          )
        br
        with FormColumn():
          with FormRow():
            del_p_no_backup = gr.Checkbox(label="Backup", value=True)
          
          
          del_p_status = gr.Textbox(label="Status")
          del_p_btn = gr.Button("Delete")
          del_p_btn.click(
            fn=delete_prompt_template.delete_selected,
            inputs=[del_p_template], outputs=[del_p_status]
          )
    
  with gr.Tab("Character Exchanger"):
    with FormRow():
      ce_mode = DropdownMulti(
        choices=["lora", "name", "prompt"],
        label="Mode (Exchange Target)", value=["lora", "name", "prompt"]
      )
    
    with FormRow():
      ce_ch = gr.Dropdown(label="Exchange to (Character)", choices=get_lora_list("manual"))
    
    br
    with gr.Row():
      ce_base = gr.Textbox(label="Exchange Target Prompt", lines=10)
      ce_out = gr.Textbox(label="Resized Prompt", lines=10)
    br
    ce_info = gr.Textbox(label="Character dict Information")
    
    ce_run = gr.Button("Exchange")
    ce_run.click(
      fn=character_exchanger,
      inputs=[ce_mode, ce_base, ce_ch],
      outputs=[ce_out, ce_info]
    )


if __name__ == "__main__":
  if not os.path.exists(os.path.join(shared.ROOT_DIR, "launch_check.lunafile")):
    preprocessing.run()
  main_iface.queue(64)
  main_iface.launch()