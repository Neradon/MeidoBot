import discord
import re
from discord.ext import commands
import requests

class voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        safe = True
        report = "STOP"
        try:
            r = requests.post("http://neradonien.goip.de:5000/erp", data={'message':message.clean_content,'author':message.author.name,'time':message.created_at})
        except Exception as e:
            print(e)

        if message.channel.id == 460913402458537985:
            safe = False
            report = "https://i.imgur.com/eN4ea9f.gif"
            if message.author.voice is not None:
                if message.author.voice.channel.id == 459425873234362369:
                    safe = True
        if message.channel.id == 528330541888700418:
            safe = False
            report = "https://i.imgur.com/hvoixCS.gif"
            if message.author.voice is not None:
                if message.author.voice.channel.id == 528329844044333058:
                    safe = True
        if safe is False:
            await message.delete()
            await message.author.send(str(report))
        return


def setup(client):
    client.add_cog(voice(client))
