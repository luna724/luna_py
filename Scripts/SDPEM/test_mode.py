import gradio as gr
from typing import Literal

from test_script import ce
from lunapy_module_importer import Importer

def main(mode:Literal["ce", "g_template"]):
  if mode == "ce": #Archived (tests/ce.py)
    iface = ce.get()
  
  elif mode == "g_template":
    class var:
      refresh = "\U0001f504"
      cfn:dict = {
        "interactive": False,
        "show_copy_button": True,
        "max_lines": 1
      }
    
    tmpl_common = Importer("modules.generate.common")
    get_template = tmpl_common.obtain_template_list
    get_lora_template = tmpl_common.obtain_lora_list
    
    with gr.Blocks() as iface:
      # Initialize
      module = Importer("modules.generate.template")
      
      with gr.Row():
        template = gr.Dropdown(label="Template", choices=get_template.webui(), scale=4)
        template_refresh = gr.Button(var.refresh, scale=1)
        template_refresh.click(
          fn=get_template.update,
          outputs=template
        )
        
        lora = gr.Dropdown(label="LoRA Template", choices=get_lora_template.manual(), scale=4)
        lora_refresh = gr.Button(var.refresh, scale=1)
        lora_refresh.click(
          fn=get_lora_template.update, outputs=lora
        )
      
      with gr.Accordion("LoRA Variables", open=True, visible=False) as lora_var:
        with gr.Row():
          lora_var_check_1 = gr.Checkbox(label="", interactive=False)
          lora_var_check_2 = gr.Checkbox(label="", interactive=False)
        with gr.Row():
          lora_var_check_1_info = gr.Textbox(label="", **var.cfn)
          lora_var_check_2_info = gr.Textbox(label="", **var.cfn)
          
      with gr.Blocks():
        with gr.Row():
          with gr.Column():
            # Code for user variable
            pass
          with gr.Column():
            # Code for NOT Interactive interface
            # Selected LoRA
            with gr.Row():
              lora_id_1 = gr.Textbox(label="LoRA ID", **var.cfn)
              lora_nm_1 = gr.Textbox(label="LoRA Name", **var.cfn)
            with gr.Row():
              lora_pm_1 = gr.Textbox(label="LoRA Prompt", **var.cfn)
              lora_ex_1 = gr.Textbox(label="LoRA Extend", **var.cfn)
            
            # Selected Template
            with gr.Row():
              method = gr.Textbox(label="Method ver.", **var.cfn)
              tmpl_key = gr.Textbox(label="Key", **var.cfn)
            with gr.Row():
              tmpl_prompt = gr.Textbox(label="Prompt", lines=5, interactive=False)
              tmpl_negative = gr.Textbox(label="Negative", lines=5, interactive=False)
            
            tmpl_adetailer = gr.Checkbox(label="ADetailer Status")
            with gr.Row(visible=False) as tmpl_adetailer_visible:
              tmpl_ad_prompt = gr.Textbox(label="Prompt 1st", lines=3, interactive=False)
              tmpl_ad_negative = gr.Textbox(label="Negative 1st", lines=3, interactive=False)
            
            tmpl_hires = gr.Checkbox(label="Hires.fix Status")
            with gr.Group(visible=False) as tmpl_hires_visible:
              with gr.Row():
                tmpl_hi_upscaler = gr.Textbox(label="Hires UpScaler", **var.cfn)
                tmpl_hi_step = gr.Slider(0, 150, label="Hires Step", **var.cfn)
              with gr.Row():
                tmpl_hi_denoise = gr.Slider(0, 1, label="DeNoising Strength", **var.cfn)
                tmpl_hi_upscale = gr.Slider(1, 4, label="Upscale (×)", **var.cfn)
            
            tmpl_cn = gr.Checkbox(label="ControlNet[1st] Status")
            with gr.Group(visible=False) as tmpl_cn_visible:
              with gr.Row():
                tmpl_cn_mode = gr.Textbox(label="Control Mode", **var.cfn)
                tmpl_cn_weight = gr.Slider(-1, 2, label="Control Weights", **var.cfn)
              
              with gr.Accordion("Image"):
                tmpl_cn_image = gr.Image(height=768, width=768, image_mode="RGBA", type="pil", label="COntrolNet Image", elem_classes=["image-center"], **var.cfn)
                tmpl_cn_load_image = gr.Button("Load", variant="primary")
                tmpl_cn_load_image.click(
                  None, [template], tmpl_cn_image
                ) ## Load CN Image Function
            
            tmpl_rp = gr.Checkbox(label="Regional Prompter Status")
            with gr.Group(visible=False) as tmpl_rp_visible:
              tmpl_rp_mode = gr.Textbox(label="Generation Mode", **var.cfn)
              with gr.Row():
                tmpl_rp_base = gr.Checkbox(label="Use base prompt", **var.cfn)
                tmpl_rp_common = gr.Checkbox(label="Use common prompt", **var.cfn)
                tmpl_rp_ncommon = gr.Checkbox(label="Use common negative prompt", **var.cfn)
              tmpl_rp_ratio = gr.Textbox(label="Base Ratio", **var.cfn)
              
              with gr.Row():
                tmpl_rp_stop = gr.Slider(0, 150, label="LoRA stop step", **var.cfn)
                tmpl_rp_hires = gr.Slider(0, 150, label="LoRA Hires stop step", **var.cfn)
              
              with gr.Row():
                with gr.Column():
                  tmpl_rp_split = gr.Textbox(label="Main Matrix mode", **var.cfn)
                  tmpl_rp_division = gr.Textbox(label="Division Ratio", **var.cfn)
                with gr.Column():
                  tmpl_rp_w = gr.Slider(1, 2048, label="Width", **var.cfn)
                  tmpl_rp_h = gr.Slider(1, 2048, label="Height", **var.cfn)
              
              with gr.Row():
                tmpl_rp_template = gr.Textbox(label="Template", **var.cfn)
              
              with gr.Accordion(label="Sample"):
                tmpl_rp_image = gr.Image(height=768, width=768, image_mode="RGBA", type="pil", label="COntrolNet Image", elem_classes=["image-center"], **var.cfn)
                tmpl_rp_load_image = gr.Button("Load", variant="primary")
                tmpl_rp_load_image.click(
                  None, [template], tmpl_rp_image
                ) ## Load RP Sample Image Function
            
            tmpl_ex = gr.Checkbox(label="Example values", **var.cfn)
            with gr.Group(visible=False) as tmpl_ex_visible:
              tmpl_ex_lora = gr.Textbox(label="LoRA Template (When saved)", **var.cfn)
              
              with gr.Row():
                tmpl_ex_weight = gr.Slider(-2.0, 2.0, label="LoRA Weight", **var.cfn)
                tmpl_ex_extend = gr.Checkbox(label="Apply Extend Prompt", **var.cfn)
              with gr.Row():
                tmpl_ex_header = gr.Textbox(label="Header", **var.cfn)
                tmpl_ex_lower = gr.Textbox(label="Lower", **var.cfn)
              with gr.Row():
                tmpl_ex_face = gr.Textbox(label="1st Face", **var.cfn)
                tmpl_ex_face_2 = gr.Textbox(label="2nd Face", **var.cfn)
              with gr.Row():
                tmpl_ex_location = gr.Textbox(label="1st Location", **var.cfn)
                tmpl_ex_location_2 = gr.Textbox(label="2nd Location", **var.cfn)
              with gr.Row():
                tmpl_ex_accessory = gr.Textbox(label="Accessory", **var.cfn)
                tmpl_ex_other = gr.Textbox(label="Other", **var.cfn)
              
              with gr.Blocks():
                with gr.Row():
                  tmpl_ex_w = gr.Slider(1, 2048, label="Width", **var.cfn)
                  tmpl_ex_h = gr.Slider(1, 2048, label="Height", **var.cfn)
                with gr.Row():
                  clip_skip = gr.Slider(1, 15, label="Clip Skip", **var.cfn)
              
              with gr.Accordion("Image"):
                tmpl_ex_image = gr.Image(height=768, width=768, image_mode="RGBA", type="pil", label="COntrolNet Image", elem_classes=["image-center"], **var.cfn)
                tmpl_ex_load_image = gr.Button("Load", variant="primary")
                tmpl_ex_load_image.click(
                  None, [template], tmpl_ex_image
                ) ## Load Sample Image Function
            
            tmpl_bi = gr.Checkbox(label="Builtins Opts", value=True)
            with gr.Group(visible=True) as tmpl_bi_visible:
              with gr.Row():
                tmpl_bi_model = gr.Textbox(label="Checkpoints", **var.cfn)
                tmpl_bi_vae = gr.Textbox(label="VAE", value="Auto", **var.cfn)
              with gr.Row():
                tmpl_bi_sampler = gr.Textbox(label="Sampler", **var.cfn)
                tmpl_bi_method = gr.Textbox(label="Sampler Method", **var.cfn)
            
            
            ## Update database
            lora.change(
              module.change_lora, lora, [lora_var, # 
                lora_var_check_1, lora_var_check_1_info, #
                lora_var_check_2, lora_var_check_2_info, # LoRA Variables
                lora_id_1, lora_nm_1, lora_pm_1, lora_ex_1 # LoRA Example Viewer
                ]
            )
            template.change(
              module.change_template, template,
              [
                method, tmpl_key, tmpl_prompt, tmpl_negative,
                
              ]
            )
            
  iface.queue(64).launch(server_port=9999)