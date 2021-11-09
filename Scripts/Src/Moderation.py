"""
3303 License

Copyright (c) [copyright-year] [full-name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. YOU ARE NOT ALLOWED TO USE ANY PATENTS OR ANY FORM OF COPYRIGHT FROM
THIS PROJECT AN EXCEPTION IS **NOT** MADE FOR CUSTOM SYSTEMS 
MADE FOR THIS PROJECT.
"""

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
