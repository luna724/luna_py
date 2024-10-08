from webui import UiTabs, os, gr
from typing import *
from lunapy_module_importer import Importer

class Template(UiTabs):
  def __init__(self, path):
    super().__init__(path)
    self.child_path = os.path.join(UiTabs.PATH, "define_child", "lora_versions")
  
  def title(self):
    return "LoRA"

  def index(self):
    return 1
  
  def ui(self, outlet):
    def selected_ver(ver):
      module.selected_version_changer(ver)
      invisible = gr.update(visible=False)
      visible = gr.update(visible=True)
      
      if ver == "v4.0":
        return visible
    
    tmpl_common = Importer("modules.generate.common")
    get_template = tmpl_common.obtain_template_list
    get_lora_template = tmpl_common.obtain_lora_list
    
    module = Importer("modules.manage.templates.save")
    AVV = module.available_versions
    
    with gr.Blocks() as iface:
      ver = gr.Markdown("CURRENTLY Alpha: v4.0-pre1")
      
      selected_version = gr.Dropdown(AVV, value=AVV[0], label="Selected version")
      selected_version.change(
        selected_ver,
        selected_version
      )
      ## TODO: get versions (e.g. v3/modules/ui/mt_child/define_child/prompt.py)
      
      