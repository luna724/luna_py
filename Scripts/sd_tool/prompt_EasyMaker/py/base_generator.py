import log_writer
import simple_generator as data

def Base(
  charactor_name="",
  charactor_prompt="",
  charactor_lora="",
  charactor_DrawAt="",
  charactor_Cloth="",
  additional_prompt="",
  face_type="",
  #addition_list=[], # COMING SOON..
  print_negative_ad=False
):
  p = f"$NAME+LORA, $CHARACTOR, $FACE, $CLOTHING, $LOCATION, $ADDITIONAL, {data.quality_data}"
  
  LORA = charactor_lora
  PROMPTS = charactor_prompt.lower()
  NAME = charactor_name.lower()
  CLOTH = charactor_Cloth
  LOCATION = charactor_DrawAt
  FACE = face_type
  
  NAME, PROMPTS, LORA, _ = data.charactor_check(NAME)
  
  prompt = data.applicate(p, NAME, LORA, PROMPTS, CLOTH, LOCATION, FACE).replace("$ADDITIONAL, ", additional_prompt.strip())
  
  negative = "(EasyNegative), badhandv4, (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, sad, (inaccurate limb:1.2), (Low resolution:1.1), Tint shift, Image blurring, JPEG artifacts, Hidden elements, Missing areas, Unnatural proportions, Botched facial expressions, Messy hair depiction:1.15, Coarse drawing touches, Depiction of more than two people, Text, Signatures, Usernames, Mirrors, character assimilated into background, no human, shading off, collar, unclear face, Blurry faces, Misaligned facial proportions, chinese clothes, dress, fused fingers, (see through:1.5), stockings, knee-highs, particle"
  adp = "(best quality)++, (masterpiece)++, (kawaii:1.1), cute, baby face:0.6, Consistent and proportionate facial features, High-Quality facial textures"
  adn = "(bad anatomy:1.4), (distorted features:1.1), (realistic:1.1), (low quality, worst quality:1.1), lips, unclear face, Distorted facial features, Jagged lines in faces"
  
  prompt = data.delete_duplicate_comma(prompt)
  
  new_prompt = prompt.replace("<", "\\<").replace(">", "\\>")
  return_prompt = data.return_markdown(new_prompt)
  log_writer.w("./base_generator.py-log.txt", prompt, "")
  
  if print_negative_ad:
    add_markdown = data.plusnegativeplusadetailer(negative, adp, adn)
    
    return f"{return_prompt}\n{add_markdown}"
  
  return return_prompt