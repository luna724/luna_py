import LGS.misc.jsonconfig as jsoncfg
import LGS.misc.random_roll as roll
from selenium import webdriver
import random
import os
import pyautogui_mode
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == "__main__":
    # データを取得
  config = jsoncfg.read("./jsondata/config.json")
  chromebinary = config["Chrome_binary"]

  chrome_options = webdriver.ChromeOptions()
  chrome_options.binary_location = chromebinary

  # Driver
  driver = webdriver.Chrome(options=chrome_options)
  INFOMATION = {}
  
  for page_num in range(1, 101):
    url = f"https://www.curseforge.com/minecraft/search?class=mc-mods&gameFlavorsIds=1&gameVersion=1.16.5&page={page_num}&pageSize=50&sortType=2"
    driver.get(url)
    wait = WebDriverWait(driver, 60)

    # 指定されたXPATHで要素を待機して検索
    # results_container = wait.until(EC.presence_of_element_located((By.XPATH, "]")))
    project_cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='container search-page']/div[@class='results-container']/div[@class=' project-card']")))

    # 情報を格納する辞書
    

    # 各プロジェクトカードに対して処理を実行
    for card in project_cards:
        name_element = card.find_element(By.XPATH, ".//a[@class='name']/span[@class='ellipsis']")
        project_name = name_element.text
        
        link_element = card.find_element(By.XPATH, ".//a[@class='name']")
        project_link = link_element.get_attribute("href")
        
        INFOMATION[project_name] = project_link

    # 結果を表示
    print("取得した情報:", INFOMATION)
    
  jsoncfg.write(INFOMATION, "./jsondata/modlist_1.16.5-5000.json")

  # ブラウザを閉じる
  driver.quit()


def choice_(mcver, target_count, rd_chance, mod_count, database):
  if mcver == "1.12.2" and database == "5000MOD":
    data = jsoncfg.read("./jsondata/modlist_1.12.2-5000.json")
  elif mcver == "1.12.2" and database == "500MOD":
    data = jsoncfg.read("./jsondata/modlist_1.12.2-500.json")
  elif mcver == "1.16.5" and database == "5000MOD":
    data = jsoncfg.read("./jsondata/modlist_1.16.5-5000.json")
  elif mcver == "1.16.5" and database == "500MOD":
    data = jsoncfg.read("./jsondata/modlist_1.16.5-500.json")
  elif mcver == "1.16.5" and database == "10000MOD (1.16.5のみ)":
    data = jsoncfg.read("./jsondata/modlist_1.16.5-10000.json")
  elif mcver == "1.12.2" and database == "10000MOD (1.16.5のみ)":
    print("database: 10000MOD is Not available on 1.12.2.\n Loaded From 5000MOD..")
    data = jsoncfg.read("./jsondata/modlist_1.12.2-5000.json")
    
  else:
    return "Error. 設定は未実装です" 
  
  mod_count -= 1
  # 辞書のシャッフル
  items = list(data.items())
  random.shuffle(items)

  # シャッフルされたキーと値のペアに基づいて新しい辞書を作成
  shuffled_data = {key: value for key, value in items}
  
  # Target countの数まで減らす
  if len(shuffled_data) > target_count:
    while len(shuffled_data) > target_count:
      key_to_remove = random.choice(list(shuffled_data.keys()))
      del shuffled_data[key_to_remove]
      
    copy_target_key = []
    while len(copy_target_key) <= mod_count:
      for content in shuffled_data.keys():
        if roll.random_roll((rd_chance / 100)):
          copy_target_key.append(content)
        if len(copy_target_key) >= mod_count:
          break
  else:
    print(f"stderr: Shuffled data is low from target_count ({len(shuffled_data)} / {target_count})")
    copy_target_key = shuffled_data

  # 抽選結果に基づいた値を取得
  url_list = []
  for content in copy_target_key:
    url_list.append(data[content])
  
  # url_write_here.txt に書き込み、pyautogui_mode.pyで取得
  if os.path.exists("./url_write_here.txt"):
    os.remove("./url_write_here.txt")
    
  for content in url_list:
    with open("./url_write_here.txt", "a") as f:
        f.write(f"{content}\n")
  
  # 読みやすくする
  sess = 0
  markdown = "| MOD リスト | | | | |\n| --- | --- | --- | --- | --- |\n"
  for content in copy_target_key:
    sess += 1
    markdown += f"| {content} "
    
    if sess == 5:
      markdown += "|\n"
      sess = 0
  
  
  return markdown