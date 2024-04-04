import pyperclip
import re
from LGS.misc.jsonconfig import write_text
from datetime import datetime
from typing import * 

from modules.shared import ROOT_DIR, args, language
from modules.generate_util import *
from modules.lib import re4prompt, time_takens, override_print, prompt_special_words, is_exists
from modules.prompt_resize import prompt_resizer

def character_exchanger(mode, prompt, character, strict_check, autoclip, ptdh):
  """this function will be discontinued!!!"""
  
  """
  DISCONTINUED Function.
  new function -> .:character_exchanger
  """
  if not args.local:
    autoclip = False
    print("[CE]: auto clip are supported only local env (if you're in local, launch launch.py with arg \"--local\")")
  
  if pyperclip.paste() != "" and autoclip:
    print("[CE]: clipboard object found. printout..")
    print(pyperclip.paste())

  if ptdh:
    mode = []

  print("[CE]: WARN: mode control is experimental feature")
  # mode: List(Literal["lora", "name", "prompt"])
  
  # 割とシビアにloraを取得 -> $LORA に変換
  prompt_lora = re4prompt(r"(<lora:.*:).*>", prompt)
  ch_lora_list_raw = get_lora_list("only_lora")
  ch_lora_list = []
  
  for x in ch_lora_list_raw:
    #print(x)
    ch_lora_list.append( # <lora:hello:1.0> -> <lora:hello:
      (x[0].split(":")[0] + ":" + x[0].split(":")[1] + ":", x[1], x[2])
    )
    #print("x: ",x[0].split(":"))
  
  target = None
  name = None
  for y in prompt_lora:
    if target != None:
      continue
    for tpl in ch_lora_list:
      if tpl[0] in y:
        print("[CE]: Catched.")
        target = tpl[0]
        key = tpl[1]
        
        if strict_check:
          # tpl[2] = name をもとに re4prompt を使用して name も一致するかチェック
          try:
            namecheck = re4prompt(tpl[2], prompt)
            print(f"[CE]: {len(namecheck)}'s name pattern found.")
            name = namecheck[0]
            target = tpl[0]
            break
          except IndexError as e:
            print(f"[CE]: Not match lora / name = {tpl[0]} / {tpl[2]}")
            continue
        else:
          break
    #else:
      # print(f"Not catched: {y}")
  if strict_check:
    if name == None:
      return "Error: Cannot find Character Lora (please check lora trigger syntax!)", f"Tried: Unknown -> {character}"
    
    print("[CE]: name = ", name)
    
  if target == None:
    return "Error: Cannot find Character Lora (please check lora trigger syntax!)", f"Tried: Unknown -> {character}"
  
  print("[CE]: target: ", target)
  loraname = re.findall(r"<lora:(.*):", target)[0]
  print("[CE]: loraname: ", loraname)
  current_weight = re4prompt(rf"<lora:{loraname}:(.+)>", prompt)[0]
  print(f"[CE]: Detected weight: {current_weight}")
  
  prompt = re.sub(rf"<lora:{loraname}:{current_weight}>", "$LORA", prompt, count=1)
  
  # lora名を使用してキーを特定、その他のデータも取得
  key, _, ch_name, ch_prompt, ch_extend = get_lora_list("manual", True, key)
  
  # 初期化して渡す
  prompt = re.sub(ch_name, "$NAME", prompt, count=1)
  prompt = re.sub(ch_prompt+ch_extend, "$PROMPT", prompt, count=1)
  
  if len(mode) == 3:
    prompt = prompt_character_resizer(
      prompt, current_weight, character
    )
  else:
    rpl, rpn, rpp = prompt_character_resizer(
      prompt, current_weight, character, True
    )
    
    replace_key = []
    
    if "lora" in mode:
      replace_key.append(
        ("$LORA", rpl)
      )
    if "name" in mode:
      replace_key.append(
        ("$NAME", rpn)
      )
    if "prompt" in mode:
      replace_key.append(
        ("$PROMPT", rpp)
      )
    
    prompt = multiple_replace(
      prompt, replace_key
    )
    
    if not ptdh:
      prompt = prompt_character_resizer(
        prompt, current_weight, key
      )
  
  if autoclip:
    print("[CE]: Copied!")
    pyperclip.copy(prompt)
  
  info = f"Detected: {key} -> {character}"
  
  times = datetime.now().strftime("%Y%m%d - %H:%M")
  write_text(
    f"\n\n{times}'s Data\n" + prompt, os.path.join(
    ROOT_DIR, "logs", "character_exchanger.log"
  ), False
  )
  return prompt, info


def new_character_exchanger(mode:list, prompt:str, exchange_to:str, strict:bool, copy:bool, override_lora:bool, advanced_exchange:bool=True, AE_args:str=""):
  """ 
advanced_exchange: characte prompt および extend を単語ごとに変換する。
プロンプト内にばらばらにちりばめられている場合に使用可能
"""
  timer = time_takens()
  timer.start()
  
  #print = override_print().get_func(header="[CE]: ", print_after_build=True)
  lang = language("/ui/generate/exchanger.py", "raw")
  
  # LoRAリストを取得
  lora_list = []
  for x in get_lora_list("only_lora"):
    lora_list.append( # Tuple(<lora:example:, lora_key, lora_name)
      (x[0].split(":")[0]+":"+x[0].split(":")[1]+":", x[1], x[2])
    )
  
  # プロンプトのLORAをすべて摘出
  prompt_loras = re4prompt(r"(<lora:.*:).*>", prompt)
  
  target = None
  name = None
  
  # LoRAリストにマッチするLoRAを name, target に代入
  for lora in prompt_loras:
    for tpl in lora_list:
      if tpl[0] in lora:
        print("Catched.")
        target = tpl[0]
        key = tpl[1]
        
        if strict:
          # name も一致させる
          try:
            prompt_name = re4prompt(tpl[2], prompt)
            name = prompt_name[0]
            target = tpl[0]
            break
          except IndexError:
            continue
        else:
          break
  
  if strict and name == None:
    raise gr.Error(lang["cant_find"])
  
  if target == None:
    raise gr.Error(lang["cant_find"])
  
  loraname = re.findall(r"<lora:(.*):", target)[0]
  weight = re4prompt(rf"<lora:{loraname}:(.*)>", prompt)[0]
  
  prompt = re.sub(rf"<lora:{loraname}:{weight}>", "$LORA", prompt, count=1)
  key, _, name, ch_prompt, extend = get_lora_list("manual", True, key)
  target_key, target_lora, target_name, target_prompt, target_extend = get_lora_list(
    "manual", True, exchange_to
  )
  
  if not advanced_exchange:
    prompt = re.sub(name, "$NAME", prompt, count=1)
    prompt = re.sub(ch_prompt+extend, "$PROMPT", prompt, count=1)
    
  else:
    # 引数の整理
    add_prompt_at_last = is_exists(
      AE_args, "--insert_at_lower (If the number of character prompts to be exchanged > the number of character prompts in the base prompt, the extra character prompts to be exchanged are added to the end of the base prompt)"
    )
    add_prompt_at_last_base_character_prompt = is_exists(
      AE_args, "--insert_at_last (If the number of character prompts to be replaced > the number of character prompts in the base prompt, the extra replacement character prompts are added to the end of the character prompts in the base prompt)"
    )
    keep_weight = is_exists(
      AE_args, "--keep_weight (Experimental feature) (Keep the prompt weights)"
    )
    
    prompt = re.sub(
      rf"{name},", "$NAME,", prompt, count=1
    )
    
    # re4prompt を使用し、prompt から ch_prompt を摘出
    # ひとつづつ対象のキャラの prompt に変換
    prompts = []
    for p in prompt.split(","):
      for x in prompt_special_words:
        p = p.strip().strip(x)
      
      if re.findall(r":(\d+\.\d+)", p):
        if p.count(">") > 0:
          pass
        # else:
        #   p = re.sub(r"(:\d+\.\d+)", "", p, count=1)
        
      prompts.append(p)
      
    target_prompts = [p.strip() for p in target_prompt.split(",")]
    ch_prompts = [p.strip() for p in ch_prompt.split(",")]
    
    cp_indexes = []
    for p in prompts:
      if p in ch_prompts:
        index = prompts.index(p)
        cp_indexes.append((index, p))
    
    #dev
    if len(cp_indexes) != len(ch_prompt.split(",")):
      raise ValueError("didn't matched index count. ", len(cp_indexes))
    print("cp_indexes: ", cp_indexes  )
    print("prompts: ", prompts)
    print("ch_prompts: ", ch_prompts)
    
    for running, i in enumerate(cp_indexes):
      i, text = i
      
      replaceto = get_index(target_prompts, running, "$LPYfAILEVENT")
      if replaceto == "$LPYfAILEVENT":
        prompts[i] = "#PASS"
      else:
        prompts[i] = replaceto
      
      last = (running, i)
    # 実行数より target_prompts が多い場合
    if len(target_prompts) > last[0]:
      if add_prompt_at_last_base_character_prompt:
        prompts[last[1]] = target_prompts[last[running]:]
      elif add_prompt_at_last:
        prompts.append(x for x in target_prompts[last[running]+1:])
      
    
    prompt = ""
    for x in prompts:
      if x == "#PASS":
        continue      
      prompt += x+", "
    #prompt = prompt.strip(", ").strip()
    prompt = prompt_resizer(prompt, target_key, lora_data=(weight, True, "", ""), ce_mode=True)
    return prompt, f"Detected: {key} -> {target_key}"