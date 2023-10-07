"""
{PROMPT}
Negative prompt: {Negative}
Steps: {Step}, Sampler: {Sampler}, CFG scale: {CFG}, Seed: {Seed}, Size: {Width}x{Height}, Model hash: 7eb674963a, Model: Hassaku_Hentai_model, Clip skip: {Clip Skip}, ADetailer model: face_yolov8n.pt, ADetailer prompt: "(best quality)++, (masterpiece)++, (kawaii:1.1), cute, baby face:0.6, Consistent and proportionate facial features, High-Quality facial textures", ADetailer negative prompt: "(bad anatomy:1.4), (distorted features:1.1), (realistic:1.1), (low quality, worst quality:1.1), lips, unclear face, Distorted facial features, Jagged lines in faces", ADetailer confidence: 0.3, ADetailer dilate/erode: 4, ADetailer mask blur: 4, ADetailer denoising strength: 0.4, ADetailer inpaint only masked: True, ADetailer inpaint padding: 32, ADetailer version: 23.9.2, Lora hashes: "YoisakiKanade: 98221f0b4503, masusu_breast: 32ac63d8c40e, masturbation-v1: f4b31b40d944", TI hashes: "EasyNegative: c74b4e810b03, badhandv5: aa7651be154c", Version: v1.6.0

"""

def none_checker(str):
  if len(str) == 0:
    return "Can't Find Data."
  else:
    return str[0]


import re
from datetime import datetime 
  # 簡単なものから
def opener(text):
  base_dict = {}
  # sampling
  pattern_step = r"Steps: (\d+)"
  pattern_sampler = r"Sampler: (.*), CFG"

  step = none_checker(re.findall(pattern_step, text))
  sampler = none_checker(re.findall(pattern_sampler, text))
  
  # CFG, Clip Skip
  pattern_cfg = r"CFG scale: (\d+)"
  pattern_cs = r"Clip skip: (\d+)"
  
  cfg_scale = none_checker(re.findall(pattern_cfg, text))
  clip_skip = none_checker(re.findall(pattern_cs, text))
  
  # Seed, Resolution
  pattern_seed = r"Seed: (\d+)"
  pattern_w = r"Size: (\d+)x"
  pattern_h = r"Size: \d+x(\d+),"
  
  seed = none_checker(re.findall(pattern_seed, text))
  width = none_checker(re.findall(pattern_w, text))
  height = none_checker(re.findall(pattern_h, text))
  resolution = f"{width}x{height}"
  
  # Prompt, Neg
  pattern_neg = r"\nNegative prompt: (.+)"
  pattern_p = r"(.*)\nNegative prompt: "
  
  prompt = none_checker(re.findall(pattern_p, text))
  negative = none_checker(re.findall(pattern_neg, text))
  
  # SDCP
  print("WARN: Checkpoint Model Check is Only ONE Models Detectable")
  pattern_cp = r"Model: (.*), Clip"
  checkpoint = none_checker(re.findall(pattern_cp, text))
  
  time = datetime.now()
  session_time = dates = time.strftime("%Y%m%d")
  
  # ADetailer
  print("WARN: ADetailer Data Check is Onle ONE Data Detectable")
  if len(re.findall(r"ADetailer model:", text)) < 1:
    print("Not Find ADetailer Data.\nSkipping..")
    adetailer_dict = {
      "ADetailer": False
    }
    base_dict.update(adetailer_dict)
    
  else:
    pad_model = r"ADetailer model: (.+).pt,"
    pad_prompt = r'ADetailer prompt: "(.+)", ADetailer neg'
    pad_neg_pr = r'ADetailer negative prompt: "(.+)", ADetailer '
    pad_confidence = r'ADetailer confidence: (\d+\.\d+), ADetailer '
    pad_mask_blue = r'ADetailer mask blur: (\d+), ADetailer '
    pad_denoising = r'ADetailer denoising strength: (\d+\.\d+), ADetailer '
    pad_ver = r'Detailer version: (\d+\.\d+\.\d+), '

    ad_model = none_checker(re.findall(pad_model, text))
    ad_prompt = none_checker(re.findall(pad_prompt, text))
    ad_negative = none_checker(re.findall(pad_neg_pr, text))
    ad_confidence = none_checker(re.findall(pad_confidence, text))
    ad_mask_blue = none_checker(re.findall(pad_mask_blue, text))
    ad_denoising = none_checker(re.findall(pad_denoising, text))
    ad_version = none_checker(re.findall(pad_ver, text))
    
    adetailer_dict = {
      "ADetailer": True,
      "ADetailer Info": {
        "Model": f"{ad_model}.pt",
        "Prompt": ad_prompt,
        "Negative": ad_negative,
        "Confidence": ad_confidence,
        "Mask Blur": ad_mask_blue,
        "Denoising Strength": ad_denoising,
        "Version": ad_version
      }
    }
    base_dict.update(adetailer_dict)
  
  sd_dict = {"Checkpoint": checkpoint,
      "Prompt": prompt,
                            "Negative": negative,
                            "width": width,
                            "height": height,
                            "resolution": resolution,
                            "Seed": seed,
                            "CFG Scale": cfg_scale,
                            "Clip Skip": clip_skip,
                            "Sampling Step": step,
                            "Sampling Sampler": sampler,
                            "Created Date": time.strftime("%Y-%m-%d")
                            }
  
  merged_dict = base_dict.copy()  # base_dict のコピーを作成
  merged_dict.update(sd_dict)     # sd_dict の内容を追加
  return merged_dict 

# from simple_generator import jsoncfg
