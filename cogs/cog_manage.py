# Manage your cogs using commands without needing to restart your bot.

import discord
from discord.ext import commands
import os
import asyncio

class CogManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx): # Restart ALL cogs.
        async with ctx.typing():
            embed = discord.Embed(
                title="Reloading all cogs",
                color=discord.Color.blurple(),
                timestamp=ctx.message.created_at
            )
            for ext in os.listdir("./cogs"):
                if ext.endswith('.py') and not ext.startswith('_'):
                    try:
                        self.bot.unload_extension(f'cogs.{ext[:-3]}')
                        self.bot.load_extension(f'cogs.{ext[:-3]}')
                        embed.add_field(
                            name=f'Reloaded `{ext}`',
                            value='\uFEFF'
                        )
                    except Exception as e:
                        embed.add_field(
                            name=f'Failed to reload `{ext}`',
                            value=e
                        )
                        await ctx.send(embed=embed)
                        raise e

                    await asyncio.sleep(0.5)
            await ctx.send(embed=embed)

    @commands.command(aliases=['cog'], name="reloadcog")
    @commands.is_owner()
    async def reloadcog(self, ctx, *, cogname): # Restart a single cog file.
        async with ctx.typing():
            embed = discord.Embed(
                title=f"Reloading {cogname}",
                color=discord.Color.blurple(),
                timestamp=ctx.message.created_at
            )
            try:
                self.bot.unload_extension(f'cogs.{cogname}')
                self.bot.load_extension(f'cogs.{cogname}')
                embed.add_field(
                    name=f'Reloaded `{cogname}.py`',
                    value='\uFEFF'
                )
            except Exception as e:
                embed.add_field(
                    name=f'Failed to reload `{cogname}.py`',
                    value=e
                )
                await ctx.send(embed=embed)
                raise e
            await asyncio.sleep(0.5)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def stop(self, ctx, *, cogname): # Unload/Stop a single cog file.
        async with ctx.typing():
            embed = discord.Embed(
                title=f"Stopping {cogname}",
                color=discord.Color.blurple(),
                timestamp=ctx.message.created_at
            )
            try:
                self.bot.unload_extension(f'cogs.{cogname}')
                embed.add_field(
                    name=f'Stopped `{cogname}.py`',
                    value='\uFEFF'
                )
            except Exception as e:
                embed.add_field(
                    name=f'Failed to stop `{cogname}.py`',
                    value=e
                )
                await ctx.send(embed=embed)
                raise e
            await asyncio.sleep(0.5)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, cogname): # Load/Start a single cog file.
        async with ctx.typing():
            embed = discord.Embed(
                title=f"Starting {cogname}",
                color=discord.Color.blurple(),
                timestamp=ctx.message.created_at
            )
            try:
                self.bot.load_extension(f'cogs.{cogname}')
                embed.add_field(
                    name=f'Started `{cogname}.py`',
                    value='\uFEFF'
                )
            except Exception as e:
                embed.add_field(
                    name=f'Failed to start `{cogname}.py`',
                    value=e
                )
                await ctx.send(embed=embed)
                raise e
            await asyncio.sleep(0.5)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CogManagement(bot))
