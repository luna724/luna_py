import LGS.misc.jsonconfig as jsoncfg
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    
    return api_link, filename
    
  except TimeoutException:
    pass