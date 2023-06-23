import nextcord
from nextcord.ext import tasks, commands

class edgar(commands.Cog):
    def __init__(self, client):
        self.client = client

        @tasks.loop(seconds=10)
        async def check_nickname():
            guild_id = 1114551991440515162
            member_id = 532049677231849474
            guild = client.get_guild(guild_id)
            member = guild.get_member(member_id)
            if member.nick != "ed":
                await member.edit(nick="ed")

        @client.event
        async def on_guild_available(guild):
            if guild.id == 1114551991440515162:
                check_nickname.start()

def setup(client):
    client.add_cog(edgar(client))