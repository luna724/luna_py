import gradio as gr
# import WHB_generator as whbgen
# import Masturbation_generator as mastgen
import importlib
import tentacle_clothes as tcgen
import log_writer as log_writer
import simple_generator as data
import tentacles_all as te
import base_generator as bg
import lora_info_viewer as liv
import multiple_generating as mg
import template_generator as tg
import checkpoint_info_viewer as civ

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

with gr.Blocks() as itrmain:
  rld_ui_btn = gr.Button("Reload jsondata",size="sm")
  rld_ui_btn.click(fn=reload_module)
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
    tc_chn = gr.Radio(choices=data.available_name, label="Charactor Name", value="original")
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
    
    te_name = gr.Radio(choices=data.available_name, label="Charactor Name", value="original")
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
    bg_name = gr.Radio(choices=data.available_name, label="Charactor Name", value="original")
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
          lmg_c1_chn =  gr.Radio(choices=data.available_name, label="Charactor Name", value="original")
          lmg_c1_cloth = gr.Textbox(label="Charactor Clothing")
          lmg_c1_add = gr.Textbox(label="Additional Prompt")
        
        with gr.Blocks():
          gr.Markdown("Charactor 2 Prompt Data")
          lmg_c2_chn = gr.Radio(choices=data.available_name, label="Charactor Name", value="original")
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
    with gr.Tab("Single Mode"):
      gr.Markdown("Type from \"/dataset/template.json\"")
      
      with gr.Blocks():
        tg_type = gr.Dropdown(choices=tg.key_list, label="Target Template", value="Example")
        tg_preview = gr.Button("Preview This Template")
      
      gr.Markdown("<br>")
      with gr.Blocks():
        tg_charactor = gr.Radio(choices=data.available_name, label="Charactor Name (Template)", value="original")
        with gr.Row():
          tg_lora = gr.Textbox(label="Charactor LoRA NAME")
          tg_name = gr.Textbox(label="Charactor Prompt Name")
        with gr.Row():
          tg_prompt = gr.Textbox(label="Charactor Prompt")
          tg_location = gr.Textbox(label="Draw Location (Location)")
        with gr.Row():
          tg_face = gr.Textbox(label="Charactor Face Prompt")
          tg_add = gr.Textbox(label="Charactor Additional Prompt")
      
      gr.Markdown("<br>")
      with gr.Blocks():
        tg_example = gr.Textbox(label="Example Prompt")
        with gr.Accordion("Example Image", open=False):
          tg_img = gr.Image()
          with gr.Row():
            gr.Markdown("Seed")
            tg_seed = gr.Markdown("-1")
        gr.Markdown("<br>")
        tg_output = gr.Textbox(label="Prompt")
        tg_out_neg = gr.Textbox(label="Negative")
        
        gr.Markdown("<br>")
        tg_btn = gr.Button("Generate")
        
      tg_preview.click(fn=tg.example_view, inputs=tg_type, 
                      outputs=[tg_lora, tg_name, tg_prompt,
                              tg_location, tg_face, tg_example, tg_img, tg_seed])
      tg_btn.click(fn=tg.template_gen,
                  inputs=[tg_type, tg_charactor, tg_face, tg_location, tg_add],
                  outputs=[tg_output, tg_out_neg])
  
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
itrmain.launch(inbrowser=True, server_port=25566)