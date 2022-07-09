import discord
from discord.ext import commands

import re
import asyncio
import os
from dotenv import load_dotenv

description = "lana del SLAY"

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guild_messages = True

bot = commands.Bot(command_prefix="?", description=description, intents=intents)

load_dotenv()

@bot.event
async def on_ready():
    print("Logged in as {0.user}, time to slay the boots down".format(bot))

@bot.event
async def on_message(message):
    if (message.author.id == bot.user.id):
        return

    match = re.search('(?i)slay', message.content)
        
    if (match != None):
        await message.channel.send("um yes queen skinny legend versace boots the house down slay queen hunty mama and oop daddy work charli xcx snatch my wig", tts=True)
        if (message.author.voice):
            if (message.author.voice.channel):
                memberChannel = message.author.voice.channel
                vc = await memberChannel.connect()
                vc.play(discord.FFmpegPCMAudio("slay.mp3"))
                await asyncio.sleep(5)
                await vc.disconnect()

bot.run(os.environ['TOKEN'])