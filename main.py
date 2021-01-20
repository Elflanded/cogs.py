import discord
from discord.ext import commands

from os import environ

bot = Bot(
    command_prefix=environ.get("DISCORD_PREFIX"), prefix=environ.get("DISCORD_PREFIX"),
    developer_ids=environ.get("DEVELOPERS"), command_attrs=dict(hidden=True), intents=discord.Intents(
        guilds=True, members=True, messages=True, reactions=True, presences=True
    )
)


for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")



print("I'm ready for usage.")
bot.run(environ.get("DISCORD_TOKEN"))