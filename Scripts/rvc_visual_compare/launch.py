import argparse
import pkg_resources
import subprocess
import os
from modules.config_manager import config, update_session_config

def parse() -> None:
  parser = argparse.ArgumentParser("parser")
  parser.add_argument("--share", action="store_true", required=False, default=False)
  parser.add_argument("--m", required=True)
  return parser.parse_known_args()

def apply_arg_to_config(arg:argparse.Namespace) -> None:
  update_session_config(
    "_ui_share", arg.share
  )
def is_installed(pkg):
  try:
    version = pkg_resources.get_distribution(pkg).version
    return True, version
  except pkg_resources.DistributionNotFound:
    print(f"{pkg} is not installed.")
    return False, version

def main():
  args, _ = parse()
  apply_arg_to_config(args)
  
  if not config.disable_additional_inference:
    if is_installed("torch"):
      # 簡易的に torch のみを取得
      pass
    else:
      print("Installing requirements for \"Additional Inference\"")
      subprocess.run(
        ["pip3", "install", "-r", "requirements_additional_feature.txt"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        text=True
      )
    
    pass
  
  # ipynb モード
  if args.m == "ipynb":
    from ipynb import main
    main.main(".ipynb")()
    
  elif args.m == "gradio":
    # from modules import ui
    # ui.webui()("allow")
    #COMING SOON
    pass
    
main()