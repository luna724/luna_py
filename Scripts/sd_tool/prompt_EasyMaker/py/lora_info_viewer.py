import loradata.lora_dataset as data
import os

lora_list = ["Sakurai nozomi prcn", "prcn style", "Incoming Hug", "Incoming Kiss", "Rei no himo", "In Glass Cup", "In Box", "In Water Capsule", "Skin Fang", "Cat Eyes", "Peace Sign", "Ojousama Pose", "POV Across Table", "Color", "Pocky Game", "Yuri Kiss", "yuri Mutual Masturbation", "hoshi119's POV Cunniling", "69 Yuri", "Liquid Clothes", "Bondage Outfit/Dominatrix", "Miniskirt+", "Naked Towel", "Clothes Pull 446", "Track Uniform", "Greek Cloth", "Plastic Bag","Better Naked Bathrobe", "Morrigan Aensland (Vampire)", "Dangerous Beast Cosplay", "Onesie Pajamas", "Highleg Sideless Leotard", "Cheerleader (BlueArchive)", "WHB (by. sevora)", "Hospital Gown", "WHB (by. psoft)", "Akuma Homura's BlackDress", "Bondage Amine", "masusu Breasts", "Standing cunnillingus", "Milking Machine","catcat xl sdxl","Slime girl v16 by.NeutronSlime","Slime girl v11 by.NeutronSlime","Slime girl by.momoura","furnace 75v1 Cu6","Sketch Inpaint v20","Pose yuri Mutual Masturbation","Sticky Slime","Object Masturbation","Desk Humping","Vibrator Masturbation","Living Clothes","Yuri Tribadism","Detail Tweaker"]

def generate_table(contents, items_per_row=5):
    table_html = "| Available LoRA Information | | | | |\n| --- | --- | --- | --- | --- |\n"
    for index, content in enumerate(contents, start=1):
        table_html += f"| {content} "
        if index % items_per_row == 0:
            table_html += "|\n"
    table_html += "|"
    return table_html

def search_filtering(search, ui_mode=True):
  r_list = []
  print("lora_list: ", lora_list)
  for s in lora_list:
    if search.lower() in s.lower().strip():
      r_list.append(s)
    else:
      continue
  
  if not ui_mode:
    return r_list
  
  if len(r_list) < 1:
    return "| Available LoRA Information |\n| --- |\n| ### No Match Found |"
  
  print("WARN: China lang Is Translated to ja-jp")
  return generate_table(r_list)



def main(view_target):
  print("lora_list: ", lora_list)
  low_lora_list = []
  for x in lora_list:
    low_lora_list.append(x.lower())
  
  print("low_lora_list: ", low_lora_list)
  if not view_target.lower() in low_lora_list:
    available_ = search_filtering(view_target, False)
    if len(available_) == 1:
      view_target = available_[0]
    else:
      print("WARN: Convert Target LoRA Model has Not Found.\nSearching Result 2+ Found (Not All Match) Using Index 0")
      view_target = available_[0]

  # LoRA名に基づいて呼び出し
  info, html = data.html(view_target.lower())
  print(info)
  print(os.getcwd())
  return info, html