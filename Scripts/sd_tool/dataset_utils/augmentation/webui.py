import gradio as gr
import os
from typing import *
from tkinter import Tk, filedialog

from augmentation.func import functions, average

def browse_directory():
  root = Tk()
  root.attributes("-topmost", True)
  root.withdraw()
  
  filenames = filedialog.askdirectory()
  if len(filenames) > 0:
    root.destroy()
    return str(filenames)
  else:
    filename = "Please select directory."
    root.destroy()
    return str(filename)

def create_ui() -> gr.Blocks:
  component = gr.Blocks()
  with component:
    gr.Markdown("Dataset Image augmentation!")
    
    with gr.Row():
      mode = gr.Dropdown(
        choices=["random", "random(count-Limited)", "select"],
        value="select", interactive=True, label="file selection Mode"
      )
      
      augment_mode = gr.Dropdown(
        choices=["single(random)", "single", "multi", "multi(random)"], value="single",
        interactive=True, label="Augment selection mode"
      )
    
    with gr.Row():
      input_dir = gr.Textbox(
        value="", lines=1, max_lines=1, label="Input path", scale=8, interactive=False
      )
      input_dir_browse = gr.Button(scale=2, size="sm", value="Browse")
    
    with gr.Row():
      output_dir = gr.Textbox(
        value="?replace", lines=1, max_lines=1, label="Output path", scale=8, placeholder="'?replace' for replace previous image", interactive=False
        )
      output_dir_browse = gr.Button(scale=2, size="sm", value="Browse")
    
    with gr.Row():
      with gr.Group(visible=True, elem_id="file_mode") as file_mode_select:
        file_selected = gr.Dropdown(
          label="Target file",
          multiselect=True, choices=["Please select Input dir!"],
          value="Please select Input dir!", interactive=True
        )
        file_refresh = gr.Button(
          "Refresh", size="sm"
        )
        file_refresh.click(
          fn=functions.file_selected_refresh,
          inputs=[input_dir],
          outputs=[file_selected]
        )
      
      with gr.Group(visible=False, elem_id="file_random_count") as file_mode_randc:
        file_max_count = gr.Slider(
          label="Files count limit", value=-1, minimum=-1, maximum=0,
          step=1
        )
        # 指定されたファイル数によって値を変更
      
      with gr.Group(visible=True, elem_id="augment_mode") as augment_mode_single:
        augment_selected = gr.Dropdown(
          label="Target Augment",
          multiselect=False, choices=functions.get_available_augmentation(),
          interactive=True
        )
      
      augment_mode_single_random = gr.Dropdown(
      choices=functions.get_available_augmentation(),
      value=functions.get_default_available_augmentation(), multiselect=True,
      label="Target Augment (choices 1 from selected)", visible=False
      )
      
      with gr.Group(visible=False) as augment_mode_multi:
        augments_selected = gr.Dropdown(
          label="Target Augments",
          multiselect=True, choices=functions.get_available_augmentation(),
          interactive=True, value=functions.get_default_available_augmentation()
        )
      
      with gr.Group(visible=False) as augment_mode_multi_random:
        augments_selected_random = gr.Dropdown(
          choices=functions.get_available_augmentation(),
        value=functions.get_default_available_augmentation(), multiselect=True,
        label="Target Augments (choices any count(set at below) from selected)"
        )
        augments_selected_random_min = gr.Slider(1, len(functions.get_default_available_augmentation()), 1, step=1, label="Augments Min Count")
        augments_selected_random_max = gr.Slider(1, len(functions.get_default_available_augmentation()), 1, step=1, label="Augments Max Count") 
      
    
    status = gr.Textbox(label="Status")
    run = gr.Button("Run with your options", variant="primary")
    average_run = gr.Button("[beta] Run with community recommended options", variant="secondary", size="sm")
    run.click(
      fn=functions.call,
      inputs=[mode, augment_mode,
              input_dir, output_dir, file_selected, file_max_count,
              augment_mode_single_random, augment_selected, augments_selected, augments_selected_random, augments_selected_random_min, augments_selected_random_max],
      outputs=status
    )
    
    average_run.click(
      fn=average.call,
      inputs=[input_dir, output_dir], 
      outputs=status
    )
    
    input_dir_browse.click(
      fn=browse_directory,
      outputs=[input_dir]
    )
    output_dir_browse.click(
      fn=browse_directory,
      outputs=[output_dir]
    )
    
    input_dir.change(
      fn=functions.input_dir_changed,
      inputs=[input_dir],
      outputs=[file_selected, file_max_count]
    )
    
    mode.change(
      fn=functions.file_mode_changed,
      inputs=[mode],
      outputs=[file_mode_select, file_mode_randc]
    )
    augment_mode.change(
      fn=functions.augment_mode_changed,
      inputs=[augment_mode],
      outputs=[augment_mode_single_random, augment_mode_single, augment_mode_multi, augment_mode_multi_random]
    )
    
    augments_selected_random.change(
      fn=functions.augments_selected_random_update,
      inputs=[augments_selected_random],
      outputs=[augments_selected_random_min, augments_selected_random_max]
    )
  return component


def launch():
  create_ui().queue(64).launch(
    inbrowser=True,
    server_port=7965
  )
  return "TERMINATED."