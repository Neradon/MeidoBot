import discord
import re
from discord.ext import commands

class no_erp:
    def __init__(self, client):
        self.client = client

    async def on_message(self, message):
        if message.author == self.client.user:
            return
        text = message.content
        text = re.sub(r'[^\w\s]','', text).split()
        if "no" in text and "erp" in text:
            return
        elif "erp" in text or "lewd" in text:
            await message.channel.send("NO ERP")

def setup(client):
    client.add_cog(no_erp(client))
