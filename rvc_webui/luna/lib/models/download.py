### Using Aria2c
import subprocess
import os
from luna.modules.utils import jsoncfg
from modules.shared import ROOT_DIR

def download_file(
  url: str,
  out_dir: str,
  out_file: str,
  max_connection: int = 12,
  min_split_size: str = "1M",
  error_level: str = "error"
):
  cmd = f"aria2c --console-log-level={error_level} -c -x {max_connection} -s {max_connection} -k {min_split_size} {url} -d {out_dir} -o {out_file}"
  
  try:
    subprocess.run(cmd, shell=True, check=True)
  except subprocess.CalledProcessError as e:
    print("Error running Aria2 command:", e)

def download_model():
  model_data = jsoncfg.read("./luna/configs/model_config.json")

  for value in model_data.value():
    if value["MODEL"] == "model_name":
      continue
    
    output_dir = ROOT_DIR
    
    for x in value["PATH"]:
      output_dir = os.path.join(output_dir, x)
    
    # インストール
    os.makedirs(output_dir, exist_ok=True)
    
    download_file(
      url=value["URL"],
      out_dir=output_dir,
      out_file=value["MODEL"],
      max_connection=16,
      min_split_size="1M",
      error_level="error"
    )