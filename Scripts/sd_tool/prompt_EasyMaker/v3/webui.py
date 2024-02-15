import gradio as gr
import os
import mimetypes
import sys
import subprocess
import importlib.util
import importlib
import logging
from typing import *

## code by. AUTOMATIC1111 / Stable-Diffusion-WebUI
from a1111_ui_util import *

## Prompt Template
from modules.generate import get_template
from modules.generate import generate as template_generate, example_view
from modules.generate_util import get_lora_list
from modules.character_exchanger import character_exchanger
from modules import make_prompt_template, delete_prompt_template

## Lora Template
from modules import manage_lora_template

## Other
import preprocessing
import modules.shared as shared
import modules.regional_prompter as rp
from modules.misc import modify_database, get_js, parse_parsed_arg
from modules.lib import browse_file, show_state_from_checkbox
from javascript.reload_js import reload_js
from modules.lib_javascript import *

## LGS
import LGS.misc.nomore_oserror as los
import LGS.misc.jsonconfig as jsoncfg

# some variable
ui_path = os.path.join(shared.ROOT_DIR, "modules", "ui")
rootID_list = ["generate", "manage_template", "MT/define",
              "MT/delete", "MT/restore", "manage_config"]
load_js = {
  # "key": javascript_function
  "overall": javascript_overall
}

# logger
logging.basicConfig(filename="./script_log/latest.log", encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(filename="./script_log/latest_warn.log", encoding='utf-8', level=logging.WARN)

# Tab Class
class UiTabs: # this code has inspirated by. ddpn08's rvc_webui
  PATH = ui_path
  
  def __init__(self, path):
    self.filepath = path
    self.rootpath = UiTabs.PATH
    pass
  
  def variable(self) -> Tuple[str]:
    """ return tab_title"""
    return ("Tab_Title")
  
  def index(self) -> int:
    """ return ui's index """
    return 0
  
  def get_ui(self) -> list:
    tabs = []
    files = [file for file in os.listdir(self.child_path) if file.endswith(".py")]

    for file in files:
      module_name = file[:-3]
      module_path = os.path.relpath(
        self.child_path, UiTabs.PATH 
      ).replace("/", ".").strip(".")
      module = importlib.import_module(f"modules.ui.{module_path}.{module_name}")
      
      attrs = module.__dict__
      TabClass = [
        x for x in attrs.values() if type(x) == type and issubclass(x, UiTabs) and not x == UiTabs
      ]
      if len(TabClass) > 0:
        tabs.append((file, TabClass[0]))
      
    tabs = sorted([TabClass(file) for file, TabClass in tabs], key= lambda x: x.index())
    return tabs
  
  def ui(self, outlet: Callable):
    """ make ui data 
    don't return """
    pass
  
  # def has_child(self):
  #   return [rootID, child_rel_import_path, importlib's Path]
  
  def __call__(self):
    child_dir = self.filepath[:-3]  #.py を取り除く子ディレクトリの検出
    children = []
    tabs = []
    child_tabs = []
    
    if os.path.isdir(child_dir):
      for file in [file for file in os.listdir(child_dir) if file.endswith(".py")]:
        module_name = file[:-3]
        
        parent = os.path.relpath(
          UiTabs.PATH, UiTabs.PATH
        ).replace(
          "/", "."
        ).strip(".")
        print("parent: ", parent)
        
        children.append(
          importlib.import_module(
            f"modules.ui.{parent}.{module_name}"
          ) # インポートしていたものを children に追加
        )
        
    children = sorted(children, key=lambda x: x.index())
    
    for child in children:
      # 辞書として変数の値を取得
      # このクラスのサブクラスを発見したら最初のものを追加
      attrs = child.__dict__
      tab = [x for x in attrs.values() if issubclass(x, UiTabs)]
      if len(tab) != 0:
        tabs.append(tab[0])
      
    
    
    # これに関してはわからんけど
    # おそらく self.ui に取得したタブの要素を追加
    def outlet():
      with gr.Tabs():
        for tab in tabs:
          tab:UiTabs # for IDE
          with gr.Tab(tab.variable()[0]): # タイトル
            tab() # __call__ を再実行？
                    
    
    return self.ui(outlet)
  
def get_ui() -> List[UiTabs]: # this code too inspirated by. ddPn08's rvc-webui
  tabs = []
  files = [file for file in os.listdir(UiTabs.PATH) if file.endswith(".py")]
  
  for file in files:
    module_name = file[:-3]
    module = importlib.import_module(f"modules.ui.{module_name}")
    
    attrs = module.__dict__
    TabClass = [
      x for x in attrs.values()
      if type(x) == type and issubclass(x, UiTabs) and not x == UiTabs
    ]
    if len(TabClass) > 0:
      tabs.append((file, TabClass[0]))
  
  tabs = sorted([TabClass(file) for file, TabClass in tabs], key=lambda x: x.index())
  return tabs
  
def create_ui(): # this code too inspirated by. ddPn08's rvc-webui
  block = gr.Blocks(title="lunapy / SD - PEM")
  
  with block:
    with gr.Tabs():
      tabs = get_ui()
      for tab in tabs:
        with gr.Tab(tab.variable()[0]):
          tab()
  
  reload_js()
  return block


# Old Method

def old_create_ui():
  # JS
  js = get_js()
  with gr.Blocks(title="lunapy / SD - Prompt EasyMaker") as main_iface:
    reload_js()
    #gr.Code(get_js(), language="javascript", visible=True)
    br = gr.Markdown("<br>")
    splitter = gr.Markdown("---", elem_classes="minimize_splitter_md")
    
    with gr.Tab("Database"):
      with FormColumn():
        dbng = gr.Textbox(label="Negative", value=shared.database("negative"))
        dbap = gr.Textbox(label="ADetailer Positive", value=shared.database("ad_pos"))
        dban = gr.Textbox(label="ADetailer Negative", value=shared.database("ad_neg"))
      br
      br
      with gr.Accordion("Modify values", open=False):
        db_negative = gr.Textbox(label="Negative", value=shared.database("negative"))
        db_ad_pos   = gr.Textbox(label="ADetailer Positive", value=shared.database("ad_pos"))
        db_ad_neg   = gr.Textbox(label="ADetailer Negaitve", value=shared.database("ad_neg"))

        db_btn = gr.Button("Modify")
        db_btn.click(
          fn=modify_database,
          inputs=[db_negative, db_ad_pos, db_ad_neg],
          outputs=[dbng, dbap, dban]
        )
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
              br
              
              with gr.Accordion(label="Secondary Prompt - opts", open=True, visible=True) as secondary_root:
                with gr.Row():
                  lora2 = gr.Dropdown(label="Select Character Template", choices=get_lora_list("manual"))
                  lw2 = gr.Slider(-2.0, 2.0, 0.75, step=0.01, label="LoRA weight")
              
                with FormRow():
                  location2 = gr.Textbox(label="Draw location")
                  face2 = gr.Textbox(label="Character face")
                with FormRow():
                  header2 = gr.Textbox(label="Prompt header")
                  lower2 = gr.Textbox(label="Prompt lower")
              
              out_prompt = gr.Textbox(label="Output Prompt", show_copy_button=True, lines=5)
              out_negative = gr.Textbox(label="Negative", show_copy_button=True, lines=5)
              with FormRow():
                out_ad_prompt = gr.Textbox(label="Output ADetailer", show_copy_button=True, lines=3)
                out_ad_negative = gr.Textbox(label="Output ADetailer Negative", show_copy_button=True, lines=3)
              
              status = gr.Textbox(label="Status", lines=1, interactive=False)
              br
              generate = gr.Button("DISCONTINUED generate")
              ex_generate = gr.Button("Generate with Right Tab's Data")
              generate.click(
                fn=None,
                inputs=[
                  template, lora, location, face, header, lower,
                  lora_weight, use_face_for_adetailer,
                  activate_negative, overall_weight_control,
                  lora2, lw2, location2, face2, header2, lower2
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
                    with gr.Column():
                      ex_characters_data = gr.Textbox(label="Selected Character Template")
                      ex_isextend = gr.Checkbox(label="Character Prompt Extender")
                    ex_lora_weight = gr.Slider(-2.0, 2.0, label="LoRA Weight")
                  with FormRow():
                    ex_lora = gr.Textbox(label="LoRA ID", placeholder="")
                    ex_name = gr.Textbox(label="Character Name", placeholder="")
                  with FormRow():
                    ex_prompt = gr.Textbox(label="Character Prompt", placeholder="")
                  with FormRow():
                    ex_face = gr.Textbox(label="Character Face", placeholder="")
                    ex_location = gr.Textbox(label="Draw Location", placeholder="")
                  with FormRow():
                    ex_header = gr.Textbox(label="Prompt Header", placeholder="")
                    ex_lower = gr.Textbox(label="Prompt Lower", placeholder="")
                  ex_csn = gr.Textbox(label="Creator's Memo", lines=3)
                
                with gr.Blocks():
                  with gr.Accordion("Secondary prompt args", visible=False) as ex_sp_root:
                    with gr.Column():
                      with FormRow():
                        ex_sp_character = gr.Textbox(label="Selected character template")
                        ex_sp_lw = gr.Slider(-2.0, 2.0, label="LoRA Weight", value=0.75, step=0.01)
                      with FormRow():
                        ex_sp_lora = gr.Textbox(label="LoRA ID")
                        ex_sp_name = gr.Textbox(label="Name")
                      with FormRow():
                        ex_sp_prompt = gr.Textbox(label="Character Prompt")
                      with FormRow():
                        ex_sp_face = gr.Textbox(label="Face")
                        ex_sp_location = gr.Textbox(label="Location")
                      with FormRow():
                        ex_sp_header = gr.Textbox(label="Header")
                        ex_sp_lower = gr.Textbox(label="Lower")
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
                
                br
                with gr.Blocks():
                  with gr.Accordion(label="Regional Prompter", open=True, visible=False) as ex_rp_root:
                    ex_rp_mode = gr.Textbox(label="Generation Mode")
                    br
                    
                    with FormRow():
                      ex_rp_use_base = gr.Checkbox(label="use base prompt")
                      ex_rp_use_common = gr.Checkbox(label="use common prompt")
                      ex_rp_use_ncommon = gr.Checkbox(label="use common negative prompt")
                    ex_rp_base_ratio = gr.Textbox(label="Base Ratio")
                    br
                    
                    with FormRow():
                      ex_rp_lora_stop = gr.Slider(0, 150, label="LoRA stop step", step=1)
                      ex_rp_lora_hires = gr.Slider(0, 150, label="LoRA Hires stop step", step=1)
                    
                    with gr.Blocks():
                      with gr.Row():
                        with gr.Column():
                          ex_rp_split_mode = gr.Textbox(label="Main Matrix Mode")
                          ex_rp_div_ratio = gr.Textbox(label="Division Ratio")
                        with gr.Column():
                          ex_rp_res_w = gr.Slider(1, 2048, label="Width")
                          ex_rp_res_h = gr.Slider(1, 2048, label="Height")
                      br
                      with gr.Row():
                        ex_rp_img = gr.Image(label="Sample", type='pil', height=256, width=256)
                        ex_rp_template = gr.Textbox(label="Template", lines=4)
                
                ex_view.click(
                  fn=example_view,
                  inputs=[template],
                  outputs=[
                    ex_characters_data, ex_lora, ex_lora_weight,
                    ex_name,
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
                    ex_rp_root, ex_rp_mode, ex_rp_use_base,
                    ex_rp_use_common, ex_rp_use_ncommon,
                    ex_rp_lora_stop, ex_rp_lora_hires,
                    ex_rp_res_w, ex_rp_res_h,
                    ex_rp_split_mode, ex_rp_div_ratio,
                    ex_rp_base_ratio, ex_rp_img, 
                    ex_rp_template, ex_sp_root,
                    ex_sp_character, ex_sp_lw,
                    ex_sp_lora, ex_sp_name,
                    ex_sp_prompt, ex_sp_face,
                    ex_sp_location, ex_sp_header,
                    ex_sp_lower, ex_method_ver, secondary_root
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
              
              splitter
              with gr.Blocks():
                with gr.Accordion(open=True, label="ADetailer Prompts"):
                  dt_enable_adetailer = gr.Textbox(visible=False, value="")
                  with FormRow():
                    dt_ad_prompt = gr.Textbox(label="Adetailer Prompt", lines=5)
                    dt_ad_negative = gr.Textbox(label="Adetailer Negative", lines=5)
              
              splitter
              with gr.Blocks():
                with gr.Accordion(open=False, label="ControlNet"):
                  dt_enabled_controlnet= gr.Checkbox(label="[TEMPORARY] use ControlNet", value=False)
                  with FormRow():
                    dt_cn_mode = gr.Textbox(label="Control Mode", placeholder="OpenPose")
                    dt_cn_weight = gr.Slider(-1, 2.0, label="ControlNet Weight", value=0.75, step=0.05)
                  dt_cn_image = gr.Image(label="ControlNet Image", type="pil", source="upload")
              
              splitter
              with gr.Blocks():
                with gr.Accordion(open=False, label="Regional Prompter / Latent Couple"):
                  dt_enabled_md = gr.Checkbox(label="[TEMPORARY] use Regional Prompter / Latent Couple", value=False)
                  
                  br
                  with gr.Accordion(open=True, label="Secondary prompt option"):
                    dt_md_second_prompt = gr.Textbox(label="Secondary LoRA applicable prompt", lines=4)
                    br
                    
                    gr.Markdown("")
                    with gr.Row():
                      with gr.Column():
                        with gr.Row():
                          dt_md_ex_characters = gr.Dropdown(
                            choices=get_lora_list("manual"), label="Character template"
                          )
                          dt_md_ex_character_r = ToolButton("\U0001f504", size="sm")
                          dt_md_ex_character_r.click(
                            fn=get_lora_list, inputs=[], outputs=[dt_md_ex_characters]
                          )
                        with gr.Row():
                          dt_md_ex_lora = gr.Textbox(label="LoRA")
                          dt_md_ex_lora_weight = gr.Slider(-2.0, 2.0, value=0.75, step=0.01, label="LoRA Weight")
                        
                        dt_md_ex_name = gr.Textbox(label="Name")
                        dt_md_ex_header = gr.Textbox(label="Header")
                      with gr.Column():
                        dt_md_ex_prompt = gr.Textbox(label="Prompt")
                        dt_md_ex_face = gr.Textbox(label="Face")
                        dt_md_ex_location = gr.Textbox(label="Location")
                        dt_md_ex_lower = gr.Textbox(label="Lower")
                    dt_md_get_face_and_location_from_main = gr.Checkbox(label="Get face and location from first prompt")
                  
                  with FormRow():
                    dt_md_mode = gr.Radio(choices=["Attention", "Latent"], value="Attention", label="Generation Mode")
                  br
                  with FormRow():
                    dt_md_use_base = gr.Checkbox(label="use base prompt", value=False)
                    dt_md_use_common = gr.Checkbox(label="use common prompt", value=False)
                    dt_md_use_common_neg = gr.Checkbox(label="use common negative prompt", value=False)
                  dt_md_base_radio = gr.Number(label="Base Ratio", value=0.2)
                  br
                  with FormRow():
                    dt_md_lora_stop = gr.Slider(0, 150, label="LoRA stop step", value=0, step=1)
                    dt_md_lora_hires = gr.Slider(0, 150, label="LoRA hires stop step", step=1)

                  with gr.Blocks():
                    with gr.Row():
                      with gr.Column():
                        dt_md_split_mode = gr.Radio(choices=["Rows", "Columns", "Random"], value="Columns", label="Matrix Mode")
                        dt_md_split_text = gr.Textbox(label="Division Ratio", value="1:1")
                      with gr.Column():
                        dt_md_res_width = gr.Slider(1, 2048, label="Width", value=768, step=1)
                        dt_md_res_height = gr.Slider(1, 2048, label="Height", value=512, step=1)
                    br
                    dt_md_try_visualize = gr.Button("[WIP] Visualize")
                    dt_md_img = gr.Image(label="Sample", type='pil', height=256, width=256)
                    
                    dt_md_try_visualize.click(
                      fn=rp.visualize,
                      inputs=[dt_md_split_mode, dt_md_split_text,
                              dt_md_res_width, dt_md_res_height,
                              dt_md_use_common, dt_md_use_base,
                              dt_md_base_radio],
                      outputs=[dt_md_img]
                    )
                    
              splitter
              with gr.Blocks():
                with gr.Accordion(open=True, label="Hires.fix"):
                  dt_enabled_h = gr.Checkbox(label="[TEMPORARY] use Hires.fix", value=True)
                  with FormRow():
                    dt_h_sampler = gr.Textbox(label="Hires.fix Sampler", value="R-ESRGAN 4x+ Anime6B")
                    dt_h_steps = gr.Slider(0, 150, step=1,label="Hires Steps", value=8)
                  with FormRow():
                    dt_h_denoise = gr.Slider(0, 1.0, step=0.01, label="Denoising Strength", value=0.45)
                    dt_h_upscl = gr.Slider(1.0, 4.0, value=2.0, step=0.01, label="Upscale")
              
              splitter
              with gr.Accordion(open=True, label="Example Viewer's data"):
                dt_enabled_ex = gr.Checkbox(label="[TEMPORARY] use Example", value=True)
                with FormRow():
                  dt_ex_characters_beta = gr.Dropdown(
                    choices=get_lora_list("manual"), label="Character template")
                  dt_ex_characters_beta_r = ToolButton("\U0001f504", size="sm")
                  dt_ex_characters_beta_r.click(fn=get_lora_list,inputs=[],outputs=[dt_ex_characters_beta])
                with FormRow():
                  with gr.Column():
                    dt_ex_lora = gr.Textbox(label="LoRA", placeholder="in to \"$LORA\"")
                    dt_ex_lora_weight = gr.Number(label="LoRA Weight (for character template. not needed on LoRA)", placeholder=1.0)
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
                with gr.Accordion(open=True, label="Memo"):
                  dt_enabled_csn = gr.Textbox(visible=False, value="")
                  with FormColumn():
                    dt_ex_csn = gr.Textbox(label="Memo for template user", placeholder="", lines=4)
                br
                dt_ex_image = gr.Image(label="Example Image", type="pil", source="upload")
                
              splitter
              with gr.Accordion("Builtins", open=True):
                with FormRow():
                  dt_sampler = gr.Textbox(label="Sampling Method", value="DPM++ 2M Karras", placeholder="Euler a")
                  dt_resolution = gr.Textbox(label="Recommended Image Resolution", value="512x512", placeholder="{width}x{height}")
                with FormRow():
                  dt_clip = gr.Slider(0, 15, label="Clip Skip", value="2")
            
            splitter;splitter
            dt_db_path = gr.Textbox(label="Database Path", interactive=False)
            dt_status = gr.Textbox(label="Status")
            with FormRow():
              dt_overwrite = gr.Checkbox(label="Overwrite previous template (if exists)", value=False)
              dt_save = gr.Button("Save")
            dt_save.click(
              fn=make_prompt_template.save,
              inputs=[
                dt_displayname, dt_prompt, dt_negative, dt_ad_prompt,
                dt_ad_negative, dt_enabled_controlnet, dt_cn_mode,
                dt_cn_weight, dt_cn_image, dt_enabled_h, dt_h_upscl,
                dt_h_sampler, dt_h_denoise, dt_h_steps, dt_resolution,
                dt_sampler, dt_enabled_ex, dt_ex_characters_beta,
                dt_ex_lora, dt_ex_lora_weight,
                dt_ex_name, dt_ex_prompt, dt_ex_isExtend,
                dt_ex_face, dt_ex_location, dt_ex_header, dt_ex_lower,
                dt_ex_image, dt_enabled_csn, dt_ex_csn, dt_clip,
                dt_db_path, dt_overwrite, dt_enabled_md,
                dt_md_mode, dt_md_use_base, dt_md_use_common,
                dt_md_use_common_neg, dt_md_base_radio,
                dt_md_lora_stop, dt_md_lora_hires, dt_md_split_mode,
                dt_md_split_text, dt_md_res_width, dt_md_res_height,
                dt_md_second_prompt, dt_md_ex_characters,
                dt_md_ex_lora,
                dt_md_ex_lora_weight, dt_md_ex_name,
                dt_md_ex_header, dt_md_ex_prompt,
                dt_md_ex_face, dt_md_ex_location,
                dt_md_ex_lower, dt_md_get_face_and_location_from_main
                
                ],outputs=[dt_status])
        
        with gr.Tab("Lora"):
          with gr.Blocks():
            dp_displayname = gr.Textbox(label="display Name")
            
            with FormColumn():
              with FormRow():
                dp_lora = gr.Textbox(label="Lora trigger", placeholder="<lora:ichika3:1.0>")
                dp_name = gr.Textbox(label="Name (into Prompt Template's $NAME)", placeholder="luna")
              
              dp_prompt = gr.Textbox(label="Character Prompt", placeholder="multicolored hair, blue eyes, silver and white hair")
              dp_extend = gr.Textbox(label="Extend (can toggled Character Prompt)", placeholder="light blue light, (lights' refraction:0.25)")

            br
            with FormRow():
              dp_overwrite = gr.Checkbox(label="overwrite", value=False)
          br
          dp_status = gr.Textbox(label="Status")
          dp_save = gr.Button("Save") 
          dp_save.click(
            fn=manage_lora_template.save,
            inputs=[dp_displayname, dp_lora, dp_name,
                    dp_prompt, dp_extend, dp_overwrite],
            outputs=[dp_status]
          )
          
          with gr.Blocks():
            with gr.Accordion("Load template (for modify)"):
              with FormRow():
                dp_loaded_lora = gr.Dropdown(
                  choices=get_lora_list("manual"),
                  label="Target template"
                )
                dp_refresh_loaded = ToolButton("\U0001f504", size="sm")
                dp_refresh_loaded.click(fn=get_lora_list, inputs=[], outputs=[dp_loaded_lora])
              
              br
              dp_load = gr.Button("Load (NOT saved entered data will be lost)")
              dp_load.click(
                fn=manage_lora_template.load,
                inputs=[dp_loaded_lora, dp_displayname, dp_lora, dp_name, dp_prompt, dp_extend],
                outputs=[dp_status, dp_displayname, dp_lora, dp_name,
                        dp_prompt, dp_extend]
              )
              
              
          
      with gr.Tab("Delete"):
        with gr.Tab("Prompt"):
          with FormRow():
            del_p_template = gr.Dropdown(label="Target template", choices=get_template("webui"))
            del_p_template_refresh = ToolButton("\U0001f504")
          br
          with FormColumn():
            with FormRow():
              del_p_no_backup = gr.Checkbox(label="Backup", value=True)

          br
          del_p_status = gr.Textbox(label="Status")
          del_p_btn = gr.Button("Delete")
          del_p_btn.click(
            fn=delete_prompt_template.delete_selected,
            inputs=[del_p_template, del_p_no_backup], outputs=[del_p_status, del_p_template]
          )
          br
          
          with gr.Accordion("Multimode"):
            with FormRow():
              del_p_multi_select = DropdownMulti(
                label="Target Templates", choices=get_template("webui")
              )
              #del_p_template_refreshs = ToolButton("\U0001f504")
            del_p_multi_btn = gr.Button("Multiple Deletion")
        
          del_p_multi_btn.click(
            fn=delete_prompt_template.delete_multi,
            inputs=[del_p_multi_select, del_p_no_backup], outputs=[del_p_status, del_p_multi_select]
          )
          del_p_template_refresh.click(
            fn=get_template,
            inputs=[],outputs=[del_p_template]
          )
          del_p_template_refresh.click(
            fn=get_template,
            inputs=[],outputs=[del_p_multi_select]
          )
          
        with gr.Tab("Lora"):
          with gr.Blocks():
            with FormRow():
              del_l_template = gr.Dropdown(
                  choices=get_lora_list("manual"),
                  label="Target template"
                )
              del_l_refresh_loaded = ToolButton("\U0001f504", size="sm")
              del_l_refresh_loaded.click(fn=get_lora_list, inputs=[], outputs=[del_l_template])
            
            br
            with FormColumn():
              del_l_no_backup = gr.Checkbox(label="backup", value=True)
            br
          
          with gr.Blocks():
            del_l_status = gr.Textbox(label="Status")
            del_l_btn = gr.Button("Delete")
            del_l_btn.click(
              fn=manage_lora_template.delete,
              inputs=[del_l_template, del_l_no_backup],
              outputs=[del_l_status, del_l_template]
            )
            br
          
          with gr.Blocks():
            with gr.Accordion("Multimode", open=True):
              with FormRow():
                del_l_multi_selected = DropdownMulti(
                  choices=get_lora_list("manual"),
                  label="Target templates"
                )
              del_l_multi_btn = gr.Button("Multiple Deletion")
              del_l_refresh_loaded.click(fn=get_lora_list, inputs=[], outputs=[del_l_multi_selected])
              del_l_multi_btn.click(
                fn=manage_lora_template.multi_delete,
                inputs=[del_l_multi_selected, del_l_no_backup],
                outputs=[del_l_status, del_l_multi_selected]
              )
          
      with gr.Tab("Restore"):
        with gr.Tab("Prompt"):
          with gr.Blocks():
            with FormRow():
              res_p_template = gr.Dropdown(label="Restore target Template Backup data", choices=delete_prompt_template.format_backup_filename(gr_update=False))
              res_p_template_refresh = ToolButton("\U0001f504")
              res_p_template_refresh.click(
                fn=delete_prompt_template.format_backup_filename,
                inputs=[], outputs=[res_p_template]
              )
            br
            gr.Markdown("if \"Advanced Restore\" Enabled, can restore v3.0.2 or above's dict and update it (newer version feature value are into blank)")
            with FormRow():
              res_p_delete_this = gr.Checkbox(label="Delete this data, after restore", value=False)
              res_p_advanced = gr.Checkbox(label="Advanced Restore", value=False)
            with FormRow():
              res_p_overwrite = gr.Checkbox(label="Overwrite previous template (if exist)", value=False)
              res_p_bypass_nd = gr.Checkbox(label="bypass name dupe (append restore time to key and displayName)", value=True)
            with FormRow():
              res_p_only_delete = gr.Checkbox(label="Only Delete backup data (Don't restore data)", value=False)
            
            with InputAccordion(label="Restore from filepath", value=False) as res_p_from_filepath:
              res_p_filepath = gr.Textbox(label="target filepath (.json)", placeholder=os.path.join(shared.ROOT_DIR, "logs", "template_backups", "prompt", "example.json"))
              res_p_file_browse = gr.Button("Browse file")
              res_p_file_browse.click(
                fn=browse_file,
                inputs=[],
                outputs=[res_p_filepath]
              )
            br
            
            with FormColumn():
              res_p_status = gr.Textbox(label="Status")
              res_p_btn = gr.Button("Restore")
            res_p_btn.click(
              fn=delete_prompt_template.restore_selected,
              inputs=[res_p_template, res_p_delete_this, res_p_advanced,
                      res_p_overwrite, res_p_bypass_nd,
                      res_p_from_filepath, res_p_filepath,
                      res_p_only_delete],
              outputs=[res_p_status, res_p_template]
            )
            
            br
            with gr.Accordion("Multimode"):
              res_p_multi_select = DropdownMulti(
                choices=delete_prompt_template.format_backup_filename(gr_update=False),
                label="Restore target Template Backup dates"
              )
              res_p_template_refresh.click(
                fn=delete_prompt_template.format_backup_filename,
                inputs=[], outputs=[res_p_multi_select]
              )
              
              res_p_multi_btn = gr.Button("Multiple Restore")
              res_p_multi_btn.click(
                fn=delete_prompt_template.restore_multi,
                inputs=[res_p_multi_select, res_p_delete_this, res_p_advanced,
                      res_p_overwrite, res_p_bypass_nd, res_p_only_delete],
                outputs=[res_p_status, res_p_multi_select]
              )
        
        with gr.Tab("LoRA"):
          with FormRow():
            res_l_template = gr.Dropdown(label="Restore target Template backup data", choices=manage_lora_template.format_backup_filename(gr_update=False))
            res_l_template_refresh = ToolButton("\U0001f504", size="sm")
            res_l_template_refresh.click(
              fn=manage_lora_template.format_backup_filename,
              inputs=[], outputs=[res_l_template]
            )
          br
          
          with gr.Blocks():
            with FormRow():
              res_l_delete_after = gr.Checkbox(label="Delete this data, after restored", value=False)
              res_l_overwrite = gr.Checkbox(label="Overwrite previous template (if exist)", value=False)
            with FormRow():
              res_l_bypass_nd = gr.Checkbox(label="bypas name dupe (append restore time to key and displayName)", value=True)
              res_l_delete = gr.Checkbox(label="Delete backup data (without restore it)", value=False)
          br
          
          with gr.Blocks():
            with FormColumn():
              res_l_status = gr.Textbox(label="Status")
              res_l_btn = gr.Button("Restore")
              res_l_btn.click(
                fn=manage_lora_template.restore,
                inputs=[res_l_template, res_l_delete_after,
                        res_l_overwrite, res_l_bypass_nd, res_l_delete],
                outputs=[res_l_status, res_l_template]
              )
          br
          
          with gr.Blocks():
            with gr.Accordion("multimode"):
              res_l_multi_selected = DropdownMulti(
                choices=manage_lora_template.format_backup_filename(gr_update=False),
                        label="Selected templates"
              )
              res_l_multi_btn = gr.Button("Multiple Restore")
              res_l_multi_btn.click(
                fn=manage_lora_template.multi_restore,
                inputs=[res_l_multi_selected, res_l_delete_after,
                        res_l_overwrite, res_l_bypass_nd, res_l_delete],
                outputs=[res_l_status, res_l_multi_selected]
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
      
      br
      with gr.Blocks():
        with FormColumn():
          with FormRow():
            ce_strict = gr.Checkbox(label="Strict parse (for multi character lora)", value=False)
            ce_clip = gr.Checkbox(label="auto clip", value=True)
          with FormRow():
            ce_ptdh = gr.Checkbox(label="Exchange to Prompt Template")
        
      ce_run = gr.Button("Exchange")
      ce_run.click(
        fn=character_exchanger,
        inputs=[ce_mode, ce_base, ce_ch, ce_strict, ce_clip, ce_ptdh],
        outputs=[ce_out, ce_info]
      )
  return main_iface

def launch_ui(isloopui:bool=False):
  port = parse_parsed_arg(shared.args.ui_port, None, None)
  ip = parse_parsed_arg(shared.args.ui_ip, None)
  if port:
    port = int(port)
  
  ui = old_create_ui()
  if shared.args.new_ui:
    ui = create_ui()
  
  ui.queue(64).launch()
  return "DONE."
  
  # ui.queue(64)
  # ui.launch(
  #   server_port=port,
  #   inbrowser=shared.args.open_browser,
  #   share=shared.args.share,
  #   server_name=ip
  # )

def start():
  print("Ctrl+C to Terminate")
  mimetypes.init()
  mimetypes.add_type('application/javascript', '.js')
  
  if shared.args.loopui:
    print("[UI]: Starting UI with loopui\nclose this window to Terminate")
    try:
      launch_ui(True)
    except KeyboardInterrupt:
      print("[UI]: Terminated with KeyboardInterrupt")
      if shared.args.dev_restart:
        print("[UI]: Restarting UI with reload..")
        nest = os.path.basename(os.path.realpath(shared.ROOT_DIR))
        cmd = os.path.join(
          nest, "launch_user.bat"
        ) + " " + sys.argv[1:]
        subprocess.Popen(
          cmd
        )
        pass
      else:
        print("[UI]: Restarting UI..")
        start()
        pass
  else:
    launch_ui()
    
  return "Terminated"

if __name__ == "__main__":
  if not os.path.exists(os.path.join(shared.ROOT_DIR, "lscript_alreadyprp.ltx")):
    preprocessing.run()

  print(start())