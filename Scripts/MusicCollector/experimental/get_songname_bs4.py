import LGS.misc.jsonconfig as jsonconfig
import requests
from LGS.misc.re_finder import extract as r
from bs4 import BeautifulSoup

# 関数
def get_html_parser(target_url):
  # 取得
  response = requests.get(target_url)
  
  # 404 Not Found を返された場合、無視
  if response.status_code == 404:
    return None
  
  # 正常に成功したなら
  elif response.status_code == 200:
    res_txt = response.text
    print(f"Return Responce(Full): {res_txt}")
    # print(f"Text Mode: {}")
    pars = BeautifulSoup(res_txt, 'html.parser')
    return pars
  
  # それ以外なら失敗コードを返す
  else:
    print("Error Code: " + response.status_code)
    return "Failed-lunaFailCode.004"
  
  
# 取得すべきもの
# <h6 class="MuiTypography-root MuiTypography-h6 css-58dzjf">DAYBREAK FRONTLINE</h6>

# 値の取得
def get_songname(parser, Debugging=False):
  # とりあえず、探して
  class_list = parser.find_all(class_='MuiTypography-root MuiTypography-h6 css-58dzjf')
  
  print(f"Class_list: {class_list}")
  # 一つ目に絞り込み
  item = class_list[0].text
  
  # あってるかチェック
  print(f"Return {item}")
  
  # 返す
  return item

# メイン関数
def Function_mode(cooldown=0.01, min_max=[1, 383]):
  # 初期化
  url_list = []
  song_data_dict = {}
  
  # URLリストの用意
  for x in range(min_max[0], min_max[1]):
    url_list.append(f"https://sekai.best/music/{x}")
  
  # 取得開始
  for url in url_list:
    # データ変換
    dldata = r(pattern=r"music/(\d+)", str=url)
    dldata = "{:04d}".format(int(dldata))
    
    # html.parser を data に代入
    data = get_html_parser(url)
    
    # エラーが起きているなら
    # if luna.errcheck(data):
    #  raise ValueError("200 または 404 以外のステータスコードが返されました。")
      
    # 404 Not Foundなら
    if data == None:
      print(f"{url}\n\
        404 Not Foundが返されました。")
      continue
      
    # 当てはまらなかったら、値を取得
    song_name = get_songname(data)
    
    # 何か入ってるなら続ける
    if not song_name == None:
      song_data_dict[dldata] = song_name
    
    else:
      print(f"{url}\n 曲名が取得できませんでした。")
    
  jsonconfig.write(song_data_dict, "./song_info.json")


if __name__ == "__main__":
  cd = float(input("クールダウンの値を設定 (float): "))
  min = int(input("曲ID の最小取得値を設定 (integer): "))
  max = int(input("曲iD の最終取得値を設定 (integer): "))
  
  min_max = [min, max]
  
  Function_mode(cd, min_max)
  