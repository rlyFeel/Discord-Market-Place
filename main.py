import nextcord
import os
from cfg.cfg import Ds_token
from nextcord.ext.commands import Bot

activity = nextcord.Streaming(name='With 💙 for you ', url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
intents = nextcord.Intents.all()
bot = Bot(command_prefix="/", intents=intents, activity=activity, status=nextcord.Status.do_not_disturb)
bot.remove_command("help")

@bot.event
async def on_ready():
    async def load_cogg(name):
        bot.load_extension(f"cogs.{name}")

    async def reload_cogg(name):
        bot.unload_extension(f"cogs.{name}")
        bot.load_extension(f"cogs.{name}")

    print('------')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await load_cogg(filename[:-3])
            except Exception as ex:
                print(f"{filename[:-3]} crashed. I'm automaticly fixing it")
                await reload_cogg(filename[:-3])

bot.run(Ds_token)