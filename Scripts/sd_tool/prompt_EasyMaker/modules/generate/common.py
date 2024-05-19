from lunapy_module_importer import Importer, Importable
from LGS import jsoncfg
from typing import *
import os
import gradio as gr

collectorTypes = Importer("modules.types", isTypes="collector")

class obtain_lora_list(collectorTypes):
  def __init__(self):
    super().__init__()
    self.cfg_root = super().get_data_path()
  
  def initialize(self):
    self.lora_raw = jsoncfg.read(
      os.path.join(self.cfg_root, "lora_template.json")
    )
  
  def manual(self, parse:bool=False, name:str=None, method:Literal["v3", "v4.0"]="v3") -> Tuple[str, str, str, str, str] | List[str]:
    self.initialize()
    rtl = list(self.lora_raw.keys())
    
    if parse:
      if not name in rtl:
        raise ValueError(f"Failed. {name} isn't in lora_list")
      data = self.lora_raw[name][1]
      
      if method == "v3":
        return name, data["lora"], data["name"], data["prompt"], data["extend"]
      elif method == "v4.0":
        return name, data["lora"], data["name"], data["prompt"], data["extend"], None
      
    
    return rtl
  
  def full(self) -> dict:
    self.initialize()
    return self.lora_raw
  
  def update(self) -> dict:
    self.initialize()
    return gr.update(choices=list(self.lora_raw.keys()))
  
  def only_lora(self) -> List[Tuple[str, str, str]]:
    self.initialize()
    return [
      (self.lora_raw[x][1]["lora"], x, self.lora_raw[x][1]["name"])
      for x in list(self.lora_raw.keys())
    ]

class _generate_common:
  obtain_lora_list = obtain_lora_list()
  

class generate_common(Importable):
  def __init__(self):
    return
  def __call__(self, **kwargs):
    return _generate_common