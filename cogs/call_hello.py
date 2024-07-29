from discord.ext import commands
import discord
import os

WELCOME = os.getenv('WELCOME_CHANNEL')


class CallHello(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command(name="simulate_join")
    async def simulate_join(self, ctx, member: discord.Member):
        print('hello')
        hello_cog = self.bot.get_cog('Hello')
        if hello_cog:
            # Directly call the on_member_join function
            await hello_cog.on_member_join(member)
        else:
            await ctx.respond("Command not loaded. Please contact a staff member.")

def setup(bot):
    bot.add_cog(CallHello(bot))
