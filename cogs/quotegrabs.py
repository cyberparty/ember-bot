from typing import ContextManager
import discord
from discord import mentions
from discord.ext import commands
from util.ember_bot import EmberBot
from uuid import uuid4

class QuoteGrabs(commands.Cog):

    def __init__(self, bot:EmberBot):
        self.bot = bot

    @commands.command()
    async def grab(self, ctx) -> bool:
        if ctx.message.author == ctx.message.mentions[0]:
            ctx.send("You cannot grab your own message.")
            return False
        else:
            async for msg in ctx.channel.history():
                if msg.author == ctx.message.mentions[0]:
                    await self.bot.database.run_sql("INSERT INTO quotes(quote_id, quote_text, user_id, grabber_id, time_grabbed) VALUES (?, ?, ?, ?, datetime('now'))", 
                    (str(uuid4()), 
                    msg.content, 
                    msg.author.id, 
                    ctx.author.id))

                    ctx.send("Grabbed message.")
                    return True
            await ctx.send("User has not send a recent message.")
            return False
    
    async def quote(self, ctx) -> bool:
        if ctx.message.author == ctx.message.mentions[0]:
            ctx.send("You cannot grab your own message.")
            return False
        else:
            quote_res = await self.bot.database.run_sql("SELECT * FROM quotes WHERE user_id=? ORDER BY time_grabbed ASC LIMIT 1", (ctx.message.mentions[0],))
            if quote_res is None:
                ctx.send("User has no quotes.")
                return False
            else:
                ctx.send(quote_res[1])


    

def setup(bot:EmberBot):
    bot.add_cog(QuoteGrabs(bot))
