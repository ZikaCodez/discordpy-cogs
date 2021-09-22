import discord
from discord.ext import commands

# Let's pretend this is a welcome event cog.

class Welcoming(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.Cog.listener() # In cogs, it's @commands.Cog.listener() and not @bot.event.
  async def on_member_join(self, member):
    await member.send("Welcome!")
    
def setup(bot):
  bot.add_cog(Welcoming(bot))
