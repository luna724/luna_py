import _sha256; import os
import luna_GlobalScript.downloading_script.request as download
import luna_GlobalScript.project_sekai.unit_charactor_analyser.main as charactor_checker
import luna_GlobalScript.misc.luna_log_reader as load

def check(id, name, dl, cd, dlc, x, y, z): # キャラクターがどのユニットに所属しているか、チェックする
    if id == "01" or id == "02" or id == "03" or id == "04":
        event_type = "Leo/need"
        Unit_ID = "01"
    elif id == "05" or id == "06" or id == "07" or id == "08":
        event_type = "MORE MORE JUMP!"
        Unit_ID = "02"
    elif id == "09" or id == "10" or id == "11" or id == "12":
        event_type = "Vivid Bad Squad"
        Unit_ID = "03"
    elif id == "13" or id == "14" or id == "15" or id == "16":
        event_type = "Wonderlands & Showtime"
        event_type_ja = "ワンダーランズ×ショウタイム"
        Unit_ID = "04"
    elif id == "17" or id == "18" or id == "19" or id == "20":
        event_type = "Nightcode at 25ji"
        event_type_ja = "25時、ナイトコードで。"
        Unit_ID = "05"
    elif id == "21" or id == "22" or id == "23" or id == "24" or id == "25" or id == "26":
        event_type = "Virtual Singer"
        Unit_ID = "00"
    os_check = os.environ.get("OS") # Windowsの場合、TEMPファイルを指定
    if os_check == "Windows_NT":    # そうでない場合、相対パスを使用
        temp_dir = os.environ.get("TEMP")
        temp_dir = temp_dir + "\\"
    else:
        temp_dir = "./temp/"
    output_directory = temp_dir + "lunascripttemp.txt"
    charactor_checker.check(Unit_ID, event_type, id, name, output_directory)
    returna = load.load(output_directory, True)
    download.main(id, Unit_ID, dl, cd, dlc, x, y, z)
# (member_name, member_id, url, cds, dlc)
# https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_{y}_{z}_rip/voice_ev_shuffle_28_01_{x}_{member_id}.mp3
# メイン関数
def main_function(name, id, dl, cd, dlc):
    counts = 0
    x = "01"; y = "01"; z = "01"
    dl = f"https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_{y}_{z}_rip/voice_ev_shuffle_28_01_{x}_{id}.mp3"
    check(id, name, dl, cd, dlc, x, y, z)
