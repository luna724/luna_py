import LGS.misc.jsonconfig as jsoncfg
import os

ROOT_DIR = os.getcwd()

# Database
def database(key):
  if key == None:
    return jsoncfg.read(
    os.path.join(ROOT_DIR, "database", "v3", "database_ui.json")
  )
  
  return jsoncfg.read(
    os.path.join(ROOT_DIR, "database", "v3", "database_ui.json")
  )[key]

delete_cache = False


# Template Prompt System
currently_version = "v3"
currently_template_versionID = 2 # v3-r5 - 3.0.2
noneimg = os.path.join(ROOT_DIR, "database", "v3", "noneimg8cmwsvcifvfosi923jrvsvvnsfs.png")

class script_data():
  class modules_generate():
    acceptable_version = ["v3", "v4β"]
    
  generate_py = modules_generate()
  

data = script_data()