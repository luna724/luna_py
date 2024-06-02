import datetime as DT
import os
import re
import nbformat as nbf
from modules.config_manager import sys_config, config
import LGS.misc.jsonconfig as jsoncfg

from modules.main import Main

class main(Main):
  def __init__(self, ext:str):
    self.CRT = DT.datetime.now().strftime(sys_config.crt_method)
    self.extension = ext
    self.out_rule = config.ipynb_name_rule
    self.compare_based = config.based_file_compare
    self.target_models = None
    self.sha256 = None
    
    ipynb_path = os.path.join(os.getcwd(), sys_config.ipynb_basic)
    with open(ipynb_path, "r", encoding="utf-8") as f:
      self.note = nbf.read(f, as_version=4)
    
    self.md = jsoncfg.read_text(
      os.path.join(os.getcwd(), sys_config.md_template)
    )
    
    # 出力規則の変数を解析
    if "{datetime}" in config.ipynb_dir_rule:
      self.ipynb_dir_rule = config.ipynb_dir_rule.format(datetime=self.CRT)
    else:
      self.ipynb_dir_rule = config.ipynb_dir_rule
    
    try: 
      self.ipynb_name = config.ipynb_name_rule
      
      self.ipynb_name = self.ipynb_name.format(
        datetime=self.CRT
      )
      self.ipynb_name = self.ipynb_name.format(
        model_name=self.target_models
      )
      self.ipynb_name = self.ipynb_name.format(
        sha=self.sha256
      )
    except KeyError:
      pass
    except UnboundLocalError:
      pass
    self.ipynb_name += self.extension
    
    super().__init__()
  
  
  def __call__(self):
    # 出力先
    audio_dir = os.path.realpath(os.path.join(self.ipynb_dir_rule, self.ipynb_name))
    os.makedirs(self.ipynb_dir_rule, exist_ok=True)
    os.makedirs(audio_dir+"_dir")
    
    markdown = ""
    for mn in self.Items.keys():
      for i in self.Items[mn]:
        if not self.compare_based:
          # オーディオのコピー
          sa = os.path.join(audio_dir+"_dir", i["fn"])
          print("start: ", i["realpath"], "\nsa: ", sa)
          os.rename(
            os.path.join(self.fp, i["fn"]), sa
          )
          n = i["num"]
          bfn = i["based_fn"]
          af = i["aud_format"]
          markdown += f"| {n} | {mn} | <audio controls src=\"{os.path.relpath(sa, self.ipynb_dir_rule)}\"></audio> | {bfn} | {af} |\n"
    
    cell = nbf.v4.new_markdown_cell(
      f"{self.md}\n{markdown}"
    )
    
    self.note.cells.append(cell)
    
    with open(audio_dir, "w", encoding="utf-8") as f:
      nbf.write(self.note, f)
    
    return