import random
from discord import Intents, Client, Message, Embed
from re import findall as findall
import os
from dotenv import load_dotenv
from typing import Final
import requests
from datetime import date, timedelta

#Load Stock Data API key
load_dotenv()
TOKEN: Final[str] = os.getenv('STOCK_DATA_API_KEY')

#URL for stock data
URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={TOKEN}'

def get_response(user_input: str) -> Embed:
    lowered: str = user_input.lower()
    
    if 'stock' in lowered:
        stock_input = findall(r'\w+', lowered[6:])
        embed_data = get_stock_data()
        response_embed = Embed(title=embed_data[0])
        return response_embed

    return


def get_stock_data() -> list:
    r = requests.get(URL)
    data = r.json()
    today = date.today() - timedelta(days = 1)
    date_as_str = today.strftime(r"%Y-%m-%d")
    closing_price = data["Time Series (Daily)"][date_as_str]['4. close']
    return list([closing_price, date_as_str])
   



