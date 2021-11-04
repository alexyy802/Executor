from pistonapi import PistonAPI
import discord
from discord.ext import commands

piston = PistonAPI()

class CodeCompiler(commands.Cog):
  def __innit__(self,execute):
    self.executor = execute

  @commands.command()
  async def run(self,ctx,n,* ,code):
    nm = n.lower()
    a = code.replace("```","")

    if nm == "bh":
      b = (piston.execute(language="bash",version="5.1.0",code=a))
      c = str(b)
      em = discord.Embed(title="Bash Code Run",description=f"```bash\nOutput:\n{c}```",colour=discord.Color.blue())
      await ctx.send(embed=em)
      return
    if nm == "jav":
      b = (piston.execute(language="java",version="15.0.2",code=a))
      c = str(b)
      em = discord.Embed(title="Java Code Run",description=f"```java\nOutput:\n{c}```",colour=discord.Color.blue())
      await ctx.send(embed=em)
      return
    elif nm == "py":
      b = (piston.execute(language="python",version="3.10.0",code=a))
      c = str(b)
      em = discord.Embed(title="Python Code Run",description=f"```py\nOutput:\n{c}```",colour=discord.Color.blue())
      await ctx.send(embed=em)
      return
    elif nm == "ts":
      b = (piston.execute(language="typescript",version="4.2.3",code=a))
      c = str(b)
      em = discord.Embed(title="Typescript Code Run",description=f"```ts\nOutput:\n{c}```",colour=discord.Color.blue())
      await ctx.send(embed=em)
      return
    elif nm == "php":
      b = (piston.execute(language="php",version="8.0.2",code=a))
      c = str(b)
      em = discord.Embed(title="Php Code Run",description=f"```php\nOutput:\n{c}```",colour=discord.Color.blue())
      await ctx.send(embed=em)
      return
    else:
      await ctx.send(f'{ctx.author.mention}, The Programming Language you provided is not supported yet!')
      return
    
  @commands.command()
  async def help_run(self,ctx):
    e = discord.Embed(colour=discord.Color.blue())
    e.add_field(name="Language codes",value="```yaml\nBash = bh\n \nPython = py\n \nJava = jav\n```")
    e.set_footer(text="More languages coming soon!")
    await ctx.send(embed=e)

def setup(execute):
  execute.add_cog(CodeCompiler(execute))
