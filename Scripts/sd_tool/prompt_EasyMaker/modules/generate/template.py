from lunapy_module_importer import Importer, Importable
from typing import *
import os
import gradio as gr

example_template = {"test": {
  # Method: v4
  "Method": "v4.0.0",
  "Method_Release": 10,
  "Key": "test",
  "Values": {
    "Prompt": "prompt here",
    "Negative": "negative prompt here",
    "AD_Prompt": "ADetailer prompt here",
    "AD_Negative": "ADetailer negative prompt here"
  },
  "ControlNet": {
    "isEnabled": False,
    "Mode": "OpenPose",
    "Weight": 0.75,
    "Image": "path/to/image"
  },
  "Hires": {
    "isEnabled": True,
    "Upscale": 1.5,
    "Sampler": "R-ESRGAN 4x+ Anime6B",
    "Denoising": 0.35,
    "Steps": 6
  },
  "Regional_Prompter": {
    "isEnabled": False,
    "rp_mode": "Matrix",
    "mode": "Attention",
    "base": False,
    "use_common": False,
    "use_ncommon": False,
    "lora_stop": 0,
    "lora_hires_stop": 0,
    "resolution": [512, 512],
    "split_mode": "Columns",
    "split_ratio": "1:1",
    "base_ratio": 0.2,
    "template": ["ADDCOL"],
    "Example": {
      "lora": "LoRA Template",
      "weight": 0.75,
      "extend": False,
      "face": ["1st Face", "2nd Face"],
      "location": ["1st Location", "2nd Location"],
      "Headers": ["Headers", "Lowers"],
      "Other": ["Accessory", "Other"]
    }
  },
  "Example": {
    "lora": "LoRA Template",
    "weight": 0.75,
    "extend": False,
    "face": ["1st Face", "2nd Face"],
    "location": ["1st Location", "2nd Location"],
    "Headers": ["Headers", "Lowers"],
    "Other": ["Accessory", "Other"],
    "clip": 2, # Clip Skip
    "image": "/path/to/image"
  },
  "Buildins": {
    "model": "SD Checkpoints",
    "vae": "SD VAE",
    "sampler": "Sampler",
    "method": "Sampler method"
  }
}}

example_lora_template = {"test": {
  "v5",
  {
    "lora": "<lora:example:1.0>",
    "name": "LoRA Main trigger",
    "prompt": "LoRA sub trigger",
    "extend": "LoRA assistant",
    "key": "test",
    "lora_variables": [
      [False, False], #LoRA Variables is Enabled? (1st, 2nd)
      ["info1", "info2"] #LoRA Variable Information (1st, 2nd)
    ]
  }
}}


generatorTypes = Importer("modules.types", isTypes="generator")
class Templates(generatorTypes):
  def __init__(self):
    super().__init__()
    self.get_templates = self.generate_common.obtain_template_list
    self.get_lora = self.generate_common.obtain_lora_list
    
    self.selected_template:str = None
    self.selected_lora:str = None
    
    # Temporary Variable
    self.lora_template_v5_from_above = ["v5"]
    
  @staticmethod
  def get_module_name():
    return "templates-v4"
  
  
  def show_example_values(self, template=None):
    def resize(x: Any, instance: Any = str) -> Any:
      if x is None:
        return instance()
      else:
        return x
    
    class Tweaking:
      def __init__(self, template: dict):
        self.t = template
      
      def __call__(self, key: str) -> Any:
        try:
          return self.t[key]
        except KeyError:
          return None
        except IndexError:
          return None
        
    rtl = list()
    if template == None:
      template = self.selected_template
    
    # テンプレート v3 以上で有効
    # 現状、V2 より下のテンプレートは SD-PEM v3 でサポート打ち切り
    tmpl, _ = self.get_templates.get_template_value(template)
    
    get = Tweaking(tmpl)

    
  
  def detect_lora_variable(self, lora_template=None):
    # v4 method
    rtl = []
    if lora_template == None:
      lora_template = self.selected_lora
    
    # LoRA テンプレ v5.0 以上で有効 (v2 以下なら IndexError)
    lora = self.get_lora.full()[lora_template]
    method = lora[0]
    
    if method in self.lora_template_v5_from_above:
      lora = lora[1]
      lora_vars = lora["lora_variables"]
      
      lv1, lv2 = tuple(lora_vars[0])
      if lv1:
        rtl.append((True, lora_vars[1][0]))
      if lv2:
        rtl.append((True, lora_vars[1][1]))

      return rtl
    else:
      print("[INFO]: this Template versions too low.")
      return [(False, ""), (False, "")]

  # Update database
  def change_lora(self, lora) -> tuple:
    rtl = []
    self.selected_lora = lora
    
    # LoRA Changed triggers
    # 1. LoRA Variable showcase
    lvs = self.detect_lora_variable()
    if lvs[0][0] or lvs[1][0]:
      lv = True
    else:
      lv = False
      
    rtl += [gr.update(visible=lv), lvs[0][0], lvs[0][1], lvs[1][0], lvs[1][1]]
    
    return tuple(rtl)
    
  def change_template(self, tmpl) -> tuple:
    self.selected_template = tmpl
    rtl = []
    args_example_view = list(
      
    ) 
    
    return tuple(rtl)
  
  
  def v3(self, template,lora_name:str,
  lora_id:str,
  ch_name:str,
  ch_prompt:str,
  location:str,
  face:str,
  header:str,
  lower:str,
  lora_weight:float,
  has_extend:bool,
  adetailer_plus:bool,
  apply_positive:bool,
  apply_negative:bool,
  apply_weight_to_positive:bool,
  apply_weight_to_negative:bool,
  sp_lora_name:str,
  sp_lora_id:str,
  sp_ch_name:str,
  sp_ch_prompt:str,
  sp_location:str,
  sp_face:str,
  sp_header:str,
  sp_lower:str,
  sp_sync_some:bool,
  sp_lora_weight:float,
  sp_has_extend:bool,
  #convert_break_to_template:bool, # beta Function. convert BREAK to Template value (e.g. BREAK -> ADDCOL)
  face2:str,
  location2:str,
  cloth:str,
  cloth2:str,
  accessory:str,
  other:str,
  quality_prompt:bool):
    def r(x:str) -> str:
      return x.strip().strip(",")
  
    if lora_name == "" and lora_id == "":
      print("Catched: lora_name == None and lora_id == None")
      raise gr.Error("LoRAs not selected.")
      
    data, _ = self.get_templates.get_template_value(template)
    _, lora, name, character_prompt, ch_extend = self.get_lora.manual(True, lora_name)
    
    values = data["Values"]
  
    prompt = values["Prompt"]
    negative = values["Negative"]
    ad_prompt = values["AD_Prompt"]
    ad_negative = values["AD_Negative"]
    
    lora , name, character_prompt, location, face = r(lora), r(name), r(character_prompt), r(location), r(face)
    if has_extend and isinstance(ch_extend, str):
      character_prompt += ", "+r(ch_extend)
      
    prompt1 = self.finalizer(
      prompt, template, (lora_weight, 1.0)
    )
    
    # v3.0.3+ Regional Prompter
    rp = data["Regional_Prompter"]["Secondary_Prompt"]
    prompt = rp["prompt"]
    