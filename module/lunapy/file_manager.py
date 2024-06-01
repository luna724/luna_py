"""
file_manager.py  @lunapy.file_manager as fm
fm.py            @lunapy.fm

ファイルの書き込み、読み込み、削除、作成を行う

主に書き込みに焦点を当てており、書き込み方法の自動検出などをサポートしている
"""
from typing import Literal, Any
from lunapy.lunapy import lunapyDefault
import os

def read(f:str, mode:Literal["r", "rb", "+r"]="r", stderr: Any = lunapyDefault):
  """args:
  f: FilePath: str,
  mode: Mode for open() function: str,
  stderr: if files not exist, return this. (except stderr == lunapyDefault)
  
  -> FileData
  """
  if not os.path.exists(f) or not os.path.isfile(f): 
    if stderr == lunapyDefault:
      raise RuntimeError("Files not exist.")
    else:
      return stderr
    
  with open(f, mode=mode) as f: return f

def write(f:str, data:Any, mode:Literal["w", "wb"], spec_mode: Literal["binary", "binary-image", "binary-audio", "raw", "numpy", "json", "sqlite", "sha", "log", "auto-detect"] = "auto-detect", force_generate_directory: bool = True, stderr: Any = lunapyDefault):
  """ args:
  """
  
  # ディレクトリの作成
  if not os.path.exists(os.path.join(f, "..\\")) or not os.path.isdir(os.path.join(f, "..\\")):
    if force_generate_directory:
      rf = os.path.realpath(f)
      for x in f.split("\\")[1:]:
        os.makedirs(x, exist_ok=True)
  
  # モードの自動検出
  file = os.path.basename(f)[1]
  if spec_mode == "auto-detect":
    # !!
    