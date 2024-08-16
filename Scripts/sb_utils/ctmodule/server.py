from aiohttp import web
import ctmodule.database as dates
import main.bots as bots

import json
from typing import *

def server_path() -> str:
  return "/receive_data"

def server_func(app: web.Application):
  # CT Module からの POST を受け取る
  async def parse_post(request):
    try:
      data = await request.json()  # 非同期でJSONデータを取得
      print("Received data:", data)
      
      if data["mode"] == "treas":
        # treas モードに値を設定
        current = dates.value.treas
        lens = len(current.keys())
        
        dates.value.treas[lens+1] = data["value"]
        #print("current_treas value: ", dates.value.treas)
        # e.g. {1: "100,000"}
        
      return web.json_response({'status': 'success', 'message': 'Data processed successfully'}, status=200)
    except json.JSONDecodeError as e:
      return web.json_response({'status': 'error', 'message': 'Invalid JSON data'}, status=400)

  app.router.add_post("/receive_data", parse_post)
  
  
  async def flip_tracker(request):
    try:
      data = await request.json()
      print("Received data:", data)
      
      if data["command"] is not None:
        post = data["command"]
        key:str = data["key"] # /coin コマンドを処理
        subst:Literal["-", "+"] = data["subst"]
        # スクリプト的呼び出しなので "-" or "+" 
        price:str = data["value"].replace(",", "")
        # jsonように str に変換されるだけなので float() で変換可能
        
        # コマンド呼び出し
        def get_stdout(*arg, **kw):
          return "".join(arg)
          
        myctx = bots.via_ctx(get_stdout)
        await bots.coin_main(myctx, key, subst, price)
        
        stdout = myctx.get_return()
        if stdout is not None: stdout = f"Response: {stdout}"
        else: stdout = "Response: None, hmm, bot's broken?"
        
      return web.json_response({'status': 'success', 'message': stdout}, status=200)
    except json.JSONDecodeError as e:
      return web.json_response({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
  app.router.add_post("/flip_tracker", flip_tracker)