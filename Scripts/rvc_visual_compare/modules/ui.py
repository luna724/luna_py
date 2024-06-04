from modules.main import Main
from modules.config_manager import sys_config, config

from typing import Literal, Any, List, Callable
import gradio as gr
import os
import importlib

class UiTabs:
  PATH = os.path.join(os.getcwd(), "modules/tabs")
  
  def __init__(self, path):
    self.filepath = path
    self.rootpath = UiTabs.PATH
    pass
  
  def title(self) -> str:
    """ return tab_title"""
    return "Tab_Title"
  
  def index(self) -> int:
    """ return ui's index """
    return 0
  
  def get_ui(self) -> list:
    tabs = []
    files = [file for file in os.listdir(self.child_path) if file.endswith(".py")]

    for file in files:
      module_name = file[:-3]
      module_path = os.path.relpath(
        self.child_path, UiTabs.PATH 
      ).replace("/", ".").replace("\\", ".").strip(".")
      module = importlib.import_module(f"modules.tabs.{module_path}.{module_name}")
      
      attrs = module.__dict__
      TabClass = [
        x for x in attrs.values() if type(x) == type and issubclass(x, UiTabs) and not x == UiTabs
      ]
      if len(TabClass) > 0:
        tabs.append((file, TabClass[0]))
      
    tabs = sorted([TabClass(file) for file, TabClass in tabs], key= lambda x: x.index())
    return tabs
  
  def ui(self, outlet: Callable):
    """ make ui data 
    don't return """
    pass
  
  # def has_child(self):
  #   return [rootID, child_rel_import_path, importlib's Path]
  
  def __call__(self):
    child_dir = self.filepath[:-3]  #.py を取り除く子ディレクトリの検出
    children = []
    tabs = []
    
    if os.path.isdir(child_dir):
      for file in [file for file in os.listdir(child_dir) if file.endswith(".py")]:
        module_name = file[:-3]
        
        parent = os.path.relpath(
          UiTabs.PATH, UiTabs.PATH
        ).replace(
          "/", "."
        ).strip(".")
        print("parent: ", parent)
        
        children.append(
          importlib.import_module(
            f"modules.tabs.{parent}.{module_name}"
          ) # インポートしていたものを children に追加
        )
        
    children = sorted(children, key=lambda x: x.index())
    
    for child in children:
      # 辞書として変数の値を取得
      # このクラスのサブクラスを発見したら最初のものを追加
      attrs = child.__dict__
      tab = [x for x in attrs.values() if issubclass(x, UiTabs)]
      if len(tab) != 0:
        tabs.append(tab[0])
      
    def outlet():
      with gr.Tabs():
        for tab in tabs:
          tab:UiTabs # for IDE
          with gr.Tab(tab.variable()[0]): 
            tab() 
    
    return self.ui(outlet)


class webui(Main):
  @staticmethod
  def convert_to_none(text:Any, trigger:Any) -> Any | None:
    if text == trigger:
      return None
    
    else:
      return text
  
  def __init__(self, edit_file:Literal["allow", "disallow"]):
    self.written = edit_file == "allow"
    
    super().__init__()
  
  @staticmethod
  def get_ui() -> List[UiTabs]:
    tabs = []
    files = [file for file in os.listdir(UiTabs.PATH) if file.endswith(".py")]
    
    for file in files:
      module_name = file[:-3]
      module = importlib.import_module(f"modules.tabs.{module_name}")
      
      attrs = module.__dict__
      TabClass = [
        x for x in attrs.values()
        if type(x) == type and issubclass(x, UiTabs) and not x == UiTabs
      ]
      if len(TabClass) > 0:
        tabs.append((file, TabClass[0]))
    
    tabs = sorted([TabClass(file) for file, TabClass in tabs], key=lambda x: x.index())
    return tabs
  
  def create_ui(self):
    block = gr.Blocks(title="lunapy / R-VC")
    
    with block:
      with gr.Tabs():
        tabs = self.get_ui()
        for tab in tabs:
          with gr.Tab(tab.title()):
            tab()
    
    return block
  
  def __call__(self):
    ui = self.create_ui()
    ui.queue(64)
    
    ui.launch(
      inbrowser=sys_config.auto_open_browser,
      server_port=self.convert_to_none(config.gradio_port, "?"),
      server_name=self.convert_to_none(config.gradio_ip, "?"),
      share=config._ui_share
    )
    