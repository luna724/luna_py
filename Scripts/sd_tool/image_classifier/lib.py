import deepdanbooru as dd
import huggingface_hub
import os
import tensorflow as tf

from shared import shared
from proccessing import Processing

def load_model(model_path, isProjectModel:bool = False, compile_model=True):
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
    Processing.model = model
    return model
  
def update_tags(new_tags, append:bool = False):
  # Method: v1
  if append:
    tags = Processing.tags
    if tags is None:
      tags = []
    
    for new in new_tags:
      if new in tags:
        continue
      
      Processing.tags.append(new)
    
  else:
    Processing.tags = new_tags

def listup_models():
  shared.dd_models = [
    os.path.realpath(os.path.join(shared.model_dir, x))
    for x in os.listdir(shared.model_dir)
  ]
  if len(shared.dd_models) < 1:
    model_path = huggingface_hub.hf_hub_download("public-data/DeepDanbooru", "model-resnet_custom_v3.h5")
    shared.dd_models = [model_path]
    
  return shared.dd_models