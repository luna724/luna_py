import os
import preprocessing
import argparse

from webui import start



if __name__ == "__main__":
  #shared.args = arg_parse()
  
  if not os.path.exists(os.path.join(
    os.getcwd(), "lscript_alreadyprp.ltx")):
    preprocessing.run()
    
  # if arg_parse().test_mode:
  #   iface.queue(64)
  #   print(iface.launch(server_port=9999))
  
  print(start())