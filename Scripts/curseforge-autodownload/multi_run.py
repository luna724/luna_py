import LGS.misc.jsonconfig as jsoncfg
import LGS.web_tool.move_chrome as access_url
import os
import json
import subprocess

def multiple_run_main(content_list, api_dict, log_dict, mcver, use_adblock, mode, split_per_process):
  # nプロセスに分割
  content_count = len(content_list)
  try:
    per_file = int(content_count / split_per_process)
  
  except ZeroDivisionError:
    raise ZeroDivisionError(f"URL数または分割数が0です。")
  
  if split_per_process == 2:
    list_1 = content_list[:per_file+1]
    list_2 = content_list[per_file+1:]
    date = {"list_1": list(list_1),
            "list_2": list(list_2),
            "list_1_STATUS": False,
            "list_2_STATUS": False}
  elif split_per_process == 3:
    list_1 = content_list[:per_file+1]
    list_2 = content_list[per_file+1:(per_file*2)+1]
    list_3 = content_list[(per_file*2)+1:]
    date = {"list_1": list(list_1),
            "list_2": list(list_2),
            "list_3": list(list_3),
            "list_1_STATUS": False,
            "list_2_STATUS": False,
            "list_3_STATUS": False}
  elif split_per_process == 4:
    list_1 = content_list[:per_file+1]
    list_2 = content_list[per_file+1:(per_file*2)+1]
    list_3 = content_list[(per_file*2)+1:(per_file*3)+1]
    list_4 = content_list[(per_file*3)+1:]
    date = {"list_1": list(list_1),
            "list_2": list(list_2),
            "list_3": list(list_3),
            "list_4": list(list_4),
            "list_1_STATUS": False,
            "list_2_STATUS": False,
            "list_3_STATUS": False,
            "list_4_STATUS": False}
  elif split_per_process == 5:
    list_1 = content_list[:per_file+1]
    list_2 = content_list[per_file+1:(per_file * 2) + 1]
    list_3 = content_list[(per_file * 2) + 1:(per_file * 3) + 1]
    list_4 = content_list[(per_file * 3) + 1:(per_file * 4) + 1]
    list_5 = content_list[(per_file * 4)+ 1:]
    date = {"list_1": list(list_1),
          "list_2": list(list_2),
          "list_3": list(list_3),
          "list_4": list(list_4),
          "list_5": list(list_5),
          "list_1_STATUS": False,
          "list_2_STATUS": False,
          "list_3_STATUS": False,
          "list_4_STATUS": False,
          "list_5_STATUS": False}
  
  
  # 必要な情報を渡す
  date["MCVER"] = mcver
  date["ADBLOCK"] = use_adblock
  date["API_DICT"] = api_dict
  date["MODE"] = mode
  date["LOG_DICT"] = log_dict
  
  # 書き込みして実行
  if os.path.exists("./data.json"):
    os.remove("./data.json")
  
  jsoncfg.write(date, "./sub/data.json")
  
  # 消す
  for id in range(1, 6):
    if os.path.exists(f"./sub/sub{id}_stdout.json"):
      os.remove(f"./sub/sub{id}_stdout.json")
  
  # 実行
  subprocess.Popen(["./sub/launch.bat"])

  # 修了確認待機
  process_status = True
  while process_status:
    try:
      date = jsoncfg.read("./sub/data.json")
    
    except FileNotFoundError:
      pass
    
    except json.JSONDecodeError:
      pass
      
    if date["list_1_STATUS"] == True and date["list_2_STATUS"] == True and date["list_3_STATUS"] == True and date["list_4_STATUS"] == True and date["list_5_STATUS"] == True:
      process_status = False
      break
      
    else:
      continue
  
  
  # 終わったら読み込み
  output_data1 = jsoncfg.read("./sub/sub1_stdout.json")
  output_data2 = jsoncfg.read("./sub/sub2_stdout.json")
  output_data3 = jsoncfg.read("./sub/sub3_stdout.json")
  output_data4 = jsoncfg.read("./sub/sub4_stdout.json")
  output_data5 = jsoncfg.read("./sub/sub5_stdout.json")
  
  # まとめる
  output_data = output_data1.update(output_data2).update(output_data3).update(
    output_data4).update(output_data5)
  
  # Legacyの処理
  if mode == "Legacy_Curseforge":
    output_data_date = output_data["DATE"]
    output_data_api_dict = output_data["UPDATED_API_DICT"]
    jsoncfg.write(output_data_api_dict, "./jsondata/api_link_cache_legacy_CF.json")
    
    for url in output_data_date.values():
      print("Requesting ", url)
      access_url.forcemove_pyautogui(url, False)
  
  # Modrinthの処理
  elif mode == "Modrinth":
    pass