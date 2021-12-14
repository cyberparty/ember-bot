import discord
import re
from util.ember_bot import EmberBot
from glob import glob

client = discord.AutoShardedClient()
bot = EmberBot()

print("Ember Bot")

#load cogs
for file in glob("./cogs/*.py"):
    cog = 'cogs.' + re.split('[\\/]',file)[-1][:-3]
    bot.load_extension(cog)

