### ALL DISCONTINUED FUNCTIONS
from typing import *
import json
import os

#@bot.command()
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
        

#@bot.command()
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

#@bot.command()
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