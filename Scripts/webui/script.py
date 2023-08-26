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

def launch_Audio_Augmentation(input_dir, output_dir, output_type, p):
  inputs = input_dir
  outputs = output_dir
  out_type = output_type
  
  aa.Function_mode(inputs, outputs, out_type, p)
  
  return f"Done."

# jtp (jpg to png)
import jpgTopngConverter.main as jtp

def launch_pics_format_converter(a, b, c, d, e, f, g, h):
  jtp.Function_mode(a, b, c, d, e, f, g, h)
  
  return f"Convert Done."


# adc (Audio Duration Calculator)
import audio_lengh_calculator.main as adc
import LGS.misc.re_finder as luna_re

def launch_audio_duration_calculator(a, b, c, d, e):
  # adc_input = [adc_target_dir, adc_td_min_silent, adc_splitsec, adc_split_output, adc_split_skip]
  if c == "Example: 0h 0m 45s 0ms":
    Advanced = False
    Advanced_dict = {"Advanced": Advanced}
  
  else:
    Advanced = True
    
  
  if Advanced:
    set_h = int(luna_re.extract(pattern=r"(\d+)h ", str=c))
    set_m = int(luna_re.extract(pattern=r" (\d+)m ", str=c))
    set_s = int(luna_re.extract(pattern=r" (\d+)s ", str=c))
    set_ms = int(luna_re.extract(pattern=r" (\d+)ms", str=c))
    activate_chance = e // 1000
    
    split_after_sec = (set_h * 3600) + (set_m * 60) + (set_s)
    print(f"split_after_sec: {split_after_sec}")
    split_after = (split_after_sec * 1000) + set_ms
    print(f"split_after: {split_after}")
    
    print(f"Formated Input: {set_h}h {set_m}m {set_s}s {set_ms}ms")
    
    # print(f"split_after: {split_after}")
    
    Advanced_dict = {"Advanced" : Advanced,
                     "SplitAfter": split_after,
                     "Output": d,
                     "Activate_chance": activate_chance
                     }
  
  
  total_time, file = adc.main(target_path=a, ignore_silence_time=b, advanced=Advanced_dict)
  
  if total_time == True:
    return f'\n- {file - 1} File Added. \n\n| Total Duration |\n| --- |\n| {split_after}ms |'
  
  print(f"Return: {total_time}")
  tt = total_time
  
  hour = total_time // 3600
  total_time %= 3600
  missn = total_time // 60
  total_time %= 60
  sec = total_time
  ms2 = sec * 1000
  ms = tt * 1000
  ms_cut = ms2 % 1000
  
  if int(hour) == 0:
    hour_f = ""
  else:
    hour_f =  f"{int(hour)}h"
  
  min_f = f" {int(missn)}m"
  
  # min_f = ""
  
  sec_f = f"{int(sec)}s"
  ms_f = f"{int(ms)}ms"
  
  total_time_format = f"{hour_f}{min_f} {sec_f} {int(ms_cut)}ms"
  
  return f'\n- {file} File Calculated. \n\n| Total Duration | Total Duration (seconds) | Total Duration (millseconds) |\n| --- | --- | --- |\n| {total_time_format} | {int(tt)}s | {ms_f} |'


# Audio Properties Auto Setting
import audio_prop_autogen.main as apas

def Audio_Properties_Auto_Setting(a, b, c, d, e, f, g, h, i, j):
  # def main(target_dir, 
        #  auto_get_composer=False,
        #  songname_pattern="",
        #  pattern_type="replace", # or re
        #  template_title="",
        #  template_artist="",
        #  template_album="",
        #  template_genre="",
        #  template_composer=""):
  
  if b:
    if c == "Example: (.*?)\\ Gamesize":
      pattern = d
      pattern_type = "replace"
    elif d == "Example: Gamesize":
      pattern = c
      pattern_type = "re"
    
    elif not c == "Example: (.*?)\\ Gamesize" and not d == "Example: Gamesize":
      pattern = c
      pattern_type = "re"
    
    else:
      pattern = ""
      pattern_type = ""
  
  else:
    pattern = ""
    pattern_type = ""
  
  apas.main(a, b, pattern, pattern_type, e, f, g, h, i, j)

  return "Done.  <br> <strong>'./backups'</strong> Folder is can Deletable"