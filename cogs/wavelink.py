import nextcord
from nextcord.ext import commands
import wavelink

class wavelink(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def join(message: nextcord.Message):
            channel = message.author.voice.channel
            await channel.connect()
            await messsage.send(f'connected to {channel.name}')

        @client.command()
        async def leave(guild: nextcord.Guild, message: nextcord.Message):
            voice_client = guild.voice_client
            if voice_client:
                await voice_client.disconnect()
                await message.channel.send(f'disconnected')
            else:
                await message.channel.send('not connected to a voice channel')
        
        @client.command()
        async def vlock(message: nextcord.Message):
            await message.author.voice.channel.edit()


def setup(client):
    client.add_cog(wavelink(client))