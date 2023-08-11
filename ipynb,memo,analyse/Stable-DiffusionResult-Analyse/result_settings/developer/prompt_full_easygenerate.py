import luna_GlobalScript.misc.jsonconfig as jsonconfig
import os
import random
from luna_GlobalScript.misc.nomore_oserror import filename_resizer as no_more_oserror
import luna_GlobalScript.misc.compact_input as inres

os.makedirs("./cache",exist_ok=True)
# 分岐処理を行う関数
def hiresfix(value):
    #if value:
        # Hires.fixオン時の処理
    #else:
        return 0

def adetailer(value):
    global adetailer_model
    if value:
        # ADetailer有効時の処理
        n = input("15-2. ADetailer model: ")
        adetailer_model = exc("Model", "adetailer_model", n)
        
    else:
        return 0

# メイン処理

if os.path.exists(f"./cache/prompt_config.json"): # 上書きを行わないための読み込み処理
    main = jsonconfig.read("./cache/prompt_config.json")
    session_number = main["latest_session"]
    old_config_dir = main["from"] # 辞書を読み込み
    old_config = jsonconfig.read(old_config_dir)
    session_number += 1
    x = "{:06d}".format(session_number)
    print(f"Successfully Setup Session \nNumber:{session_number}  Starting!")
else: # メインコンフィグが存在しない場合
    print("Error: Cannot find main config\n(if you first run, No problem)")
    session_number = 0
    x = "{:06d}".format(session_number)
    print(f"Successfully Setup Session \nNumber:{session_number}  Starting!")
    
# ファイル名 用  ランダム値生成
random = random.randrange(0, 999999)
random = "{:06d}".format(random) 
# コンフィグファイル名受付、処理
configname = input("Config Name(ファイル名): ")
if inres.isnone(configname):
    configname = "Nothing_Input"
else:
    configname = no_more_oserror(configname, "filename", "_")

# 変数設定
writing_config_dict = {}
config_dir = f"./cache/{configname}_prompt_config_{x}-{random}.json" # configディレクトリの設定

# コンフィグ入力変更処理
    
def cnps(config_name_printout, value): # プリントアウト用の処理
    # cnps = config_name_printout
    cnpss, value = str(config_name_printout), str(value)
    return f"{cnpss}: {value}"

def exc(cnp, config, value="NOTHING_INPUT_USE_HISTORY-98421651924", type_num=False, isboolean=False, isonly_selected_can_here=False, not_normalize=False, special_function=False, special_function_name=""):
    global writing_config_dict
    dict_name = {"Hires_fix": hiresfix,
                 "ADetailer": adetailer}
    if isonly_selected_can_here: # それぞれの属性を取得
        value = value
        writing_config_dict[f"{config}"] = f"{value}"
        if special_function:
            dict_name[special_function_name](value)
        if not_normalize:
            return value
        f = cnps(cnp, value)
        return f
    if isboolean:
        value = inres.tfgen(value)
    if type_num:
        value = str(type_num)
    if value == "NOTHING_INPUT_USE_HISTORY-98421651924" or value == "From0History" or value == "@log":
        # ログからの取得
        x = "Unknown"
        try:
            old_config.get(config, x)
        except Exception as e:
            print(f"Program Can't Catched This Error.\nSelected {config} to \"Unknown\"\Error: {e}")
            value = "Unknown"
            writing_config_dict[f"{config}"] = f"{value}"
            if special_function:
                dict_name[special_function_name](value)
            if not_normalize:
                return value
            f = cnps(cnp, value)
            return f
        value = old_config.get(config, x)
        if value == x:
            print(f"{config}: 過去内容の取得に失敗しました。\nKeyError: '{config}'")
    writing_config_dict[f"{config}"] = f"{value}"
    if special_function:
        dict_name[special_function_name](value)
    if not_normalize:
        return value
    f = cnps(cnp, value)
    return f
    

# ユーザー入力制御
print("何も入力しなかった場合、前回に入力した内容が使用されます。\n")
n = input("1. Prompt: ")
prompt = exc("Prompt", "prompt", n)
n = input("2. Negative (Prompt): ")
negative = exc("Negative Prompt", "negative", n)
n = input("3. Result Width: ")
width = exc("", "width", n, True, False, False, True)
n = input("4. Result Height: ")
height = exc("", "height", n, True, False, False, True)
n = input("5. Batch Size: ")
bs = exc("Batch Size", "batch_size", n, True)
n = input("6. Batch Count: ")
bc = exc("Batch Count", "batch_count", n, True)
n = input("7. CFG Scale: ")
cfg = exc("CFG Scale", "cfg_scale", n, True)
n = input("8. Seed: ")
seed = exc("Seed", "seed", n, True)
n = input("9. Restore Faces (0 or 1): ")
rsf = exc("Restore Faces", "restore_faces", n, False, True)
n = input("10. Tilling (0 or 1): ")
tilling = exc("Tilling", "tilling", n, False, True)
n = input("11. Hires.fix (0 or 1): ")
hires_fix = exc("Hires.fix", "hires_fix", n, False, True, False, False, True, "Hires_fix")
n = input("12. Sampling Method: ")
smethod = exc("Sampling Method", "sampling_method", n)
n = input("13. Sampling Steps: ")
ssteps = exc("Sampling Steps", "sampling_steps", n, True)
n = input("14. ToMe Extension (0 or 1): ")
tome = exc("To Me Enabled", "tome_enable", n, False, True)
n = input("15. ADetailer Enabled (0 or 1): ")
adetailer = exc("ADetailer Extension Enabled", "adetailer_enable", n, False, True, False, False, True, "ADetailer")


# 上書きを行わないための書き込み処理
writing = {"latest_session": f"{session_number}",
           "from": f"{config_dir}"}
jsonconfig.write(writing, "./cache/prompt_config.json")


# Test
jsonconfig.write(writing_config_dict, config_dir)