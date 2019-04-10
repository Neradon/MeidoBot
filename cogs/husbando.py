import discord
import random
from discord.ext import commands

class vrc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def husbando(self, ctx):
        await ctx.send(random.choice(ctx.guild.members).mention +" is curently the best husbando")

def setup(client):
    client.add_cog(vrc(client))
