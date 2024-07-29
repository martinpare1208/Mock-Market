from discord.ext import commands
import discord
import os

WELCOME = os.getenv('WELCOME_CHANNEL')


class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = discord.utils.get(member.guild.text_channels, name='general')  # Adjust channel name as needed
        if channel:
            try:
                await channel.send(f"Welcome to the server, {member.mention}!")
                print(f"Sent welcome message to {member.name}")
            except Exception as e:
                print(f"Failed to send welcome message: {e}")



def setup(bot):
    bot.add_cog(Hello(bot))