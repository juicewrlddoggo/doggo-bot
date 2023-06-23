import nextcord
from nextcord.ext import commands
from nextcord import FFmpegPCMAudio
import json
import os

class jplay(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def jplay(message: nextcord.Message, *, search_term):
            with open('data.json') as f:
                data = json.load(f)

            if search_term in data:
                audio_file = data[search_term]

                if os.path.exists(f'unreleased/{audio_file}'):

                    voice_channel = message.author.voice.channel
                    voice_client = await voice_channel.connect()

                    await voice_client.play(source=f'unreleased/{audio_file}')

                    await voice_client.disconnect()
                else:
                    await ctx.send("audio file not found.")
            else:
                await ctx.send("search not found")

def setup(client):
    client.add_cog(jplay(client))