from typing import Literal
import gradio as gr

class launch:
  def __init__(self, env_type:Literal["pem", "pdb"], **kwargs):
    self.is_api= env_type == "pdb"
    if self.is_api:
      raise RuntimeError("class webui.py:launch was called from SDPDB.\nthat class is ONLY supported SDPEM. please remove them.")
    
  @staticmethod
  def launch_ui():
    return
  
  @staticmethod
  def build_ui() -> gr.Blocks:
    return
  
  def __call__(self):
    ui = self.build_ui()
    raise TimeoutError(self.launch_ui(ui))

# Define Importer
if "__main__" == "pem_launcher.py":
  import lunapy_module_importer
  lunapy_module_importer.Importer = lunapy_module_importer.moduleImporter("pem")