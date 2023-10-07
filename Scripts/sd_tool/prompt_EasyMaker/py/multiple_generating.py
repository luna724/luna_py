import simple_generator as data
from log_writer import w as log_write

def latent_couple(ch1_name="",
                  ch1_cloth="",
                  ch1_add="",
                  ch2_name="",
                  ch2_cloth="",
                  ch2_add="",
                  location="",
                  quality=True):
  base_prompt = """$Quality 2 girls, $LOCATION, \nAND\n$Charactor_Quality, 2 girls, $NAME+LORA, $CHARACTOR, $CLOTHING, $ADDITIONAL, $LOCATION,\nAND\n$Charactor_Quality, 2 girls, $NAME+LORA2, $CHARACTOR2, $CLOTHING2, $ADDITIONAL2, $LOCATION"""
  
  """
  $Quality = data.quality_data 
  $Charactor_Quality = Mini Quality Data
  """
  
  # 全体の処理
  if quality:
    base_prompt = base_prompt.replace("$Quality", f"{data.quality_data},")
    
  else:
    base_prompt = base_prompt.replace("$Quality ", "")
  
  base_prompt = base_prompt.replace("$Charactor_Quality", "(best quality, masterpiece)").replace(
    "$LOCATION", location.strip(", ")
  )
  # Charactor2 のデータ
  NAME = ch2_name
  CLOTH = ch2_cloth
  ADDITIONAL = ch2_add
  NAME, PROMPTS, LORA, _ = data.charactor_check(NAME)
  
  base_prompt = base_prompt.replace(
    "$NAME+LORA2", f"{LORA}, {NAME}"
  ).replace(
    "$CHARACTOR2, ", PROMPTS
  ).replace(
    "$CLOTHING2, ", CLOTH
  ).replace(
    "$ADDITIONAL2, ", ADDITIONAL
  )
  
  # Charactor1 
  NAME = ch1_name
  CLOTH = ch1_cloth
  ADDITIONAL = ch1_add
  NAME, PROMPTS, LORA, _ = data.charactor_check(NAME)
  prompt = data.applicate(base_prompt, NAME, LORA, PROMPTS, CLOTH, "", "").replace("$ADDITIONAL", ADDITIONAL)
  
  prompt = data.delete_duplicate_comma(prompt)
  
  log_write("./latent_couple-log.txt", prompt, "")
  return prompt


def multidiffusion(ch1_name="",
                  ch1_cloth="",
                  ch1_add="",
                  ch2_name="",
                  ch2_cloth="",
                  ch2_add="",
                  location="",
                  quality=True):
  base_prompt = """$Charactor_Quality, 2 girls, $NAME+LORA, $CHARACTOR, $CLOTHING, $ADDITIONAL, $LOCATION,\nAND\n$Charactor_Quality, 2 girls, $NAME+LORA2, $CHARACTOR2, $CLOTHING2, $ADDITIONAL2, $LOCATION"""
  
  """
  $Quality = data.quality_data 
  $Charactor_Quality = Mini Quality Data
  """
  
  # 全体の処理
  if quality:
    base_prompt = base_prompt.replace("$Quality", f"{data.quality_data},")
    
  else:
    base_prompt = base_prompt.replace("$Quality ", "")
  
  base_prompt = base_prompt.replace("$Charactor_Quality", "(best quality, masterpiece)").replace(
    "$LOCATION", location.strip(", ")
  )
  # Charactor2 のデータ
  NAME = ch2_name
  CLOTH = ch2_cloth
  ADDITIONAL = ch2_add
  NAME, PROMPTS, LORA, _ = data.charactor_check(NAME)
  
  base_prompt = base_prompt.replace(
    "$NAME+LORA2", f"{LORA}, {NAME}"
  ).replace(
    "$CHARACTOR2, ", PROMPTS
  ).replace(
    "$CLOTHING2, ", CLOTH
  ).replace(
    "$ADDITIONAL2, ", ADDITIONAL
  )
  
  # Charactor1 
  NAME = ch1_name
  CLOTH = ch1_cloth
  ADDITIONAL = ch1_add
  NAME, PROMPTS, LORA, _ = data.charactor_check(NAME)
  prompt = data.applicate(base_prompt, NAME, LORA, PROMPTS, CLOTH, "", "").replace("$ADDITIONAL", ADDITIONAL)
  
  _, prompt = data.final_process(prompt, "./multidiffusion-log.txt")
  
  # log_write("./multi-log.txt", prompt, "")
  return prompt

def launch(ch1_name="",
                  ch1_cloth="",
                  ch1_add="",
                  ch2_name="",
                  ch2_cloth="",
                  ch2_add="",
                  location="",
                  quality=True,
                  extension=""):
  # 拡張機能次第で実行
  if extension == "Latent Couple":
    prompt = latent_couple(ch1_name,ch1_cloth,ch1_add,ch2_name,ch2_cloth,ch2_add,location,quality)
    
  elif extension == "MultiDiffusion":
    prompt = multidiffusion(ch1_name,ch1_cloth,ch1_add,ch2_name,ch2_cloth,ch2_add,location,quality)
    
  else:
    raise ValueError(f"Unknown Extension Value ({extension})")
  
  print(f"Extension Mode: {extension}")
  
  return prompt