from lunapy_module_importer import Importer, Importable
from typing import *
import os
import gradio as gr

generatorTypes = Importer("modules.types", isTypes="generator")
class Templates(generatorTypes):
  def __init__(self):
    super().__init__()
    self.get_templates = self.generate_common.obtain_template_list
    self.get_lora = self.generate_common.obtain_lora_list
  
  @staticmethod
  def get_module_name():
    return "templates-v4"
  
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
    