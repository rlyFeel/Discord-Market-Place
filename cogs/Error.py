import nextcord
from nextcord.ext import commands

class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Cogs is loaded - Error')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error,commands.MissingPermissions):
            emb = nextcord.Embed(title='📛 Error 📛', description='```Лох вгетай права, ez ez```', color=nextcord.Color.blurple())
            await ctx.send(embed=emb)
        elif isinstance(error,commands.MissingRequiredArgument):
            emb = nextcord.Embed(title='📛 Error 📛', description='```Лох вгетай аргумент, ez ez```', color=nextcord.Color.blurple())
            await ctx.send(embed=emb)
        elif isinstance(error, commands.CommandNotFound):
            emb = nextcord.Embed(title='📛 Error 📛', description='```Лох вгетай мозг, ez ez```', color=nextcord.Color.blurple())
            await ctx.send(embed=emb)




async def setup(bot):
    bot.add_cog(Error(bot))
