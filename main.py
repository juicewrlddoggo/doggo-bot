import nextcord
from nextcord.ext import tasks, commands
import json
import os
import random

with open('config.json') as f:
    data = json.load(f)
    DISCORDTOKEN = data["discordtoken"]
    LASTFMKEY = data["lastfmkey"]
    LASTFMSECRET = data["lastfmsecret"]
    GENIUSTOKEN = data["geniustoken"]
    IMAGESEARCHKEY = data["googlecustomsearchapikey"]


intents = nextcord.Intents.all()
client = commands.Bot(command_prefix = ",", intents = intents)
client.remove_command('help')
client.owner_id = 532049677231849474


@client.event
async def on_ready():
    print('{0.user} is now logged in'.format(client))
    await client.change_presence(status=nextcord.Status.idle, activity=nextcord.Activity(type=nextcord.ActivityType.playing, name=f"with the clouds"))
    for guild in client.guilds:
        print(f'{guild.name} , {guild.id}')

for fn in os.listdir("./cogs"):
    if fn.endswith(".py"):
        client.load_extension(f"cogs.{fn[:-3]}")


client.run(DISCORDTOKEN)