from argparse import ArgumentParser, Namespace
import os
import importlib
import requests
import zipfile
import json
from typing import Tuple

metadata_example = {
  "require_chromedriver": False
}

def launch(m) -> Tuple[Namespace, bool]:
  parser = ArgumentParser("main")
  
  parser.add_argument(
    "--api", action="store_true", default=False, required=False
  )
  parser.add_argument(
    "--webui", action="store_true", default=True, required=False
  )
  parser.add_argument(
    "--m", "-m", "--mode", required=False, default=None
  )
  
  if os.path.exists(
    os.path.join(
      os.getcwd(), m, "api.py"
    )
  ):
    # module/api.py がある場合、APIモードを有効化
    module_api = importlib.import_module(f"{m}.api")
    if callable(module_api.parse):
      module_api.parse(parser)
    
    API_runner = True
  
  else:
    API_runner = False
    print(f"can't detected api.py in selected module ({m}).\nrunning without API runner..")
  
  if os.path.exists(
    os.path.join(
      os.getcwd(), m, "launch.py"
    )
  ):
    # module/launch.py がある場合、その中の launch 関数を実行。
    # 引数には launch() が返す Namespace を渡す
    if callable(importlib.import_module(f"{m}.launch").launch):
      return (parser.parse_args(), API_runner)
  
  raise RuntimeError("can't detected launch.py in selected module.")

def main():
  p = ArgumentParser("prld")
  p.add_argument("--m", "-m", "--mode", required=True)
  p, _ = p.parse_known_args()
  mode = p.m
  
  parsed_args, API_accessable = launch(mode)
  if os.path.exists(os.path.join(mode, "metadata.json")):
    with open(os.path.join(mode, "metadata.json"), "r", encoding="utf-8") as f:
      metadata = json.load(f)
  else:
    print(f"can't detected metadata.json in selected module ({mode}).\nrunning with default metadata.json..")
    metadata = metadata_example
  
  if metadata["require_chromedriver"]:
    print("Downloading Chromedriver..")
    
    # auto download chrome driver
    start_dir = os.getcwd()
    if os.path.exists(os.path.join(start_dir, "chromedriver.exe")):
      os.remove(os.path.join(start_dir, "chromedriver.exe"))
    latest_chrome_driver = requests.get("https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE").text.strip()
    chrome_driver_path = f"https://storage.googleapis.com/chrome-for-testing-public/{latest_chrome_driver}"
    # プラットフォームを検出
    os_name = os.name
    if os_name == "nt":
      pf = "win{}"
      import platform
      bit = platform.architecture()[0].replace("bit", "")
      pf = pf.format(bit)
      ext = ".exe"
      
    elif os_name == "posix":
      pf = "linux64" 
      ext = ""
    
    else:
      pf = "mac-x64"
      ext = ""
    
    chrome_driver_path += f"/{pf}/chromedriver-{pf}.zip"
    chrome_driver_zip = requests.get(chrome_driver_path)
    zip_file_path = os.path.join(start_dir, f"chromedriver.zip")
    with open(zip_file_path, "wb") as f:
      f.write(chrome_driver_zip.content)
  
    print("zip_file_Path", zip_file_path) 
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
      zip_ref.extractall(start_dir)
    
    os.rename(os.path.join(start_dir, f"chromedriver-{pf}/chromedriver{ext}"), os.path.join(start_dir, f"chromedriver{ext}"))
    os.remove(zip_file_path)
  
  API_mode = parsed_args.api and API_accessable
  print(importlib.import_module(f"{mode}.launch").launch(parsed_args, api_mode=API_mode))

main()