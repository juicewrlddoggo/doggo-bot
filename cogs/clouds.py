import nextcord
from nextcord.ext import commands

class clouds(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def clouds(message: nextcord.Message):
            await message.send("pet")


def setup(client):
    client.add_cog(clouds(client))