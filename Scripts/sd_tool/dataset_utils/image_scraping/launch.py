from argparse import Namespace

from image_scraping.webui import ui
from image_scraping.func import run

def launch(args:Namespace, api_mode:bool=False, **kwargs) -> None:
  if args.webui:
    ui(args)
  
  if api_mode:
    run(
      
    )