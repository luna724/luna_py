from typing import List, Tuple, Literal, AnyStr
import re
import os

from modules.generate_util import get_lora_list
from modules.manage_keybox import use_keybox
from modules.shared import DB_PATH, language, all_passkeys
from modules.config.get import cfg
from modules.lib import get_keys_from_dict, get_keys_from_list, time_takens, error_handling_helper, prompt_special_words, multiple_replace

def prompt_resizer(prompt:str="AnyPrompt", target_character:str="AnyLoRAKey", prompt_ver:tuple=("v3", 3), lora_data:Tuple[float, bool]=(0.75, False, "Header", "Lower", "Face", "Face2", "Location", "Location2", "Cloth", "Cloth2", "Accessory", "Other", "Variable1", "Variable2", "Variable3", "Variable4", "Variable5~10"), ce_mode:bool=False) -> str:
  """Resize the prompt.
  this function build for easy update. 
  
  lora_data: weight, hasextend, header, lower are required.
  other are optional.
  """
  InstaTimer = time_takens()
  InstaTimer.start()
  InstaTimer.wrap(r"Started resizing.. ({})")
  
  def instance_checker(x:str="AnyPrompt") -> str:
    """instance checking."""
    if isinstance(x, (str)):
      return x
    else:
      raise RuntimeError(f"This instance type is not supported in prompt_resizer.\nobtained_value: {x}")
    
  
  def same_checker(text:str="Target", trigger:str="TriggerForStartswith", mode:Literal["starts", "ends"]="starts", bool_mode:bool=False) -> (int | bool):
    """bool_mode: returns bool
    check up, how many characters match the first character
    """
    same = 0
    if mode=="starts":
      while text.startswith(trigger):
        same += 1
        
        try:  
          text = text[len(trigger):]  # triggerの文字数分を削除して次の部分をチェック
        except IndexError:
          break
    elif mode=="ends":
      while text.endswith(trigger):
        same += 1
        
        try:
          text =  text[:(len(text) - len(trigger))]
        
        except IndexError:
          break
    
    if bool_mode and same > 0:
      return True
    elif bool_mode:
      return False
    
    return same
  
  def splitter(x:str="AnyPrompt", stripping_target:(List[AnyStr] | Tuple[AnyStr])=prompt_special_words) -> List[Tuple[str, float]]:
    """split prompt each the words. (splitted by comma)
    return data format:
    [("prompt_words", weight:List[float] | float, spec:Dict[str: int]), ...]
    """
    return_data = []
    
    splitted = [
      x.strip() for x in x.split(",")
    ]
    
    finalized = []
    for n in splitted:
      # (), [] のチェック 存在する場合、spec に追加
      eq1 = same_checker(n, "(")
      eq2 = same_checker(n, ")")
      eq3 = same_checker(n, "[")
      eq4 = same_checker(n, "]")
      
      e = "ends"
      eq5 = same_checker(n, "(", e)
      eq6 = same_checker(n, ")", e)
      eq7 = same_checker(n, "[", e)
      eq8 = same_checker(n, "]", e)
      
      spec = {str(k): int(v) for k, v in locals().items() if k.startswith("eq") and isinstance(v, (int, float))}
      
      # weightの摘出
      for srp in stripping_target:
        n = n.strip().strip(srp)
      
      weights = re.findall(r":(\d*\.\d+)", n)
      print("weights: ", weights)
      weight = []
      if len(weights) > 0:
        for w in weights:
          if isinstance(w, (str, int, float)):
            if isinstance(w, str):
              w = float(w)
            else:
              raise ValueError(f"w: {w}")
          else:
            w = float(w)
          weight.append(w)
      else:
        weight = [1.0]
      
      # weight の平均値を取得
      if cfg.use_average_weights:
        v=0
        for w in weight:
          v += w
        weight = v / len(weight)
      
      # weight を削る (<lora: 出ない場合)
      if n.count("<lora:") < 1:
        n = re.sub(r"(:\d*.\d+)", "", n, count=1)
      
      # フォーマット
      data = (
        n, weight, spec 
      )
      return_data.append(data)
    return return_data
  
  
  def applicate_eq(x:str="AnyWord", eq:dict={"eq1": 0}) -> str:
    for q, count in eq.items():
      if count < 1:
        continue
      elif q in ["eq4", "eq8"]:
        i = "]"
      elif q in ["eq2", "eq6"]:
        i = ")"
      elif q in ["eq3", "eq7"]:
        i = "["
      if q in ["eq1", "eq5"]:
        i = "("
      i *= count
      if q in ["eq1", "eq2", "eq3", "eq4"]:
        x = f"{i}{x}"
      else:
        x = f"{x}{i}"
    return x

    
  def resize_words(word:Tuple[str, (List[float] | float), dict]) -> str:
    """
    Resize words. 
    from splitter() data format (Tuple)
    """
    # 初期化 / UnboundLocalError の回避
    isLoRA = False
    isKey = False
    isInternalKey = False
    isPassKey = False
    
    weight = word[1]
    eqs = word[2]
    word:str = word[0]
    
    # LoRAの場合のチェック
    if "<lora:" in word:
      isLoRA = True
    
    # キーワードの場合
    if word.startswith("$") and same_checker(word, "$") == 1:
      isKey = True
    if word.startswith("%") and word.endswith("%"):
      isKey = True
    if word in ["$LORA", "$NAME", "$PROMPT", "$FACE", "$LOCATION", "$CLOTH", "$CLOTH2", "$ACCESSORY", "%LORA%", "%CH_NAME%", "%CH_PROMPT%", r"%FACE%", "%LOCATION%"]:
      isInternalKey = True
    if word.startswith("#") and word in all_passkeys:
      isPassKey = True
    
    # 基礎処理
    # Weight の検出 -> 再処理
    if not isinstance(weight, list):
      weight = f":{weight}"
    else:
      wtext = ""
      for w in weight:
        wtext += f":{w}"
      weight = wtext
    if not isLoRA and not isKey and not isInternalKey and not isPassKey:
      # ただのプロンプトの場合、Weightと eq を適用しパス
      if not weight == ":1.0":
        word = word+weight
      prompt = applicate_eq(word, eqs)
      return prompt
    elif isLoRA:
      # 同じ動作
      # prompt = word+weight
      prompt = applicate_eq(word, eqs)
    elif isPassKey:
      # 実行元に託す
      return word
    elif isInternalKey:
      # 処理
      if word in ["$LORA", "$NAME", "$PROMPT", "$FACE", "$LOCATION", "$CLOTH", "$CLOTH2", "$ACCESSORY"]:
        return word
      
      # 旧式の変換
      if word in ["%LORA%", "%CH_NAME%", "%CH_PROMPT%", r"%FACE%", "%LOCATION%"]:
        # %WORD% -> $WORD
        if word in ["%CH_NAME%", "%CH_PROMPT%"]:
          if word == "%CH_NAME%":
            return "$NAME"
          else:
            return "$PROMPT"
        
        word = word.strip("%")
        return "$"+word
    elif isKey:
      # キーボックスの場合
      return use_keybox(word)
    
    else:
      errfile = error_handling_helper(locals(), __name__)
      raise ValueError(f"Unknown Exception.\nvariables save at {errfile}")
    
  
  def rs_replace(text:str) -> str:
    if text == "":
      return ""
    else:
      return text+","
  
  
  InstaTimer.wrap(r"functions defined.")
  
  
  prompt_piece = []
  prompts = []
  for tpl in splitter(instance_checker(prompt)):
    prompt_piece.append(
      resize_words(tpl)
    )
  
  _, lora_id, lora_name, lora_prompt, lora_extend = get_lora_list("manual", True, target_character)
  for p in prompt_piece:
    if p == "#PASS":
      continue
    prompts.append(p)
  
  p = ""
  for x in prompts:
    if x is None:
      print("[dev]: x is None! (prompt_resize.py ln241) prompts: ", prompts)
    
    p += x+", "
  p.strip(", ")
  
  # extend
  if lora_data[1]:
    lora_prompt += ", "+lora_extend
    lora_prompt = lora_prompt.strip(", ")
  header = lora_data[2]
  lower = lora_data[3]
  
  p = multiple_replace(
        p, [(
          "$LORA", lora_id
        ), (
          "$NAME", lora_name
        ), (
          "$PROMPT", lora_prompt
        )
          ]
      )
  if ce_mode:
    return p
  
  # 2 opts
  face, location = get_keys_from_list(
    lora_data, [4, 6], "$$$"
  )
  p = multiple_replace(
    p, [(
      "$FACE,", rs_replace(face)
    ), (
      "$LOCATION,", rs_replace(location)
    )]
  )
  
  # v3.0.4 or above
  # Header & Lower
  if prompt_ver[1] >= 4:
    if p.count("$$H") > 0:
      p = p.replace("$$HEADER", header)
    else:
      p = header+p
    if p.count("$$L") > 0:
      p = p.replace("$$LOWER", lower)
    else:
      p = p+lower
  
  else:
    p = header+p+lower
  
  # v3.0.5 or above
  # 6 prompt opts
  if prompt_ver[1] >= 5:
    face2, location2, cloth, cloth2, accessory, other = get_keys_from_list(
      lora_data, [5, 7, 8, 9, 10, 11], "$$$"
    )
    p = multiple_replace(
      p, [(
        "$CLOTH,", rs_replace(cloth)
      ), (
        "$CLOTH2,", rs_replace(cloth2)
      ), (
        "$FACE2,", rs_replace(face2)
      ), (
        "$LOCATION2,", rs_replace(location2)
      ), (
        "$ACCESSORY,", rs_replace(accessory)
      ), (
        "$OTHER,", rs_replace(other)
      )]
    )

  