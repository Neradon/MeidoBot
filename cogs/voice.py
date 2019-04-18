import discord
import re
from discord.ext import commands


class voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 460913402458537985:
            print(str(message.author.voice.channel))
            if message.author.voice.channel is not None:
                print(str(message.author.voice.channel.id))

        print(str(message.author)+" - "+str(message.channel.id))
        return


def setup(client):
    client.add_cog(voice(client))
