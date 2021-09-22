import discord
from discord.ext import commands

# Let's pretend this is a utility commands cog.

class Util(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command() # In cogs, we use @commands.command() and not @bot.command().
  async def ping(self, ctx): # You must not forget to pass "self" as the first parameter for functions inside classes.
    await ctx.send(f"Pong! Running on {round(self.bot.latency*1000)}ms") # We don't use "bot.something", we use "self.bot.something" in cogs.
    
def setup(bot):
  bot.add_cog(Util(bot))
