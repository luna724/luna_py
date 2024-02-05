from LGS.misc.jsonconfig import write
import LGS.misc.jsonconfig as jsoncfg
import LGS.misc.nomore_oserror as los
import os
import argparse

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

def get_js():
    # javascript の読み込み
  js = ""
  for x in los.file_extension_filter(
    os.listdir(os.path.join(ROOT_DIR, "javascript")), 
    [".js"]
  ):
    js += jsoncfg.read_text(
      os.path.join(ROOT_DIR, "javascript", x)
    )
    js += "\n"
  return js

def parse_parsed_arg(arg, rtl_value, instance_check=None):
  """

  Args:
      arg (_type_): _description_
      rtl_value (_type_): _description_
      instance_check (_type_, optional): use isinstance() check. Defaults to None.
  """
  
  if arg == None:
    return rtl_value
  
  if arg:
    if not instance_check == None:
      if isinstance(arg, instance_check):
        return arg
    return arg
  else:
    return arg