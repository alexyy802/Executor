import discord
from discord.ext import commands

exec = commands.Bot(command_prefix="exe!",help_command=False)

@exec.event()
async def on_ready():
  print('Bot is ready to complie code!')
  
@exec.command()
async def ping(ctx):
  await ctx.send('Ping pong!')
  

exec.run("discord-bot-token")
