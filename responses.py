import random
from discord import Intents, Client, Message, Embed
TRUCKING_FACTS = [
    
]

def get_response(user_input: str) -> Embed:
    lowered: str = user_input.lower()
    response_embed = Embed(title=lowered)

    if 'stock' in user_input:
        response_embed = get_stock_data()
        return response_embed

    return response_embed


def get_stock_data() -> Embed:
    
    return Embed(title="STOCK DATA!!!!!")
   



