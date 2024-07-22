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
    "AD_Negative": "ADetailer negative prompt here",
    "NSFW_Prompt": "NSFW prompt here"
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
    "method": "Sampler method",
    "refiner": ["SD Checkpoints", 0.85]
  }
}}

example_lora_template = {"test": [
  "v5",
  {
    "lora": "<lora:example:1.0>",
    "name": "LoRA Main trigger",
    "prompt": "LoRA sub trigger",
    "extend": "LoRA assistant",
    "key": "test",
    "lora_variables": [
      [False, False, ...], #LoRA Variables is Enabled? (1st, 2nd)
      [("Variable1-title", "info1"), ("Variable2-title", "info2"), ...] #LoRA Variable Information (1st, 2nd)
    ] # V5現在、2つまで対応
  }
]}


generatorTypes = Importer("modules.types", isTypes="generator")
class Templates(generatorTypes):
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

  def __init__(self):
    super().__init__()
    self.get_templates = self.generate_common.obtain_template_list
    self.get_lora = self.generate_common.obtain_lora_list
    self.ui_config = self.config.get_spec_value("user_variable.ui.system")
    
    self.selected_template:str = None
    self.selected_lora:str = None
    
    # Template
    self.blank_template = gr.update(interactive=False, label="")
    
    
    # Temporary Variable
    self.lora_template_v5_from_above = ["v5"]
  
  
  class Template:
    """dataclass"""
    def __init__(self, **kwarg):
      for k, v in kwarg:
        setattr(self, k.lower(), v)
    
    def set(self, k:str, v):
      setattr(self, k.lower(), v)
    
    def __call__(self, key:str):
      if hasattr(self, key):
        return getattr(self, key)
      else:
        return None
  
  @staticmethod
  def get_module_name():
    return "templates-v4"
  
  
  def get_example_values(self, template=None) -> Template:
    if template == None:
      template = self.selected_template
    
    # テンプレート v3 以上で有効
    # 現状、V2 より下のテンプレートは SD-PEM v3 でサポート打ち切り
    tmpl, _ = self.get_templates.get_template_value(template)
    value = Templates.Template()

    specify_values_key = [
      # 変数に登録する辞書キーを定義する
      "method_ver", "method_release", "template_key",
      "prompt", "negative", "ad_prompt", "ad_negative", "nsfw_prompt",
      "cn_enabled", "cn_mode", "cn_weight", "cn_image",
      "hires_enabled", "hires_upscale", "hires_sampler", "hires_denoise",
      "hires_steps", "lora", "lora_weight", "has_extend", "faces", "locations",
      "headers", "others", "clip_skip", "example_image", "sdcp",
      "sdvae", "sampler", "sampling_method", "refiner_data"
    ]
    specify_values = [
      # 定義した辞書キーに紐づく値がある位置を定義する
      "Method", "Method_Release", "Key",
      "Values.Prompt", "Values.Negative", "Values.AD_Prompt", "Values.AD_Negative", "Values.NSFW_Prompt",
      "ControlNet.isEnabled", "ControlNet.Mode", "ControlNet.Weight", "ControlNet.Image",
      "Hires.isEnabled", "Hires.Upscale", "Hires.Sampler", "Hires.Denoising",
      "Hires.Steps", "Example.lora", "Example.weight", "Example.extend", "Example.face", "Example.location",
      "Example.Headers", "Example.Other", "Example.clip", "Example.image", "Buildins.model",
      "Buildins.vae", "Buildins.sampler", "Buildins.method", "Buildins.refiner"
    ]
    
    for i, vkey in enumerate(specify_values_key):
      value.set(vkey, 
                self.lib.get_treed_value(
                  tmpl, specify_values[i], None
                ))
    
    return value
  
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
      return [(False, ["", ""]), (False, ["", ""])]

  # Update database
  def change_lora(self, lora) -> tuple:
    """return > """
    rtl = []
    self.selected_lora = lora
    
    # LoRA Changed triggers
    # 1. LoRA Variable showcase
    lvs = self.detect_lora_variable()
    if (lvs[0][0] or lvs[1][0]) and self.ui_config["enable_lora_variable_showcase"]:
      lv = True
    else:
      lv = False
    
    lv1_active = lvs[0][0]
    if lv1_active:
      lv1_infos = lvs[0][1]
      lv1_checkbox = gr.Checkbox.update(
        label=lv1_infos[0], value=False, interactive=True)
      lv1_info = lv1_infos[1]
    else:
      lv1_checkbox = self.blank_template
      lv1_info = ""
    
    lv2_active = lvs[1][0]
    if lv2_active:
      lv2_infos = lvs[1][1]
      lv2_checkbox = gr.Checkbox.update(
        label=lv2_infos[0], value=False, interactive=True
      )
      lv2_info = lv2_infos[1]
    else:
      lv2_checkbox = self.blank_template
      lv2_info = ""
    
    rtl += [gr.update(visible=lv), lv1_checkbox, lv1_info, lv2_checkbox, lv2_info]
    
    # 2. LoRA Example Viewer
    values = self.get_lora.manual(parse=True, name=lora)
    rtl += [
      values[1], values[2], values[3], values[4]
    ]
    
    return tuple(rtl)
    
  def change_template(self, tmpl) -> tuple:
    self.selected_template = tmpl
    rtl = []
    template_value = self.get_example_values(tmpl)
    
    # 1. Compact Example Viewer
    method = template_value("method_ver")
    tmpl_key = template_value("Key")
    tmpl_prompt = template_value("prompt")
    tmpl_negative = template_value("negative")
    rtl += [method, tmpl_key, tmpl_prompt, tmpl_negative]
    
    # 2. LoRA opts Auto-Setting (from Example value)
    lw = template_value("lora_weight")
    has_extend = template_value("has_extend")
    
    rtl += [lw, has_extend]
    
    return tuple(rtl)
  
  def update_tmpl_prompts_ui_values(self, mode:Literal["NSFW_Prompt", "Default"]) -> Tuple[str]:
    """ return tmpl_prompt and tmpl_negative"""
    template_value = self.get_example_values()
    
    if mode == "Default":
      tmpl_prompt = template_value("prompt")
      tmpl_negative = template_value("negative")
      return (tmpl_prompt, tmpl_negative)
    
    elif mode == "NSFW_Prompt":
      nsfw_prompt = template_value("nsfw_prompt")
      tmpl_negative = template_value("negative")
      if nsfw_prompt is None:
        gr.Info("Templates version is too low! (v3.2 and below), if NSFW Prompt saved, your template will automatically update")
        nsfw_prompt = ""
      return (nsfw_prompt, tmpl_negative)
  
  def variables_from_example(self):
    """Button (Get from eaxmple data)'s function
    return tuple(str, ..) (len=8)"""
    tv = self.get_example_values()
    faces = tv("faces")
    locations = tv("locations")
    headers = tv("headers")
    others = tv("others")
    
    return (
      faces[0], faces[1], locations[0], locations[1],
      others[0], others[1], headers[0], headers[1]
    )
  
  def get_prompts_info(self) -> str:
    """ return HTML style.
    information for tmpl_prompts
    """
    return "COMING SOON"
  
  def update_prompt_only(self, new_prompt, new_negative):
    ## TODO: prompt only SAVE System
    gr.Info("updated.")
  
  
  # .change() Methods
  def use_prompt_nsfw_mode(self, slf:bool): # -> Tuple(str, str)
    if slf:
      return self.update_tmpl_prompts_ui_values("NSFW_Prompt")
    else:
      return self.update_tmpl_prompts_ui_values("Default")
    
class _template(Importable):
  def __call__(self, **kwargs):
    return Templates()