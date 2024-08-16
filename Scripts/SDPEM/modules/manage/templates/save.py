from lunapy_module_importer import Importer, Importable
import gradio as gr

generatorTypes = Importer("modules.types", isTypes="generator")
class save(generatorTypes):
  def __init__(self):
    template_utils = Importer("modules.template_util")
    super().__init__()
    self.get_templates = self.generate_common.obtain_template_list
    self.get_lora = self.generate_common.obtain_lora_list
    self.model_db = Importer("modules.model_db")
    
    self.baseData = template_utils.getBase.templates
  
    # Variable for UI
    self.available_versions:list = ["v4.0"]
    self.avv_information:dict = {
      # AVV: ["gr.Info caller", save_method_function]
      "v4.0": ["[v4.0]: Compatibility UI version: (v4.1.1R ~ v4.1.1R)", None],
      "v3.0.3": ["[v3.0.3]: Compatibility UI version: V3", None],
      "βv4.1": ["[β4.1]: Compatibility UI version: (None)", None]
    }
  
  # change method
  def activate_method(self, activater):
    """return: (activate.change, disable.change, accordion.change)"""
    if activater:
      return (
        gr.Checkbox.update(visible=False, value=False),
        gr. Checkbox.update(visible=True, value=False),
        gr.update(visible=True)
      )
  
  def deactivate_method(self, deactivater):
    """return: (activate.change, disable.change, accordion.change)"""
    if deactivater:
      return (
        gr.Checkbox.update(visible=True, value=False),
        gr.Checkbox.update(visible=False,value=False),
        gr.update(visible=False)
      )
  
  def selected_version_changer(self, current):
    try:
      info = self.avv_information[current]
      if info[1] is None:
        raise KeyError()
    except KeyError:
      raise gr.Error("version data wasn't found.\n[ErrID:SAVE-000]: this error is NOT throwable")
    desc = info[0]
    self.save = info[1]
    
    if desc is None or desc == "":
      raise gr.Error("version info wasn't found.\n[ErrID:SAVE-001]: Throwable")
    gr.Info(desc)
  
  
    
class _save:
  def __call__(self, **kwargs):
    return save()