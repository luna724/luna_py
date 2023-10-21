import sys

sys.path.append("")

# >_<
from v3 import new_main as v3
from lib import *

from LGS.misc.nomore_oserror import file_extension_filter
import LGS.misc.jsonconfig as jsoncfg
from LGS.misc.random_roll import random_roll as roll

# import
import subprocess
from multiprocessing import cpu_count, Pool
import multiprocessing as mp
import gradio as gr
from tqdm import tqdm
import os
import time


def start(
  version: str = "v3",
  target_characters: str = "1",
  target_unit: str = "Leo/need",
  output_dir: str = "./outputs",
  filenames: str = "out",
  multiprocessing: bool = True,
  use_cpu: int = 75,
  use_aria2: bool = True,
  multi_download: int = 12,
  randget: bool = False,
  randcount: int = 100
  ):
  print("Use URL Cache: True")
  os.makedirs(output_dir, exist_ok=True)
  target_character = target_characters.split(",")
  target_event = [""]
  dataset_info = False
  # len(0) チェック
  for target in [target_event, target_character]:
    lencheck(target)
  
  multi = True
  
  # マルチならマルチモード開始
  if multi:
    yield "Preprocessing.."
    data = launch_multi(target_event, target_character,
                  use_aria2, target_unit, randget, dataset_info)
    # データを処理してダウンロード
    urls = []
    for url in data.values():
      if urlcheck(url):
        continue
      else:
        urls.append(url)
      
    # マルチプロセスで処理
    cpu_per = use_cpu / 100
    cpu = int(cpu_count() * cpu_per)
    
    while cpu_count() < cpu:
      print(f"CPU -1 ({cpu-1})")
      cpu -= 1
    
    yield "URL Status Checking.."
    with Pool(processes=cpu) as pool:
      results = list(tqdm(pool.imap(status_check, urls), total=len(urls), desc="URL Status Checking.."))
    
    status_200, status_404 = result_unzipper(results)
    copy_status_200 = status_200
    
    # ランダム取得なら目的数まで減らす
    if randget:
      while len(copy_status_200) > randcount:
        for x in status_200:
          if roll(0.01):
            copy_status_200.remove(x)   
    else:
      copy_status_200 = status_200
    
    url_200 = copy_status_200
    
    
    yield "Downloading.."
    if version == "v3":
      os.chdir("./v3")
      v3.request_multi(url_200, output_dir, 0.001)
      x = 0
      for file in file_extension_filter(os.listdir()):
        filename = f"{filenames}-data({x:04d}).mp3"
        
        os.rename(
          os.path.join(output_dir, file),
          os.path.join(output_dir, filename)
        )
        
        x += 1
      os.chdir("..\\")
    elif version == "v4":
      if not use_aria2:
        print("WARNING: You are not using Aria2.\nDownload mode was forced to single processing mode!")
      for url in tqdm(url_200, desc="Downloading File.."):
        if use_aria2:
          x = 0
          filename = f"{filenames}.{x:04d}.mp3"
          # ダウンロード
          cmd = f"aria2c --console-log-level=error -c -x {multi_download} {url} -d {output_dir} -o {filename}"
          subprocess.Popen(cmd)
          time.sleep(0.5)
          
          x += 1
          
        else:
          x = 0
          filename = f"{filenames}.{x:04d}.mp3"
          v3.save_data(url, output_dir, 0.00001)
          x = 0
      
      if not use_aria2:
        for file in file_extension_filter(os.listdir(output_dir)):
          filename = f"{filenames}-data({x:04d}).mp3"
          
          os.rename(
            os.path.join(output_dir, file),
            os.path.join(output_dir, filename)
          )
          
          x += 1
      
      if use_aria2:
        print("Waiting For Download ending..")
        # ダウンロード終了待機
        cmd = "aria2c -c -x 12 --console-log-level=error https://storage.sekai.best/sekai-assets/character/member/res001_no001_rip/card_normal.png -d ./cache -o file"
        subprocess.run(cmd)
        print("done..")
      
      if os.path.exists("./404_list.json"):
        datedict = jsoncfg.read("./404_list.json")
      else:
        datedict = {
          "404_list": []
        }
      
      datedict["404_list"].extend(status_404)
      
      jsoncfg.write(datedict, "./404_list.json")
      return "Process Done."
      

def create():
  with gr.Blocks() as i:
    with gr.Blocks():
      with gr.Row():
        mode = gr.Radio(choices=["v3", "v4"], value="v4", label="Script Version")
        multi = gr.Checkbox(label="MultiProcessing Mode (v3 = 5process / v4 = 12process)", value=True, visible=False)

    with gr.Blocks():
      with gr.Row():
        target_character = gr.Textbox(label="Target Character ID  (v3 / v4)", placeholder="1,2,3,4", value="1")
      with gr.Row():
        target_unit = gr.Radio(choices=["Leo/need","MORE MORE JUMP!"], value="Leo/need", label="Target Unit (Event)")
      with gr.Row():
        output_dir = gr.Textbox(label="Output Directory", value="./outputs")
        filenames = gr.Textbox(label="Base Filename", value="星乃一歌")
      with gr.Row():
        use_cpu = gr.Slider(1, 100, step=1, value=50, label="Using CPU Percentage (v4)")
        with gr.Column():
          use_aria2 = gr.Checkbox(value=True, label="Use Aria2c (v4)")
          download_count = gr.Slider(1, 16, step=1,label="Aria2c Download Session Count (-x)",value=12)
      with gr.Row():
        randget = gr.Checkbox(label="Random Getting", value=False)
        randcount = gr.Slider(1, 5000, step=1, label="Random Getting Limit Count", value=1)
    
    status = gr.Textbox(label="Status")
    btn = gr.Button("Start")
    
    btn.click(
      fn=start,
      inputs=[mode, target_character, target_unit,
              output_dir, filenames, multi, use_cpu, use_aria2, download_count,
              randget, randcount],
      outputs=status
    )
    
  return i

# ui を実行
if __name__ == "__main__":
  iface = create()
  iface.queue(64)
  iface.launch(
    server_port=25567,
    inbrowser=True
  )