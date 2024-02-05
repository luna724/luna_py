from LGS.misc.jsonconfig import write as json_write
from LGS.misc.jsonconfig import read as json_read
from LGS.misc.nomore_oserror import file_extension_filter, get_nested_files

import modules.shared as shared
from modules.generate import get_template, get_template_value
from modules.make_prompt_template import BASIC
from modules.shared import ROOT_DIR

from datetime import datetime
import gradio as gr
import os
import re

def delete_selected(template_key, backup):
  # template を取得してバックアップ
  template :dict= get_template("full")
  
  try:
    template_key = get_template_value(template_key, rtl_resized_name=True)
  except KeyError:
    return f"Cannot find template. try refresh template's dropdown", ""
  except ValueError:
    return f"Cannot find template. try refresh template's dropdown", ""
  
  # backup
  backup_dict = template[template_key]
  # 保存して消す
  
  if backup:
    json_write(backup_dict, os.path.join(ROOT_DIR, "logs", "template_backups", "prompt", f"{datetime.now().strftime('%Y%m%d%H%M%S')}_backupdata_key-{template_key}.json"))
  else:
    print("[Delete]: catch backup=False  printing backup data...")
    print(backup_dict)
    
  template.pop(template_key)
  json_write(template, os.path.join(ROOT_DIR, "database", "v3", "template_list.json"))
  return "OK.", ""

def delete_multi(template_keys, backup):
  total = len(template_keys)
  fail = 0
  
  for x in template_keys:
    status, _ = delete_selected(x, backup)
    if status != "OK.":
      fail += 1
      print("[Delete]: Failed to Delete: ", x, "\nStatus: ", status)
  
  return f"Done. Status: ({total - fail} / {total})", []

def format_backup_filename(formatted_to_filename=False, target_text="", gr_update=True):
  filelist = file_extension_filter(
    os.listdir(os.path.join(
      ROOT_DIR, "logs", "template_backups", "prompt"
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
    
  if not formatted_to_filename:
    if gr_update:
      return gr.Dropdown.update(
        choices=rtl
      )
    return rtl
  
  time = re.findall(r"(.*)'s Data -", target_text)[0]
  parsed_datetime = datetime.strptime(time, '%Y/%m/%d %H:%M:%S')
  title = re.findall("'s Data - (.*)", target_text)[0]
  formatted_time = parsed_datetime.strftime('%Y%m%d%H%M%S')
  print(f"[Restore]: time: {time}\ntitle: {title}\n formatted_time: {formatted_time}")
  
  return f"{formatted_time}_backupdata_key-{title}.json"

def restore_selected(target_template, delete_after_restored, advanced_mode, overwrite, bypass_name_dupe, restore_from_filepath, filepath, only_delete):
  """
      advanced_mode : Beta Argument
  """
  
  print(f"[Restore]: target_template: {target_template}")
  print(f'[Restore]: Path: {os.path.join(ROOT_DIR, "logs", "template_backups", "prompt", format_backup_filename(True, target_template))}')
  
  if not restore_from_filepath:
    filepath = os.path.join(ROOT_DIR, "logs", "template_backups", "prompt", 
                  format_backup_filename(True, target_template))
  
  if not os.path.exists(filepath):
    return "Failed Restore. File not found.", ""

  data = json_read(filepath)
  if advanced_mode:
    # 元の値を優先してアプデ
    datas = BASIC
    datas.update(data)
    data = datas
    
    # 一部 shared から取得
    data["Method"] = shared.currently_version 
    data["Method_Release"] = shared.currently_template_versionID
    
  version = data["Method"]
  releaseid = data["Method_Release"]
  print(f"[Restore]: version data found. {version} - {releaseid}")
  
  # 情報の取得
  time = re.findall(r"(.*)'s Data -", target_template)[0]
  template = get_template("full")
  
  if data["Key"] in get_template("manual") and not overwrite and not bypass_name_dupe:
    return "Error: this name is already taken. try use \"overwrite\" or \"bypass name dupe\".", ""
  elif data["Key"] in get_template("manual") and overwrite and not bypass_name_dupe:
    backup = template.pop(data["Key"])
  elif data["Key"] in get_template("manual") and bypass_name_dupe:
    data["Key"] == f"{data['Key']}_{time}"
    data["displayName"] == f"{time}'s {data['displayName']}"
  template[data["Key"]] = data
  
  if only_delete:
    delete_after_restored = True
    print("[Restore]: Catch only delete=True! printing backup data\n", f'"{data["Key"]}": {data}')
  else:
      json_write(
    template, os.path.join(ROOT_DIR, "database", "v3", "template_list.json")
      )
  if delete_after_restored:
    os.remove(
      filepath
    )
  return "OK.", ""

def restore_multi(target_templates, delete_after, advanced, overwrite, bypass_nd, only_delete):
  total = len(target_templates)
  fail = 0
  
  for x in target_templates:
    status, _ = restore_selected(
      x, delete_after, advanced, overwrite, bypass_nd, False, "", only_delete
    )
    if not status != "OK.":
      fail += 1
      print("Failed to Restore: ", x, "\nStatus: ", status)
  
  return f"Done. Status: ({total - fail} / {total})", []