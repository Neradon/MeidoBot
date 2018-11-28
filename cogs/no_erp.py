import discord
from discord.ext import commands

class no_erp:
	def __init__(self, client):
		self.client = client

	async def on_message(self, ctx):
		if ctx.author == self.client.user:
			return
		messagecontent = ctx.content.lower()
		if messagecontent == "no erp":
			return
		elif "erp" in messagecontent or "lewd" in messagecontent:
			await ctx.channel.send("NO ERP")

def setup(client):
	client.add_cog(no_erp(client))
