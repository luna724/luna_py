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

import simple_generator as data
from simple_generator import charactor_check, final_process, get_loraweight
from simple_generator import jsoncfg, ROOT_DIR
from PIL import Image
import os

class EasyDatabase():
  v2 = "Disabled. because V2 method"
  noneimg = os.path.join(ROOT_DIR, "dataset", "image", "None.png")
  current_method = "v2"
warn = EasyDatabase()



def template_gen(template_type, ch_n, face,
                location, additional, 
                header_additional: str, #v2 method
                
                ):
  def prompt_setup(
    LORA,
    NAME,
    PROMPT,
    base_prompt,
  ):
    p = base_prompt
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
    if not additional == "" or not additional == None:
      print("Lower throwed! ")
      additional.strip(",")
      fprompt += f", {additional}"
    if not header_additional == "" or not header_additional == None:
      print("Header throwed! ")
      header_additional.strip(",")
      fprompt = f"{header_additional}, {fprompt}"
    
    # , の重複を消す
    # formatted_prompt = data.delete_duplicate_comma(fprompt)
    
    logfile = "./template_generator.py-log.txt"
    new_prompt, return_prompt = final_process(fprompt, logfile)
    
    return return_prompt
  # データの読み取り
  template_dict = jsoncfg.read("./dataset/template.json")

  # キャラクター情報の取得
  NAME, PROMPT, LORA, _ = charactor_check(ch_n)
  if template_type in template_dict.keys():
    target = template_dict[template_type]
  else:
    raise ValueError(f"Template: {template_type}\nUnknown Template ID")
      
      
  # v1 Method
  if len(target) == 4 or target[0] == "v1":
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
    if not additional == "" or not additional == None:
      print("Lower throwed! ")
      additional.strip(",")
      fprompt += f", {additional}"
    if not header_additional == "" or not header_additional == None:
      print("Header throwed! ")
      header_additional.strip(",")
      fprompt = f"{header_additional}, {fprompt}"
    
    # , の重複を消す
    # formatted_prompt = data.delete_duplicate_comma(fprompt)
    
    logfile = "./template_generator.py-log.txt"
    new_prompt, return_prompt = final_process(fprompt, logfile)
    
    return return_prompt.strip(", "), ng
  elif target[0] == "v2":
    print("using v2 Method..")
    # v2 Method
    base = target[1]["Prompt"]
    negative = target[1]["Negative"]
    
    return prompt_setup(LORA, NAME, PROMPT, base).strip(", "), negative
    
def template_get(template_type):
  template_dict = jsoncfg.read("./dataset/template.json")
  print(f"Returned dict: {template_dict}")
  if not template_type in template_dict.keys():
    raise ValueError(f"Template: {template_type}\nUnknown Template ID")
  date = template_dict[template_type]
  method = date[0]
  
  if method == "v1" or len(date) == 4:
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
      "%LOCATION%", LOCATIO
    ).replace(
      "%FACE%", FACE
    ), "./__pycache__/vdawhaochdwcuorhwaodaw.txt")
    
    IMAGE = template_dict[template_type][2]
    SEED = template_dict[template_type][3]
    print(f" File dir: {IMAGE}")
    
    return LORA, NAME, PROMPT, LOCATION, FACE, ex_prompt, IMAGE, SEED, warn.v2, warn.noneimg, warn.v2, warn.v2, warn.v2, warn.v2, warn.v2, warn.v2, warn.v2, warn.v2, warn.v2, warn.v2, warn.v2
  elif method == "v2":
    if not template_type in template_dict.keys():
      raise ValueError(f"Template: {template_type}\nUnknown Template ID")
    date = template_dict[template_type]
    print(f"Obtained data: {date}")
    example_date = date[2]
    cndate = date[5]
    
    date_method = date[0]
    template_prompt = date[1]["Prompt"]
    negative = date[1]["Negative"]
    example_lora = example_date[0]
    example_name = example_date[1]
    example_ch_prompt = example_date[2]
    example_location = example_date[3]
    example_face = example_date[4]
    example_lower_add = example_date[5]
    example_upper_add = example_date[6]
    example_image = date[3]
    example_seed = date[4]
    cn_image = cndate[0]
    cn_method = cndate[1]
    example_cn_weight = cndate[2]
    example_cn_mode = cndate[3]
    example_img2img = cndate[4]
    example_cfg = date[6]
    example_sdcp = date[7]
    res = date[8]
    sampler = date[9]
    example_hires_method = date[10]
    
    _, resized_prompt = final_process(template_prompt.replace(
      "%LORA%", example_lora
    ).replace(
      "%CH_NAME%", example_name
    ).replace(
      "%CH_PROMPT%", example_ch_prompt
    ).replace(
      "%LOCATION%", example_location
    ).replace(
      "%FACE%", example_face
    ), "./__pycache__/vdawhaochdwcuorhwaodaw.txt")
    
    if not example_lower_add == "":
      resized_prompt += f", {example_lower_add}"
    if not example_upper_add == "":
      resized_prompt = f"{example_upper_add}, {resized_prompt}"
    
    if not os.path.exists(example_image):
      print(f"Image not found. Except FileNotFoundError.")
      example_image = os.path.join(ROOT_DIR, "dataset", "image", "None.png")
    
    return example_lora, example_name, example_ch_prompt, example_location, example_face, resized_prompt, example_image, example_seed, date_method, cn_image, example_cn_weight, example_cn_mode, example_img2img, cn_method, example_cfg, example_sdcp, res, sampler, example_hires_method, example_upper_add, example_lower_add
  
  

file_path = "./dataset/template.json"
data = jsoncfg.read(file_path)
key_list = data.keys()


def save(
  method: str,
  name: str,
  LORA: str,
  NAME: str,
  PROMPT: str,
  LOCATION: str,
  FACE: str,
  IMAGE,
  SEED: int,
  Negative: str,
  base_prompt: str,
  LOWER_ADD: str,
  UPPER_ADD: str,
  cn_image, # image can upload!
  cn_method: str, # method e.g. [IP2P, OpenPose, Lineart]
  cn_weight: float, # weight -1.0 ~ 2.0? 
  cn_mode: str, # cn mode not method e.g. [my prompt is more important, balanced]
  cn_img2img: bool, # is image for img2img?
  cfg_scale: float, # CFG Scale: 7.0 +0.5 ~ 
  sd_model: str, # SD Model name (checkpoint)
  res: str, # recommended resolution {int}x{int} (str)
  sampler: str, #Sampling Method: e.g. [euler a, DPM++ SDE Karras]
  hireS_method: str, # Hires.fix Method name
  force_update: bool
):
  if "Single" == "Single":
    method = warn.current_method
    template_dict = jsoncfg.read("./dataset/template.json")
    
    # もし名前が既に存在するならエラー
    if name in template_dict.keys():
      if not force_update:
        return "stderr: This name is already taken."
    
    if IMAGE == "NO IMAGE":
      IMAGE_ = "./dataset/image/None.png"
    elif IMAGE == None:
      IMAGE_ = "./dataset/image/None.png"
    else:
      # 存在するならファイル名を設定して保存、IMAGE_ に入力
      IMAGE.save(
        os.path.join(ROOT_DIR, "dataset", "image", f"{name}_{SEED}.png"), "PNG"
      )
      IMAGE_ = os.path.join(ROOT_DIR, "dataset", "image", f"{name}_{SEED}.png")
    
    if cn_image == None:
      CN_IMAGE_ = "./dataset/image/None.png"
    else:
      cn_image.save(
        os.path.join(ROOT_DIR, "dataset", "image", f"{name}_controlnet.png"), "PNG"
      )
      CN_IMAGE_ = os.path.join(ROOT_DIR, "dataset", "image", f"{name}_controlnet.png")
      
      
    generative_dict = {
      name: [
        method,
        {"Prompt": base_prompt,
        "Negative": Negative
      }, [LORA, NAME, PROMPT, LOCATION, FACE, LOWER_ADD, UPPER_ADD], 
        IMAGE_, str((SEED)),
        [CN_IMAGE_, cn_method, cn_weight, cn_mode, cn_img2img],
        cfg_scale,
        sd_model,
        res,
        sampler,
        hireS_method]
    }
    
    print("Generated Data: ", generative_dict)
    
    template_dict.update(generative_dict)
    
    jsoncfg.write(template_dict, "./dataset/template.json")
    
    return "Success! Reloading the UI will add it to generation mode options"

def update_template(
  target: str,
  detection_mode: str = "len", # len = use len() for database version check
  # method = use database key: method for database version check
  updateAll: bool = False
):
  if updateAll:
    target_template = list(key_list)
  else:
    target_template = [target]
  
  for f in target_template:
    if not f in key_list:
      print(f"Target Template Not found. (Template: {f})")
      continue
    flen = len(f)
    correct_len = 11
    # Nesting
    # f[1] = len(2)
    # f[2] = len(5)
    # f[3], [4] = len(1)
    # f[5] = len(5)
    # f[6] ~ [10] = len(1) 

#if __name__ == "__main__":
  