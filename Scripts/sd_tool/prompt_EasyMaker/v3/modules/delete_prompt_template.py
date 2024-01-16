from LGS.misc.jsonconfig import write
from modules.generate import get_template
from modules.shared import ROOT_DIR

from datetime import datetime

import os

def delete_selected(template_key):
  # template を取得してバックアップ
  template = get_template("full")
  
  try:
    _ = template[template_key]
  except KeyError:
    return f"Cannot find template. try refresh template's dropdown"
  
  # backup
  backup_dict = template[template_key]
  # 保存して消す
  write(backup_dict, os.path.join(ROOT_DIR, "logs", "template_backups", "prompt", f"{datetime.now().strftime('%Y%m%d%H%M%S')}_backupdata_key-{template_key}.json")
  del template[template_key]
  return "OK."

def restore_selected():
  return