import gradio as gr
from typing import Literal

from test_script import ce, g_template
from lunapy_module_importer import Importer

def main(mode:Literal["ce", "g_template", "mt_s_template", "mt_s_lora"]):
  if mode == "ce": #Archived (tests/ce.py)
    iface = ce.get()
  elif mode == "g_template": #Archived (tests/g_template.py)
    iface = g_template.get()
  elif mode == "mt_s_template":
    # tmpl_common = Importer("modules.generate.common")
    # get_template = tmpl_common.obtain_template_list
    # get_lora_template = tmpl_common.obtain_lora_list
    
    # module = Importer("modules.manage.templates.save")
    # AVV = module.available_versions
    
    # with gr.Blocks() as iface:
    #   selected_version = gr.Dropdown(AVV, value=AVV[0], label="Selected version")
    #   selected_version.change(
    #     module.selected_version_changer,
    #     selected_version
    #   )
    #   ## TODO: get versions (e.g. v3/modules/ui/mt_child/define_child/prompt.py)
      
    #   ## From below, insert to "/prompts/v4.py"
    #   with gr.Blocks():
    #     display_name = gr.Textbox(label="displayName")
        
    #     with gr.Row():
    #       prompt = gr.Textbox(label="Prompt", lines=4, placeholder="All buildins keywords at template_info.md")
    #       negative = gr.Textbox(label="Negative prompt", lines=4, placeholder="if blank, insteads database's value\nif need blank Negative, set to \".\"")
        
    #     with gr.Row():
    #       with gr.Column():
    #         with gr.Group():
    #           adetailer_activate = gr.Checkbox(label="activate ADetailer")
    #           with gr.Accordion(label="ADetailer", visible=False) as adetailer_root:
    #             adetailer_disable = gr.Checkbox(label="deactivate ADetailer")
                
    #             # change
    #             adetailer_activate.change(
    #               module.activate_method,
    #               [adetailer_activate], 
    #               [adetailer_activate, adetailer_disable, adetailer_root]
    #             )
    #             adetailer_disable.change(
    #               module.deactivate_method,
    #               [adetailer_disable], 
    #               [adetailer_activate, adetailer_disable, adetailer_root]
    #             )
                
    #             adetailer_model = gr.Dropdown(
    #               allow_custom_value=True, label="ADetailer model",
    #               choices=module.model_db.get_adetailer_models(),
    #               value=module.model_db.get_adetaler_primary_model()
    #             )
                
    #             with gr.Row():
    #               adetailer_prompt = gr.Textbox(
    #                 label="Prompt", lines=3
    #               )
    #               adetailer_negative = gr.Textbox(
    #                 label="Negative Prompt", lines=3
    #               )
            
    #         with gr.Group():
    pass
  elif mode == "mt_s_lora":
    tmpl_common = Importer("modules.generate.common")
    get_lora_template = tmpl_common.obtain_lora_list
    module = Importer("modules.manage.lora.save")
    
    with gr.Blocks() as iface:
      with gr.Row():
        display_name = gr.Textbox(label="displayName", max_lines=1, scale=7)
        version = gr.Dropdown(label="version", scale=3, choices=module.get_avv(), value=module.get_recommend_version())
      
      
      with gr.Tab("v5"): # version によって変更するタブ  template/save.py 参照
        with gr.Row():
          lora_id = gr.Textbox(label="$LORA trigger", placeholder="<lora:example:1.0>  |  . to Empty", scale=62)
          lora_id_is_lora = gr.Checkbox(True, scale=20, label="isLoRA")
          check_lora_id = gr.Button("Check", scale=12)
          check_lora_id.click(module.check_lora_id, [lora_id, lora_id_is_lora])
        
        with gr.Row():
          name = gr.Textbox(label="$NAME trigger", placeholder="My template treats it as a character name.")
        
        with gr.Row():
          prompt = gr.Textbox(label="$PROMPT trigger", placeholder="My template treats it as a character prompt. (except hair and other variable features)")
          extend = gr.Textbox(label="$EXTEND trigger", placeholder="My template treats it as a def Character prompt (include ONLY hair and other variables.)")
        
        with gr.Row():
          with gr.Column():
            lora_var1 = gr.Checkbox(label="LoRA Variable1 ($LV1)")
            with gr.Group(visible=False) as lv1:
              var1_title = gr.Textbox(label="Title (doesn't affect code/template)", placeholder="memo for user")
              var1_prompt = gr.Textbox(label="Prompt for this")
        
        with gr.Column():
          lora_var2 = gr.Checkbox(label="LoRA Variable2 ($LV2)")
          with gr.Group(visible=False) as lv2:
            var2_title = gr.Textbox(label="Title (doesn't affect code/template)", placeholder="memo for user")
            var2_prompt = gr.Textbox(label="Prompt for this")
        
        lora_var1.change(module.bool2visible, lora_var1, lv1)
        lora_var2.change(module.bool2visible, lora_var2, lv2)
        
        with gr.Row():
          overwrite = gr.Checkbox(label="Overwrite")
        
        status = gr.Textbox(label="Status")
        save = gr.Button("Save", variant="primary")
        
        gr.Markdown("<br />")
        with gr.Group():
          with gr.Accordion("Load", open=False):
            with gr.Row():
              target = gr.Dropdown(
                choices=get_lora_template.manual(), label="Target", scale=72
              )
              refresh = gr.Button("♲", scale=28)
              refresh.click(get_lora_template.manual, outputs=target)
            load = gr.Button("Load", variant="primary")
            load.click(
              module.load_primary, # バージョンが変われば load_primary -> module.legacy.load_for_v5 等に変更
              [target, display_name, lora_id, lora_id_is_lora, name, prompt, extend,
                lora_var1, var1_title, var1_prompt, lora_var2, var2_title, var2_prompt,
                overwrite],
              [status, display_name, lora_id, name, prompt, extend,
                lora_var1, var1_title, var1_prompt, lora_var2, var2_title, var2_prompt,
                lora_id_is_lora, overwrite]
            )
        
        save.click(
          module.save_primary,
          [target, display_name, lora_id, lora_id_is_lora, name, prompt, extend,
                lora_var1, var1_title, var1_prompt, lora_var2, var2_title, var2_prompt,
                overwrite],
          status
        )

                
  iface.queue(64).launch(server_port=9999)