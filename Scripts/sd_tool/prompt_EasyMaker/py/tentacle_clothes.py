import simple_generator as date
import log_writer

def Tentacle_Clothes_Generator(
                               ch_p="", 
                               ch_wp="", 
                               ch_lora="<lora:Example>",
                               ch_draw="",
                               face_type="blush", # or orgasm or blush+
                               ch_n="Original", # or charactor_name
                               more_nude=False,
                               more_tentacle=False):
  p = f"nsfw, <lora:tentacle_clothes:1.2>, (tentacle clothes:1.2), tentacles, nipples, small nipples, cowboy shot, $FACE, $NAME+LORA, $LOCATION, {date.quality_data}, $CLOTHING, $CHARACTOR"
  ch_lora = ch_lora.strip() #.replace("<", "\\<").replace(">", "\\>")
  ch_p = ch_p.lower().strip()
  ch_n = ch_n.lower().strip()
  cloth = ch_wp.strip()
  location = ch_draw.strip()
  
  # ch_n がオリジナルなら
  if not ch_n in date.available_name:
    use_ch_template = True
    ch_n = ""
  
  else:
    use_ch_template = False
    ch_p = date.charactor_prompt[ch_n]
    ch_lora = date.charactor_lora[ch_n][0]
    ch_n = date.charactor_lora[ch_n][1]
    
  
  # 変数を読みやすく
  NAME = f", {ch_n}" 
  LORA = ch_lora
  CHARACTOR_PROMPT = ch_p
  CLOTH = f"{cloth}"
  LOCATION = f"{location}"
  FACE = face_type
  
  if use_ch_template:
    NAME = ""
  # 変換
  if FACE == "blush+":
    FACE = "sad, (orgasm), blush, wink"
  
  prompt = p.replace(
    # キャラクターの設定
    "$CHARACTOR", CHARACTOR_PROMPT
  ).replace(
    "$NAME+LORA", f"{LORA}{NAME}"
  ).replace(
    # 表情
    "$FACE", FACE
  ).replace(
    # 服装
    "$CLOTHING, ", CLOTH
  ).replace(
    # 場所
    "$LOCATION, ", LOCATION
  )
  
  # Nude, Tentacle
  #if more_nude:
  #  prompt = prompt.replace(
  #    "$NUDE+", "")
  
  if more_tentacle:
    prompt = prompt.replace(
      "(tentacle clothes:1.2), tentacles, ", "(tentacle clothes:1.35), (tentacles), "
    )

 # else:
 #   prompt = prompt.replace("$MORE_TENTACLE, ", "")
    
    
  new_prompt = prompt.replace("<", "\\<").replace(">", "\\>")
  return_prompt = f"| Prompt |\n| --- |\n| {new_prompt} |"
  log_writer.w("./tentacle_clothes.py-log.txt", prompt, "")
  
  return return_prompt