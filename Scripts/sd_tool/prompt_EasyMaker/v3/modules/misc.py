from LGS.misc.jsonconfig import write
import os

from modules.shared import ROOT_DIR, database

def modify_database(neg, adp, adn):
  new = {
    "negative": neg,
    "ad_pos": adp,
    "ad_neg": adn
  }
  
  write(
    new, os.path.join(ROOT_DIR, "database", "v3", "database_ui.json")
  )
  
  d = database(None)
  return d["negative"], d["ad_pos"], d["ad_neg"]