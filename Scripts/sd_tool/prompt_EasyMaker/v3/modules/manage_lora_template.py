from modules.generate_util import get_lora_list, control_lora_weight, lora_saver
from modules.shared import ROOT_DIR

from LGS.misc.nomore_oserror import file_extension_filter
import LGS.misc.jsonconfig as jsoncfg
import os
import re
import gradio as gr
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

def format_backup_filename(gr_update:bool=True, reverse:bool=False, target_text:str=""):
  filelist = file_extension_filter(
    os.listdir(os.path.join(
      ROOT_DIR, "logs", "template_backups", "lora"
    )), [".json"]
  )
  
  rtl = []
  
  for x in filelist:
    try:
      time = re.findall(r"(\d+)_backupdata_key-", x)[0]
      title = re.findall(r"_backupdata_key-(.*).json", x)[0]
    except IndexError:
      print(f"[Restore]: Failed Analyze File: {x}")
      continue
    
    parsed_datetime = datetime.strptime(time, '%Y%m%d%H%M%S')
    formatted_time = parsed_datetime.strftime('%Y/%m/%d %H:%M:%S\'s Data -')
    
    rtl.append(
      f"{formatted_time} {title}"
    )
    
  if not reverse:
    if gr_update:
      return gr.Dropdown.update(
        choices=rtl
      )
    return rtl

  time = re.findall(r"(.*)'s Data -", target_text)[0]
  parsed_datetime = datetime.strptime(time, "%Y/%m/%d %H:%M:%S")
  title = re.findall("'s Data - (.*)", target_text)[0]
  formatted_time = parsed_datetime.strftime('%Y%m%d%H%M%S')
  print(f"[Restore]: time: {time}\ntitle: {title}\n formatted_time: {formatted_time}")
  
  return f"{formatted_time}_backupdata_key-{title}.json"

def restore(template, after_delete, overwrite, bypass_nd, delete_only):
  filepath = os.path.join(
    ROOT_DIR, "logs", "template_backups", "lora", format_backup_filename(False, True, template)
  )
  
  data = jsoncfg.read(filepath)
  
  version = data[0]
  data = data[1]
  print("[Restore]: version found. ", version)
  
  if version == "v4":
    key = data[1]["key"]
  elif version == "v3":
    key = re.findall("_backupdata_key-(.*).json", format_backup_filename(False, True, template))[0]
  else:
    return "stderr: Unknown version.", ""
  
  status = lora_saver(
    key, "", "", "", "", False, True
  )
  
  time = re.findall(r"(.*)'s Data -", template)[0]
  lora_db = get_lora_list("full")
  
  if status != "OK.":
    dupe = True
  else:
    dupe = False
  
  if dupe:
    if not overwrite and not bypass_nd:
      return "stderr: this name was already taken.", None
    elif bypass_nd:
      key = time + "'s " + key
    elif overwrite:
      prv_data = lora_db.pop(key)
      print("[Restore]: overwrite=True.. printing previous data")
      print(f"'{key}': ", prv_data)
  
  lora_db[key] = data
  
  if delete_only:
    after_delete = True
    print("[Restore]: Catch only delete=True! printing backup data\n", f'"{key}": {data}')
  else:
    jsoncfg.write(
      lora_db, os.path.join(ROOT_DIR, "database", "v3", "lora_list.json")
    )
  if after_delete:
    os.remove(
      filepath
    )
  return "OK.", ""

def multi_restore(target_templates, delete_after, overwrite, bypass_nd, delete_only):
  total = len(target_templates)
  fail = 0
  
  for x in target_templates:
    status, _ = restore(
      x, delete_after, overwrite, bypass_nd, delete_only
    )
    
  return "Done. Status: ({total - fail} / {total})", []