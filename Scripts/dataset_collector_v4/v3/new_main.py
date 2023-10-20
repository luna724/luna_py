"""

いベストからのキャラIDに基づいた取得
https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_01_{:02d}_rip/voice_ev_{unit_type}_01_{}_{:02d}_" + f"{id}.mp3

バーチャルライブからのIDに基づいた取得
https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_bd_2023ichika_1_rip/voice_mc_bd_2023ichika_04_01.mp3

スペシャルストーリーからのIDに基づいた取得
https://storage.sekai.best/sekai-assets/sound/scenario/voice/connect_live_01_band_rip/connectlive_band_beforestory_01_03_01.mp3

キャラストーリーからの取得
https://storage.sekai.best/sekai-assets/sound/scenario/voice/self_ichika_rip/voice_selfep_band_03_01.mp3

サイドストーリーからの取得 (ID)
https://storage.sekai.best/sekai-assets/sound/card_scenario/voice/001001_ichika01_rip/voice_card_01_01a_07_02.mp3
https://storage.sekai.best/sekai-assets/sound/card_scenario/voice/001026_ichika01_rip/voice_card_bd_202308_01_4a_02_01.mp3


"""

import LGS.misc.compact_input as cin
import LGS.misc.output_folder as fos
import requests
import LGS.misc.jsonconfig as jsoncfg
import json
import subprocess
import os
import hashlib
import random
import LGS.misc.nomore_oserror as los
import time

#> request.py
# リクエストを行う
def save_data(url, save_directory, wait_time):
  response = requests.get(url)
  
  # ステータスコードの確認
  if not response.status_code == 200:
    if not response.status_code == 404:
      print(f"Failed: {url}\n  Response Code: {response.status_code}")
    return False
  
  # セーブ
  encoded_url = url.encode("utf-8")
  hashed_url = hashlib.sha1(encoded_url).hexdigest()
  id = random.randrange(0, 999999999)
  save_name = los.filename_resizer(f"{id}_{hashed_url}_{url}.mp3", replaceTo="_")
  
  with open("success_urls.txt", "w") as file:
        file.write("\n".join(url))
        
  with open(os.path.join(save_directory, save_name), "wb") as f:
    f.write(response.content)
  
  time.sleep(wait_time)
  
  return True
  
  
      

#> pattern.py
# 全パターンのURLを返す
def get_event_list(unit, target_id):
  story_id = 1
  talking_id = 1
  date_list = []
  target_id = int(target_id)
  
  if unit == "Leo/need":
    url_dict = [
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_01_{:02d}_rip/voice_ev_band_01_{}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_10_{:02d}_rip/voice_ev_band_02_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_13_{:02d}_rip/voice_ev_shuffle_04_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_16_{:02d}_rip/voice_ev_shuffle_05_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_18_{:02d}_rip/voice_ev_shuffle_06_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_20_{:02d}_rip/voice_ev_band_03_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_27_{:02d}_rip/voice_sc_ev_band_04_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_30_{:02d}_rip/voice_sc_ev_shuffle_10_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_34_{:02d}_rip/voice_ev_band_05_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_40_{:02d}_rip/voice_ev_band_06_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_50_{:02d}_rip/voice_ev_band_07_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_56_{:02d}_rip/voice_ev_band_08_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_65_{:02d}_rip/voice_ev_band_09_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_63_{:02d}_rip/voice_ev_shuffle_21_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_69_{:02d}_rip/voice_ev_band_10_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_76_{:02d}_rip/voice_ev_band_11_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_83_{:02d}_rip/voice_ev_band_12_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_84_{:02d}_rip/voice_ev_shuffle_28_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_90_{:02d}_rip/voice_ev_shuffle_30_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_91_{:02d}_rip/voice_ev_band_13_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_94_{:02d}_rip/voice_ev_shuffle_31_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_101_{:02d}_rip/voice_ev_band_14_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_106_{:02d}_rip/voice_ev_shuffle_36_{:02d}_{:02d}_{:02d}.mp3",
            "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_108_{:02d}_rip/voice_ev_shuffle_38_{:02d}_{:02d}_{:02d}.mp3"
            ]
  elif unit == "MORE MORE JUMP!":
    url_dict = [
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_05_{:02d}_rip/voice_ev_idol_01_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_11_{:02d}_rip/voice_ev_idol_02_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_17_{:02d}_rip/voice_ev_idol_03_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_23_{:02d}_rip/voice_ev_idol_04_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_31_{:02d}_rip/voice_sc_ev_idol_05_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_36_{:02d}_rip/voice_ev_shuffle_12_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_43_{:02d}_rip/voice_ev_idol_06_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_48_{:02d}_rip/voice_ev_shuffle_16_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_52_{:02d}_rip/voice_ev_idol_07_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_57_{:02d}_rip/voice_ev_idol_08_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_67_{:02d}_rip/voice_ev_idol_09_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_73_{:02d}_rip/voice_ev_idol_10_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_78_{:02d}_rip/voice_ev_idol_11_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_80_{:02d}_rip/voice_ev_shuffle_26_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_85_{:02d}_rip/voice_ev_idol_12_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_92_{:02d}_rip/voice_ev_idol_13_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_94_{:02d}_rip/voice_ev_shuffle_31_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_98_{:02d}_rip/voice_ev_idol_13_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_102_{:02d}_rip/voice_ev_shuffle_34_{:02d}_{:02d}_{:02d}.mp3",
      "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_108_{:02d}_rip/voice_ev_shuffle_38_{:02d}_{:02d}_{:02d}.mp3"
    ]
  for base_url in url_dict:
    while story_id <= 8: # 8以下なら続行
      talking_id = 1 # リセット
      while talking_id <= 140: # 140以下なら続行
        url = base_url.format(story_id, story_id, talking_id, target_id)
        # リストに追加
        date_list.append(url)
        
        talking_id += 1
        
      story_id += 1
    story_id = 1
  
    
  # 返す
  return date_list 

def get_leoneed_main_story(target_id):
  # https://storage.sekai.best/sekai-assets/sound/scenario/voice/leo_01_00_rip/voice_op_band0_01_01.mp3
  story_num = 0
  msop = ["ms", "op"]
  date_list = []
  talking_id = 1
  target_id = int(target_id)

  base_url = "https://storage.sekai.best/sekai-assets/sound/scenario/voice/leo_01_{:02d}_rip/voice_{}_band{}_{:02d}_{:02d}.mp3"

  while story_num <= 20:
    talking_id = 1
    while talking_id <= 150:
      for mo in msop:
        url = base_url.format(
          story_num, mo, story_num, talking_id, target_id
        )
        date_list.append(url)
        
      talking_id += 1
    story_num +=1
  story_num = 1
  
  return date_list

def get_card_story(target_id):
  # https://storage.sekai.best/sekai-assets/sound/card_scenario/voice/001001_ichika01_rip/voice_card_01_01a_01_01.mp3
  # https://storage.sekai.best/sekai-assets/sound/card_scenario/voice/001001_ichika01_rip/voice_card_01_01a_02_01.mp3
  # https://storage.sekai.best/sekai-assets/sound/card_scenario/voice/001001_ichika02_rip/voice_card_01_01b_01_01.mp3
  # https://storage.sekai.best/sekai-assets/sound/card_scenario/voice/001006_ichika01_rip/voice_card_ev_band_02_01_3a_03_01.mp3
  # https://storage.sekai.best/sekai-assets/sound/card_scenario/voice/001018_ichika02_rip/voice_card_bd_202208_01_4b_01_01.mp3
  base_url = "https://storage.sekai.best/sekai-assets/sound/card_scenario/voice/{:03d}{:03d}_ichika{:02d}_rip/voice_card_ev_band_{:02d}_{:02d}_{}{}_{:02d}_{:02d}.mp3"
  # target_id, charactor_card_id, story_type, event_id, target_id, page_id, (a or b), talking_id, target_id
  target_id = int(target_id)
  date_list = []

  for charactor_card_id in range(1, 27):
      for story_type in range(1, 3):
          for event_id in range(1, 16):
              for page_id in range(1, 5):
                  for story_type_str in ["a", "b"]:
                      for talking_id in range(1, 141):
                          url = base_url.format(
                              charactor_card_id, story_type, event_id,
                              target_id, page_id, story_type_str,
                              talking_id, target_id
                          )
                          date_list.append(url)
      
  
  return date_list
  
def get_vlive_list(unit, target_id):
  mcid = 1
  talking_id = 1
  target_id = int(target_id)
  date_list = []
    
  if unit == "Leo/need":
    url_bd2023_ichika = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_bd_2023ichika_{}_rip/voice_mc_bd_2023ichika_{:02d}_{:02d}.mp3"
    url_ev14 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_band_14_{}_rip/voice_mc_ev_band_14_MC_{:02d}_{:02d}.mp3"
    url_sev32 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_shuffle_32_{}_rip/voice_mc_ev_shuffle_32_MC_{:02d}_{:02d}.mp3"
    url_bd2023_saki = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_bd_2023saki_{}_rip/voice_mc_bd_2023saki_{:02d}_{:02d}.mp3"
    url_sev31 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_shuffle_31_{}_rip/voice_mc_ev_shuffle_31_MC_{:02d}_{:02d}.mp3"
    url_ev13 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_band_13_{}_rip/voice_mc_ev_band_13_MC_{:02d}_{:02d}.mp3"
    url_whiteday2023 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_2023whiteday_{}_rip/voice_mc_2023whiteday_{:02d}_{:02d}.mp3"
    url_sev30 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_shuffle_30_{}_rip/voice_mc_ev_shuffle_30_MC_{:02d}_{:02d}.mp3"
    url_sev28 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_shuffle_28_{}_rip/voice_mc_ev_shuffle_28_MC_{:02d}_{:02d}.mp3"
    url_2023 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_2022countdown_{}_rip/voice_mc_2022countdown_{:02d}_{:02d}.mp3"
    url_bd2023_shiho = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_bd_2023shiho_{}_rip/voice_mc_bd_2023shiho_{:02d}_{:02d}.mp3"
    url_ev12 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_band_12_{}_rip/voice_mc_ev_band_12_MC_{:02d}_{:02d}.mp3"
    url_newyear_2023_leoneed = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_2023newyear_01_{}_rip/voice_mc_2023newyear_l_{:02d}_{:02d}.mp3"
    url_2022christmas = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_2022christmas_{}_rip/voice_mc_2022christmas_{:02d}_{:02d}.mp3"
    url_bd2022_honami = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_bd_2022honami_{}_rip/voice_mc_bd_2022honami_{:02d}_{:02d}.mp3"
    url_ev11 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_band_11_{}_rip/voice_mc_ev_band_11_MC_{:02d}_{:02d}.mp3"
    url_sev23 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_shuffle_23_{}_rip/voice_mc_ev_shuffle_23_MC_{:02d}_{:02d}.mp3"
    url_ev10 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_band_10_{}_rip/voice_mc_ev_band_10_MC_{:02d}_{:02d}.mp3"
    url_bd2022_ichika = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_bd_2022ichika_{}_rip/voice_mc_bd_2022ichika_{:02d}_{:02d}.mp3"
    url_ev9 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_band_09_{}_rip/voice_mc_ev_band_09_MC_{:02d}_{:02d}.mp3"
    url_ev8 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_band_08_{}_rip/voice_mc_ev_band_08_MC_{:02d}_{:02d}.mp3"
    url_ev7 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_band_07_{}_rip/voice_mc_ev_band_07_MC_{:02d}_{:02d}.mp3"
    url_ev6 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_band_06_{}_rip/voice_mc_ev_band_06_MC_{:02d}_{:02d}.mp3"
    url_ev5 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_band_05_{}_rip/voice_mc_ev_band_05_MC_{:02d}_{:02d}.mp3"
    url_ev4 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_band_04_{}_rip/voice_mc_ev_band_04_MC_{:02d}_{:02d}.mp3"
    url_ev3 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_band_03_{}_rip/voice_mc_ev_band_03_1_{:02d}_{:02d}.mp3"
    url_ev2 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_band_02_{}_rip/voice_mc_ev_band_02_01_{:02d}_{:02d}.mp3"
    url_ev1 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_band_01_{}_rip/voice_mc_ev_band_01_1_{:02d}_{:02d}.mp3"
    url_tanabata2022 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_2022tanabata_{}_rip/voice_mc_2022tanabata_{:02d}_{:02d}.mp3"
    url_bd2022_saki = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_bd_2022saki_{}_rip/voice_mc_bd_2022saki_{:02d}_{:02d}.mp3"
    url_newyear_2022_leoneed = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_2022newyear_01_{}_rip/voice_mc_2022newyear_l_{:02d}_{:02d}.mp3"
    url_bd2022_shiho = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_bd_2022shiho_{}_rip/voice_mc_bd_2022shiho_{:02d}_{:02d}.mp3"
    url_sev16 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_shuffle_16_{}_rip/voice_mc_ev_shuffle_16_MC_{:02d}_{:02d}.mp3"
    url_bd2021_honami = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_bd_2021honami_{}_rip/voice_mc_bd_2021honami_{:02d}_{:02d}.mp3"
    url_1year_anniv = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_2021anniversary_{}_rip/voice_mc_2021anniversary_p_{:02d}_{:02d}.mp3"
    url_sev11 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_shuffle_11_{}_rip/voice_mc_ev_shuffle_11_MC_{:02d}_{:02d}.mp3"
    url_bd2021_saki = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_bd_2021saki_{}_rip/voice_mc_bd_2021saki_{:02d}_{:02d}.mp3"
    url_sev10 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_shuffle_10_{}_rip/voice_sc_ev_shuffle_10_MC_{:02d}_{:02d}.mp3"
    url_bd2021_ichika = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_bd_2021ichika_{}_rip/voice_mc_bd_2021ichika_{:02d}_{:02d}.mp3"
    url_sev5 = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_ev_shuffle_05_{}_rip/voice_ev_mc_shuffle_05_1_{:02d}_{:02d}.mp3"
    url_bd2021_shiho = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_bd_2021shiho_{}_rip/voice_mc_bd_2021shiho_{:02d}_{:02d}.mp3"
    url_newyear_2021_leoneed = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_2021newyear_01_{}_rip/voice_mc_2021newyear_01_{:02d}_{:02d}.mp3"
    url_welcomelive_allstar = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_release_07_{}_rip/voice_mc_release_07_1_{:02d}_{:02d}.mp3"
    url_welcomelive_leoneed = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_release_02_{}_rip/voice_mc_release_02_1_{:02d}_{:02d}.mp3"
    url_bd2020_honami = "https://storage.sekai.best/sekai-assets/virtual_live/mc/voice/mc_bd_honami01_{}_rip/voice_mc_bd_2020honami_{:02d}_{:02d}.mp3"
    
    url_dict = [
    url_bd2023_ichika,
    url_ev14,
    url_sev32,
    url_bd2023_saki,
    url_sev31,
    url_ev13,
    url_whiteday2023,
    url_sev30,
    url_sev28,
    url_2023,
    url_bd2023_shiho,
    url_ev12,
    url_newyear_2023_leoneed,
    url_2022christmas,
    url_bd2022_honami,
    url_ev11,
    url_sev23,
    url_ev10,
    url_ev9,
    url_bd2022_ichika,
    url_tanabata2022,
    url_bd2022_saki,
    url_ev8,
    url_ev7,
    url_newyear_2022_leoneed,
    url_bd2022_shiho,
    url_sev16,
    url_ev6,
    url_bd2021_honami,
    url_ev5,
    url_sev11,
    url_bd2021_saki,
    url_ev4,
    url_sev10,
    url_bd2021_ichika,
    url_ev3,
    url_sev5,
    url_ev2,
    url_bd2021_shiho,
    url_newyear_2021_leoneed,
    url_welcomelive_allstar,
    url_welcomelive_leoneed,
    url_bd2020_honami,
    url_ev1
]
    
    for base_url in url_dict:
      while mcid <= 6: # 6以下なら
        talking_id = 1
        while talking_id <= 160:
          url = base_url.format(mcid, talking_id, target_id)
          
          date_list.append(url)
          talking_id += 1
        
        mcid += 1
      mcid = 1
    
    
    mcid = 1
    talking_id = 1
    
    while mcid <= 12: # 12
      talking_id = 1
      while talking_id <= 200:
        url = url_1year_anniv.format(mcid, talking_id, target_id)
        
        date_list.append(url)
        
        talking_id += 1
      mcid += 1
    mcid = 1
        
  # 返す
  return date_list 

def get_charactor_story():
  base_url = "https://storage.sekai.best/sekai-assets/sound/scenario/voice/self_ichika_rip/voice_selfep_band_{:02d}_01.mp3"
  talking_id = 1
  date_list = []
  
  while talking_id <= 30:
    url = base_url.format(talking_id)
    date_list.append(url)
    
    talking_id += 1
    
  return date_list
  
#> main.py
# データ取得関数
def request_multi(url_list, save_dir, cd):
  # 5プロセスに分割
  url_count = len(url_list)
  per_file = int(url_count / 5)
  
  # リストに変換
  # メモ
  # list_1 に [:100+1] 0 ~ 100
  # list_2 に [100+1:(100 * 2) +1] 101 ~ 200
  # list_3 に [(100 * 2) + 1:(100 * 3) + 1] 201 ~ 300
  list_1 = url_list[:per_file+1]
  list_2 = url_list[per_file+1:(per_file * 2) + 1]
  list_3 = url_list[(per_file * 2) + 1:(per_file * 3) + 1]
  list_4 = url_list[(per_file * 3) + 1:(per_file * 4) + 1]
  list_5 = url_list[(per_file * 4)+ 1:]

  # jsonに書き込み
  date = {"list_1": list(list_1),
          "list_2": list(list_2),
          "list_3": list(list_3),
          "list_4": list(list_4),
          "list_5": list(list_5),
          "list_1_STATUS": False,
          "list_2_STATUS": False,
          "list_3_STATUS": False,
          "list_4_STATUS": False,
          "list_5_STATUS": False,
          "SAVE_DIRECTORY": save_dir,
          "COOLDOWN": cd}
  
  # あるなら消す
  if os.path.exists("./data.json"):
    os.remove("./data.json")
  
  jsoncfg.write(date, "./data.json")
  
  # 実行
  subprocess.Popen(["sub.bat"])
  
  # 修了確認待機
  process_status = True
  while process_status:
    try:
      date = jsoncfg.read("./data.json")
    
    except FileNotFoundError:
      pass
    
    except json.JSONDecodeError:
      pass
      
    if date["list_1_STATUS"] == True and date["list_2_STATUS"] == True and date["list_3_STATUS"] == True and date["list_4_STATUS"] == True and date["list_5_STATUS"] == True:
      process_status = False
      break
      
    else:
      continue
  
  
  return "Done."

#> run.py
# 取得実行
def run(date_dict):
  # データを取得
  CD = date_dict["Cooldown"]
  MEMBER_ID = date_dict["ID"]
  LOGGING = date_dict["IsLogging"]
  OUTPUT_PATH = date_dict["from_path"]
  adalurlcsab = False
  
  # IDに応じたテンプレURLを作成
  # EV_BASE_URL =\
    # "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_" \
    # + f"{event_id}" \
    # + "_{:02d}_rip/" \
    # + f"{voice_ev}_" \
    # + f"{event_single}_{event_single_id}" \
    # + "_{:02d}_{:02d}_" \
    # + f"{MEMBER_ID}.mp3"

  VLIVE_BASE_URL =\
    ""
    
  # 全パターンをすべて取得
  EV_URL_ALL = get_event_list(unit="Leo/need", target_id=MEMBER_ID)
  VLIVE_URL_ALL = get_vlive_list(unit="Leo/need", target_id=MEMBER_ID)
  UNIT_STORY_ALL = get_leoneed_main_story(target_id=MEMBER_ID)
  if MEMBER_ID == "01":
    CHARACTOR_STORY_ALL = get_charactor_story()
    adalurlcsab = True
    
#  ALL_URL = EV_URL_ALL.extend(VLIVE_URL_ALL)
#  ALL_URL = ALL_URL.extend(UNIT_STORY_ALL)
  
#  if adalurlcsab:
#    ALL_URL = ALL_URL.extend(CHARACTOR_STORY_ALL)
  
  # 実行
  request_multi(EV_URL_ALL, OUTPUT_PATH, CD)
  print("Waiting Cooldown.. (120s)")
  time.sleep(120)
  request_multi(VLIVE_URL_ALL, OUTPUT_PATH, CD)
  print("Waiting Cooldown.. (120s)")
  time.sleep(120)
  request_multi(UNIT_STORY_ALL, OUTPUT_PATH, CD)
  print("Waiting Cooldown.. (120s)")
  time.sleep(120)
  request_multi(CHARACTOR_STORY_ALL, OUTPUT_PATH, CD)
  
  
  # 名前の変更
  if MEMBER_ID == "01":
    MEMBER_ID = "星乃一歌"
  
  rename_filelist = los.file_extension_filter(os.listdir(OUTPUT_PATH), [".mp3"])
  
  x = 0
  
  for files in rename_filelist:
    filename = f"ID_{MEMBER_ID}-data({x:06d}).mp3"
    
    os.rename(os.path.join(OUTPUT_PATH, files), os.path.join(OUTPUT_PATH, filename))
    print(f"Renamed: {files}")
    
    x += 1
  
#> launch.py
# 設定、定義データ保持などを行う
# start
def start(cd, member, logging, outputs):
  # cd のチェック
  if 0 < cd < 0.15:
    pass
  else:
    cd = 0.0001
    print(f"クールダウンの値が正しくなかったため、修正されました。 ( -> {cd}s)")

  # 辞書へいろいろと渡す
  date_passed_dict = {
    "Cooldown": cd,
    "ID": member,
    "IsLogging": logging,
    "from_path": outputs
  }
  
  # 実行
  run(date_passed_dict)

if __name__ == "__main__":
  cd = float(input("クールダウンの設定 (秒単位): "))
  #member = input("取得キャラID (:02d): ")
  member = "01"
  logging = input("Logging (0 / 1): ")
  logging = cin.tfgen_boolean(logging)
  output = fos.output(True)
  
  start(cd, member, logging, output)
