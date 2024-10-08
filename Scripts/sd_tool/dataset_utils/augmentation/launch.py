from argparse import Namespace

import os
import sys

def launch(args:Namespace, api_mode:bool=False, **kw) -> None:
  # パスを追加
  sys.path.append(os.path.join(os.getcwd(), "augmentation"))
  
  import webui
  return webui.launch()