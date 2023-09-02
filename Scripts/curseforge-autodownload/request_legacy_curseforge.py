import LGS.misc.jsonconfig as jsoncfg
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time

def request_legacy_curseforge(url, mcver):
  try:
    # データを取得
    config = jsoncfg.read("./jsondata/config.json")
    chromebinary = config["Chrome_binary"]
    driverpath = config["Webdriver"]
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chromebinary
    
    # Driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    wait = WebDriverWait(driver, 30)
    
    # //main[@class='flex-auto root-content z-1 flex flex-col w-full h-full']/div[@class='z-0']/div[@class='mx-auto container pb-5']/section[@class='-mx-2 flex flex-col-reverse lg:flex-row']/div[@class='flex-1 px-2']/div[@class='flex flex-col']/div[@class='mb-4']/section[@class='flex flex-col']/div[@class='listing-container listing-container-table']/div[@class='listing-body']/table[@class='listing listing-project-file project-file-listing b-table b-table-a']/tbody
    # 出てくるまで待機
    Index0_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='listing-body']/table[@class='listing listing-project-file project-file-listing b-table b-table-a']/tbody/tr")))
    
    # もっかい
    Index0_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='listing-body']/table[@class='listing listing-project-file project-file-listing b-table b-table-a']/tbody/tr")))
    
    # それに対していろいろと
    # まず td[1] 要素の .text と href を取得
    target_td_index1 = Index0_element.find_elements(By.XPATH, "//td")[1]
    tti1_a = target_td_index1.find_element(By.XPATH, "//a[@data-action='file-link']")
    
    filename = tti1_a.text
    filelink = tti1_a.get_attribute("href")
    
    print("Getted Filelink: ", filelink)
    
    # https://legacy.curseforge.com/minecraft/mc-mods/surge/files/2916357
    # -> https://legacy.curseforge.com/minecraft/mc-mods/surge/download/2916357/file
    
    api_link = filelink.replace("/files/", "/download/")
    api_link += "/file"
    
    print(f"Filename: {filename}\nApi Link: {api_link}")
    
    # 前提があるなら取得
    driver.get(filelink)
        # 最初の要素が現れるまで待機
    section_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='flex flex-col']/div/section[@class='flex flex-col']")))

    elements = driver.find_elements(By.XPATH, "//h4[text()='Required Dependency']/div[@class='flex flex-wrap -mx-1 w-full']/div/div/div/p[@class='font-bold']/a")
    elements = driver.find_elements(By.XPATH, "//h4[text()='Required Dependency']/div[@class='flex flex-wrap -mx-1 w-full']/div/div/div/p[@class='font-bold']/a")
    
    if len(elements) > 0:
      dependies = []
      for element in elements:
        href_value = element.get_attribute("href")
        print("Found Dependies: ", href_value)
        # 前処理して、追加
        dependies.append(f"https://legacy.curseforge.com{href_value}")
    
      driver.quit()
      return api_link, filename. dependies
    
    driver.quit()
    
    return api_link, filename
    
  except TimeoutException:
    driver.quit()
    pass
  
def legacy_cf_download(url, download_path):
    # データを取得
  config = jsoncfg.read("./jsondata/config.json")
  chromebinary = config["Chrome_binary"]
  driverpath = config["Webdriver"]
  
  chrome_options = Options()
  chrome_options.binary_location = chromebinary
  chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": False
  })

  driver = webdriver.Chrome(chrome_options=chrome_options)
  
  
  # セキュリティ設定ページにアクセス
  driver.get("chrome://settings/security")
  wait = WebDriverWait(driver, 30)
  # XPATHを使用して要素をクリック
  # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[5]/settings-privacy-page//settings-animated-pages/settings-subpage[3]/settings-security-page//div[1]/settings-radio-group/settings-collapse-radio-button[3]//div/div[1]/div[1]"))).click()  
  time.sleep(2)
  driver.get(url)
  
  
  time.sleep(5)
  driver.quit()
  return None