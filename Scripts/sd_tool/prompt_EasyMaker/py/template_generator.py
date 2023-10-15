# Template Data form /dataset/template.json
# Prompt > data[key][0]["Prompt"]
# Negative > data[key][0]["Negative"]
# Example > data[key][1]
# 0 -> 3
# %LORA% -> %FACE%
#
# Replace Target
# %LORA%, %CH_NAME%, %CH_PROMPT%, %LOCATION%,
# %FACE%
#

import simple_generator as data
from simple_generator import charactor_check, final_process, get_loraweight
from simple_generator import jsoncfg

def template_gen(template_type, ch_n, face,
                location, additional):
  # データの読み取り
  template_dict = jsoncfg.read("./dataset/template.json")

  # キャラクター情報の取得
  NAME, PROMPT, LORA, _ = charactor_check(ch_n)
  
  # テンプレ情報の取得 
  if template_type in template_dict.keys():
    p = template_dict[template_type][0]["Prompt"]
    ng = template_dict[template_type][0]["Negative"]
  else:
    raise ValueError(f"Template: {template_type}\nUnknown Template ID")
  
  if "%LORA%" in p:
    fprompt = p.replace(
      "%LORA%", LORA
    ).replace(
      "%CH_NAME%", NAME
    ).replace(
      "%CH_PROMPT%", PROMPT
    ).replace(
      "%LOCATION%", location
    ).replace(
      "%FACE%", face
    )
  
  
  elif "%LORA:" in p:
    fprompt = p.replace(
      "%CH_NAME%", NAME
    ).replace(
      "%CH_PROMPT%", PROMPT
    ).replace(
      "%LOCATION%", location
    ).replace(
      "%FACE%", face
    )
    
    lw, replacefrom = get_loraweight(fprompt)
    
    fprompt = fprompt.replace(
      replacefrom, f"{LORA}$WEIGHT"
    )
    
    fprompt = fprompt.replace(
      ":1.0>$WEIGHT", ":{}>".format(lw)
    )
  
  # Additional を追加
  fprompt += f", {additional}"
  
  # , の重複を消す
  # formatted_prompt = data.delete_duplicate_comma(fprompt)
  
  logfile = "./template_generator.py-log.txt"
  new_prompt, return_prompt = final_process(fprompt, logfile)
  
  return return_prompt, ng

def template_get(template_type):
  template_dict = jsoncfg.read("./dataset/template.json")
  print(f"Returned dict: {template_dict}")
  
  if template_type in template_dict.keys():
    date = template_dict[template_type][1]
    
  else:
    raise ValueError(f"Template: {template_type}\nUnknown Template ID")
  print(f"obtained_data: {date}")
  
  LORA, NAME, PROMPT, LOCATION, FACE = date[0], date[1], date[2], date[3], date[4]
  ex_prompt = template_dict[template_type][0]["Prompt"]
  _, ex_prompt = final_process(ex_prompt.replace(
    "%LORA%", LORA
  ).replace(
    "%CH_NAME%", NAME
  ).replace(
    "%CH_PROMPT%", PROMPT
  ).replace(
    "%LOCATION%", LOCATION
  ).replace(
    "%FACE%", FACE
  ), "./__pycache__/vdawhaochdwcuorhwaodaw.txt")
  
  IMAGE = template_dict[template_type][2]
  SEED = template_dict[template_type][3]
  print(f" File dir: {IMAGE}")
  
  return LORA, NAME, PROMPT, LOCATION, FACE, ex_prompt, IMAGE, SEED

def example_view(template_type):
  l, n, p, l, f, exp, image, seed = template_get(template_type)
  return l, n, p, l, f, exp, image, seed


file_path = "./dataset/template.json"
data = jsoncfg.read(file_path)
key_list = data.keys()