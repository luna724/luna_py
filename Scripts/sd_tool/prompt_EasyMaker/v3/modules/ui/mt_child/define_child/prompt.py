import gradio as gr
import os
from typing import List, Literal
import LGS.misc.jsonconfig as jsoncfg

from modules.shared import ROOT_DIR, language
from webui import js_manager, FormColumn, FormRow, show_state_from_checkbox, get_template
from webui import UiTabs, get_lora_list, rp, browse_file, make_prompt_template, get_background_picture, resize_picture
from modules.config.get import cfg as config

class Prompt(UiTabs):
  l = language("/ui/mt_child/define/prompt.py", "raw")
  
  def __init__(self, path):
    super().__init__(path)
    self.child_path = os.path.join(UiTabs.PATH, "mt_child", "define_child", "prompts")
  
  def variable(self):
    return [Prompt.l["tab_title"]]
  
  def index(self):
    return 1
      
  def ui(self, outlet):
    def select_ver(ver):
      invisible = gr.update(visible=False)
      visible = gr.update(visible=True)
      if ver == "v3.0.3":
        return visible, invisible
      elif ver == "v3.0.6":
        return invisible, visible
      
    def get_ver_tabs(tabs:List[UiTabs], rtn_version:Literal["v3.0.3", "v3.0.6"]="v3.0.3") -> UiTabs:
      version_list = {
        "v3.0.3": 1, "v3.0.6": 306
      }
      
      trigger_i = version_list[rtn_version]
      for tab in tabs:
        if tab.index() == trigger_i:
          return tab
    l = Prompt.l

    child_tabs = self.get_ui()
    
    selected_versions = gr.Dropdown(label="[β] Selected Version",choices=[
      "v3.0.3", "v3.0.6"
    ], value="v3.0.3", interactive=True)
    
    
    
    with gr.Column(visible=True) as v303_root:
      with gr.Tabs():
        with gr.Tab("v3.0.3"):
          get_ver_tabs(child_tabs, "v3.0.3")()
    
    with gr.Column(visible=False) as v306_root:
      with gr.Tabs():
        with gr.Tab("v3.0.6"):
          get_ver_tabs(child_tabs, "v3.0.6")()
    
    
    selected_versions.change(
      select_ver, selected_versions, [v303_root, v306_root]
    )