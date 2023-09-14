def e():
  if __name__ == "__main__":
    raise ValueError("正しい値を入力してください")
  else:
    print("値が正しくありません。")
    
def Masturbation_gen(charactor_name,
                     charactor_prompt,
                     charactor_clothing,
                     draw_position="",
                     prompt_type="Solo", # or yuri
                     face_type="blush", # or orgasm or 露出えっち
                     on_bed=False,
                     is_nude=False,
                     on_vibrator=False,
                     important_solo=True,
                     more_nsfw=False,
                     masturbation_type="Fingering" # or tables
                     ):
  # 前処理
  if prompt_type=="Solo" or prompt_type == "一人えっち":
    if masturbation_type == "Fingering":
      prompt = "<lora:solo_masturbation_normal-masturbation:1.0>, nsfw, masturbation, (best quality, masterpiece, detailed, incredibly fine illustration, kawaii), nsfw, masturbation, (isnude)(onbed)fingering, schlick, pussy, pussy juice, trembling, female focus, (FACES), (キャラクタープロンプト), (服装プロンプト), 1girl', (場所関連)" # 要研究
      
      print("Selected Template Type: \"Solo Fingering (一人指マン)\"")
    
    elif masturbation_type == "tables":
      prompt = ""
      
      print("Selected Template Type: \"Solo Table Masturbation (一人角えっち)\"")
      
    else:
      e()
      
  elif prompt_type=="yuri" or prompt_type == "百合えっち":
    prompt = ""
    
  else:
    e()
    
  # 変数の HR化
  NAME = charactor_name.strip()
  CHARACTOR_PROMPT = charactor_prompt.strip()
  CLOTH = charactor_clothing.strip()
  FACE = face_type.lower().strip()
  
  # 変換
  prompt = prompt.replace(
    # キャラクタープロンプトの変更
    "(キャラクタープロンプト)", f"<lora:hoshino1:1.0>, {NAME}, {CHARACTOR_PROMPT}"
  ).replace(
    # 表情タイプ
    "(FACE_TYPE)", face_type
    )
  
  # is nude?
  if is_nude:
    prompt = prompt.replace("(isnude)", "nude, ")
  else:
    prompt = prompt.replace("(isnude)", "")
  
  # on bed?
  if on_bed:
    prompt = prompt.replace("(onbed)", "on bed, sitting on bed, ")
  else:
    prompt = prompt.replace("(onbed)", "")
  
  # more nsfw?
  if more_nsfw:
    prompt = prompt.replace(
      # nsfw, masturbation, LoRA Weightの強化、強調
      "<lora:solo_masturbation_normal-masturbation:1.0>, nsfw, masturbation,", "<lora:solo_masturbation_normal-masturbation:1.2>, (nsfw), (masturbation), female masturbation,"
    ).replace(
      # 強制orgasm化、pussy強調
      "pussy, pussy juice,", "(pussy), pussy juice,"
    )
    FACE = "orgasm"
  
  # face is?
  if face_type == "露出えっち":
    FACE = "sad, blush, (orgasm)" 
  prompt = prompt.replace("(FACES)", FACE)
  
  # 絶対に一人である必要が？
  if important_solo:
    prompt = prompt.replace("1girl'", "(((1girl)))")
    
  else:
    prompt = prompt.replace("1girl'", "1girl")
    
  # 服装設定
  prompt = prompt.replace("(服装プロンプト)", charactor_clothing)
  
  # 場所指定
  prompt = prompt.replace("(場所関連)", draw_position)
  
  # On Vibrator
  
  new_prompt = prompt.replace("<", "\\<").replace(">", "\\>")
  return_prompt = f"| Prompt |\n| --- |\n| {new_prompt} |"
  
  return return_prompt