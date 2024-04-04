import gradio as gr
import os
import mimetypes
import sys
import subprocess
import importlib.util
import importlib
import logging
from typing import *

## code by. AUTOMATIC1111 / Stable-Diffusion-WebUI
from a1111_ui_util import *

## Prompt Template
from modules.generate import get_template
from modules.generate import generate as template_generate, example_view, applicate_opts, applicate_lora, template_convert
from modules.generate_util import get_lora_list
from modules.character_exchanger import new_character_exchanger as character_exchanger
from modules import make_prompt_template, delete_prompt_template

## Lora Template
from modules import manage_lora_template

## Other
import preprocessing
import modules.shared as shared
import modules.regional_prompter as rp
from modules.sorting import start_sorting
from modules.misc import modify_database, get_js, parse_parsed_arg
from modules.lib import browse_file, show_state_from_checkbox, get_background_picture, resize_picture
from javascript.reload_js import reload_js
from modules.lib_javascript import *
from modules import some_tiny_tweaks, manage_keybox

## LGS
import LGS.misc.nomore_oserror as los
import LGS.misc.jsonconfig as jsoncfg

# some variable
ui_path = os.path.join(shared.ROOT_DIR, "modules", "ui")
rootID_list = ["generate", "manage_template", "MT/define",
              "MT/delete", "MT/restore", "manage_config"]
load_js = {
  # "key": javascript_function
  "overall": javascript_overall
}

# logger
logging.basicConfig(filename="./script_log/latest.log", encoding='utf-8', level=logging.WARNING)

# Tab Class
class UiTabs: 
  """ this code has inspirated by. ddpn08's rvc_webui """
  PATH = ui_path
  
  def __init__(self, path):
    self.filepath = path
    self.rootpath = UiTabs.PATH
    pass
  
  def variable(self) -> Tuple[str]:
    """ return tab_title"""
    return ("Tab_Title")
  
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
      module = importlib.import_module(f"modules.ui.{module_path}.{module_name}")
      
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
            f"modules.ui.{parent}.{module_name}"
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
      
    
    
    # これに関してはわからんけど
    # おそらく self.ui に取得したタブの要素を追加
    def outlet():
      with gr.Tabs():
        for tab in tabs:
          tab:UiTabs # for IDE
          with gr.Tab(tab.variable()[0]): # タイトル
            tab() # __call__ を再実行？
                    
    
    return self.ui(outlet)
  
def get_ui() -> List[UiTabs]:
  tabs = []
  files = [file for file in os.listdir(UiTabs.PATH) if file.endswith(".py")]
  
  for file in files:
    module_name = file[:-3]
    module = importlib.import_module(f"modules.ui.{module_name}")
    
    attrs = module.__dict__
    TabClass = [
      x for x in attrs.values()
      if type(x) == type and issubclass(x, UiTabs) and not x == UiTabs
    ]
    if len(TabClass) > 0:
      tabs.append((file, TabClass[0]))
  
  tabs = sorted([TabClass(file) for file, TabClass in tabs], key=lambda x: x.index())
  return tabs
  
def create_ui():
  block = gr.Blocks(title="lunapy / SD - PEM")
  
  with block:
    with gr.Tabs():
      tabs = get_ui()
      for tab in tabs:
        with gr.Tab(tab.variable()[0]):
          tab()
  
  reload_js()
  return block

def launch_ui(isloopui:bool=False):
  port = parse_parsed_arg(shared.args.ui_port, None, None)
  ip = parse_parsed_arg(shared.args.ui_ip, None)
  if port:
    port = int(port)
  
  ui = create_ui()
  
  ui.queue(64).launch(server_name=ip)
  return "DONE."
  
  # ui.queue(64)
  # ui.launch(
  #   server_port=port,
  #   inbrowser=shared.args.open_browser,
  #   share=shared.args.share,
  #   server_name=ip
  # )

def start():
  print("Ctrl+C to Terminate")
  mimetypes.init()
  mimetypes.add_type('application/javascript', '.js')
  
  if shared.args.loopui:
    print("[UI]: Starting UI with loopui\nclose this window to Terminate")
    try:
      launch_ui(True)
    except KeyboardInterrupt:
      print("[UI]: Terminated with KeyboardInterrupt")
      if shared.args.dev_restart:
        print("[UI]: Restarting UI with reload..")
        nest = os.path.basename(os.path.realpath(shared.ROOT_DIR))
        cmd = os.path.join(
          nest, "launch_user.bat"
        ) + " " + sys.argv[1:]
        subprocess.Popen(
          cmd
        )
        pass
      else:
        print("[UI]: Restarting UI..")
        start()
        pass
  else:
    launch_ui()
    
  return "Terminated"

if __name__ == "__main__":
  if not os.path.exists(os.path.join(shared.ROOT_DIR, "lscript_alreadyprp.ltx")):
    preprocessing.run()

  print(start())