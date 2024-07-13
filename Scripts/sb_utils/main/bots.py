import discord
from discord.ext import commands
from typing import *
import json, os

def convert(v:float) -> str:
    """ 
    Convert integer to text (e.g. 200,000,000 -> 200M)
    Max: B (1000000000)
        Min: K (1000)
    """
    print(f"[Convert]: Input: {v}")
    def under_one(v) -> int:
        if v < 1:
            return 0
        else:
            return int(v)
    
    b = v / 1000000000
    m = v / 1000000
    k = v / 1000
    last = v - k*1000
    
    b = under_one(b)
    m = under_one(m)
    k = under_one(k)
    print(f"[Convert]: first value: b: {b} m: {m} k: {k} last: {last}")
    # b, m, k を上にあるものを引いていく
    m = m - (b*1000)
    k = k - (m*1000)
    
    text = ""
    if b != 0:
        text = f"{b}B"
        if m != 0:
            text += f".{int(m)}"
        text += "B"
        
    elif m != 0:
        text = f"{m}"
        if k != 0:
            text += f".{int(k)}"
        text += "M"
        
    elif k != 0:
        text = f"{k}"
        if last != 0:
            text += f".{int(last)}"
        text += "K"
    else:
        text = f"{last}coin"

    return text

def txt2coin(x) -> int | float:
    x:str = x.lower()
    trigger = x[-1]
    x = x[:-1]
    
    if trigger == "k":
        multiplier = 1000
    elif trigger == "m":
        multiplier = 1000000
    elif trigger == "b":
        multiplier = 1000000000
    else:
        multiplier = 1
    
    if "." in x:
        x = float(x)
    else:
        x = int(x)
    
    return x * multiplier

def bz_to_npc_profit_calculator(x: float, y: int, z: float, d: bool = True) -> Tuple[float, float, int]:
    """ 購入と売却から利益、利益率、売却にかかる日数を計算する関数 """
    buy = x * y  # 購入総額
    sell = z * y  # 売却総額
    profit = sell - buy  # 利益

    # 利益率の計算。購入額が0ではないことを確認
    if buy != 0:
        profit_percentage = (profit / buy) * 100
    else:
        profit_percentage = 0  # 購入額が0の場合、利益率も0とする

    # 売れるまでの日数の計算
    if d:
        npc_daily_limit = 10000000  # NPCが1日に買い取れる上限額を仮定
    else:
        npc_daily_limit = 200000000
    sellable_days = int(z / npc_daily_limit)

    return profit, profit_percentage, sellable_days

# ボットのセットアップ
def modify_bot(bot):
    print("Registering commands..")
    @bot.command()
    async def simple_flip(ctx, buyed_price: float, purchase_count: int, selling_price: float, low_limit: Literal["LowLimit", ""] = ""):
        print("Command executed (simple_flip)")
        
        if low_limit == "LowLimit": low_limit = True
        else: low_limit = False
        
        profit, profit_percentage, sellable_days = bz_to_npc_profit_calculator(buyed_price, purchase_count, selling_price, low_limit)
        await ctx.send(f"- Cost: {convert(buyed_price * purchase_count)}\n- Profit: {convert(profit)} ({profit_percentage:.2f}%)\n> days required for sale(NPC): {sellable_days}d")

    @bot.command()
    async def ram(ctx, k:str, v:str, calc: Literal["append", "subtract", "+", "-"]=None, f="ram"):
        print("command executed (ram)")
        via_f = f
        if not os.path.exists(f"{via_f}.json"):
            with open(f"{via_f}.json", "w", encoding="utf-8") as f: json.dump({"__init__": [None]}, f)
        
        with open(f"{via_f}.json", mode="r", encoding="utf-8") as f:    
            ds = json.load(f)
        
        if k in ds.keys():
            await ctx.send(f"This Keys Already Defined.")
        
        if calc is not None:
            v = float(v)
            current = float(ds[k][0])
            
            if calc == "append" or calc == "+":
                ds[k][0] = current + v
            elif calc == "subtract" or calc == "-":
                ds[k][0] = current - v
            
            await ctx.send(f"Calculated. ({ds[k]})")        
        else:
            if k in ds.keys():
                ds[k].append(v)
            else:
                ds[k] = [v]
        
        with open(f"{via_f}.json", "w", encoding="utf-8") as f:
            json.dump(ds, f, indent=2)
            await ctx.send("OK.")
        print("Done. (ram)")
        
    @bot.command()
    async def load(ctx, k:str, f="ram"):
        print("command executed (load)")
        via_f = f
        with open(f"{via_f}.json", mode="r", encoding="utf-8") as f:
            ds = json.load(f)
        if os.path.exists(f"{via_f}!memo.json"):
            with open(f"{via_f}!memo.json", "r", encoding="utf-8") as f:
                memo = json.load(f)
            try:
                memo = memo[k]
            except KeyError:
                memo = None
        else:
            memo = None
        
        if k == "__show_all__":
            await ctx.send(f"All values\n```{ds}\n```")
            return
            
        if not k in ds.keys():
            await ctx.send(f"Err: that keys not defined.")
        else:
            text = f"{k}'s value\n```"
            vs = ds[k]
            for i, x in enumerate(vs):
                text += f"{i + 1}. {x}\n"
            text += "```"
            
            if memo is not None:
                text += f"\nMemo: {memo}"
            
            await ctx.send(f"{text}")

    @bot.command()
    async def ram_note(ctx, k:str, m:str, f="ram"):
        print("command executed (ram_note)")
        via_f = f
        with open(f"{via_f}.json", mode="r", encoding="utf-8") as f:
            ds = json.load(f)
        

        if not os.path.exists(f"{via_f}!memo.json"):
            with open(f"{via_f}!memo.json", "w", encoding="utf-8") as f: json.dump({"__init__": "Variable for RAM initialize"}, f)
        
        with open(f"{via_f}!memo.json", "r", encoding="utf-8") as f:
            memo = json.load(f)

        if k in memo.keys():
            ctx.send(f"Previous Memo: {memo[k]}")
        
        memo[k] = m
        
        with open(f"{via_f}!memo.json", "w", encoding="utf-8") as f:
            json.dump(memo, f)
        await ctx.send("OK.")

    @bot.command()
    async def coin(ctx, k:str, s:str, v:str):
        print("command executed (coin)")
        with open("coins.json", "r", encoding="utf-8") as f:
            ds = json.load(f)
        
        v = txt2coin(v)
        if s == "-":
            v *= -1
            
        if not k in ds.keys():
            ds[k] = 0
            
        ds[k] += v
        
        with open("coins.json", "w", encoding="utf-8") as f:
            json.dump(ds, f)
        await ctx.send(f"OK. ({ds[k]})")
    
    @bot.command()
    async def coin_load(ctx, k:str):
        print("command executed (coin_load)")
        with open("coins.json", "r", encoding="utf-8") as f:
            ds = json.load(f)
        with open("coins!memo.json", "r", encoding="utf-8") as f:
            memo = json.load(f)
        
        try:
            m = memo[k]
        except Exception:
            m = None
        
        text = f"{k}'s Value\n```"
        text += f"{convert(ds[k])}```\nMemo: {m}"
        await ctx.send(text)
    
    @bot.command()
    async def coin_note(ctx, k:str, v:str):
        print("command executed (coin_note)")
        with open("coins!memo.json", "r", encoding="utf-8") as f:
            ds = json.load(f)
        ds[k] = v
        with open("coins!memo.json", "r", encoding="utf-8") as f:
            json.dump(ds, f)
        
        await ctx.send("OK.")
    return bot
