from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
from bs4 import BeautifulSoup
import time
### 動作確認バージョン
# Google Chrome 114.0.5735.199（Official Build）windows10 - amd64bit
# Selenium 3.14.1
# Google Engine 2023/08/26 15:11 www.google.com ja-jp

def simple_search(search_text="Wikipedia", chromebinary_v114_location="E:\\Application\\Google\\Chrome\\Application\\chrome.exe"):
  # # WebDriverを起動
  # chrome_options = webdriver.ChromeOptions()
  # chrome_options.binary_location = "E:\\Application\\Google\\Chrome\\Application\\chrome.exe"  # もし指定する場合
  
  # driver = webdriver.Chrome(options=chrome_options)

  # # Googleにアクセス
  # driver.get("https://www.google.com")

  # # 検索ボックスの要素を取得
  # search_box = driver.find_element("class name", "gLFyf")

  # ペーストするテキスト
  # pyperclip.copy(search_text)

  # # テキストをペースト
  # search_box.send_keys(Keys.CONTROL + "v")

  # # ペースト後、Enterキーを押して検索
  # search_box.send_keys(Keys.RETURN)

  # 少し待機
  # time.sleep(3)
  
  
  
  # 結果を取得
  # cite_elements = driver.find_elements("css selector", "cite")
  
  # # 最初の<cite>要素のテキストを表示
  # if cite_elements:
  #   first_cite_text = cite_elements[0].text
  #   first_cite_text = first_cite_text.split(" ›")[0]
  #   if not first_cite_text.startswith("http"):
  #     raise ValueError(f"<cite> の帰り値がURLでありません。 ({first_cite_text})")
    
  
  # else:
  #   raise ValueError("<cite> の値を取得できませんでした。")
    
  # WebDriverを終了
  # driver.quit()

  # まず探す
  chrome_options = webdriver.ChromeOptions()
  chrome_options.binary_location = chromebinary_v114_location
  
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(f"https://www.google.com/search?q={search_text}")

  # ページのHTMLを取得してBeautifulSoupで解析
  page_source = driver.page_source
  soup = BeautifulSoup(page_source, 'html.parser')

  # 特定の要素を取得する（例：classが "yuRUbf" の最初の <a> 要素）
  c_elements = soup.find_all(class_='yuRUbf')
  if c_elements:
      first_c_element = c_elements[0]  # 最初の <a> 要素を取得
      target_a_element = first_c_element.find("a")
      href = target_a_element.get('href')  # href 属性を取得
      print(href)
  else:
      print("No <a> elements with class 'yuRUbf' found.")

  # ドライバーを閉じる
  driver.quit()
  
  return href