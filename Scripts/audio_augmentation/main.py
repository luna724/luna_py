"""
1. それぞれに何の拡張を適用するか、定義

"""
Debug_Mode = True

# 0
  # ファイル取得、辞書追加、定義
import LGS.misc.debug_tool as dt
def dprint(str): 
  if Debug_Mode: 
    dt.dprint(str)
import augment as augmentation
import LGS.misc.random_roll as roll
import random
import LGS.misc.jsonconfig as jsoncfg
import os
import LGS.misc.compact_input as cin
import LGS.misc.nomore_oserror as los

#
y = 0

# 前処理 (処理済みファイルがある場合、そっちを使用)
target_dir = input("Target Directory (未入力で前回の設定引継ぎ): ")
if cin.isnone(target_dir):
  if os.path.exists("./latest_date.json"):
    filelist_dict = jsoncfg.read("./latest_date.json")
  else:
    raise ValueError("前回のコンフィグが見つかりませんでした。")
  
else:
  filelist_raw = os.listdir(target_dir)

  # ファイルチェック (拡張可能な拡張子)

  filelist_filteling = los.file_extension_filter(filelist_raw, allowed_extensions=[".mp3", ".wav", ".flac"])
  filelist_dict = {}
  dprint(f"リストアップファイル: {filelist_raw}\n \
  チェック後リスト: {filelist_filteling}")
  
  # 拡張可能なものが0なら
  if not len(filelist_filteling) > 0:
    raise ValueError("対象ファイルが見つかりません。")
  
  # ディレクトリ乗法
  filelist_dict["Target_Directory_INFO"] = target_dir 
  
  # 辞書追加
  for file in filelist_filteling:
    # 拡張子の取得
    file_extension = os.path.splitext(file)[1].lower()
    filelist_dict[file] = [{"format":f"{file_extension}"}]
    ## {"file": [{"format": {extension}}]}
    
    # 有効な拡張リストから、ランダムで選出
    filelist_dict[file][0]["augment"] = [random.choice(augmentation.augment_list)]
    #{"file": [{"format": "extension", 
    # "augment": [{"augment_1": "augment_1"}, 
    #{"augment_2": "augment_2"}] }]}
    
    # ここから先は確率で付与
    if roll.random_roll(0.2):
      # 20% で一つ追加
      """
      "augment" 辞書内のキーにアクセス
      その中のリストに、新たな拡張を追加
      """
      filelist_dict[file][0]["augment"].append(random.choice(augmentation.augment_list))
      # 同じものがロールされたら、消す
      if filelist_dict[file][0]["augment"][0] == filelist_dict[file][0]["augment"][1]:
        filelist_dict[file][0]["augment"].pop(1)
      
    if roll.random_roll(0.05):
      # 5% でもういっこ (1%で二つ)
      # リストインデックス1 がある場合
      if len(filelist_dict[file][0]["augment"]) == 2:
        filelist_dict[file][0]["augment"].append(random.choice(augmentation.augment_list))
      # 同じものがロールされたら、消す
        if filelist_dict[file][0]["augment"][0] == filelist_dict[file][0]["augment"][2] or filelist_dict[file][0]["augment"][1] == filelist_dict[file][0]["augment"][2]:
          filelist_dict[file][0]["augment"].pop(2)
      
      # 20% がロールされてないなら
      else:
        filelist_dict[file][0]["augment"].append(random.choice(augmentation.augment_list))
        # 同じものがロールされたら、消す
        if filelist_dict[file][0]["augment"][0] == filelist_dict[file][0]["augment"][1]:
          filelist_dict[file][0]["augment"].pop(1)
    
    # ノイズがロールされたら、ノイズタイプをロール
    x = len(filelist_dict[file][0]["augment"])
    while x != 0:
      x -= 1
      inner_dict = filelist_dict[file][0]["augment"][x]  # 内側の辞書を取得
      if "1" in inner_dict:
        filelist_dict[file][0]["augment"][x]["1"] = random.choice(augmentation.noise_type_list)
      
    # ID割り当て (ファイル名重複防止)
    y += 1
    filelist_dict[file][0]["ID"] = "{:04d}".format(y)
    
    # ファイル名を取得
    filelist_dict[file][0]["NAME"] = os.path.splitext(file)[0]
    



  # 出力先
  out_dir = input("Output Directory: ")
  if cin.isnone(out_dir):
    print("未記入のため、\"./augmented/\" に出力します。")
    out_dir = "./augmented/"

  filelist_dict["Target_Directory_OUT"] = out_dir
  
# とりあえず、保存
jsoncfg.write(filelist_dict, "./latest_date.json")

dprint(filelist_dict)
# 拡張実行の前に..
# アウトプットディレクトリ
# 許可: mp3, wav, flac, auto
output_type_raw = input("(Available: wav, flac, mp3, auto(Keep-format type)\nOutput Format: ").lower()

if not output_type_raw in ["mp3", "flac", "wav", "auto"]:
  raise ValueError("拡張子タイプが不明です。\n[mp3, flac, wav, auto]のいずれかを入力してください。")

# AUTO じゃない場合
if not output_type_raw == "auto":
  out_extension = output_type_raw
  auto_detection = False
  
else:
  auto_detection = True
  out_extension = "wav"
  

# 拡張実行
augmentation.augment(filelist_dict, auto_detection, out_extension)