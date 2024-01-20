import os
import preprocessing
import argparse

from webui import start
from modules.shared import ROOT_DIR
import modules.shared as shared

from modules.test.webui import iface

def arg_parse():
  parse = argparse.ArgumentParser("parser")
  parse.add_argument("--test_mode", action='store_true')

  return parse.parse_args()

if __name__ == "__main__":
  shared.args = arg_parse()
  
  if not os.path.exists(os.path.join(
    ROOT_DIR, "lscript_alreadyprp.ltx")):
    preprocessing.run()
    
  if shared.args.test_mode:
    iface.queue(64)
    print(iface.launch(server_port=9999))
    
  print(start())