from simple_generator import jsoncfg

# 定義
data = jsoncfg.read("./database/sdcp.json")

# 小文字キーと通常キーを結び付け
# 小文字キーから data の値を呼び出せるように
low_key_data = {}
for k, d in data.items():
  low_key_data[k.lower()] = k

cp_list = list(data.keys())
low_cplist = list(low_key_data.keys())

def generate(model):
  # もし見つからなかったら
  if model == "Error?MODELNOTFOUND".lower():
    print("モデルが見つかりませんでした。")
    raise ValueError("Model Not Found")  
  
  # 摘出
  negative = "<strong_> EasyNegative, (realistic, low quality, worst quality:1.2), badhandv5 </strong>"
  key = low_key_data[model]
  dt = data[key]
  
  TITLE = dt["Site Name"]
  DESCRIPTION = ""
  URL = dt["URL"]
  VAE = dt["VAE"]
  SAMPLE_OFFICAL = dt["Offical Sample"]
  SAMPLE_SIMPLE = dt["Sample Image1"]
  SAMPLE_CUTE = dt["Sample Image2"]
  SAMPLE_RND = dt["Sample Image3"]
  COMPABILITY = dt["Compability"]
  MODEL_TYPE = dt["MODEL_TYPE"]
  
  markdown_up = f"""
  # {TITLE}

  {DESCRIPTION}
  
  ## Sample Images
  
  | Sample Image Info | Image |   
  | --- | --- |
  | Offical Sample Image | <img src="{SAMPLE_OFFICAL}"> |
  """
  
  md_simple = f"""
  Simply Image
  
  - Prompt
    <strong>nahidadef, <lora:nahida1:0.75>, 1girl, solo, smile, blush, shy, no background, simple background, white background, standing, looking at viewer, small breasts, 14 years old, baby faces:0.7, slim, masterpiece, best quality, rori, cute, kawaii, </strong>
  
  - Negative
    {negative}
  
  - ADetailer
    None
  
  Seed: 85
  """
  
  md_cute = f"""
  Cute Naked Coat
  
  - Prompt
    <strong>nahidadef, <lora:nahida1:0.625>, 12 years old, 1girl, solo, shy, baby face:0.75, lying on bed, naked coat, white coat, nude, pussy, nipples, small breasts, blush, looking at away, slim, masterpiece, best quality, rori, cute, kawaii, nsfw, white tights, zettai ryouiki, <lora:masusu_breast:0.65> </strong>
    
  - Negative
    {negative}
    
  - ADetailer
    None
  
  Seed: 85
  """
  
  md_rnd = f"""
  Model Default
  
  - Prompt
    <strong>1girl, solo, cute, kawaii, masterpiece, best quality, looking at viewer, white wing, 14 years old, white hair, aqua eyes, ocean, </strong>
  
  - Negative
    <strong> EasyNegative, badhandv5, (low quality, worst quality:1.1) </strong>
  
  - ADetailer
    None
    
  Seed: 85
  """
  
  md_down = f"""
  Recommended VAE: {VAE}
  LoRA Compability Rate: {COMPABILITY} / 10.0
  
  Offical Site: {URL}
  """
  
  return markdown_up, md_down, md_simple, md_cute, md_rnd, SAMPLE_SIMPLE, SAMPLE_CUTE, SAMPLE_RND