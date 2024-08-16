import discord
from discord.ext import commands
from aiohttp import web

import os, importlib, json
import aiohttp, asyncio

BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN_FOR_LUNAPY")

intents = discord.Intents.default()
intents.messages = True  # For handling messages
intents.message_content = True  # Specifically for accessing message content
discord_bot = commands.Bot(command_prefix="/", intents=intents)

@discord_bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occurred: {str(error)}")

bot_dirs = os.listdir()
root_dir = os.getcwd()

extend_files = []
# Walk through the directory
for dirpath, dirnames, filenames in os.walk(root_dir):
  # Check each file to see if it's 'extend.py'
  for filename in filenames:
    if filename == 'bots.py':
      # Get the relative path of the file from the root directory
      relative_path = os.path.relpath(os.path.join(dirpath, filename), root_dir)
      extend_files.append(relative_path)

for path in extend_files:
  module = importlib.import_module(os.path.splitext(path)[0].replace("\\", "."))
  mods = module.__dict__
  
  if "modify_bot" in mods.keys():
    func = mods["modify_bot"]
  
    discord_bot = func(discord_bot)

# Makefiles
fns = [
  "coin_tracker", "coins!memo", "coins"
]
for fn in fns:
  if not os.path.exists(f"{fn}.json"):
    with open(f"{fn}.json", "w", encoding="utf-8") as f:
      json.dump({}, f)


print("[BOT_TOKEN]: ", BOT_TOKEN)


async def start_discord_bot():
  await discord_bot.start(BOT_TOKEN)


# Webserver
bot_dirs = os.listdir()
extend_files = []
webserver_functions = []
for dirpath, dirnames, filenames in os.walk(root_dir):
  for filename in filenames:
    if filename == "server.py":
      relative_path = os.path.relpath(os.path.join(dirpath, filename), root_dir)
      extend_files.append(relative_path)

for path in extend_files:
  module = importlib.import_module(os.path.splitext(path)[0].replace("\\", "."))
  mods = module.__dict__
  if "server_func" in mods.keys() and "server_path" in mods.keys():
    func = mods["server_func"]
    #path:str = mods["server_path"]()
    
    webserver_functions.append(func)

async def start_webserver():
  app = web.Application()
  for x in webserver_functions:
    x(app)

  runner = web.AppRunner(app)
  await runner.setup()
  site = web.TCPSite(runner, 'localhost', 9876)
  await site.start()
  print("Webserver started on http://localhost:9876")

  # サーバーが永遠に動き続けるように待機します
  while True:
      await asyncio.sleep(360000)  # 長時間待機


async def main():
  await asyncio.gather(
    start_discord_bot(),
    start_webserver()
  )
  
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
