# DiscordbotRM35

import os

import discord
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from quote import get_quote, get_random_name
from discord import opus
import asyncio

load_dotenv("TOKEN.env")
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()
opus.load_opus('libopus-0.x64.dll')

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/74.0'}
BBC_NEWS_URL = 'https://www.bbc.co.uk/news'


async def play_sound(sound, voice_s):
    if voice_s is not None:
        channel_id = voice_s.channel
        vc = await channel_id.connect()
        vc.play(discord.FFmpegPCMAudio(sound))
        while vc.is_playing():
            await asyncio.sleep(1)
        vc.stop()
        await vc.disconnect()
    else:
        await message.channel.send('You are not in a voice channel.')


@client.event
async def on_ready():
    print('Connection with Discord started.')


@client.event
async def on_message(message):

    if message.content.startswith("!quote"):
        msg = message.content
        x = msg.split()
        if len(x) > 1:
            name = str(msg.split()[1])
        else:
            name = get_random_name()
        quote = get_quote(name)
        await message.channel.send(quote)

    if message.content.startswith("sound"):
        await play_sound('example.mp3', message.author.voice)

    if message.contet.startswith("bbcnews"):
        page = requests.get(BBC_NEWS_URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        list2 = soup.select(".thumbnail-info-wrapper a", id='title')


client.run(TOKEN)
