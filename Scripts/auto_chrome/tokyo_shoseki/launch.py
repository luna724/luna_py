import os
import sys
import random
import time
import json
from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import io
import base64
from launch import DRIVER_PATH, ROOT_DIR
DRIVER_PATH:str;ROOT_DIR:str

class VariableStorage:
  humanize = False
  looping = True
  end_estim = time.time() + random.randrange(3600*2, 3600*4, 100)
variable = VariableStorage()

class stop_async: when_video_pause_play_video = True
def jsonread(path): 
  with open(path, "r", encoding="utf-8") as f: return json.load(f)

def loop_start(wait: WebDriverWait):
  def click_next():
    print("click_next called")
    wait.until(
      EC.element_to_be_clickable((By.ID, "pictPlayerTool-next"))
    ).click()
  
  def visualizeSleep(times:float):
    print(f"Sleeping {times}s")
    while not times == 1:
      times -= 1
      print(f"{times}.. ", end="")
      sys.stdout.flush()
      time.sleep(1)
    print("done")
    return
    
  # 60秒以内に動画をユーザーが開始
  _ = wait.until(
    EC.element_to_be_clickable((By.ID, "pictPlayerTool-stop"))
  )
  print("Script started!\nautomatically moved to next video!")
  if variable.humanize:
    print("Humanize = True")
  class end_time: text = None
  
  while variable.looping:
    print(f"Moved to next video.. (Previous video time: {end_time.text})")
    if random.randrange(1, 100, 1) == 1 and variable.humanize:
      print("Stopped by Humanize (onVideoStartedOnePercentage)")
      break;
    if random.randrange(1, 1000, 1) < 10 and variable.humanize:
      print("Video Skipped by Humanize (onVideoStartedSkipHandler)")
      click_next()
    
    visualizeSleep(3)
    video_toolbar = wait.until(
      EC.presence_of_element_located((By.ID, "pictPlayerToolbar"))
    )
    current_time = video_toolbar.find_element(By.ID, "pictPlayerTool-duration1")
    end_time = video_toolbar.find_element(By.ID, "pictPlayerTool-duration2")
    
    while current_time.text != end_time.text:
      current_time = video_toolbar.find_element(By.ID, "pictPlayerTool-duration1")
      end_time = video_toolbar.find_element(By.ID, "pictPlayerTool-duration2")
      if current_time.text == end_time.text: break;
      else:
        if random.random() < 1e-10 and variable.humanize:
          # 停止
          variable.looping = False
          print("Stopped by Humanize (whileLoopingTrigger)")
    
    # クールダウン
    sleepTime = random.randrange(1, 45)
    if variable.humanize: 
      print(f"Sleeping by Humanize ({sleepTime})")
      visualizeSleep(sleepTime)
    if variable.humanize and variable.end_estim < time.time():
      print("Stopped by Humanize (Timeout)")
      break
    click_next()

  raise RuntimeError("While loops closed! (maybe Humanize related)")

def launch(humanize=False) -> None:
  data = jsonread(os.path.join(ROOT_DIR, "tokyo_shoseki", "login_data.json"))
  
  url = "https://kouza.tokyo-shoseki.co.jp/oslms/login"
  options= Options()
  service = Service(DRIVER_PATH)
  driver = webdriver.Chrome(service=service, options=options)
  driver.get(url)
  wait = WebDriverWait(driver, 60)
  variable.humanize = humanize
  
  # ID loginbox を取得
  loginbox = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "loginbox"))
  )
  
  # ID, PASSWORD を入力し、ログイン
  inputs = loginbox.find_elements(By.CLASS_NAME, "input")
  if inputs:
    for input in inputs:
      main_input = input.find_element(By.TAG_NAME, "input")
      if main_input.get_attribute("id") == "loginId":
        main_input.send_keys(data["id"])
      elif main_input.get_attribute("id") == "passwd":
        main_input.send_keys(data["password"])
    
    btn_root = loginbox.find_element(By.CLASS_NAME, "button")
    login_button = btn_root.find_element(By.ID, "loginBtn").click()

  # 移動を待機
  time.sleep((random.randrange(1, 200, step=1) / 100))
  print("Waiting for starting first video..")
  
  if not loop_start(wait):
    raise RuntimeError("loop's Ended NOT Correctly")