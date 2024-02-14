from javascript.reload_js import reload_js
import gradio as gr
import os
from LGS.misc.jsonconfig import read_text
from modules.shared import ROOT_DIR

def javascript_overall():
  return reload_js()


def js_manager(filepath: str, route=gr.routes.templates.TemplateResponse):
  if os.path.exists(os.path.join(ROOT_DIR, "lunascript", filepath+".js")):
    js = read_text(os.path.join(ROOT_DIR, "lunascript", filepath+".js"))
    
    def template_response(*args, **kwargs):
      response = route(*args, **kwargs)
      response.body = response.body.replace(b'</head>', f"{js}</head>".encode("utf8"))
      
      response.init_headers()
      return response
    
    gr.routes.templates.TemplateResponse = template_response
  else:
    print("Can't found js file: "+filepath)
    return