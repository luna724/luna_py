import LGS.web_tool.google as ls
import LGS.misc.jsonconfig as jsoncfg
import LGS.web_tool.move_chrome as access_url
from tqdm import tqdm
import requests
import time
import os
from request_curseforge import request_curseforge
from request_modrinth import request_modrinth
from request_legacy_curseforge import request_legacy_curseforge
from request_legacy_curseforge import legacy_cf_download

def url_split(data, legacy_split=False):
  mr = []
  cf = []
  lcf = []
  for content in data:
    if legacy_split:
      if content.startswith("https://legacy.curseforge.com/minecraft/mc-mods/"):
        lcf.append(content)
    if content.startswith("https://www.curseforge.com/minecraft/mc-mods/"):
      cf.append(content)
    elif content.startswith("https://modrinth.com/"):
      mr.append(content)
  
  if legacy_split:
    return cf, mr, lcf
  
  return cf, mr


def main(data_filepath, mcver, modname_search=False, search_mode="curseforge.com", stable_mode=True,
        output_path="./out", use_legacy_url=False, use_multi_mode=False,
        use_adblock=False):
  # データの取得
  mcver_format_dict = jsoncfg.read("./jsondata/mcver_legacy_formatted.json")
  legacy_api_dict = jsoncfg.read("./jsondata/legacy_curseforge_apilink_cache.json")
  config = jsoncfg.read("./jsondata/config.json")
  chromebinary = config["Chrome_binary"]
  
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
      content_url = ls.simple_search(f"{content} {mcver} {search_mode}", chromebinary)
      print(f"{content} -> {content_url}")
      
      # チェックして追加
      if content_url.startswith("https://www.curseforge.com/minecraft/mc-mods/"):
        if content_url.count("/files/") > 0:
          content_url = content_url.split("/files/")[0]
          print(f" -> {content_url}")
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
  if use_legacy_url:
    curseforge, modrinth, _ = url_split(data, True)
  else:
    curseforge, modrinth = url_split(data)
  
  # 0なら停止
  if len(curseforge) < 1 and len(modrinth) < 1:
    raise ValueError("Minecraft MOD URL Not Found.")

  # Curseforgeのほうを実行
  if not len(curseforge) < 1:
    curseforge_preurl = []
    for content in tqdm(curseforge, desc="Curseforge Preprocessing.."):
      if use_legacy_url:
        print("Legacy Mode: Content: ", content, " ->")
        if not mcver in mcver_format_dict.keys():
          print(f"Traceback: ValueError \nLegacy Site Not Supported This MCver: {mcver}")
          raise ValueError(f"Legacy Site Not Supported This MCver: {mcver}")
        mcver_formatted = mcver_format_dict[mcver]
        content = content.replace("https://www.curseforge.com", "https://legacy.curseforge.com")
        content += f"/files/all?filter-game-version={mcver_formatted}"
        curseforge_preurl.append(content)
        print(content)
      else:
        content += f"/files?version={mcver}"
        curseforge_preurl.append(content)
      time.sleep(0.01)
      
    print("Starting Curseforge Download..")
    download_from_api_cf = {}
    for content in tqdm(curseforge_preurl, desc="Curseforge API Request Processing.."):
      if use_legacy_url:
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
          
          download_from_api_cf[filename] = api_url
          legacy_api_dict[content] = [api_url, filename]

          if not dependies == None:
            for contents in tqdm(dependies, desc="Installing Dependies"):
              mcver_formatted = mcver_format_dict[mcver]
              contents += f"/files/all?filter-game-version={mcver_formatted}"
              api_url2, filename2, _ = request_legacy_curseforge(contents, mcver, use_adblock)
              
              if api_url2 == None and filename2 == None:
                continue
              
              download_from_api_cf[filename2] = api_url2
              
        #legacy_cf_download(url=api_url, download_path=output_path)
          
      else:
        api_url, filename = request_curseforge(url=content, mcver=mcver, stable_mode=stable_mode)
        download_from_api_cf[filename] = api_url
    
    # ダウンロード
    for filename, url in download_from_api_cf.items():
      print(f"Requesting {url}")
      if use_legacy_url:
        access_url.forcemove_pyautogui(url)
        
      else:  
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
  