import re
import json
import os
class jsonconfig():
  def read(self, filepath):
    print("Reading jsondata..")
    with open(filepath, 'r') as file:
        date = json.load(file)
    return date

  def write(self, date, filepath): 
      print("Writing config to jsondata..")
      with open(filepath, 'w') as file:
          json.dump(date, file, indent=4)  # indent=4でフォーマットを整形して書き込み
      return date
jsoncfg = jsonconfig()

ROOT_DIR = os.getcwd()

charactor_lora = jsoncfg.read("./database/charactor_lora.json")
available_name = list(charactor_lora.keys())
charactor_prompt = jsoncfg.read("./database/charactor_prompt.json")
prompt_format = jsoncfg.read("./database/prompt_formatter.json")

quality_data = '(best quality, masterpiece, detailed, incredibly fine illustration, kawaii)'
badhand = 'badhandv5'
years_prompt = '14 years old, baby face'

# この下は趣旨プロンプト
cat = 'cat ears, cat tail'
ocean_back = 'open beach, ocean, sun, water, beach'
orgasm_plus = '((orgasm, blush, full blush, sad, crying:1.2))'

# 基礎データセット
basic_negative = 'EasyNegative, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, sad, (inaccurate limb:1.2), (Low resolution:1.1), (((1boy, penis)))'
basic_adetailer_p = '(best quality)++, (masterpiece)++, (kawaii:1.1), cute, baby face:0.6, Consistent and proportionate facial features, High-Quality facial textures'
basic_adetailer_neg = '(bad anatomy:1.4), (distorted features:1.1), (realistic:1.1), (low quality, worst quality:1.1), lips, unclear face, Distorted facial features, Jagged lines in faces'




face_type_list = ["blush", "blush+", "orgasm", "smile"]
def facetype(type):
  if type == "blush+":
    FACE = "sad, (orgasm), blush, wink"
  else:
    FACE = type
    
  return FACE

def charactor_check(name):
  if not name in available_name:
    isTemplate = True
    return "", "", "", isTemplate
  
  else:
    isTemplate = False
    ch_name = charactor_lora[name][1]
    ch_lora = charactor_lora[name][0]
    ch_prompt = charactor_prompt[name]
  
  print(f"\
    Input: {name}\n\
    Return: \n\
      NAME: {ch_name}  |  LoRA: {ch_lora}\n\
      Charactor Prompt: {ch_prompt}")
  
  return ch_name, ch_prompt, ch_lora, isTemplate

def applicate(p, NAME, LORA, PROMPTS, CLOTH, LOCATION, FACE):
  prompt = p.replace(
    "$NAME+LORA", f"{LORA}, {NAME}"
  ).replace(
    "$FACE", FACE
  ).replace(
    "$CLOTHING, ", CLOTH
  ).replace(
    "$LOCATION, ", LOCATION
  ).replace(
    "$CHARACTOR", PROMPTS
  )
  
  return prompt

def return_markdown(new_prompt):
  return f"| Prompt |\n| --- |\n| {new_prompt} |"

def plusnegativeplusadetailer(negative, adp, adn):
  return f"| Negative |\n| --- |\n| {negative} |\n| ADetailer Prompt |\n| --- |\n| {adp} |\n| ADetailer Negative |\n| --- |\n| {adn} |"

def delete_duplicate_comma(p):
  while p.count(", , ") > 0:
    p = p.replace(", , ", ", ")
  
  return p


import data_opener as data_analyzer
def get_data(data, return_mode="WebUI" # or DICT
            ):
  if data == "" or data == None:
    raise ValueError(f"Invalid Data: {data}")
  
  if return_mode == "DICT":
    print("Starting Analyze Data..")
    date = data_analyzer.opener(data)
    print(f"Success! \nData: {date}")
    return date
  
  else:
    print("Starting Analyzing Data.. (WebUI Return Mode)")
    date = data_analyzer.opener(data)
    print("Success! \nStarting Open Data..")
    
    if 1 == 1:
        out = date
        cp = out["Checkpoint"]
        prompt = out["Prompt"]
        neg = out["Negative"]
        res = out["resolution"]
        seed = out["Seed"]
        cfg = out["CFG Scale"]
        cs = out["Clip Skip"]
        ss = out["Sampling Step"]
        sr = out["Sampling Sampler"]
        created = out["Created Date"]
        w = out["width"]
        h = out["height"]
        
        if out["ADetailer"]:
          ad = out["ADetailer Info"]
          ad_show = out["ADetailer"]
          ad_model = ad["Model"]
          ad_prompt = ad["Prompt"]
          ad_neg = ad["Negative"]
          ad_conf = ad["Confidence"]
          ad_mask = ad["Mask Blur"]
          ad_denoise = ad["Denoising Strength"]
          ad_ver = ad["version"]
        else:
          print("ADetailerは検出されませんでした")
          ad_show = False
          ad_model, ad_prompt, ad_neg, ad_conf, ad_mask, ad_denoise, ad_ver = "", "", "", "", "", "", ""
          
    #else:
      #raise ValueError("date の帰り値が > 2 です。")
    
    print(f"Success! \nDict Data: {date}")
    return cp, prompt, neg, res, seed, cfg, cs, ss, sr, created, w, h, ad_model, ad_prompt, ad_neg, ad_conf, ad_mask, ad_denoise, ad_ver
  
        
  
# プロンプトセットに基づき変換
def prompt_formatter(prompt: str):
  # パターン数の取得関数
  def get_pattern(target: str):
    pattern = r"%([^%]+)%"
    
    matches = re.findall(pattern, target)
    
    print(len(matches), "Formatter Found.")
    print("Formatting Target: ", matches)
    
    # フォーマットが利用可能かチェック
    return_matches = []
    
    x = list(prompt_format.keys())
    for y in matches:
      if y.lower() in x:
        return_matches.append(y.lower())
      else:
        print("Can't Detect Formatter Key.\nUnknown Keyword: ", y)
    
    return len(return_matches), return_matches
  
  pattern_count, _ = get_pattern(prompt)
  
  if pattern_count < 1:
    print("Not Found Formatting.\nSkipping Convert")
    return prompt
  else:
    # 変換!
    for k, d in prompt_format.items():
      prompt = prompt.replace(f"%{k}%", d)
    
    return prompt
    # Example 
    # %blush+%,
    # ->
    # blush, shy, looking at away,
    

def get_loraweight(prompt: str):
  if not "%LORA:" in prompt:
    return prompt, "%LORA%"

  pattern = r"%LORA:(\d+\.\d+)%"
  
  match = re.findall(pattern, prompt)[0]
  
  return float(match), f"%LORA:{match}%"
  
import log_writer as lw
def final_process(p, logfile):
  nocp = delete_duplicate_comma(p)
  nocp = prompt_formatter(nocp)
  md_formatted_p = nocp.replace("<", "\\<").replace(">", "\\>")
  return_prompt = nocp
  lw.w(logfile, nocp, "")
  return md_formatted_p, return_prompt