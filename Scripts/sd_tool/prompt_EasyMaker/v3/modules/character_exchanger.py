import pyperclip
import re
from LGS.misc.jsonconfig import write_text
from datetime import datetime


from modules.shared import ROOT_DIR, args
from modules.generate_util import *
from modules.lib import re4prompt

def character_exchanger(mode, prompt, character, strict_check, autoclip, ptdh):
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