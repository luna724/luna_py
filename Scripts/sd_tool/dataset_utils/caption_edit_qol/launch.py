import sys
sys.path.append("..\\")

from tkinter import Tk, filedialog
from LGS.misc.jsonconfig import read_text, write_text
from PIL import Image
import os
import gradio as gr

def browse_folder():
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()

    filename = filedialog.askdirectory()
    if filename:
        if os.path.isdir(filename):
            root.destroy()
            return str(filename)
        else:
            root.destroy()
            return str(filename)
    else:
        filename = "Folder not selected"
        root.destroy()
        return str(filename)

def get_nested_files(root_dir):
  file_list = []
  for root, dirs, files in os.walk(root_dir):
      for file in files:
              file_path = os.path.join(root, file)
              file_list.append(file_path)
  return file_list

class main():
  def replace(self, replace_target, caption, *args):
    # return resized_caption, status
    replace = replace_target.strip().split(";")
    caption_piece = caption.strip().split(",")
    copied_caption = caption_piece
    if len(replace) <= 0:
      return caption, "Failed. Error: (Replace Target not found.)"
    
    # 入力 "hello;example" なら hello と example を取り除き、 "," を消す
    for x in replace:
      print(f"Scanning {x}..")
      for y in caption_piece:
        if x.strip().lower() == y.strip().lower():
          copied_caption.remove(y)
    
    # キャプションを生成
    new_caption = ""
    for x in copied_caption:
      new_caption += f"{x.strip()}, "
    new_caption.strip(", ")
    
    # 重複コンマを消す
    caption = new_caption.replace(", ,", ",").replace(",,", ",").strip(",").strip().strip(",").strip()
    print(f"return: {caption}")
    
    return caption, f"Success"
  
  def save_caption(self, caption, filepath, backup):
    if backup:
      os.rename(filepath, filepath + "prvfile..")
    
    write_text(caption, filepath, True)
    # return status, caption, path
    return "Success", caption, filepath
    
  def load_directory(self, target_path, load_tree, load_extension, caption_extension):
    if not os.path.exists(target_path):
      return "", ""
    if not os.path.isdir(target_path):
      return "", ""
    
    raw_accepted_ext = load_extension.strip().split(";")
    accepted_ext = []
    for x in raw_accepted_ext:
      accepted_ext.append(f".{x}")
    
    if load_tree:
      listfile = get_nested_files(target_path)
    else:
      listfile = os.listdir(target_path)
    
    files = []
    for x in listfile:
      if os.path.isdir(x):
        continue
      print(x)
      if os.path.splitext(x)[1] in accepted_ext:
        print(f"[0] = {os.path.splitext(x)[0]}")
        print("catched.")
        files.append(x)
        continue
    
    # relpath のリストを返す
    rtn = []
    for x in files:
      rtn.append(os.path.relpath(x, target_path))
    
    print("Return: ", rtn)
    # return loadfrom (gr.Dropdown.update())
    return gr.Dropdown.update(
      choices=rtn
    ), target_path
  
  def load_this_file(self, loadfrom, caption_extension, root_path):
    caption_path = os.path.splitext(loadfrom)[0] + caption_extension
    target_file_path = os.path.join(root_path, caption_path)
    
    with Image.open(os.path.join(root_path, loadfrom)) as img:
      w = img.width
      h = img.height
      res = f"{w}x{h}"
    
    if os.path.exists(target_file_path):
      caption = read_text(os.path.join(root_path, caption_path))
    else:
      return target_file_path, os.path.join(root_path, loadfrom), loadfrom, res, "WARN: Caption File not found."
    return target_file_path, os.path.join(root_path, loadfrom), caption, res, "Success"
    # return target_file_path, target_file_image, target_file_caption, status

resize_prompt = main()

def get_ui():
  with gr.Blocks() as iface:
    gr.Markdown("dataset_utils / caption_edit_qol")
    
    with gr.Tab("Text Resizer"):
      with gr.Row():
        replace_target = gr.Textbox(label="Replace Target Prompt", placeholder="Syntax: (if you need delete Prompt \"censored\" and \"nsfw\"\n input: \"censored|nsfw\")")
        replace_btn = gr.Button("Replace")
      
      target_file_path = gr.Textbox(label="File path", interactive=False)
      with gr.Row():
        with gr.Column():
          target_file_image = gr.Image(label="Image", height=512, width=512)
          target_file_res = gr.Textbox(label="Image Resolution", interactive=False)
        target_file_caption = gr.Textbox(label="Selected Image's Caption", lines=25)
      with gr.Row():
        save = gr.Button("Save this Caption")
        backup = gr.Checkbox(label="Backup Previous Caption (Worst Quality)", value=True)
      gr.Markdown("<br>")
      with gr.Row():
        loadfrom = gr.Dropdown(label="Loaded File")
        caption_extension = gr.Textbox(label="Caption File Extension", placeholder=".txt", value=".txt")
        load_this = gr.Button("Load this File")
      with gr.Row():
        target_path = gr.Textbox(label="Target Path")
        tp_browse = gr.Button("Browse File")
        tp_browse.click(fn=browse_folder, outputs=[target_path])
      with gr.Row():
        load_tree = gr.Checkbox(label="Load tree image", value=True, interactive=False)
        load_ext = gr.Textbox(label="Load Extension", placeholder="png;jpg", value="png")
      current_path = gr.Textbox(label="Current Loaded Directory", interactive=False)
      load = gr.Button("Load Directory")
      
      status = gr.Textbox(label="Status")
      
      save.click(fn=resize_prompt.save_caption,
                  inputs=[
                    target_file_caption, target_file_path, backup
                  ], outputs=[
                    status, target_file_caption, target_file_path
                  ])
      load.click(fn=resize_prompt.load_directory,
                  inputs=[
                  target_path, load_tree, load_ext, caption_extension
                  ],
                  outputs=[
                  loadfrom, current_path
                  ])
      load_this.click(fn=resize_prompt.load_this_file,
                      inputs=[
                        loadfrom, caption_extension, current_path
                      ],
                      outputs=[
                        target_file_path, target_file_image, target_file_caption, target_file_res, status
                      ])
      replace_btn.click(fn=resize_prompt.replace,
                        inputs=[
                          replace_target, target_file_caption
                        ], outputs=[
                          target_file_caption, status
                        ])

  return iface

def launch():
  ui = get_ui()
  ui.queue(64)
  ui.launch()
  return


if __name__ == "__main__":
  launch()