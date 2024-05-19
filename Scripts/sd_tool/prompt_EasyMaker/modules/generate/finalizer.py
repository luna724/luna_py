from lunapy_module_importer import Importable, Importer
from typing import *
import re

#generatorTypes = Importer("modules.types", isTypes="generator")
class _finalizer:
  def __init__(self):
    self.generate_common = Importer("modules.generate.common")
    self.lib = Importer("modules.lib")
    self.config = Importer("modules.config.get")
    self.get_lora = self.generate_common.obtain_lora_list
    self.getAny = {
      "%LORA%|$LORA|$$LORA": "?AnyLoRA",
      "%CH_NAME%|$NAME|$$NAME": "?AnyName",
      "%CH_PROMPT%|$PROMPT|$$_PROMPT": "?AnyPrompt",
      "$$EXTEND": "?AnyExtend",
      "$$_STYLE": "?AnyStyle"
    }
    self.script_word = ["#PASS"]
  @staticmethod
  def convert_weight(piece:str, weight:float | int) -> str:
    weights = re.findall(r":(\d*\.\d+)", piece)
    if len(weights) >= 1:
      w = weights[0]
    else:
      return piece
    
    return piece.replace(w, weight, 1)
  
  def convert_method_to_any_version(self, prompt:str, updateTo: Literal["v4", "v3-stable"]="v3-stable") -> str:
    """制約:
    入力に必要な型
    1. キーはウェイトを持っていない
    2. キーは単語ごとに区切られている
    
    返り値の規則性
    1. プロンプトをワードごとに切り、x, ... の型で返す
    """
    converting = []
    for i, value in enumerate(prompt.split(",")):
      item = None
      value = value.strip()
      for any, v in self.getAny.items():
        if value in any.split("|"):
          item = v
        else:
          continue
      if item is None:
        continue
      
      converted = ver[item]
      converting.append((i, converted))
    
    prompts = [x.strip() for x in prompt.split(",")]
    for (i, t) in converting:
      prompts[i] = t
    
    prompt = ""
    for x in prompts:
      prompt += f"{x}, "
    return prompt.strip(", ")
  
  
  def update_legacy_method(self, prompt:str, updateTo:Literal["v4", "v3-stable"]="v3-stable") -> str:
    """制約:
    入力に必要な型
    1. キーはウェイトを持っていない
    2. キーは単語ごとに区切られている
    
    返り値の規則性
    1. プロンプトをワードごとに切り、x, ... の型で返す
    """
    updateList = {
      "v3-stable": {
        "?AnyLoRA": "$LORA",
        "?AnyName": "$NAME",
        "?AnyPrompt": "$PROMPT",
        "?AnyExtend": "",
        "?AnyStyle": ""
      },
      "v4": {
        "?AnyLoRA": "$$LORA",
        "?AnyName": "$$NAME",
        "?AnyPrompt": "$$_PROMPT",
        "?AnyExtend": "$$EXTEND",
        "?AnyStyle": "$$_STYLE"
      }
    }
    
    ver = updateList[updateTo]
    converting = []
    for i, value in enumerate(prompt.split(",")):
      item = None
      value = value.strip()
      for any, v in self.getAny.items():
        if value in any.split("|"):
          item = v
        else:
          continue
      if item is None:
        continue
      
      converted = ver[item]
      converting.append((i, converted))
    
    prompts = [x.strip() for x in prompt.split(",")]
    for (i, t) in converting:
      prompts[i] = t
    
    prompt = ""
    for x in prompts:
      prompt += f"{x}, "
    return prompt.strip(", ")
  
  @staticmethod
  def delete_duplicate_commas(prompt:str) -> str:
    styling = [", , ", ",,"]
    while any(s in prompt for s in styling):  # stylingのいずれかがpromptに含まれる限りループ
      for s in styling:
        if s in prompt:
          prompt = prompt.replace(s, ", ")
    return prompt
  
  def applicate_lora_template(self, prompt, template_name, weight, methodVer:Literal["v3-stable", "v4-StylingUpdate"]="v3") -> str:
    _, lora, name, ch_prompt, extend, style = self.get_lora.manual(True, template_name, "v4.0")
    weight_lora = self.convert_weight(lora, weight[0])
    
    # convert to Trigger list
    if weight[1] == 1.0:
      pass
    else:
      name = f"{name}:{weight[1]}"
    keyValue = [
      ("$LORA", lora), ("$NAME", name), ("$PROMPT", ch_prompt)
    ]
    
    # update methodVer
    if methodVer != "v3-stable":
      keyValue.append(("?AnyExtend", extend),("?AnyStyle", style))
    
    # 適用
    p = self.lib.multiple_replace(prompt, keyValue)
    return p, ((lora, weight_lora), name, ch_prompt, extend, style)
  
  def applicate_keyword(self, prompt):
    return prompt
  
  def finalize(self, prompt:str, methoddata: tuple | None = None, **kwargs):
    """ args information
    methodData:
    (変換対象のテンプレ, (LoRAのweight, nameのweight), )
    
    kwargs:
      1. high-quality template (hqt:bool)
    """
    version = self.config.get_spec_value("script_version.call_api.finalizer")
    prompt = self.delete_duplicate_commas(
                self.applicate_keyword( # update, applicate lora, applicate keyword, delete comma の順で処理
                  self.applicate_lora_template(
                    #self.update_legacy_method(prompt, version),
                      prompt,
                      methoddata[0], methoddata[1], version)[0]))
    
    prompts = []
    for p in prompt.split(","):
      p = p.strip()
      if p in self.script_word:
        continue
      
      prompts.append(p)
    
    item = ""
    for p in prompts:
      item += f"{p}, "
    item = item.strip(", ")
    
    get_value = self.lib.get_value
    # kwargs の解析
    hqt:bool = get_value(kwargs, "hqt", False)
    """High-quality template: クオリティを上げるためのテンプレを提供。 promptの一番最後に代入される"""
    
    if hqt:
      item += self.config.get_spec_value("user_variable.prompt.hqt")
    
    return item


class Finalizer(Importable):
  def __call__(self, **kwargs):
    return _finalizer()