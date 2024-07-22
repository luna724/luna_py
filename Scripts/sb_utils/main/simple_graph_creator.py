import os
from PIL import Image, ImageDraw, ImageFont
import matplotlib.figure
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

# with open("!SGC_input.txt", "r", encoding="utf-8") as f:
#   txt = f.read()

class data:
  def __init__(self, txt):
    self.output_path_found = txt.count("\n!") > 0
    
    self.x:str = None 
    self.y:str = None
    self.graph:str = None
    self.graph_values:list = None
    self.output_path:str = None
    
    self.use_meiryo: bool = True # os.name == "nt"
    
    # new variable
    self.extend: bool = False

def functional(i:data) -> Image.Image:
  # def parse_input(input: str) -> data:
  #   init = data(input)
    
  #   # Axis の取得
  #   axis = input.split("\n")[0]
  #   init.x, init.y = tuple(axis.split(r"\&"))
    
  #   # グラフタイトルの取得
  #   init.graph = input.split("\n")[1]
  #   if len(init.graph) >= 30:
  #     print("[wARN]: グラフタイトルは 30文字以下が推奨されています")
    
  #   try:
  #     if init.output_path_found:
  #       output_path = input.split("\n!")[-1]
  #     else:
  #       init.output_path = "?simple_graph_creator.py.png"
  #   except IndexError:
  #     init.output_path = "?simple_graph_creator.py.png"
    
  #   if init.output_path == None:
  #     init.output_path = output_path.strip("!")
    
  #   listln = input.split("\n")[2:]
  #   if init.output_path_found:
  #     listln = listln[:-1]
    
  #   listln = "".join(listln)
  #   init.graph_values = []
  #   for v in listln.strip("[").strip("]").split(","):
  #     v = v.strip("\n").strip()
      
  #     if v.isdigit():
  #       init.graph_values.append(int(v))
  #     else:
  #       init.graph_values.append(float(v))
    
  #   return init

  # 作成
  def create(values:list, i:data) -> Image.Image:
    """Code by GPT-4o"""
    # if i.use_meiryo:
    font_path = 'C:/Windows/Fonts/meiryo.ttc'
    font_prop = fm.FontProperties(fname=font_path)
    font = ImageFont.truetype(font_path, size=35)
    # ステップ1: グラフの作成
    fig, ax = plt.subplots()
    ax.plot(values)
    
    if i.extend:
      ax.set_xlabel(i.x, fontproperties=font_prop)
      ax.set_ylabel(i.y, fontproperties=font_prop)
      ax.set_title(i.graph, fontproperties=font_prop)
    else:
      ax.axis("off")
    
    # else:
    #   fig, ax = plt.subplots()
    #   ax.plot(values)
    #   ax.set_xlabel(i.x)
    #   ax.set_ylabel(i.y)
    #   ax.set_title(i.graph)
    
    # ステップ2: グラフを画像として保存
    fig.canvas.draw()
    width, height = fig.canvas.get_width_height()
    graph_image = Image.frombytes('RGB', (width, height), fig.canvas.tostring_rgb())
      
    plt.close(fig)
    return graph_image

  # 実行
  # i = parse_input(txt)
  return create(i.graph_values, i=i)