# customtrain.py
# modules.tabs.customtrain

import os
import shutil
import gradio as gr
from multiprocessing import cpu_count
from typing import *

# >_<
from modules.ui import Tab
from modules.shared import ROOT_DIR

# luna
from luna.modules.set_config import UITrainingConfig

class Customtrain(Tab):
  def title(self):
    return "Customtrain"
  
  def sort(self):
    return 7
  
  def ui(self, outlet):
    ltuiconfig_path = os.path.join(ROOT_DIR, "luna", "configs", "ui", "training.json")
    uicfg = UITrainingConfig.parse_file(ltuiconfig_path)
    
    with gr.Group():
      with gr.Box():
        with gr.Row():
          with gr.Column():
            model_name = gr.Textbox(
              label="Model Name",
              placeholder="test_Modelv2",
              value=uicfg.model_name
            )
            dataset_glob = gr.Textbox(
              label="Dataset Path",
              placeholder="/dataset/*.wav",
              value=uicfg.dataset_path
            )
          with gr.Column():
            