import os
from PIL import Image, ImageDraw, ImageFont
import matplotlib.figure
import matplotlib.pyplot as plt

with open("!SGC_input.txt", "r", encoding="utf-8") as f:
  txt = f.read()

class data:
  def __init__(self, txt):
    self.output_path_found = txt.count("\n!") > 0
    
    self.x:str = None 
    self.y:str = None
    self.graph:str = None
    self.graph_values:list = None
    self.output_path:str = None

  def __call__(self) -> str:
    # Check output path
    if self.output_path.startswith("?"):
      self.output_path = os.path.join(os.getcwd(), self.output_path.strip("?"))
    else:
      self.output_path = os.path.realpath(self.output_path)
    
    if os.path.isdir(self.output_path):
      if not os.path.exists(os.path.join(self.output_path, "simple_graph_creator.py.png")):
        self.output_path = os.path.join(self.output_path, "simple_graph_creator.py.png")
    
    if not os.path.splitext(self.output_path)[1] == ".png":
      print("[WARN]: 出力パスは png 拡張子である必要があります。")
      self.output_path += ".png"
    
    return self.output_path
    
def parse_input(input: str) -> data:
  init = data(input)
  
  # Axis の取得
  axis = input.split("\n")[0]
  init.x, init.y = tuple(axis.split(r"\&"))
  
  # グラフタイトルの取得
  init.graph = input.split("\n")[1]
  if len(init.graph) >= 30:
    print("[wARN]: グラフタイトルは 30文字以下が推奨されています")
  
  try:
    if init.output_path_found:
      output_path = input.split("\n!")[-1]
    else:
      init.output_path = "?simple_graph_creator.py.png"
  except IndexError:
    init.output_path = "?simple_graph_creator.py.png"
  
  if init.output_path == None:
    init.output_path = output_path.strip("!")
  
  listln = input.split("\n")[2:]
  if init.output_path_found:
    listln = listln[:-1]
  
  listln = "".join(listln)
  init.graph_values = []
  for v in listln.strip("[").strip("]").split(","):
    v = v.strip("\n").strip()
    
    if v.isdigit():
      init.graph_values.append(int(v))
    else:
      init.graph_values.append(float(v))
  
  return init

# 作成
def create(values:list, i:data) -> Image.Image:
  """Code by GPT-4o"""
  # ステップ1: グラフの作成
  fig, ax = plt.subplots()
  ax.plot(values)
  plt.xlabel(i.x)
  plt.ylabel(i.y)
  
  # ステップ2: グラフを画像として保存
  fig.canvas.draw()
  width, height = fig.canvas.get_width_height()
  graph_image = Image.frombytes('RGB', (width, height), fig.canvas.tostring_rgb())
  
  # ステップ3: 画像の高さを増やしてリスト情報を書き込む
  new_height = height + 75  # 情報を書くために高さを50ピクセル増やす
  new_image = Image.new('RGB', (width, new_height), (255, 255, 255))
  new_image.paste(graph_image, (0, 0))
  
  # フォントと描画オブジェクトの作成
  draw = ImageDraw.Draw(new_image)
  font = ImageFont.load_default()
  
  # リスト情報を書き込む
  info_text = i.graph
  text_bbox = draw.textbbox((0, 0), info_text, font=font)
  text_width, _ = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
  text_x = (width - text_width) // 2  # 中央に配置
  text_y = height + 50  # グラフの下に配置
  draw.text((text_x, text_y), info_text, fill=(0, 0, 0), font=font)
  
  plt.close(fig)
  return new_image

# 実行
i = parse_input(txt)
create(i.graph_values, i=i).save(i())