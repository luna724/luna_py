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
import subprocess
import LGS.misc.output_folder as out
from LGS.misc.debug_tool import dprint as dprint
import LGS.misc.jsonconfig as jsoncfg
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
#
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

# 拡張子を指定
ext = input("音声ファイル拡張子(wav, flac, mp3): ")
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
if get_sekai:
    mode_list.append("se")
if get_anov:
    mode_list.append("an")


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
    save_name = f"{x}"