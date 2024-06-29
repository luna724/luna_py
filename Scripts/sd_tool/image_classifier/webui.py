from typing import *
import os
import shutil
import json
import deepdanbooru as dd
import tensorflow as tf
import huggingface_hub
import gradio as gr
from PIL import Image

from proccessing import Processing
import lib
from shared import shared
from ui import build

def webui():
  with open("config.json", "r", encoding="utf-8") as f: cfg = json.load(f)
  
  # 初回設定
  print("Preparing Models..")
  model_dir = cfg["model_directory"]
  if not os.path.exists(model_dir):
    try:
      os.makedirs(model_dir, exist_ok=True)
    except OSError:
      print("Error: unable to access the model directory.")
      model_dir = "dd_models"
      os.makedirs(model_dir, exist_ok=True)

  shared.model_dir = model_dir
  shared.model_path = shared.model_dir
  shared.dd_models = lib.listup_models()
  
  # モデルがない場合
  if len(shared.dd_models) < 1:
    model_path = huggingface_hub.hf_hub_download("public-data/DeepDanbooru", "model-resnet_custom_v3.h5")
    shutil.copy(model_path, os.path.join(model_dir, "model-resnet_custom_v3.h5"))
    shared.dd_models = lib.listup_models()
    
  # タグ
  tag_path = huggingface_hub.hf_hub_download(repo_id="public-data/DeepDanbooru", filename="tags.txt")
  with open(tag_path, 'r', encoding='utf-8') as f:
    shared.tags = [line.strip() for line in f]
  # コンフィグのタグを追加
  shared.tags += cfg["custom_tags"]
  lib.update_tags(shared.tags)
  
  # とりあえずモデルを読み込む
  print("Loading Models..")
  pre_model_path = shared.dd_models[0]
  lib.load_model(pre_model_path, isProjectModel=False)
  
  # UIの構築 (静的)
  ui = build(Processing, shared)
  ui.queue(64).launch(server_port=7855)