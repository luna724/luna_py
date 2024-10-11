import requests
import argparse
import os
import zipfile
import importlib

def argparser() -> argparse.Namespace:
  parser = argparse.ArgumentParser(__name__)
  parser.add_argument(
    "--humanize", default=False, required=False, action="store_true"
  )
  parser.add_argument(
    "--mode", required=True
  )
  parser.add_argument(
    "--is32bit", action="store_true", required=False, default=False
  )
  return parser.parse_args()

def launch(args:argparse.Namespace=None, start_dir:str=None):
  if args is None:
    raise ValueError("args is None!")

  humanize = args.humanize
  mode = args.mode
  winbit = args.is32bit
  if winbit: winbit = "32"
  else: winbit="64"
  
  if os.path.exists(os.path.join(start_dir, mode)):
    module = importlib.import_module(os.path.join(mode, "launch").replace("\\", "."))
  else:
    raise ValueError("mode not found.")
  
  # update Chrome driver
  if os.name == "nt":
    if os.path.exists(os.path.join(start_dir, "chromedriver.exe")):
      os.remove(os.path.join(start_dir, "chromedriver.exe"))
    latest_chrome_driver = requests.get("https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE").text.strip()
    chrome_driver_zip = requests.get(f"https://storage.googleapis.com/chrome-for-testing-public/{latest_chrome_driver}/win{winbit}/chromedriver-win{winbit}.zip")
    zip_file_path = os.path.join(start_dir, "chromedriver.zip")
    with open(zip_file_path, "wb") as f:
      f.write(chrome_driver_zip.content)
    
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
      zip_ref.extractall(start_dir)
    
    os.rename(os.path.join(start_dir, f"chromedriver-win{winbit}/chromedriver.exe"), os.path.join(start_dir, "chromedriver.exe"))
    os.remove(zip_file_path)
  else:
    raise RuntimeError(f"this scripts ONLY supported NT(Win64).\n(detected your enviroment: {os.name})")
  
  # 実行
  if callable(module.launch):
    return module.launch(humanize)
  else:
    raise ValueError(f"{module.launch} isn't callable.")

if __name__ == "__main__":
  launch(argparser(), os.getcwd())

ROOT_DIR = os.getcwd()
DRIVER_PATH = os.path.join(ROOT_DIR, "chromedriver.exe")
