# 雑処理
import argparse
import subprocess




def launch():
  def v1():
    subprocess.run("python ..\\./py/webui.py")
  def v3():
    subprocess.run("v3β.bat")
  
  parser = argparse.ArgumentParser()
  parser.add_argument("--version")
  args = parser.parse_args()
  if args.version:
    v = args.version
  else:
    v = "v3"
  verdict = {
  "v1": v1,
  "v3": v3
}
  verdict[v]()
  
  return

if __name__ == "__main__":
  launch()