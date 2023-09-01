import LGS.misc.jsonconfig as jsoncfg
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def request_curseforge(url, mcver, stable_mode=True):
  # データを取得
  config = jsoncfg.read("./jsondata/config.json")
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