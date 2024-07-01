import deepdanbooru as dd
import json, os, shutil
from PIL import Image
import numpy as np
import time
import tensorflow as tf

class Processing:
  def load_model(self, model_path, isProjectModel:bool = False, compile_model=True):
    # Method: v2
    
    if isProjectModel:
      if os.path.exists(model_path):
        model = dd.deepdanbooru.project.load_model_from_project(model_path, compile_model=compile_model)
      else:
        raise ValueError("model path is not a valid path!")
      
      Processing.model = model
      return model
    else:
      model = tf.keras.models.load_model(model_path)
      self.model = model
      return model
    
  model = None
  tags: list = None
  
  model_name: str = None
  
  def __init__(self):
    self.model = Processing.model
    self.tags = Processing.tags
    
    if hasattr(Processing, "last_model_name"):
      self.last_model_name = Processing.last_model_name
    else:
      self.last_model_name = None
    
def run(using_model, in_path:str, out_path:str, classify_tags:str, threshold:float,
        caption_mode:bool = False, captioning_extension: str = ".txt"):
  yield "Starting.."
  started_time = time.time()
  with open("config.json", "r", encoding="utf-8") as f: cfg = json.load(f)
  
  # モデルの読み込み
  yield "Initializing.."
  proc = Processing()
  
  yield "Processing model.."
  if not using_model == proc.last_model_name or not cfg["use_model_cache"]:
    yield "[PM]: Loading model.."
    proc.model = proc.load_model(using_model, compile_model=False)
    Processing.model_name = using_model
    proc.last_model_name = using_model
    yield "[PM]: done."
  
  yield "Making directories.."
  # 出力パスの作成
  if out_path == ".": 
    out_path = os.path.join(in_path, f"..\\{os.path.basename(in_path)}-outputs")
  
  out_path = os.path.abspath(out_path)
  os.makedirs(out_path, exist_ok=True)
    
  # 整理タグの解析と出力パスの作成
  proc.target_tags = []
  for x in classify_tags.split(","):
    proc.target_tags.append(x.strip())
    name = os.path.join(out_path, x.replace(":","-"))
    if os.path.exists(name):
      if os.path.isdir(name):
        shutil.rmtree(name)
    
    os.makedirs(name)
  
  # 処理
  yield "Processing.."
  model = proc.model
  user_tags_set = set(classify_tags)

  for subdir, dirs, files in os.walk(in_path):
    for file in files:
      yield f"[PROC]: in {subdir}/{file}"
      file_path = os.path.join(subdir, file)
      try:
        yield f"[{file}]: Infering.."
        img = Image.open(file_path).convert('RGB')
        img = img.resize((model.input_shape[1], model.input_shape[2]), Image.LANCZOS)
        image_array = np.array(img) / 255.0
        image_array = image_array.reshape((1, model.input_shape[1], model.input_shape[2], 3))
        
        # 予測結果の取得
        predictions = model.predict(image_array)[0]
        
        file_tags = []
        yield f"[{file}]: Analyzing tags.."
        for i, tag in enumerate(proc.tags):
          score = predictions[i]
          if tag in user_tags_set and score >= threshold:
            yield f"[{file}]: Hooked."
            file_tags.append((tag, score))
            tag_dir = os.path.join(out_path, tag)
            if not os.path.exists(tag_dir):
              os.makedirs(tag_dir)
            shutil.copy(file_path, tag_dir)
          else:
            yield f"[{file}]: pass"
      
        # キャプションファイルの生成
        if caption_mode:
          yield f"[{file}/CP]: Starting Captioning.."
          caption_string = ", ".join([f"{tag}" for tag, score in file_tags])
          caption_file_path = os.path.join(out_path, f"{file}{captioning_extension}")
          with open(caption_file_path, 'w', encoding='utf-8') as f:
            f.write(caption_string)
          yield f"[{file}/CP]: Done."
      except Exception as e:
        yield f"[{file}]: Error occurred. for more details, please see prompts."
        print(f"Error processing {file_path}: {e}")
  
  ended_time = time.time()
  elapsed_time = ended_time - started_time
  
  yield f"All Processes done.\nElapsed: {elapsed_time}"
  return