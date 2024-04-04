import os
import preprocessing
import argparse

from webui import start

def dbfiles(fp) -> None:
  from modules.shared import DB_PATH

  if os.path.exists(os.path.join(DB_PATH, fp)):
    return
  else:
    from LGS.misc.jsonconfig import write
    write({}, os.path.join(DB_PATH, fp))
    


if __name__ == "__main__":
  #shared.args = arg_parse()
  
  # if not os.path.exists(os.path.join(
  #   os.getcwd(), "lscript_alreadyprp.ltx")):
  #   preprocessing.run()
    
  # if arg_parse().test_mode:
  #   iface.queue(64)
  #   print(iface.launch(server_port=9999))
  dbfile = [
    "keywords_list.json", "lora_list.json",
    "template_list.json"
  ]
  for x in dbfile:
    dbfiles(x)
  
  
  print(start())