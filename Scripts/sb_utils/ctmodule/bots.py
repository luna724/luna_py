import discord
import asyncio
import json
from discord.ext import commands
from typing import *

from main.bots import set_coin_tracker, txt2coin, convert
from ctmodule.database import value as ctm

# treas の更新
with open("db_treas.json", "r", encoding="utf-8") as f:
  db_treas = json.load(f)
  ctm.treas = {int(k): v for k, v in db_treas.items()}

def reindex_dict(d, remove_key):
  """ 辞書からキーを削除し、それ以降のキーを再インデックスする """
  # 指定されたキーを辞書から削除
  if remove_key in d:
      del d[remove_key]
  # 新しい辞書を作成して、削除したキー以降を再インデックス
  new_dict = {}
  for key in sorted(d.keys()):
      # キーが削除キーより大きい場合、1を減らす
      new_key = int(key) - 1 if int(key) > int(remove_key) else int(key)
      new_dict[new_key] = d[key]
  return new_dict

def modify_bot(bot):
  @bot.command()
  async def calcProfit(ctx, ezm:Literal["treas"]="treas", selled_value:str|None=None):
    print("command executed: calcProfit")
    # 最初の値 8つの値を取得、sell-this を行い、その後 this を消去する
    if selled_value is None:
      await ctx.send("Error: selled_value を指定してください。")
      return
    
    # selled_value に ^ がある場合は反復処理を行う
    if "^" in selled_value:
      loop = int(selled_value.split("^")[-1])
      selled_value = selled_value.split("^")[0]
    else: loop = 1
    
    first_selled = selled_value
    for x in range(loop):
      # 初期化
      selled_value = first_selled
      if ezm == "treas":
        # 最初の値が8つあるか確認。ないならば 800000 で補完する
        treas:dict = ctm("treas")
        finals:dict = treas.copy()
        
        lens = len(treas.keys())
        values = []
        for key, v in treas.items():
          if len(values) == 8:
            break
          values.append(v)
          finals = reindex_dict(finals, key)
        
        if not len(values) == 8:
          while not len(values) == 8:
            values.insert(-1, "800k") # or 800,000

        # for v in values: # V の値チェック
        #   print(f"Value: {v}, Type: {type(v)}")  # デバッグ: vの値と型を表示
        #   if not isinstance(v, str):
        #     print(f"Error: Expected string, got {type(v)} with value {v}")
        #     continue  # エラー時は次のループへ
        
        ctm.treas = finals
        # 全ての値を処理、計算する
        cost = 0
        purchased = ""
        for v in values:
          if not v.count(",") > 0:
            coins = txt2coin(v)
          else:
            # , がある場合、それらをすべて消す
            text = v.replace(",", "").replace(".", "")
            coins = int(text)
          cost += coins
          purchased += f"{convert(coins, silent=True)}, "
        purchased = purchased.strip(", ")
        
        # Fee を計算し、値を返す
        selled_value = txt2coin(selled_value)
        
        fee = selled_value * (1/100)
        profit = selled_value - fee - cost - 1200 # 1200 は 2Day での販売Fee
        # 自動で ah に計算
        with open("coins.json", "r", encoding="utf-8") as f:
          ds = json.load(f)
        ds["ah"][0] += profit
        with open("coins.json", "w", encoding="utf-8") as f:
          json.dump(ds, f)
        
        if ds["ah"][1]:
          set_coin_tracker(ds["ah"], "ah")
          await ctx.send(f"Purchased: {purchased}\nProfit: {convert(profit, silent=True)}")
          await asyncio.sleep(0.1)
          await ctx.send(f"/coin ah + {profit}")
          await asyncio.sleep(0.33)
          await ctx.send(f"OK. (with tracking) ({ds['ah'][0]})")
        else:
          await ctx.send(f"Purchased: {purchased}\nProfit: {convert(profit, silent=True)}")
          await asyncio.sleep(0.1)
          await ctx.send(f"/coin ah + {profit}")
          await asyncio.sleep(0.33)
          await ctx.send(f"OK. ({ds['ah'][0]})")
        #print(locals())
        await asyncio.sleep(0.5)
        continue
      continue
    return
  
  return bot