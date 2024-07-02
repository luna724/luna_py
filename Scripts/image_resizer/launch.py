import webui
from modules import *

def launch():
  iface = webui.ui()
  
  iface.queue(64)
  iface.launch(server_port=7857, inbrowser=True)

launch()