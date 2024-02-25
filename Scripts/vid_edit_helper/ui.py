

import logging
import os
import importlib
import time
import gradio as gr

script_root = os.path.join(os.getcwd(), "modules")

class Tabs:
  ROOT_DIR = script_root
  PATH = script_root
  
  def __init__(self, path):
    self.filepath = path
    self.rootpath = script_root
    
    pass
  
  def variable(self):
    return ["tab_title"]
  
  def index(self) -> int:
    return 0
  
  def get_ui(self) -> list:
    tabs = []
    files = [f for f in os.listdir(self.child_path) if f.endswith(".py")]
    
    for file in files:
      name = file[:-3]
      path = os.path.relpath(
        self.child_path, Tabs.ROOT_DIR
      ).replace("/", ".").replace("\\", ".").strip(".")
      module = importlib.import_module(
        f"modules.{path}.{name}"
      )
      
      attrs = module.__dict__
      TabClass = [
        x for x in attrs.values() if type(x) == type and issubclass(x, Tabs) and not x == Tabs
      ]
      if len(TabClass) > 0:
        tabs.append((file, TabClass[0]))
      
    tabs = sorted([TabClass(file) for file, TabClass in tabs], key=lambda x: x.index())
    return tabs
  
  def ui(self, outlet):
    pass
  
  def __call__(self):
    child_dir = self.filepath[:-3]
    children = []
    tabs = []
    
    if os.path.isdir(child_dir):
      for file in [file for file in os.listdir(child_dir) if file.endswith(".py")]:
        module_name = file[:-3]
        
        parent = os.path.relpath(
          Tabs.PATH, Tabs.PATH
        ).replace(
          "/", "."
        ).strip(".")
        print("parent: ", parent)
        
        children.append(
          importlib.import_module(
            f"modules.{parent}.{module_name}"
          ) # インポートしていたものを children に追加
        )
        
    children = sorted(children, key=lambda x: x.index())
    
    for child in children:
      # 辞書として変数の値を取得
      # このクラスのサブクラスを発見したら最初のものを追加
      attrs = child.__dict__
      tab = [x for x in attrs.values() if issubclass(x, Tabs)]
      if len(tab) != 0:
        tabs.append(tab[0])
      
    
    
    # これに関してはわからんけど
    # おそらく self.ui に取得したタブの要素を追加
    def outlet():
      with gr.Tabs():
        for tab in tabs:
          tab:Tabs # for IDE
          with gr.Tab(tab.variable()[0]): # タイトル
            tab() # __call__ を再実行？
                    
    
    return self.ui(outlet)

def get_ui():
  tabs = []
  files = [file for file in os.listdir(Tabs.PATH) if file.endswith(".py")]
  
  for file in files:
    module_name = file[:-3]
    module = importlib.import_module(f"modules.{module_name}")
    
    attrs = module.__dict__
    print(attrs)
    TabClass = [
      x for x in attrs.values()
      if type(x) == type and issubclass(x, Tabs) and not x == Tabs
    ]
    if len(TabClass) > 0:
      tabs.append((file, TabClass[0]))
    else:
      print("NOT FOUND TABCLASS")
  
  tabs = sorted([TabClass(file) for file, TabClass in tabs], key=lambda x: x.index())
  return tabs

def create_ui(): # this code too inspirated by. ddPn08's rvc-webui
  block = gr.Blocks(title="lunapy / VEH")
  
  with block:
    with gr.Tabs():
      tabs = get_ui()
      for tab in tabs:
        with gr.Tab(tab.variable()[0]):
          tab()
  
  return block

def start():
  print(".done")
  print("Ctrl+C to Terminate")
  print("Starting logging API..",end="")
  logging.basicConfig(filename="logger/latest.log", encoding="utf-8", level=logging.WARN)
  print(".Done")
  
  create_ui().queue(64).launch(
    inbrowser=True, server_port=9999
  )
  return "Terminated.\nCode: 0"

if __name__ == "__main__":
  print("Building WebUI..",end="")
  print(start())
  time.sleep(3)