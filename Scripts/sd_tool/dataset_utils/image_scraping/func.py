from tkinter import Tk, filedialog
from typing import Tuple, Literal, List
from PIL import Image
from bs4 import BeautifulSoup
from io import BytesIO
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from LGS.misc.nomore_oserror import file_extension_filter
import LGS.misc.jsonconfig as jsoncfg
import gradio as gr
import requests
import os

def browse_file():
  root = Tk()
  root.attributes("-topmost", True)
  root.withdraw()
  
  filenames = filedialog.askopenfile()
  if len(filenames) > 0:
      root.destroy()
      return str(filenames)
  else:
      filename = "ディレクトリを指定してください。"
      root.destroy()
      return str(filename)


def whenModeChanged(mode) -> Tuple[dict, dict, dict]:
  see = gr.update(visible=True)
  hide = gr.update(visible=False)
  
  if mode == 0:
    return hide, see, hide
  elif mode == 1:
    return see, hide, hide
  elif mode == 2:
    return hide, hide, see
  else:
    raise RuntimeError(f"mode: {mode}")


class CooldownManager:
  from random import randrange as rand
  import time
  
  def __init__(self, manual_cooldown=None):
    self.manual = False
    if manual_cooldown == None:
      self.cd = (self.rand(1, 500) / 100)
    else:
      self.manual = True
      self.cd = manual_cooldown
    
  def __call__(self, event:Literal[
    "Searching"
  ]):
    multiplier = {
      "Searching": 1.125
    }
    
    additive = {
      "Searching": 3
    }
    
    cd = (self.cd * multiplier[event]) + additive[event]
    print(f"Waiting {cd}seconds..", end="")
    self.time.sleep(cd)

def get_fn(base, target_dir, ext) -> str:
  fcount = file_extension_filter(
    os.listdir(target_dir), [".png", ".jpg", ".jpeg"]
  )
  for i in range(500):
    fn = f"{i:05}" 
    full_fn = f"{fn}-{base}.{ext}"
    if os.path.exists(
      os.path.join(target_dir, full_fn)
    ):
      continue
    else:
      break
  
  return full_fn
  

def save(data:List[Tuple[requests.Response, str, str]], fp:Tuple[str, str, Literal["png", "jpg", "keep"]], bn:str=None, return_list:bool=False) -> List[Tuple[requests.Response, str, str]]|None:
  """
  fp: Tuple[dir, fn, exts]
  bn: basename. for resize mode
  return_lists: return lists, after saved (saved data will be deleted.)"""
  if fp[2] == "keep":
    fp[2] = "jpg"
    if bn is not None:
      fp[2] = os.path.splitext(bn)[1].strip(".")
  os.makedirs(fp[0], exist_ok=True)
  dirs, fn, exts = fp
  FORMAT = exts.upper()
  if FORMAT == "JPG":
    FORMAT = "JPEG"
  
  copied_data = data
  for (content, info, url) in data:
    try:
      img_bytes = content.content
      image = Image.open(
        BytesIO(img_bytes)
      )
      infotxt = f"""
      Image info:
      retrieval from {url} 
      title: {info}
      
      retrieval time: {datetime.now().strftime("%Y%m%d%H%M%s")}
      """
      name = get_fn(fn, dirs, exts)
      fp = os.path.join(dirs, name)
      
      image.save(
        fp, FORMAT)
      with open(fp+".info", "w", encofing="utf8") as f:
        f.write(infotxt)
    except Exception as e:
      print(f"Unknown Exception in image saving.\nError: {e}\nSaving current list..")
      jsoncfg.write(
        {"tmp": data}
      )
      continue
    copied_data.remove((content, info, url))
  
  if return_list:
    return copied_data


def run(
  mode:int, search_text:str, img:Image.Image, resize:str,
  dir:str, fn:str|None, exts:Literal["png", "jpg", "keep"],
  manual_cd:int|None, safemode:bool, isAPI:bool=False
) -> Tuple[Image.Image, str] | None:
  """ main function """
  print("Tips: AIイラストを使用してGoogleレンズモードを使用することはお勧めしません。")
  if mode in [0, 1]:
    cooldown = CooldownManager(manual_cd)
    url = "https://www.google.com/imghp?hl=ja&authuser=0&ogbl"
    
    # Google method  
    options = Options()
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    wait = WebDriverWait(driver, 120)
    
    # 分岐
    if mode == 1:
      # テキストモード
      textbox = wait.until(
        EC.presence_of_element_located((By.ID, "APjFqb"))
      )
      textbox.send_keys(
        search_text
      )
      searcher_root = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[1]/div[3]/form/div[1]/div[1]/div[1]/button/div/span/svg"))
      ).click()
      # svg_clickable = WebDriverWait(searcher_root, 10).until(
      #   EC.element_to_be_clickable((By.XPATH, "//svg"))#.find_element(
      #   #By.XPATH, "//svg"
      # #).click()
      # #span/svg
      # ).click()
      
      cooldown("Searching")
      
      # 検索終了まで待機
      wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "YmvwI"))
      )
      image_root = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "wIjY0d"))
      )
      
      image_elements = image_root.find_elements(
        By.CLASS_NAME, "eA0Zlc"
      )
      
      imgs:List[Tuple[requests.Response, str, str]] = []
      repeating = 0
      for elem in image_elements:
        repeating += 1
        html = elem.get_attribute("outerHTML")
        soup = BeautifulSoup(soup, "html.parser")
        href_holder = soup.find(
          "div", class_="czzyk XOEbc"
        ).find(
          "h3", class_="ob5Hkd"
        ).find(
          "a"
        )
        image_holder = href_holder.find("div").find("div").find("div").find(
          "g-img", class_="mNsIhb"
        ).find(
          "img"
        )
        
        imgsrc = image_holder.get("src")
        imginfo = image_holder.get("alt")
        siteurl = href_holder.get("href")
        
        # 画像を取得
        content = requests.get(
          imgsrc
        )
        imgs.append(
          # (content, name, siteurl)
          content, imginfo, siteurl
        )
        
        if safemode:
          imgs = save(imgs, (dir, fn, exts), return_list=True)
        
        if repeating >= 200:
          break
        
      save(imgs, (dir, fn, exts))
    elif mode == 0:
      # Googleレンズモード
      raise RuntimeError("Googleレンズモードは現在サポートされていません。")
    
    driver.close()
  else:
    # mode == 2
    # フォルダの再パターン化
    target = resize
    
    if not os.path.exists(target):
      raise RuntimeError("対象パスが存在しません。")
    
    for f in file_extension_filter(os.listdir(target), [".png", ".jpg", ".jpeg", ".raw"]):
      bfn, ext = os.path.splitext(f)
      if not ext == exts and not exts == "keep":
        # 拡張子の変更
        ext = exts
      ext = "."+ext
      
      
      