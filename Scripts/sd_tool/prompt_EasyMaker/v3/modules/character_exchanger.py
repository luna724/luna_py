import gradio as gr
import re
from typing import * 

from modules.shared import language
from modules.generate_util import get_lora_list as obtain_lora_list
from modules.lib import re4prompt, time_takens, prompt_special_words, get_index
from modules.prompt_resize import prompt_resizer

# def character_exchanger(mode, prompt, character, strict_check, autoclip, ptdh):
#   """this function will be discontinued!!!"""
  
#   """
#   DISCONTINUED Function.
#   new function -> .:character_exchanger
#   """
#   if not args.local:
#     autoclip = False
#     print("[CE]: auto clip are supported only local env (if you're in local, launch launch.py with arg \"--local\")")
  
#   if pyperclip.paste() != "" and autoclip:
#     print("[CE]: clipboard object found. printout..")
#     print(pyperclip.paste())

#   if ptdh:
#     mode = []

#   print("[CE]: WARN: mode control is experimental feature")
#   # mode: List(Literal["lora", "name", "prompt"])
  
#   # 割とシビアにloraを取得 -> $LORA に変換
#   prompt_lora = re4prompt(r"(<lora:.*:).*>", prompt)
#   ch_lora_list_raw = get_lora_list("only_lora")
#   ch_lora_list = []
  
#   for x in ch_lora_list_raw:
#     #print(x)
#     ch_lora_list.append( # <lora:hello:1.0> -> <lora:hello:
#       (x[0].split(":")[0] + ":" + x[0].split(":")[1] + ":", x[1], x[2])
#     )
#     #print("x: ",x[0].split(":"))
  
#   target = None
#   name = None
#   for y in prompt_lora:
#     if target != None:
#       continue
#     for tpl in ch_lora_list:
#       if tpl[0] in y:
#         print("[CE]: Catched.")
#         target = tpl[0]
#         key = tpl[1]
        
#         if strict_check:
#           # tpl[2] = name をもとに re4prompt を使用して name も一致するかチェック
#           try:
#             namecheck = re4prompt(tpl[2], prompt)
#             print(f"[CE]: {len(namecheck)}'s name pattern found.")
#             name = namecheck[0]
#             target = tpl[0]
#             break
#           except IndexError as e:
#             print(f"[CE]: Not match lora / name = {tpl[0]} / {tpl[2]}")
#             continue
#         else:
#           break
#     #else:
#       # print(f"Not catched: {y}")
#   if strict_check:
#     if name == None:
#       return "Error: Cannot find Character Lora (please check lora trigger syntax!)", f"Tried: Unknown -> {character}"
    
#     print("[CE]: name = ", name)
    
#   if target == None:
#     return "Error: Cannot find Character Lora (please check lora trigger syntax!)", f"Tried: Unknown -> {character}"
  
#   print("[CE]: target: ", target)
#   loraname = re.findall(r"<lora:(.*):", target)[0]
#   print("[CE]: loraname: ", loraname)
#   current_weight = re4prompt(rf"<lora:{loraname}:(.+)>", prompt)[0]
#   print(f"[CE]: Detected weight: {current_weight}")
  
#   prompt = re.sub(rf"<lora:{loraname}:{current_weight}>", "$LORA", prompt, count=1)
  
#   # lora名を使用してキーを特定、その他のデータも取得
#   key, _, ch_name, ch_prompt, ch_extend = get_lora_list("manual", True, key)
  
#   # 初期化して渡す
#   prompt = re.sub(ch_name, "$NAME", prompt, count=1)
#   prompt = re.sub(ch_prompt+ch_extend, "$PROMPT", prompt, count=1)
  
#   if len(mode) == 3:
#     prompt = prompt_character_resizer(
#       prompt, current_weight, character
#     )
#   else:
#     rpl, rpn, rpp = prompt_character_resizer(
#       prompt, current_weight, character, True
#     )
    
#     replace_key = []
    
#     if "lora" in mode:
#       replace_key.append(
#         ("$LORA", rpl)
#       )
#     if "name" in mode:
#       replace_key.append(
#         ("$NAME", rpn)
#       )
#     if "prompt" in mode:
#       replace_key.append(
#         ("$PROMPT", rpp)
#       )
    
#     prompt = multiple_replace(
#       prompt, replace_key
#     )
    
#     if not ptdh:
#       prompt = prompt_character_resizer(
#         prompt, current_weight, key
#       )
  
#   if autoclip:
#     print("[CE]: Copied!")
#     pyperclip.copy(prompt)
  
#   info = f"Detected: {key} -> {character}"
  
#   times = datetime.now().strftime("%Y%m%d - %H:%M")
#   write_text(
#     f"\n\n{times}'s Data\n" + prompt, os.path.join(
#     ROOT_DIR, "logs", "character_exchanger.log"
#   ), False
#   )
#   return prompt, info


def new_character_exchanger(
  mode:list, prompt:str, exchange_to:str,
  for_ptemplate:bool):
  
  timer = time_takens()
  timer.start()
  
  lang = language("/ui/generate/exchanger.py", "raw")
  
  # リストを取得
  lora_list = []
  for x in obtain_lora_list("only_lora"):
    lora_list.append(# Tuple(<lora:example:, lora_key, lora_name)
      (x[0].split(":")[0]+":"+x[0].split(":")[1]+":", x[1], x[2])
    )
  
  # プロンプトの LoRA を摘出
  prompt_lora = re4prompt(r"(<lora:.*:).*>", prompt)
  
  target = None
  name = None
  
  # LoRAリストにマッチするLoRAを name, target に代入
  for lora in prompt_lora:
    for tpl in lora_list:
      if tpl[0] in lora:
        print("Catched.")
        target = tpl[0]
        key = tpl[1]
        
        # name も一致させる
        try:
          prompt_name = re4prompt(tpl[2], prompt)
          name = prompt_name[0]
          target = tpl[0]
          break
        except IndexError:
          continue
  
  if for_ptemplate:
    mode = ["prompt", "lora", "name"]
  
  if name == None or target == None:
    raise gr.Error(lang["cant_find"])
  
  loraname = re.findall(r"<lora:(.*):", target)[0]
  weight = re4prompt(rf"<lora:{loraname}:(.*)>", prompt)[0]
  
  prompt = re.sub(rf"<lora:{loraname}:{weight}>", "$LORA", prompt, count=1)
  key, _, name, ch_prompt, extend = obtain_lora_list("manual", True, key)
  target_key, target_lora, target_name, target_prompt, target_extend = obtain_lora_list(
    "manual", True, exchange_to
  )
  if not "lora" in mode:
    target_key = key
  
  if "name" in mode:
    prompt = re.sub(
      rf"{name},", "$NAME,", prompt, count=1
    )
  # re4prompt を使用し、prompt から ch_prompt を摘出
  # ひとつづつ対象のキャラの prompt に変換
  if for_ptemplate:
    mode = ["prompt"]
    target_prompt = "$PROMPT"
  
  if "prompt" in mode:
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
    
    if target_prompt.count(",") < 1:
      target_prompts = [target_prompt.strip()]
    else:
      target_prompts = [
        p.strip() for p in target_prompt.split(",")]
    if ch_prompt.count(",") < 1:
      ch_prompts = [ch_prompt.strip()]
    else:
      ch_prompts = [
        p.strip() for p in ch_prompt.split(",")]
    
    cp_indexes = []
    for p in prompts:
      if p in ch_prompts:
        index = prompts.index(p)
        cp_indexes.append((index, p))

    if len(cp_indexes) != len(ch_prompts):
      raise gr.Error("can't find character name")

    for running, (i, text) in enumerate(cp_indexes):
      replaceTo = get_index(
        target_prompts, running, "$LPY-fAILEVENT"
      )
      if replaceTo == "$LPY-fAILEVENT":
        prompts[i] = "#PASS"
      else:
        prompts[i] = replaceTo
      
      last = (running, i)
    
    print("target_prompts: ", target_prompts)
    print("last: ", last)
    if not len(target_prompts) == last[0]:
      # prompts を分割、最後の ch_prompts の位置にすべて残りを突っ込む
      prompt1 = prompts[:last[1]+1]
      prompt2 = prompts[last[1]+1:]
      
      for x in target_prompts[last[0]+1:]:
        prompt1.append(x)
      
      prompts = prompt1 + prompt2
    
    prompt = ""
    for x in prompts:
      if x == "#PASS":
        continue
      prompt += str(x)+", "
  if for_ptemplate:
    while prompt.count(", , ") >= 1:
      prompt = prompt.replace(", , ", ", ")
  
    return prompt, f"converted: -> Template mode"
  prompt = prompt_resizer(prompt, target_key, lora_data=(weight, True, "", ""), ce_mode=True)
  
  while prompt.count(", , ") >= 1:
    prompt = prompt.replace(", , ", ", ")
  
  return prompt, f"Detected: {key} -> {target_key}"