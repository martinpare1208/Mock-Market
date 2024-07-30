from discord.ext import commands
import os
from dotenv import load_dotenv
from typing import Final
import discord
import asyncio
from create_db import create_db as create_database

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
APP_ID = int(os.getenv('APP_ID'))
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(
    command_prefix='!', intents=intents, application_id=APP_ID
)

cwd = os.getcwd()
db_path = os.path.join(cwd, 'database.db')

@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')
    
async def load():
    for filename in os.listdir('./cogs'):
        # if filename.endswith('.py'):
        #     bot.load_extension(f'cogs.{filename[:-3]}')
        try:
            if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Cogfile: {filename} loaded!')
        except Exception as err:
            print(f"Cog file {filename} could not be run! Going to the next cog file.")
            print(err)
            pass


async def db_file():
    if os.path.isfile(db_path):
        print('Database already created. Will not proceed with creation of DB.')
    else:
        print('DB not found. Executing DB Script.')
        await create_database()
        print('DB Successfully created!')

async def main():
    async with bot:
        await load()
        await db_file()
        await bot.start(TOKEN)

asyncio.run(main())
