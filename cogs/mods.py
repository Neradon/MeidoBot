import discord
from discord.ext import commands

class no_erp:
    def __init__(self, client):
        self.client = client
    x=1
    async def on_message(self, ctx):
        if ctx.author == self.client.user:
            return
        messagecontent = ctx.content.lower()
        if messagecontent == "no erp":
            return
        elif "<@!222255802000343040>" in messagecontent or "<@!212975202651471873>" in messagecontent:
            if x==1:
                await ctx.channel.send("please dont ping the mods for non urgent matters, thank you :)")
                print (x)
                if x>5:
                    x=0
                    print (x)
                x=x+1

def setup(client):
	client.add_cog(no_erp(client))
