"""
prompt_config.json
{session_number: str.06d
 last_session: str (last session path)
}

"""

  
# 初期処理
write_dict = {}
db_list = []
spf_dict = {"title": title}
get_config = False
  # とりあえずユーザーからの入力を受け取る
import LGS.misc.re_finder as re
import hashlib
import random
import LGS.misc.compact_input as cin
import LGS.misc.nomore_oserror as los
save_dir = input("Save Config Name: ")
if cin.isnone(save_dir):
  save_dir = hashlib.sha1("{:06d}".encode().format(random.randrange(0, 1000000))).hexdigest()
else:
  save_dir = los.filename_resizer(save_dir, replaceTo="_")
save_dir = f"{save_dir}-{random.randrange(0,10000)}_{hashlib.sha1(save_dir.encode()).hexdigest()}.json"

  # なきゃいけない
import os
os.makedirs("./cache", exist_ok=True)

    # 存在するなら前回の設定を読み込み
import LGS.misc.jsonconfig as jsoncfg
if os.path.exists("./cache/prompt_config.json"):
  config = jsoncfg.read("./cache/prompt_config.json")
  last_data_dir = config["last_session"]
  if os.path.exists(last_data_dir):
    last_data = jsoncfg.read(last_data_dir)
    get_config = True
    session_nums = int(config["session_number"])
    session_nums += 1
    session_num = "{:06d}".format(session_nums)
    prompt_config_savedict = {
      "session_number": session_num,
      "last_session": save_dir
    }
    # 作る
    jsoncfg.write(prompt_config_savedict, "./cache/prompt_config.json")
  else:
    get_config = False
    config = {}
    
  # 存在しないなら
if not get_config:
  session_num = "{:06d}".format(0)
  prompt_config_savedict = {
    "session_number": session_num,
    "last_session": save_dir
  }
  # 作る
  jsoncfg.write(prompt_config_savedict, "./cache/prompt_config.json")

def title(x):
  global n
  # ナンバーを取得
  if get_config:
    num = int(config[session_num])
  else:
    num = int(session_num)
  
  titles = f"{num}. {n}"
  return {f"title": titles}
  
# 関数 (前処理)
def prpc(out_name,  # プリント時の表示名前 
         value, # インプット値
         config_out="", # cfg書き込み時の表示名
         isboolean=False, # 0 / 1 処理
         special_function=False, # 結果によって追加処理
         special_functions="None"  #追加処理の名前
         ):
  global spf_dict
  global write_dict
  global db_list
  rdict = {}
  # config_out が空かどうか 
  if config_out == "":
    config_out = out_name.lower().replace(" ", "_")
  
  # Valueがからかどうか
  if value == "" and get_config == True:
    value = last_data[config_out]
    isboolean = False # 空なら取得
    
  # boolかどうか
  if isboolean:
    if value == "0":
      value = "False"
      rb = False
    elif value == "1":
      value = "True"
      rb = True
    else:
      print("値が不明です。 0 または 1 を入力してください。")
      value = "Unknown"
      rb = False
  else:
    # 違うなら
    if isinstance(value, (float, int)): 
      # float, int型を持つ場合
      value = str(value)
    # LoRAモデルの摘出
    # if config_out == "prompt":
    #   find_lora = re.extract(r"<lora:([\d\w\s,]+):([\d.]+)>", value)
    #   if find_lora:
    #     lora_name = find_lora.group(1)
    #     lora_weight = find_lora.group(2)
  
  # 特殊関数
  if special_function:
    if isboolean: # boolであるなら
      if rb: # True なら
        if special_functions == "None":
          # special_functions がないなら
          print("Special Functionsが指定されていません。")
        else:
          rdict = spf_dict[special_functions](True)
      elif not rb: # Falseなら
        if special_functions == "None":
          # special_functions がないなら
          print("Special Functionsが指定されていません。")
        else:
          rdict = spf_dict[special_functions](False)
    elif not isboolean:
      if special_functions == "None":
        print("Special Functionsが指定されていません。")
      else:
        rdict = spf_dict[special_functions](value)
  
  # 最後の処理
  # 辞書に追加
  db = (out_name, config_out, value)
  db_list.append(db)
  # write_dict[config_out] = value
  write_dict[db[1]] = db[2]
  
  # プリントアウト用の処理
  if not len(rdict) > 0:
    prout = f"{out_name}: {value}"
    return prout
  elif len(rdict) > 0: # rdictが存在するなら
    prouts = []
    rdict_w = {}
    prout = f"{out_name}: {value}"
    prouts.append(prout)
    for kx, vx in rdict.items():
      # コンフィグ用に変更  
      kxcfg = kx.lower().replace(" ", "_")
      rdict_w[kxcfg] = vx
      
      # プリントアウト用
      pr = f"{kx}: {vx}"
      prouts.append(pr)
      
    write_dict.update(rdict_w)
    return prouts
  # キャッチされなかったら
  print(f"Error: Skipped function with {out_name}")
  return -1

# メイン入力制御
print("何も入力しなかった場合、前回に入力した内容が使用されます。\n")
n = input("0. Title: ")
name = prpc("", n, "title", special_function=True, special_functions="title")
n = input("1. Prompt: ")
prompt = prpc("Prompt", n)
n = input("2. Negative Prompt: ")
negative = prpc("Negative Prompt", n, "negative")
n = input("3. Width: ")
w = prpc("Width", n)
n = input("4. Height: ")
h = prpc("Height", n)
resolution = f"{w}x{h}"
n = input("5. Batch Size: ")
bs = prpc("Batch Size", n)
n = input("6. Batch Count: ")
bc = prpc("Batch Count", n)
n = input("7. CFG Scale: ")
cfg = prpc("CFG Scale", n)
n = input("8. Seed: ")
seed = prpc("Seed", n)
### Seed 追加設定未実装
n = input("9. Restore Faces (0 / 1): ")
rs_face = prpc("Restore Faces", n, "restore_face", True)
n = input("10. Tilling (0 / 1): ")
tilling = prpc("Tilling", n, isboolean=True)
n = input("11. Hires.fix (0 / 1): ")
h_fix = prpc("Hires.fix", n, "hires_fix", True)
### Hires.fix 追加設定未実装
n = input("12. Sampling Method: ")
sm = prpc("Sampling Method", n)
n = input("13. Sampling Steps: ")
ss = prpc("Sampling Step", n)
n = input("14. ")

jsoncfg.write(write_dict, f"./cache/{save_dir}")

printed = f"""\
<details><summary>{name}</summary>

| 設定 | 値 | 
| --- | --- | 
| Prompt | <details><summary>click to open</summary> {prompt} </details> |
| Negative | <details><summary>click to open</summary> {negative} </details> |
| Resolution | {resolution} |
| Batch Size | {bs} |
| Batch Count | {bc} |
| CFG Scale | {cfg} |
| Seed | {seed} |
| Restore Faces | {rs_face} |
| Tilling | {tilling} |
| Hires.fix | {h_fix} |
| Sampling Method | {sm} |
| Sampling Steps | {ss} |

</details>

"""