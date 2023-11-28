from flask import Flask
from LGS.misc.jsonconfig import read as read_json
from LGS.misc.jsonconfig import read_text
import os


def lprint(*args: str, end: str ="\n"):
  print("[lunapy]: ", end="")
  
  for arg in args:
    print(arg, end="")
  
  if end:
    print(" ", end=end)
    
class Sharing():
  ROOT_PATH = os.getcwd()
  
  
share = Sharing()



app = Flask("lunapy_docs.py")

@app.route('/')
def index():
  return read_text(os.path.join(share.ROOT_PATH, "html", "index.html"), False)

@app.route('/module/')
def module_root():
  base = read_text(os.path.join(share.ROOT_PATH, "html", "module", "root.html"))

  module_list_raw = read_text(os.path.join(share.ROOT_PATH, "html", "module", ""))
  

if __name__ == '__main__':
  app.run(debug=True)