import discord
from discord.ext import commands

class block_tenor(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        text = message.content.lower()
        if "https://tenor.com" in text:
            await message.delete()

def setup(client):
    client.add_cog(block_tenor(client))
