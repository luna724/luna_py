import re
import os
import nbformat as nbf
from modules.config_manager import sys_config, config
import LGS.misc.jsonconfig as jsoncfg

class Main:
  @staticmethod
  def parse_filename(text, known_model_names, sys_config) -> tuple:
    """
    This function is Provided by. GPT-4o
    """
    # Step 1: Extract the audio format
    text, aud_format = os.path.splitext(text)
    aud_format = aud_format.strip(".") if aud_format in ["mp3", "flac", "wav"] else None
    
    # Step 2: Extract the number
    pattern = r"(?P<number>\d+)-.*"
    match = re.match(pattern, text)
    if match:
        number = match.group("number")
        text = text.replace(
          f"{number}-", ""
        )
    else:
        number = None
        print("Numbers not found.\ntext: ", text)
    
    # Step 3: Decide whether to use known model names to split model_name and based_fn
    if sys_config.use_known_model_names_to_parse_fn:
        model_name = None
        based_fn = text
        for known_name in known_model_names:
            if text.startswith(known_name):
                model_name = known_name
                based_fn = text[len(known_name)+1:]  # +1 to remove the hyphen
                break
    else:
        parts = text.split("-", 1)
        model_name = parts[0] if len(parts) > 0 else None
        based_fn = parts[1] if len(parts) > 1 else None
    
    # Catch None cases and handle appropriately
    if model_name is None:
        raise ValueError("Model name could not be determined")
    if based_fn is None:
        raise ValueError("Based function name could not be determined")

    return number, model_name, based_fn, aud_format
  
  def __init__(self):
    self.fp = config.target_fp
    self.rule = config.file_named_rule
    self.compare_based = config.based_file_compare
    
    # FPの変換
    if self.fp.startswith("//"):
      pass
    else:
      self.fp = os.path.join(os.getcwd(), self.fp)
    
    self.allFile = [
      os.path.realpath(x)
      for x in os.listdir(self.fp)
      if os.path.splitext(x)[1] in [".mp3", ".wav", ".flac"]
    ]
    
    # ファイル命名規則に基づき、処理
    # trigger = re.findall(
    #   r"{(.*)}", self.rule
    # )
    # if not "model_name" in trigger and not "based_fn" in trigger:
    #   raise RuntimeError("stderr: [config]: [file_named_rule]: {model_name}, {based_fn} のいずれかが含まれていません。")

    # ファイル命名規則に基づき設定
    i = []
    for x in self.allFile:
      text = os.path.basename(x)
      known_model_names = sys_config.known_model_names

      try:
          number, model_name, based_fn, aud_format = self.parse_filename(text, known_model_names, sys_config)
      except ValueError as e:
          print("Error:", e)

      i.insert(-1, {
        "realpath": x,
        "fn": text,
        "model_name": model_name,
        "based_fn": based_fn,
        "aud_format": aud_format,
        "num": number
      })
    
    
    self.Items = {}
    for item in i:
      mn = item["model_name"]
      bf = item["based_fn"]
      num = item["num"]
      
      if num is None:
        num = "?"
      
      if mn not in self.Items.keys():
        self.Items[mn] = []
      self.Items[mn].insert(-1, item)
  
    for key in self.Items.keys():
      self.Items[key] = sorted(self.Items[key], key=lambda x: int(x["num"]))
    cp = self.Items
    
    self.Items = {key: cp[key] for key in sorted(self.Items.keys())}