#DiscordbotRM35

import os
import discord
from dotenv import load_dotenv
from quote import get_quote,get_random_name

##############################

load_dotenv("TOKEN.env")
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()

##############################

@client.event
async def on_ready():
    print('Connection with Discord started.')
    
@client.event
async def on_message(message):
	if message.content.startswith("!quote"):
		msg = message.content
		x = msg.split()
		if len(x)>1:
			name = str(msg.split()[1])
		else:
			name = get_random_name()
		quote = get_quote(name)
		await message.channel.send(quote)
	#if message.content.startswith("!quoteadd"):
	
client.run(TOKEN)

##############################