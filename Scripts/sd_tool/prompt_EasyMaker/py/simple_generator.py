available_name = ["original", "ichika", "luna",
                  "emu", "nene", "kanade", "mizuki", "hoshino", "laby",
                  "midori", "momoi", "shiroko", "klee",
                  "barbara", "saki", "shiho", "honami",
                  "minori", "haruka", "airi", "shizuku",
                  "kohane", "ann", "shefi", "natsu", "serina", "neneka", "nahida", "aisha landar"
                  ]


quality_data = '(best quality, masterpiece, detailed, incredibly fine illustration, kawaii)'
badhand = 'badhandv5'
years_prompt = '14 years old, baby face'

charactor_lora = { # [Loraモデル, キャラ名]
  "ichika": ["<lora:HoshinoIchika:1.0>", "ichika"],
  "luna": ["<lora:ichika3:0.4>", "ichika"],
  "emu": ["<lora:OtoriEmu:1.0>", "wdhemu"],
  "nene": ["<lora:NotKyo:1.0>", "nene"],
  "kanade": ["<lora:YoisakiKanade:1.0>", "yoka"],
  "mizuki": ["<lora:AkiyamaMizuki:1.0>", "mizuki"],
  "hoshino": ["<lora:hoshino1:1.0>", "hoshinornd"],
  "midori": ["<lora:midori1:1.0>", "midorirnd"],
  "shiroko": ["<lora:shiroko1:1.0>", "shirokornd"],
  "klee": ["<lora:klee1:1.0>", "kleernd"],
  "barbara": ["<lora:barbara1:1.0>", "barbararnd"],
  "laby": ["<lora:LabyElsword:1.0>", "laby"],
  "saki": ["<lora:TenmaSaki:1.0>", "saki"],
  "shiho": ["<lora:ShihoV3:1.0>", "hinoshiho"],
  "honami": ["<lora:HonamiV2:1.0>", "mhonami"],
  "minori": ["<lora:HanasatoMinori:1.0>", "minori"],
  "haruka": ["<lora:KiritaniHaruka:1.0>", "kiriharu"],
  "airi": ["<lora:MomoiAiri:1.0>", "momoai"],
  "shizuku": ["<lora:Shizuku_H:1.0>", "shizuku"],
  "kohane": ["<lora:AzusawaKohane:1.0>", "kohane"],
  "ann": ["<lora:Anv2:1.0>", "shian"],
  "shefi": ["<lora:shefi2:1.0>", "shefi"],
  "momoi": ["<lora:momoi1:1.0>", "momoirnd"],
  "natsu": ["", "natsurnd"],
  "serina": ["", "serinarnd"],
  "neneka": ["", "nenekarnd"],
  "nahida": ["<lora:nahida1:1.0>", "nahidarnd"],
  "aisha landar": ["", "aisha"]
}

charactor_prompt = {
  "luna": '(light blue hair), light purple hair, white hair, blue eyes, blush, hair between eyes, straight hair, small twintale, 12 years old, cat ears, blue light',
  "ichika": "absorbing long hair, swept bangs, black hair, grey eyes",
  "emu": "pink eyes, pink hair",
  "nene": "long hair, 1girl, purple eyes, green hair, grey hair:0.6",
  "kanade": "blue eyes, grey hair, blue hair, long hair, very long hair, hair between eyes",
  "mizuki": "red hair ribbon, pink eyes, small breasts, light pink hair, side ponytail, wavy hair",
  "hoshino": "light pink hair, very long hair, long hair, ahoge, orange and blue differently colored eyes",
  "midori": "beige hair, green eyes, short hair, small breasts, side mini ponytail, cat ear green bandana",
  "shiroko": "",
  "klee": "",
  "barbara": "beige hair, blue eyes, medium hair, large breasts, twintails",
  "laby": "short hair, pink hair, hair between eyes, bare shoulders, pink eyes",
  "saki": "blonde hair, pink hair, pink eyes, long hair, twintails",
  "shiho": "green eyes, grey hair",
  "honami": "short hair, blue eyes, brown hair, hair ornament, hairclip",
  "minori": "brown hair, grey eyes, medium hair",
  "haruka": "short hair, blue eyes, blue hair",
  "airi": "pink hair, two side up, pink eyes, long hair, fang",
  "shizuku": "long hair, blue hair, blue eyes, small breasts, mole, mole under mouth",
  "kohane": "blonde hair, twintails, brown eyes, hair between eyes",
  "ann": "long hair, black hair, blue hair, orange eyes, star (symbols), star hair ornament",
  "shefi": "aqua hair, asymmetrical gloves, black gloves, brown gloves, fangs, sidelocks, single braid",
  "momoi": "",
  "natsu": "",
  "serina": "",
  "neneka": "pink hair, twintails, small breasts",
  "nahida": "lustrous skin, silver hair, side ponytail, long hair, green eyes, medium breasts, cape",
  "aisha landar": "purple hair, purple eyes"
}

# この下は趣旨プロンプト
cat = 'cat ears, cat tail'
ocean_back = 'open beach, ocean, sun, water, beach'
orgasm_plus = '((orgasm, blush, full blush, sad, crying:1.2))'


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

import json
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

import log_writer as lw
def final_process(p, logfile):
  nocp = delete_duplicate_comma(p)
  md_formatted_p = nocp.replace("<", "\\<").replace(">", "\\>")
  return_prompt = nocp
  lw.w(logfile, nocp, "")
  return md_formatted_p, return_prompt

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
  
        
  
  