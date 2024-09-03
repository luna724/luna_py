## THIS FUNCTIONS BETA!
## NOT SUPPORTING EXTERNAL AUGMENTS AND ALL ARGS! (exclude input, output_path)

import random
import os
import time

from augmentation.func.functions import call as run_call
import augmentation.func.functions as functions

def call(input_path, output_path):
  class stt: status = ""
  stats = stt()
  def add_status(*string:str) -> str:
    newstring = "".join(string)
    status = stats.status
    status += f'{newstring}\n'
    stats.status = status
    return stats.status
  
  # 入力パスの画像ファイルをリストアップ
  files = [
      f 
      for f in os.listdir(input_path)
      if os.path.splitext(f)[1].lower() in [".png", ".jpg", ".jpeg"]
  ]
  
  # 最終的な画像数がデータ拡張により40~45%になるように
  target_expanded_image_count = int(len(files) / (1 - 0.425) - len(files))
  
  # 拡張の各条件に基づく枚数を計算
  rotate_count = int(target_expanded_image_count * 0.15)
  invert_count = int(target_expanded_image_count * 0.20)
  zoom_count = int(target_expanded_image_count * 0.15)
  color_adjust_count = int(target_expanded_image_count * 0.30)
  combined_count = int(target_expanded_image_count * 0.20)
  
  all_count = f"Here's expand target images count:\nexpanded_target_image: {target_expanded_image_count}\nrotate: {rotate_count}\ninvert: {invert_count}\nzoom: {zoom_count}\ncolor_adjust: {color_adjust_count}\ncombined: {combined_count}"
  yield add_status(all_count)
  time.sleep(2.5)

  # 拡張内容と対応する名称のマッピング
  augment_map = {
      "Rotate90": "Rotate90",
      "Rotate180": "Rotate180",
      "Rotate270": "Rotate270",
      "Invert (Horizontal)": "Invert (Horizontal)",
      "Zoom-in": "Zoom-in",
      "Zoom-out": "Zoom-out",
      "Refactor-brightness": "Refactor-brightness",
      "Adjust-sharpness": "Adjust-sharpness",
      "Adjust-contrast": "Adjust-contrast",
      "Adjust-color": "Adjust-color"
      # 他の拡張が必要ならここに追加
  }
  
  # 拡張リストの初期化
  processing_target_images = {f: [] for f in files}
  
  # 拡張処理の適用
  def apply_augment(file, augment):
    processing_target_images[file].append(augment_map[augment])

  # 各条件に基づき拡張を適用
  for _ in range(rotate_count):
    f = random.choice(files)
    a = random.choice(["Rotate90", "Rotate180", "Rotate270"])
    apply_augment(f, a)
    yield add_status(f"added {a} to {f}")
  
  for _ in range(invert_count):
    f = random.choice(files)
    apply_augment(f, "Invert (Horizontal)")
    yield add_status(f"added Invert (Horizontal) to {f}")
    
  for _ in range(zoom_count):
    f = random.choice(files)
    a = random.choice(["Zoom-in", "Zoom-out"])
    apply_augment(f, a)
    yield add_status(f"added {a} to {f}")

  for _ in range(color_adjust_count):
    f = random.choice(files)
    a = random.choice(["Refactor-brightness", "Adjust-sharpness", "Adjust-contrast", "Adjust-color"])
    apply_augment(f, a)
    yield add_status(f"added {a} to {f}")

  # 複数の拡張をランダムに組み合わせて適用
  augmentations = augment_map.keys()
  for _ in range(combined_count):
    selected_file = random.choice(files)
    selected_augments = random.sample(augmentations, random.randint(2, 4))  # 2〜4個のランダムな拡張を選択
    for augment in selected_augments:
      apply_augment(selected_file, augment)
    yield add_status(f"Multiply added {selected_augments} to {f}")
  
  for fn, target_augments in processing_target_images.items():
    yield add_status(f"Starting analyze for {fn}..")
    if len(target_augments) < 1:
      yield add_status(f"skipped file. (Reason: target_augments < 1)")
      continue
    
    file = os.path.join(input_path, fn)
    
    if len(target_augments) == 1:
      augment_mode = "single"
    else:
      augment_mode = "multi"
    
    call_kwrg = {
      "file_mode": "select", "augment_mode": augment_mode,
      "input_path": input_path, "out_path": output_path, "files": [file],
      "file_limit": 1, "target_augments_single_rand": [],
      "augment_selected": target_augments[0], "augment_selected_multi": target_augments,
      "augment_selected_from_random": [], "augments_selected_from_random_min": 0,
      "augments_selected_from_random_max": 0
    }
    yield add_status(
      f"running functions.call with args: {call_kwrg}"
    )
    for message in run_call(**call_kwrg, call_from_average=True):
      yield add_status(f"[functions.call]: {message}")
      
    yield add_status("success.")
  yield add_status("ALL Tasks Done.")
  return;