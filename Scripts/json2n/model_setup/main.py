""" 
入力
{"なんかしら英語4文字(小文字)": ["モデル名", "タイプ (Lora / Lycoris)", "拡張子", "DL URL", "NSFW (0 / 1)", "モデルファイル名"]}

出力
1.
!wget <URL> -O <dir>/<TYPE>/<FILE_NAME>.<EXTENSION>

2.
Download_<MODEL_NAME><IS_NSFW> = False #@param {"type":boolean}

3.
if Download_<MODEL_NAME><IS_NSFW>:
  !cp -r <dir>/<TYPE>/<FILE_NAME>.<EXTENSION> <dir2>/<TYPE>/<FILE_NAME>.<EXTENSION>
"""
# ゴミ処理 + 定義
import os
if os.path.exists("./in/out.txt"):
  os.remove("./in/out.txt")
x = 0
wgets, params, if_strs = [], [], []
data_list = []
dir = "/content/gdrive/MyDrive/SD_Model"
dir2 = "/content/stable-diffusion-webui/models"

# とりあえず受け取ろうではないか
import LGS.misc.jsonconfig as jc
import LGS.misc.compact_input  as cin

datas = jc.read("./in/json.json")


# 辞書のアイテム数を取得
d_item = len(datas)
print(f"{d_item}のインプットを受け取りました。")

# 摘出
for k, d in datas.items():
  x += 1
  print(f"""Starting Extract line{x}.\n \
    ("{k}": {d})""")
  # まず、文字数制限をチェック
  if len(k) == 4:
    # 次に、リスト数が正常かどうか
    if len(d) == 6:
      # ここに摘出処理
      # 別辞書に代入
      data = {}
      data["name"] = k
      data["MODEL_NAME"] = d[0]
      data["TYPE"] = d[1]
      data["EXTENSION"] = d[2]
      data["URL"] = d[3]
      data["IS_NSFW"] = cin.tfgen(d[4])
      data["FILE_NAME"] = d[5]
      
      data_list.append(data)
      
    else:
      print(f"Failed line{x}.\n \
        Not Matching Value list len (!= 6)  Skipped..")
      continue
  else:
    print(f"Failed line{x}.\n \
      Not Matching key len (!= 4)  Skipped..")
    continue

print(f"Visualized Data: {data_list}")

# 変換処理
for x in data_list:
  # 前処理
  if not x["URL"].startswith("http"):
    print("不明なタイプです。 \"URL\" \n(http)で始まっていません。")
    continue
  if x["TYPE"] == "Lora":
    TYPE = "LoRA/"
    TYPE_D2 = "Lora"
  elif x["TYPE"] == "Lycoris":
    TYPE = "LyCORIS/"
    TYPE_D2 = "LyCORIS"
  elif x["TYPE"] == "sd.cp":
    TYPE = ""
    TYPE_D2 = "stable-diffusion"
  else:
    print("不明なタイプです。\"TYPE\" \n(Lora / Lycoris / sd.cp)を入力してください。")
    continue
  
  if x["IS_NSFW"] == "False":
    IS_NSFW = ""
  elif x["IS_NSFW"] == "True":
    IS_NSFW = "_nsfw"
  else:
    print("不明なタイプです。\"IS_NSFW\" \n(0 / 1)の文字列を入力してください。")
    continue
    
  wget = f'\
!wget "{x["URL"]}" -O "{dir}/{TYPE}{x["FILE_NAME"]}.{x["EXTENSION"]}"'
  
  param = f'\
Download_{x["MODEL_NAME"]}{IS_NSFW} = False #@param {{type: "boolean"}}'
  
  if_str = f'\
if Download_{x["MODEL_NAME"]}{IS_NSFW}:\n\
  !cp -r "{dir}/{TYPE}{x["FILE_NAME"]}.{x["EXTENSION"]}" "{dir2}/{TYPE_D2}/{x["FILE_NAME"]}.{x["EXTENSION"]}"'
      
  wgets.append(wget)
  params.append(param)
  if_strs.append(if_str)
  
wg = f"--- wget(onetime) ---\n"
pa = f"\n\n--- Boolean ---\n"
ifs = f"\n\n--- Download ---\n"

for w in wgets:
  wg = wg + w + "\n"
  
for p in params:
  pa = pa + p + "\n"
  
for i in if_strs:
  ifs = ifs + i + "\n"
  
jc.write_text(f"{wg}{pa}{ifs}", "./in/out.txt", overwrite=False)
