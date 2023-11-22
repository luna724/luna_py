def help_message():
  message = f"""Help is nothing here."""
  
  return message

import gradio as gr
import random
import os
import requests
import socket
import eyed3
import re
import time
import argparse
import sys
import shutil
from datetime import datetime
from pydub import AudioSegment
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from tqdm import tqdm
from bs4 import BeautifulSoup
import LGS.misc.jsonconfig as jsoncfg
import LGS.misc.nomore_oserror as los

# pjlib
sys.path.append("..\\..\\./module") # luna_py/modules
import pjlib.pjlib as pjlibs

pjlib = pjlibs.project_sekai_lib()


class main_class():
  def get_driver(self):
    config = jsoncfg.read("./config/driver_config.json", silent=True)
    chromebinary = config["Chrome Binary Location"]
    driverpath = config["ChromeDriver Location (if added SystemPATH, can ignored)"]
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chromebinary
    driver = webdriver.Chrome(options=chrome_options)
    return driver

main = main_class()

class Share():
  dev = False
  
  # # # # #
  available_module = ["v2", "v1"]
  available_unit = ["*","leo/need", "more more jump!", "nightcode at 25ji", "wonderlands×showtime", "vivid bad squad", "leo2", "25", "mmj", "vvbs", "dasyo"]
  webui = False
  webui_share = False
  datedict = {
    "MODE": "",
    "MODULE": "",
    "UNIT": "",
    "ANOTHER": False,
    "VIRTUAL_SINGER": False,
    "V1": False,
    "NOLOOP": False,
    "OUTPUT": "",
    "LIMIT": 429,
    "Maximum_WAIT": 60,
    "EXT": "MP3" # or FLAC
  }
shared = Share()

def status_check(response, if404="pass", ifsomething="stderr"):
  if if404 == "pass":
    if404 = True
  else:
    if404 = False
  if ifsomething == "stderr":
    ifsomething = False
  else:
    ifsomething = True
  
  code = response.status_code
  if code == 200:
    return True
  elif code == 404 and if404:
    return False
  elif code == 404 and not if404:
    raise ValueError(f"Response Status: 404 \n({response})")
  elif code != 200 and code != 404 and ifsomething:
    return False
  else:
    raise ValueError(f"Response Status: {code} \n({response})")

def find_free_port():
  # ポート0を指定することで空いているポート番号を取得できる
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 0))
    return s.getsockname()[1]
def dprint(str_, *kwarg):
  if shared.dev:
    for x in kwarg:
      str_ += x
    print(str_)
def done():
  raise ValueError("Done.")

def launch():
  url_dict = {}
  data = shared.datedict
  MODULE = data["MODULE"]
  UNIT = data["UNIT"]
  VS = data["VIRTUAL_SINGER"]
  LOOP = not data["NOLOOP"]
  OUTPUT = data["OUTPUT"]
  LIMIT = data["LIMIT"]
  FILESOURCE = data["EXT"]
  
  os.makedirs("./cache", exist_ok=True)
  
  if OUTPUT == "":
    OUTPUT = "./out"
  
  if OUTPUT == los.filename_resizer(OUTPUT, replaceTo="-"):
    os.makedirs(OUTPUT, exist_ok=True)
  else:
    if shared.webui:
      return "Failed. Reason: filename checking are failed. (if not contain Can't add to Windows filename char, please report to github issues)"
    else:
      raise ValueError("\n\nstderr: Failed. \nReason: filename checking are failed. (if not contain Can't add to Windows filename char, please report to github issues)")
      
  if LOOP:
    os.remove("./already_obtained.json")
    
  cache_num = "0"
  if os.path.exists("./already_obtained.json"):
    cache_num_raw = jsoncfg.read("./already_obtained.json", silent=True)
    cache_num = cache_num_raw["-"]
    
  cache_num = int(cache_num)

  if MODULE == "v2": 
    if UNIT == "*": # 全取得モード
      if cache_num == "0":
        disable_limit = True
      else:
        disable_limit = False
      
      for session in tqdm(range(1, LIMIT), desc="Session"):
        print("Starting Session: ", session, "..", end=" ")
        if session <= cache_num and not disable_limit:
          print("Skipped\nReason: session <= cache_num")
          continue
        
        URL = f"https://sekai.best/music/{session}"
        response = requests.get(URL)
        if not response.status_code == 200:
          if response.status_code == 404:
            print("Skipped\nReason: status = 404 Not Found")
          else:
            print("Failed.\nUnknown Error Occurpted status_code == ",response.status_code)
        else:
          # MODE: Selenium
          
          # ポート番号の取得
          for _ in range(0, 10):
            port = find_free_port()
            service_args = [f'--port={port}']
          
          driver = main.get_driver()
          driver.get(URL)
          
          wait = WebDriverWait(driver, data["Maximum_WAIT"])
          time.sleep(2.42)
          
          # タイトルを取得
          try:
            song_title_element = wait.until(EC.presence_of_element_located((By.XPATH, "//h6[@class='MuiTypography-root MuiTypography-h6 css-1u18iur']")))
            song_title_element = wait.until(EC.presence_of_element_located((By.XPATH, "//h6[@class='MuiTypography-root MuiTypography-h6 css-1u18iur']")))
          except Exception as error:
            driver.quit()
            print(f"Error Catched on driver.get(): ERROR\n{error}")
            continue
          
          song_title = song_title_element.text
          dprint(f"\nObtained Song Title: {song_title}")
          
          # とりあえず、バチャシンDL
          #if VS:
          #  download_element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//svg[@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv']"))).click()
          #else:  # え？ しないの？
          #  download_element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//svg[@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv']")))
          # 作曲者の設定
          # /html/body/div[1]/div/div[3]/div[2]/div[5]/div[7]/p
          artist_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div[5]/div[7]/p")))
          artist_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div[5]/div[7]/p")))
          
          artist = artist_element.text
          dprint(f"Obtained Artist: {artist}")
          
          # 合計ボーカルタイプを取得
          # エレメント解析、特定クラスの数を vocal_count に代入
          vocal_root_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[3]/div/div[2]')))
          html = vocal_root_element.get_attribute('outerHTML')
          dprint(f"HTML: {html}")
          jsoncfg.write_text(filepath="./cache/vocal_root_element_html.lunacache", data=f"HTML: \n{html}")
          
          soup = BeautifulSoup(html, "html.parser")
          vocal_element = soup.find_all("input", class_="PrivateSwitchBase-input css-1m9pwf3", attrs={"name": "vocal-type"})
          dprint(f"Vocal_element: {vocal_element}")
          
          vocal_count = len(vocal_element)
          dprint(f"vocal_count: {vocal_count}")
          
          for x in tqdm(range(0, vocal_count),desc="Vocal Downloading.."):
            dprint(f"Vocal Session: {x}")
            # ボーカル数に応じて処理を行う
            time.sleep(1.5)
            
            # MuiGrid-root MuiGrid-container MuiGrid-item MuiGrid-spacing-xs-1 MuiGrid-grid-xs-12 MuiGrid-grid-md-9 css-18ou6kw
            # ボーカル摘出ラインまでHTMLを絞り込む
            #vocal_extract_element = wait.until(EC.presence_of_element_located((
            #  By.XPATH, 
            #  '/')))
            soup = BeautifulSoup(html, "html.parser")
            soup_stableopen_div = soup.find("div", class_="MuiGrid-root MuiGrid-container MuiGrid-item MuiGrid-spacing-xs-1 MuiGrid-grid-xs-12 MuiGrid-grid-md-9 css-18ou6kw")
            soup_stableopen = soup_stableopen_div.find("div", class_="MuiFormControl-root css-13sljp9")
            vocal_selection_root = soup_stableopen.find("div", class_="MuiFormGroup-root MuiFormGroup-row css-p58oka")
            
            # ボーカル種類別エレメントをひとつづつ処理
            target_list = vocal_selection_root.find_all("label", class_="MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd css-kswqkt")
            target = target_list[x]
            dprint(f"Target: {target} (in {target_list})")
            jsoncfg.write_text(filepath="./cache/vocal_selection_root_target_html", data=f"HTML: \n{target}")
            
            # singer ID の取得 + ファイル名処理
            soup_stableopen = target.find(
              "div", class_="MuiGrid-root MuiGrid-container css-cgxzmc"
            )
            singers = soup_stableopen.find_all(
              "div", class_="MuiGrid-root MuiGrid-item css-1wxaqej"
            )
            dprint(f"got singers: {len(singers)}")
            
            singer_list = []
            for singer in singers:
              img_element = singer.find("img")
              if not img_element == None:
                ch_id_raw = img_element.get("alt")
                dprint(f"ch_id_raw: {ch_id_raw}")
              
                pattern = r"character (\d+)"
                ch_id = re.findall(pattern, ch_id_raw)[0]
                dprint(f"ch_id: {ch_id}")
              else:
                ch_id = 27
              # キャラクター名を取得
              singer_list.append(
                pjlib.character_id_to_name[int(ch_id)]
              )
              dprint(f"appended {pjlib.character_id_to_name[int(ch_id)]}")
            
            if not len(singer_list) == 0:
              if not x == 1: # sekai ver じゃないなら
                song_title_resized = song_title.split(" | ")[0]
                filename = f"{song_title_resized} ft. "
                for name in singer_list:
                  filename += f"{name}、"
                
                filename = filename.strip("、")
              else: # sekai ver
                filename = f"{song_title_resized} Gamesize"
              
              dprint(f"filename: {filename}")
              
              # 情報をもとに URL を作成
              base_url1 = "https://storage.sekai.best/sekai-assets/music/long/{:04d}_{:02d}_rip/{:04d}_{:02d}.mp3"
              base_url2 = "https://storage.sekai.best/sekai-assets/music/long/{}_{:04d}_{:02d}_rip/{}_{:04d}_{:02d}.mp3"

              song_id = session
              vocal_id = x +1 
              lvocal_id = vocal_id
              mode = ""
              # mode の取得
              if vocal_id == 0:
                mode = "vs"
              elif vocal_id == 1:
                mode = "se"
              else:
                mode = "an"
                vocal_id -= 2
              
              url1 = base_url1.format(
                song_id, lvocal_id, song_id, lvocal_id
              )
              
              url2 = base_url2.format(
                mode, song_id, vocal_id, mode, song_id, vocal_id
              )
              
              if not VS and mode == "vs":
                dprint("Skipped download. bc this is Virtual Singer")
                pass
              url_dict[f"{filename}"] = (url1, url2, artist)
              print("done")
              jsoncfg.write(url_dict, "./cache/cache_url_dict.json",silent=True)
          driver.quit()
          
      
      # ダウンロード処理
      print("all session is successfully completed")
      dprint("Done!")
      jsoncfg.write(url_dict, "./cache/previous_session.json")
      for filename, urls in tqdm(url_dict.items(), desc="Downloading.."):
        print(f"Downloading file {filename}... ", end="")
        dprint(f"Starting Download: \nfilename: {filename}\nURL: {urls[:1]}")
        filename = los.filename_resizer(filename, replaceTo="_")
        legacy_url = urls[0]
        url = urls[1]
        artist_ = urls[2]
        new_ = True
        time.sleep(0.5)
        response_legacy = requests.get(legacy_url)
        response_new = requests.get(url)
        time.sleep(1.25)
        
        if status_check(response_legacy):
          new_ = False
          content = response.content
          dprint("Response Data: Legacy")
          dprint(f"content Data: -> {filename}")
          legacy_ = True
        if status_check(response_new):
          legacy_ = False
          content = response.content
          dprint("Response Data: New")
          dprint(f"content Data: -> {filename}")
          new_ = True
        
        if not filename.endswith(".mp3") and FILESOURCE == "MP3":
          filename += ".mp3"
        elif not filename.endswith(".flac") and FILESOURCE == "FLAC":
          filename += ".flac"
        
        with open(os.path.join(os.getcwd(), "cache", filename), "wb") as f:
          f.write(content)
        
        # 作曲者の設定
        audiofile = eyed3.load(os.path.join(os.getcwd(), "cache", filename))
        
        audiofile.tag.artist = artist_
        audiofile.tag.save()
        
        # 最初の8.5秒を消す
        audio = AudioSegment.from_file(os.path.join(os.getcwd(), "cache", filename))
        cut_audio = audio[:8500]
        cut_audio.export(os.path.join(os.getcwd(), OUTPUT, filename), format=FILESOURCE.lower())
      
      os.makedirs("logs", exist_ok=True)
      shutil.move(os.path.join(os.getcwd(), "cache", "previous_session.json"), os.path.join(os.getcwd(), "logs", f"session-TIME{datetime.now().strftime('%Y%m%d-')}{random.randrange(1, 2100000000)}.json"))
      shutil.rmtree("./cache")

class WebUI():
  def stable(self):
    return
  
  def dev(self):
    with gr.Blocks() as iface:
      gr.Markdown("UIMODE: DEBUG (WebUI.dev)")
      
      mode = gr.Radio(
        label="Module Mode",
        choices=["Selenium (v2)", "Silent (v1)", "pyautogui (v1)"],
        value="Selenium (v2)"
      )
    
    return iface
webui_instance = WebUI()

def itrmain(
  mode, #Module Mode ["Selenium (v2)", "Silent (v1)", "pyautogui (v1)"]
  
):
  return


def arg_parser():
  parser = argparse.ArgumentParser(description="parser")
  
  parser.add_argument('--webui', action='store_true')
  parser.add_argument('--unit')
  parser.add_argument('--another_vocal', action='store_true')
  parser.add_argument('--module')
  parser.add_argument('--virtual_singer', action='store_true')
  parser.add_argument('--mode')
  parser.add_argument('--noloop', action='store_true') # 取得済みの曲を再取得しない
  parser.add_argument('--v1', action='store_true')
  parser.add_argument('--info_arg', action='store_true')
  parser.add_argument('--output')
  parser.add_argument('--share_webui', action='store_true')
  parser.add_argument('--dev', action='store_true')

  args = parser.parse_args()
  
  #dev
  if args.dev:
    shared.dev = args.dev
  else:
    shared.dev = False
  
  # フォーマット
  if not args.webui and not args.info_arg:
    datedict = shared.datedict
    if args.unit:
      unit = args.unit
      if unit.lower() in shared.available_unit:
        datedict["UNIT"] = unit
    if args.another_vocal:
      another = args.another_vocal
      datedict["ANOTHER"] = another
      print("WARN: \"--another_vocal\" is Disabled.")
    if args.module:
      module = args.module
      if module.lower() in shared.available_module:
        datedict["MODULE"] = module
    if args.virtual_singer:
      vsinger = args.virtual_singer
      datedict["VIRTUAL_SINGER"] = vsinger
    if args.mode:
      print("notify: \"--mode\" argument is no longer supported.\nplease Use \"--module\" instead.")
      mode = args.mode
      if mode.lower() in ["instant", "legacy"]:
        # datedict["MODE"] = mode
        datedict["MODE"] = mode
    if args.noloop:
      noloop = args.noloop
      datedict["NOLOOP"] = noloop
    if args.output:
      output = args.output
    else:
      output = "./out"
    datedict["OUTPUT"] = output
    
    shared.datedict = datedict
    
  elif args.info_arg:
    if args.webui:
      print("WARN: \"--info_arg\" detected.\n\"--webui\" are Terminated.")
    print(help_message())
    exit()
  
  elif args.webui:
    if args.share_webui:
      print("launching webui with \"--share_webui\"..")
      shared.webui = True
      shared.webui_share = True
    else:
      print("launching webui..")
      shared.webui = True
      shared.webui_share = False
  
  print("argparse done.")

def launch_webui():
  if shared.webui:
    iface = webui_instance.stable()
    if shared.dev:
      iface = webui_instance.dev()
    
    iface.launch(
      share=shared.webui_share,
      port=25567
    )
  else:
    print("webui are not hooked")
    launch()

if __name__ == "__main__":
  arg_parser()
  launch_webui()
  