from lib import reset_keybind, reset_selected, ui
import random
import string
import os
import pyperclip
import LGS.misc.jsonconfig as jsoncfg


def randomname(n):
  randlst = [random.choice(string.ascii_letters + string.digits)
             for i in range(n)]
  return ''.join(randlst)

def main_function(target_cfg_path, your_cfg_path, replace_keybind_if_none, replace_visuals_if_none, easy_load, strict_check,
                  convert_visuals, convert_target=[], convert_keybind=True):
  if not os.path.exists(target_cfg_path):
    return "cannot find config file. please input valid path"
  
  new_config = jsoncfg.read(target_cfg_path)
  db_config = jsoncfg.read(your_cfg_path)
  
  if not len(new_config["modules"]) == len(db_config["modules"]):
    print("WARN: inconsistent config data.")
    print("WARN: using strict check.. (!!Experimental Mode)")
    strict_check = True

  ## 処理 - キーバインドの結合
  if convert_keybind:
    new_config = reset_keybind(new_config, db_config, replace_keybind_if_none, strict_check)
  
  ## 処理 - テーマの結合
  #if convert_visuals:
  #  new_config = reset_visuals(new_config, db_config, replace_visuals_if_none)
  if convert_visuals:
    convert_target_vs = [
      "ANY VIsuals Item"
    ] 
    for x in convert_target_vs:
      convert_target.append(x)
  
  ## 処理 - その他選択したものの結合
  if len(convert_target) != 0:
    new_config = reset_selected(new_config, db_config, convert_target)
  
  if easy_load:
    cmd = ".config load "
    
    filename = os.path.basename(target_cfg_path) + "_" + randomname(12) +".json"
    cmd += filename
    
    user_home = os.path.expanduser("~")
    prax_cfg_path = os.path.join(user_home, r'AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\RoamingState\Prax\config')
  
    if os.path.exists(prax_cfg_path):
      jsoncfg.write(new_config, os.path.join(prax_cfg_path, filename))
  
    print('config load command are copied to clipboard!')
    backup_copy = pyperclip.paste()
    pyperclip.copy(cmd)
    
  else:
    jsoncfg.write(new_config, os.path.join(os.getcwd(), "outputs", filename))
  return "Done."

if __name__ == "__main__":
  print(ui().queue(64).launch())