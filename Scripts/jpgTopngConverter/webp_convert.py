import subprocess

def main(inputs, outputs):
  # cwebpコマンドを呼び出してPNGからWebPへの変換を行う
  subprocess.run(["cwebp", inputs, "-o", outputs])