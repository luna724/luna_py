import gradio as gr
import os

from modules.shared import ROOT_DIR, language
from webui import example_view, get_template, get_lora_list, FormRow
from webui import show_state_from_checkbox, applicate_opts, applicate_lora, template_convert
from webui import UiTabs

class Template(UiTabs):
  l = language("/ui/generate/template.py", "raw")
  
  def variable(self):
    return [Template.l["tab_title"]]
  
  def index(self):
    return 1
  
  def ui(self, outlet):
    l = Template.l
    with gr.Blocks():
      with gr.Row():
        template = gr.Dropdown(label=l["template"], choices=get_template("webui"))
        template_refresh = gr.Button("\U0001f504", elem_classes=['refresh_btn'])
        template_refresh.click(
          fn=get_template,
          outputs=[template]
        )
        
      with gr.Blocks():
        with gr.Row():
          with gr.Column():
            lora = gr.Dropdown(label=l["lora"], choices=get_lora_list("manual"))
            
            with FormRow():
              _lora = gr.Textbox(label=l["lora_id"])
              name = gr.Textbox(label=l["name"])
            with FormRow():
              character_prompt = gr.Textbox(label=l["character_prompt"])
              with gr.Row():
                load_extend = gr.Checkbox(label="[Experiment]: "+l["hasextend"], value=False, scale=1)
                extend_prompt = gr.Textbox(label=l["extend_prompt"], interactive=False, scale=10)
            with FormRow():
              header = gr.Textbox(label=l["header"])
              lower = gr.Textbox(label=l["lower"])
            with gr.Row():
              location = gr.Textbox(label=l["location"])
              face = gr.Textbox(label=l["face"])
              
            # 3.0.5 or above feature
            with gr.Accordion("[Beta] v3.0.5 Feature", visible=False) as v305_variable:
              with gr.Row():
                sec_face = gr.Textbox(label=l["face"]+" 2")
                sec_location = gr.Textbox(label=l["location"]+" 2")
              with gr.Row():
                cloth = gr.Textbox(label=l["clothes"])
                sec_cloth = gr.Textbox(label=l["clothes"]+ " 2")
              with gr.Row():
                accessory = gr.Textbox(label=l["accessory"])
                other = gr.Textbox(label=l["other"])
              
              with gr.Accordion("[Beta] more variables", visible=False) as manual_variables:
                with gr.Row():
                  pv1 = gr.Textbox(label=l["variable_templates"].format("1"), interactive=False)
                  pv2 = gr.Textbox(label=l["variable_templates"].format("2"), interactive=False)
                with gr.Row():
                  pv3 = gr.Textbox(label=l["variable_templates"].format("3"), interactive=False)
                  pv4 = gr.Textbox(label=l["variable_templates"].format("4"), interactive=False)
                with gr.Row():
                  pv5 = gr.Textbox(label=l["variable_templates"].format("5"), interactive=False)
                  pv6 = gr.Textbox(label=l["variable_templates"].format("6"), interactive=False)
                with gr.Row():
                  pv7 = gr.Textbox(label=l["variable_templates"].format("7"), interactive=False)
                  pv8 = gr.Textbox(label=l["variable_templates"].format("8"), interactive=False)
                with gr.Row():
                  pv9 = gr.Textbox(label=l["variable_templates"].format("9"), interactive=False)
                  pv0 = gr.Textbox(label=l["variable_templates"].format("10"), interactive=False)
                  
            
            lora.change(
              applicate_lora, lora,
              outputs=[_lora, name, character_prompt, extend_prompt]
            )
            with gr.Accordion(label=l["adv_opts"], open=True) as adv_opts:
              lora_weight = gr.Slider(-2.0, 2.0, step=0.01, value=1.0, label=l["weight"])
              
              activate_adetailer_plus = gr.Checkbox(label=l["activate_adetailer"], value=False)
              
              with gr.Accordion(label=l["adetailer_plus_opts"], visible=False, open=True) as adetailer_plus_opts:
                activate_adetailer_plus.change(
                fn=show_state_from_checkbox, inputs=[
                  activate_adetailer_plus
                ], outputs=[adetailer_plus_opts]
              )
                with FormRow():
                  apply_positive = gr.Checkbox(label=l["apply_positive"], value=True)
                  apply_negative = gr.Checkbox(label=l["apply_negative"])
                
                with FormRow():
                  positive_apply_weight = gr.Slider(-2.0, 2.0, step=0.01, value=None, label=l["adetailer_weight_positive"], visible=True)
                  negative_apply_weight = gr.Slider(-2.0, 2.0, None, step=0.01, label=l["adetailer_weight_negative"], visible=False)
                  
                  apply_positive.change(
                    show_state_from_checkbox, apply_positive, positive_apply_weight
                  )
                  apply_negative.change(
                    show_state_from_checkbox, apply_negative, negative_apply_weight
                  )
                  
            with gr.Accordion(label=l["secondary_prompt"], open=True, visible=False) as secondary_prompt_opts:
              with gr.Column():
                loras = gr.Dropdown(label=l["lora"], choices=get_lora_list("manual"))
                lora_weights = gr.Slider(-2.0, 2.0, step=0.01, value=1.0, label=l["weight"])
                
                with FormRow():
                  sp_lora = gr.Textbox(label=l["lora_id"])
                  sp_name = gr.Textbox(label=l["name"])
                with FormRow():
                  sp_ch_prompt = gr.Textbox(label=l["character_prompt"],)
                  sp_extend = gr.Checkbox(False, label=l["hasextend"])                                  
                with FormRow():
                  locations = gr.Textbox(label=l["location"])
                  faces = gr.Textbox(label=l["face"])
                with FormRow():
                  headers = gr.Textbox(label=l["header"])
                  lowers = gr.Textbox(label=l["lower"])
                sp_sync_main = gr.Checkbox(label=l["sync"], value=False)
              loras.change(
                applicate_lora, loras,
                outputs=[sp_lora, sp_name, sp_ch_prompt, sp_extend]
              )

            prompt = gr.Textbox(label=l["output_prompt"], show_copy_button=True, lines=5, interactive=False)
            negative = gr.Textbox(label=l["output_negative"], show_copy_button=True, lines=5, interactive=False)
            
            with FormRow():
              adetailer_prompt = gr.Textbox(label=l["output_adetailer_prompt"], lines=3, show_copy_button=True, interactive=False)
              adetailer_negative = gr.Textbox(label=l["output_adetialer_negative"], lines=3, show_copy_button=True, interactive=False)
              
            status = gr.Textbox(label=l["Status"], interactive=False)
            
            generate = gr.Button(l["generate"])
            ex_generate = gr.Button(l["ex_generate"])
            
            generate.click(
              fn=template_convert,
              inputs=[
                template, lora, _lora, name, character_prompt,
                location, face, header, lower,
                lora_weight, load_extend, activate_adetailer_plus,
                apply_positive, apply_negative,
                positive_apply_weight, negative_apply_weight,
                loras, sp_lora, sp_name, sp_ch_prompt, 
                locations, faces, headers, lowers, sp_sync_main,
                lora_weights, sp_extend, sec_face, sec_location, cloth,
                sec_cloth, accessory, other
              ],
              outputs=[
                prompt, negative, adetailer_prompt, adetailer_negative, status
              ]
            )
            
          with gr.Column():
            view = gr.Button(l["view_this_template"])
            method_version = gr.Textbox(label=l["method"], interactive=False)
            
            with gr.Blocks():
              with gr.Group():
                selected_lora = gr.Textbox(label=l["selected_lora"])
                isExtend = gr.Checkbox(label=l["use_extend"])
                Elora_weight = gr.Slider(-2.0, 2.0, label=l["weight"])
              with FormRow():
                elora = gr.Textbox(label=l["lora_id"])
                ename = gr.Textbox(label=l["name"])
              with FormRow():
                eprompt = gr.Textbox(label=l["character_prompt"])
                blank = gr.Textbox(label="")
              with FormRow():
                eface = gr.Textbox(label=l["face"])
                elocation = gr.Textbox(label=l["location"])
              with FormRow():
                eheader = gr.Textbox(label=l["header"])
                elower = gr.Textbox(label=l["lower"])
              memo = gr.Textbox(label=l["memo"], lines=3)
              
            with gr.Blocks():
              with gr.Accordion(l["secondary_prompt"], visible=False) as sp_root:
                with gr.Column():
                  with FormRow():
                    es_character = gr.Textbox(label=l["selected_lora"])
                    es_weight = gr.Slider(-2.0, 2.0, label=l["weight"])
                    es_extend = gr.Checkbox(label=l["use_extend"])
                  with FormRow():
                    es_lora = gr.Textbox(label=l["lora_id"])
                    es_name = gr.Textbox(label=l["name"])
                  with FormRow():
                    es_prompt = gr.Textbox(label=l["character_prompt"])
                    blank = blank
                  with FormRow():
                    es_face = gr.Textbox(label=l["face"])
                    es_location = gr.Textbox(label=l["location"])
                  with FormRow():
                    es_header = gr.Textbox(label=l["header"])
                    es_lower = gr.Textbox(label=l["lower"])
                
                  with gr.Accordion("[Beta] v3.0.5 Feature", visible=False) as es_v305_variable:
                    with gr.Row():
                      es_sec_face = gr.Textbox(label=l["face"]+" 2")
                      es_sec_location = gr.Textbox(label=l["location"]+" 2")
                    with gr.Row():
                      es_cloth = gr.Textbox(label=l["clothes"])
                      es_sec_cloth = gr.Textbox(label=l["clothes"]+ " 2")
                    with gr.Row():
                      es_accessory = gr.Textbox(label=l["accessory"])
                      es_other = gr.Textbox(label=l["other"])
                    
                    with gr.Accordion("[Beta] more variables", visible=False) as es_manual_variables:
                      with gr.Row():
                        es_pv1 = gr.Textbox(label=l["variable_templates"].format("1"), interactive=False)
                        es_pv2 = gr.Textbox(label=l["variable_templates"].format("2"), interactive=False)
                      with gr.Row():
                        es_pv3 = gr.Textbox(label=l["variable_templates"].format("3"), interactive=False)
                        es_pv4 = gr.Textbox(label=l["variable_templates"].format("4"), interactive=False)
                      with gr.Row():
                        es_pv5 = gr.Textbox(label=l["variable_templates"].format("5"), interactive=False)
                        es_pv6 = gr.Textbox(label=l["variable_templates"].format("6"), interactive=False)
                      with gr.Row():
                        es_pv7 = gr.Textbox(label=l["variable_templates"].format("7"), interactive=False)
                        es_pv8 = gr.Textbox(label=l["variable_templates"].format("8"), interactive=False)
                      with gr.Row():
                        es_v9 = gr.Textbox(label=l["variable_templates"].format("9"), interactive=False)
                        es_pv0 = gr.Textbox(label=l["variable_templates"].format("10"), interactive=False)
                      
            with gr.Blocks():
              with gr.Accordion(l["example_images"], visible=False) as image_root:
                example_image = gr.Image(label="", interactive=False, elem_classes='image_resizer')
                
                with FormRow():
                  resolution = gr.Textbox(label=l["resolution"], placeholder="512×768")
                  clip_skip  = gr.Slider(1, 15, step=1, label=l["clip_skip"])
                  sampler = gr.Textbox(label=l["sampler"])
                  
            with gr.Blocks():
              with gr.Accordion(label=l["hires_root"], visible=False) as hires_root:
                with FormRow():
                  upscaler = gr.Textbox(label=l["upscaler"])
                  hstep = gr.Slider(0, 150, label=l["step"])
                with FormRow():
                  denoise = gr.Slider(0, 1, step=0.01, label=l["denoising_strength"])
                  upscale = gr.Slider(1, 4, step=0.01, label=l["upscaled"])
            
            with gr.Blocks():
              with gr.Accordion(label=l["cnunit"]+str(0), visible=False) as cn_root:
                with FormRow():
                  mode = gr.Textbox(label=l["cnmode"])
                  weight = gr.Slider(-1, 2, step=0.01, label=l["cnweight"])
                cnimage = gr.Image(label=l["cnimage"], interactive=False, elem_classes='image_resizer')
            
            with gr.Blocks():
              with gr.Accordion(label=l["rp"], visible=False) as rp_root:
                rp_mode = gr.Textbox(label=l["rp_mode"])
                
                with FormRow():
                  use_base = gr.Checkbox(label=l["use_base"])
                  use_common = gr.Checkbox(label=l["use_common"])
                  use_ncommon = gr.Checkbox(label=l["use_negative_common"])
                base_ratio = gr.Textbox(label=l["base_ratio"])
                
                with FormRow():
                  lora_stop = gr.Slider(0, 150, label=l["stop_step"],step=1)
                  lora_hires = gr.Slider(0, 150, label=l["stop_hires"], step=1)
                
                with gr.Blocks():
                  with gr.Row():
                    with gr.Column():
                      split_mode = gr.Textbox(label=l["matrix"])
                      division = gr.Textbox(label=l["division"])
                    with gr.Column():
                      res_w = gr.Slider(1, 2048, label=l["w"])
                      res_h = gr.Slider(1, 2048, label=l["h"])
                  
                  with gr.Row():
                    rp_image = gr.Image(label=l["sample"], type='pil', elem_classes='image_resizer')
                    rp_template = gr.Textbox(label=l["rp_template"],lines=4)
          view.click(fn=example_view,inputs=[template],
              outputs=[
                selected_lora, elora, Elora_weight,
                ename, eprompt, isExtend, eface, elocation,
                eheader, elower, memo, example_image,
                resolution, clip_skip, sampler, hires_root,
                upscaler, hstep, denoise, upscale, cn_root,
                mode, weight, cnimage, rp_root,
                rp_mode, use_base, use_common, use_ncommon,
                lora_stop, lora_hires, res_w, res_h,
                split_mode, division, base_ratio, rp_image,
                rp_template, sp_root, es_character, es_weight,
                es_lora, es_name, es_prompt, es_face, es_location,
                es_header, es_lower, method_version, secondary_prompt_opts
              ])
          template.change(
            applicate_opts,
            template,
            outputs=[
              secondary_prompt_opts, lora_weight,
              lora_weights, v305_variable, manual_variables,
              face, sec_face, location, sec_location, 
              cloth, sec_cloth, accessory, other
            ]
          )