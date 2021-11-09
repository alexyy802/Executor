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

import discord
from discord.ext import commands
import json

def read_json(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data


def write_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

class Settings(commands.Cog):
    def __init__(self, execute):
        self.execute = execute

    @commands.command(name="disable-mod",description="Disable automod in ur server.")
    @commands.has_permissions(administrator=True)
    async def disable_mod(self,ctx):
      guild = ctx.guild
      data = read_json("db/config/automod.json")
      automod = data["servers"]
      if guild.id not in automod:
        await ctx.send('You did not enable automod yet! <a:nono:900278651906572288>')
        return
      guild = ctx.guild
      data = read_json("db/config/automod.json")
      data["servers"].remove(guild.id)
      write_json(data, "db/config/automod.json")
      await ctx.send('Automod disabled! <a:checkmark:900276103942377472>')
    
    @commands.command(name="enable-mod",description="Enable automod in ur server.")
    @commands.has_permissions(administrator=True)
    async def enable_mod(self,ctx):
      guild = ctx.guild
      data = read_json("db/config/automod.json")
      automod = data["servers"]
      if guild.id in automod:
        await ctx.send('Automod has already been enabled in this server! <a:nono:900278651906572288>')
        return

      data = read_json("db/config/automod.json")
      data["servers"].append(guild.id)
      write_json(data, "db/config/automod.json")
      await ctx.send('Automod enabled! <a:checkmark:900276103942377472>')

    @commands.command(name="enable-autolink",description="Enable anti link in ur server.")
    async def enable_link(self,ctx):
      guild = ctx.guild
      data = read_json("db/config/antilinks.json")
      antilink = data["servers"]
      if guild.id in antilink:
        await ctx.send('Anti Link has already been enabled in this server! <a:nono:900278651906572288>')
        return
      
      data = read_json("db/config/antilinks.json")
      data["servers"].append(guild.id)
      write_json(data, "db/config/antilinks.json")
      await ctx.send('Anti link enabled! <a:checkmark:900276103942377472>')
      return

    @commands.command(name="disable-autolink",description="Disable autolink in ur server.")
    async def disable_link(self,ctx):
      guild = ctx.guild
      data = read_json("db/config/antilinks.json")
      antilink = data["servers"]
      if guild.id not in antilink:
        await ctx.send('Anti Link is not active in this server! <a:nono:900278651906572288>')
        return
      
      data = read_json("db/config/antilinks.json")
      data["servers"].remove(guild.id)
      write_json(data, "db/config/antilinks.json")
      await ctx.send('Anti link disabled! <a:checkmark:900276103942377472>')
      return


def setup(execute):
  execute.add_cog(Settings(execute))
