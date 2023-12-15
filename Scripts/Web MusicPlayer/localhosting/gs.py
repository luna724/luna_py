import argparse
import os
import json
from pydub import AudioSegment
import re
import gradio as gr
from builtins import print as bi_print

class lgs_misc_jsonconfig():
  def read(self, filepath, encode: str = "utf-8", silent=False):
    #if not silent:
       # print("Reading jsondata..")
    with open(filepath, 'r', encoding=encode) as file:
        data = json.load(file)
    return data

  def write(self, data, filepath, encode: str = "utf-8", silent=False): 
      #if not silent:
          #print("Writing config to jsondata..")
      with open(filepath, 'w', encoding=encode) as file:
          json.dump(data, file, indent=4)  # indent=4でフォーマットを整形して書き込み
      return data

  def read_text(self, filename: str, 
                  strip_mode: DeprecationWarning("") = None):
      with open(filename, 'r', encoding='utf-8') as file:
          data = file.read()
      return data

  def write_text(self, data, filepath="./out.txt", overwrite=True, encode:str = "utf-8"):
      if overwrite:
          with open(filepath, "w", encoding=encode) as f:
              f.write(data)
      
      else:
          with open(filepath, "a", encoding=encode) as f:
              f.write(data)

jsoncfg = lgs_misc_jsonconfig()

class S():
  dev = False
  noprint = False
s = S()

def print(*args, end="\n"):
  if not s.dev or s.noprint:
    return
  bi_print("[dev]: ",end="")
  for x in args:
    bi_print(x, end="")
  bi_print("",end=end)


def main():
  parser = argparse.ArgumentParser(description="parser")
  
  parser.add_argument(
    "--dev", action='store_true'
  )
  parser.add_argument(
    "--noprint", action='store_true'
  )
  parser.add_argument(
    "--ui", action='store_true'
  )
  
  args = parser.parse_args()
  
  if args.dev:
    s.dev = args.dev
  if args.noprint:
    s.noprint = args.noprint
  if args.ui:
    ui = args.ui
  else:
    ui = False
    
  if s.dev:
    ui = input("is UI? [0 / 1]: ")
    if ui == "0":
      ui = False
    elif ui == "1":
      ui = True
    else:
      ui = False
  
  db = jsoncfg.read("database.json")
  
  # 必要情報を取得
  table_basic = db["table"]
  html_lower = db["html_lower"]
  html_header = db["html_header"]
  if os.path.exists("index.html"):
    html_base = jsoncfg.read_text(
      "index.html"
    )
  else:
    html_base = html_header + html_lower
  
  jsoncfg.write_text(html_base, "index.html", True)
  
  # 追加関数
  def add(tableName, audio, overwrite=False):
    print(f"filepath: {audio}")
    audio_ = AudioSegment.from_file(audio)
    output_file = f"music/table_{tableName}.mp3"
    audio_.export(output_file, format="mp3")
    #audio_, sr = sf.read(audio)
    #sf.write(output_file, audio_, sr)
    
    html = jsoncfg.read_text("index.html")
    
    # テーブルを作成
    table = table_basic.replace(
      "%NAME%", tableName
    ).replace("%FILE%", f"music/table_{tableName}.mp3")
    
    if not overwrite:
      # lower を切り取る
      html = html.replace(html_lower, "")
      if not table in html:
        html += table
      else:
        print("this name is already taken. Skipped!")
      html += html_lower
      
    else:
      html = html.replace(html_lower, "")
      html = re.sub(rf"<tr><td>{tableName}</td>(.*)</audio></td></tr>", "", html)
      html += table
      html += html_lower
    
    # ファイルがないなら警告
    if not os.path.exists(f"music/table_{tableName}.mp3"):
      print("WARN: File Not Found! ({})".format(f"music_table_{tableName}.mp3"))
    
    jsoncfg.write_text(html, "index.html")
    
    return "Done."
  
  def get_all_audio():
    html = jsoncfg.read_text("index.html")
    
    pattern = r"<tr><td>(.*)</td><td><audio"
    allname = re.findall(pattern, html)
    
    return allname
  
  def edit(element, changeaudio, target, delete):
    if changeaudio and delete:
      return "Error: canno't input \"Change Audio\" and \"Delete element\""
    elif changeaudio:
      return add(element, target, True)
    elif delete:
      html = jsoncfg.read_text("index.html")
      
      html = re.sub(rf"<tr><td>{element}</td>(.*)</audio></td></tr>\n", "", html)
      
      jsoncfg.write_text(html, "index.html")
    
  # WebUI の構築
  if ui:
    with gr.Blocks() as iface:
      gr.Markdown("smart music player")
      with gr.Tab("Append New Audio"):
        tn = gr.Textbox(label="tableName")
        with gr.Row():
          audio = gr.Audio(source="upload", label="Input Audio", format="mp3", type="filepath")
        status = gr.Textbox(label="Status")
        run = gr.Button("Run")
        
        run.click(
          fn=add,
          inputs=[tn, audio],
          outputs=status
        )
      with gr.Tab("Edit Audio"):
        target = gr.Dropdown(choices=get_all_audio())
        
        changeFile = gr.Checkbox(label="Change Audio File", value=False)
        with gr.Accordion("changed to", open=False):
          targetaudio = gr.Audio(source="upload", label="Target Audio", format="mp3", type="filepath")
        
        deleteThis = gr.Checkbox(label="Delete element", value=False)
        
        status2 = gr.Textbox(label="Status")
        run2 = gr.Button("Run")
        run2.click(
          fn=edit,
          inputs=[target,changeFile,targetaudio,deleteThis],
          outputs=status2
        )
        
    iface.queue(64)
    iface.launch()
  
  return

if __name__ == "__main__":
  main()