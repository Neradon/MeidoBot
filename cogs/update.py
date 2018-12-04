import discord
import random
from discord.ext import commands

class Update:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def update(self, ctx):
        await ctx.send("Updating bot and restarting...")
        await self.client.close()


    async def version(self, ctx):
        await ctx.send("current version: super hyper pre alpha")

def setup(client):
    client.add_cog(Update(client))
