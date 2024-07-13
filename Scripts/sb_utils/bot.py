import discord
from discord.ext import commands

import os, importlib, sys

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

print("BOT_TOKEN: ", BOT_TOKEN)
discord_bot.run(BOT_TOKEN)