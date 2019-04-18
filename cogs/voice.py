import discord
import re
from discord.ext import commands


class voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        safe = True
        if message.channel.id == 460913402458537985:
            safe = False
            if message.author.voice is not None:
                if message.author.voice.channel.id == 459425873234362369:
                    safe = True
        if message.channel.id == 528330541888700418:
            safe = False
            if message.author.voice is not None:
                if message.author.voice.channel.id == 528329844044333058:
                    safe = True
        if safe is False:
            await message.delete()
            await message.author.send("STOP")
        return


def setup(client):
    client.add_cog(voice(client))
