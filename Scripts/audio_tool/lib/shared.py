import os
import locale
import LGS.misc.jsonconfig as jsoncfg

ROOT_PATH = os.getcwd()
db = jsoncfg.read(os.path.join(ROOT_PATH, "database.json"))
setting = db["user_setting"]

# 言語設定
if os.name == "nt":
  lang_data = locale.getdefaultlocale()
  
  if lang_data[0] == "ja_JP": # 安定性向上のためのキャッチ処理
    print(f"return: {lang_data}\nSelected Language: ja_jp")
    lang = jsoncfg.read(
      os.path.join(ROOT_PATH, "lang", db["lang_path"]["ja_jp"]))
  elif lang_data[0] == "en_US":
    print(f"return: {lang_data}\nSelected Language: en_US")
    lang = jsoncfg.read(
      os.path.join(ROOT_PATH, "lang", db["lang_path"]["en_us"])
    )
  else:
    lang = lang_data[0]
    print(f"Unsupported Language: {lang}")
    
    if f"{lang}.json" in db["lang_path"]["created"]:
      lang = jsoncfg.read(
        os.path.join(ROOT_PATH, "lang", f"{lang}.json")
      )
      print(f"Language File Found!\nusing Custom lang file..")
    
    else:
      lang = jsoncfg.read(
        os.path.join(ROOT_PATH, "lang", db["lang_path"]["en_us"])
      )
      print("Language File Not found.\nUsing en_us.json..")
    
else:
  print(f"using old method")
  lang_data = os.getenv('LANG')
  # COMING SOON
  
  lang = jsoncfg.read(
    os.path.join(ROOT_PATH, "lang", "en_us.json]")
  )

if setting["override_lang"]:
  lang = jsoncfg.read(
    os.path.join(ROOT_PATH, "lang", setting["target_langPath"])
  )

