import LGS.misc.jsonconfig as jsoncfg
from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def request_modrinth(url, mcver):
  try:
    # データを取得
    config = jsoncfg.read("./jsondata/config.json")
    chromebinary = config["Chrome_binary"]
    driverpath = config["Webdriver"]
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chromebinary
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
        
    # Driver
    driver = webdriver.Chrome(executable_path=driverpath ,options=chrome_options)
    time.sleep(2)
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
  