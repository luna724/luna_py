from modules.config_manager import config, sys_config, update_config

def find(base:str, trigger:str) -> bool:
  if trigger in base:
    return True
  return False

class inrs:
  @staticmethod
  def see():
    return config.ipynb_name_rule
  def add(i:list, base:str):
    # 競合なし
    for x in i:
      x = str(x)
      if find(base, x):
        base = base.replace(x, "")
      else:
        base = base + " " + x
    return [], base
    
class idrs:
  @staticmethod
  def see():
    return config.ipynb_dir_rule
  def add(i:list, base:str):
    # 競合なし
    for x in i:
      x = str(x)
      if find(base, x):
        return [], base.replace(x, "")
      else:
        return [], base + " " + x

class dais:
  @staticmethod
  def see():
    return config.disable_additional_inference

class tfs:
  @staticmethod
  def see():
    return config.target_fp
  def add(i:list, base:str):
    # 競合なし
    for _ in i:
      if base.startswith("//"):
        base = base.replace("//", "")
      else:
        base = "//"+base
    return [], base

class fnrs:
  @staticmethod
  def see():
    return config.file_named_rule
  def add(i:list, base:str):
    # 競合なし
    for x in i:
      x = str(x)
      if find(base, x):
        base = base.replace(x, "")
      else:
        base = base + " " + x
    return [], base

class gips:
  @staticmethod
  def see():
    return config.gradio_ip
  def add(i:list, base:str):
    # 競合なし
    return []. i

class bfcs:
  @staticmethod
  def see():
    return config.based_file_compare

class gps:
  @staticmethod
  def see():
    return config.gradio_port
  def add(i:list, base:str):
    # 競合なし
    if i == "?":
      return [], "?"
    else:
      return [], base
  def update(v, id):
    import gradio as gr
    if v == 80:
      raise gr.Error("Port 80 are unavailable.")
    
    
    else:
      update_config(id, v)

class usrs:
  @staticmethod
  def see():
    return config._ui_share