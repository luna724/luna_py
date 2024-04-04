from flask import Flask, jsonify, request
from typing import Literal
import os
import gradio as gr
from datetime import datetime
import pyperclip
import LGS.misc.jsonconfig as jsoncfg

from modules.shared import ROOT_DIR, language

def get_basic() -> str:
  return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <a href="/apply"> apply changes </a>
    <title>Sortable List</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Sortable/1.14.0/Sortable.min.js"></script>
    <style>
        #sortable-list {
            list-style-type: none;
            padding: 0;
            margin: 0;
        }
        #sortable-list li {
            border: 1px solid #ccc;
            margin: 5px 0;
            padding: 10px;
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <h2>Sortable List</h2>
    <ul id="sortable-list">
        $LI
    </ul>
    <script>
        var sortableList = document.getElementById('sortable-list');

        new Sortable(sortableList, {
          animation: 200,
          scroll: true,
          scrollSensitivity: 25,
          scrollSpeed: 10,
            onEnd: function (evt) {
                var items = sortableList.getElementsByTagName("li");
                var keyData = {};

                for (var i = 0; i < items.length; i++) {
                    var text = items[i].innerText;
                    keyData[text] = i; // アイテムのテキストをキーにし、インデックスを値に設定
                }

                // Ajaxリクエストを作成し、Pythonにデータを送信
                fetch('/key_data', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ keyData: keyData }) // JSON形式でデータを送信
                })
                    .then(response => {
                        // サーバーからの応答を処理
                        console.log('Key data sent to server successfully');
                    })
                    .catch(error => {
                        console.error('Error sending key data to server:', error);
                    });
            }
        });
    </script>
</body>
</html>"""

def get_keys(mode=None, rtl_dict=False) -> str:
  if mode == "prompt_template":
    fp = "template_list.json"
    port = 7858
  elif mode == "lora_template":
    fp = "lora_list.json"
    port = 7859
  elif mode == "keybox_template":
    fp = "keywords_list.json"
    port = 7857
  else:
    raise UnboundLocalError("mode is not defined in modules.sorting.py:start_sorting(mode)")
  
  if rtl_dict:
    return os.path.join(ROOT_DIR, "database", "v3", fp)
  
  base = ""
  for k in jsoncfg.read(os.path.join(ROOT_DIR, "database", "v3", fp)):
    base += f"<li> {k} </li>\n"
  return base.strip("\n"), port

def start_sorting(mode:Literal["prompt_template", "lora_template", "keybox_template"]="lora_template"):
  class variable:
    recent_data:dict = {}
    def __init__(self, v=None):
      self.variable = v
    def __call__(self):
      return self.variable
    def update(self, v=None):
      self.variable = v
    
    share = {
      
    }
    
    
  def finalize():
    data = variable.recent_data
    if data == {}:
      return "LeastOne"
    
    print("Finalized!")
  
    # data をソート
    sorted_data = [
      x[0] for x in sorted(data.items(), key= lambda x: x[1])
    ]
    print("sorted_data: ", sorted_data)
    
    # それをもとにテンプレートを操作する
    path = get_keys(mode, True)
    template = jsoncfg.read(path)
    new = {}
    
    # キーの順番を sorted_data の順番と同期
    if not len(sorted_data) == len(template.keys()):
      print("Keycount was not matched. raise ParseError")
      variable.share["KC_wasn't_matched"] = variable(f"sorted_data: {len(sorted_data)} | template_keys: {len(template.keys())}")
      return "ParseError"
    
    for key in sorted_data:
      values = None
      # ソート順に設定
      for k, v in template.items():
        k = k.strip() ### #Issue11 [重要] sorted_list の値に .strip() と同じ動作がどこかで掛けられているせいでテンプレートの名前の両端に空白がある場合、問題が発生する。 部分の一時解決コード
        if key == k:
          values = v
      
      if values is not None:
        new[key] = values
      else:
        print(f"key wasn't matched ({key}). raise ParseError")
        variable.share["KC_wasn't_matched"] = variable(f"sorted_data: {sorted_data} | template_keys: {template.keys()}")
        return "ParseError"

    jsoncfg.write(new, path)
    return True
  
  lang = language("/ui/mt_child/sort.py", "raw")["system"]
  btn = gr.Button.update(visible=True)
  yield lang["starting"], btn
  _, port = get_keys(mode)

  app = Flask("lunapy SD-PEM"+lang["title"]+f" ({mode})")
  @app.route("/")
  def i():    
    keys, _ = get_keys(mode)
    html = get_basic().replace("$LI",keys)
    return html
  
  @app.route("/key_data", methods=["POST"])
  def receive():
    key = request.json.get("keyData")
    print("Received data. Waiting for finalizing")
    variable.recent_data = key
    return jsonify({'message': 'Key data received successfully'})
    
  @app.route('/apply')
  def apply():
    lang = language("/ui/mt_child/sort.py", "raw")["system"]
    finalized = finalize()
    if not finalized == True:
      if finalized == "LeastOne":
        return lang["at_least_one"]
      elif finalized == "ParseError":
        return lang["parse_error"].format(variable.share["KC_wasn't_matched"]())
      else:
        return lang["all_fail"]
    return lang["full_success"]
  
  print("previous Copied item: "+pyperclip.paste())
  pyperclip.copy(f"localhost:{port}")

  yield lang["start_success"].replace("localhost:7859", f"localhost:{port}"), btn
  app.run(port=port)
  