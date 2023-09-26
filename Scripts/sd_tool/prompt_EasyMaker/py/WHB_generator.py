import datetime as d

def e():
  if __name__ == "__main__":
    raise ValueError("正しい値を入力してください")
  else:
    print("値が正しくありません。")


def WHB_Generator(ch_n, ch_p, ch_wp, template_id="1", face_type="blush", use_adetailer="0", powerful_whb="0", on_vibrator="0", easy_cloth="0"):
  if template_id == "1" or template_id == "着衣h":
    prompt = "<lora:whb:1>, nsfw, whb, (best quality, masterpiece, detailed, incredibly fine illustration, kawaii), blush, full body, pussy, pussy juice, nipple, female focus, (キャラクタープロンプト), (服装プロンプト), looking at viewer, skirt, miniskirt, bare breasts, 14 years old, baby face:0.7, 2dimensional-charactor, trembling, straddling the whb, 1girl"

    print("Using Template \"着衣h\"")
    
  elif template_id =="2" or template_id == "服なんていらない☆":
    prompt = "<lora:whb:1>, nsfw, whb, nude, (best quality, masterpiece, detailed, incredibly fine illustration, kawaii), blush, full body, pussy, pussy juice, nipple, female focus, (キャラクタープロンプト), looking at viewer, nude, bare breasts, 14 years old, baby face:0.7, 2dimensional-charactor, trembling, straddling the whb, 1girl"

    print("Using Template \"服なんていらない☆\"")
  
  else:
    e()

  # 修正
  adetailer_prompt = ""
  ch_prompt_ = ch_p.lower().strip().replace("1girl, ", "")
  ch_name = ch_n.lower().strip()
  ch_prompt = f"<lora:MODEL:1.0>, {ch_name}, {ch_prompt_}"
  ch_wearing_prompt = ch_wp.lower().strip()
  
  # 埋め込み
  new_prompt = prompt.replace("(キャラクタープロンプト)", ch_prompt).replace("(服装プロンプト)", ch_wearing_prompt)
  
    # 指定されているならば
  if face_type.strip() == "orgasm":
    new_prompt = new_prompt.replace("kawaii), blush, full", "kawaii), orgasm, full")
  
  # 服装なんていらない？
  if template_id=="2":
    new_prompt = new_prompt.split("|CUTOFF,")[0]
  
  # ADetailerも変更する？
  if use_adetailer == "1":
    adetailer_prompt = "(best quality)++, (masterpiece)++, (kawaii:1.1), cute, baby face:0.6, Consistent and proportionate facial features, High-Quality facial textures, <blush/orgasm>, <eyes>"
    
    adetailer_prompt = adetailer_prompt.replace("<blush/orgasm>", face_type).replace(", <eyes>", "")
    
  elif use_adetailer == "0":
    adetailer_prompt = "(best quality)++, (masterpiece)++, (kawaii:1.1), cute, baby face:0.6, Consistent and proportionate facial features, High-Quality facial textures"
  
  else:
    e()
    
  # Powerful WHB
  if powerful_whb == "1":
    new_prompt = new_prompt.replace("nsfw, whb", "(nsfw), (whb)").replace("<lora:MODEL:1.0>", "<lora:MODEL:0.875>")
    
  # On Vibrator
  if on_vibrator == "1":
    new_prompt = new_prompt + ", <lora:vibrator-vibrator_on_nipple-vibrator_under_clothes-etc:0.95>, vibrator on nipples"
    
  # Easy Clothes
  if easy_cloth == "1":
    new_prompt = new_prompt + ", bare breasts:1.1, <lora:bobsout1:0.65>"
  
  if __name__ == "__main__":
    return new_prompt, adetailer_prompt
  else:
    # ログに残す
    date = d.datetime().now()
    with open("./WHB_Generator_logs.txt", "a") as f:
      f.write(f"\ndate: {str(date)}\nPrompt ${new_prompt}\nADetailer Prompt ${adetailer_prompt}\n")
    
    new_prompt = new_prompt.replace("<", "\\<").replace(">", "\\>")
    return f"| Prompt |\n| --- |\n| {new_prompt} |", f"| ADetailer |\n| --- |\n| {adetailer_prompt} |"
  
if __name__ == "__main__":
  def isnone_bool(x):
    if x == "":
      return True
    else:
      return False
  
# 入力を受け取る
  ch_n = input("Charactor Prompt Name (e.g: 10ma_s): ")
  ch_detect_prompt = input("Charactor Prompt: ")
  use_template = input("Using Template (1 / 2): ")
  ch_wp = input("服装プロンプト 省略可 未入力で \"black serafuku\": ")
  if isnone_bool(ch_wp):
    ch_wp = "black serafuku, grey serafuku"
  face_type = input("表情タイプ (blush / orgasm) 省略可 未入力で \"blush\": ")
  if isnone_bool(face_type):
    face_type = "blush"
  ad_modify = input("ADetailer 表情プロンプトの変更 (目の色とかの反映) (0 / 1) 省略可 未入力で \"0\": ")
  if isnone_bool(ad_modify):
    ad_modify = "0"
  powerful_whb = input("WHB描画の強化 (0 / 1) 小ry買うか  未入力で \"0\"")
  if isnone_bool(powerful_whb):
    powerful_whb = "0"
  on_vibrator = input("胸バイブ (0 / 1) 省略可 未記入で \"0\"")
  if isnone_bool(on_vibrator):
    on_vibrator = "0"

# 関数実行!
  returns, adetailer = WHB_Generator(ch_n, ch_detect_prompt, ch_wp, use_template, face_type, ad_modify, powerful_whb, on_vibrator)
  
# プリントアウト
  print(returns)