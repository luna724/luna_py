from v3 import new_main as v3
import LGS.misc.jsonconfig as jsoncfg
import requests
import os


def lencheck(target: list):
  if len(target) != 0:
    return None
  elif len(target) == 0:
    raise ValueError("入力値が正しくありません。\nターゲットは一つ以上指定する必要があります")

def urlcheck(url: str):
  if url.startswith("https://"):
    return False
  else:
    return True
  
def launch_multi(ev, ch, aria, unit, randget, info):
  # 初期化 
  data = {}
  info = False
  
  # イベントリストを取得
  if len(ch) == 1:
    urls = v3.get_event_list(unit, ch[0])
  else:
    urls = []
    for character in ch:
      url = v3.get_event_list(unit, character)
      urls.append(url)
  
  # リクエスト数を計算
  req_count = len(urls)
  print(f"Request Count: {req_count}")
  
  
  # 説明をつける
  if info:
    for x in urls:
      information = ""
      
      data[information] = str(x)
      
  else:
    n = 0
    for x in urls:
      n += 1
      data[str(n)] = str(x)
  
  
  return data

if os.path.exists("./404_list.json"):
  status_404_list = jsoncfg.read("./404_list.json")
else:
  status_404_list = []
  
def status_check(url):
  if url in status_404_list:
    return (404, url)
  
  response = requests.get(url)
  
  if not response.status_code == 200:
    if not response.status_code == 404:
      print(f" Failed. \nStatus Code: {response.status_code}")
      return (999, "")
    #print("Failed.  Reason: 404 Not Found")
    return (404, url)
  #print("Success.  Status: 200 OK")
  return (200, url)

def result_unzipper(result):
  r200 = []
  r404 = []
  
  for x in result:
    if x[0] == 200:
      r200.append(x[1])
    elif x[0] == 404:
      r404.append(x[1])
  
  return r200, r404