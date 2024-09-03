#> MAIN
import os
import gradio as gr
import random
from typing import *
from PIL import Image
import importlib

class Augment:
  # Augment Main Class
  def __init__(self):
    self.augment_name = None
    self.augment_index = -1
    self.augment_default = True
    self.exclude_random = False 
  
  def augment(self, **kw):
    raise ValueError()
  
  def index(self):
    # return this index
    return self.augment_index
  
  def getName(self):
    return self.augment_name
  
  def getDefault(self):
    return self.augment_default
  
  def getExcludeRandom(self):
    return self.exclude_random
  
  def getAugment(self):
    return self.augment

def collect_all_augment() -> List[Augment]:
  augments = []
  augments_file = [
    F"augmentation.func.augments.{os.path.splitext(x)[0]}"
    for x in os.listdir(os.path.realpath("./augmentation/func/augments"))
    if os.path.splitext(x)[1].lower() == ".py"
  ]

  for f in augments_file:
    module = importlib.import_module(f)
    print(f"Trying import {module}")
    augment_module = [
      x()
      for x in module.__dict__.values()
      if isinstance(x, type) and not x == Augment and issubclass(x, Augment)
    ]
    if len(augment_module) < 1:
      print("Failed. (reason: target class not found)")
      continue
    augment_mod = augment_module[0]
    
    print("Success. augments added successfully")
    augments.append(augment_mod)
  global cls
  cls = augments

cls = None
collect_all_augment()
    
def get_augments_value() -> List[list]:
  names = []
  for c in cls:
    if c.getName() != None:
      names.append(c)
  
  for i, name in enumerate(sorted(names, key=lambda x: x.index())):
    names[i] = [name.getName(), name.getDefault(), name.getExcludeRandom(), name.getAugment()]
  return names

def get_available_augmentation() -> List[str]:
  # Return: available augmentation (list of all get_augments_value()[n][0])
  available = [
    x[0]
    for x in get_augments_value()
    if isinstance(x[0], str)
  ]
  return available

def get_default_available_augmentation() -> List[str]:
  # Return: (list of all get_available_augmentation() but, only x[1] = True)
  available = [
    x[0]
    for x in get_augments_value()
    if isinstance(x[0], str)
    if x[1]
  ]
  return available

def get_callable_augmentation() -> dict:
  # Return: {"x[0]": x[3]}
  available = {
    x[0]: x[3]
    for x in get_augments_value()
    if isinstance(x[0], str)
    if callable(x[3])
  }
  return available

def call(
  file_mode:Literal["random", "random(count-Limited)", "select"], 
  augment_mode:Literal["single(random)", "single", "multi", "multi(random)"], 
  input_path:str, out_path:str, files:List[str], file_limit:int, 
  target_augments_single_rand:List[str], augment_selected:str,
  augment_selected_multi:List[str], augment_selected_from_random:List[str], 
  augments_selected_from_random_min:int, augments_selected_from_random_max:int,
  call_from_average:bool=False
):
  class stats:
    status = ""
  stat = stats()
  def add_status(*statuses: str) -> str:
    newstring = "".join(statuses)
    status = stat.status
    status += f'{newstring}\n'
    stat.status = status
    return stat.status

  if not os.path.exists(input_path) or not os.path.isdir(input_path):
    gr.Warning("cannot found input path or it's not directory!")
    return "An Error raised: cannot found input path or it's not directory!"
  
  if file_mode == "random":
    # ファイルをランダムに追加
    files = []
    for f in os.listdir(input_path):
      if os.path.splitext(f)[1].lower() in [".png", ".jpg", ".jpeg"]:
        if (random.randrange(0, 1000, 1) / 10) < 37.5: # 37.5%
          files.append(f)
          yield add_status(f"Passed file: {f}")
          
      else:
        yield add_status(f"Skipped file: {f}.")
  
  if file_mode == "random(count-Limited)":
    # ファイルを個数制限しながら追加
    files = []
    while len(files) < file_limit:
      for f in os.listdir(input_path):
        if os.path.splitext(f)[1].lower() in [".png", ".jpg", ".jpeg"]:
          if (random.randrange(0, 1000, 1) / 10) < 37.5: # 37.5%
            files.append(f)
            yield add_status(f"Passed file: {f}")
            if not (len(files) < file_limit):
              break
        else:
          yield add_status(f"Skipped file: {f}.")
  
  if file_mode == "select":
    # ファイルを確認
    for f in files:
      if not os.path.splitext(f)[1].lower() in [".png", ".jpg", ".jpeg"]:
        files.remove(f)
        yield add_status(f"Removed file {f} because format not supported.")
        continue
      yield add_status(f"Passed file: {f}")

  files = [
    os.path.abspath(os.path.join(input_path, f))
    for f in files
  ]
  
  
  yield add_status(f"Finalized files: {files}")
  # Augmentation の処理
  # モードが single ならそれに変更
  if augment_mode == "single":
    target_augments = [augment_selected]
  elif augment_mode == "single(random)":
    target_augments = [random.choice(target_augments_single_rand)]
  elif augment_mode == "multi":
    target_augments = augment_selected_multi
  elif augment_mode == "multi(random)":
    yield add_status("mode == multi(random)")
    if not (augments_selected_from_random_min <= augments_selected_from_random_max):
      yield add_status("!min <= max detected.")
      augments_selected_from_random_max = augments_selected_from_random_min
    
    if not (augments_selected_from_random_min == augments_selected_from_random_max):
      augments_count = random.randrange(augments_selected_from_random_min, augments_selected_from_random_max, 1)
    else:
      augments_count = augments_selected_from_random_min
    yield add_status(f"Finalized augments_count: {augments_count}")
    yield add_status(f"augment_selected_from_random: {augment_selected_from_random}")
    
    target_augments = []
    while not (augments_count == len(target_augments)):
      choiced = random.choice(augment_selected_from_random)
      if not choiced in target_augments:
        target_augments.append(choiced)
    yield add_status(f"Finalized target_augents: {target_augments}")
    
  # 各ファイルの内容をランダムなaugmentに基づき実行
  augment_collection = get_callable_augmentation()
  if len(target_augments) == 1:
    for f in files:
      yield add_status(f"infering file: {f}..")
      augment = target_augments[0]
      if not augment in augment_collection.keys():
        yield add_status(f"An error occurred in augment: {augment}")
        continue
      
      img = Image.open(f)
      fn = f.split("\\")[-1]
      
      yield add_status(f"Infering augment: {augment}..")
      new_image, new_fn = augment_collection[augment](img, fn)
      new_image:Image.Image
      # 保存
      if out_path.lower() == "?replace":
        output = os.path.realpath(f)
      else:
        os.makedirs(out_path, exist_ok=True)
        output = os.path.join(out_path, new_fn)
      
      yield add_status(f"Saving file.. ({f}) to {new_fn}")
      new_image.save(output, jpeg2jpg(os.path.splitext(new_fn)[1][1:]).upper())
  else:
    for f in files:
      yield add_status(f"infering file: {f}..")
      img = Image.open(f)
      fn = f.split("\\")[-1]
      
      for augment in target_augments:
        if not augment in augment_collection.keys():
          yield add_status(f"An error occurred in augment: {augment}")
          continue
        
        yield add_status(f"Infering augment: {augment}..")
        img, fn = augment_collection[augment](img, fn)
      
      if out_path.lower() == "?replace":
        output = os.path.realpath(f)
      else:
        os.makedirs(out_path, exist_ok=True)
        output = os.path.join(out_path, fn)
      
      yield add_status(f"Saving file.. ({f}) to {fn}")
      img.save(output, jpeg2jpg(os.path.splitext(fn)[1][1:]).upper())  
  yield add_status("ALL Tasks Done.")
  
  if not call_from_average:
    return;
  return;
  
def input_dir_changed(input_directory):
  # return: [file_selected, file_max_count]
  if not os.path.exists(input_directory): 
    raise gr.Error("directory aren't exists.")
  
  files = [
    f.split("\\")[-1]
    for f in os.listdir(input_directory)
    if os.path.splitext(f)[-1].lower() in [".png", ".jpg", ".jpeg"]
  ]
  
  new_slider = gr.Slider.update(
    value=len(files), minimum=0, maximum=len(files)
  )
  new_dropdown = gr.Dropdown.update(
    value=files, choices=files
  )
  return new_dropdown, new_slider

def file_mode_changed(file_mode: Literal["random", "random(count-Limited)", "select"]):
  if file_mode == "random":
    let = (False, False)
  elif file_mode == "random(count-Limited)":
    let = (False, True)
  elif file_mode == "select":
    let = (True, False)
  
  let = [
    gr.update(visible=l)
    for l in let
  ]
  return tuple(let)

def augment_mode_changed(augment_mode: Literal["single", "single(random)", "multi", "multi(random)"]):
  # return [augment_mode_single_random, augment_mode_single, augment_mode_multi, augment_mode_multi_random]
  if augment_mode == "single(random)":
    let = (True, False, False, False)
  elif augment_mode == "single":
    let = (False, True, False, False)
  elif augment_mode == "multi":
    let = (False, False, True, False)
  elif augment_mode == "multi(random)":
    let = (False, False, False, True)
  
  let = [
    gr.update(visible=l)
    for l in let
  ]
  return tuple(let)

def file_selected_refresh(input_dir):
  return input_dir_changed(input_dir)[0]

def augments_selected_random_update(random_selected):
  # return [min in max, max in max]
  let = (len(random_selected), len(random_selected))
  
  let = [
    gr.Slider.update(maximum=l, value=l)
    for l in let
    if isinstance(l, int)
  ]
  return tuple(let)

def jpeg2jpg(string:str) -> str:
  if string.lower() == "jpeg":
    return "jpg"
  else:
    return string