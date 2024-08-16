import discord
from discord.ext import commands
from typing import *
from PIL import Image
import json, os, time, numpy as np, io, random, string

from main.util import via_ctx
from main.simple_graph_creator import functional as sgc, data as sgc_data

def convert(v:float, **kw) -> str:
    """ 
    Convert integer to text (e.g. 200,000,000 -> 200M)
    Max: B (1000000000)
        Min: K (1000)
    """
    if isinstance(v, int):
        v = float(v)
    dic = False
    
    # print(f"[Convert]: Input: {v}")
    def under_one(v) -> int:
        if v < 1:
            return 0
        else:
            return int(v)
    
    if str(v).startswith("-"):
        dic = True
        v *= -1
    
    b = v / 1000000000
    m = v / 1000000
    k = v / 1000
    last = v - k*1000
    
    b = under_one(b)
    m = under_one(m)
    k = under_one(k)
    # print(f"[Convert]: first value: b: {b} m: {m} k: {k} last: {last}")
    # b, m, k を上にあるものを引いていく
    m = m - (b*1000)
    k = k - (m*1000)
    
    text = ""
    if b != 0:
        text = f"{b}"
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
    
    if dic: text = "-"+text
    
    return text

def txt2coin(x) -> int | float:
    x:str = x.lower()
    trigger = x[-1]
    if trigger.isdigit():
        multiplier = 1
    else:
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
   
def get_up_percentage(prv: float, new: float) -> str:
    """floatは .01d"""
    # 増減率の計算
    if prv != 0:
        profit_percentage = ((new-prv) / prv) * 100
        if profit_percentage < 0: dig = "" 
        else: dig = "+"
        profit_percentage = f"{dig}{profit_percentage:.1f}%"
    else:
        profit_percentage = "+∞"
    return profit_percentage
    
def remove_zero_dot(v:int | float | str) -> (float | int):
    def ret(v):
        if v.count(".") > 0:
            return float(v)
        else:
            return int(v)
    v = str(v)
    if not v.count(".") > 0:
        return ret(v)
    if not v.endswith("0"):
        return ret(v)
    if len(v.split(".")[1]) > 1:
        while v.endswith("0"):
            v = v[:-1]
        return ret(v)
    else:
        return ret(v.split(".")[0])

def set_coin_tracker(v:list, k:str):
    current = v[0]
    with open("coin_tracker.json", "r", encoding="utf-8") as f:
        tracker = json.load(f)
    
    try:
        track = tracker[k]
    except KeyError:
        track = [0]
    
    track.append(v[0])
    tracker[k] = track
    with open("coin_tracker.json", "w", encoding="utf-8") as f:
        json.dump(tracker, f)

async def coin_main(ctx, k, s, v):
    with open("coins.json", "r", encoding="utf-8") as f:
        ds = json.load(f)
    
    if k == "__tracker__" or k == "$track":
        if s in ds.keys():
            ds[s][1] = not ds[s][1]
            value = ds[s][1]
            if value:
                await ctx.send(f"{s} values tracking started.")
            else:
                await ctx.send(f"{s} values tracking stopped.")

            with open("coins.json", "w", encoding="utf-8") as f:
                json.dump(ds, f)
        
        else:
            await ctx.send(f"[stderr]: {s}: Unknown key")
            return

    else:   
        if not k in ds.keys():
            ds[k] = [0, False]
        
        if not s in ["-", "+"]:
            # 解析しようとする
            legacy_s = s
            if legacy_s.startswith("-"):
                s = "-"
            else:
                if legacy_s[0].isdigit() or legacy_s.startswith("+"):
                    s = "+"
                else:
                    await ctx.send("入力された値が正しくありません")
            v = legacy_s[1:]
            # print("legacy_s & v: ", legacy_s, ", ", v)
        
        v = txt2coin(v)
        if s == "-":
            v *= -1
        ds[k][0] += v
        
        with open("coins.json", "w", encoding="utf-8") as f:
            json.dump(ds, f)
        if ds[k][1]:
            # Tracker
            set_coin_tracker(ds[k], k)
            
            await ctx.send(f"OK. (with tracking) ({ds[k][0]})")
            return
        
        await ctx.send(f"OK. ({ds[k][0]})")

def make_launch_hash():
    digits = [random.choice(string.ascii_letters + string.digits)
            for i in range(16)]
    return "".join(digits)

# ボットのセットアップ
def modify_bot(bot):
    print("Registering commands..")
    launch_hashes = make_launch_hash()
    print(f"launching hash: {launch_hashes}")
    
    @bot.command()
    async def simple_flip(ctx, buyed_price: float, purchase_count: int, selling_price: float, low_limit: Literal["LowLimit", ""] = ""):
        print("Command executed (simple_flip)")
        
        if low_limit == "LowLimit": low_limit = True
        else: low_limit = False
        
        profit, profit_percentage, sellable_days = bz_to_npc_profit_calculator(buyed_price, purchase_count, selling_price, low_limit)
        await ctx.send(f"- Cost: {convert(buyed_price * purchase_count)}\n- Profit: {convert(profit)} ({profit_percentage:.2f}%)\n> days required for sale(NPC): {sellable_days}d")

    @bot.command()
    async def coin(ctx, k:str, s:str, v:str="入力なし"):
        print("command executed (coin)")
        await coin_main(ctx, k, s, v)
    
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
        text += f"{convert(ds[k][0])}```\nMemo: {m}\nisTracking: {ds[k][1]}"
        await ctx.send(text)
    
    @bot.command()
    async def coin_note(ctx, k:str, v:str, *arg):
        print("command executed (coin_note)")
        with open("coins!memo.json", "r", encoding="utf-8") as f:
            ds = json.load(f)
        
        arg = list(arg)
        arg.insert(0, v)
        v = " ".join(arg)
        v = v.strip()
        ds[k] = v
        with open("coins!memo.json", "w", encoding="utf-8") as f:
            json.dump(ds, f)
        
        await ctx.send("OK.")
    
    @bot.command()
    async def tracker(ctx, k:str="", mode:Literal["graph", "list", "help"] = "graph", theme:Literal["dark", "light"] = "dark", extended:Literal["yes", "no"] = "no"):
        print("command executed (tracker)")
        await ctx.send("please wait..")
        if mode == "help":
            text = """
            ## `/tracker`
            引数: `/tracker <key> <mode> <theme> <extended>
            
            #### `<mode>`
            モードを指定する
            graph, list, help が利用可能
            
            #### `<theme>`
            テーマを指定する
            dark, light が利用可能
            これらは graph モードでのみ有効になる
            
            #### `<extended>`
            グラフの詳細を書き込む
            yes, no が利用可能
            これらは graph モードでのみ有効になる
            """
            
            await ctx.send(text)
            return
        
        with open("coin_tracker.json", "r", encoding="utf-8") as f:
            tracker = json.load(f)
        
        # list の場合すぐ終わる
        if mode == "list":
            def text_init(): return f"{k}'s value history (list mode)\n```"
            def space(v, req) -> str:
                v = str(v)
                while not (len(v) == req):
                    v = f"0{v}"
                return v
                
            def special_convert(x:str) -> str:
                first = x[0]
                last = x[-1]
                if not last.lower() in ["k", "m", "t"]:
                    if last.lower() == "n":
                        x = x.replace("coin", "")
                    if not x.isdigit(): x = float(x)
                    x = str(int(x))
                    if first != "-": x = f"+{x}"
                    return x
                else:
                    # 入ってるなら
                    x = x[:-1]
                    if not x.isdigit(): x = float(x)
                    x = str(int(x))
                    if first != "-": x = f"+{x}"
                    return x+last
                
                
            text = text_init()
            track = tracker[k]
            
            v = len(str(len(track))) # len40 -> 40 -> len2
            #print("[tracker]: [v]: ", v, "[len(track)]: ", len(track))
            for i, t in enumerate(track):
                if len(text) >= 1500:
                    await ctx.send(text+"```")
                    text = "```\n"
                text += f"{space(i+1, v)}. {remove_zero_dot(t):,} ({special_convert(convert(t-track[i-1], silent=True))} ({get_up_percentage(track[i-1], t)}))\n" # (2, 1) -> " "  # (4, 1) -> "   "
                time.sleep(0.01)
            await ctx.send(text+"```")
            return
        
        else:
            text = f"{k}'s values history (graph mode)\n"
            track = tracker[k]
            
            # sgc用データを作成
            graph_maker = sgc_data("")
            graph_maker.x = "time"
            graph_maker.y = "value"
            graph_maker.graph = k
            graph_maker.graph_values = track
            graph_maker.extend = extended == "yes"
            graph_image = sgc(graph_maker)
            
            # # Check if the image is correctly created
            # if isinstance(graph_image, Image.Image):
            #     print("Image is a valid PIL Image.")
            # else:
            #     print("Image is not a valid PIL Image.")
                    
            if theme == "dark":
                graph_image = np.invert(graph_image)
                graph_image = Image.fromarray(graph_image)
            
            # メモリに保存し、送信
            with io.BytesIO() as image_binary:
                graph_image.save(image_binary, 'PNG')
                image_binary.seek(0)  # Move the pointer to the beginning of the stream
            
                await ctx.send(text)
                await ctx.send(file=discord.File(fp=image_binary, filename=f'tmp-img.png'))
    
    @bot.command()
    async def terminate(ctx, launch_key:str = ""):
        print("command executed (terminate)")
        await ctx.send("Stopping..")
        
        if launch_key == launch_hashes:
            await ctx.send("Saving cached data..")
            import ctmodule.database 
            with open("db_treas.json", "w", encoding="utf-8") as f:
                json.dump(ctmodule.database.value.treas, f)
                print(ctmodule.database.value.treas)
            
            await ctx.send("Success. exit_code: 200")
            exit(200)
        else:
            await ctx.send("Failed. unknown key")
            
    @bot.command()
    async def launch_hash(ctx):
        print("command executed (launch_hash)")
        print(f">>> launch_hash: {launch_hashes} <<<")
        await ctx.send("printed.")
    
    return bot