import discord
from discord.ext import commands
from sqlalchemy.exc import IntegrityError
import sqlalchemy as db
import sqlalchemy.orm as orm
import os
from models import *


cwd = os.getcwd()

engine = db.create_engine(f'sqlite:///{db_path}')
Session = orm.sessionmaker(bind=engine)
session = Session()

class GetBalance(commands.Cog):
    def __init__(self, bot):
        self.bot = commands.Bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot is online!')
    @discord.slash_command(name='bal')
    async def get_bal(self, ctx):
        user = ctx.author
        stmt = db.select(BankAccount)
        row = session.execute(stmt).first()
        print(row)
        await ctx.respond('hello')
        
def setup(bot):
    bot.add_cog(GetBalance(bot))