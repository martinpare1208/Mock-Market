import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot is online!")


    @discord.slash_command(name="ping")
    async def ping(self, ctx):
        await ctx.respond('pong')

def setup(bot):
    bot.add_cog(Ping(bot))