import LGS.misc.jsonconfig as jsoncfg
import random
import time

id = "2"

# それが有効か確認
date = jsoncfg.read("./data.json")

if not f"list_{id}_STATUS" in date:
  date[f"list_{id}_STATUS"] = True
  output_date = {"DATE": {},
                "UPDATED_API_DICT": {}}
  jsoncfg.write(output_date, f"./sub{id}_stdout.json")
  time.sleep((random.randrange(1, 10) * random.randrange(1, 10)) / 50)
  
  jsoncfg.write(date, "./data.json")

import sys
import tqdm
from request_legacy_curseforge import request_legacy_curseforge
sys.path.append("..\\")

MODE = date["MODE"]
mcver = date["MCVER"]

if MODE == "Legacy_Curseforge":
  # データの取得
  curseforge_preurl = date[f"list_{id}"]
  use_adblock = date["ADBLOCK"]
  legacy_api_dict = date["API_DICT"]
  legacy_LOG_dict = date["LOG_DICT_LEGACY"]
  mcver_format_dict = jsoncfg.read("..\\./jsondata/mcver_legacy_formatted.json")
  download_from_api_cf = {}
  
  for content in tqdm(curseforge_preurl, desc=f"Curseforge API Request Processing.. (In Process {id})"):
    if content in legacy_api_dict.keys():
      try:
        api_url = legacy_api_dict[content][0]
        filename = legacy_api_dict[content][1]
        download_from_api_cf[filename] = api_url
      except IndexError:
        print(f"in File: {content}\n in Cache Getting: IndexError")
        raise IndexError("Please Reset \"Legacy_curseforge_apilink cache.json\"")
        
    else:      
      api_url, filename, dependies = request_legacy_curseforge(url=content, mcver=mcver, adb=use_adblock)
      if api_url == None and filename == None and dependies == None:
        continue
      
      try:
        download_from_api_cf[filename] = api_url
        legacy_api_dict[content] = [api_url, filename]
      
      except TypeError:
        print(f"保存に失敗しました。: {content}")
        pass


      if not dependies == None:
        legacy_LOG_dict[content] = []
        for contents in tqdm(dependies, desc="Installing Dependies"):
          mcver_formatted = mcver_format_dict[mcver]
          contents += f"/files/all?filter-game-version={mcver_formatted}"
          try:
            api_url2, filename2, dependies2 = request_legacy_curseforge(contents, mcver, use_adblock)
            download_from_api_cf[filename2] = api_url2
          except TypeError:
            print(f"Failed: {contents}")
          
          if api_url2 == None and filename2 == None:
            continue
          
          if not dependies2 == None:
            for contents2 in tqdm(dependies2, desc="Installing Dependies"):
              mcver_formatted = mcver_format_dict[mcver]
              contents2 += f"/files/all?filter-game-version={mcver_formatted}"
              api_url23, filename23, _ = request_legacy_curseforge(contents, mcver, use_adblock)
              
              if api_url23 == None and filename23 == None:
                continue
              
              download_from_api_cf[filename23] = api_url23
              # 前提の前提
              legacy_LOG_dict[content].append(api_url23)
              
          else:
            # 前提の前提がないなら
            legacy_LOG_dict[content].append(api_url2)
            
        # 最後にメインファイルを入れる
        legacy_LOG_dict[content].append(api_url)
        
      else:
        # 前提がないなら
        legacy_LOG_dict[content] = [api_url]
  # データを渡す
  output_date = {"DATE": download_from_api_cf,
                "UPDATED_API_DICT": legacy_api_dict}
  
  jsoncfg.write(output_date, f"./sub{id}_stdout.json")
  date[f"list_{id}_STATUS"] = True
  jsoncfg.write(date, "./data.json")