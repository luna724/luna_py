import requests
from selenium import webdriver

def webdriver(url, binary_location="E:\\Application\\Google\\Chrome\\Application\\chrome.exe"):
    # WebDriverの起動
  chrome_options = webdriver.ChromeOptions()
  chrome_options.binary_location = binary_location
  
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(url)
  
  return driver.page_source

def request(url):
  response = requests.get(url)
  return response.text