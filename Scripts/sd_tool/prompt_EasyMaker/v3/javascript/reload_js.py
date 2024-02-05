import os
from modules.shared import ROOT_DIR as cwd
from modules import shared 
from LGS.misc.nomore_oserror import file_extension_filter
import gradio as gr

class pathss():
    from modules.shared import ROOT_DIR
    modules_path = os.path.join(ROOT_DIR, "modules")
    script_path = os.path.dirname(modules_path)

paths = pathss()

def webpath(fn):
    if fn.startswith(cwd):
        web_path = os.path.relpath(fn, cwd)
    else:
        web_path = os.path.abspath(fn)

    return f'file={web_path}?{os.path.getmtime(fn)}'


def javascript_html():
    script_js = os.path.join(paths.script_path, "script.js")
   # head = f'<script type="text/javascript"> </script>\n'
   
    head = f'<script type="text/javascript" src="{webpath(script_js)}"></script>\n'
    for script in file_extension_filter(os.listdir(os.path.join(cwd, "javascript")), [".js"]):
        script = os.path.join(cwd, "javascript", script)
        head += f'<script type="text/javascript" src="{webpath(script)}"></script>\n'
        
    return head

def css_html():
    head = ""

    def stylesheet(fn):
        return f'<link rel="stylesheet" property="stylesheet" href="{webpath(fn)}">'

    head += stylesheet(os.path.join(cwd, "style.css"))

    return head


def reload_js(): ## Target function
    js = javascript_html()
    css = css_html()
    def template_response(*args, **kwargs):
        res = shared.GradioTemplateResponseOriginal(*args, **kwargs)
        res.body = res.body.replace(b'</head>', f'{js}</head>'.encode("utf8"))
        res.body = res.body.replace(b'</body>', f'{css}</body>'.encode("utf8"))
        res.init_headers()
        return res

    gr.routes.templates.TemplateResponse = template_response

if not hasattr(shared, 'GradioTemplateResponseOriginal'):
    shared.GradioTemplateResponseOriginal = gr.routes.templates.TemplateResponse