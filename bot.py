import discord
import os
from discord.ext import commands
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
TOKEN = "" # Insert your bot's token here.

@bot.event
async def on_ready():
  for cog in os.listdir(r"cogs"): # Loop through each file in your "cogs" directory.
      if cog.endswith(".py"):
          try:
              cog = f"cogs.{cog.replace('.py', '')}"
              bot.load_extension(cog) # Load the file as an extension.
          except Exception as e:
              print(f"{cog} is failed to load:")
              raise e
  print(f"Logged in as {bot.user}")
    
bot.run(TOKEN)
