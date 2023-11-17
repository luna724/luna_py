import gradio as gr
# import WHB_generator as whbgen
# import Masturbation_generator as mastgen
import importlib
import os
import subprocess
import tentacle_clothes as tcgen
import log_writer as log_writer
import simple_generator as data
import lib as data_new
import tentacles_all as te
import base_generator as bg
import lora_info_viewer as liv
import multiple_generating as mg
import template_generator as tg
import checkpoint_info_viewer as civ
import template_multi as tmg
import database_setup as dbs
from lib import preprocessing

def reload_module():
  importlib.reload(tcgen)
  importlib.reload(log_writer)
  importlib.reload(data)
  importlib.reload(te)
  importlib.reload(bg)
  importlib.reload(liv)
  importlib.reload(mg)
  importlib.reload(tg)
  importlib.reload(civ)
  print("Module Reload Successfully Completed!")

def reload_ui():
  subprocess.Popen(["python", "webui.py"])
  os._exit(0)
  
with gr.Blocks() as itrmain:
  rld_ui_btn = gr.Button("Reload jsondata",size="sm")
  rld_ui_btn.click(fn=reload_module)
  
  rldui_btn = gr.Button("Reload WebUI", size="sm")
  rldui_btn.click(fn=reload_ui)
  
  gr.Markdown("Colab: https://colab.research.google.com/drive/1NJJrxjKK3YzfiElHrmS2AmzXv65Y38TR#scrollTo=TmcYoEe8dFK9")
  # with gr.Tab("WHB_Generator"):
  #   whbgen_chname = gr.Textbox(label="Charactor Prompt Name")
  #   whbgen_chprom = gr.Textbox(label="Charactor Prompt")
  #   whbgen_template_type = gr.Radio(choices=["着衣h", "服なんていらない☆"], value="着衣h", label="Template Type")
  #   whbgen_clothes = gr.Textbox(label="Charactor Clothes (Only Work with 着衣h)", value="black serafuku, grey serafuku")
  #   whbgen_facetype = gr.Radio(choices=["blush", "orgasm"], value="blush", label="Face Type")
  #   whbgen_adetailer = gr.Radio(choices=["0", "1"], value="0", label="ADetailer Modify")
  #   whbgen_whb__ = gr.Radio(choices=["0", "1"], label="Powerful WHB Draw", value="0")
  #   whbgen_vibrator = gr.Radio(choices=["0", "1"], label="Breasts on Vibrator", value="0")
  #   whbgen_ezclothH = gr.Radio(choices=["0", "1"], label="Easy 着衣H Generator", value="0")
    
  #   whbgen_inputs = [whbgen_chname, whbgen_chprom,
  #                    whbgen_clothes,
  #                    whbgen_template_type,
  #                    whbgen_facetype,
  #                    whbgen_adetailer,
  #                    whbgen_whb__,
  #                    whbgen_vibrator,
  #                    whbgen_ezclothH]
    
  #   whbgen_outputs = [gr.Markdown(""), gr.Markdown("")]

  #   whbgen_buttons = gr.Button("Convert")
    
  # whbgen_buttons.click(fn=whbgen.WHB_Generator, inputs=whbgen_inputs,
  #                      outputs=whbgen_outputs)
    
  # with gr.Tab("Masturbation_Generator"):
  #   gr.Markdown("standingやsmall breasts などの項目は キャラクタープロンプト、または服装プロンプトに代入")
  #   mast_chname = gr.Textbox(label="Charactor Prompt Name")
  #   mast_chprom = gr.Textbox(label="Charactor Prompe")
  #   mast_cloth  = gr.Textbox(label="Charactor Clothes")
  #   mast_draw_at = gr.Textbox(label="Position Prompt")
  #   mast_type = gr.Radio(choices=["Solo", "yuri"], label="Masturbation Type", value="Solo")
  #   mast_facetype = gr.Radio(choices=["blush", "orgasm", "露出えっち"], label="Face Types", value="blush")
  #   mast_onbed = gr.Checkbox(label="Charactor Sitting on bed?", value=False)
  #   mast_isnude = gr.Checkbox(label="Charactor is nude?", value=False )
  #   mast_vibrator = gr.Checkbox(label="Charactor Nipples on Vibrator?", value=False)
  #   mast_require_solo = gr.Checkbox(label="Emphasis on 1girl", value=True)
  #   mast_more_nsfw = gr.Checkbox(label="More NSFW", value=False)
  #   mast_types = gr.Radio(choices=["Fingering", "tables"], value="Fingering", label="Masturbation Types (Work with Solo Only)")
        
  #   mast_inputs =[mast_chname,
  #                 mast_chprom,
  #                 mast_cloth,
  #                 mast_draw_at,
  #                 mast_type,
  #                 mast_facetype,
  #                 mast_onbed,
  #                 mast_isnude,
  #                 mast_vibrator,
  #                 mast_require_solo,
  #                 mast_more_nsfw,
  #                 mast_types]
  #   mast_outputs = gr.Markdown("")  
  #   mast_btns = gr.Button("Convert")
  
  # mast_btns.click(fn=mastgen.Masturbation_gen,
  #                 inputs= mast_inputs,
  #                 outputs=mast_outputs)
  
  with gr.Tab("Tentacle Clothes Generator"):
    tc_chn = gr.Radio(choices=data_new.webui_tweaks("CHARACTER"), label="Character Name", value="original")
    tc_drawat = gr.Textbox(label="Location Prompt")
    tc_chwp = gr.Textbox(label="Charactor Clothing Prompt (NOT Recomendded)")
    with gr.Accordion("Original Option", open=False):
      gr.Markdown(" > Only Needed Choices \"Original\"")
      tc_chp = gr.Textbox(label="Charactor Prompt")
      tc_lora = gr.Textbox(label="Charactor LoRA Model+Name (Example: <Lora:HoshinoIchika:1.0>, ichika)")
    
    tc_face = gr.Radio(choices=["blush", "orgasm", "blush+"], value="blush", label="Face Type")
    tc_more = gr.Checkbox(label="More Nude", value=False)
    tc_more_t = gr.Checkbox(label="More Tentacles", value=False)

    tc_btn = gr.Button("Generate")
  
    tc_outputs = gr.Markdown("")
    tc_input = [tc_chp, tc_chwp, tc_lora, tc_drawat,
                tc_face,
              tc_chn, tc_more, tc_more_t]
    tc_btn.click(fn=tcgen.Tentacle_Clothes_Generator,
               inputs=tc_input, outputs=tc_outputs)
  
    with gr.Accordion("Prompt Log", open=False):
      tc_file = gr.Textbox(label="Log File", value="tentacle_clothes.py-log.txt", visible=False)
      apas_log = gr.Markdown("")
      
      with gr.Row().style(equal_height=True):
        apas_log_btn = gr.Button("Refresh")
        apas_log_del = gr.Button("Reset Log")
        apas_log_btn.click(fn=log_writer.r,
                           inputs=tc_file,
                           outputs=apas_log)
        apas_log_del.click(fn=log_writer.delete,
                           inputs=tc_file
                           )
  
  with gr.Tab("Tentacles Generator"):
    
    te_name = gr.Radio(choices=data_new.webui_tweaks("CHARACTER"), label="Charactor Name", value="original")
    te_locate = gr.Textbox(label="Draw Location")
    te_clothing = gr.Textbox(label="Charactor Clothes")
  
    with gr.Accordion("Original Option", open=False):
      gr.Markdown(" > Only Need Choices \"Original\"")
      te_prompt = gr.Textbox(label="Charactor Prompt")
      te_lora = gr.Textbox(label="Charactor Lora Model")

    te_face = gr.Radio(choices=data.face_type_list, value="blush+", label="Face Type")
    te_type = gr.Radio(choices=["Horosuke", "ICEJelly"], value="ICEJelly", label="Tentacle Model Type")
    
    te_prneg = gr.Checkbox(label="Print Negative Prompt + ADetailer Prompt", value=False)
    
    te_btn = gr.Button("Generate")
    te_in = [te_name, te_prompt, te_lora, te_locate,
             te_clothing, te_face, te_type, te_prneg]
    te_outputs = gr.Markdown()
    
    te_btn.click(fn=te.Tentacle_ALL,
                 inputs=te_in,
                 outputs=te_outputs)
        
    with gr.Accordion("Prompt Log", open=False):
      te_file = gr.Textbox(label="Log File", value="tentacles_all.py-log.txt", visible=False)
      te_log = gr.Markdown("")
      
      with gr.Row().style(equal_height=True):
        te_log_btn = gr.Button("Refresh")
        te_log_del = gr.Button("Reset Log")
        te_log_btn.click(fn=log_writer.r,
                           inputs=te_file,
                           outputs=te_log)
        te_log_del.click(fn=log_writer.delete,
                           inputs=te_file
                           )
  
  with gr.Tab("Charactor Base Prompt Generator"):
    bg_name = gr.Radio(choices=data_new.webui_tweaks("CHARACTER"), label="Charactor Name", value="original")
    bg_locate = gr.Textbox(label="Draw Location")
    bg_cloth = gr.Textbox(label="Charactor Clothes")
    bg_face = gr.Textbox(label="Face Prompt")
    bg_add = gr.Textbox(label="Additional Prompt")
    
    with gr.Accordion("Original Option", open=False):
      gr.Markdown(" > Only Need Choices \"Original\"")
      bg_prompt = gr.Textbox(label="Charactor Prompt")
      bg_lora = gr.Textbox(label="Charactor Lora Model")
      
    bg_prneg = gr.Checkbox(label="Print Negative Prompt + ADetailer Prompt", value=False)
    bg_btn = gr.Button("Generate")
    bg_in = [bg_name, bg_prompt, bg_lora, bg_locate,
             bg_cloth, bg_add, bg_face, bg_prneg]
    bg_out = gr.Markdown("")
    bg_btn.click(fn=bg.Base,
                 inputs=bg_in,
                 outputs=bg_out)
    
    with gr.Accordion("Prompt Log", open=False):
      bg_file = gr.Textbox(label="Log File", value="base_generator.py-log.txt", visible=False)
      bg_log = gr.Markdown("")
      
      with gr.Row().style(equal_height=True):
        bg_log_btn = gr.Button("Refresh")
        bg_log_del = gr.Button("Reset Log")
        bg_log_btn.click(fn=log_writer.r,
                           inputs=bg_file,
                           outputs=bg_log)
        bg_log_del.click(fn=log_writer.delete,
                           inputs=bg_file
                           )
  with gr.Tab("Model Info Viewer"):
    with gr.Tab("Lora Info Viewer"):
      with gr.Row():
        liv_sbox = gr.Textbox(label="Filtering", placeholder="search..")
        liv_search = gr.Button("View Available")
      liv_result = gr.Markdown("Match Search Result")
      
      liv_btn = gr.Button("View")
      
      liv_rmd = gr.Markdown("")
      liv_rhtml = gr.HTML("")
      liv_type = gr.Checkbox(value=True, visible=False)
      liv_btn.click(fn=liv.main,
                    inputs=liv_sbox,
                    outputs=[liv_rmd, liv_rhtml])
      liv_search.click(fn=liv.search_filtering,
                        inputs=[liv_sbox, liv_type],
                        outputs=liv_result)
    with gr.Tab("Checkpoint Info Viewer"):
      with gr.Row():
        civ_sbox = gr.Textbox(label="Filtering", placeholder="search..")
        civ_search = gr.Button("View Filtering Result")
      civ_result = gr.Markdown("\\-")
      
      civ_btn = gr.Button("View Information")
      
      with gr.Blocks():
        civ_rmd_up = gr.Markdown("")
        
        with gr.Row():
          civ_rmd_simply = gr.Markdown("")
          civ_simply_img = gr.Image()
          
        with gr.Row():
          civ_rmd_cute = gr.Markdown("")
          civ_cute_img = gr.Image()
        
        with gr.Row():
          civ_rmd_rnd = gr.Markdown("")
          civ_rnd_img = gr.Image()
          
        civ_rmd_down = gr.Markdown("")
        
      civ_btn.click(fn=civ.view,inputs=[civ_sbox],
                    outputs=[civ_rmd_up,civ_rmd_simply,
                              civ_simply_img, civ_rmd_cute,
                              civ_cute_img, civ_rmd_rnd, civ_rnd_img,
                              civ_rmd_down])
      civ_search.click(fn=civ.search,
                       inputs=[civ_sbox],
                       outputs=[civ_result])
  
  with gr.Tab("Multiple Generating"):
    ext_mode = gr.Radio(label="Extension Mode", choices=["Latent Couple", "MultiDiffusion"])
    
    with gr.Blocks():
      with gr.Blocks():
        with gr.Blocks():
          gr.Markdown("Overall Prompt Data")
          lmg_ov_location = gr.Textbox(label="Location Prompt")
          lmg_ov_quality_prompt = gr.Checkbox(label="Quality Prompt", value=True)
        
        with gr.Blocks():
          gr.Markdown("Charactor 1 Prompt Data")
          lmg_c1_chn =  gr.Radio(choices=data_new.webui_tweaks("CHARACTER"), label="Charactor Name", value="original")
          lmg_c1_cloth = gr.Textbox(label="Charactor Clothing")
          lmg_c1_add = gr.Textbox(label="Additional Prompt")
        
        with gr.Blocks():
          gr.Markdown("Charactor 2 Prompt Data")
          lmg_c2_chn = gr.Radio(choices=data_new.webui_tweaks("CHARACTER"), label="Charactor Name", value="original")
          lmg_c2_cloth = gr.Textbox(label="Charactor Clothing")
          lmg_c2_add = gr.Textbox(label="Additional Prompt")
        
        lmg_btn = gr.Button("Generate")
        lmg_out = gr.Textbox(label="Prompt", placeholder="Outputs Here..")
        
        lmg_btn.click(fn=mg.launch,
                      inputs=[lmg_c1_chn,
lmg_c1_cloth, lmg_c1_add, lmg_c2_chn, lmg_c2_cloth,
lmg_c2_add, lmg_ov_location, lmg_ov_quality_prompt, ext_mode],
                      outputs=lmg_out)
    
  with gr.Tab("Many Type Generator"):
    with gr.Tab("Template Setup Mode"):
      with gr.Tab("Single Mode"):
        gr.Markdown("Create New Template")
        
        with gr.Blocks():
          tgs_type = gr.Textbox(label="Template Name", max_lines=1, placeholder="Template Name")
        
        gr.Markdown("<br>")
        
        with gr.Blocks():
          gr.Markdown("Preview this Template (Optional)")
          with gr.Row():
            tgs_preview_lora = gr.Textbox(label="Character LoRA Name")
            tgs_preview_name = gr.Textbox(label="Character Prompt Name")
          with gr.Row():
            tgs_preview_prom = gr.Textbox(label="Character Prompt")
            tgs_preview_loca = gr.Textbox(label="Draw Location (Location)")
          with gr.Row():
            tgs_preview_face = gr.Textbox(label="Character Face")
            tgs_preview_nega = gr.Textbox(label="Negative Prompt", placeholder="EasyNegative, badhandv5, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1)")
          with gr.Row():
            tgs_preview_upper = gr.Textbox(label="header additional prompt")
            tgs_preview_low = gr.Textbox(label="lower additional prompt")
          with gr.Row():
            tgs_preview_cfg = gr.Slider(1.0, 12.0, step=0.5, value=7.0, label="CFG Scale")
            tgs_preview_sdcp = gr.Textbox(label="SD Checkpoint", value="FuwaFuwaMix V1.5")
          with gr.Row():
            tgs_preview_res = gr.Textbox(label="Resolution", value="512x512", placeholder="{width}x{height}")
          with gr.Row():
            tgs_preview_sampler = gr.Textbox(label="Sampling Method", value="DPM++ SDE Karras", placeholder="Euler a")
            tgs_preview_hires_method = gr.Textbox(label="Hires.fix Method", value="", placeholder="Latent")
          with gr.Column():
            tgs_preview_img = gr.Image(type="pil", source="upload")
            tgs_preview_seed = gr.Number(label="Example Image Seed", placeholder="if Nothing, type \"-1\"")
            
          with gr.Accordion("ControlNet Options", open=False):
            with gr.Column():
              tgs_cn_image = gr.Image(source="upload", type="pil")
              tgs_cn_img2img = gr.Checkbox(label="is img2img", value=False)
            with gr.Row():
              tgs_cn_method = gr.Textbox(label="ControlNet Method", placeholder="e.g. OpenPose")
              tgs_cn_weight = gr.Slider(label="ControlNet Weight", minimum=-1.0, maximum=2.0, step=0.05, value=0.5)
              tgs_cn_mode = gr.Textbox(label="ControlNet Conrtol Mode", placeholder="e.g. balanced")
          
          
              
        gr.Markdown("<br>")
        with gr.Blocks():
          gr.Markdown("Template Base Prompt")
          
          gr.Markdown(
            """Template Prompt all Keyword\n
            \n
            - %LORA% = Character LoRA Name is assigned Here\n
            - %CH_NAME% = Character LoRA name is assigned here\n
            - %CH_PROMPT% = Character Prompt is assigned Here\n
            - %LOCATION% = Draw Location is assigned Here\n
            - %FACE% = Character Face is assigned Here\n
            \n
            and all Prompt Formatter keyword\n
            \n
            <strong>All keyword is Optional</strong>"""
            )
          
          tgs_base = gr.Textbox(label="Template Base Prompt (Requirement)")
          tgs_force_update = gr.Checkbox(label="Force Update (Previous Date is Deleted.)", value=False)
          tgs_save = gr.Button("Save")
          
          tgs_status = gr.Textbox(label="Status")
          tgs_value = gr.Textbox(value="Single", visible=False)
          tgs_save.click(fn=tg.save,
                        inputs=[
                          tgs_value,
                          tgs_type,
                          tgs_preview_lora,
                          tgs_preview_name,
                          tgs_preview_prom,
                          tgs_preview_loca,
                          tgs_preview_face,
                          tgs_preview_img,
                          tgs_preview_seed,
                          tgs_preview_nega,
                          tgs_base,
                          tgs_preview_low,
                          tgs_preview_upper,
                          tgs_cn_image,
                          tgs_cn_method,
                          tgs_cn_weight,
                          tgs_cn_mode,
                          tgs_cn_img2img,
                          tgs_preview_cfg,
                          tgs_preview_sdcp,
                          tgs_preview_res,
                          tgs_preview_sampler,
                          tgs_preview_hires_method,
                          tgs_force_update
                          ],
                        outputs=tgs_status)
      with gr.Tab("Double Mode"):
        gr.Markdown("Create New Template")
        
        with gr.Blocks():
          tmgs_type = gr.Textbox(label="Template Name", max_lines=1, placeholder="Template Name")
        gr.Markdown("<br>")
        
        with gr.Blocks():
          gr.Markdown("Character 1 prompt")
          tmgs_ch1_prompt = gr.Textbox(label="Character 1 Prompt", max_lines=1)
          
          with gr.Accordion("Character 1 Preview Data (Optional)", open=False):
            with gr.Row():
              tmgs_lora1 = gr.Textbox(label="Character LoRA")
              tmgs_name1 = gr.Textbox(label="Character Prompt Name")
            with gr.Row():
              tmgs_prom1 = gr.Textbox(label="Character Prompt")
              tmgs_loca1 = gr.Textbox(label="Location")
            with gr.Row():
              tmgs_face1 = gr.Textbox(label="Character Face")
        gr.Markdown("<br>")
        with gr.Blocks():
          gr.Markdown("Character 2 prompt")
          tmgs_ch2_prompt = gr.Textbox(label="Character 2 Prompt", max_lines=1)
          
          with gr.Accordion("Character 2 Preview Data (Optional)", open=False):
            with gr.Row():
              tmgs_lora2 = gr.Textbox(label="Character LoRA")
              tmgs_name2 = gr.Textbox(label="Character Prompt Name")
            with gr.Row():
              tmgs_prom2 = gr.Textbox(label="Character Prompt")
              tmgs_loca2 = gr.Textbox(label="Location")
            with gr.Row():
              tmgs_face2 = gr.Textbox(label="Character Face")
        gr.Markdown("<br>")

        with gr.Blocks():
          gr.Markdown("Global Prompt")
          gr.Markdown("All is Optional")
          
          tmgs_neg = gr.Textbox(label="Negative Prompt")
          
          with gr.Row():
            tmgs_img = gr.Textbox(label="Preview Image path (from /py)")
            tmgs_seed = gr.Textbox(label="Preview Image Seed")
          
        gr.Markdown("<br>")
        
        tmgs_force_update = gr.Checkbox(label="Force Update (Previous Data is Deleted.)", value=False)
        tmgs_btn = gr.Button("Save")
        
        tmgs_status = gr.Textbox(label="Status")
        
        tmgs_btn.click(
          fn=tmg.save,
          inputs=[tmgs_type, tmgs_ch1_prompt, tmgs_ch2_prompt,
                  tmgs_lora1, tmgs_name1, tmgs_prom1, tmgs_loca1, tmgs_face1,
                  tmgs_lora2, tmgs_name2, tmgs_prom2, tmgs_loca2, tmgs_face2,
                  tmgs_neg, tmgs_img, tmgs_seed, tmgs_force_update],
          outputs=[tmgs_status]
        )
        
    with gr.Tab("Generate Mode"):
      with gr.Tab("Single Mode"):
        gr.Markdown("Type from \"/dataset/template.json\"")
        
        with gr.Blocks():
          tg_type = gr.Dropdown(choices=tg.key_list, label="Target Template", value="Example")
          with gr.Column():
            tg_preview = gr.Button("Preview This Template")
            tg_method_ver = gr.Textbox(label="config Method Version", value="unknown")
            
        gr.Markdown("<br>")
        with gr.Blocks():
          tg_charactor = gr.Radio(choices=data_new.webui_tweaks("CHARACTER"), label="Charactor Name (Template)", value="original")
          with gr.Row():
            tg_lora = gr.Textbox(label="Character LoRA NAME")
            tg_name = gr.Textbox(label="Character Prompt Name")
          with gr.Row():
            tg_prompt = gr.Textbox(label="Character Prompt")
            tg_location = gr.Textbox(label="Draw Location (Location)")
          with gr.Row():
            tg_face = gr.Textbox(label="Character Face Prompt")
          with gr.Row():
            tg_head = gr.Textbox(label="Character header Additional Prompt")
            tg_low = gr.Textbox(label="Character lower Additional Prompt")
        
        gr.Markdown("<br>")
        with gr.Blocks():
          with gr.Accordion("ControlNet", open=False):
            tg_cnimg = gr.Image()
            with gr.Row():
              tg_cnweight = gr.Slider(-1.0, 2.0, step=0.1, label="ControlNet Weight")
              tg_cnmode = gr.Textbox(label="ControlNet Control mode")
            with gr.Row():
              tg_cnmethod = gr.Textbox(label="ControlNet Method")
              tg_cnisimg2img = gr.Checkbox(label="is img2img")
            
          tg_example = gr.Textbox(label="Example Prompt")
          with gr.Accordion("Example Image", open=False):
            tg_img = gr.Image()
            with gr.Row():
              gr.Markdown("Seed")
              tg_seed = gr.Markdown("-1")
          
          with gr.Row():
            tg_cfg = gr.Textbox(label="CFG Scale")
            tg_sdcp = gr.Textbox(label="SD Checkpoint")
            tg_sampler = gr.Textbox(label="Sampling Method")
          with gr.Row():
            tg_hiresmethod = gr.Textbox(label="Hires.fix Resolution")
            tg_res = gr.Textbox(label="Resolution")
          
          gr.Markdown("<br>")
          tg_output = gr.Textbox(label="Prompt")
          tg_out_neg = gr.Textbox(label="Negative")
          
          gr.Markdown("<br>")
          tg_btn = gr.Button("Generate")
          
        tg_preview.click(fn=tg.template_get, inputs=tg_type, 
                        outputs=[tg_lora, tg_name, tg_prompt,
                                tg_location, tg_face, tg_example, tg_img, tg_seed,
                                tg_method_ver, tg_cnimg, tg_cnweight, tg_cnmode,
                                tg_cnisimg2img, tg_cnmethod, tg_cfg, tg_sdcp, tg_res,
                                tg_sampler, tg_hiresmethod, tg_head, tg_low])
        tg_btn.click(fn=tg.template_gen,
                    inputs=[tg_type, tg_charactor, tg_face, tg_location, tg_low, tg_head],
                    outputs=[tg_output, tg_out_neg])
      with gr.Tab("Double Mode"):
        gr.Markdown("Type from \"/dataset/multi_template.json\"")
        
        with gr.Blocks():
          tmg_type = gr.Dropdown(choices=tmg.key_list, label="Target Template", value="Example")
          tmg_preview = gr.Button("Preview This Template")
        gr.Markdown("<br>")
        
        with gr.Blocks():
          with gr.Accordion("Character 1 (Upper / Left)", open=False):
            tmg1_ch = gr.Radio(choices=data_new.webui_tweaks("CHARACTER"), label="Charactor Name (Template)", value="original")
            with gr.Row():
              tmg1_lora = gr.Textbox(label="Character LoRA Name")
              tmg1_character = gr.Textbox(label="Character Prompt Name")
            with gr.Row():
              tmg1_prompt = gr.Textbox(label="Character Prompt")
              tmg1_location = gr.Textbox(label="Draw Location")
            with gr.Row():
              tmg1_face = gr.Textbox(label="Character Face")
              with gr.Column():
                tmg1_add = gr.Textbox(label="Additional Prompt")
                tmg1_add_head = gr.Checkbox(label="Additional Prompt to Header", value=False)
          gr.Markdown("<br>")
          with gr.Accordion("Character 2 (Down / Right)", open=True):
            tmg2_ch = gr.Radio(choices=data_new.webui_tweaks("CHARACTER"), label="Character Name (Template)", value="original")
            with gr.Row():
              tmg2_lora = gr.Textbox(label="Character LoRA Name")
              tmg2_character = gr.Textbox(label="Character Prompt Name")
            with gr.Row():
              tmg2_prompt = gr.Textbox(label="Character Prompt")
              tmg2_location = gr.Textbox(label="Draw Location")
            with gr.Row():
              tmg2_face = gr.Textbox(label="Character Face")
              with gr.Column():
                tmg2_add = gr.Textbox(label="Additional Prompt")
                tmg2_add_head = gr.Checkbox(label="Additional Prompt to Header", value=False)
          #
        gr.Markdown("<br>")
        with gr.Blocks():
          tmg_example = gr.Textbox(label="Preview Prompt")
          with gr.Accordion("Preview Image", open=False):
            tmg_img = gr.Image()
            with gr.Row():
              gr.Markdown("Seed: ")
              tmg_seed = gr.Markdown("-1")
          gr.Markdown("<br>")
          tmg_output_prompt = gr.Textbox(label="Prompt")
          tmg_output_negative = gr.Textbox(label="Negative Prompt")
          
          gr.Markdown("<br>")
          tmg_generate = gr.Button("Generate")
        
        tmg_preview.click(
          fn=tmg.preview,
          inputs=[tmg_type],
          outputs=[tmg1_lora, tmg1_character, tmg1_prompt,
                  tmg1_location, tmg1_face,
                  tmg2_lora, tmg2_character, tmg2_prompt,
                  tmg2_location, tmg2_face,
                  tmg_example, tmg_img, tmg_seed
                  ]
        )
        tmg_generate.click(
          fn=tmg.generate,
          inputs=[tmg_type, tmg1_ch, tmg1_location,
                  tmg1_face, tmg1_add, tmg1_add_head,
                  
                  tmg2_ch, tmg2_location,
                  tmg2_face, tmg2_add, tmg2_add_head],
          outputs=[tmg_output_prompt, tmg_output_negative]
        )
        
  with gr.Tab("Data Opener"):
    with gr.Column(visible=False):
      do_return_mode = gr.Textbox(value="WebUI")
      
    gr.Markdown("More Visualize Stable-Diffusion (or CivitAI) Output Generation Data")
    gr.Markdown("Supported Extension\n\
                - ADetailer\n\
                - (Upcoming) ControlNet\n\
                - (Upcoming) Hires.fix")
    with gr.Accordion("Generation Data", open=True):
      do_indata = gr.Textbox(lines=2, placeholder="Paste Generation Data Here..")
    
    do_btn = gr.Button("Open")
    
    gr.Markdown("<br>")
    with gr.Blocks():
      with gr.Row():
        do_cp = gr.Textbox(label="Checkpoints", placeholder="AnythingV3")
        do_cs = gr.Slider(0, 20, label="Clip Skip", value=2)
      gr.Markdown("<br>")
      do_pr = gr.Textbox(label="Prompt", placeholder="Prompt is Here!")
      do_neg = gr.Textbox(label="Negative", placeholder="EasyNegative?")
      
      with gr.Row():
        do_sr = gr.Textbox(label="Sampling Method", placeholder="Euler a")
        do_ss = gr.Slider(0, 125, label="Sampling Steps", value=24)
      
      with gr.Row():
        do_w = gr.Slider(0, 2048, label="Width", value=512)
        do_h = gr.Slider(0, 2048, label="Height", value=768)
        do_res = gr.Textbox(label="Resolution", placeholder="(512×768)")
      
      with gr.Row():
        do_se = gr.Textbox(label="Seed", placeholder="-1")
        do_cfg = gr.Slider(0, 15, step=0.5, label="CFG Scale", value=7)
      
      do_time = gr.Textbox(label="Creation Date: 0000-00-00")
      
    do_btn.click(fn=data.get_data,
                 inputs=[do_indata, do_return_mode],
                 outputs=[do_cp, do_pr, do_neg, do_res, do_se, do_cfg, do_cs, do_ss, do_sr, do_time, do_w, do_h])
  with gr.Tab("Dataset"):
    with gr.Tab("Basic Generation Data"):
      gr.Textbox(label="Negative Prompt",
                value=data.basic_negative)
      gr.Textbox(
        label="ADetailer Prompt",
        value = data.basic_adetailer_p
      )
      gr.Textbox(
        label="ADetailer Negative",
        value= data.basic_adetailer_neg
      )
  with gr.Tab("Database Setup"):
    with gr.Tab("LoRA Data"):
      with gr.Blocks():
        db_lora_name = gr.Textbox(label="WebUI Name", placeholder="", max_lines=1)
      gr.Markdown("<br>")
      with gr.Blocks():
        with gr.Column():
          db_lora_trigger_lora = gr.Textbox(label="LoRA Trigger (set lora weight to 1.0 (for LoRA weight controller))", placeholder="(e.g. <lora:luna_original007:1.0>)")
          db_lora_trigger_word = gr.Textbox(label="LoRA Trigger Word", placeholder="(e.g. luna07)")
          db_lora_optional_word = gr.Textbox(label="LoRA Optional Word", placeholder="(e.g. (light blue hair), light purple hair, white hair, multicolored hair, blue eyes, blush, hair between eyes, straight hair, small twintale, 14 years old, cat ears, blue light)")
      gr.Markdown("<br>")
      with gr.Blocks():
        with gr.Column():
          db_lora_status = gr.Textbox(label="Status")
          db_lora_force_update = gr.Checkbox(label="Force Update (Previous data is delete.)")
        gr.Markdown("<br>")
        db_lora_generate = gr.Button("Save")
        db_lora_load = gr.Button("Load")
        
        db_lora_generate.click(
          fn=dbs.lora_data.save,
          inputs=[
            db_lora_name, db_lora_trigger_lora, db_lora_trigger_word,
            db_lora_optional_word, db_lora_force_update],
          outputs=[db_lora_status]
        )
        db_lora_load.click(
          fn=dbs.lora_data.load,
          inputs=[db_lora_name],
          outputs=[
            db_lora_name, db_lora_trigger_lora, db_lora_trigger_word,
            db_lora_optional_word, db_lora_status]
        )
if __name__ == "__main__":
  preprocessing()
  itrmain.launch(inbrowser=False, server_port=25566)