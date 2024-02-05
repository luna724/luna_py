# 入力jsonの形式
eg_json = {
  "anyint": {
    "displayName": "モデル表示名 (JupyterNotebook上およびファイル名)",
    "type": "モデルタイプ からの場合 LoRAが割り当てられる (lora / sdcp / vae / tv / cn)",
    "ext": "ファイル拡張子 空の場合 safetensors が割り当てられる",
    "url": "モデルダウンロードリンク CivitAI の場合 api.civitai.com で始まる",
    "groupid": "任意 いずれかの整数で指定し、この項目を同じ id のものでグループ化する",
    "lora": { "NONE": "Lora Templateを自動的に設定するための値",
      "lora": "<lora:example:1.0>",
      "name": "example",
      "prompt": "white hair",
      "extend": "pink eyes",
      "key": "example_lora <- lora を記入する場合、ここの存在チェックが行われるため必須"
    }
  }
}

import LGS.misc.jsonconfig as jsoncfg
from LGS.misc.nomore_oserror import filename_resizer
import os
from tqdm import tqdm

cwd = os.getcwd()

# ファイル / もうあるなら消す
out_path = os.path.join(
  cwd, "output.txt")

if os.path.exists(out_path):
  prv_data = jsoncfg.read_text(out_path)
  os.remove(out_path)
  print("[MSC]: backup data of output.txt\n", prv_data)

data = jsoncfg.read(os.path.join(cwd, "data.json"))
print(f"[MSC]: {len(data)} inputs found.")

out_lists = {
  "groupid.x": []
}

sessions = []
for k, d in tqdm(data.items(), desc="Processing.."):
  if not isinstance(k, int) or not isinstance(k, float):
    print(f"[MSC]: Skipping: {k}..\nthis key aren't int/float")
    continue
  
  if not isinstance(d, dict):
    print(f"[MSC]: Skipping: {k}..\nthis key's value aren't dict")
    continue
  
  session = {}
  for x, y in d.items():
    if x == "lora" or x == "groupid":
      if y == "" or y["key"] == "": # lora または gid が定義されていない？
        if x == "groupid": # groupid が定義されていないなら 0
          session["gid"] = 0
          continue
        else: # lora なら
          session["lora_dict"] = {"isEnabled": False}
          continue
      else: #されているなら
        if x == "groupid": # gid
          try:
            session["gid"] = int(y)
            continue
          except ValueError:
            print(f"[MSC]: Failed in {x}. {y} can't convert to int\n[MSc]: Disabled groupid")
          session["gid"] = 0
          continue
        else: #lora
          y.pop("NONE")
          session["lora_dict"] = y
    
    # extension
    elif x == "ext":
      y = y.strip(".").strip()
      
      if y == "":
        y = "safetensors"
      session["extension"] = y
      continue
    
    elif x == "type":
      #(lora / sdcp / vae / tv / cn)
      available = ["lora", "sdcp", "vae", "tv", "cn"]
      if not y in available:
        print(f"[MSC]: Failed in {x}. Unknown model type: {y}")
        session["type"] = "unknown"
        continue
      
      session["type"] = y
      continue
    
    elif x == "displayName":
      session["name"] = filename_resizer(y.strip().replace(
        " ", ""
      ), replaceTo="_")
      continue
    
    elif x == "url":
      session["url"] = y
    
    else:
      session[x] = y
      
  sessions.append(session)

target_dir = {
  "ROOT": "/content/gdrive/MyDrive/SD_Model",
  "lora": "/LoRA/",
  "sdcp": "/",
  "vae": "/VAE/",
  "tv": "/Texture_Inversion/",
  "cn": "/ControlNet/"
}


wget = "--- wget (one times only) ---\n"


for x in sessions:
  # wget を作成
  
