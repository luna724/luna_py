import log_writer
import simple_generator as data

def Tentacle_ALL(
  charactor_name="",
  charactor_prompt="",
  charactor_Lora="",
  charactor_DrawAt="",
  charactor_Clothing="",
  face_type="", # [blush, orgasm, blush+], 
  tentacle_type="", # [Horosuke, ICEJelly]
  print_negative_ad=False
):
  p = f"nsfw, $TENTACLE_MODEL, (tentacles), tentacles, nipples, small nipples, cowboy shot, $FACE, $NAME+LORA, {data.quality_data}, $LOCATION, $CHARACTOR, $CLOTHING, "
  
  ch_lora = charactor_Lora.strip()
  ch_prompt = charactor_prompt.lower().strip()
  ch_name = charactor_name.lower().strip()
  ch_cloth = charactor_Clothing.strip()
  ch_locate = charactor_DrawAt.strip()
  
  ch_name, ch_prompt, ch_lora, isTemplate = data.charactor_check(ch_name)
  
  NAME = ch_name
  LORA = ch_lora
  PROMPTS = ch_prompt
  CLOTH = ch_cloth
  LOCATION = ch_locate
  FACE = data.facetype(face_type)
  
  prompt = data.applicate(p, NAME, LORA, PROMPTS, CLOTH, LOCATION, FACE)
  negative = "badhandv5, mosaic, (worst quality, low quality:1.3), (depth of field, blurry:1.2), (greyscale, monochrome:1.1), 3D face, nose, cropped, lowres, text, jpeg artifacts, signature, watermark, username, blurry, artist name, trademark, watermark, title, multiple view, Reference sheet, Mosaic, Hide pussy, line of revision"
  adetailerp = "(best quality)++, (masterpiece)++, (kawaii:1.1), cute, baby face:0.6, Consistent and proportionate facial features, High-Quality facial textures"
  adetailerneg = "(bad anatomy:1.4), (distorted features:1.1), (realistic:1.1), (low quality, worst quality:1.1), lips, unclear face, Distorted facial features, Jagged lines in faces"
  
  if tentacle_type == "Horosuke":
    prompt = prompt.replace("$TENTACLE_MODEL", "<lora:chushou111:1.1>")
  
  elif tentacle_type == "ICEJelly":
    prompt = prompt.replace("$TENTACLE_MODEL", "<lora:chushou:1.0>")
  
  else:
    raise ValueError("NOT Matching tentacle_type")

  prompt = data.delete_duplicate_comma(prompt)
  
  new_prompt = prompt.replace("<", "\\<").replace(">", "\\>")
  return_prompt = data.return_markdown(new_prompt)
  log_writer.w("./tentacles_all.py-log.txt", prompt, "")
  
  if print_negative_ad:
    add_markdown = data.plusnegativeplusadetailer(negative, adetailerp, adetailerneg)
    
    return f"{return_prompt}\n{add_markdown}"
  
  return return_prompt