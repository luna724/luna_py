import os
import asyncio
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

class stop_async:
  when_video_pause_play_video = True


def jsonread(path): 
  with open(path, "r", encoding="utf-8") as f: return json.load(f)

async def when_video_pause_play_video(pictPlayerToolPlay_Element:WebElement, driver: webdriver.Chrome):
  """ 非同期的に再生ボタンを検出する関数 
  止まった場合、自動的に再開する"""
  def check(pictPlayerToolPlay_Element:WebElement):
    if pictPlayerToolPlay_Element.get_attribute("data-value") == "play":
      return False
    elif pictPlayerToolPlay_Element.get_attribute("data-value") == "pause":
      return True
  
  while stop_async.when_video_pause_play_video:
    while check(pictPlayerToolPlay_Element):
      continue
    driver.execute_script("arguments[0].click();", pictPlayerToolPlay_Element)

def launch(url=None) -> None:
  data = jsonread(os.path.join(ROOT_DIR, "tokyo_shoseki", "login_data.json"))
  
  url = "https://kouza.tokyo-shoseki.co.jp/oslms/login"
  options= Options()
  service = Service(DRIVER_PATH)
  driver = webdriver.Chrome(service=service, options=options)
  driver.get(url)
  wait = WebDriverWait(driver, 60)
  
  # ID loginbox を取得
  loginbox = wait.until(
    EC.presence_of_element_located((By.ID, "loginbox"))
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
  
  # 60秒以内に動画をユーザーが開始
  _ = wait.until(
    EC.element_to_be_clickable((By.ID, "pictPlayerTool-stop"))
  )
  print("Script started!\nautomatically moved to next video!")
  class end_time: text = None
  
  while True:
    print(f"Moved to next video.. (Previous video time: {end_time.text})")
    time.sleep(3)
    video_toolbar = wait.until(
      EC.presence_of_element_located((By.ID, "pictPlayerToolbar"))
    )
    current_time = video_toolbar.find_element(By.ID, "pictPlayerTool-duration1")
    end_time = video_toolbar.find_element(By.ID, "pictPlayerTool-duration2")
    #video_paused = 
    
    while current_time.text != end_time.text:
      current_time = video_toolbar.find_element(By.ID, "pictPlayerTool-duration1")
      end_time = video_toolbar.find_element(By.ID, "pictPlayerTool-duration2")
    
    clickable = wait.until(
      EC.element_to_be_clickable((By.ID, "pictPlayerTool-next"))
    ).click()
  
  # # テーブルリストに飛ぶ
  # mainbox = wait.until(
  #   EC.presence_of_element_located((By.ID, "kyokaPages"))
  # )
  # contents = mainbox.find_elements(By.CLASS_NAME, "contents")[0]
  # table = contents.find_element(By.XPATH, "//table[@class='list']")
  # body = table.find_element(By.TAG_NAME, "tbody")
  # trs = body.find_elements(By.CLASS_NAME, "dataRow")
  
  # # 残りの ToDo を保存
  # available_kyoka = trs
  # for todo in trs:
  #   print("todo started!")
  #   todo.click()
  #   time.sleep(1)
  #   lecture = mainbox.find_element(By.ID, "mLecture")
  #   content = lecture.find_element(By.CLASS_NAME, "contents")
  #   # root_div = content.find_element(By.CLASS_NAME, "ckr4kgk")
  #   list_div = content.find_elements(By.XPATH, "//div/div[@class='bk']")# + content.find_elements(By.XPATH, "//div[@class='rw data1']")
    
  #   print("list_div: ", list_div)
  #   time.sleep(4)
  #   for div in list_div:
  #     print("list div called! (near line92)")
  #     time.sleep(2.5)
      
  #     video_lists = div.find_elements(By.XPATH, "//div[@class='rw data2']")
  #     print("video_lists: ", video_lists)
  #     for video in video_lists:
  #       if video.get_attribute("data-playable") != "on":
  #         continue
        
  #       complete = video.get_attribute("data-complete")
  #       # クリア済みかどうかを取得
  #       if complete == "on":
  #         isCompleted = True
  #       else:
  #         isCompleted = False
        
  #       time.sleep(2)
  #       integrate = video.find_element(By.XPATH, "//div[@class='co integrate']")
  #       play_btn = integrate.find_element(By.XPATH, "//div[@class='item play movie']")
  #       timeroot = play_btn.find_element(By.CLASS_NAME, "icon")
  #       video_time = timeroot.find_element(By.TAG_NAME, "div")
  #       size = play_btn.size
  #       location = play_btn.location
  #       print(f"Size: {size}, Location: {location}")

        
  #       print(f"Try to starting play video..\nVideo time: {video_time}")
  #       # ActionChains(driver).move_to_element(timeroot).perform()
  #       driver.execute_script("arguments[0].click();", play_btn)
  #       time.sleep(1)
  #       #timeroot.click()
  #       print("Started!")
  #       # 動画開始処理
  #       playerpages = wait.until(
  #         EC.presence_of_element_located((By.ID, "playerPages")))
  #       toolbar = playerpages.find_element(By.ID, "pictPlayerToolbar")
  #       maxtime = toolbar.find_element(By.ID, "pictPlayerTool-duration2")
  #       mintime = None
        
  #       # 再生ボタンは常に検知
  #       asyncio.run(when_video_pause_play_video(toolbar.find_element(By.ID, "pictPlayerTool-play"), driver))
        
  #       # 動画が終わるまで待機
  #       while mintime.text == maxtime.text:
  #         mintime = toolbar.find_element(By.ID, "pictPlayerTool-duration1")

  #         if mintime.text == maxtime.text:
  #           break
  #       stop_async.when_video_pause_play_video = False
  #       time.sleep(0.5)
  #       stop_async.when_video_pause_play_video = True
        
  #       next_btn = playerpages.find_element(By.ID, "pictPlayerTool-back")
  #       next_btn.click()
        