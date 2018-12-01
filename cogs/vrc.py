import discord
import random
from discord.ext import commands

class vrc:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def husbando(self, ctx):

        await ctx.send(random.choice(ctx.guild.members).mention +" is curently the best husbando")

    async def version(self, ctx):
        await ctx.send("current version: super hyper pre alpha")
def setup(client):
    client.add_cog(vrc(client))
