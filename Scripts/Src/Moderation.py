import discord, datetime
from discord.ext import commands
from Utils import checks
from pytimeparse.timeparse import timeparse

class Admin(commands.Cog):
    """Commands for managing Discord servers."""
    def __init__(self,bot):
        self.bot = bot

    @checks.can_kick()
    @commands.command()
    async def kick(self, ctx, user : discord.Member,*,reason=None):
        """Kicks a user from the server."""
        if ctx.author == user:
            return await ctx.send("You cannot kick yourself.")
        await user.kick()
        embed = discord.Embed(title=f'User {user.name} has been kicked.', color=0x00ff00)
        embed.add_field(name="Information",value=f"\nUser ID : {user.id}\n \nUsername : {user.name}\n \nReason : {reason}")
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)

    @checks.can_ban()
    @commands.command()
    async def ban(self, ctx, user : discord.Member,*,reason=None):
        """Bans a user from the server."""
        if ctx.author == user:
            return await ctx.send("You cannot ban yourself.")
        await user.ban()
        embed = discord.Embed(title=f'User {user.name} has been banned.', color=0x00ff00)
        embed.add_field(name="Information",value=f"\nUser ID : {user.id}\n \nUsername : {user.name}\n \nReason : {reason}")
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)

    @checks.can_managemsg()
    @commands.command(description="Delete's a specified amount of messages max [100]")
    async def prune(self, ctx, count: int):
        """Deletes a specified amount of messages. (Max 100)"""
        count = max(1, min(count, 100))
        await ctx.message.channel.purge(limit=count, bulk=True)

    @checks.can_managemsg()
    @commands.command(description="Clear's the bot messages max 100 messages")
    async def clean(self, ctx):
        """Cleans the chat of the bot's messages."""
        def is_me(m):
            return m.author == self.bot.user
        await ctx.message.channel.purge(limit=100, check=is_me())

def setup(execute):
  execute.add_cog(Admin(execute))
