import random
from discord import Intents, Client, Message, Embed
from re import findall as findall
import os
from dotenv import load_dotenv
from typing import Final
import requests
from datetime import date

#Load Stock Data API key
load_dotenv()
TOKEN: Final[str] = os.getenv('STOCK_DATA_API_KEY')

#URL for stock data
URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={TOKEN}'

def get_response(user_input: str) -> Embed:
    lowered: str = user_input.lower()
    
    if 'stock' in lowered:
        stock_input = findall(r'\w+', lowered[6:])
        response_embed = get_stock_data(stock_input)
        return response_embed

    return


def get_stock_data(user_input: str) -> Embed:
    r = requests.get(URL)
    data = r.json()
    today = date.today()
    date_as_str = today.strftime(r"%Y-%m-%d")
    print(date_as_str)
    return Embed(title="STOCK DATA!!!!!")
   



