



# Template Data from /dataset/multi_template.json
# Prompt > data[key][0]["Prompt"]
# Negative > data[key][0]["Negative"]
# Example Character1 > data[key][1]["Character1"]
# Example Character2 > data[key][1]["Character2"]
#
# Example Image > data[key][2]
# Example Image Seed > data[key][3]
""" # Example Json
{
  "example": [{
    "Prompt": "Prompt",
    "Negative": "Negative"},
    { "Character1": ["%LORA%", "%CH_NAME%", "%CH_PROMPT%", "%LOCATION%", "%FACE%"],
      "Character2": ["%LORA%", "%CH_NAME%", "%CH_PROMPT%", "%LOCATION%", "%FACE%"]},
    "./dataset/image_multi/None.png",
    "-1"]
}
"""

import simple_generator as data
import os
from simple_generator import charactor_check, final_process, get_loraweight, jsoncfg

def preview(template_type):
  def single_prompt_format(
    prompt, preview_list):
    if not len(preview_list) == 5:
      print("Failed. PreviewList Not Maching Len.")
      raise ValueError(f"{preview_list}\nNot Matching len. (!= 5)")
    
    LORA = preview_list[0]
    NAME = preview_list[1]
    CH_PROMPT = preview_list[2]
    LOCATION = preview_list[3]
    FACE = preview_list[4]
    
    format_prompt = prompt.replace(
      "%LORA%", LORA
    ).replace(
      "%CH_NAME%", NAME
    ).replace(
      "%CH_PROMPT%", CH_PROMPT
    ).replace(
      "%LOCATION%", LOCATION
    ).replace(
      "%FACE%", FACE)
    
    _, format_prompt = final_process(format_prompt, "./__pycache__/4vdawhaochdwcuorhwaodaw.txt")
    
    return format_prompt, LORA, NAME, CH_PROMPT, LOCATION, FACE
    
  template_dicts = jsoncfg.read("./dataset/multi_template.json")
  print(f"Returned dict: {template_dicts}")
  
  if template_type in template_dicts.keys():
    date = template_dicts[template_type]
  
  else:
    raise ValueError(f"Template: {template_type}\nUnknown Template ID")
  print(f"obtained_data: {date}")
  
  ch1_preview_data = date[1]["Character1"]
  ch2_preview_data = date[1]["Character2"]
  
  ex_prompt = date[0]["Prompt"]
  _, ex_prompt = final_process(ex_prompt, "./__pycache__/4vdawhaochdwcuorhwaodaw.txt")
  
  IMAGE = date[2]
  SEED = date[3]
  
  print(f" File dir: {IMAGE} ({SEED})")
  
  ch1_prompt_splited = ex_prompt.split("\nAND\n")[0]
  ch2_prompt_splited = ex_prompt.split("\nAND\n")[1]
  
  ch1_prompt, lora_1, name_1, ch_prompt_1, location_1, face_1 = single_prompt_format(
    prompt=ch1_prompt_splited,
    preview_list=ch1_preview_data
  )
  ch2_prompt, lora_2, name_2, ch_prompt_2, location_2, face_2 = single_prompt_format(
    prompt=ch2_prompt_splited,
    preview_list=ch2_preview_data
  )
  
  formatted_prompt = f"{ch1_prompt}\nAND\n{ch2_prompt}"
  
  if not os.path.exists(IMAGE):
    print(f"caught \"Gradio.ImageNotFoundError\"\nSample Image Path: {IMAGE}\n-> \"./dataset/image/None.png\"")
    IMAGE = "./dataset/image/None.png"
  
  return lora_1, name_1, ch_prompt_1, location_1, face_1, lora_2, name_2, ch_prompt_2, location_2, face_2, formatted_prompt, IMAGE, SEED


def generate(
  template_type,
  ch1, locate1, face1, add1, add_to_head1,
  ch2, locate2, face2, add2, add_to_head2
):
  template_dict = jsoncfg.read("./dataset/multi_template.json")
  
  NAME1, PROMPT1, LORA1, _ = charactor_check(
    ch1
  )
  NAME2, PROMPT2, LORA2, _ = charactor_check(
    ch2
  )
  
  if template_type in template_dict.keys():
    p = template_dict[template_type][0]["Prompt"]
    negative = template_dict[template_dict][0]["Negative"]
  else:
    raise ValueError(f"Template: {template_type}\nUnknown Template ID")
  
  p_1 = p.split("\nAND\n")[0]
  p_2 = p.split("\nAND\n")[1]
  
  if "%LORA%" in p_1:
    fprompt = p_1.replace(
      "%LORA%", LORA1
    ).replace(
      "%CH_NAME%", NAME1
    ).replace(
      "%CH_PROMPT%", PROMPT1
    ).replace(
      "%LOCATION%", locate1
    ).replace(
      "%FACE%", face1
    )
  
  elif "%LORA:" in p_1:
    fprompt = p_1.replace(
      "%CH_NAME%", NAME1
    ).replace(
      "%CH_PROMPT%", PROMPT1
    ).replace(
      "%LOCATION%", locate1
    ).replace(
      "%FACE%", face1
    )
    
    lw, replacefrom = get_loraweight(p_1)
    
    p_1 = p_1.replace(
      replacefrom, f"{LORA1}$WEIGHT"
    )
    p_1 = p_1.replace(
      ":1.0>$WEIGHT", f":{lw}>"
    )
    
  if "%LORA%" in p_2:
    fprompt = p_2.replace(
      "%LORA%", LORA2
    ).replace(
      "%CH_NAME%", NAME2
    ).replace(
      "%CH_PROMPT%", PROMPT2
    ).replace(
      "%LOCATION%", locate2
    ).replace(
      "%FACE%", face2
    )
  
  elif "%LORA:" in p_2:
    fprompt = p_2.replace(
      "%CH_NAME%", NAME2
    ).replace(
      "%CH_PROMPT%", PROMPT2
    ).replace(
      "%LOCATION%", locate2
    ).replace(
      "%FACE%", face2
    )
    
    lw, replacefrom = get_loraweight(p_2)
    
    p_2 = p_2.replace(
      replacefrom, f"{LORA2}$WEIGHT"
    )
    p_2 = p_2.replace(
      ":1.0>$WEIGHT", f":{lw}>"
    )
    
  # Additional
  if add_to_head1:
    p_1 = f"{add1}, {p_1}"
  else:
    p_1 += f", {add1}"
    
  if add_to_head2:
    p_2 = f"{add2}, {p_2}"
  else:
    p_2 += f", {add2}"
  
  fprompt = f"{p_1}\nAND\n{p_2}"
  
  logfile = "./template_multi.py-log.txt"
  _, formatted_prompt = final_process(
    fprompt, logfile
  )
  
  return formatted_prompt, negative


key_list = jsoncfg.read("./dataset/multi_template.json").keys()