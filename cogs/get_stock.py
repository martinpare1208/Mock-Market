from datetime import date, timedelta
from typing import Final
from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
import requests

#Load Stock Data API key
load_dotenv()
TOKEN: Final[str] = os.getenv('STOCK_DATA_API_KEY')



class GetStock(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @discord.slash_command(name="getstock")
    async def get_stock(self, ctx, stock_ticker) -> discord.Embed:
        #URL for stock data
        try:
            if stock_ticker[0] != '':
                stock_ticker = stock_ticker[1:].upper()
            else:
                stock_ticker = stock_ticker.upper()
            URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_ticker}&apikey={TOKEN}'
            r = requests.get(URL)
            data = r.json()
            today = date.today()
            #If monday, sunday go back to friday
            if today.weekday() == 0:
                today = date.today() - timedelta(days = 3)
            elif today.weekday() == 6:
                today = date.today() - timedelta(days = 2)
            else:
                today = date.today() - timedelta(days = 1)

            date_as_str = today.strftime(r"%Y-%m-%d")
            closing_price = data["Time Series (Daily)"][date_as_str]['4. close']
            embed = discord.Embed(title=f"Closing Price of ${stock_ticker} on {date_as_str}", description=f'${round(float(closing_price), 2)}')
            await ctx.respond(embed=embed)
        except Exception as err:
            print('Get Request Failed.')
            ctx.respond('Could not get data from API. Check to see if you have a misspelling in your entry or contact a staff member if problem persists.')
            print(err)
   

def setup(bot):
    bot.add_cog(GetStock(bot))
