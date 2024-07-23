from typing import Final
import os
from discord import Intents, Client, Message, Embed
from dotenv import load_dotenv
from responses import get_response


#Load discord bot token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#Setup bot
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


#Message functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled)')
        return
    
    #Send a dm
    is_private = user_message[0] == '?'
    #Send in current channel
    is_general = user_message[0] == '!'
    
    
    #Determine to use dm
    if is_private:
        user_message = user_message[1:]
    #Determine to use general chat
    elif is_general:
        user_message = user_message[1:]
    try:
        #Create a response based on user message
        response: Embed = get_response(user_message)
        #Send private message
        if is_private:
            await message.author.send(embed=response)
        else:
            #Send to general channel
            await message.channel.send(embed=response)
    except Exception as e:
        print(e)


# Startup for bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# Handle incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel} {username}: "{user_message}"]')
    await send_message(message, user_message)


# main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
