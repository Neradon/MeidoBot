import discord
from discord.ext import commands

class block_tenor:
    def __init__(self, client):
        self.client = client

    async def on_message(self, message):
        if message.author == self.client.user:
            return
        text = message.content.lower()
        if "https://tenor.com/view" in text:
            await message.delete()

def setup(client):
    client.add_cog(block_tenor(client))
