import LGS.misc.jsonconfig as jsoncfg
import os
import argparse

ROOT_DIR = os.getcwd()
DB_PATH = os.path.join(ROOT_DIR, "database", "v3")

# Database
def database(key):
  if key == None:
    return jsoncfg.read(
    os.path.join(DB_PATH, "database_ui.json")
  )
  
  return jsoncfg.read(
    os.path.join(DB_PATH, "database_ui.json")
  )[key]


negative = database("negative")
ad_pos = database("ad_pos")
ad_neg = database("ad_neg")

delete_cache = False


# Template Prompt System
currently_version = "v3"
currently_template_versionID = 3 # 3.0.3
noneimg = os.path.join(DB_PATH, "noneimg8cmwsvcifvfosi923jrvsvvnsfs.png")

class script_data():
  class modules_generate():
    acceptable_version = ["v3", "v4β"]
    
  generate_py = modules_generate()
  

data = script_data()


def arg_parse():
  parse = argparse.ArgumentParser("parser")
  parse.add_argument("--test_mode", action='store_true')
  parse.add_argument("--local", action='store_true')
  parse.add_argument("--loopui", action='store_true')
  parse.add_argument("--open_browser", action='store_true')
  parse.add_argument("--dev_restart", action='store_true')
  parse.add_argument("--share", action='store_true')
  parse.add_argument("--ui_port")
  parse.add_argument("--ui_ip")

  return parse.parse_args()
args = arg_parse()