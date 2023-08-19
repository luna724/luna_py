import os
import sys
import os
from tkinter import Tk, filedialog

# Scripts/をパスに追加
sys.path.append("..\\")

# Import
import LightChanger.main as lc

def launch_LightChanger(LightLevel):
  # Input = slider(0, 100)
  # output = text
  values = LightLevel
  lc.Function_mode(values)
  
  return f"Successfully Turned Light Level to <strong>{values}</strong>."


# フォルダ選択画面の関数
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
        filename = "Folder not seleceted"
        root.destroy()
        return str(filename)

# ファイル選択画面の関数
def browse_file():
  root = Tk()
  root.attributes("-topmost", True)
  root.withdraw()
  
  filenames = filedialog.askopenfilenames()
  if len(filenames) > 0:
      root.destroy()
      return str(filenames)
  else:
      filename = "Files not seleceted"
      root.destroy()
      return str(filename)

# Audio Augmentation
import audio_augmentation.main as aa

def launch_Audio_Augmentation(input_dir, output_dir, output_type):
  inputs = input_dir
  outputs = output_dir
  out_type = output_type
  
  aa.Function_mode(inputs, outputs, out_type)
  
  return f"Done."

# jtp (jpg to png)
import jpgTopngConverter.main as jtp

def launch_pics_format_converter(a, b, c, d, e, f, g, h):
  jtp.Function_mode(a, b, c, d, e, f, g, h)
  
  return f"Convert Done."