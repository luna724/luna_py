import os
import modules.shared
from modules.shared import ROOT_DIR
from modules.lib import mkdir

def run():
  print("preprocessing..", end="")
  def convertToJson(filename):
    os.rename(
    os.path.join(ROOT_DIR, "database", "v3", f"{filename}.jsraw"), os.path.join("database", "v3", f"{filename}.json")
    )
    return
  
  mkdir(["logs", "template_backups", "prompt"])
  jsraw2json = [""]

  
  with open(os.path.join(ROOT_DIR, "lscript_alreadyprp.ltx"), "w") as f:
    f.write("don't delete this file. maybe reset template system")
  
  print("  Done.")
  return