""" 
入力
{"なんかしら英語4文字(小文字)": ["モデル名", "タイプ (Lora / Lycoris / sd.cp / vae / t_inv)", "拡張子", "DL URL", "NSFW (0 / 1)",
"Site Name", "Trigger Word (list)", "Sample Image URL", "Image Generation Data", "CivitAI Site URL"}

出力
1.
!wget <URL> -O <dir>/<TYPE>/<FILE_NAME>.<EXTENSION>

2.
Download_<MODEL_NAME><IS_NSFW> = False #@param {"type":boolean}

3.
if Download_<MODEL_NAME><IS_NSFW>:
  !cp -r <dir>/<TYPE>/<FILE_NAME>.<EXTENSION> <dir2>/<TYPE>/<FILE_NAME>.<EXTENSION>

4.
"<manipuate_value>": ["<MODEL_SITE_NAME>", "[<TRIGGER_WORD>]", "?", "None", "<Sample Image>", "<image generation data>", "<CivitAI URL>"]

"""
# ゴミ処理 + 定義
import os
if os.path.exists("./in/out.txt"):
  os.remove("./in/out.txt")
x = 0
wgets, params, if_strs, lora_infovwrs, li2 = [], [], [], [], []
data_list = []
dir = "/content/gdrive/MyDrive/SD_Model"
dir2 = "/content/stable-diffusion-webui"

# とりあえず受け取ろうではないか
import LGS.misc.jsonconfig as jc
import LGS.misc.compact_input  as cin

datas = jc.read("./in/json.json")


# 辞書のアイテム数を取得
d_item = len(datas)
print(f"{d_item}のインプットを受け取りました。")
sdcp_db = {}

# 摘出
for k, d in datas.items():
  x += 1
  print(f"""Starting Extract line{x}.\n""")
  # ("{k}": {d})""")
  # まず、文字数制限をチェック
  if len(k) == 4:
    # 次に、リスト数が正常かどうか
    if len(d) == 10:
      # ここに摘出処理
      # 別辞書に代入
      data = {}
      data["name"] = k
      data["MODEL_NAME"] = d[0]
      data["TYPE"] = d[1]
      data["EXTENSION"] = d[2]
      data["URL"] = d[3]
      data["IS_NSFW"] = cin.tfgen(d[4])
      data["FILE_NAME"] = d[0].lower().strip()
      data["MANIPUATE"] = d[0].replace("_", " ")
      data["SITE_NAME"] = d[5]
      data["TRIGGER_WORD"] = d[6]
      data["SAMPLE_IMG"] = d[7]
      data["IMG_GEN_DATA"] = d[8]
      data["SITE_URL"] = d[9]
      
      data_list.append(data)
      
    else:
      print(f"Failed line{x}.\n \
        Not Matching Value list len (!= 10)  Skipped..")
      continue
  else:
    print(f"Failed line{x}.\n \
      Not Matching key len (!= 4)  Skipped..")
    continue

#print(f"Visualized Data: {data_list}")

# 変換処理
for x in data_list:
  # 前処理
  if not x["URL"].startswith("http"):
    print("不明なタイプです。 \"URL\" \n(http)で始まっていません。")
    continue
  if x["TYPE"] == "Lora":
    TYPE = "LoRA/"
    TYPE_D2 = "models/Lora"
  elif x["TYPE"] == "lycoris":
    TYPE = "LyCORIS/"
    TYPE_D2 = "models/Lora"
  elif x["TYPE"] == "sd.cp":
    TYPE = ""
    TYPE_D2 = "models/Stable-diffusion" # Stable-diffusion/
  elif x["TYPE"] == "vae":
    TYPE = "VAE/"
    TYPE_D2 = "models/Stable-diffusion"
  elif x["TYPE"] == "t_inv":
    TYPE = "Texture_Inversion/"
    TYPE_D2 = "embeddings"
  else:
    print("不明なタイプです。\"TYPE\" \n(Lora / Lycoris / sd.cp / vae)を入力してください。")
    continue
  
  if x["IS_NSFW"] == "False":
    IS_NSFW = ""
  elif x["IS_NSFW"] == "True":
    IS_NSFW = "_nsfw"
  else:
    print("不明なタイプです。\"IS_NSFW\" \n(0 / 1)の文字列を入力してください。")
    continue
  
  if x["TYPE"] == "vae":
    wget = f'\
!wget "{x["URL"]}" -O "{dir}/{TYPE}{x["FILE_NAME"]}.vae.{x["EXTENSION"]}"'
  
  else:
    wget = f'\
!wget "{x["URL"]}" -O "{dir}/{TYPE}{x["FILE_NAME"]}.{x["EXTENSION"]}"'
  
  param = f'\
Download_{x["MODEL_NAME"]}{IS_NSFW} = False #@param {{type: "boolean"}}'
  
  if_str = f'\
if Download_{x["MODEL_NAME"]}{IS_NSFW}:\n\
  !cp -r "{dir}/{TYPE}{x["FILE_NAME"]}.{x["EXTENSION"]}" "{dir2}/{TYPE_D2}/{x["FILE_NAME"]}.{x["EXTENSION"]}"'
  
  # Lora の場合のみ追加
  if x["TYPE"] == "Lora" or x["TYPE"] == "lycoris":
    lora_infovwr = f'\
"{x["MANIPUATE"].lower()}": ["{x["SITE_NAME"]}", ["{x["TRIGGER_WORD"][0]}"], "?", "None", "{x["SAMPLE_IMG"]}", """{x["IMG_GEN_DATA"]}""", "{x["SITE_URL"]}"],' 

    lora_infovwr2 = f'\
"{x["MANIPUATE"]}", '
    lora_infovwrs.append(lora_infovwr)
    li2.append(lora_infovwr2)
      
  wgets.append(wget)
  params.append(param)
  if_strs.append(if_str)
  
  # CP なら
  if x["TYPE"] == "sd.cp":
    add_sdcp = {}

    add_sdcp = {
      "Site Name": x["SITE_NAME"],
      "URL": x["SITE_URL"],
      "VAE": "Recommended VAE",
      "Offical Sample": x["SAMPLE_IMG"], # Image src Path (<img src="">)
      "Sample Image1": "./loradata/image_sdcp/sample1/.png", # from /sd_tool/prompt_easymaker/py/
      "Sample Image2": "./loradata/image_sdcp/sample2/.png",
      "Sample Image3": "./loradata/image_sdcp/sample3/.png",
      "Compability": "Unknown",
      "MODEL_TYPE": [10.0,10.0,10.0,10.0] # 2Dimensional  Cute  NSFW  Detailed
    }
    print("SDCP Updated!")#, add_sdcp)
    
    sdcp_db[x["MANIPUATE"]] = add_sdcp

  
wg = f"--- wget(onetime) ---\n"
pa = f"\n\n--- Boolean ---\n"
ifs = f"\n\n--- Download ---\n"
lis = f"\n\n--- Lora Info Viewer ---\n"
lis2 = f"\n\n--- Lora Info Viewer List ---\n"

for w in wgets:
  wg = wg + w + "\n"
  
for p in params:
  pa = pa + p + "\n"
  
for i in if_strs:
  ifs = ifs + i + "\n"

for l in lora_infovwrs:
  lis = lis + l + "\n"
  
for l2 in li2:
  lis2 = lis2 + l2
  
jc.write_text(f"{wg}{pa}{ifs}{lis}{lis2.strip(', ')}", "./in/out.txt", overwrite=False)

# database を更新
# os.chdir("..\\")
# os.chdir("..\\")
# os.chdir("./sd_tool/prompt_EasyMaker/py/database")

# Checkpoint
if os.path.exists("./in/sdcp.json"):
  previous_data = jc.read("./in/sdcp.json")
  previous_data.update(sdcp_db)
else:
  previous_data = sdcp_db
jc.write(previous_data,"./in/sdcp.json")
