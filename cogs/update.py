import discord
import random
from discord.ext import commands
import subprocess
import sys, string, os

class Update:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def update(self, ctx):

        await ctx.send("Updating bot and restarting...")
        SW_MINIMIZE = 6
        info = subprocess.STARTUPINFO()
        info.dwFlags = subprocess.STARTF_USESHOWWINDOW
        info.wShowWindow = SW_MINIMIZE
        subprocess.Popen("Update.bat", startupinfo=info)
        sys.exit(0)

    async def version(self, ctx):
        await ctx.send("current version: super hyper pre alpha")
def setup(client):
    client.add_cog(Update(client))
