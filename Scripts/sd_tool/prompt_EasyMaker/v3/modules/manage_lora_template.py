from modules.generate_util import get_lora_list, control_lora_weight, lora_saver
from modules.shared import ROOT_DIR


import LGS.misc.jsonconfig as jsoncfg
import os
from datetime import datetime

def load(
  target, dn, l, n, p, e
):
  if not dn == "" or dn == None:
    lora_dict = {
      dn: [
        "v3",
        {
          "lora": l,
          "name": n,
          "prompt": p,
          "extend": e
        }
      ]
    }
    print("[Load]: entered data found. printing entered data..")
    print(lora_dict)
  
  lora = get_lora_list("full")
  
  if not lora_saver(target, "", "", "", "", False) == "stderr: this name is already taken.":
    print("[Load]: catch Exception")
    # target を削除する機構 (OK. が返ってくるため保存に成功している)
    
    return "stderr: can't found lora template data"
  
  data = lora[target][1]
  ver = lora[target][0]
  print("[Load]: Template version: ", ver)
  
  return "OK.", target, data["lora"], data["name"], data["prompt"], data["extend"]

def save(dname, lora, name, prompt, extend, overwrite):
  if dname == "" or dname == None:
    return "please enter displayName"
  
  lora = control_lora_weight(lora, 1.0)
  
  return lora_saver(dname, lora, name, prompt, extend, overwrite)


def delete(template, backup):
  loras: dict= get_lora_list("full")
  
  try:
    template_key = loras[template]
  except KeyError:
    return f"Cannot find template. try refresh template's dropdown", ""
  
  backup_dict = loras[template]
  
  if backup:
    jsoncfg.write(
      backup_dict, os.path.join(
        ROOT_DIR, "logs", "template_backups", "lora", f"{datetime.now().strftime('%Y%m%d%H%M%S')}_backupdata_key-{template}.json"
      )
    )
  else:
    print("[Delete]: catch backup=False  printing backup data..")
    print(backup_dict)
  
  loras.pop(template)
  jsoncfg.write(
    loras, os.path.join(
      ROOT_DIR, "database", "v3", "lora_list.json"
    )
  )
  return "OK.", ""

def multi_delete(templates, backup):
  total = len(templates)
  fail = 0
  
  for x in templates:
    status, _ = delete(x, backup)
    if status != "OK.":
      fail += 1
      print("[Delete]: Failed to Delete: ", x, "\nStatus: ", status)
  
  return f"Done. Status: ({total - fail} / {total})", []