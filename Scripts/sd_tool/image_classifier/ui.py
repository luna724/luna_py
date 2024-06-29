import gradio as gr

from shared import shared
from proccessing import Processing, run as run_script
import lib
import json

class get_desc:
  def on_path():
    return "Classifier opts"
  def on_tag():
    return "parsing tags (separate with comma)\nThis values use for classify\nto classify \"1girl, solo, rating:safe\"'s image and \"1girl, solo, rating:explicit\"'s image.\ne.g. \"1girl&solo&rating:safe,1girl&solo&rating:explicit,\""
  def status():
    return "Status"
  
def refresh_model():
  lib.listup_models()
  return gr.update(
    choices=shared.dd_models
  )

def refresh_tags():
  lib.update_tags([], True)
  return gr.update(
    choices=Processing.tags
  )

def get_new(cfg_path: tuple):
  """cfg pathに指定された値のコンフィグの細心の値を取得する"""
  with open("config.json", "r", encoding="utf-8") as f: cfg = json.load(f)
  for x in cfg_path:
    cfg = cfg[x]
  
  return cfg

def build(p: Processing, s: shared) -> gr.Blocks:
  with open("config.json", "r", encoding="utf-8") as f: cfg = json.load(f)
  with gr.Blocks(title="lunapy / Image Classifier") as i:
    with gr.Row():
      model = gr.Dropdown(choices=s.dd_models, value=s.dd_models[0], scale=4, label="models")
      model_r = gr.Button("♲", variant="primary", scale=2)
      
      model_r.click(
        refresh_model, outputs=model
      )
      
      tag_info = gr.Dropdown(choices=p.tags, interactive=True, scale=3, label="tags") 
      tag_info_r = gr.Button("♲", variant="primary", scale=1)
      tag_info_r.click(
        refresh_tags, outputs=tag_info
      )

    desc1 = gr.Markdown(get_desc.on_path())
    with gr.Row():
      in_path = gr.Textbox(label="input Directory", value=get_new(("cache","in_path")), scale=4)
      in_path_r = gr.Button("参照", variant="secondary", scale=1)
      out_path = gr.Textbox(label="output Directory", placeholder="if set to '.', output to input Directory", scale=4, value=get_new(("cache", "out_path")))
      out_path_r = gr.Button("参照", variant="secondary", scale=1)
    
    desc2 = gr.Markdown(get_desc.on_tag())
    with gr.Row():
      tagging = gr.Textbox(label="Classify tags (booru tags)", value="",
  lines= 4, max_lines=100)
    
    with gr.Row():
      threshold = gr.Slider(label="Threshold", minimum=0.05, maximum=0.95, value=0.45, step=0.05, scale=7)
      caption_mode = gr.Checkbox(label="Captioning mode (Beta)", value=False, interactive=False, scale=3)
      print_any_log = gr.Checkbox(label="EasyDevelop", value=False, interactive=False)
      
    
    status = gr.Textbox(get_desc.status, interactive=False, every=2000)
    run = gr.Button("Infer", variant="primary")
    run.click(
      run_script, inputs=[
        model, in_path, out_path, tagging, threshold, caption_mode, print_any_log
      ],
      outputs=[status]
    )
  return i