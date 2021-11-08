import discord
from discord.ext import commands
import os
from server import server

execute = commands.Bot(command_prefix="exe!",help_command=None)

@execute.event
async def on_ready():
  print('---------------------------')
  print(f'Logged in as : {execute.user}')
  print(f'Bot ID : {execute.user.id}')
  print(f'Bot in : {len (execute.guilds)} servers')
  print('---------------------------')
  await execute.change_presence(status=discord.Status.dnd,activity=discord.Activity(type=discord.ActivityType.watching, name="exe!help for help!"))

execute.load_extension("Scripts.src.Run")
execute.load_extension("Scripts.src.Rtfm")
execute.load_extension("Scripts.src.Config")
execute.load_extension("Scripts.src.Moderation")

@execute.event
async def on_message(message):
  mention = f"<@!{execute.user.id}>"
  if message.content == mention:
    e = discord.Embed(title=f"Hello! my name is {execute.user}! you can use `exe!help` for my help command!",colour=discord.Color.blue())
    await message.channel.send(embed=e)
  await execute.process_commands(message)

@execute.event
async def on_guild_join(guild):
  e = discord.Embed(title="Thanks for inviting me! <a:confeti:906405377745223690>")
  e.add_field(name="For help you can ping me, or you can use exe!help for my help command! for my docs use exe!docs and i will give you the link to my docs!",value="If you need further help use exe!support")
  e.set_footer(text="TM® & COPYRIGHT © 2021 By NotAlexy_Kyu#4003")
  await guild.system_channel.send(embed=e)

@execute.command(name="help",description="Executor help command.")
async def help(ctx):
  e = discord.Embed(title="Executor Help List",colour=discord.Color.blue())
  for command in execute.walk_commands():
    description = command.description
    if not description or description is None or description == "":
      description = "No description"
    e.add_field(name=f"`exe!{command.name}{command.signature if command.signature is not None else ''}`",value=description,inline=False)
  await ctx.send(embed=e)

execute.sniped_messages = {}
  
@execute.event
async def on_message_delete(message):
  execute.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)
    
@execute.command(description="Get down sniper!")
async def snipe(ctx):
  try:
    contents, author, channel_name, time = execute.sniped_messages[ctx.guild.id]
        
  except:
    await ctx.channel.send("There was an error while trying to snipe the message.")
    return
  embed = discord.Embed(description=contents,
                        color=ctx.author.color,
                        timestamp=time)
  embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
  embed.set_footer(text=f"Last deleted message in #{channel_name}")
    
  await ctx.send(embed=embed)

@execute.command(description="Invite me!")
async def invite(ctx):
  e = discord.Embed(title="<:Invite:907202961019658260> Invite me!",description="You can invite me using [this link](https://discord.com/api/oauth2/authorize?client_id=905796323012403210&permissions=8&scope=bot)",colour=discord.Color.blue())
  await ctx.send(embed=e)

@execute.command(description="Link to my source code")
async def source(ctx):
  e = discord.Embed(title="<:github:907202527236341821> My Source Code",description="Find it in [Github](https://github.com/alexyy802/Executor)")
  await ctx.send(embed=e)

token = os.environ['token']
server()
execute.run(token)
