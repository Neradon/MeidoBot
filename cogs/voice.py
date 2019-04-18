import discord
import re
from discord.ext import commands

class voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def on_message(self, message):
        print(str(message.author)+" - "+str(message.channel.id))


def setup(client):
    client.add_cog(voice(client))
