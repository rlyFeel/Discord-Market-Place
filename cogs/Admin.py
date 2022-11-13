import nextcord
from nextcord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Cogs is loaded - Admin')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=100):
        await ctx.channel.purge(amount=amount+1)
        emb = nextcord.Embed(title='Очистка чата!',description=f'Было удаленно{amount} сообщения')
        await ctx.channel.send(embed=emb)



async def setup(bot):
    bot.add_cog(Admin(bot))
