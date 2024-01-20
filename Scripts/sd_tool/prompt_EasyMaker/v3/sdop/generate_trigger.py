from modules.shared import ROOT_DIR

from datetime import datetime
import os


class beta_feature():
  def print_out(self, gend_text):
    print("[SD-WebUI Output Paster]: ", end="")
    print(gend_text)
    
    with open(os.path.join(ROOT_DIR, "sdop_out", datetime.now().strftime("%Y%m%d%H%M%S"))) as f:
      f.write(f"Source: @NONE@\n\n{gend_text}")
    return
  
  def parse(self, text):
    return

# RECOMMENDED import ALL
# from sdop.generate_trigger import * (or beta_feature)