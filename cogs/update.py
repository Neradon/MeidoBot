import discord
import json
import random
from discord.ext import commands

class Update:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def update(self, ctx):

        with open('token.json') as talk1:
            data1 = json.load(talk1)
            talk1.close()
        channel = self.client.get_channel(int(data1['discord_twitch_channel']))
        livemessage = await channel.get_message(int(data1['discord_message_id']))
        await livemessage.delete()

        with open('token.json', 'w') as talk1:
            data1['live_noti'] = "1"
            json.dump(data1, talk1)
            talk1.close()

        await ctx.send("Updating bot and restarting...")
        await self.client.close()


    async def version(self, ctx):
        await ctx.send("current version: super hyper pre alpha")

def setup(client):
    client.add_cog(Update(client))
