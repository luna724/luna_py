import re
from LGS.misc.jsonconfig import write_text
from datetime import datetime
from modules.shared import ROOT_DIR
from modules.generate_util import *
from modules.lib import re4prompt

def character_exchanger(mode, prompt, character):
  print("WARN: mode control is currently disabled.")
  
  # 割とシビアにloraを取得 -> $LORA に変換
  prompt_lora = re4prompt(r"(<lora:.*:).*>", prompt)
  ch_lora_list_raw = get_lora_list("only_lora")
  ch_lora_list = []
  
  for x in ch_lora_list_raw:
    print(x)
    ch_lora_list.append( # <lora:hello:1.0> -> <lora:hello:
      (x[0].split(":")[0] + ":" + x[0].split(":")[1] + ":", x[1])
    )
    print("x: ",x[0].split(":"))
  
  target = None
  for y in prompt_lora:
    if target != None:
      continue
    for tpl in ch_lora_list:
      if tpl[0] in y:
        print("Catched.")
        target = tpl[0]
        key = tpl[1]
    else:
      print(f"Not catched: {y}")
  if target == None:
    return "Error: Cannot find Character Lora (please check lora trigger syntax!)", f"Tried: Unknown -> {character}"
  
  print("target: ", target)
  loraname = re.findall(r"<lora:(.*):", target)[0]
  print("loraname: ", loraname)
  current_weight = re4prompt(rf"<lora:{loraname}:(.+)>", prompt)[0]
  print(f"Detected weight: {current_weight}")
  
  prompt = re.sub(rf"<lora:{loraname}:{current_weight}>", "$LORA", prompt, count=1)
  
  # lora名を使用してキーを特定、その他のデータも取得
  key, _, ch_name, ch_prompt, ch_extend = get_lora_list("manual", True, key)
  
  # 初期化して渡す
  prompt = re.sub(ch_name, "$NAME", prompt, count=1)
  prompt = re.sub(ch_prompt+ch_extend, "$PROMPT", prompt, count=1)
  
  info = f"Detected: {key} -> {character}"
  
  
  times = datetime.now().strftime("%Y%m%d")
  write_text(
    f"\n\n{times}'s Data\n" + prompt_character_resizer(
    prompt, current_weight, character
  ), os.path.join(
    ROOT_DIR, "logs", "character_exchanger.log"
  ), False
  )
  return prompt_character_resizer(
    prompt, current_weight, character
  ), info