import LGS.web_tool.google as ls
import LGS.misc.jsonconfig as jsoncfg
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import random
from tqdm import tqdm
import requests
import time
import os 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def skip_cloudflare():
  # ランダムで待ってクリック
  # ((1 / 1)^(1/1.2))
  time.sleep((random.randrange(1000, 3000) / 1000) ** (random.randrange(1000, 2000) / random.randrange(800, 1200)))

def url_split(data):
  mr = []
  cf = []
  for content in data:
    if content.startswith("https://www.curseforge.com/minecraft/mc-mods/"):
      cf.append(content)
    elif content.startswith("https://modrinth.com/"):
      mr.append(content)
    
  return cf, mr

def request_curseforge(url, mcver, stable_mode=True):
  # データを取得
  config = jsoncfg.read("./config.json")
  chromebinary = config["Chrome_binary"]
  driverpath = config["Webdriver"]
  
  chrome_options = webdriver.ChromeOptions()
  chrome_options.binary_location = chromebinary
  
  # Driver
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(url)
  if stable_mode:
    wait = WebDriverWait(driver, 60)
  else:
    wait = WebDriverWait(driver, 60)
  
  time.sleep(5)
  
  try:
    # 特定のXPATHの要素を検索
    elements = driver.find_elements(By.XPATH, "//body[@class='no-js']/div[@class='main_wrapper']/div[@class='main-content']/h1[@class='zone-name-title h1']")
    
    if len(elements) > 0:
        print("Trying Skip Cloudflare")
        skip_cloudflare()
    else:
        pass
  except NoSuchElementException:
    pass
      
  if stable_mode:
    # files-table-container columns の値の取得
    ftccnum = 4
    wh = True
    while wh == True:
      ftccnum += 1
      print(f"ftccnum: {ftccnum}")
      try:
        modname_element = wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='container project-page']/section[@class='tab-content']/div[@class=' files-table-container columns-{ftccnum}']/div[@class='files-table']/div[@class='file-row']")))
        wh = False  
        
      except TimeoutException:
        a = 0
      
      if ftccnum > 12:
        wh = False
        mcver = "Failed"
      
    
    modname_element = wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='container project-page']/section[@class='tab-content']/div[@class=' files-table-container columns-{ftccnum}']/div[@class='files-table']/div[@class='file-row']")))
    filterver_element = wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='container project-page']/section[@class='tab-content']/div[@class=' filters']/div[@class=' select-dropdown']/div[@class=' dropdown']/p[@class='dropdown-selected-item']/span")))

    print("Page Filtered MCVer: ", filterver_element.text)
    print("Filtered MCVer: ", mcver)
    # バージョンとURLのバージョンが一致しているかチェック
    if not mcver == filterver_element.text:
      print("Traceback: VersionNotFoundError\nURLとサイトのMinecraft Versionが一致しません")
      return "Failed-lunaErr404", ""

    # クリック
    modname_element = wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='container project-page']/section[@class='tab-content']/div[@class=' files-table-container columns-{ftccnum}']/div[@class='files-table']/div[@class='file-row']")))
    
    # Cookie警告は死ね
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='cookiebar']/div[@class='cookiebar-content']/div[@id='cookiebar-ok']"))).click()
    
    # Index0 をクリック
    modname_element = wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='container project-page']/section[@class='tab-content']/div[@class=' files-table-container columns-{ftccnum}']/div[@class='files-table']/div[@class='file-row']")))
    page_source = driver.page_source
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='container project-page']/section[@class='tab-content']/div[@class=' files-table-container columns-{ftccnum}']/div[@class='files-table']/div[@class='file-row']"))).click()
    
    # ダウンロードをクリック
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='container project-page']/section[@class='tab-content']/section[@class='file-details']/h2/div[@class='actions']/div[@class=' split-button more-options-gap']/button[@class='btn-cta download-cta']"))).click()
    
    # ダウンロードリンクを取得
    dllink_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='client-marketing']/div[@class='timer small']/p/a")))
    
    dllink_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='client-marketing']/div[@class='timer small']/p/a")))
    
    # 要素のhref属性を取得
    link_url = dllink_element.get_attribute("href")

  else:
    modname_element = wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='files-table']/div[@class='file-row']")))
    filterver_element = wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='container project-page']/section[@class='tab-content']/div[@class=' filters']/div[@class=' select-dropdown']/div[@class=' dropdown']/p[@class='dropdown-selected-item']/span")))

    print("Page Filtered MCVer: ", filterver_element.text)
    print("Filtered MCVer: ", mcver)
    # バージョンとURLのバージョンが一致しているかチェック
    if not mcver == filterver_element.text:
      print("Traceback: VersionNotFoundError\nURLとサイトのMinecraft Versionが一致しません")
      return "Failed-lunaErr404", ""

    # クリック
    modname_element = wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='files-table']/div[@class='file-row']")))
    
    # Cookie警告は死ね
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='cookiebar']/div[@class='cookiebar-content']/div[@id='cookiebar-ok']"))).click()
    
    # Index0 をクリック
    modname_element = wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='files-table']/div[@class='file-row']")))
    page_source = driver.page_source
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='files-table']/div[@class='file-row']"))).click()
    
    # ダウンロードをクリック
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='container project-page']/section[@class='tab-content']/section[@class='file-details']/h2/div[@class='actions']/div[@class=' split-button more-options-gap']/button[@class='btn-cta download-cta']"))).click()
    
    # ダウンロードリンクを取得
    dllink_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='client-marketing']/div[@class='timer small']/p/a")))
    
    dllink_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='client-marketing']/div[@class='timer small']/p/a")))
    
    # 要素のhref属性を取得
    link_url = dllink_element.get_attribute("href")

  
  # 取得したURLを表示
  print("api link: ", link_url)
  
  soup = BeautifulSoup(page_source, "html.parser")
  
  span_name = soup.find_all("span", class_="name")
  print("NAME: ", span_name[0].text)
  
  driver.quit()
  
  return link_url, span_name[0].text

def request_modrinth(url, mcver):
  try:
    # データを取得
    config = jsoncfg.read("./config.json")
    chromebinary = config["Chrome_binary"]
    driverpath = config["Webdriver"]
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chromebinary
    
    # Driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    wait = WebDriverWait(driver, 30)
    
    # ダウンロードできるかどうか
    dllink_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='content']/div[@class='universal-card all-versions']/div[@class='version-button button-transparent']/a[@class='download-button square-button brand-button release v-popper--has-tooltip']")))  
    dllink_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='content']/div[@class='universal-card all-versions']/div[@class='version-button button-transparent']/a[@class='download-button square-button brand-button release v-popper--has-tooltip']")))
    api_link = dllink_element.get_attribute("href")
    
      # データの取得# Index0 をクリック
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='content']/div[@class='universal-card all-versions']/div[@class='version-button button-transparent']/a[@class='version__title']"))).click()
    
    # ファイル名を取得
    modname_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='version-page__files universal-card']/div[@class='file primary']/span[@class='filename']/strong")))
    
    modname_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='version-page__files universal-card']/div[@class='file primary']/span[@class='filename']/strong")))
    
    filename = modname_element.text
    
    print("api link: ", api_link)
    print("NAME: ", filename)
    
    # 前提MODがあるなら取得
    elements = driver.find_elements(By.XPATH, "//div[@class='version-page__dependencies universal-card']/div[@class='dependency button-transparent']/a[@class='info']")
    elements = driver.find_elements(By.XPATH, "//div[@class='version-page__dependencies universal-card']/div[@class='dependency button-transparent']/a[@class='info']")

    if len(elements) > 0:
      dependies = []
      for element in elements:
        href_value = element.get_attribute("href")
        print("Found Dependies: ", href_value)
        dependies.append(href_value)
        
      driver.quit()
      return api_link, filename, dependies
    

  
  except TimeoutException:
    driver.quit()
    print("Not found Matching Version")
    return None, None, None
  
  driver.quit()
  return api_link, filename, None
  

def main(data_filepath, mcver, modname_search=False, search_mode="curseforge.com", stable_mode=True,
        output_path="./out"):
  if modname_search:
    with open(data_filepath, "r") as f:
      pre_data = f.readlines()
    
    # URLではない場合の前処理
    search = []
    data = []
    for content in pre_data:
      content = content.strip()
      if content.startswith("https://"):
        data.append(content)
        continue
      search.append(content)
    
    # 検索
    for content in tqdm(search, desc="Mod URL Searching.."):
      # まずは結果を受け取る
      content_url = ls.simple_search(f"{content} {mcver} {search_mode}")
      print(f"{content} -> {content_url}")
      
      # チェックして追加
      if content_url.startswith("https://www.curseforge.com/minecraft/mc-mods/"):
        data.append(content_url)
      elif content_url.startswith("https://modrinth.com"):
        data.append(content_url)  
      
      else:
        print(f"Error: {content}\nCan't Find Curseforge / Modrinth Site. (Return: {content_url})")
      
  else:
    with open(data_filepath, "r") as f:
      pre_data = f.readlines()
    
    # 前処理
    data = []
    for content in pre_data:
      if content.startswith("https://"):
        data.append(content)
    
  # 分ける
  curseforge, modrinth = url_split(data)
  
  # 0なら停止
  if len(curseforge) < 1 and len(modrinth) < 1:
    print("Minecraft MOD URL Not Found.")
    return " # ERROR "

  # Curseforgeのほうを実行
  if not len(curseforge) < 1:
    curseforge_preurl = []
    for content in tqdm(curseforge, desc="Curseforge Preprocessing.."):
      content += f"/files?version={mcver}"
      curseforge_preurl.append(content)
      time.sleep(0.01)
      
    print("Starting Curseforge Download..")
    download_from_api_cf = {}
    for content in tqdm(curseforge_preurl, desc="Curseforge API Request Processing.."):
      api_url, filename = request_curseforge(url=content, mcver=mcver, stable_mode=stable_mode)
      download_from_api_cf[filename] = api_url
    
    print("Download Data Dict: ", download_from_api_cf)
    if os.path.exists("./api_link_cache_curseforge.json"):
      previous_cache = jsoncfg.read("./api_link_cache_curseforge.json")
      previous_cache.update(download_from_api_cf)
      save_d = previous_cache
    else:
      save_d = download_from_api_cf
    
    jsoncfg.write(save_d, "./api_link_cache_curseforge.json")
    
    # ダウンロード
    for filename, url in download_from_api_cf.items():
      print(f"Requesting {url}")
      response = requests.get(url)
      
      # Status code
      if not response.status_code == 200:
        print(f"Can't Get Response Status Code: {response.status_code}")
      
      # ファイル名に基づいて保存
      os.makedirs(output_path, exist_ok=True)
      output_paths = os.path.join(output_path, filename)
      with open(output_paths, "wb") as f:
        f.write(response.content)
      print(f"Saving File.. {output_paths}")
    
  # Modrinth
  if not len(modrinth) < 1:
    modrinth_preurl = []
    for content in tqdm(modrinth, desc="Modrinth Preprocessing.."):
      if content.count("/version/") > 0:
        content = content.split("/version/")[0]
      content += f"/versions?g={mcver}"
      modrinth_preurl.append(content)
      time.sleep(0.01)
    
    print("Starting Modrinth Download..")
    print("WARNING: Modrinth Download is Not Supported Version Check")
    download_from_api_mr = {}
    for content in tqdm(modrinth_preurl, desc="Modrinth Download Processing.."):
      api_url, filename, dependies_list = request_modrinth(content, mcver)
      # NoneならSkip
      if api_url == None and filename == None and dependies_list == None:
        continue
      
      download_from_api_mr[filename] = api_url
      
      if not dependies_list == None:
        for contents in tqdm(dependies_list, desc="Installing Dependies"):
          contents += f"/versions?g={mcver}"
          api_url2, filename2, _ = request_modrinth(contents, mcver)

          if api_url2 == None and filename2 == None:
            continue
            
          download_from_api_mr[filename2] = api_url2
          
      

      
    print("Download Data Dict (Modrinth): ", download_from_api_mr)
    if os.path.exists("./api_link_cache_modrinth.json"):
      previous_cache = jsoncfg.read("./api_link_cache_modrinth.json")
      previous_cache.update(download_from_api_mr)
      save_d = previous_cache
    else:
      save_d = download_from_api_mr
    
    jsoncfg.write(save_d, "./api_link_cache_modrinth.json")
    
    # ダウンロード
    for filename, url in download_from_api_mr.items():
      print(f"Requesting {url}")
      response = requests.get(url)
      
      # Status code
      if not response.status_code == 200:
        print(f"Can't Get Response Status Code: {response.status_code}")
      
      # ファイル名に基づいて保存
      os.makedirs(output_path, exist_ok=True)
      output_paths = os.path.join(output_path, filename)
      with open(output_paths, "wb") as f:
        f.write(response.content)
      print(f"Saving File.. {output_paths}")
      
      
if __name__ == "__main__":
  main("./url_write_here.txt", "1.12.2", True)
  