from pistonapi import PistonAPI
import discord
from discord.ext import commands
import asyncio

piston = PistonAPI()

loading = "<a:loading:905792871314128906>"

class CodeCompiler(commands.Cog):
  def __innit__(self,execute):
    self.executor = execute

  @commands.command()
  async def run(self,ctx,n,* ,code):
    nm = n.lower()
    a = code.replace("```","")

    if nm == "bh":
      await ctx.message.add_reaction(loading)
      await asyncio.sleep(0.5)
      await ctx.message.clear_reactions()
      b = (piston.execute(language="bash",version="5.1.0",code=a))
      c = str(b)
      em = discord.Embed(title="Bash Code Run",description=f"```bash\n{c}```",colour=discord.Color.blue())
      await ctx.reply(embed=em)
      return
    if nm == "jav":
      await ctx.message.add_reaction(loading)
      await asyncio.sleep(0.5)
      await ctx.message.clear_reactions()
      b = (piston.execute(language="java",version="15.0.2",code=a))
      c = str(b)
      em = discord.Embed(title="Java Code Run",description=f"```java\n{c}```",colour=discord.Color.blue())
      await ctx.reply(embed=em)
      return
    elif nm == "py":
      await ctx.message.add_reaction(loading)
      await asyncio.sleep(0.5)
      await ctx.message.clear_reactions()
      b = (piston.execute(language="python",version="3.10.0",code=a))
      c = str(b)
      em = discord.Embed(title="Python Code Run",description=f"```py\n{c}```",colour=discord.Color.blue())
      await ctx.reply(embed=em)
      return
    elif nm == "ts":
      await ctx.message.add_reaction(loading)
      await asyncio.sleep(0.5)
      await ctx.message.clear_reactions()
      b = (piston.execute(language="typescript",version="4.2.3",code=a))
      c = str(b)
      em = discord.Embed(title="Typescript Code Run",description=f"```ts\n{c}```",colour=discord.Color.blue())
      await ctx.reply(embed=em)
      return
    elif nm == "php":
      await ctx.message.add_reaction(loading)
      await asyncio.sleep(0.5)
      await ctx.message.clear_reactions()
      b = (piston.execute(language="php",version="8.0.2",code=a))
      c = str(b)
      em = discord.Embed(title="Php Code Run",description=f"```php\n{c}```",colour=discord.Color.blue())
      await ctx.reply(embed=em)
      return
    elif nm == "rst":
      await ctx.message.add_reaction(loading)
      await asyncio.sleep(0.5)
      await ctx.message.clear_reactions()
      b = (piston.execute(language="rust",version="3.0.1",code=a))
      c = str(b)
      em = discord.Embed(title="Rust Code Run",description=f"```rust\n{c}```",colour=discord.Color.blue())
      await ctx.reply(embed=em)
      return
    elif nm == "exs":
      await ctx.message.add_reaction(loading)
      await asyncio.sleep(0.5)
      await ctx.message.clear_reactions()
      b = (piston.execute(language="elixir",version="1.11.3",code=a))
      c = str(b)
      em = discord.Embed(title="Elixir Code Run",description=f"```elixir\n{c}```",colour=discord.Color.blue())
      await ctx.reply(embed=em)
      return
    elif nm == "swift":
      await ctx.message.add_reaction(loading)
      await asyncio.sleep(0.5)
      await ctx.message.clear_reactions()
      b = (piston.execute(language="swift",version="5.3.3",code=a))
      c = str(b)
      em = discord.Embed(title="Swift Code Run",description=f"```swift\n{c}```",colour=discord.Color.blue())
      await ctx.reply(embed=em)
      return
    elif nm == "lua":
      await ctx.message.add_reaction(loading)
      await asyncio.sleep(0.5)
      await ctx.message.clear_reactions()
      b = (piston.execute(language="lua",version="5.4.2",code=a))
      c = str(b)
      em = discord.Embed(title="Lua Code Run",description=f"```lua\n{c}```",colour=discord.Color.blue())
      await ctx.reply(embed=em)
      return
    elif nm == "go":
      await ctx.message.add_reaction(loading)
      await asyncio.sleep(2)
      await ctx.message.clear_reactions()
      b = (piston.execute(language="go",version="1.16.2",code=a))
      c = str(b)
      em = discord.Embed(title="Golang Code Run",description=f"```go\n{c}```",colour=discord.Color.blue())
      await ctx.reply(embed=em)
      return
    elif nm == "erlang":
      await ctx.message.add_reaction(loading)
      await asyncio.sleep(2)
      await ctx.message.clear_reactions()
      b = (piston.execute(language="erlang",version="23.0.0",code=a))
      c = str(b)
      em = discord.Embed(title="Erlang Code Run",description=f"```erlang\n{c}```",colour=discord.Color.blue())
      await ctx.reply(embed=em)
      return
    elif nm == "lol":
      await ctx.message.add_reaction(loading)
      await asyncio.sleep(2)
      await ctx.message.clear_reactions()
      b = (piston.execute(language="lolcode",version="0.11.2",code=a))
      c = str(b)
      em = discord.Embed(title="Lolcode Code Run",description=f"```lolcode\n{c}```",colour=discord.Color.blue())
      await ctx.reply(embed=em)
      return
    else:
      await ctx.reply(f'{ctx.author.mention}, The Programming Language you provided is not supported yet!')
      return
    
  @commands.command(name="run-help")
  async def help_run(self,ctx):
    e = discord.Embed(colour=discord.Color.blue())
    e.add_field(name="Language codes",value="```yaml\nBash = bh\n \nPython = py\n \nJava = jav\n \nPhp = php\n \nrust = rst\n \nTypescript = ts\n \nElixir = exs\n \nSwift = swift\n \nLua = lua\n \nGoLang = go\n \nErlang = erlang\n \nLolcode = lolcode\n```")
    e.add_field(name="IMPORTANT",value="You dont need to specify the language in a code block, all you need to do is to specify the language outside of the code block example : exe!run <language-codes> ```normal code block``` If you run it in a code block with the language inside of the code block it might result into a error")
    e.add_field(name="Examples",value="exe!run py ```print('Hello World!')```")
    e.set_footer(text="More languages coming soon!")
    await ctx.send(embed=e)

def setup(execute):
  execute.add_cog(CodeCompiler(execute))
