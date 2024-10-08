import sys

import _directory_tagging

if not __name__ == "__main__":
  raise ValueError("_launch aren't Importable!")

def run():
  args = sys.argv[1:]

  if len(args) == 0:
    raise ValueError("args not enough")

  if args[0] == "help":
    print("lunapy_dsu {mode} {modes_arg}")
    return
  
  if args[0] == "directory_tagging":
    print(f"Called: directory_tagging.py with arguments: {args}")
    _directory_tagging.call(args)
 
run()