from sqlalchemy.exc import IntegrityError 
import discord
from discord.ext import commands
import sqlalchemy as db
import sqlalchemy.orm as orm
import os
from models import *

#Get current directory of bot
cwd = os.getcwd()
db_path = os.path.join(cwd, 'database.db')

engine = db.create_engine(f'sqlite:///{db_path}')
Session = orm.sessionmaker(bind=engine)
session = Session()


class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = commands.Bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot is online!')

    @discord.slash_command(name='register')
    async def register(self, ctx):
        user = ctx.author
        with orm.Session(engine) as session:
            try:
                await ctx.respond('Creating your own Mock Market Portfolio...', ephemeral=True)
                #Add user to database
                new_account = BankAccount(username=user.name)
                session.add(new_account)
                session.commit()
                await ctx.respond('Account created successfully!', ephemeral=True)
            except IntegrityError as err:
                print('DEBUG: IntegrityError Block entered')
                session.rollback()
                await ctx.edit(content='Account already created! Do /bank to see your balance.')
                print(err)
            except Exception as err:
                print('Exception Block Entered')
                session.rollback()
                await ctx.edit(content="Account creation failed. Please contact a staff member.")
                print(err)
            finally:
                session.close()
                
def setup(bot):
    bot.add_cog(Register(bot))



