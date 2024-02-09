not_bind = 0
import tqdm





def get_binds(basic_data_dict):
  print("get_binds started.")
  binds4module = []
  
  for x in basic_data_dict["modules"]:
    bind = x["keybind"]
    #print(f"Detected keybind for {x['name']} key: {x['keybind']}")
    
    if bind != 0 and bind != None:
      binds4module.append(bind)
    elif bind == None:
      binds4module.append(0)
    else:
      binds4module.append(0)
  
  print(binds4module)
  return binds4module

def get_module_index_from_name(name, target_config):
  for index, data in enumerate(target_config["modules"]):
    if data["name"] == name:
      print("Found!", index)
      return index
  print(f"[WARN]: Module name '{name}' not found in target config.")
  return None

def set_key_from_index(target_config, index, key, replace):
  """入力したコンフィグのインデックスのキーバインドをキーで置き換える"""
  prv_bind = get_binds(target_config)[index]
  name = target_config["modules"][index]["name"]
  
  if replace and prv_bind == not_bind:
    print(f"[{name}]: Resized bind: {prv_bind} -> {prv_bind}")
    return target_config
  
  target_config["modules"][index]["keybind"] = key
  print(f"[{name}]: Resized bind: {prv_bind} -> {key}")
  return target_config

def reset_keybind(prv_config, db_config, replace, strict=True):
  bind_list = get_binds(db_config)
  newed_binds = get_binds(prv_config)
  
  for index, bind in tqdm.tqdm(enumerate(bind_list), desc="Resetting keybind.."):
    if len(db_config["modules"]) <= index or len(prv_config["modules"]) <= index:
      print(f"Index {index} out of range. Skipping reset for this index.")
      correctly_index = get_module_index_from_name(db_config["modules"][index]["name"], prv_config)
      if correctly_index == None:
        continue
    
    else:
      if db_config["modules"][index]["name"] != prv_config["modules"][index]["name"]:
        print("not matched module name in ", index, ".\nanalyzing correct module..", end="")
        correctly_index = get_module_index_from_name(db_config["modules"][index]["name"], prv_config)
      else:
        correctly_index = index
    
    if correctly_index != None:
      prv_config = set_key_from_index(prv_config, correctly_index, bind, replace)
  
  return prv_config

##### Convert Visuals


# def reset_visuals(prv_config, db_config, replace, convert_target=[]):
#   # bind 以外をアップデート
  
#   bind_list = get_binds(prv_config)
  
#   for index, data in enumerate(prv_config["modules"]):
#     if len(db_config["modules"]) <= index or len(prv_config["modules"]) <= index:
#       print(f"Index {index} out of range. Skipping reset for this index.")
#       correctly_index = get_module_index_from_name(db_config["modules"][index]["name"], prv_config)
#       if correctly_index == None:
#         continue
  
#     else:
#       if db_config["modules"][index]["name"] != prv_config["modules"][index]["name"]:
#         correctly_index = get_module_index_from_name(db_config["modules"][index]["name"], prv_config)
#       else:
#         correctly_index = index
    
#     if correctly_index != None:
#       cfg_data = db_config["modules"][correctly_index]
#     prv_config["modules"][correctly_index].update(cfg_data)
    
#   return prv_config

def reset_selected(prv_config, db_config, convert_target):
  return prv_config

##### UI
import os

ui_path = os.path.join(os.getcwd(), "ui")
PASSCODE = -1

import gradio as gr
from LGS.misc.nomore_oserror import file_extension_filter

def get_tabs_data():
  import importlib.util 
  def import_module_from_path(module_path): # function provided by chatGPT
      spec = importlib.util.spec_from_file_location("module_name", module_path)
      module = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(module)
      return module
  def execute_build_function(module): # function provided by chatGPT
    if hasattr(module, "build"):
        return module.build()
    else:
        print("Error: 'build' function not found in the module.")
        return PASSCODE
  
  r = []
  for x in file_extension_filter(os.listdir(ui_path), [".py"]):
    path = os.path.join(os.path.relpath(ui_path), x)
    
    ui_data: tuple = execute_build_function(
      import_module_from_path(path)
    )
    
    r.append(
      {
        "name": ui_data[0], # Tab's name
        "ui": ui_data[1], # gradio ui data
        "ui_index": ui_data[2] # ui index
      }
    )

  # uidata を 整理
  def uii(item):
    return item["ui_index"]
  r.sort(key=uii)
  
  return r

def ui():
  with gr.Blocks(title="lunapy / Prax Config switch helper") as i:
    with gr.Tabs():
      for d in get_tabs_data():
        with gr.Tab(label=d["name"]):
          d["ui"]

  return i