import nextcord
from nextcord.ext import commands
import os
import random

class shiba(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def shiba(message: nextcord.Message):
            folder_path = './shibas'
            images = [file for file in os.listdir(folder_path) if file.endswith(('.webp'))]
            image_file = random.choice(images)
            image_path = os.path.join(folder_path, image_file)
            
            await message.send(file=nextcord.File(image_path))


def setup(client):
  client.add_cog(shiba(client))