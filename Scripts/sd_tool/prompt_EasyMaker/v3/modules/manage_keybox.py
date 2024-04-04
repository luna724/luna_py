import os
import gradio as gr
from typing import *
from datetime import datetime
import LGS.misc.jsonconfig as jsoncfg

from modules.lib import time_takens
from modules.shared import language, DB_PATH, ROOT_DIR

def r(_x:str) -> str:
  return _x.strip()
def save(displayname:str,
        keyword:str,
        multikey:bool,
        keywords:str,
        sequence:Literal["$WORD", "%WORD%"],
        multiseq:bool,
        replaceto:str,
        info:str,
        overwrite:bool,
        hide:bool,
        emulate:bool=False
        ):
  lang = language("/ui/mt_child/define/keybox.py", "raw")["system"]
  
  # Error handling
  if r(keyword) == "" or r(replaceto) == "":
    raise gr.Error(lang["empty_variable"])
  
  # Sequence のセット
  if multiseq:
    sequence = ["$", "%"]
  else:
    if sequence in ["$WORD", "%WORD%"]:
      sequence = [sequence[:1]]
    else:
      gr.Warning(lang["unknown_sequence"])
      sequence = ["$", "%"]
  
  # Key のセット
  if multikey:
    if r(keywords) != "":
      keys = [r(x) for x in keywords.split("$")]
      keys.insert(0, keyword)
    
    else:
      keys = [keyword]
  else:
    keys = [keyword]
  
  print("Keys: ", keys)
  data = {
    "dictkey": displayname,
    "version": "v1",
    "key": keys,
    "seq": sequence,
    "value": r(replaceto),
    "info": r(info),
    "hide": hide    
  }
  
  prv_data = jsoncfg.read(
    os.path.join(DB_PATH, "keywords_list.json")
  )
  
  if overwrite:
    s = True
  elif not overwrite and not displayname in list(prv_data.keys()):
    s = True
  else:
    s = False
  
  if s and not emulate:
    prv_data[displayname] = data
    jsoncfg.write(prv_data, os.path.join(DB_PATH, "keywords_list.json"))
    return lang["success"]
  elif not s and not emulate:
    gr.Error(lang["already_found"])
  elif s and emulate:
    return "OK."
  elif not s and emulate:
    return "FAIL."
  else:
    print("listed locals: ", locals())
    raise RuntimeError("Unknown exception.")
    
    
def get_keybox(variant:Literal["manual", "update", "full"]="update") -> (list | dict):
  keyboxes = jsoncfg.read(
    os.path.join(DB_PATH, "keywords_list.json")
  )
  
  if variant == "manual":
    return list(keyboxes.keys())
  elif variant == "update":
    return gr.Dropdown.update(choices=list(keyboxes.keys()))
  elif variant == "full":
    return keyboxes
  else:
    raise ValueError('The required variable is "manual," "update," or "full."')


def use_keybox(keys:str="$WORD") -> str:
  keybox = get_keybox("full")
  
  # トリガーのリストアップ
  triggers = [] #.append tuple ([triggers], dictkey)
  trigger_keys = [] 
  for v in keybox.values():
    triggers.append((v["key"], v["dictkey"]))
  for x in triggers:
    trigger_keys.append(x[0])
  tk = trigger_keys
  trigger_keys = []
  for x in tk:
    for v in x:
      trigger_keys.append(v.upper())
  seq = keys[:1]
  if not seq in ["$", "%"]:
    raise ValueError(f"Unknown seq. seq: {seq}")
  
  key = keys.strip("$").strip("%").upper()
  dict_key = []
  if key in trigger_keys:
    for sub, dkey in triggers:
      if key in sub:
        dict_key.append(dkey)
        
  else:
    raise ValueError(f"Unknown key. key: {key}")
  
  # seq のチェック
  if len(dict_key) == 1:
    dkey = dict_key[0]
    seqs = keybox[dkey]["seq"]
    if seq in seqs:
      pass
    else:
      raise ValueError(f"Unknown key. key: {key}")
  else:
    for dkey in dict_key:
      seqs = keybox[dkey]["seq"]
      if seq in seqs:
        ok = True
        dkey = dkey
        break
    if not ok:
      raise UnboundLocalError
  
  return keybox[dkey]["value"]
      
  

def load_from_exists(target, display, keyword, sequence, prompt, info, hide, multiseq, multikey, keys):
  timer = time_takens()
  timer.start()
  
  if r(keyword) == "" or r(display) == "" or r(sequence) == "":
    pass
  else:
    print("exists data found.. ",end="")
    data = {
    "dictkey": display,
    "version": "v1",
    "key": keys,
    "seq": sequence,
    "value": r(prompt),
    "info": r(info),
    "hide": hide    
  }
    jsoncfg.write(
      data, os.path.join(
        ROOT_DIR, "logs", "template_backups", "keybox", f"{datetime.now().strftime('%Y%m%d%H%M%S')}_backupdata_key-{display}.json"
      )
    )
    print("backup complete")
  
  data = get_keybox("full")
  if not target in list(data.keys()):
    raise gr.Error("can't find keybox template.")
  
  value = data[target]
  key = data[target]["dictkey"]
  version = data[target]["version"]
  print("[Load]: Template version: ", version)
  
  # v1 method
  if version == "v1":
    name = key
    keywords = value["key"]
    seqs = value["seq"]
    
    # keyword を multikey, keyword, keys に分解
    if len(keywords) > 1:
      multikey = True
      main_key = keywords[0]
      subkeys  = ""
      for x in keywords[1:]:
        subkeys += x+"$"
      subkeys = subkeys.strip("$")
    
    else:
      multikey = False
      main_key = keywords[0]
      subkeys = ""
    
    # multiseq
    if len(seqs) > 1:
      multiseq = True
      seq = seqs[0]+"WORD"
    else:
      multiseq = False
      seq = seqs[0]+"WORD"
    if seq[:1] == "%":
      seq += "%"
    
    prompt = value["value"]
    info = value["info"]
    hide = value["hide"]
    
    return name, main_key, seq, prompt, info, hide, multiseq, multikey, subkeys, timer.resize_estimated(timer.finish())