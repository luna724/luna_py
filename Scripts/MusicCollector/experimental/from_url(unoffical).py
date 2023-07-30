"""
    this script is not verified Sekai Viewer System.
    if not working please use "..\new_main.py"
"""
# BASE URL
# https://storage.sekai.best/sekai-assets/music/long/0006_01_rip/0006_01.flac
# music/long/ {:04d} <- Song ID
# music/long/{:o4d}_ {:02d} <- Vocal (00 = VSinger
# 01 = Sekai Ver, 02... = Another Vocal) Max = 08 Journey
# music/long/{:o4d}_{:02d}_rip/{:04d}_{:02d}. {extension} <- flac(FLAC) or mp3 (MP3)
#
Debug_Mode = True
# デバッグモード - プリントアウトによる処理検知用

import requests
import os
import random
import hashlib
import time
import LGS.misc.output_folder as out
from LGS.misc.debug_tool import dprint as dprint
import LGS.misc.jsonconfig as jsoncfg
import LGS.misc.re_finder as find
import LGS.misc.random_roll as roll
import LGS.misc.compact_input as cin
import LGS.misc.nomore_oserror as los
import LGS.music_file.flac2wav as flac2wav
import LGS.music_file.wav2mp3 as wav2mp3
# Bitrate 768Kbps (FLAC) -> 1411Kbps (WAV)
import LGS.project_sekai.unit_charactor_analyser.id.any_roma2idxname as name_resizer

def dp(str):
    if Debug_Mode == True:
        dprint(str)
def errorgen(str):
    print(str)
    # raise f"str"
def get(url, save_name, dir):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(dir, save_name), 'wb') as f:  # 新しく保存
            f.write(response.content)
            print('ファイルを', os.path.join(dir, save_name), "に保存しました")
    else:
        print(f"Failed Get Response from: {url} \n \
                Status: {response.status_code}")

old_base_url = "https://storage.sekai.best/sekai-assets/music/long/{:04d}_{:02d}_rip/{:04d}_{:02d}.{}"
new_base_url = "https://storage.sekai.best/sekai-assets/music/long/{}_{:04d}_{:02d}_rip/{}_{:04d}_{:02d}.{}"
url_list = []
mode_list = []
old_url = []
url_dict = {}
url = ""
get_vs = False
get_anov = False
get_sekai = False
filename_num = 0

# 入力、変数
iffilter = input("ベータ機能: フィルタの設定 (0(なし) or 1(あり)): ")
if cin.tfgen_boolean(iffilter):
    dp("Starting Beta Filtering")
    filter = True
    print(f"注意: この設定はβモードです。\nフィルタ設定: ")
    member_filter = input("取得したいキャラの名前を入力 (例: ichika): ")
    member_name, members = name_resizer.returnmode_02d(member_filter, False)
    
    # TEMP 未実装が選択されたら
    if not members == "01":
        filter = False
        dp("Error: Not Available Charactor ID Selected.")
        print(f"未実装のキャラクターが選択されたため、フィルタはオフになりました。")
        
else:
    filter = False
    dp("Skipping Beta Filtering")
    
# フィルタチェック
if filter:
    print(f"フィルタオンで続行。\nFilter: {members}")
elif not filter:
    print(f"フィルタオフで続行。")

# URLの用意、取得環境の確認

# 拡張子を指定
ext = input("音声ファイル拡張子(wav, flac): ")
if ext == "wav":
    print("WAV形式では、FFmpegを使用し、1411Kbpsでの出力を行います。")
    extension = "flac"
    convertWAV = True
elif ext == "flac":
    print("FLAC形式では、768Kbpsでの取得を行います。")
    extension = "flac"
    convertWAV = False
elif ext == "mp3":
    print("MP3形式では、320Kbpsでの取得を行います。")
    extension = "mp3"
    convertWAV = False
    convertMP3 = True
else: # 違う場合、終了
    print("不明な形式です。すべて小文字で、選択肢内の物を選んでください。")
    raise f"ValueError: Not Matching File Extension"

# バチャシンの取得確認
vsinger = input("バーチャルシンガー(Virtual Singers)のボーカルの取得も行いますか？(0 or 1): ")
if cin.tfgen_boolean(vsinger):
    get_vs = True
    print("Virtual Singerの取得も行います。")

# セカイver の取得確認
sekai = input("セカイver のボーカル取得も行いますか？(0 or 1): ")
if cin.tfgen_boolean(sekai):
    get_sekai = True
    print("Sekai Ver. の取得も行います。")

# アナザーボーカルの取得確認
anov = input("アナザーボーカルの取得も行いますか？(0 or 1): ")
if cin.tfgen_boolean(anov):
    get_anov = True
    print("アナザーボーカルの取得も行います。")
    
# モードリストの設定
if get_vs:
    mode_list.append("vs")
else:
    errorgen("ValueError: Can Input 0 or 1")
if get_sekai:
    mode_list.append("se")
else:
    errorgen("ValueError: Can Input 0 or 1")
if get_anov:
    mode_list.append("an")
else:
    errorgen("ValueError: Can Input 0 or 1")


# ループでURLを生成する
# 2023/07/29  382曲存在
for song_id in range(0, 383):
    for vocal_id in range(1, 6): 
        # 旧URLでの取得
        url = old_base_url.format(song_id, vocal_id, song_id, vocal_id, extension)
        old_url.append(url)
        dp(f"Added List \"{url}\"")
    
    # 新URLでの取得
    for vocal_id in range(1, 6):    
        for mode in mode_list:
            url = new_base_url.format(mode, song_id, vocal_id, mode, song_id, vocal_id, extension)
            url_list.append(url)
            dp(f"Added List \"{url}\"")
        
dp(f"Starting Download.. \n\
    URL_List: {url_list} \n\
    OLD_List: {old_url}")

# セーブ位置の設定
dir = out.output(True)
dp(f"Setting Output Directory: {dir}")

# ダウンロード、書き出し
for url in old_url:
    filename_num += 1
    filename = find.extract(r"/(\d+_\d+)\.flac", url)
    save_name = f"{filename_num}-{filename}.flac"

    get(url, save_name, dir)
    
    if roll.random_roll(0.75):
        sleep = random.randrange(1, 5)
        if roll.random_roll(0.3):
            sleep /= 10
        time.sleep(sleep)

# 新しいタイプのURLのダウンロー°、書き出し
for url in url_list:
    filename_num += 1
    filename = find.extract(r"/([a-zA-Z]+_\d+_\d+)\.flac", url)
    filename_bytes = filename.encode("utf-8") # バイト列に変換
    hashs = hashlib.sha1(filename_bytes).hexdigest()
    save_name_ = f"f{hashs}.{filename_num}-{filename}.flac"
    # 正則化
    save_name = los.filename_resizer(save_name_, replaceTo="0")

    get(url, save_name, dir)
    
    if roll.random_roll(0.75):
        sleep = random.randrange(1, 5)
        if roll.random_roll(0.3):
            sleep /= 10
        time.sleep(sleep)


# ファイル名の変更
"""
listfile に取得ファイルのリストを保存
flacの拡張子のみに厳選
-{filename} に当たる位置を x に取得

forループ内で、値に応じたファイル名を取得
ファイル名に応じてリネーム

    """

listfile = os.listdir(dir)
listfile = los.file_extension_filter(listfile, ["flac"])
os.chdir(dir)

for file in listfile:
    x = file.split("-", 1)[-1]
    
    # この先には値に応じてファイル名を変更する機能を実装する
    """
    
    info_dict = jsoncfg.read("./song_info.json")
    new_name = info_dict[x]
    os.rename(x, new_name)
    print(f"{x} -> {new_name}")
    
    """
    
    # 変換がオンの場合
    if convertWAV:
        flac2wav.main(x, dir)
    
    if convertMP3:
        flac2wav.main(x, dir)
        time.sleep(10)
        wav2mp3.main(x, dir)